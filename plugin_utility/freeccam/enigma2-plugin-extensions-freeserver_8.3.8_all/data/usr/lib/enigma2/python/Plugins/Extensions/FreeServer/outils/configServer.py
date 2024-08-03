# -*- coding: UTF-8 -*-
from __future__ import print_function

from enigma import getPrevAsciiCode
from Tools.NumericalTextInput import NumericalTextInput
from Tools.Directories import resolveFilename, SCOPE_CONFIG, fileExists
from Components.Harddisk import harddiskmanager
from copy import copy as copy_copy
from os import path as os_path
from time import localtime, strftime

class ConfigElement(object):

    def __init__(self):
        self.saved_value = None
        self.save_forced = False
        self.last_value = None
        self.save_disabled = False
        self.__notifiers = None
        self.__notifiers_final = None
        self.enabled = True
        self.callNotifiersOnSaveAndCancel = False
        return

    def getNotifiers(self):
        if self.__notifiers is None:
            self.__notifiers = []
        return self.__notifiers

    def setNotifiers(self, val):
        self.__notifiers = val

    notifiers = property(getNotifiers, setNotifiers)

    def getNotifiersFinal(self):
        if self.__notifiers_final is None:
            self.__notifiers_final = []
        return self.__notifiers_final

    def setNotifiersFinal(self, val):
        self.__notifiers_final = val

    notifiers_final = property(getNotifiersFinal, setNotifiersFinal)

    def setValue(self, value):
        self._value = value
        self.changed()

    def getValue(self):
        return self._value

    value = property(getValue, setValue)

    def fromstring(self, value):
        return value

    def load(self):
        sv = self.saved_value
        if sv is None:
            self.value = self.default
        else:
            self.value = self.fromstring(sv)
        return

    def tostring(self, value):
        return str(value)

    def save(self):
        if self.save_disabled or self.value == self.default and not self.save_forced:
            self.saved_value = None
        else:
            self.saved_value = self.tostring(self.value)
        if self.callNotifiersOnSaveAndCancel:
            self.changed()
        return

    def cancel(self):
        self.load()
        if self.callNotifiersOnSaveAndCancel:
            self.changed()

    def isChanged(self):
        sv = self.saved_value
        if sv is None and self.value == self.default:
            return False
        else:
            return self.tostring(self.value) != sv
            return

    def changed(self):
        if self.__notifiers:
            for x in self.notifiers:
                x(self)

    def changedFinal(self):
        if self.__notifiers_final:
            for x in self.notifiers_final:
                x(self)

    def addNotifier(self, notifier, initial_call = True, immediate_feedback = True):
        if immediate_feedback:
            self.notifiers.append(notifier)
        else:
            self.notifiers_final.append(notifier)
        if initial_call:
            notifier(self)

    def disableSave(self):
        self.save_disabled = True

    def __call__(self, selected):
        return self.getMulti(selected)

    def onSelect(self, session):
        pass

    def onDeselect(self, session):
        if not self.last_value == self.value:
            self.changedFinal()
            self.last_value = self.value


KEY_LEFT = 0
KEY_RIGHT = 1
KEY_OK = 2
KEY_DELETE = 3
KEY_BACKSPACE = 4
KEY_HOME = 5
KEY_END = 6
KEY_TOGGLEOW = 7
KEY_ASCII = 8
KEY_TIMEOUT = 9
KEY_NUMBERS = range(12, 22)
KEY_0 = 12
KEY_9 = 21

def getKeyNumber(key):
    return key - KEY_0


