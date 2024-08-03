#!/usr/bin/env python
# -*- coding: utf-8 -*-

from Screens.Screen import Screen
from Screens.MessageBox import MessageBox
from Screens.Console import Console
from Screens.TextOut import TextOut
from Components.ActionMap import NumberActionMap
# from Components.Label import Label
from Components.Sources.StaticText import StaticText
from Components.PluginComponent import plugins
# from Components.PluginList import *
from Plugins.Plugin import PluginDescriptor
# from Tools.Import import my_import
from OpenPanelList import OPEntryComponent, OpenPanelList
from xml.dom import minidom, Node
from enigma import getDesktop
import os
import sys


PY3 = sys.version_info.major >= 3
if PY3:
    from urllib.request import urlopen
    unicode = str
    unichr = chr
    long = int
    PY3 = True
else:
    from urllib2 import urlopen


# from msg import choice

xml_file = '/etc/openpanel.xml'
start_daemon = '/usr/sbin/op-start-daemon'
pythonpath = '/usr/lib/enigma2/python'


class OpenPanel(Screen):

    global HD_Res
    try:
        sz_w = getDesktop(0).size().width()
    except:
        sz_w = 720
    if sz_w == 1280:
        HD_Res = True
    else:
        HD_Res = False

    if HD_Res:

        skin = """
        <screen name="OpenPanel" position="240,100" size="800,540" title="OpenPanel">
            <widget name="list" position="10,20" size="780,520" scrollbarMode="showOnDemand" zPosition="0"/>
        </screen>"""

    else:
        skin = """
        <screen name="OpenPanel" position="160,70" size="400,460" title="OpenPanel">
            <widget name="list" position="5,5" size="390,450" scrollbarMode="showOnDemand" zPosition="0"/>
        </screen>"""

    def __init__(self, session, list=[], keys=None):
        Screen.__init__(self, session)
        self.zapHistory = [None]
        self.pluginlist = plugins.getPlugins([PluginDescriptor.WHERE_PLUGINMENU, PluginDescriptor.WHERE_EXTENSIONSMENU])
        try:
            if os.path.isfile(xml_file) is False:
                print('xml_file not exist')
                # raise StandardError
            self.errorId = 2
            parser = minidom.parse(xml_file)
            self.currentNode = parser.documentElement
            self.errorId = 3
            self.getList(self.makeEntrys(self.currentNode)[0], self.makeEntrys(self.currentNode)[1])
            self["list"] = OpenPanelList(list=self.list, selection=0)
            self["summary_list"] = StaticText()
            self.updateSummary()
            self.errorId = 0

        except Exception as e:  # StandardError:
            print(e)
            self.errorId = 1
            self["list"] = OpenPanelList(None)
        except:
            # print "file %s not found!" % xml_file
            self["list"] = OpenPanelList(None)

        self["actions"] = NumberActionMap(["WizardActions", "InputActions", "ColorActions", "DirectionActions"],
                                            {
                                            "ok": self.go,
                                            "back": self.cancel,
                                            "1": self.keyNumberGlobal,
                                            "2": self.keyNumberGlobal,
                                            "3": self.keyNumberGlobal,
                                            "4": self.keyNumberGlobal,
                                            "5": self.keyNumberGlobal,
                                            "6": self.keyNumberGlobal,
                                            "7": self.keyNumberGlobal,
                                            "8": self.keyNumberGlobal,
                                            "9": self.keyNumberGlobal,
                                            "0": self.keyNumberGlobal,
                                            "red": self.keyRed,
                                            "green": self.keyGreen,
                                            "yellow": self.keyYellow,
                                            "blue": self.keyBlue,
                                            "up": self.up,
                                            "down": self.down
                                            }, -1)
        self["title"] = StaticText()
        self.onExecBegin.append(self.error)
        self.onShown.append(self.updateTitle)

    def updateTitle(self):
        attr = self.currentNode.attributes
        for attrName in attr.keys():
            if attrName == 'name':
                attrNode = attr.get(attrName)
                self.newtitle = attrNode.nodeValue.encode('utf-8')
                self.setTitle(self.newtitle)
                self["title"].setText(self.newtitle)

    def error(self):
        if self.errorId == 0:
            print("[OpenPanel]: GUI OK")
        else:
            errorMsg = [None, _("file not found!"), _("XML parser error!"), _("list error!"), _("url not found!"), _("code error: check your embedded scripts!"), _("Plugin not found! see plugin_names.txt how to call Plugins from openanel.xml")]
            self.session.open(MessageBox, text=errorMsg[self.errorId], type=MessageBox.TYPE_ERROR)
            print("[OpenPanel]", errorMsg[self.errorId])
            self.close(None)

    def execPlugin(self, name):
        self.errorId = 6
        for plugin in self.pluginlist:
            if plugin.name == name:
                self.errorId = 0
                print("[OpenPanel] found plugin :", name)
                plugin(session=self.session)
                break

    def opTextOut(self, text="", title=""):
        self.session.open(TextOut, text=text, title=title)
        print("[OpenPanel] open TextOut: ", title, text)

    def closePluginBrowser(self):
        sh = "sleep 1; ebox exit"
        print("[OpenPanel] closing extern Pluginbrowser: %s '%s &'\n" % (start_daemon, sh))
        command = "%s '%s &'" % (start_daemon, sh)
        os.system(command)

    def noDoubleKeys(self, keylist, key):
        if keylist == []:
            return key
        if key == "":
            return ""
        for x in keylist:
            if x == key:
                return ""
        else:
            return key

    def makeEntrys(self, currentNode):
        name = shortcut = exit = help = target = code = None
        keylist = []
        mnulist = []
        entry_idx = -1
        for node in currentNode.childNodes:
            if node.nodeType == Node.ELEMENT_NODE:
                # Write out the element name.
                if node.nodeName == 'entry' or node.nodeName == 'shell' or node.nodeName == 'usersh' or node.nodeName == 'plugin' or node.nodeName == 'xmlfile' or node.nodeName == 'text':
                    # print 'makeEntrys: found tagentry'
                    attrs = node.attributes
                    for attrName in attrs.keys():
                        if attrName == 'name':
                            attrNode = attrs.get(attrName)
                            name = attrNode.nodeValue.encode('utf-8')

                        elif attrName == 'shortcut':
                            attrNode = attrs.get(attrName)
                            shortcut = attrNode.nodeValue.encode('utf-8')

                        elif attrName == 'exit':
                            attrNode = attrs.get(attrName)
                            exit = attrNode.nodeValue.encode('utf-8')

                        elif attrName == 'help':
                            attrNode = attrs.get(attrName)
                            help = attrNode.nodeValue.encode('utf-8')

                        elif attrName == 'target':
                            attrNode = attrs.get(attrName)
                            target = attrNode.nodeValue.encode('utf-8')

                        elif attrName == 'text':
                            attrNode = attrs.get(attrName)
                            text = attrNode.nodeValue.encode('utf-8')

                if node.nodeName == 'entry':
                    entry_idx += 1
                    mnulist.append((name, "entry", node, help, entry_idx))
                    keylist.append((self.noDoubleKeys(keylist, shortcut)))

                elif node.nodeName == 'usersh':
                    entry_idx += 1
                    mnulist.append((name, "usersh", target, help, exit))
                    keylist.append((self.noDoubleKeys(keylist, shortcut)))

                elif node.nodeName == 'shell':
                    entry_idx += 1
                    for node2 in node.getElementsByTagName("sh"):
                        for node3 in node2.childNodes:
                            if node3.nodeType == Node.TEXT_NODE:
                                sh = node3.data.encode('utf-8')
                                mnulist.append((name, "shell", sh, help, exit))
                                keylist.append((self.noDoubleKeys(keylist, shortcut)))

                elif node.nodeName == 'separator':
                    entry_idx += 1
                    mnulist.append(("--", "--"))
                    keylist.append((""))

                elif node.nodeName == 'text':
                    entry_idx += 1
                    for node2 in node.getElementsByTagName('code'):
                        for node3 in node2.childNodes:
                            if node3.nodeType == Node.TEXT_NODE:
                                code = node3.data.encode('utf-8')
                                mnulist.append((name, "text", target, help, exit, code, text))
                                keylist.append((self.noDoubleKeys(keylist, shortcut)))

                elif node.nodeName == 'plugin':
                    entry_idx += 1
                    for node2 in node.getElementsByTagName('code'):
                        for node3 in node2.childNodes:
                            if node3.nodeType == Node.TEXT_NODE:
                                code = node3.data.encode('utf-8')
                                mnulist.append((name, "plugin", target, help, exit, code))
                                keylist.append((self.noDoubleKeys(keylist, shortcut)))

                elif node.nodeName == 'xmlfile':
                    entry_idx += 1
                    print("[OpenPanel] xmlfile entry: ", node.nodeName)
                    for node2 in node.getElementsByTagName('code'):
                        print("[OpenPanel] node: ", node.nodeName)
                        for node3 in node2.childNodes:
                            if node3.nodeType == Node.TEXT_NODE:
                                code = node3.data.encode('utf-8')
                                print("[OpenPanel] code: ", code)
                                mnulist.append((name, "xmlfile", target, help, node, code, entry_idx))
                                keylist.append((self.noDoubleKeys(keylist, shortcut)))
        # print "[OpenPanel] MENU/KEY LISTS: ",mnulist,keylist
        return mnulist, keylist

    def getList(self, list, keys):
        self.list = []
        self.summarylist = []
        if keys is None:
            self.__keys = [""] * 14 + (len(list) - 10) * [""]
        else:
            self.__keys = keys + (len(list) - len(keys)) * [""]

        self.keymap = {}
        pos = 0
        for x in list:
            strpos = str(self.__keys[pos])
            self.list.append(OPEntryComponent(key=strpos, text=x))
            if self.__keys[pos] != "":
                self.keymap[self.__keys[pos]] = list[pos]
            self.summarylist.append((self.__keys[pos], x[0]))
            pos += 1

    def keyLeft(self):
        pass

    def keyRight(self):
        pass

    def up(self):
        if len(self["list"].list) > 0:
            while 1:
                self["list"].instance.moveSelection(self["list"].instance.moveUp)
                self.updateSummary(self["list"].l.getCurrentSelectionIndex())
                if self["list"].l.getCurrentSelection()[0][0] != "--" or self["list"].l.getCurrentSelectionIndex() == 0:
                    break

    def down(self):
        if len(self["list"].list) > 0:
            while 1:
                self["list"].instance.moveSelection(self["list"].instance.moveDown)
                self.updateSummary(self["list"].l.getCurrentSelectionIndex())
                if self["list"].l.getCurrentSelection()[0][0] != "--" or self["list"].l.getCurrentSelectionIndex() == len(self["list"].list) - 1:
                    break

    # runs a number shortcut
    def keyNumberGlobal(self, number):
        self.goKey(str(number))

    # runs the current selected entry
    def go(self):
        cursel = self["list"].l.getCurrentSelection()
        if cursel:
            self.goEntry(cursel[0])
        else:
            self.cancel()

    # runs a specific entry
    def goEntry(self, entry):
        # print self["list"].l.getCurrentSelectionIndex() #[0][1]

        if entry[1] == "entry":
            self.currentNode = entry[2]
            self.zapHistory.append(entry[4])
            print("[OpenPanel] self.zapHistory: ", self.zapHistory)
            self.getList(self.makeEntrys(self.currentNode)[0], self.makeEntrys(self.currentNode)[1])
            self["list"].l.setList(self.list)
            self["list"].instance.moveSelectionTo(0)
            self["summary_list"] = StaticText()
            self.updateSummary()
            self.updateTitle()

        elif entry[1] == "plugin":
            if entry[5] != "" and entry[5] != "\n" and entry[5] is not None:
                try:
                    exec(entry[5])
                except:
                    self.errorId = 5
                    print("[OpenPanel] plugin entry: code error exec: %s\n" % (entry[5]))
                    # self.error()

            if entry[2] != "":
                self.execPlugin(entry[2])
            if entry[4] == "no":
                pass
            else:
                self.close(None)

        elif entry[1] == "shell":
            command = "%s '%s &'" % (start_daemon, entry[2])
            try:
                debug = os.popen(command)
                print("[OpenPanel] shell entry exec: begin\n")
                for line in debug:
                    print(line)

                print("[OpenPanel] shell entry exec: end\n")
            except:
                self.errorId = 5
                print("[OpenPanel] shell entry: error script exec: %s '%s &'\n" % (start_daemon, entry[2]))
                # self.error()

            if entry[4] == "no":
                pass
            else:
                self.close(None)

        elif entry[1] == "usersh":
            if os.path.isfile(entry[2]):
                self.session.open(Console, _("Executing User shell"), [entry[2]])
                if entry[4] == "no":
                    pass
                else:
                    self.closePluginBrowser()
                    self.close(None)
            else:
                self.session.open(MessageBox, (_("file %s\n not found") % entry[2]), MessageBox.TYPE_ERROR)

        elif entry[1] == "xmlfile":
            print("[OpenPanel] xml entry:", entry)
            tmp_xml = None
            if entry[2][:1] == "/":
                tmp_xml = entry[2]

            elif entry[2][:7] == "file://":
                tmp_xml = entry[2][7:]

            elif entry[2][:4] == "http" or entry[2][:3] == "ftp":
                try:
                    self.errorId = 4
                    print("[OpenPanel] urllib.urlopen(entry[2]) ", entry[2])
                    f = urlopen(entry[2])
                    userxml = f.read()
                    tmp_xml = "/tmp/.openpanel.xml"
                    print("[OpenPanel] file = open ")
                    file = open(tmp_xml, "w")
                    file.write(userxml)
                    file.close()
                    print("[OpenPanel] download done ", entry[2])

                except IOError, e:
                    tmp_xml = None
                    # self.error()
                    print("[OpenPanel] error while loading ", entry[2], e)

                except:
                    tmp_xml = None
                    # self.error()
            else:
                print("[OpenPanel] XML path syntax error!\n")

            if tmp_xml is not None:
                if entry[5] != "" and entry[5] != "\n" and entry[5] is not None:
                    try:
                        exec(entry[5])
                    except:
                        self.errorId = 5
                        print("[OpenPanel] xmlfile entry: code error exec: %s\n" % (entry[5]))
                        # self.error()
                try:
                    if os.path.isfile(tmp_xml) is False:
                        print('xml_file not exist')

                    self.errorId = 2
                    parser = minidom.parse(tmp_xml)
                    tmpChildNode = parser.documentElement
                    self.currentNode.replaceChild(tmpChildNode, entry[4])
                    self.errorId = 3
                    self.getList(self.makeEntrys(self.currentNode)[0], self.makeEntrys(self.currentNode)[1])
                    self["list"].l.setList(self.list)
                    self["summary_list"] = StaticText()
                    self.updateSummary()
                    if os.path.isfile("/tmp/.openpanel.xml") is True:
                        os.remove("/tmp/.openpanel.xml")

                    self.errorId = 0
                    self["list"].instance.moveSelectionTo(entry[6])
                    self.go()

                except Exception as e:
                    print(e)
                    self.errorId = 1
                    # self.error()
                # except:
                    # self.error()

        elif entry[1] == "text":
            if entry[5] != "" and entry[5] != "\n" and entry[5] is not None:
                try:
                    exec(entry[5])
                except:
                    self.errorId = 5
                    print("[OpenPanel] plugin entry: code error exec: %s\n" % (entry[5]))
                    # self.error()

            if entry[6] != "" and entry[6] is not None:
                self.opTextOut(entry[6])

            elif entry[2] != "" and entry[2] is not None:
                file = open(entry[2], 'r')
                text = file.read()
                file.close()
                self.opTextOut(text=text, title=entry[0])

            if entry[4] == "no":
                pass
            else:
                self.close(None)
        else:
            print("[OpenPanel] error: No tag entrys found, exit")
            self.close(None)

    # lookups a key in the keymap, then runs it
    def goKey(self, key):
        if self.keymap.has_key(key):
            entry = self.keymap[key]
            self.goEntry(entry)

    # runs a color shortcut
    def keyRed(self):
        self.goKey("red")

    def keyGreen(self):
        self.goKey("green")

    def keyYellow(self):
        self.goKey("yellow")

    def keyBlue(self):
        self.goKey("blue")

    def updateSummary(self, curpos=0):
        pos = 0
        summarytext = ""
        for entry in self.summarylist:
            # print "[OpenPanel].updateSummary: entry: ",entry
            if pos > curpos-2 and pos < curpos+5:
                if pos == curpos:
                    summarytext += ">"
                else:
                    summarytext += entry[0]
                summarytext += ' ' + entry[1] + '\n'
            pos += 1
        self["summary_list"].setText(summarytext)

    def cancel(self):
        backZap = self.zapHistory.pop(len(self.zapHistory) - 1)
        if backZap > -1:
            self.currentNode = self.currentNode.parentNode
            self.getList(self.makeEntrys(self.currentNode)[0], self.makeEntrys(self.currentNode)[1])
            self["list"].l.setList(self.list)
            self["list"].instance.moveSelectionTo(backZap)
            self["summary_list"] = StaticText()
            self.updateSummary()
            self.updateTitle()
        else:
            print("[OpenPanel] - end")
            self.close(None)
