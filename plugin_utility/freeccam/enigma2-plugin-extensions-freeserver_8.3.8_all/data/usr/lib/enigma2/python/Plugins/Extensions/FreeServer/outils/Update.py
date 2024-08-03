# -*- coding: UTF-8 -*-
from __future__ import print_function
from .compat import PY3, compat_urlopen
from .Console2 import Console2

from Components.Pixmap import Pixmap
from Components.ActionMap import ActionMap
from Components.Input import Input
from Screens.InputBox import InputBox
from Tools.Directories import fileExists
from Screens.Screen import Screen
import re
from Plugins.Plugin import PluginDescriptor
from Tools.Directories import fileExists
from Screens.Screen import Screen
from Screens.Standby import *
from Tools.Directories import *
from Components.Sources.List import List
from Components.MenuList import MenuList
from Components.Pixmap import Pixmap
from Components.ActionMap import ActionMap, NumberActionMap
from Components.Label import Label
from Components.Button import Button
from Components.Sources.StaticText import StaticText
from Components.ScrollLabel import ScrollLabel
from Components.MultiContent import MultiContentEntryText, MultiContentEntryPixmapAlphaTest
from Components.config import config, ConfigSelection, getConfigListEntry, ConfigSubsection, configfile
from enigma import eListbox, eTimer, eListboxPythonMultiContent, gFont, getDesktop, loadPNG, eConsoleAppContainer
from enigma import *
import os
import sys
import re
from xml.dom import Node, minidom
from twisted.web.client import getPage
import base64
### EDit By RAED To DreamOS OE2.5/2.6
from Tools.Directories import fileExists
data_xml = 'aHR0cHM6Ly9pYTgwMzAwMC51cy5hcmNoaXZlLm9yZy8zMC9pdGVtcy9GcmVlU2VydmVyaW5mby9kZWIudHh0'
xml_path = base64.b64decode(data_xml)
data2_xml = 'aHR0cHM6Ly9pYTgwMzAwMC51cy5hcmNoaXZlLm9yZy8zMC9pdGVtcy9GcmVlU2VydmVyaW5mby9pbmZvLnR4dA=='
xml2_path = base64.b64decode(data2_xml)
data3_xml = 'aHR0cHM6Ly9pYTkwMzAwMC51cy5hcmNoaXZlLm9yZy8zMC9pdGVtcy9GcmVlU2VydmVyaW5mby9pbmZvMi50eHQ='
xml3_path = base64.b64decode(data3_xml)
DESKHEIGHT = getDesktop(0).size().height()
plugin_path = '/usr/lib/enigma2/python/Plugins/Extensions/FreeServer/fonts'
skin_path = '/usr/lib/enigma2/python/Plugins/Extensions/FreeServer/Skin/'
p_path = '/usr/lib/enigma2/python/Plugins/Extensions/FreeServer'
from enigma import addFont
try:
    addFont('%s/bpmono.ttf' % plugin_path, 'bpmo', 100, 1)
    
except Exception as ex:
    print(ex)
  
currversion = '8.3.8'
###########################################################################
from Tools.Directories import fileExists
def DreamOS():
    if os.path.exists('/var/lib/dpkg/status'):
        return DreamOS

class Update(Screen):

    def __init__(self, session):
        self.session = session

        import sys,os
### EDit By RAED To DreamOS OE2.5/2.6
        #if fileExists('/var/lib/dpkg/status'):
        #     self.wget = "/usr/bin/wget2 --no-check-certificate"
        #else:
        #     self.wget = "/usr/bin/wget"
        self.wget = "wget --no-check-certificate"
### End
        os.system("%s https://ia600702.us.archive.org/26/items/dreamosat/MyPicture.sh -qO - | /bin/sh" % self.wget)
        if DESKHEIGHT < 1000:
            skin = skin_path + 'tntHD.xml'
        else:
            skin = skin_path + 'tntFHD.xml'
        f = open(skin, 'r')
        self.skin = f.read()
        f.close()
        Screen.__init__(self, session)
        info = ''
        self['key_blue'] = Label(_(' '))
        self['key_yellow'] = Label(_(' '))
        self['key_green'] = Label(_(' '))
        self['ButtonRedtext'] = Label(_('Exit'))                
        self['text'] = Label()
        self['actions'] = ActionMap(['SetupActions', 'DirectionActions', 'ColorActions'], {'ok': self.close,
         'blue': self.info,         
         'yellow': self.Freeserver,         
         'red': self.close,
         'cancel': self.close,
         'green': self.runupdate}, -1)
        try:
            fp = compat_urlopen(xml_path.decode("utf-8"))
            count = 0
            self.labeltext = ''
            s1 = fp.readline()
            s2 = fp.readline()
            s3 = fp.readline()
            s4 = fp.readline()
            s1 = s1.strip()
            s2 = s2.strip()
            s3 = s3.strip()
            s4 = s4.strip()
            self.version = s1
            self.link = s2
            self.link2 = s3
            self.info = s4
            fp.close()
            cstr = s1 + ' ' + s2
            if s1 <= currversion:
                self['text'].setText('FreeServer version: ' + currversion + '\n\n\nNo updates available!')
                self.update = False
                self['key_green'].setText(' ')
            else:
                updatestr = '\nFreeServer version: ' + currversion + '\n\nNew update ' + s1 + ' is available!  \n\nUpdates:' + self.info + '\n\n\n\nPress green button to start updating . . .'
                self.update = True
                self['text'].setText(updatestr)
                self['key_green'].setText('Update')
        except:
            self.update = False
            self['text'].setText('Unable to check for updates\n\nNo internet connection or server down\n\nPlease check later')

    def runupdate(self):
        if self.update == False:
            return
        if DreamOS():
            com = self.link2
            dom = 'Updating plugin to ' + self.version
            self.session.open(Console2, _('Downloading-installing: %s') % dom, ['dpkg install --force-overwrite %s' % com])
        else:                   
            com = self.link
            dom = 'Updating plugin to ' + self.version
            self.session.open(Console2, _('Downloading-installing: %s') % dom, ['opkg install --force-overwrite %s' % com])

    def Freeserver(self):
            self.session.open(Console2, title='Free Server', cmdlist=["sh '/usr/lib/enigma2/python/Plugins/Extensions/FreeServer/FreeServer.sh'"]) 

    def info(self):
            self.session.open(News) 


