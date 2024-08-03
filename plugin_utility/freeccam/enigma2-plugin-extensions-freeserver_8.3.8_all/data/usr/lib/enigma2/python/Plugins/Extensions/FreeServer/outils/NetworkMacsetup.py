# -*- coding: UTF-8 -*-
from __future__ import print_function
from .compat import PY3

from os import path as os_path, remove, unlink, rename, chmod, access, X_OK
from shutil import move
import time
from enigma import eTimer, eConsoleAppContainer
from enigma import eListbox, eTimer, eListboxPythonMultiContent, gFont, getDesktop, loadPNG, eConsoleAppContainer
from Screens.Screen import Screen
from Screens.MessageBox import MessageBox
from Screens.Standby import TryQuitMainloop
from Screens.HelpMenu import HelpableScreen
from Components.Console import Console
from Components.Console import Console as iConsole
from Components.Sources.StaticText import StaticText
from Components.Sources.Boolean import Boolean
from Components.Sources.List import List
from Components.SystemInfo import SystemInfo
from Components.Label import Label, MultiColorLabel
from Components.Input import Input
from Screens.InputBox import InputBox
from Components.ScrollLabel import ScrollLabel
from Components.Pixmap import Pixmap, MultiPixmap
from Components.MenuList import MenuList
##### Edit by RAED SCOPE_ACTIVE_SKIN  , getVersionString         
from .config import ConfigMacText, NoSave, ConfigPassword, config, ConfigSubsection, ConfigYesNo, ConfigIP, ConfigSelection, getConfigListEntry, ConfigNumber, ConfigLocations
from Components.About2 import about
if PY3:
	from Components.Network import iNetwork
else:
	from .Network import iNetwork
##### End edit          
from Components.ConfigList import ConfigListScreen
from Components.PluginComponent import plugins
from Components.FileList import MultiFileSelectList
from Components.ActionMap import ActionMap, NumberActionMap, HelpableActionMap
from Tools.Directories import fileExists, resolveFilename, SCOPE_PLUGINS
from Tools.LoadPixmap import LoadPixmap
from Plugins.Plugin import PluginDescriptor
from subprocess import call
import glob,sys,os,random,datetime,time
from Screens.Standby import TryQuitMainloop
session = None
from time import *

### EDit By RAED To DreamOS OE2.5/2.6
from Tools.Directories import fileExists
def DreamOS():
    if os.path.exists('/var/lib/dpkg/status'):
        return DreamOS
######################################################################################################
plugin_path = '/usr/lib/enigma2/python/Plugins/Extensions/FreeServer/fonts'
skin_path = '/usr/lib/enigma2/python/Plugins/Extensions/FreeServer/Skin/'
p_path = '/usr/lib/enigma2/python/Plugins/Extensions/FreeServer'   
from enigma import addFont
try:
    #addFont('%s/slyk-medium.ttf' % plugin_path, 'slyk', 100, 1)
    addFont('%s/bpmono.ttf' % plugin_path, 'Play', 100, 1)
except Exception as ex:
    print(ex)
#########################################################################################################
DESKHEIGHT = getDesktop(0).size().height()
skin_path = '/usr/lib/enigma2/python/Plugins/Extensions/FreeServer/Skin/'

def DreamOS():
    if os.path.exists('/var/lib/dpkg/status'):
        return DreamOS

