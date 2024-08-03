# -*- coding: UTF-8 -*-
from __future__ import print_function

from Plugins.Plugin import PluginDescriptor
from Screens.Screen import Screen
from datetime import date, datetime
from Components.Label import Label
from Components.Sources.StaticText import StaticText
from enigma import eTimer, eConsoleAppContainer
from Screens.MessageBox import MessageBox
from Screens.Standby import TryQuitMainloop
from Components.MenuList import MenuList
from Components.ActionMap import ActionMap
from Components.MediaPlayer import *
from enigma import *
from Screens.MessageBox import MessageBox
from Components.Pixmap import Pixmap  
from Components.GUIComponent import *
from Screens.ServiceInfo import *
from Components.config import *
from enigma import eServiceReference
from Tools.Directories import fileExists, pathExists
from Plugins.Extensions.FreeServer.outils.myInput import *  
from Plugins.Extensions.FreeServer.outils.myInput2 import * 
from Plugins.Extensions.FreeServer.outils.myInput3 import * 
from Plugins.Extensions.FreeServer.outils.myInput4 import *  
from Plugins.Extensions.FreeServer.outils.myInput5 import *  
from Plugins.Extensions.FreeServer.outils.myInput6 import *  
from Plugins.Extensions.FreeServer.outils.myInput7 import *  
from time import *
import time
from enigma import eTimer, getDesktop
from enigma import *
import os, sys, re
#import urllib
import base64
#session = None
#data_xml = 'aHR0cHM6Ly9pYTYwMDcwMi51cy5hcmNoaXZlLm9yZy8yNi9pdGVtcy9kcmVhbW9zYXQvY2Ftc3RhcnQwLnR4dA=='
#xml_path = base64.b64decode(data_xml)
#version = '7710'    
#currversion = '7710'   
###################################################################################################### 

#https://www.logitheque.com/wp-content/uploads/sites/4/2020/09/how-set-up-iptv-smarters-pro-1024x576.jpg
######################################################################################################
plugin_path = '/usr/lib/enigma2/python/Plugins/Extensions/FreeServer/fonts'
skin_path = '/usr/lib/enigma2/python/Plugins/Extensions/FreeServer/Skin/'
p_path = '/usr/lib/enigma2/python/Plugins/Extensions/FreeServer'   
from enigma import addFont
try:
    addFont('%s/bpmono.ttf' % plugin_path, 'bpmo', 100, 1)
    
except Exception as ex:
    print(ex)

def DreamOS():
    if os.path.exists('/var/lib/dpkg/status'):
        return DreamOS

def getDesktopSize():
    s = getDesktop(0).size()
    return (s.width(), s.height())

def isHD():
    desktopSize = getDesktopSize()
    return desktopSize[0] == 1280