class ConfigSequence(ConfigElement):

    def __init__(self, seperator, limits, default, censor_char = '2'):
        ConfigElement.__init__(self)
        self.marked_pos = 0
        self.seperator = seperator
        self.limits = limits
        self.censor_char = censor_char
        self.last_value = self.default = default
        self.value = copy_copy(default)
        self.endNotifier = None
        return

    def validate(self):
        max_pos = 0
        num = 0
        for i in self._value:
            max_pos += len(str(self.limits[num][1]))
            if self._value[num] < self.limits[num][0]:
                self._value[num] = self.limits[num][0]
            if self._value[num] > self.limits[num][1]:
                self._value[num] = self.limits[num][1]
            num += 1

        if self.marked_pos >= max_pos:
            if self.endNotifier:
                for x in self.endNotifier:
                    x(self)

            self.marked_pos = max_pos - 1
        if self.marked_pos < 0:
            self.marked_pos = 0

    def validatePos(self):
        if self.marked_pos < 0:
            self.marked_pos = 0
        total_len = sum([ len(str(x[1])) for x in self.limits ])
        if self.marked_pos >= total_len:
            self.marked_pos = total_len - 1

    def addEndNotifier(self, notifier):
        if self.endNotifier is None:
            self.endNotifier = []
        self.endNotifier.append(notifier)
        return

    def handleKey(self, key):
        if key == KEY_LEFT:
            self.marked_pos -= 1
            self.validatePos()
        elif key == KEY_RIGHT:
            self.marked_pos += 1
            self.validatePos()
        elif key == KEY_HOME:
            self.marked_pos = 0
            self.validatePos()
        elif key == KEY_END:
            max_pos = 0
            num = 0
            for i in self._value:
                max_pos += len(str(self.limits[num][1]))
                num += 1

            self.marked_pos = max_pos - 1
            self.validatePos()
        elif key in KEY_NUMBERS or key == KEY_ASCII:
            if key == KEY_ASCII:
                code = getPrevAsciiCode()
                if code < 48 or code > 57:
                    return
                number = code - 48
            else:
                number = getKeyNumber(key)
            block_len = [ len(str(x[1])) for x in self.limits ]
            total_len = sum(block_len)
            pos = 0
            blocknumber = 0
            block_len_total = [0]
            for x in block_len:
                pos += block_len[blocknumber]
                block_len_total.append(pos)
                if pos - 1 >= self.marked_pos:
                    pass
                else:
                    blocknumber += 1

            number_len = len(str(self.limits[blocknumber][1]))
            posinblock = self.marked_pos - block_len_total[blocknumber]
            oldvalue = self._value[blocknumber]
            olddec = oldvalue % 10 ** (number_len - posinblock) - oldvalue % 10 ** (number_len - posinblock - 1)
            newvalue = oldvalue - olddec + 10 ** (number_len - posinblock - 1) * number
            self._value[blocknumber] = newvalue
            self.marked_pos += 1

    def genText(self):
        value = ''
        mPos = self.marked_pos
        num = 0
        for i in self._value:
            if value:
                value += self.seperator
                if mPos >= len(value) - 1:
                    mPos += 1
            if self.censor_char == '':
                value += ('%0' + str(len(str(self.limits[num][1]))) + 'd') % i
            else:
                value += self.censor_char * len(str(self.limits[num][1]))
            num += 1

        return (value, mPos)

    def getText(self):
        value, mPos = self.genText()
        return value

    def getMulti(self, selected):
        value, mPos = self.genText()
        if self.enabled:
            return ('mtext'[1 - selected:], value, [mPos])
        else:
            return ('text', value)

    def tostring(self, val):
        return self.seperator.join([ self.saveSingle(x) for x in val ])

    def saveSingle(self, v):
        return str(v)

    def fromstring(self, value):
        return [ int(x) for x in value.split(self.seperator) ]

    def onDeselect(self, session):
        if self.last_value != self._value:
            self.changedFinal()
            self.last_value = copy_copy(self._value)


ip_limits = [(0, 23), (0, 59)]

class ConfigIP(ConfigSequence):

    def __init__(self, default, auto_jump = False):
        ConfigSequence.__init__(self, seperator=':', limits=ip_limits, default=default)
        self.block_len = [ len(str(x[1])) for x in self.limits ]
        self.marked_block = 0
        self.overwrite = True
        self.auto_jump = auto_jump

    def handleKey(self, key):
        if key == KEY_LEFT:
            if self.marked_block > 0:
                self.marked_block -= 1
            self.overwrite = True
        elif key == KEY_RIGHT:
            if self.marked_block < len(self.limits) - 1:
                self.marked_block += 1
            self.overwrite = True
        elif key == KEY_HOME:
            self.marked_block = 0
            self.overwrite = True
        elif key == KEY_END:
            self.marked_block = len(self.limits) - 1
            self.overwrite = True
        elif key in KEY_NUMBERS or key == KEY_ASCII:
            if key == KEY_ASCII:
                code = getPrevAsciiCode()
                if code < 48 or code > 57:
                    return
                number = code - 48
            else:
                number = getKeyNumber(key)
            oldvalue = self._value[self.marked_block]
            if self.overwrite:
                self._value[self.marked_block] = number
                self.overwrite = False
            else:
                oldvalue *= 10
                newvalue = oldvalue + number
                if self.auto_jump and newvalue > self.limits[self.marked_block][1] and self.marked_block < len(self.limits) - 1:
                    self.handleKey(KEY_RIGHT)
                    self.handleKey(key)
                    return
                if newvalue < 10:
                    self._value[self.marked_block] = '0' + str(newvalue)
                    self.handleKey(KEY_RIGHT)
                else:
                    self._value[self.marked_block] = newvalue
            if len(str(self._value[self.marked_block])) >= self.block_len[self.marked_block]:
                self.handleKey(KEY_RIGHT)

    def genText(self):
        value = ''
        block_strlen = []
        for i in self._value:
            block_strlen.append(len(str(i)))
            if value:
                value += self.seperator
            value += str(i)

        leftPos = sum(block_strlen[:self.marked_block]) + self.marked_block
        rightPos = sum(block_strlen[:self.marked_block + 1]) + self.marked_block
        mBlock = range(leftPos, rightPos)
        return (value, mBlock)

    def getMulti(self, selected):
        value, mBlock = self.genText()
        if self.enabled:
            return ('mtext'[1 - selected:], value, mBlock)
        else:
            return ('text', value)

    def getHTML(self, id):
        return '.'.join([ '%d' % d for d in self.value ])