class NetworkMacsetup(Screen, ConfigListScreen, HelpableScreen):
    skin = """
    <screen name="NetworkMacSetup" position="center,center" size="720,400" title="MAC address setup" >
        <ePixmap pixmap="/usr/lib/enigma2/python/Plugins/Extensions/FreeServer/Deco/key_info.png" position="10,300" size="140,40" zPosition="10" alphatest="blend" />
        <ePixmap pixmap="/usr/lib/enigma2/python/Plugins/Extensions/FreeServer/Deco/button_red.png" position="20,356" size="140,40" zPosition="10" alphatest="blend" />
        <ePixmap pixmap="/usr/lib/enigma2/python/Plugins/Extensions/FreeServer/Deco/button_green.png" position="160,356" size="140,40" zPosition="10" alphatest="blend" />
        <ePixmap pixmap="/usr/lib/enigma2/python/Plugins/Extensions/FreeServer/Deco/button_yellow.png" position="350,356" size="140,40" zPosition="10" alphatest="blend" />
        <ePixmap pixmap="/usr/lib/enigma2/python/Plugins/Extensions/FreeServer/Deco/button_blue.png" position="500,356" size="140,40" zPosition="10" alphatest="blend" />
        <widget source="key_info" render="Label" position="6,292" zPosition="1" size="140,40" font="Regular;22" halign="center" valign="center" backgroundColor="#ffffff" transparent="1" />
        <widget source="key_red" render="Label" position="26,346" zPosition="1" size="140,40" font="Regular;22" halign="center" valign="center" backgroundColor="#ffffff" transparent="1" />
        <widget source="key_green" render="Label" position="190,346" zPosition="1" size="140,40" font="Regular;22" halign="center" valign="center" backgroundColor="#ffffff" transparent="1" />
        <widget source="key_yellow" render="Label" position="360,346" zPosition="1" size="140,40" font="Regular;22" halign="center" valign="center" backgroundColor="#ffffff" transparent="1" />
        <widget source="key_blue" render="Label" position="510,346" zPosition="1" size="200,40" font="Regular;22" halign="center" valign="center" backgroundColor="#ffffff" transparent="1" />
        <widget name="config" position="10,50" size="700,600" scrollbarMode="showOnDemand" />
        <widget source="introduction" render="Label" position="80,200" size="560,50" zPosition="10" font="Regular;21" halign="center" valign="center" backgroundColor="#25062748" transparent="1" />
    </screen>
"""
    def __init__(self, session):
        Screen.__init__(self, session)
        HelpableScreen.__init__(self)
        self.onChangedEntry = []
        self.list = []
        ConfigListScreen.__init__(self, self.list, session=self.session, on_change=self.selectionChanged)
        Screen.setTitle(self, _('MAC-address settings'))
        self.curMac = self.getmac('eth0')
        self.getConfigMac = NoSave(ConfigMacText(default=self.curMac))
        self['key_info'] = StaticText(_('Info'))        
        self['key_red'] = StaticText(_('Cancel'))
        self['key_green'] = StaticText(_('Change Now !'))
        self['key_yellow'] = StaticText(_('Random'))
        self['key_blue'] = StaticText(_('Restore Original'))
        self['introduction'] = StaticText(_('Press OK to set the MAC-address.'))
        self['OkCancelActions'] = HelpableActionMap(self, 'OkCancelActions', {'cancel': (self.cancel, _('Exit nameserver configuration')),
         'ok': (self.ok, _('Activate current configuration'))})
        self['ColorActions'] = HelpableActionMap(self, 'ColorActions', {'red': (self.cancel, _('Exit MAC-address configuration')),
         'green': (self.ok, _('Activate MAC-address configuration')),
         'yellow': (self.newRandom, _('Random')),
         "showEventInfo": (self.convert, _('info')),
         'blue': (self.OriginalMac, _('Restore Original'))})
        self['actions'] = ActionMap(['MovieSelectionActions', 'SetupActions', 'DirectionActions', 'ColorActions'], {'ok': self.ok, "showEventInfo": self.convert}, -2)
        self.list = []
        ConfigListScreen.__init__(self, self.list)
        self.createSetup()
        self.output_line = ''
        self.updateList()
        self.iConsole = iConsole()
        self.container = eConsoleAppContainer()
        retval = self.container.execute("ifconfig > /tmp/tmac && route >> /tmp/tmac && echo Address MAC Original  `echo $(ethtool -P eth0 | awk '{print $3}')` >> /tmp/tmac && echo Current Address MAC    `echo $(ifconfig | grep HW | awk '{print $5}')` >> /tmp/tmac")
        if self.selectionChanged not in self['config'].onSelectionChanged:
            self['config'].onSelectionChanged.append(self.selectionChanged)
        self.selectionChanged()

    def selectionChanged(self):
        item = self['config'].getCurrent()
        
    def getmac(self, iface):
        eth = about.getIfConfig(iface)
        print("eth ************", eth)
        return eth['hwaddr']
        
    def createSetup(self):
        self.list = []
        self.list.append(getConfigListEntry(_('MAC-address'), self.getConfigMac))
        self['config'].list = self.list
        self['config'].l.setList(self.list)

    def ok(self):
        MACETC = '/etc/enigma2/hwmac'
        TMPCAC = '/tmp/hwmac'
        if not fileExists(MACETC):
            os.system('touch %s' % MACETC)
        if fileExists(TMPCAC):
            with open(MACETC, 'w') as outFile:
              with open(TMPCAC, 'r') as hwmac:
                for line in hwmac.read().split('\n'):
                  if line.strip() != '':
                    print(line, file=open(MACETC,'a'))
                    os.remove(TMPCAC)
                    MAC = self.getConfigMac.value
                    f = open(MACETC, 'r')
                    for line in f.readlines():
                        try:
                        	MAC = line.strip('\n')
                        except:
                        	pass       
                        self.restartLan()
        else:        
            MAC = self.getConfigMac.value
            f = open(MACETC, 'r')
            for line in f.readlines():
                try:
                	MAC = line.strip('\n')  
                except:
                	pass       
                self.restartLan()
                
    def newRandom(self):
        self.MacAddress.value = self.GenerateMacAddress()
        self['config'].invalidateCurrent()

    def updateList(self):
        self.MacAddress = NoSave(ConfigPassword(default=''))
        self.list.append(getConfigListEntry(_('New Address MAC'), self.MacAddress))
        self['config'].list = self.list
        self['config'].l.setList(self.list)  
        
    def GenerateMacAddress(self):        
        if DreamOS():
               random.choice('0123456789abcdef')         
               create_random_mac = "00:09:34:%02x:%02x:%02x" % (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
               MAC = self.getConfigMac.value
               MAC = create_random_mac
               f = open('/tmp/hwmac', 'w')
               f.write(MAC)
               f.close()
               return create_random_mac
        else:
               random.choice('0123456789abcdef')  
               create_random_mac = "00:1d:ec:%02x:%02x:%02x" % (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
               MAC = self.getConfigMac.value
               MAC = create_random_mac
               f = open('/tmp/hwmac', 'w')
               f.write(MAC)
               f.close()
               return create_random_mac
               
    def OriginalMac(self): 
        self.container = eConsoleAppContainer()
        retval = self.container.execute("macadr=`echo $(ethtool -P eth0 | awk '{print $3}')`&& echo $macadr > /etc/enigma2/hwmac")
        self.restartLan()
        
    def KeyInfo(self): 
        self.setTitle(_("Please wait"))
        self["status"] = StaticText()
        self.iConsole = iConsole()
        self.container = eConsoleAppContainer()
        retval = self.container.execute("ifconfig")
        self.restartLan()
        self["status"].text = _("Converting %s" % config.plugins.m2b.m3ufile.value)
    
                            
    def run(self):
        self.ok()

    def cancel(self):
        self.close()

    def restartBox(self, answer):
        if answer is True:
            self.session.open(TryQuitMainloop, 2)
        else:
            self.close()

    def restartLan(self):
        iNetwork.restartNetwork(self.restartLanDataAvail)
        self.restartLanRef = self.session.openWithCallback(self.restartfinishedCB, MessageBox, _('Please wait while we configure your network...'), type=MessageBox.TYPE_INFO, enable_input=False)

            
    def restartLanDataAvail(self, data):
        if data is True:
            iNetwork.getInterfaces(self.getInterfacesDataAvail)

    def getInterfacesDataAvail(self, data):
        if data is True:
            self.restartLanRef.close(True)
            
    def restartfinishedCB(self, data):
        if data is True:
           if DreamOS():
               message = _('Finished configuring your network - Need Restart STB (Important)\n\nRestart your STB now?')
               mbox = self.session.openWithCallback(self.restartBox, MessageBox, message, MessageBox.TYPE_YESNO)
               mbox.setTitle(_('Restart STB'))
           else:         
               self.session.openWithCallback(self.close, MessageBox, _('Finished configuring your network'), type=MessageBox.TYPE_INFO, timeout=10, default=False)      

    def convert(self):
            self.session.open(create_bouquet)
    
INFO_SKIN = '<screen name="Panel-Info"  position="center,center" size="730,400" title="PANEL-Info" >\n\t<widget name="label2" position="0,10" size="730,25" font="Regular;20" transparent="1" halign="center" foregroundColor="#f2e000" />\n\t<widget name="label1" position="10,45" size="710,350" font="Console;20" zPosition="1" backgroundColor="#251e1f20" transparent="1" />\n</screen>'

class create_bouquet(Screen):

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
                #self.Network()
                #self.setTitle(_("Please wait"))   
                #self['text'] = Label()
                #self["status"] = StaticText()
                #self.iConsole = iConsole()
                #self.container = eConsoleAppContainer()
                #retval = self.container.execute("ifconfig > /tmp/tmac")
                #retval = self.container.execute("ifconfig > /tmp/tmac&&route >> /tmp/tmac&&echo Address MAC Original  `echo $(ethtool -P eth0 | awk '{print $3}')` >> /tmp/tmac&&echo Current Address MAC    `echo $(ifconfig | grep HW | awk '{print $5}')` >> /tmp/tmac")                
                #try:
                #	time.sleep(2)
                #except:
                #	pass
                info = ''
                self['ButtonRedtext'] = Label(_('Exit'))
                self['myPic'] = Pixmap()
                self['text'] = ScrollLabel(info)
                self['actions'] = ActionMap(['SetupActions', 'DirectionActions'], {'right': self['text'].pageDown,
                'ok': self.close,
                'red': self.close,       
                'up': self['text'].pageUp,
                'down': self['text'].pageDown,
                'cancel': self.close,
                'left': self['text'].pageUp}, -1)
                try:
                    fp = open('/tmp/tmac', 'r')
                    count = 0
                    self.labeltext = ''
                    while True:
                        s = fp.readline()
                        count = count + 1
                        self.labeltext = self.labeltext + str(s)
                        if s:
                            continue
                        else:
                            break
                            continue
                    fp.close()
                    self['text'].setText(self.labeltext)
                except:
                    self['text'].setText('Unable to download...')
                
        def cancel(self, result, retval, extra_args):
                self.close()
                