#########################################################################################################
class Myiptvservices(Screen):
#### Edit By RAED
        if not isHD():
            if DreamOS():
            	skin = """
                      <screen position="0,0" size="1920,1080" title="Schedule to football matchs this week" backgroundColor="#16000000" flags="wfNoBorder">             
                      <eLabel text="Move Up/Down or Left/Right to move list/page" position="0,0" size="1920,50" backgroundColor="#16000000" zPosition="2"/>
                      <widget name="myMenu" position="14,60" size="800,1010" backgroundColor="#16000000" transparent="1" zPosition="2"/>
                      <ePixmap position="0,0" size="1916,1080" pixmap="/usr/lib/enigma2/python/Plugins/Extensions/FreeServer/Deco/SLIDE_02_FHD.jpg" alphatest="blend" transparent="1" />
                      </screen>"""
            else:
            	skin = """
                      <screen position="0,0" size="1920,1080" title="Schedule to football matchs this week" backgroundColor="#16000000" flags="wfNoBorder">             
                      <eLabel text="Move Up/Down or Left/Right to move list/page" position="0,0" size="1920,50" font="Play;35" foregroundColor="#FC0000" backgroundColor="#16000000" zPosition="2"/>
                      <widget name="myMenu" position="14,60" size="800,1010" font="Play;35" itemHeight="40" foregroundColor="#FEFEFE" transparent="1" zPosition="2"/>
                      <ePixmap position="0,0" size="1916,1080" pixmap="/usr/lib/enigma2/python/Plugins/Extensions/FreeServer/Deco/SLIDE_02_FHD.jpg" alphatest="blend" transparent="1" />
                      </screen>"""
        else:
            if DreamOS():        
                skin = """
                      <screen position="0,0" size="1280,720" title="Schedule to football matchs this week" backgroundColor="#16000000" flags="wfNoBorder">              
                      <eLabel text="Move Up/Down or Left/Right to move list/page" position="600,7" size="680,32" backgroundColor="#16000000" zPosition="2"/>
                      <widget name="myMenu" position="12,56" size="620,650" backgroundColor="#16000000" transparent="1" zPosition="2"/>
                      <ePixmap position="0,0" size="1280,720" pixmap="/usr/lib/enigma2/python/Plugins/Extensions/FreeServer/Deco/SLIDE_02.jpg" alphatest="blend" transparent="1" />
                      </screen>"""
            else:
                skin = """
                      <screen position="0,0" size="1280,720" title="Schedule to football matchs this week" backgroundColor="#16000000" flags="wfNoBorder">              
                      <eLabel text="Move Up/Down or Left/Right to move list/page" position="600,7" size="680,32" font="Play;28" foregroundColor="#FC0000" backgroundColor="#16000000" zPosition="2"/>
                      <widget name="myMenu" position="12,56" size="620,650" foregroundColor="#FEFEFE" transparent="1" zPosition="2"/>
                      <ePixmap position="0,0" size="1280,720" pixmap="/usr/lib/enigma2/python/Plugins/Extensions/FreeServer/Deco/SLIDE_02.jpg" alphatest="blend" transparent="1" />
                      </screen>"""

        def __init__(self, session, finishedCallback = None, picPath = None, args = 0):
                self.session = session
                Screen.__init__(self, session)
                self.finishedCallback = finishedCallback
                self.setTitle("List of IPTV server avilable")
                self.wget = "wget --no-check-certificate"
                list = []       
                list.append(("        Server 1", "com_1"))
                list.append(("        Server 2", "com_2"))      
                list.append(("        Server 3", "com_3"))
                list.append(("        Server 4", "com_4")) 
                list.append(("        Server 5", "com_5"))
                list.append(("        Server 6", "com_6"))             
                list.append(("        Server 7", "com_7"))
                list.append(("        Server 8", "com_8"))          
                list.append(("        Server 9", "com_9"))
                list.append(("        Server 10", "com_10"))
                list.append(("        Server 11", "com_11"))
                list.append(("        Server 12", "com_12"))  
                list.append(("        Server 13", "com_13"))
                list.append(("        Server 14", "com_14"))
                list.append(("        Server 15", "com_15"))                          
                list.append(("        Server 16", "com_16"))            
                list.append(("        Server 17", "com_17"))
                list.append(("        Server 18", "com_18"))                    
                list.append(("        Server 19", "com_19"))
                list.append(("        Server 20", "com_20"))
                list.append(("        Server 21", "com_21"))
                list.append(("        Server 22", "com_22"))
                list.append(("        Server 23", "com_23"))
                list.append(("        Server 24", "com_24"))
                list.append(("        Server 25", "com_25"))
                list.append(("        Server 26", "com_26"))                    
                list.append(("        Server 27", "com_27"))
                list.append(("        Server 28", "com_28"))
                list.append(("        Server 29", "com_29"))
                list.append(("        Server 30", "com_30"))
                list.append(("        Server 31", "com_31"))
                list.append(("        Server 32", "com_32"))
                list.append(("        Server 33", "com_33"))                    
                list.append(("        Server 34", "com_34"))
                list.append(("        Server 35", "com_35"))
                list.append(("        Server 36", "com_36"))
                list.append(("        Server 37", "com_37"))
                list.append(("        Server 38", "com_38"))
                list.append(("        Server 39", "com_39"))
                list.append(("        Server 40", "com_40"))
                list.append(("        Server 41", "com_41"))
                list.append(("        Server 42", "com_42"))
                list.append(("        Server 43", "com_43"))
                list.append(("        Server 44", "com_44"))  
                list.append(("        Server 45", "com_45"))
                list.append(("        Server 46", "com_46"))
                list.append(("        Server 47", "com_47"))  
                list.append(("        Server 48", "com_48"))
                list.append(("        Server 49", "com_49"))              
                list.append(("        Server 50", "com_50"))
                list.append(("        Server 51", "com_51"))
                list.append(("        Server 52", "com_52"))
                list.append(("        Server 53", "com_53"))
                list.append(("        Server 54", "com_54"))
                list.append(("        Server 55", "com_55"))  
                list.append(("        Server 56", "com_56"))  
                list.append(("        Server 57", "com_57"))
                list.append(("        Server 58", "com_58"))  
                list.append(("        Server 59", "com_59"))
                list.append(("        Server 60", "com_60"))                                    
                list.append(("        Server 61", "com_61"))
                list.append(("        Server 62", "com_62"))    
                list.append(("        Server 63", "com_63"))
                list.append(("        Server 64", "com_64")) 
                list.append(("        Server 65", "com_65"))
                list.append(("        Server 66", "com_66"))             
                list.append(("        Server 67", "com_67"))
                list.append(("        Server 68", "com_68"))          
                list.append(("        Server 69", "com_69"))
                list.append(("        Server 70", "com_70"))
                list.append(("        Server 71", "com_71"))
                list.append(("        Server 72", "com_72"))  
                list.append(("        Server 73", "com_73"))
                list.append(("        Server 74", "com_74"))
                list.append(("        Server 75", "com_75"))                          
                list.append(("        Server 76", "com_76"))            
                list.append(("        Server 77", "com_77"))
                list.append(("        Server 78", "com_78"))                    
                list.append(("        Server 79", "com_79"))
                list.append(("        Server 80", "com_80"))
                list.append(("        Server 81", "com_81"))
                list.append(("        Server 82", "com_82"))
                list.append(("        Server 83", "com_83"))
                list.append(("        Server 84", "com_84"))
                list.append(("        Server 85", "com_85"))
                list.append(("        Server 86", "com_86"))                    
                list.append(("        Server 87", "com_87"))
                list.append(("        Server 88", "com_88"))
                list.append(("        Server 89", "com_89"))
                list.append(("        Server 90", "com_90"))
                list.append(("        Server 91", "com_91"))
                list.append(("        Server 92", "com_92"))
                list.append(("        Server 93", "com_93"))                    
                list.append(("        Server 94", "com_94"))
                list.append(("        Server 95", "com_95"))
                list.append(("        Server 96", "com_96"))
                list.append(("        Server 97", "com_97"))
                list.append(("        Server 98", "com_98"))
                list.append(("        Server 99", "com_99"))
                list.append(("        Server 100", "com_100"))
                list.append((_("Exit"), "exit"))
                Screen.__init__(self, session)
                self["key_red"] = Label(_("Cancel"))
                self["key_green"] = Label(_("Clean"))
                #self["myYellowBtn"] = Label(_("restart"))
                #self["myBlueBtn"] = Label(_("Preview"))
                self.cmdlist = []
                self.onChangedEntry = []
                self.initialservice = session.nav.getCurrentlyPlayingServiceReference()         
                self["myMenu"] = MenuList(list)
                self['setupActions'] = ActionMap(['SetupActions', 'ColorActions', 'DirectionActions'], 
                {
                        'green': self.Clean,
                        # '0': self.myInput,
                        #'blue': self.gotoa,
                        'red': self.close,
                        'ok': self.go,
                        'cancel': self.close
                }, -1)
                self.timer = eTimer()
                self.timer.start(2, 1)
                self.onLayoutFinish.append(self.layoutFinished)
