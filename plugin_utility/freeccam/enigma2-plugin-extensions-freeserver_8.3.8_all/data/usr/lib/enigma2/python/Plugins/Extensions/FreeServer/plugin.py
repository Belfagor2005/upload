#!/usr/bin/python
# -*- coding: utf-8 -*-
from __future__ import print_function
import datetime

Path_1 = '/usr/lib/enigma2/python/Plugins/Extensions/FreeServer/config/author.txt'
line = open(Path_1).read()
session = None
from Plugins.Plugin import PluginDescriptor
from Screens.Screen import Screen
from Components.ScrollLabel import ScrollLabel
from enigma import eTimer, getDesktop
from Screens.MessageBox import MessageBox
from Screens.TextBox import TextBox
from Components.MultiContent import MultiContentEntryText
from Screens.Screen import Screen
from Screens.HelpMenu import HelpableScreen
from Components.ActionMap import ActionMap, NumberActionMap
from Components.ConfigList import ConfigListScreen
from Components.Label import Label
from Components.Sources.StaticText import StaticText
from Components.config import config, getConfigListEntry, ConfigSelection, ConfigSubsection, configfile, ConfigClock
from Screens.Standby import TryQuitMainloop
from Tools.Directories import fileExists, pathExists, SCOPE_PLUGINS
from Components.Pixmap import Pixmap
from Components.ConfigList import ConfigList, ConfigListScreen
from Plugins.Plugin import PluginDescriptor
from Screens.Console import Console
from Screens.Screen import Screen
from enigma import eTimer
from enigma import eConsoleAppContainer
from Components.Label import Label
from Components.Sources.StaticText import StaticText
from Components.ScrollLabel import ScrollLabel
from Components.MultiContent import MultiContentEntryText, MultiContentEntryPixmapAlphaTest
from enigma import eListbox, eTimer, eListboxPythonMultiContent, gFont, getDesktop, loadPNG, eConsoleAppContainer
import os, sys, re, time, os
from xml.dom import Node, minidom
from twisted.web.client import getPage
#import urllib
import base64
from skin import loadSkin
from Plugins.Extensions.FreeServer.outils.compat import PY3
from Plugins.Extensions.FreeServer.outils.CronTimers import *
from Plugins.Extensions.FreeServer.outils.LiseScreencccam import *
from Plugins.Extensions.FreeServer.outils.LiseScreencccam2 import * 
from Plugins.Extensions.FreeServer.outils.Console2 import Console2
from Plugins.Extensions.FreeServer.outils.Console3 import Console3
from Plugins.Extensions.FreeServer.outils.Input import *
from Plugins.Extensions.FreeServer.outils.MyShPrombt import *
matching_words = ["01", "02", "03", "04", "05", "06", "07", "08", "09", "1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "11", "12", "13", "14", "15", "16", "17", "18", "19", "20", "21", "22", "23", "24", "25", "26", "27", "28", "29", "30", "31", "32", "33", "34", "35", "36", "37", "38", "39", "40", "41", "42", "43", "44", "45", "46", "47", "48", "49", "50", "51", "52", "53", "54", "55", "56", "57", "58", "59", "60", "61", "62", "63", "64", "65", "66", "67", "68", "69", "70", "71", "72", "73", "74", "75", "76", "77", "78", "79", "80", "81", "82", "83", "84", "85", "86", "87", "88", "89", "90", "91", "92", "93", "94", "95", "96", "97", "98", "99", "100"]
### EDit By RAED
if PY3:
	from Components.config import ConfigIP
else:
	from Plugins.Extensions.FreeServer.outils.configServer import ConfigIP

def getversioninfo():
    currversion='8.3.8'
    version_file=resolveFilename(SCOPE_PLUGINS, "Extensions/FreeServer/version")
    if os_path.exists(version_file):
        try:
            fp=open(version_file, 'r').readlines()
            for line in fp:
                if 'version' in line:
                    currversion=line.split('=')[1].strip()
        except:
            pass
    return (currversion)

VER = getversioninfo()

### EDit By RAED To DreamOS OE2.5/2.6 and To new Keymap
from Tools.Directories import fileExists
#### End
config.plugins.FreeServerminoo = ConfigSubsection()
config.plugins.FreeServermino = ConfigSubsection()
config.plugins.FreeServerminooo = ConfigSubsection()
config.plugins.FreeServermino.invisible = ConfigSelection(default='disabled', choices=[('disabled', _('Disabled')), ('enabled', _('Enabled'))])  

#config.plugins.FreeServerminoo.Updattime = ConfigIP(default=[0, 0, 0, 0], auto_jump=False)
config.plugins.FreeServerminoo.Updattime = ConfigClock(default=((0 * 60) + 0) * 60)  # 0:00
config.plugins.FreeServerminoo.notification = ConfigYesNo(default=False)
################
#config.plugins.FreeServerminoo.Updattimeiptv = ConfigIP(default=[0, 0, 0, 0], auto_jump=False)
config.plugins.FreeServerminoo.Updattimeiptv = ConfigClock(default=((0 * 60) + 0) * 60)  # 0:00
config.plugins.FreeServerminoo.notificationiptv = ConfigYesNo(default=False)
## Add By RAED
config.plugins.FreeServerminoo.lang = ConfigSelection(default = "EN", choices = [
      ("EN", _("English")),
      ("AR", _("Arabic")),
      ("FR", _("French"))
      ])
config.plugins.FreeServerminoo.updateonline = ConfigYesNo(default=True)
config.plugins.FreeServerminooo.choices = ConfigSelection(default='1', choices=[('1', _('01')), ('2', _('02')), ('3', _('03')), ('4', _('04')), ('5', _('05')), ('6', _('06')), ('7', _('07')), ('8', _('08')), ('9', _('09')), ('10', _('10')), ('11', _('11')), ('12', _('12')), ('13', _('13')), ('14', _('14')), ('15', _('15')), ('16', _('16')), ('17', _('17')), ('18', _('18')), ('19', _('19')), ('20', _('20')), ('21', _('21')), ('22', _('22')), ('23', _('23')), ('24', _('24')), ('25', _('25')), ('26', _('26')), ('27', _('27')), ('28', _('28')), ('29', _('29')), ('30', _('30')), ('31', _('31')), ('32', _('32')), ('33', _('33')), ('34', _('34')), ('35', _('35')), ('36', _('36')), ('37', _('37')), ('38', _('38')), ('39', _('39')), ('40', _('40')), ('41', _('41')), ('42', _('42')), ('43', _('43')), ('44', _('44')), ('45', _('45')), ('46', _('46')), ('47', _('47')), ('48', _('48')), ('49', _('49')), ('50', _('50')), ('51', _('51')), ('52', _('52')), ('53', _('53')), ('54', _('54')), ('55', _('55')), ('56', _('56')), ('57', _('57')), ('58', _('58')), ('59', _('59')), ('60', _('60')), ('61', _('61')), ('62', _('62')), ('63', _('63')), ('64', _('64')), ('65', _('65')), ('66', _('66')), ('67', _('67')), ('68', _('68')), ('69', _('69')), ('70', _('70')), ('71', _('71')), ('72', _('72')), ('73', _('73')), ('74', _('74')), ('75', _('75')), ('76', _('76')), ('77', _('77')), ('78', _('78')), ('79', _('79')), ('80', _('80')), ('81', _('81')), ('82', _('82')), ('83', _('83')), ('84', _('84')), ('85', _('85')), ('86', _('86')), ('87', _('87')), ('88', _('88')), ('89', _('89')), ('90', _('90')), ('91', _('91')), ('92', _('92')), ('93', _('93')), ('94', _('94')), ('95', _('95')), ('96', _('96')), ('97', _('97')), ('98', _('98')), ('99', _('99')), ('100', _('100'))])   
#config.plugins.FreeServerminooo.choices = ConfigSelection(default='1', choices=[('2', '3', '4', '5', '6', '7', '8', '9', '10')])
#config.plugins.FreeServerminooo.choices = ConfigSelection(default='1', choices=[('1', _('01')), ('2', _('02')), ('3', _('03')), ('4', _('04')), ('5', _('05')), ('6'), _('06')), ('7', _('07')), ('8', _('08')), ('9', _('09')), ('10', _('10')), ('11', _('11'))])   
###########
PLUGIN_PATH = '/usr/lib/enigma2/python/Plugins/Extensions/FreeServer/Skin'
plugin_path = '/usr/lib/enigma2/python/Plugins/Extensions/FreeServer/fonts'
skin_path = '/usr/lib/enigma2/python/Plugins/Extensions/FreeServer/Skin/'
p_path = '/usr/lib/enigma2/python/Plugins/Extensions/FreeServer'   
from enigma import addFont
try:
    #addFont('%s/Raleway-Black.ttf' % plugin_path, 'Rale', 100, 1)
    #addFont('%s/PlayfairDisplay-Black.otf' % plugin_path, 'Play', 100, 1)
    addFont('%s/bpmono.ttf' % plugin_path, 'bpmo', 100, 1)
except Exception as ex:
    print(ex)
session = None
data_xml = 'aHR0cHM6Ly9pYTkwMzEwNC51cy5hcmNoaXZlLm9yZy8wL2l0ZW1zL2ZyZWVjY2NhbXNlcnZlci9jYW1zdGFydDAudHh0'
xml_path = base64.b64decode(data_xml)
data_xml2 = 'aHR0cHM6Ly9pYTkwMzEwNC51cy5hcmNoaXZlLm9yZy8wL2l0ZW1zL2ZyZWVjY2NhbXNlcnZlci9jYW1zdGFydC50eHQ='
xml_path2 = base64.b64decode(data_xml2)
#currversions = '8.0.2'
#version = '8.0.2'    
#currversion = '8.0.2'
import os
path='/usr/lib/enigma2/python/Plugins/Extensions/FreeServer/scripts/'
for root, dirs,files in os.walk(path):
    for filename in files:
        scriptfile=os.path.join(path,filename)
        os.chmod(scriptfile,755)

#### Add By RAED

def DreamOS():
    if os.path.exists('/var/lib/dpkg/status'):
        return DreamOS

def getDesktopSize():
    s = getDesktop(0).size()
    return (s.width(), s.height())

def isHD():
    desktopSize = getDesktopSize()
    return desktopSize[0] == 1280

autoStartTimer = None
autoStartTimer2 = None
####################################################################################################        
class FreeServermino(Screen, ConfigListScreen):

        def __init__(self, session):
            self.session = session
            Screen.__init__(self, session)
            self.wget = "wget --no-check-certificate"
            if isHD():
                skin = loadSkin(PLUGIN_PATH + '/skin.xml')
            else:
                if DreamOS():
                    skin = loadSkin(PLUGIN_PATH + '/skinfhdOS.xml')
                else:
                    skin = loadSkin(PLUGIN_PATH + '/skinfhd.xml')

            self.onChangedEntry = []
            self.list = []
                
            ConfigListScreen.__init__(self, self.list, session=self.session, on_change=self.changedEntry)
### EDit By RAED To Add privet keymap.xml
            self['actions'] = ActionMap(['FreeServerminoActions','MenuActions'],
            {
                'menu': self.KeyMenu,
                'info': self.KeyInfo,
                'blue': self.KeyBlue,
                'yellow': self.KeyYellow,
                'green': self.keySave,
                'red': self.keyClose,
                'cancel': self.keyClose,
                'ok': self.keySave,
                'left': self.keyLeft,
                'right': self.keyRight
            }, -1)
### End
            self.__changed = self.changedEntry
            self['Box_1'] = Label('FreeServer V_' + VER)
            #self['Box_2'] = Label(line)
            self['Box_3'] = Label()
            self['Box_33'] = Label()
            self['Box_4'] = Label()
            self['text'] = Label('')
            self['logo'] = Pixmap()
            self['aime'] = Pixmap()
            self['logo'].hide()
            #self['Box_2'].hide()
            self['Box_4'].setText('Last Update Servers  ' + ImportWritetimes())
            self['text'].hide()
            self['aime'].hide()
            self.showhide = False
            #config.plugins.FreeServerminoo.Updattime.value = self.Verif_1(config.plugins.FreeServerminoo.Updattime.value)
            #config.plugins.FreeServerminoo.Updattimeiptv.value = self.Verif_1(config.plugins.FreeServerminoo.Updattimeiptv.value)
            self.initConfig()
            self.createSetup()
            #self.timer = eTimer()
            #try:
            #      self.timer.callback.append(self.update)
            #except:
            #      self.timer_conn = self.timer.timeout.connect(self.update)
            #self.timer.start(2, 1)
            self.onLayoutFinish.append(self.layoutFinished)

            self.notification_value = config.plugins.FreeServerminoo.notification.value
            self.notificationiptv_value = config.plugins.FreeServerminoo.notificationiptv.value

        def layoutFinished(self):
                #self.update
                if config.plugins.FreeServerminoo.updateonline.value:
                	self.update()

        def update(self):
               try:
                       from twisted.web.client import getPage, error
                       url = b"https://ia803104.us.archive.org/0/items/freecccamserver/installer.sh"
                       getPage(url,timeout=10).addCallback(self.parseData).addErrback(self.errBack)
               except Exception as error:
                       print("update error")

        def errBack(self,error=None):
               print("errBack-error :", error)

        def parseData(self, data):
               if PY3:
                   data = data.decode("utf-8")
               else:
                   data = data.encode("utf-8")
               if data:
                   lines = data.split("\n")
                   for line in lines:
                       if line.startswith("version"):
                          self.new_version = line.split("=")[1]
               if VER == self.new_version or VER > self.new_version:
                   print("Updates :", "No new version available")
               else :
                   new_version = self.new_version
                   self.session.openWithCallback(self.install, MessageBox, _('New version %s is available.\n\n.Do want ot install now.' % new_version), MessageBox.TYPE_YESNO)

        def install(self,answer=False):
                if answer:
                	cmdlist = []
                	cmd="wget https://ia803104.us.archive.org/0/items/freecccamserver/installer.sh -O - | /bin/sh"
                	cmdlist.append(cmd)
                	self.session.open(Console, title='Installing last update, enigma will be started after install', cmdlist=cmdlist, finishedCallback=self.myCallback, closeOnSuccess=False)
             #try:
             #  fp = urllib.urlopen(xml_path2)
             #  count = 0
             #  self.labeltext = ''
             #  s1 = fp.readline()
             #  s2 = fp.readline()
             #  s3 = fp.readline()
             #  s1 = s1.strip()
             #  s2 = s2.strip()
             #  s3 = s3.strip()
             #  self.link = s2
             #  self.version = s1
             #  self.info = s3
             #  fp.close()
             #  cstr = s1 + ' ' + s2
             #  if s1 <= currversions:
             #      self.installupdate = False
             #  else :  
             #      self.installupdate()
            #except:
            #    if self.installupdate == False:
            #        return
            #try:
            #   fp = urllib.urlopen(xml_path)
            #   count = 0
            #   self.labeltext = ''
            #   s1 = fp.readline()
            #   s2 = fp.readline()
            #   s3 = fp.readline()
            #   s4 = fp.readline()
            #   s1 = s1.strip()
            #   s2 = s2.strip()
            #   s3 = s3.strip()
            #   s4 = s4.strip()
            #   self.version = s1
            #   self.link = s2
            #   self.link2 = s3
            #   self.info = s4
            #   fp.close()
            #   cstr = s1 + ' ' + s2
            #   if s1 <= currversion:
            #       return
            #       print('[No Update Avilable]')
            #   else :
            #       self.session.openWithCallback(self.install, MessageBox, _('New update available\nFreeServer ' + s1 + ' is available! Do you want to install now.'),MessageBox.TYPE_YESNO)
            #except: 
            #    return '[New Update Avilable]'

        #def installupdate(self):
        #    import sys,os  
        #    os.system("%s https://ia600702.us.archive.org/26/items/dreamosat/freecc.sh -qO - | /bin/sh" % self.wget)
 
        #def install(self,answer=False):
        #    if answer:
        #       if DreamOS():
        #           cmdlist = []
        #           com = self.link2
        #           dom = 'Updating plugin to ' + self.version
        #           self.session.open(Console33, _('Downloading-installing: %s') % dom, ['dpkg install --force-overwrite %s' % com], finishedCallback=self.myCallback, closeOnSuccess=True)
        #       else: 
        #           cmdlist = []           
        #           com = self.link
        #           dom = 'Updating plugin to ' + self.version
        #           self.session.open(Console33, _('downloading-installing: %s') % dom, ['opkg install --force-overwrite %s' % com], finishedCallback=self.myCallback, closeOnSuccess=True)
                
        def myCallback(self,result):
            return
      
        def Verif_1(self, Valist):
            if int(Valist[0]) < 10:
                if int(Valist[1]) < 10:
                    Valist = ['0' + str(Valist[0]), '0' + str(Valist[1])]
                else:
                    Valist = ['0' + str(Valist[0]), Valist[1]]
            elif int(Valist[1]) < 10:
                Valist = [Valist[0], '0' + str(Valist[1])]
            else:
                Valist = [Valist[0], Valist[1]]
            return Valist

        def Verif(self, Valist):
            if int(Valist[0]) < 10:
                if int(Valist[1]) < 10:
                    Valist = '%02s' % Valist[0] + ':' + '%02s' % Valist[1]
                else:
                    Valist = '%02s' % Valist[0] + ':' + str(Valist[1])
            elif int(Valist[1]) < 10:
                Valist = str(Valist[0]) + ':' + '%02s' % Valist[1]
            else:
                Valist = str(Valist[0]) + ':' + str(Valist[1])
            return Valist
  
# Edit By RAED To DreamPOS
             
        def runSetup66(self):
            self.list = []
            self.list.append(getConfigListEntry(_('Select Language TO list Menu'), config.plugins.FreeServerminoo.lang))
            self.list.append(getConfigListEntry(_('Select Update Online'), config.plugins.FreeServerminoo.updateonline))
            self.list.append(getConfigListEntry(_('Mode invisible'), config.plugins.FreeServerminooo.invisible))
            self.list.append(getConfigListEntry(_('Notify CCcam server'), config.plugins.FreeServerminoo.notification))
            self.list.append(getConfigListEntry(_('Notify IPTV service'), config.plugins.FreeServerminoo.notificationiptv))
            self.list.append(getConfigListEntry(_('Choices Server IPTV'), config.plugins.FreeServerminooo.choices))
            self['config'].list = self.list
            self['config'].setList(self.list)
            self['Box_3'].setText('')
            self['Box_33'].setText('')
            if not isHD() and DreamOS():
                   self["config"].l.setValueFont(gFont("Regular", 30)) ## set font to config menu (DreamOS images Need it)
                   self["config"].l.setItemHeight(40) ## set ItemHeight to config menu (DreamOS images Need it)

        def initConfig(self):
            #Updattime = self.Verif(config.plugins.FreeServerminoo.Updattime.value)
            #Updattimeiptv = self.Verif(config.plugins.FreeServerminoo.Updattimeiptv.value)
            self.FreeServerminoo = getConfigListEntry(_('Select Language TO list Menu'), config.plugins.FreeServerminoo.lang)
            self.updateonline = getConfigListEntry(_('Select Update Online'), config.plugins.FreeServerminoo.updateonline)
            self.FreeServermino = getConfigListEntry(_('Mode invisible'), config.plugins.FreeServermino.invisible)
            
            self.notification = getConfigListEntry(_('Notify CCcam servers'), config.plugins.FreeServerminoo.notification)
            self.Updattimeupdate = getConfigListEntry(_('AutoUpdat Server'), config.plugins.FreeServerminoo.Updattime)

            self.notificationiptv = getConfigListEntry(_('Notify IPTV servers'), config.plugins.FreeServerminoo.notificationiptv)
            self.Updattimeiptvupdate = getConfigListEntry(_('AutoUpdat IPTV'), config.plugins.FreeServerminoo.Updattimeiptv)
            self.FreeServerminooo = getConfigListEntry(_('Choices Server IPTV'), config.plugins.FreeServerminooo.choices)

        def createSetup(self):
            self.list = []
            Updattime = config.plugins.FreeServerminoo.Updattime.value
            Updattimeiptv = config.plugins.FreeServerminoo.Updattimeiptv.value

            self.list.append(self.FreeServerminoo)
            self.list.append(self.FreeServerminooo)
            self.list.append(self.FreeServermino)
            self.list.append(self.updateonline)
            
            self.list.append(self.notification)
            if config.plugins.FreeServerminoo.notification.value is True:
                   self.list.append(self.Updattimeupdate)
#                   self['Box_3'].setText('You Have Chosen..Time\n' + str(Updattime) + '\n To Update Your Servers\nCongratulations')

            self.list.append(self.notificationiptv)
            if config.plugins.FreeServerminoo.notificationiptv.value is True:
                   self.list.append(self.Updattimeiptvupdate)
#                   self['Box_33'].setText('You Have Chosen..Time\n' + str(Updattimeiptv) + '\n To Update Your iptv\nCongratulations')

            self['config'].list = self.list
            self['config'].l.setList(self.list)

        def KeyMenu(self):
            cmdlist = []
            cmdlist.append("%s -qO - '" % self.wget + "'")
            cmdlist.append("%s https://ia601506.us.archive.org/33/items/freecccamserver_201906/firecccam.sh -qO - | /bin/sh" % self.wget)
            self.session.open(Console2, title='Free CCcam 7 days', cmdlist=cmdlist, finishedCallback=None)
            return    
        
        def KeyInfo(self):
            if self.showhide:
                pass
            else:
                self.session.open(Console2, title='Free Server', cmdlist=["sh '/usr/lib/enigma2/python/Plugins/Extensions/FreeServer/FreeServer.sh'"], finishedCallback=self.installRun, closeOnSuccess=True)
       
#        def keyLeft(self):
#            if self.showhide:
#                pass
#            else:
#                ConfigListScreen.keyLeft(self)
#                if config.plugins.FreeServerminoo.notification.value == 'enabled' or config.plugins.FreeServerminoo.notificationiptv.value == 'enabled':
#                    self.runSetup()
#                else:
#                    self.runSetup66()

#        def keyRight(self):
#            if self.showhide:
#                pass
#            else:
#                ConfigListScreen.keyRight(self)
#                if config.plugins.FreeServerminoo.notification.value == 'enabled' or config.plugins.FreeServerminoo.notificationiptv.value == 'enabled':
#                    self.runSetup()
#                else:
#                    self.runSetup66()

        def keySave(self):
            if self.showhide:
                pass
            else:
                for x in self['config'].list:
                    x[1].save()
                configfile.save()
                if not self.notification_value == config.plugins.FreeServerminoo.notification.value or \
                not self.notificationiptv_value == config.plugins.FreeServerminoo.notificationiptv.value:
                	self.session.openWithCallback(self.restartenigma, MessageBox, _("Settings Changed. Restart enigma2 now ?!"))
                else:
                	self.close(True)
#                if not os.path.exists('/usr/lib/enigma2/python/Plugins/Extensions/FreeServer/config/Times.txt'):
#                        os.system("touch /usr/lib/enigma2/python/Plugins/Extensions/FreeServer/config/Times.txt")
#                if not os.path.exists('/usr/lib/enigma2/python/Plugins/Extensions/FreeServer/config/Times2.txt'):
#                        os.system("touch /usr/lib/enigma2/python/Plugins/Extensions/FreeServer/config/Times2.txt")
#                if config.plugins.FreeServerminoo.notification.value == 'enabled':
#                    Updattime = self.Verif(config.plugins.FreeServerminoo.Updattime.value)
#                    f = open('/usr/lib/enigma2/python/Plugins/Extensions/FreeServer/config/Times.txt', 'w')
#                    f.write(Updattime)
#                    f.close()
#                    self['Box_3'].setText('You Have Chosen..Time\n' + str(Updattime) + '\n To Update Your Servers\nCongratulations')
                    #self.session.openWithCallback(self.restartenigma, MessageBox, _('Free Server V_' + version + '\nRestart Enigma2 To Load New Settings?'), MessageBox.TYPE_YESNO)
#                else:
#                    f = open('/usr/lib/enigma2/python/Plugins/Extensions/FreeServer/config/Times.txt', 'w')
#                    f.write('Disabled')
#                    f.close()
#                    self['Box_3'].setText('')
#                    self.close()
#                if config.plugins.FreeServerminoo.notificationiptv.value == 'enabled':
#                    Updattimeiptv = self.Verif(config.plugins.FreeServerminoo.Updattimeiptv.value)
#                    f = open('/usr/lib/enigma2/python/Plugins/Extensions/FreeServer/config/Times2.txt', 'w')
#                    f.write(Updattimeiptv)
#                    f.close()
#                    self['Box_33'].setText('You Have Chosen..Time\n' + str(Updattimeiptv) + '\n To Update Your iptv\nCongratulations')
                    #self.session.openWithCallback(self.restartenigma, MessageBox, _('Free Server V_' + version + '\nRestart Enigma2 To Load New Settings?'), MessageBox.TYPE_YESNO)
#                else:
#                    f = open('/usr/lib/enigma2/python/Plugins/Extensions/FreeServer/config/Times2.txt', 'w')
#                    f.write('Disabled')
#                    f.close()
#                    self['Box_33'].setText('')
#                    self.close()    closeOnSuccess=True
                    
        def restartenigma(self, result):
            if result:
                self.session.open(TryQuitMainloop, 3)
       
        def LiseScreencccam(self):
            self.session.open(LiseScreencccam)         
        
        def LiseScreencccam2(self):
            self.session.open(LiseScreencccam2)

        def KeyBlue(self):
            self.session.open(Input)

        def KeyYellow(self):
           self.session.open(Console2, title='Free Server', cmdlist=["sh '/usr/lib/enigma2/python/Plugins/Extensions/FreeServer/scripts/FreeServer.sh'"], finishedCallback=self.installRun, closeOnSuccess=True)
                  
        def installRun(self):
            timeimop = Importtimes()
            NServer = NumbreServers()
            self['Box_4'].setText('Last Update Servers  Nbr_s = ' + str(NServer) + '\n\t' + timeimop)
            self['Box_4'].show()

        def keyClose(self):
            if self.showhide:
                #self['Box_2'].hide()
                self['text'].hide()
                self['logo'].hide()
                self['aime'].hide()
                self['config'].show()
                self['Box_3'].show()
                self['Box_33'].show()
                self['Box_4'].show()
                self.showhide = False
            else:
                for x in self['config'].list:
                    x[1].cancel()
                self.close()
            return
        
        def changedEntry(self):
            self.item = self['config'].getCurrent()
            for x in self.onChangedEntry:
            	x()

            try:
            	if isinstance(self['config'].getCurrent()[1], ConfigYesNo) or isinstance(self['config'].getCurrent()[1], ConfigSelection):
            		self.createSetup()
            except:
            	pass

        def cancel(self):
            self.close(None)
            
def Nmbrs_linesdatastxt():
    n = ''
    file_0 = ''
    if fileExists('/etc/CCcam.cfg'):
        file_0 = '/etc/CCcam.cfg'
        n = sum((1 for _ in open(file_0)))
    else:
        n = 'makach'
    return n
        
def NumbreServers():
    n = Nmbrs_linesdatastxt()
    if n != 'makach':
        counter = 0
        if fileExists('/etc/CCcam.cfg'):
            ptfile = open('/etc/CCcam.cfg', 'r')
            msg = ptfile.readlines()
            for i in range(n):
                if 'c:' in msg[i].lower():
                    counter = counter + 1

            print(counter)
        else:
            counter = 'Nooo'
    else:
        counter = 'Nooo'
    return counter
    
def Importtimes():
    msgtimes = ''
    hr1 = ''
    minute1 = ''
    Jour1 = ''
    mois1 = ''
    now = datetime.datetime.now()
    hr = str(now.hour)
    minute = str(now.minute)
    Nomdujour = time.strftime('%A')
    Jour = str(now.day)
    mois = str(now.month)
    Annee = str(now.year)
    if len(hr) == 1:
        hr1 = '0' + str(hr)
    else:
        hr1 = str(hr)
    if len(minute) == 1:
        minute1 = '0' + str(minute)
    else:
        minute1 = str(minute)
    if len(Jour) == 1:
        Jour1 = '0' + str(Jour)
    else:
        Jour1 = str(Jour)
    if len(mois) == 1:
        mois1 = '0' + str(mois)
    else:
        mois1 = str(mois)
    msgtimes = hr1 + ':' + minute1 + ' ' + Nomdujour + ' ' + Jour1 + ':' + mois1 + ':' + str(Annee)
    Writetimes(msgtimes)
    return msgtimes


def Writetimes(timeserv):
    f = open('/usr/lib/enigma2/python/Plugins/Extensions/FreeServer/config/Runtimes.txt', 'w')
    f.write(timeserv)
    f.close()


def ImportWritetimes():
    f = ''
    Path_1 = '/usr/lib/enigma2/python/Plugins/Extensions/FreeServer/config/Runtimes.txt'
    if fileExists(Path_1):
        f = open(Path_1).read()
    else:
        f = '......'
    return f


def comparetimes_2():
    msgestr_2 = ''
    try:
        now = datetime.datetime.now()
        hr = str(now.hour)
        minute = str(now.minute)
        if len(hr) == 1:
            hr = '0' + hr
        if len(minute) == 1:
            minute = '0' + minute
        hrminute = hr + minute
        hrminute = hrminute.replace(':', '')
        hrminute = hrminute.strip()
        ptimesfile = '/usr/lib/enigma2/python/Plugins/Extensions/FreeServer/config/Times.txt'
        ptfile = open(ptimesfile, 'r')
        data = ptfile.readlines()
        ptfile.close()
        updat_time = data[0]
        if updat_time == 'Disabled' or updat_time == '':
            msgestr_2 = ''
        else:
            updat_time1 = data[0].replace('\n', '').replace('\t', '').replace('\r', '')
            f = []
            f = updat_time.split(':')
            fhour = f[0]
            fminute = f[1]
            if len(fhour) == 1:
                fhour = '0' + fhour
            if len(fminute) == 1:
                fminute = '0' + fminute
            updat_time = str(fhour) + str(fminute)
            updat_time = updat_time.strip()
            if hrminute == updat_time:
                msgestr_2 = '\n\tWait For The Download Time ' + str(updat_time1) + ' of Your Free Servers.... You Can Find Servers Lines In (/etc/CCcam.cfg)'
        return msgestr_2
    except:
        return msgestr_2
        
def comparetimes_3():
    msgestr_3 = ''
    try:
        now = datetime.datetime.now()
        hr = str(now.hour)
        minute = str(now.minute)
        if len(hr) == 1:
            hr = '0' + hr
        if len(minute) == 1:
            minute = '0' + minute
        hrminute = hr + minute
        hrminute = hrminute.replace(':', '')
        hrminute = hrminute.strip()
        ptimesfile = '/usr/lib/enigma2/python/Plugins/Extensions/FreeServer/config/Times2.txt'
        ptfile = open(ptimesfile, 'r')
        data = ptfile.readlines()
        ptfile.close()
        updat_time = data[0]
        if updat_time == 'Disabled' or updat_time == '':
            msgestr_3 = ''
        else:
            updat_time1 = data[0].replace('\n', '').replace('\t', '').replace('\r', '')
            f = []
            f = updat_time.split(':')
            fhour = f[0]
            fminute = f[1]
            if len(fhour) == 1:
                fhour = '0' + fhour
            if len(fminute) == 1:
                fminute = '0' + fminute
            updat_time = str(fhour) + str(fminute)
            updat_time = updat_time.strip()
            if hrminute == updat_time:
                msgestr_3 = '\n\tWait For The Download Time ' + str(updat_time1) + ' of Your Free Servers.... You Can Find Servers Lines In (/etc/CCcam.cfg)'
        return msgestr_3
    except:
        return msgestr_3
                
class DoFreeServerminooScreen(Screen):
    skin = '<screen position="100,100" size="300,300" title="Free Server" ></screen>'

    def __init__(self, session):
        Screen.__init__(self, session)
        self.session = session
        self.msg = ''
        self.minutecount = 30000
        self.FreeServerminoo = eTimer()
        self.FreeServerminoo.stop()
### Edit By RAED To DreamOS
        try:
            self.FreeServerminoo.timeout.get().append(self.CheckFreeServerminoo)
        except:
            self.FreeServerminoo_conn = self.FreeServerminoo.timeout.connect(self.CheckFreeServerminoo)
### End
        self.FreeServerminoo.start(self.minutecount, True)

    def repeat(self, result = None):
        self.FreeServerminoo = eTimer()
        self.FreeServerminoo.stop()
### Edit By RAED To DreamOS
        try:
            self.FreeServerminoo.timeout.get().append(self.CheckFreeServerminoo)
        except:
            self.FreeServerminoo_conn = self.FreeServerminoo.timeout.connect(self.CheckFreeServerminoo)
### End
        self.FreeServerminoo.start(self.minutecount, True)

    def CheckFreeServerminoo(self):
        msg_2 = comparetimes_2()
        now = datetime.datetime.now()
        if not msg_2 == 'Disabled' and not msg_2 == '':
            self.minutecount = 3600000
            if config.plugins.FreeServerminoo.notification.value == 'enabled':
                self.session.openWithCallback(self.repeat, CheckFreeServerminooscreen_2, msg_2)
        else:
            self.minutecount = 30000
            self.repeat()
            
class DoFreeServerminooScreen_2(Screen):
    skin = '<screen position="100,100" size="300,300" title="Free Server" ></screen>'

    def __init__(self, session):
        Screen.__init__(self, session)
        self.session = session
        self.msg = ''
        self.minutecount = 30000
        self.FreeServerminoo = eTimer()
        self.FreeServerminoo.stop()
### Edit By RAED To DreamOS
        try:
            self.FreeServerminoo.timeout.get().append(self.CheckFreeServerminoo)
        except:
            self.FreeServerminoo_conn = self.FreeServerminoo.timeout.connect(self.CheckFreeServerminoo)
### End
        self.FreeServerminoo.start(self.minutecount, True)

    def repeat(self, result = None):
        self.FreeServerminoo = eTimer()
        self.FreeServerminoo.stop()
### Edit By RAED To DreamOS
        try:
            self.FreeServerminoo.timeout.get().append(self.CheckFreeServerminoo)
        except:
            self.FreeServerminoo_conn = self.FreeServerminoo.timeout.connect(self.CheckFreeServerminoo)
### End
        self.FreeServerminoo.start(self.minutecount, True)

    def CheckFreeServerminoo(self):
        msg_3 = comparetimes_3()
        now = datetime.datetime.now()
        if not msg_3 == 'Disabled' and not msg_3 == '':
            self.minutecount = 3600000
            if config.plugins.FreeServerminoo.notification.value == 'enabled':
                self.session.openWithCallback(self.repeat, CheckFreeServerminooscreen_3, msg_3)
        else:
            self.minutecount = 30000
            self.repeat()
            
class CheckFreeServerminooscreen_2(Screen):
    def __init__(self, session, msg = None):
        Screen.__init__(self, session)
### Edit By RAED To FHD Skin
        if isHD():
            skin = loadSkin(PLUGIN_PATH + '/skin.xml')
        else:
            if DreamOS():
                skin = loadSkin(PLUGIN_PATH + '/skinfhdOS.xml')
            else:
                skin = loadSkin(PLUGIN_PATH + '/skinfhd.xml')
### End
        self['actions'] = ActionMap(['SetupActions'], {'ok': self.disappear,
         'cancel': self.disappear}, -1) 
        self.messageupdat = msg
        self['info'] = Label()
        self['info'].setText(msg)
        self.timer = eTimer()
### Edit By RAED To DreamOS
        try:
            self.timer.callback.append(self.disappear_0)
        except:
            self.timer_conn = self.timer.timeout.connect(self.disappear_0)
### End
        self.timer.start(10000, True)

    def disappear_0(self):
        self.timer.stop()
        Importtimes()
        self.session.open(Console2, title='Free Server', cmdlist=["sh '/usr/lib/enigma2/python/Plugins/Extensions/FreeServer/scripts/FreeServer.sh'"], finishedCallback=self.installservers, closeOnSuccess=True)

    def installservers(self):
        ChServers = NumbreServers()
        if ChServers != 'Nooo':
            self.disappear()
            #self['info'].setText('\n\t Congratulations...... You Received  ' + str(ChServers) + ' Servers Free Server ' + currversion + ' @mino60')
           
    def disappear(self):
        self.timer.stop()
        self.close()
        
class CheckFreeServerminooscreen_3(Screen):
    def __init__(self, session, msg = None):
        Screen.__init__(self, session)
### Edit By RAED To FHD Skin

### End
        self['actions'] = ActionMap(['SetupActions'], {'ok': self.disappear,
         'cancel': self.disappear}, -1) 
        self.messageupdat = msg
        self['info'] = Label()
        self['info'].setText(msg)
        self.timer = eTimer()
### Edit By RAED To DreamOS
        try:
            self.timer.callback.append(self.disappear_0)
        except:
            self.timer_conn = self.timer.timeout.connect(self.disappear_0)
### End
        self.timer.start(10000, True)

    def disappear_0(self):
        self.timer.stop()
        Importtimes()
        os.system("sh '/usr/lib/enigma2/python/Plugins/Extensions/FreeServer/scripts/iptv.sh'") 

    def installservers(self):
        ChServers = NumbreServers()
        if ChServers != 'Nooo':
            self.disappear()
            #self['info'].setText('\n\t Congratulations...... You Received  iptv ')
           
    def disappear(self):
        self.timer.stop()
        self.close()

class FreeServerminoosBackgroundWorkerScreen(Screen):

    def __init__(self, session, args = 0):
        self.session = session
        Screen.__init__(self, session)
### Edit By RAED To FHD Skin
        if isHD():
            skin = loadSkin(PLUGIN_PATH + '/skin.xml')
        else:
            if DreamOS():
                skin = loadSkin(PLUGIN_PATH + '/skinfhdOS.xml')
            else:
                skin = loadSkin(PLUGIN_PATH + '/skinfhd.xml')
### End
        self.menu = args
        self.session = session
        self.loop = eTimer()
### Edit By RAED To DreamOS
        try:
            self.loop.callback.append(self.ExecTest)
        except:
            self.loop_conn = self.loop.timeout.connect(self.ExecTest)
### End

    def stopTimer(self):
        self.loop.stop()

    def startTimer(self):
        self.loop.start(1, 1)

    def ExecTest(self):
        self.loop.stop()
        self.DebugToLog()
        self.loop.start(3600000, 1)

    def DebugToLog(self):
        now = datetime.datetime.now()
        timenow = str(now)

StayLoop = FreeServerminoosBackgroundWorkerScreen(session)

def openfile():
    try:
        fp = open('/usr/lib/enigma2/python/Plugins/Extensions/FreeServer/config/Times.txt', 'r')
        line = fp.read()
        fp.close()
        return line
    except:
        cname = 'none'
        return cname


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
        self.container = eConsoleAppContainer()
        self.run = 0
        self.onShown.append(self.updateTitle)
### Edit By RAED To DreamOS   
        try:
            self.container.appClosed.append(self.runFinished)
            self.container.dataAvail.append(self.dataAvail)
        except:
            self.container.appClosed_conn = self.container.appClosed.connect(self.runFinished)
            self.container.dataAvail_conn = self.container.dataAvail.connect(self.dataAvail)
### End
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
### Edit By RAED To DreamOS
            try:
                  self.container.appClosed.remove(self.runFinished)
                  self.container.dataAvail.remove(self.dataAvail)
            except:
                  self.container.appClosed_conn = None
                  self.container.dataAvail_conn = None
### End

    def dataAvail(self, str):
        if PY3:
            import six
            str = six.ensure_str(str)
            self["text"].appendText(str)
        else:
            self['text'].setText(self['text'].getText() + str)

def menu(menuid, **kwargs):
    if menuid == 'mainmenu':
        return [('FreeServer',
          main,
          'FreeServer',
          1)]
    return []


def main(session, **kwargs):
    session.open(FreeServermino)
                                                                                         
class msgnotifier(Screen):
    skinfhd = """
          <screen name="msgnotifier" position="556,586" size="922,170" title="Congratulations!" halign="left" flags="wfNoBorder" borderColor="#000000" backgroundColor="#00000000" >
          <widget source="Title" render="Label" position="132,32" size="600,32" font="Play;28" backgroundColor="#000000" foregroundColor="#CECECE" valign="left" halign="left" zPosition="2"/>
          <widget name="icon" render="Pixmap" pixmap="/usr/lib/enigma2/python/Plugins/Extensions/FreeServer/Deco/myPic.png" zPosition="5" position="0,0" size="128,128" borderColor="#000000" backgroundColor="#00000000" />   
          <widget name="info" position="132,0" size="1200,164" font="Regular;24" zPosition="2" transparent="1" valign="left" halign="left" />
 
    
         </screen>"""
    

    skinhd = """
          <screen name="msgnotifier" position="556,586" size="922,170" title="Congratulations!" halign="left" flags="wfNoBorder" borderColor="#000000" backgroundColor="#00000000" >
          <widget source="Title" render="Label" position="132,32" size="600,32" font="Play;28" backgroundColor="#000000" foregroundColor="#CECECE" valign="left" halign="left" zPosition="2"/>
          <widget name="icon" render="Pixmap" pixmap="/usr/lib/enigma2/python/Plugins/Extensions/FreeServer/Deco/myPic.png" zPosition="5" position="0,0" size="128,128" borderColor="#000000" backgroundColor="#00000000" />   
          <widget name="info" position="132,0" size="1200,164" font="Regular;24" zPosition="2" transparent="1" valign="left" halign="left" />
 
    
         </screen>"""
  
    def __init__(self, session,msg=None):
        self.session = session
        Screen.__init__(self, session)
        if dwidth == 1280:
            self.skin = msgnotifier.skinfhd
        else:
            self.skin = msgnotifier.skinhd
            
        self.setTitle("Congratulations!")
        self["actions"] = ActionMap(["SetupActions"],
            {
                "ok": self.disappear,
                "cancel": self.disappear,
                
            }, -1)
        self["info"]=Label(msg)  
        self['icon'] = Pixmap() 
        self.timer = eTimer()
        self.timer.callback.append(self.disappear)
        self.timer.start(20000, True) 
         
                                
    def disappear(self):
        self.close()
        
def stoploop():
    
    StayLoop.stopTimer()
            
def Nmbrs_linesdatastxt():
    n = ''
    file_0 = ''
    if fileExists('/etc/CCcam.cfg'):
        file_0 = '/etc/CCcam.cfg'
        n = sum((1 for _ in open(file_0)))
    else:
        n = 'makach'
    return n
        
def NumbreServers():
    n = Nmbrs_linesdatastxt()
    if n != 'makach':
        counter = 0
        if fileExists('/etc/CCcam.cfg'):
            ptfile = open('/etc/CCcam.cfg', 'r')
            msg = ptfile.readlines()
            for i in range(n):
                if 'c:' in msg[i].lower():
                    counter = counter + 1

            print(counter)
        else:
            counter = 'Nooo'
    else:
        counter = 'Nooo'
    return counter
    
class AutoStartTimer:
    def __init__(self, session):
        self.session = session
        self.timer = eTimer()
        try:  # DreamOS fix
            self.timer_conn = self.timer.timeout.connect(self.onTimer)
        except:
            self.timer.callback.append(self.onTimer)
        self.update()

    def getWakeTime(self):
        import time
        if config.plugins.FreeServerminoo.notification.value:
            clock = config.plugins.FreeServerminoo.Updattime.value
            nowt = time.time()
            now = time.localtime(nowt)
            return int(time.mktime((now.tm_year, now.tm_mon, now.tm_mday, clock[0], clock[1], 0, now.tm_wday, now.tm_yday, now.tm_isdst)))
        else:
            return -1

    def update(self, atLeast=0):
        import time
        self.timer.stop()
        wake = self.getWakeTime()
        nowtime = time.time()
        if wake > 0:
            if wake < nowtime + atLeast:
                # Tomorrow.
                wake += 24 * 3600
            next = wake - int(nowtime)
            if next > 3600:
                next = 3600
            if next <= 0:
                next = 60
            self.timer.startLongTimer(next)
        else:
            wake = -1
        return wake

    def onTimer(self):
        import time
        self.timer.stop()
        now = int(time.time())
        wake = self.getWakeTime()
        atLeast = 0
        if abs(wake - now) < 60:
            self.runUpdate()
            atLeast = 60
        self.update(atLeast)
        
    def repeat(self, result = None):
        self.FreeServerminoo = eTimer()
        self.FreeServerminoo.stop()
        
    def Checkcounts(self):
         ChServers = NumbreServers()
         msg='\nUpdate successfully You Received  ' + str(ChServers) + ' Servers @mino60'
         print(msg)
         #self.session.openWithCallback(self.repeat,MessageBox,(msg),  MessageBox.TYPE_WARNING, timeout=20)
         self.session.openWithCallback(self.repeat,msgnotifier,msg)           

    def runUpdate(self):
        print('\n *********** AutoUpdat Server ************ \n')
        if config.plugins.FreeServermino.invisible.value == 'enabled':
            self.container = eConsoleAppContainer()
            self.container.execute('wget https://ia801504.us.archive.org/16/items/freecccamserver/FreeServer.sh -qO - | /bin/sh')                                  
        else:
            #self.session.open(Console2, title='AutoUpdat Free Server', cmdlist=["sh '/usr/lib/enigma2/python/Plugins/Extensions/FreeServer/scripts/FreeServer.sh'"], finishedCallback=self.Checkcounts, closeOnSuccess=True)
            self.session.open(Console2, title='AutoUpdat Free Server', cmdlist=["sh '/usr/lib/enigma2/python/Plugins/Extensions/FreeServer/scripts/FreeServer.sh'"], finishedCallback=self.Checkcounts, closeOnSuccess=True)
                  
    
class AutoStartTimer2:
    def __init__(self, session):
        self.session = session
        self.timer = eTimer()
        try:  # DreamOS fix
            self.timer_conn = self.timer.timeout.connect(self.onTimer)
        except:
            self.timer.callback.append(self.onTimer)
        self.update()

    def getWakeTime(self):
        import time
        if config.plugins.FreeServerminoo.notificationiptv.value:
            clock = config.plugins.FreeServerminoo.Updattimeiptv.value
            nowt = time.time()
            now = time.localtime(nowt)
            return int(time.mktime((now.tm_year, now.tm_mon, now.tm_mday, clock[0], clock[1], 0, now.tm_wday, now.tm_yday, now.tm_isdst)))
        else:
            return -1

    def update(self, atLeast=0):
        import time
        self.timer.stop()
        wake = self.getWakeTime()
        nowtime = time.time()
        if wake > 0:
            if wake < nowtime + atLeast:
                # Tomorrow.
                wake += 24 * 3600
            next = wake - int(nowtime)
            if next > 3600:
                next = 3600
            if next <= 0:
                next = 60
            self.timer.startLongTimer(next)
        else:
            wake = -1
        return wake

    def onTimer(self):
        import time
        self.timer.stop()
        now = int(time.time())
        wake = self.getWakeTime()
        atLeast = 0
        if abs(wake - now) < 60:
            self.runUpdate()
            atLeast = 60
        self.update(atLeast)

    def runUpdate(self):
        if config.plugins.FreeServermino.invisible.value == 'enabled':
           for word in matching_words:
               if word in config.plugins.FreeServerminooo.choices.value:
                  imbox = ".sh"
                  com = "https://ia601508.us.archive.org/7/items/iptvworld-1/IPTVWORLD{0}".format(word) + str(imbox)
                  if config.plugins.FreeServerminooo.choices.value == word:
                      self.container = eConsoleAppContainer()
                      #self.container.execute('+'com'+ -qO - | /bin/sh')
                      self.container.execute('wget -O - %s | bash' % (com))

        else:
            self.session.open(Console2, title='AutoUpdat Free IPTV', cmdlist=["sh '/usr/lib/enigma2/python/Plugins/Extensions/FreeServer/scripts/iptv.sh'"], closeOnSuccess=True)

######################################################################

def autostartFreeServerminoo(reason, session=None, **kwargs):
#    global session
#    try:
#        if config.plugins.FreeServerminoo.notification.value == 'disabled' or config.plugins.FreeServerminoo.notificationiptv.value == 'disabled':
#            return
#    except:
#        pass
    global autoStartTimer
    global autoStartTimer2
    if reason == 0:
        if session is not None:
            if autoStartTimer is None:
                autoStartTimer = AutoStartTimer(session)
                autoStartTimer2 = AutoStartTimer2(session)
    return

    if reason == 0:
        if openfile() == 'none':
            StayLoop.stopTimer
        else:
            StayLoop.startTimer()
    if reason == 0 and 'session' in kwargs:
        session = kwargs['session']
        session.open(DoFreeServerminooScreen_2)
        session.open(DoFreeServerminooScreen)


def Plugins(**kwargs):
    return [PluginDescriptor(name='FreeServer ', description='CCcam Free Servers for online Generator', where=PluginDescriptor.WHERE_PLUGINMENU, fnc=main, icon='/usr/lib/enigma2/python/Plugins/Extensions/FreeServer/Deco/plugin.png'), PluginDescriptor(where=[PluginDescriptor.WHERE_SESSIONSTART, PluginDescriptor.WHERE_AUTOSTART], fnc=autostartFreeServerminoo)]