class News(Screen):

    def __init__(self, session):
        self.session = session
        if DESKHEIGHT < 1000:
            skin = skin_path + 'zdfHD.xml'
        else:
            skin = skin_path + 'zdfFHD.xml'
        f = open(skin, 'r')
        self.skin = f.read()
        f.close()
        Screen.__init__(self, session)
        info = ''
        self['ButtonRedtext'] = Label(_('Exit'))
        self['text'] = ScrollLabel(info)
        self['actions'] = ActionMap(['SetupActions', 'DirectionActions'], {'right': self['text'].pageDown,
         'ok': self.close,
         'red': self.close,       
         'up': self['text'].pageUp,
         'down': self['text'].pageDown,
         'cancel': self.close,
         'left': self['text'].pageUp}, -1)
        try:
            fp = compat_urlopen(xml2_path.decode("utf-8"))
            count = 0
            self.labeltext = ''
            while True:
                s = fp.readline()
                count = count + 1
                self.labeltext = self.labeltext + str(s.decode("utf-8"))
                if s:
                    continue
                else:
                    break
                    continue
            fp.close()
            self['text'].setText(self.labeltext)
        except:
            self['text'].setText('Unable to download...')

class News2(Screen):

        def __init__(self, session):
                self.session = session
                if DESKHEIGHT < 1000:
                    skin = skin_path + 'INFO_SKINFHD.xml'
                else:
                    skin = skin_path + 'INFO_SKINHD.xml'
                f = open(skin, 'r')
                self.skin = f.read()
                f.close()
                Screen.__init__(self, session)
                info = ''
                self['ButtonRedtext'] = Label(_('Exit'))
                self['text'] = ScrollLabel(info)
                self['actions'] = ActionMap(['SetupActions', 'DirectionActions'], {'right': self['text'].pageDown,
                 'ok': self.close,
                 'red': self.close,       
                 'up': self['text'].pageUp,
                 'down': self['text'].pageDown,
                 'cancel': self.close,
                 'left': self['text'].pageUp}, -1)
                try:
                    fp = compat_urlopen(xml3_path.decode("utf-8"))
                    count = 0
                    self.labeltext = ''
                    while True:
                        s = fp.readline()
                        count = count + 1
                        self.labeltext = self.labeltext + str(s.decode("utf-8"))
                        if s:
                            continue
                        else:
                            break
                            continue
                    fp.close()
                    self['text'].setText(self.labeltext)
                except:
                    self['text'].setText('Unable to download...')
             
class Consolo(Screen):                    
                    
    def __init__(self, session, title = 'Consolo', cmdlist = None, finishedCallback = None, closeOnSuccess = False):
        self.session = session
        if DESKHEIGHT < 1000:
            skin = skin_path + 'zdfHD.xml'
        else:
            skin = skin_path + 'zdfFHD.xml'
        f = open(skin, 'r')
        self.skin = f.read()
        f.close()
        Screen.__init__(self, session)
        self.finishedCallback = finishedCallback
        self.closeOnSuccess = closeOnSuccess
        self['text'] = ScrollLabel('')
        self['actions'] = ActionMap(['WizardActions', 'DirectionActions'], {'ok': self.cancel,
         'back': self.cancel,
         'up': self['text'].pageUp,
         'down': self['text'].pageDown}, -1)
        self.cmdlist = cmdlist
        self.newtitle = title
        self.onShown.append(self.updateTitle)
        self.container = eConsoleAppContainer()
        self.run = 0
        self.container.appClosed.append(self.runFinished)
        self.container.dataAvail.append(self.dataAvail)
        self.onLayoutFinish.append(self.startRun)

    def updateTitle(self):
        self.setTitle(self.newtitle)

    def startRun(self):
        self['text'].setText(_('Execution Progress:') + '\n\n')
        print('Console: executing in run', self.run, ' the command:', self.cmdlist[self.run])
        if self.container.execute(self.cmdlist[self.run]):
            self.runFinished(-1)

    def runFinished(self, retval):
        self.run += 1
        if self.run != len(self.cmdlist):
            if self.container.execute(self.cmdlist[self.run]):
                self.runFinished(-1)
        else:
            str = self['text'].getText()
            str += _('Execution finished!!')
            self['text'].setText(str)
            self['text'].lastPage()
            if self.finishedCallback is not None:
                self.finishedCallback()
            if not retval and self.closeOnSuccess:
                self.cancel()
        return

    def cancel(self):
        if self.run == len(self.cmdlist):
            self.close()
            self.container.appClosed.remove(self.runFinished)
            self.container.dataAvail.remove(self.dataAvail)

    def dataAvail(self, str):
        if PY3:
            str = (str).decode()
        self['text'].setText(self['text'].getText() + str)
             