### Edit By RAED To DreamOS & Fix update notification restart warrning
                try:
                       self.timer.callback.append(self.update)
                except:
                       self.timer_conn = self.timer.timeout.connect(self.update)


        def layoutFinished(self):
                self.setTitle(" ")

        def update(self):
                try:
                    fp = urllib.urlopen(xml_path)
                    count = 0
                    self.labeltext = ''
                    s1 = fp.readline()
                    s2 = fp.readline()
                    s3 = fp.readline()
                    s1 = s1.strip()
                    s2 = s2.strip()
                    s3 = s3.strip()
                    self.link = s2
                    self.version = s1
                    self.info = s3
                    fp.close()
                    cstr = s1 + ' ' + s2
                    if s1 <= currversion:
                        return
                        print('[No Update Avilable]')
                    else:  
                        self.session.openWithCallback(self.install, MessageBox, _('New update available.\n\nDo you want ot install now.'), MessageBox.TYPE_YESNO)
                        print('[New Update Avilable]')
                except:
                    return

        def install(self, *retval):
            os.system("%s https://ia600702.us.archive.org/26/items/dreamosat/freecc4.sh -qO - | /bin/sh" % self.wget)
            self.session.openWithCallback(self.restartenigma, MessageBox, _('** Nedd Restart Enigma2 To Load New Update ?!! **'), MessageBox.TYPE_YESNO, timeout=10)
### End EDit
        def go(self):
                from Plugins.Extensions.FreeServer.outils.Console3 import Console3
                returnValue = self["myMenu"].l.getCurrentSelection()[1]
                if returnValue != None:         
                        if returnValue =="com_1":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia601508.us.archive.org/7/items/iptvworld-1/IPTVWORLD1.sh h -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='Free IPTVFree001', cmdlist=cmdlist, finishedCallback=None)
                        elif returnValue =="com_2":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia601508.us.archive.org/7/items/iptvworld-1/IPTVWORLD2.sh  -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='Free IPTVFree002', cmdlist=cmdlist, finishedCallback=None)
                        elif returnValue =="com_3":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'") 
                                cmdlist.append("%s https://ia601508.us.archive.org/7/items/iptvworld-1/IPTVWORLD3.sh  -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='Free IPTVFree003', cmdlist=cmdlist, finishedCallback=None)
                        elif returnValue =="com_4":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'") 
                                cmdlist.append("%s https://ia601508.us.archive.org/7/items/iptvworld-1/IPTVWORLD4.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='Free IPTVFree004', cmdlist=cmdlist, finishedCallback=None)
                        elif returnValue =="com_5":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia601508.us.archive.org/7/items/iptvworld-1/IPTVWORLD5.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='Free IPTVFree005', cmdlist=cmdlist, finishedCallback=None)
                        elif returnValue =="com_6":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia601508.us.archive.org/7/items/iptvworld-1/IPTVWORLD6.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='Free IPTVFree006', cmdlist=cmdlist, finishedCallback=None)
                        elif returnValue =="com_7":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia601508.us.archive.org/7/items/iptvworld-1/IPTVWORLD7.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='Free IPTVFree007', cmdlist=cmdlist, finishedCallback=None)
                        elif returnValue =="com_8":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")    
                                cmdlist.append("%s https://ia601508.us.archive.org/7/items/iptvworld-1/IPTVWORLD8.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='Free IPTVFree008', cmdlist=cmdlist, finishedCallback=None)
                        elif returnValue =="com_9":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia601508.us.archive.org/7/items/iptvworld-1/IPTVWORLD9.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='Free IPTVFree009', cmdlist=cmdlist, finishedCallback=None)
                        elif returnValue =="com_10":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia601508.us.archive.org/7/items/iptvworld-1/IPTVWORLD10.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='Free IPTVFree010', cmdlist=cmdlist, finishedCallback=None)
                        elif returnValue =="com_11":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia601508.us.archive.org/7/items/iptvworld-1/IPTVWORLD11.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='Free IPTVFree011', cmdlist=cmdlist, finishedCallback=None)
                        elif returnValue =="com_12":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia601508.us.archive.org/7/items/iptvworld-1/IPTVWORLD12.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='Free IPTVFree012', cmdlist=cmdlist, finishedCallback=None)
                        elif returnValue =="com_13":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia601508.us.archive.org/7/items/iptvworld-1/IPTVWORLD13.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='Free IPTVFree013', cmdlist=cmdlist, finishedCallback=None)
                        elif returnValue =="com_14":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia601508.us.archive.org/7/items/iptvworld-1/IPTVWORLD14.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='Free IPTVFree014', cmdlist=cmdlist, finishedCallback=None)
                        elif returnValue =="com_15":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia601508.us.archive.org/7/items/iptvworld-1/IPTVWORLD15.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='Free IPTVFree015', cmdlist=cmdlist, finishedCallback=None)
                        elif returnValue =="com_16":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia601508.us.archive.org/7/items/iptvworld-1/IPTVWORLD16.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='Free IPTVFree016', cmdlist=cmdlist, finishedCallback=None)
                        elif returnValue =="com_17":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia601508.us.archive.org/7/items/iptvworld-1/IPTVWORLD17.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='Free IPTVFree017', cmdlist=cmdlist, finishedCallback=None)
                        elif returnValue =="com_18":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia601508.us.archive.org/7/items/iptvworld-1/IPTVWORLD18.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='Free IPTVFree018', cmdlist=cmdlist, finishedCallback=None)
                        elif returnValue =="com_19":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia601508.us.archive.org/7/items/iptvworld-1/IPTVWORLD19.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='Free IPTVFree019', cmdlist=cmdlist, finishedCallback=None)
                        elif returnValue =="com_20":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia601508.us.archive.org/7/items/iptvworld-1/IPTVWORLD20.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='Free IPTVFree020', cmdlist=cmdlist, finishedCallback=None)
                        elif returnValue =="com_21":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia601508.us.archive.org/7/items/iptvworld-1/IPTVWORLD21.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='Free IPTVFree021', cmdlist=cmdlist, finishedCallback=None)
                        elif returnValue =="com_22":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia601508.us.archive.org/7/items/iptvworld-1/IPTVWORLD22.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='Free IPTVFree022', cmdlist=cmdlist, finishedCallback=None)
                        elif returnValue =="com_23":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia601508.us.archive.org/7/items/iptvworld-1/IPTVWORLD23.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='Free IPTVFree023', cmdlist=cmdlist, finishedCallback=None)
                        elif returnValue =="com_24":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia601508.us.archive.org/7/items/iptvworld-1/IPTVWORLD24.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='Free IPTVFree024', cmdlist=cmdlist, finishedCallback=None)
                        elif returnValue =="com_25":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia601508.us.archive.org/7/items/iptvworld-1/IPTVWORLD25.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='Free IPTVFree025', cmdlist=cmdlist, finishedCallback=None)
                        elif returnValue =="com_26":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia601508.us.archive.org/7/items/iptvworld-1/IPTVWORLD26.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='Free IPTVFree026', cmdlist=cmdlist, finishedCallback=None)
                        elif returnValue =="com_27":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia601508.us.archive.org/7/items/iptvworld-1/IPTVWORLD27.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='Free IPTVFree027', cmdlist=cmdlist, finishedCallback=None)
                        elif returnValue =="com_28":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia601508.us.archive.org/7/items/iptvworld-1/IPTVWORLD28.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='Free IPTVFree028', cmdlist=cmdlist, finishedCallback=None)
                        elif returnValue =="com_29":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia601508.us.archive.org/7/items/iptvworld-1/IPTVWORLD29.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='Free IPTVFree029', cmdlist=cmdlist, finishedCallback=None)
                        elif returnValue =="com_30":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia601508.us.archive.org/7/items/iptvworld-1/IPTVWORLD30.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='Free IPTVFree030', cmdlist=cmdlist, finishedCallback=None)
                        elif returnValue =="com_31":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia601508.us.archive.org/7/items/iptvworld-1/IPTVWORLD31.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='Free IPTVFree031', cmdlist=cmdlist, finishedCallback=None)
                        elif returnValue =="com_32":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia601508.us.archive.org/7/items/iptvworld-1/IPTVWORLD32.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='Free IPTVFree032', cmdlist=cmdlist, finishedCallback=None)
                        elif returnValue =="com_33":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia601508.us.archive.org/7/items/iptvworld-1/IPTVWORLD33.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='Free IPTVFree033', cmdlist=cmdlist, finishedCallback=None)
                        elif returnValue =="com_34":
                                #cmdlist = []
                                #cmdlist.append("%s -qO - '" % self.wget + "'")
                                #cmdlist.append("%s https://ia601508.us.archive.org/7/items/iptvworld-1/IPTVWORLD34.sh -qO - | /bin/sh" % self.wget)
                                #self.session.open(Console3, title='Free IPTVFree034', cmdlist=cmdlist, finishedCallback=None)
                                self.session.open(myInput3)
                        elif returnValue =="com_35":
                                #cmdlist = []
                                #cmdlist.append("%s -qO - '" % self.wget + "'")
                                #cmdlist.append("%s https://ia601508.us.archive.org/7/items/iptvworld-1/IPTVWORLD35.sh -qO - | /bin/sh" % self.wget)
                                #self.session.open(Console3, title='Free IPTVFree035', cmdlist=cmdlist, finishedCallback=None)
                                self.session.open(myInput4)
                        elif returnValue =="com_36":
                                #cmdlist = []
                                #cmdlist.append("%s -qO - '" % self.wget + "'")
                                #cmdlist.append("%s https://ia601508.us.archive.org/7/items/iptvworld-1/IPTVWORLD36.sh -qO - | /bin/sh" % self.wget)
                                #self.session.open(Console3, title='Free IPTVFree036', cmdlist=cmdlist, finishedCallback=None)
                                self.session.open(myInput5)
                        elif returnValue =="com_37":
                                #cmdlist = []
                                #cmdlist.append("%s -qO - '" % self.wget + "'")
                                #cmdlist.append("%s https://ia601508.us.archive.org/7/items/iptvworld-1/IPTVWORLD37.sh -qO - | /bin/sh" % self.wget)
                                #self.session.open(Console3, title='Free IPTVFree037', cmdlist=cmdlist, finishedCallback=None)
                                self.session.open(myInput6)                        
                        elif returnValue =="com_38":
                                #cmdlist = []
                                #cmdlist.append("%s -qO - '" % self.wget + "'")
                                #cmdlist.append("%s https://ia601508.us.archive.org/7/items/iptvworld-1/IPTVWORLD38.sh -qO - | /bin/sh" % self.wget)
                                #self.session.open(Console3, title='Free IPTVFree038', cmdlist=cmdlist, finishedCallback=None)
                                self.session.open(myInput7)
                        elif returnValue =="com_39":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia601508.us.archive.org/7/items/iptvworld-1/IPTVWORLD39.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='Free IPTVFree039', cmdlist=cmdlist, finishedCallback=None)
                        elif returnValue =="com_40":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia601508.us.archive.org/7/items/iptvworld-1/IPTVWORLD40.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='Free IPTVFree040', cmdlist=cmdlist, finishedCallback=None)
                        elif returnValue =="com_41":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia601508.us.archive.org/7/items/iptvworld-1/IPTVWORLD41.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='Free IPTVFree041', cmdlist=cmdlist, finishedCallback=None)
                        elif returnValue =="com_42":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia601508.us.archive.org/7/items/iptvworld-1/IPTVWORLD42.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='Free IPTVFree042', cmdlist=cmdlist, finishedCallback=None)
                        elif returnValue =="com_43":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia601508.us.archive.org/7/items/iptvworld-1/IPTVWORLD43.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='Free IPTVFree043', cmdlist=cmdlist, finishedCallback=None)
                        elif returnValue =="com_44":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia601508.us.archive.org/7/items/iptvworld-1/IPTVWORLD44.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='Free IPTVFree044', cmdlist=cmdlist, finishedCallback=None)
                        elif returnValue =="com_45":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia601508.us.archive.org/7/items/iptvworld-1/IPTVWORLD45.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='Free IPTVFree045', cmdlist=cmdlist, finishedCallback=None)
                                #self.session.open(myInput)
                        elif returnValue =="com_46":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia601508.us.archive.org/7/items/iptvworld-1/IPTVWORLD46.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='Free IPTVFree046', cmdlist=cmdlist, finishedCallback=None)
                        elif returnValue =="com_47":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia601508.us.archive.org/7/items/iptvworld-1/IPTVWORLD47.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='Free IPTVFree047', cmdlist=cmdlist, finishedCallback=None)
                        elif returnValue =="com_48":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia601508.us.archive.org/7/items/iptvworld-1/IPTVWORLD48.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='Free IPTVFree048', cmdlist=cmdlist, finishedCallback=None)
                        elif returnValue =="com_49":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia601508.us.archive.org/7/items/iptvworld-1/IPTVWORLD49.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='Free IPTVFree049', cmdlist=cmdlist, finishedCallback=None)
                        elif returnValue =="com_50":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia601508.us.archive.org/7/items/iptvworld-1/IPTVWORLD50.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='Free IPTVFree050', cmdlist=cmdlist, finishedCallback=None)
                        elif returnValue =="com_51":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia601508.us.archive.org/7/items/iptvworld-1/IPTVWORLD51.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='Free IPTVFree051', cmdlist=cmdlist, finishedCallback=None)
                        elif returnValue =="com_52":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia601508.us.archive.org/7/items/iptvworld-1/IPTVWORLD52.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='Free IPTVFree052', cmdlist=cmdlist, finishedCallback=None)
                        elif returnValue =="com_53":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia601508.us.archive.org/7/items/iptvworld-1/IPTVWORLD53.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='Free IPTVFree053', cmdlist=cmdlist, finishedCallback=None)
                        elif returnValue =="com_54":
                                #cmdlist = []
                                #cmdlist.append("%s -qO - '" % self.wget + "'")
                                #cmdlist.append("%s https://ia601508.us.archive.org/7/items/iptvworld-1/IPTVWORLD54.sh -qO - | /bin/sh" % self.wget)
                                #self.session.open(Console3, title='Free IPTVFree054', cmdlist=cmdlist, finishedCallback=None)
                                self.session.open(myInput2)
                        elif returnValue =="com_55":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia601508.us.archive.org/7/items/iptvworld-1/IPTVWORLD55.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='Free IPTVFree055', cmdlist=cmdlist, finishedCallback=None)
                        elif returnValue =="com_56":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia601508.us.archive.org/7/items/iptvworld-1/IPTVWORLD56.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='Free IPTVFree056', cmdlist=cmdlist, finishedCallback=None)
                        elif returnValue =="com_57":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia601508.us.archive.org/7/items/iptvworld-1/IPTVWORLD57.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='Free IPTVFree057', cmdlist=cmdlist, finishedCallback=None)
                        elif returnValue =="com_58":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia601508.us.archive.org/7/items/iptvworld-1/IPTVWORLD58.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='Free IPTVFree058', cmdlist=cmdlist, finishedCallback=None)
                        elif returnValue =="com_59":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia601508.us.archive.org/7/items/iptvworld-1/IPTVWORLD59.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='Free IPTVFree059', cmdlist=cmdlist, finishedCallback=None)
                        elif returnValue =="com_60":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia601508.us.archive.org/7/items/iptvworld-1/IPTVWORLD60.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='Free IPTVFree060', cmdlist=cmdlist, finishedCallback=None)
                        elif returnValue =="com_61":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia601508.us.archive.org/7/items/iptvworld-1/IPTVWORLD61.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='Free IPTVFree061', cmdlist=cmdlist, finishedCallback=None)
                        elif returnValue =="com_62":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia601508.us.archive.org/7/items/iptvworld-1/IPTVWORLD62.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='Free IPTVFree062', cmdlist=cmdlist, finishedCallback=None)
                        elif returnValue =="com_63":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia601508.us.archive.org/7/items/iptvworld-1/IPTVWORLD63.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='Free IPTVFree063', cmdlist=cmdlist, finishedCallback=None)
                        elif returnValue =="com_64":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'") 
                                cmdlist.append("%s https://ia601508.us.archive.org/7/items/iptvworld-1/IPTVWORLD64.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='Free IPTVFree064', cmdlist=cmdlist, finishedCallback=None)
                        elif returnValue =="com_65":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia601508.us.archive.org/7/items/iptvworld-1/IPTVWORLD65.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='Free IPTVFree065', cmdlist=cmdlist, finishedCallback=None)
                        elif returnValue =="com_66":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia601508.us.archive.org/7/items/iptvworld-1/IPTVWORLD66.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='Free IPTVFree066', cmdlist=cmdlist, finishedCallback=None)
                        elif returnValue =="com_67":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia601508.us.archive.org/7/items/iptvworld-1/IPTVWORLD67.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='Free IPTVFree067', cmdlist=cmdlist, finishedCallback=None)
                        elif returnValue =="com_68":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")    
                                cmdlist.append("%s https://ia601508.us.archive.org/7/items/iptvworld-1/IPTVWORLD68.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='Free IPTVFree068', cmdlist=cmdlist, finishedCallback=None)
                        elif returnValue =="com_69":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia601508.us.archive.org/7/items/iptvworld-1/IPTVWORLD69.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='Free IPTVFree069', cmdlist=cmdlist, finishedCallback=None)
                        elif returnValue =="com_70":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia601508.us.archive.org/7/items/iptvworld-1/IPTVWORLD70.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='Free IPTVFree070', cmdlist=cmdlist, finishedCallback=None)
                        elif returnValue =="com_71":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia601508.us.archive.org/7/items/iptvworld-1/IPTVWORLD71.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='Free IPTVFree071', cmdlist=cmdlist, finishedCallback=None)
                        elif returnValue =="com_72":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia601508.us.archive.org/7/items/iptvworld-1/IPTVWORLD72.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='Free IPTVFree072', cmdlist=cmdlist, finishedCallback=None)
                        elif returnValue =="com_73":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia601508.us.archive.org/7/items/iptvworld-1/IPTVWORLD73.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='Free IPTVFree073', cmdlist=cmdlist, finishedCallback=None)
                        elif returnValue =="com_74":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'") 
                                cmdlist.append("%s https://ia601508.us.archive.org/7/items/iptvworld-1/IPTVWORLD74.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='Free IPTVFree074', cmdlist=cmdlist, finishedCallback=None)
                        elif returnValue =="com_75":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia601508.us.archive.org/7/items/iptvworld-1/IPTVWORLD75.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='Free IPTVFree075', cmdlist=cmdlist, finishedCallback=None)
                        elif returnValue =="com_76":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia601508.us.archive.org/7/items/iptvworld-1/IPTVWORLD76.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='Free IPTVFree076', cmdlist=cmdlist, finishedCallback=None)
                        elif returnValue =="com_77":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia601508.us.archive.org/7/items/iptvworld-1/IPTVWORLD77.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='Free IPTVFree077', cmdlist=cmdlist, finishedCallback=None)
                        elif returnValue =="com_78":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")    
                                cmdlist.append("%s https://ia601508.us.archive.org/7/items/iptvworld-1/IPTVWORLD78.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='Free IPTVFree078', cmdlist=cmdlist, finishedCallback=None)
                        elif returnValue =="com_79":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia601508.us.archive.org/7/items/iptvworld-1/IPTVWORLD79.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='Free IPTVFree079', cmdlist=cmdlist, finishedCallback=None)
                        elif returnValue =="com_80":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia601508.us.archive.org/7/items/iptvworld-1/IPTVWORLD80.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='Free IPTVFree080', cmdlist=cmdlist, finishedCallback=None)
                        elif returnValue =="com_81":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia601508.us.archive.org/7/items/iptvworld-1/IPTVWORLD81.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='Free IPTVFree081', cmdlist=cmdlist, finishedCallback=None)
                        elif returnValue =="com_82":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia601508.us.archive.org/7/items/iptvworld-1/IPTVWORLD82.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='Free IPTVFree082', cmdlist=cmdlist, finishedCallback=None)
                        elif returnValue =="com_83":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia601508.us.archive.org/7/items/iptvworld-1/IPTVWORLD83.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='Free IPTVFree083', cmdlist=cmdlist, finishedCallback=None)
                        elif returnValue =="com_84":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia601508.us.archive.org/7/items/iptvworld-1/IPTVWORLD84.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='Free IPTVFree084', cmdlist=cmdlist, finishedCallback=None)
                        elif returnValue =="com_85":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia601508.us.archive.org/7/items/iptvworld-1/IPTVWORLD85.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='Free IPTVFree085', cmdlist=cmdlist, finishedCallback=None)
                        elif returnValue =="com_86":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia601508.us.archive.org/7/items/iptvworld-1/IPTVWORLD86.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='Free IPTVFree086', cmdlist=cmdlist, finishedCallback=None)
                        elif returnValue =="com_87":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia601508.us.archive.org/7/items/iptvworld-1/IPTVWORLD87.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='Free IPTVFree087', cmdlist=cmdlist, finishedCallback=None)
                        elif returnValue =="com_88":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia601508.us.archive.org/7/items/iptvworld-1/IPTVWORLD88.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='Free IPTVFree088', cmdlist=cmdlist, finishedCallback=None)
                        elif returnValue =="com_89":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia601508.us.archive.org/7/items/iptvworld-1/IPTVWORLD89.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='Free IPTVFree089', cmdlist=cmdlist, finishedCallback=None)
                        elif returnValue =="com_90":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%shttps://ia601508.us.archive.org/7/items/iptvworld-1/IPTVWORLD90.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='Free IPTVFree090', cmdlist=cmdlist, finishedCallback=None)
                        elif returnValue =="com_91":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia601508.us.archive.org/7/items/iptvworld-1/IPTVWORLD91.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='Free IPTVFree091', cmdlist=cmdlist, finishedCallback=None)
                        elif returnValue =="com_92":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia601508.us.archive.org/7/items/iptvworld-1/IPTVWORLD92.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='Free IPTVFree092', cmdlist=cmdlist, finishedCallback=None)
                        elif returnValue =="com_93":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia601508.us.archive.org/7/items/iptvworld-1/IPTVWORLD93.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='Free IPTVFree093', cmdlist=cmdlist, finishedCallback=None)
                        elif returnValue =="com_94":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia601508.us.archive.org/7/items/iptvworld-1/IPTVWORLD94.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='Free IPTVFree094', cmdlist=cmdlist, finishedCallback=None)
                        elif returnValue =="com_95":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia601508.us.archive.org/7/items/iptvworld-1/IPTVWORLD95.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='Free IPTVFree095', cmdlist=cmdlist, finishedCallback=None)
                        elif returnValue =="com_96":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia601508.us.archive.org/7/items/iptvworld-1/IPTVWORLD96.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='Free IPTVFree096', cmdlist=cmdlist, finishedCallback=None)
                        elif returnValue =="com_97":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia601508.us.archive.org/7/items/iptvworld-1/IPTVWORLD97.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='Free IPTVFree097', cmdlist=cmdlist, finishedCallback=None)
                        elif returnValue =="com_98":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia601508.us.archive.org/7/items/iptvworld-1/IPTVWORLD98.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='Free IPTVFree098', cmdlist=cmdlist, finishedCallback=None)
                        elif returnValue =="com_99":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia601508.us.archive.org/7/items/iptvworld-1/IPTVWORLD99.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='Free IPTVFree099', cmdlist=cmdlist, finishedCallback=None)
                        elif returnValue =="com_100":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia601508.us.archive.org/7/items/iptvworld-1/IPTVWORLD100.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='Free IPTVFree100', cmdlist=cmdlist, finishedCallback=None)
                        else:
                                print("\n[MyShPrombt] cancel\n")
                                self.close(None)

        def Update(self):
            Update = "afile"
            afile = open('/tmp/monfichier.txt', 'w')
            self.session.openWithCallback(self.restartenigma, MessageBox, _('Free Server V_' + str(Update) + '\nRestart Enigma2 To Load New Settings?'), MessageBox.TYPE_YESNO)


        #def goto(self):
            #self.session.openWithCallback(self.restartenigma, MessageBox, _('Restart Enigma2 To Load New Update?'), MessageBox.TYPE_YESNO, timeout=20)

        def restartenigma(self, result):
            if result:
                self.session.open(TryQuitMainloop, 3)
                
        def myInput(self):
            self.session.open(myInput)   

        #def gotoa(self):
            #cmdlist = []
### EDit By RAED To DreamOS OE2.5/2.6
            #cmdlist.append("%s -qO - '" % self.wget + "'")
            #cmdlist.append("%s https://ia903000.us.archive.org/30/items/FreeServerinfo/free4k.sh -qO - | /bin/sh" % self.wget)
            #self.session.open(Console3, title='Update links Bein Sport', cmdlist=cmdlist, finishedCallback=None)

        #def Clean(self):
            #tmp = os.system("echo $(ls -sh /tmp | grep 'total' | sed 's/total '//) > /tmp/volume")            
            #if os.path.exists('/tmp/volume'):
                #f = open('/tmp/volume', 'r')
                #for line in f.readlines():
                        #id = line.strip('\n')
               #os.system("rm -rf /tmp/*")
                #self.session.open.(self.restart, MessageBox, _('Job Finish.\n\n ' + (id) + ' tmp is clean.'), MessageBox.TYPE_YESNO)

                #retval = self.container.execute("echo $(df -h /tmp | tail -1 | awk '{print $2}') > /tmp/volume && echo Available:   $(df -h /tmp | tail -1 | awk '{print $2}') >> /tmp/volume && echo Use  echo $(df -h /tmp | tail -1 | awk '{print $4}' >> /tmp/volume")                

        def Clean(self):
            self.container = eConsoleAppContainer()
            retval = self.container.execute("echo $(df -h /tmp | tail -1 | awk '{print $2}') > /tmp/volume && echo $(df -h /tmp | tail -1 | awk '{print $3}') > /tmp/volume2 && echo $(df -h /tmp | tail -1 | awk '{print $4}') > /tmp/volume3 && echo $(df -h /tmp | tail -1 | awk '{print $5}') > /tmp/volume4")                
            if os.path.exists('/tmp/volume'):
               f = open('/tmp/volume', 'r')
               for line in f.readlines():
                   id = line.strip('\n')
            if os.path.exists('/tmp/volume2'):
               f = open('/tmp/volume2', 'r')
               for line in f.readlines():
                   id2 = line.strip('\n')
            if os.path.exists('/tmp/volume3'):
               f = open('/tmp/volume3', 'r')
               for line in f.readlines():
                   id3 = line.strip('\n')
            if os.path.exists('/tmp/volume4'):
               f = open('/tmp/volume4', 'r')
               for line in f.readlines():
                   id4 = line.strip('\n')
               self.session.openWithCallback(self.doclean, MessageBox, _('End of the task.\nDo you really want to Delete all temporary file storage in /tmp files ?\nSize: ' + (id) + '\nUsed ' + (id2) + '\nAvailable: ' + (id3) + '\nUsed% ' + (id4) + '\n'),  MessageBox.TYPE_YESNO)

        def doclean(self, answer=False):
            if answer:
                os.system("rm -rf /tmp/*")
            else:
                return  
                
        def AUTOUPD(self):
            cmdlist = []
            cmdlist.append("%s -qO - '" % self.wget + "'")
            cmdlist.append("%s https://ia903000.us.archive.org/30/items/FreeServerinfo/Auto_update_Freeiptv.sh -qO - | /bin/sh" % self.wget)
            self.session.open(Console3, title='AUTO Update links Bein Sport RMC', cmdlist=cmdlist, finishedCallback=None)
        def prombt(self, com):
            scripts = "/usr/lib/enigma2/python/Plugins/Extensions/FreeServer/scripts/"
            os.chmod(scripts, 755)
            self.session.open(Console3,_("Executing: %s") % (com), ["%s" % com])
        def cancel(self):
            self.close(None)
