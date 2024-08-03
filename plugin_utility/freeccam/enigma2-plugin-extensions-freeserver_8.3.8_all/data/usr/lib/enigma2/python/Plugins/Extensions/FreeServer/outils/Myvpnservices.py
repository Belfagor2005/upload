# -*- coding: UTF-8 -*-
from __future__ import print_function

from Plugins.Plugin import PluginDescriptor
from os import path as os_path, remove, unlink, rename, chmod, access, X_OK
from shutil import move
from Screens.Screen import Screen
from datetime import date, datetime
from Components.Label import Label
from Components.Sources.StaticText import StaticText
from enigma import eTimer, eConsoleAppContainer
from Screens.MessageBox import MessageBox
from Screens.Standby import TryQuitMainloop
from Components.Console import Console
from Components.MenuList import MenuList
from Components.ActionMap import ActionMap
from Components.MediaPlayer import *
from enigma import *
from Screens.MessageBox import MessageBox
from Components.Pixmap import Pixmap  
from Tools.Directories import fileExists, pathExists
from Components.GUIComponent import *
from Screens.ServiceInfo import *
from Components.config import *
from enigma import eServiceReference
from Tools.Directories import fileExists
from time import *
from Plugins.Extensions.FreeServer.outils.compat import compat_urlopen
import requests , json, re,string,time
from enigma import eTimer, getDesktop
from enigma import *
import os, sys, re
import shutil
#import urllib
import base64
#session = None
#data_xml = 'aHR0cHM6Ly9pYTYwMDcwMi51cy5hcmNoaXZlLm9yZy8yNi9pdGVtcy9kcmVhbW9zYXQvY2Ftc3RhcnQwLnR4dA=='
#xml_path = base64.b64decode(data_xml)
#version = '7710'    
#currversion = '7710'   
###################################################################################################### 
s = requests.Session()
#https://www.logitheque.com/wp-content/uploads/sites/4/2020/09/how-set-up-iptv-smarters-pro-1024x576.jpg
######################################################################################################
LINKFILE1= '/tmp/ip'
LINKFILE2= '/tmp/ip2'
WGET='wget --no-check-certificate'
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
    
def connected_to_internet():   
    try:
        _ = requests.get('https://github.com', timeout=3)
        return True
    except :
        return False
        
#########################################################################################################
class Myvpnservices(Screen):
#### Edit By RAED
        if not isHD():
            skin = """
                      <screen position="0,0" size="1916,1080" title="Schedule to football matchs this week" backgroundColor="#16000000" flags="wfNoBorder">             
                      <widget source="Title" render="Label" position="12,7" size="600,32" font="Play;28" backgroundColor="#16000000" foregroundColor="#FFE375" valign="center" halign="center" zPosition="2"/>
                      <eLabel text="Move Up/Down or Left/Right to move list/page" position="600,7" size="680,32" font="Play;28" foregroundColor="#FC0000" backgroundColor="#16000000" zPosition="2"/>           
                      <widget name="myMenu" position="17,52" size="754,1014" foregroundColor="#FEFEFE" transparent="1" zPosition="2"/>
                      <ePixmap position="0,0" size="1916,1080" pixmap="/usr/lib/enigma2/python/Plugins/Extensions/FreeServer/Deco/SLIDE_02.jpg" alphatest="blend" transparent="1" />
                      </screen>"""
        else:
                skin = """
                      <screen position="0,0" size="1280,720" title="Schedule to football matchs this week" backgroundColor="#16000000" flags="wfNoBorder">              
                      <widget source="Title" render="Label" position="12,7" size="600,32" font="Play;28" backgroundColor="#16000000" foregroundColor="#FFE375" valign="center" halign="center" zPosition="2"/>
                      <eLabel text="Move Up/Down or Left/Right to move list/page" position="600,7" size="680,32" font="Play;28" foregroundColor="#FC0000" backgroundColor="#16000000" zPosition="2"/>           
                      <widget name="myMenu" position="12,51" size="735,662" foregroundColor="#FEFEFE" transparent="1" zPosition="2"/>
                      <ePixmap position="0,0" size="1280,720" pixmap="/usr/lib/enigma2/python/Plugins/Extensions/FreeServer/Deco/SLIDE_02.jpg" alphatest="blend" transparent="1" />
                      </screen>"""
        
        def __init__(self, session, finishedCallback = None, picPath = None, args = 0):
                self.session = session
                Screen.__init__(self, session)
                self.finishedCallback = finishedCallback
                self.setTitle("List of VPN server avilable")
                self.wget = "wget --no-check-certificate"
                list = [] 
                list.append(("        Download Cert. Files", "com_01"))                         
                list.append(("        QUEBEC 910", "com_1"))
                list.append(("        MONTREAL 694", "com_2"))  
                list.append(("        BEAUHAMOIS 123", "com_3"))
                list.append(("        CANADA 121", "com_4")) 
                list.append(("        VIRGINIA 240", "com_5"))
                list.append(("        NEW YORK 184", "com_6"))             
                list.append(("        NUREMBURG 851", "com_7"))
                list.append(("        MISSOURI 473", "com_8"))          
                list.append(("        EUROPE 230", "com_9"))
                list.append(("        ATLANTA 118", "com_10"))
                list.append(("        NEW JERSEY 120", "com_11"))
                list.append(("        SEATTLE 521", "com_12"))  
                list.append(("        CHICAGO 155", "com_13"))
                list.append(("        DALLAS 938", "com_14"))
                list.append(("        LONDON 103", "com_15"))                         
                list.append(("        PARIS 221", "com_16"))            
                list.append(("        LOS ANGELES 691", "com_17"))
                list.append(("        MIAMI 149", "com_18")) 
                list.append(("        TORONTO 160", "com_19"))                                  
                list.append(("        CHICAGO 132+", "com_20"))
                list.append(("        Sydney", "com_21"))
                list.append(("        LONDON 3000", "com_022"))            
                list.append(("        UK LONDON 136", "com_023"))
                list.append(("        FRANCE 165", "com_024")) 
                list.append(("        CHICAGO (High Speed)", "com_025"))                                  
                list.append(("        NY / NJ (High Speed)", "com_026"))
                list.append(("        MIAMI (High Speed)", "com_027"))
                list.append(("        Download Openvpn Config udp_123 tcp_80", "com_02"))
                list.append(("        Buenos Aires, Argentina", "com_22"))    
                list.append(("        Sydney 2, Australia", "com_23"))    
                list.append(("        Sydney, Australia", "com_24"))      
                list.append(("        Brussels, Belgium", "com_25"))    
                list.append(("        Sofia, Bulgaria", "com_26"))      
                list.append(("        Sao Paulo, Brazil", "com_27"))     
                list.append(("        Toronto, Canada", "com_28"))    
                list.append(("        Montreal, Canada", "com_29"))  
                list.append(("        Vancouver, Canada", "com_30"))       
                list.append(("        Zurich, Switzerland", "com_31"))   
                list.append(("        Prague, Czech Republic", "com_32"))  
                list.append(("        Frankfurt, Germany", "com_33"))       
                list.append(("        Dusseldorf, Germany", "com_34"))     
                list.append(("        Seville, Spain", "com_35"))    
                list.append(("        Barcelona, Spain", "com_36"))        
                list.append(("        Helsinki, Finland", "com_37"))       
                list.append(("        Helsinki 2, Finland", "com_38"))     
                list.append(("        Paris, France", "com_39"))     
                list.append(("        London, United Kingdom", "com_40"))         
                list.append(("        London 2, United Kingdom", "com_41"))         
                list.append(("        Thessaloniki, Greece", "com_42"))         
                list.append(("        Hong Kong, Hong Kong", "com_43"))         
                list.append(("        Jakarta 6, Indonesia", "com_44"))      
                list.append(("        Jakarta 5, Indonesia", "com_45"))     
                list.append(("        Dublin, Ireland", "com_46"))        
                list.append(("        Tel Aviv, Israel", "com_47"))       
                list.append(("        Mumbai, India", "com_48"))         
                list.append(("        Palermo, Italy", "com_49"))       
                list.append(("        Tokyo 6, Japan", "com_50"))       
                list.append(("        Tokyo 2, Japan", "com_51"))       
                list.append(("        Tokyo, Japan", "com_52"))       
                list.append(("        Rotterdam, Netherlands", "com_53"))  
                list.append(("        Amsterdam, Netherlands", "com_54"))       
                list.append(("        Manila, Philippines", "com_55"))    
                list.append(("        Warsaw, Poland", "com_56"))   
                list.append(("        Bucharest, Romania", "com_57"))    
                list.append(("        St Petersburg, Russian Federation", "com_58"))       
                list.append(("        Moscow, Russian Federation", "com_59"))         
                list.append(("        Stockholm, Sweden", "com_60"))  
                list.append(("        Singapore, Singapore", "com_61"))    
                list.append(("        Singapore, Singapore", "com_62"))        
                list.append(("        Ljubljana, Slovenia", "com_63"))  
                list.append(("        Bangkok, Thailand", "com_64")) 
                list.append(("        Bursa, Turkey", "com_65"))         
                list.append(("        Bursa 2, Turkey", "com_66"))   
                list.append(("        Kiev, Ukraine", "com_67"))         
                list.append(("        Miami, United States", "com_68"))       
                list.append(("        Los Angeles, United States", "com_69"))         
                list.append(("        New York City, United States", "com_70"))
                list.append(("        Miami 2, United States", "com_71"))  
                list.append(("        Miami 3, United States", "com_72"))
                list.append(("        New York City 2, United States", "com_73")) 
                list.append(("        Johannesburg 2, South Africa", "com_74"))    
                list.append(("        Johannesburg, South Africa", "com_75")) 
                list.append(("        udp_123", "com_***"))      
                list.append(("        Buenos Aires, Argentina", "com_76"))    
                list.append(("        Sydney 2, Australia", "com_77"))    
                list.append(("        Sydney, Australia", "com_78"))      
                list.append(("        Brussels, Belgium", "com_79"))    
                list.append(("        Sofia, Bulgaria", "com_80"))      
                list.append(("        Sao Paulo, Brazil", "com_81"))     
                list.append(("        Toronto, Canada", "com_82"))    
                list.append(("        Montreal, Canada", "com_83"))  
                list.append(("        Vancouver, Canada", "com_84"))       
                list.append(("        Zurich, Switzerland", "com_85"))   
                list.append(("        Prague, Czech Republic", "com_86"))  
                list.append(("        Frankfurt, Germany", "com_87"))       
                list.append(("        Dusseldorf, Germany", "com_88"))     
                list.append(("        Seville, Spain", "com_89"))    
                list.append(("        Barcelona, Spain", "com_90"))        
                list.append(("        Helsinki, Finland", "com_91"))       
                list.append(("        Helsinki 2, Finland", "com_92"))     
                list.append(("        Paris, France", "com_93"))     
                list.append(("        London, United Kingdom", "com_94"))         
                list.append(("        London 2, United Kingdom", "com_95"))         
                list.append(("        Thessaloniki, Greece", "com_96"))         
                list.append(("        Hong Kong, Hong Kong", "com_97"))         
                list.append(("        Jakarta 6, Indonesia", "com_98"))      
                list.append(("        Jakarta 5, Indonesia", "com_99"))     
                list.append(("        Dublin, Ireland", "com_100"))        
                list.append(("        Tel Aviv, Israel", "com_101"))       
                list.append(("        Mumbai, India", "com_102"))         
                list.append(("        Palermo, Italy", "com_103"))       
                list.append(("        Tokyo 6, Japan", "com_104"))       
                list.append(("        Tokyo 2, Japan", "com_105"))       
                list.append(("        Tokyo, Japan", "com_106"))       
                list.append(("        Rotterdam, Netherlands", "com_107"))  
                list.append(("        Amsterdam, Netherlands", "com_108"))       
                list.append(("        Manila, Philippines", "com_109"))    
                list.append(("        Warsaw, Poland", "com_110"))   
                list.append(("        Bucharest, Romania", "com_111"))    
                list.append(("        St Petersburg, Russian Federation", "com_112"))       
                list.append(("        Moscow, Russian Federation", "com_113"))         
                list.append(("        Stockholm, Sweden", "com_114"))  
                list.append(("        Singapore, Singapore", "com_115"))    
                list.append(("        Singapore, Singapore", "com_116"))        
                list.append(("        Ljubljana, Slovenia", "com_117"))
                list.append(("        Bangkok, Thailand", "com_118"))                        
                list.append(("        Bursa, Turkey", "com_119"))         
                list.append(("        Bursa 2, Turkey", "com_120"))   
                list.append(("        Kiev, Ukraine", "com_121"))         
                list.append(("        Miami, United States", "com_122"))       
                list.append(("        Los Angeles, United States", "com_123"))         
                list.append(("        New York City, United States", "com_124"))
                list.append(("        Los Angeles, United States", "com_125")) 
                list.append(("        Miami 3, United States", "com_126"))
                list.append(("        New York City2, United States", "com_127"))    
                list.append(("        Johannesburg 2, South Africa", "com_128"))    
                list.append(("        Johannesburg, South Africa", "com_129")) 
                list.append(("        Download Cert. Files 7 days", "com_03")) 
                list.append(("        Ashburn", "com_130"))   
                list.append(("        Bangalore", "com_121"))         
                list.append(("        Frankfurt", "com_132"))       
                list.append(("        London", "com_133"))         
                list.append(("        New York City, United States", "com_134"))
                list.append(("        Singapore", "com_135"))    
                list.append(("        Singapore2", "com_136"))    
                list.append(("        Toronto", "com_137")) 
                list.append(("        Download Cert. Files 01 day", "com_04"))
                list.append(("        USA Vint Hill VA (2Gbit)", "com_138"))   
                list.append(("        USA Hillsboro OR (2Gbit)", "com_139"))         
                list.append(("        CAN Vancouver BC (1Gbit)", "com_140"))       
                list.append(("        Sydney AU (1Gbit)", "com_141"))         
                list.append(("        Sofia BG (1Gbit)", "com_142"))
                list.append(("        Singapore SG (1Gbit)", "com_143"))    
                list.append(("        USA Piscataway NJ (10Gbit)", "com_144"))    
                list.append(("        USA Pheonix AZ (1Gbit)", "com_145"))
                list.append(("        Bucharest RO (1Gbit)", "com_146"))
                list.append(("        Oslo NO (1Gbit)", "com_147"))    
                list.append(("        North Holland NL (10Gbit)", "com_148"))    
                list.append(("        CAN Montreal QC (1Gbit)", "com_149"))
                list.append(("        USA Miami FL (10Gbit)", "com_150"))   
                list.append(("        Madrid ES (1Gbit)", "com_151"))         
                list.append(("        USA Los Angels CA (10Gbit)", "com_152"))       
                list.append(("        USA New York NY (10Gbit)", "com_153"))         
                list.append(("        USA Las Vegas NV (1Gbit)", "com_154"))
                list.append(("        USA Kansas City MO (1Gbit)", "com_155"))    
                list.append(("        Hong Kong HK (1Gbit)", "com_156"))    
                list.append(("        Helsinki FI (1Gbit)", "com_157"))
                list.append(("        Florence IT (1Gbit)", "com_158"))
                list.append(("        Dusseldorf DE (1Gbit)", "com_159"))    
                list.append(("        USA Dallas TX (1Gbit)", "com_160"))    
                list.append(("        USA Ashburn VA (1Gbit)", "com_161"))                
                list.append(("        USA Chicago IL (10Gbit)", "com_162"))   
                list.append(("        Brussels BE (1Gbit)", "com_163"))         
                list.append(("        USA Atlanta GA (1Gbit)", "com_164"))       
                list.append(("        USA Detroit MI (1Gbit)", "com_165"))         
                list.append(("        Stockholm SE (1Gbit)", "com_166"))
                list.append(("        USA Colorado Springs CO (10Gbit)", "com_167"))    
                list.append(("        London GB (10Gbit)", "com_168"))    
                list.append(("        USA Seattle WA (1Gbit)", "com_169"))
                list.append(("        Paris FR (1Gbit)", "com_170"))
                list.append(("        USA Seattle WA (1Gbit)", "com_171"))
                list.append(("        Paris FR (1Gbit)", "com_172"))
                list.append(("        Find My Ip", "com_173"))
                list.append(("        VPN_Stop", "com_174"))
                list.append(("        VPN Start", "com_175"))
                list.append(("        VPN Auto Start-up", "com_176"))
                list.append((_("        Exit"), "exit"))
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
                        #'yellow': self.goto,
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

        #def update(self):
                #try:
                    #fp = urllib.urlopen(xml_path)
                    #count = 0
                    #self.labeltext = ''
                    #s1 = fp.readline()
                    #s2 = fp.readline()
                    #s3 = fp.readline()
                    #s1 = s1.strip()
                    #s2 = s2.strip()
                    #s3 = s3.strip()
                    #self.link = s2
                    #self.version = s1
                    #self.info = s3
                    #fp.close()
                    #cstr = s1 + ' ' + s2
                    #if s1 <= currversion:
                        #return
                        #print('[No Update Avilable]')
                    #else:  
                        #self.session.openWithCallback(self.install, MessageBox, _('New update available.\n\nDo you want ot install now.'), MessageBox.TYPE_YESNO)
                        #print('[New Update Avilable]')
                #except:
                    #return '[New Update Avilable]'

        #def install(self, *retval):
            #os.system("%s https://ia600702.us.archive.org/26/items/dreamosat/freecc4.sh -qO - | /bin/sh" % self.wget)
            #self.session.openWithCallback(self.restartenigma, MessageBox, _('** Nedd Restart Enigma2 To Load New Update ?!! **'), MessageBox.TYPE_YESNO, timeout=10)


               
### End EDit
        def go(self):
                from Plugins.Extensions.FreeServer.outils.Console3 import Console3
                returnValue = self["myMenu"].l.getCurrentSelection()[1]
                if returnValue != None:         
                        if returnValue =="com_01":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia801406.us.archive.org/25/items/iptvworld-24/IPTVWORLDVPN.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='Free VPN', cmdlist=cmdlist, finishedCallback=None)
                        elif returnValue =="com_1":
                            if connected_to_internet():
                               os.system('/etc/init.d/openvpn stop > /dev/null 2>&1')
                               os.system('rm -r %s > /dev/null 2>&1 && rm -f %s > /dev/null 2>&1' % (LINKFILE1, LINKFILE2))
                               os.system('rm -r -f /etc/openvpn; mkdir /etc/openvpn') 
                               shutil.copyfile('/etc/cfg_conf', '/etc/openvpn/cfg.conf')
                               shutil.copyfile('/etc/vpnsolution/client_conf1', '/etc/openvpn/client.conf')
                               ip = compat_urlopen("http://ip.42.pl/raw").read()  
                               with open(LINKFILE1, "wb") as f: f.write(ip)                                   
                               f = open(LINKFILE1, 'r')
                               for line in f.readlines():
                                   IP = line.strip('\n')
                                   os.system('/etc/init.d/openvpn start > /dev/null 2>&1')
                                   time.sleep(8)
                                   ip2 = compat_urlopen("http://ip.42.pl/raw").read()  
                                   with open(LINKFILE2, "wb") as f: f.write(ip2)                                       
                                   f = open(LINKFILE2, 'r')
                                   for line in f.readlines():
                                       IP2 = line.strip('\n')
                                       if ip == ip2:
                                           self.session.open(MessageBox, _('VPN Not Working?...'), MessageBox.TYPE_INFO, timeout=5)
                                       else:
                                           self.session.open(MessageBox, _('Your Ip Address is :  ' + str(IP) + '\nYour New Ip Address is :  ' + str(IP2) + '\nYour Ip Location is :  QUEBEC 910'), MessageBox.TYPE_INFO, timeout=10)
                            else:
                                self.session.open(MessageBox, _('Cannot connect (or server is down) !'), MessageBox.TYPE_INFO, timeout=5)
                            return
                        elif returnValue =="com_2":
                            if connected_to_internet():
                               os.system('/etc/init.d/openvpn stop > /dev/null 2>&1')
                               os.system('rm -r %s > /dev/null 2>&1 && rm -f %s > /dev/null 2>&1' % (LINKFILE1, LINKFILE2))
                               os.system('rm -r -f /etc/openvpn; mkdir /etc/openvpn') 
                               shutil.copyfile('/etc/cfg_conf', '/etc/openvpn/cfg.conf')
                               shutil.copyfile('/etc/vpnsolution/client_conf2', '/etc/openvpn/client.conf')
                               ip = compat_urlopen("http://ip.42.pl/raw").read()  
                               with open(LINKFILE1, "wb") as f: f.write(ip)                                   
                               f = open(LINKFILE1, 'r')
                               for line in f.readlines():
                                   IP = line.strip('\n')
                                   os.system('/etc/init.d/openvpn start > /dev/null 2>&1')
                                   time.sleep(8)
                                   ip2 = compat_urlopen("http://ip.42.pl/raw").read()  
                                   with open(LINKFILE2, "wb") as f: f.write(ip2)                                       
                                   f = open(LINKFILE2, 'r')
                                   for line in f.readlines():
                                       IP2 = line.strip('\n')
                                       if ip == ip2:
                                           self.session.open(MessageBox, _('VPN Not Working?...'), MessageBox.TYPE_INFO, timeout=5)
                                       else:
                                           self.session.open(MessageBox, _('Your Ip Address is :  ' + str(IP) + '\nYour New Ip Address is :  ' + str(IP2) + '\nYour Ip Location is :  MONTREAL 694'), MessageBox.TYPE_INFO, timeout=10)
                            else:
                                self.session.open(MessageBox, _('Cannot connect (or server is down) !'), MessageBox.TYPE_INFO, timeout=5)
                            return
                        elif returnValue =="com_3":
                            if connected_to_internet():
                               os.system('/etc/init.d/openvpn stop > /dev/null 2>&1')
                               os.system('rm -r %s > /dev/null 2>&1 && rm -f %s > /dev/null 2>&1' % (LINKFILE1, LINKFILE2))
                               os.system('rm -r -f /etc/openvpn; mkdir /etc/openvpn') 
                               shutil.copyfile('/etc/cfg_conf', '/etc/openvpn/cfg.conf')
                               shutil.copyfile('/etc/vpnsolution/client_conf3', '/etc/openvpn/client.conf')
                               ip = compat_urlopen("http://ip.42.pl/raw").read()  
                               with open(LINKFILE1, "wb") as f: f.write(ip)                                   
                               f = open(LINKFILE1, 'r')
                               for line in f.readlines():
                                   IP = line.strip('\n')
                                   os.system('/etc/init.d/openvpn start > /dev/null 2>&1')
                                   time.sleep(8)
                                   ip2 = compat_urlopen("http://ip.42.pl/raw").read()  
                                   with open(LINKFILE2, "wb") as f: f.write(ip2)                                       
                                   f = open(LINKFILE2, 'r')
                                   for line in f.readlines():
                                       IP2 = line.strip('\n')
                                       if ip == ip2:
                                           self.session.open(MessageBox, _('VPN Not Working?...'), MessageBox.TYPE_INFO, timeout=5)
                                       else:
                                           self.session.open(MessageBox, _('Your Ip Address is :  ' + str(IP) + '\nYour New Ip Address is :  ' + str(IP2) + '\nYour Ip Location is :  BEAUHAMOIS 123'), MessageBox.TYPE_INFO, timeout=10)
                            else:
                                self.session.open(MessageBox, _('Cannot connect (or server is down) !'), MessageBox.TYPE_INFO, timeout=5)
                            return
                        elif returnValue =="com_4":
                            if connected_to_internet():
                               os.system('/etc/init.d/openvpn stop > /dev/null 2>&1')
                               os.system('rm -r %s > /dev/null 2>&1 && rm -f %s > /dev/null 2>&1' % (LINKFILE1, LINKFILE2))
                               os.system('rm -r -f /etc/openvpn; mkdir /etc/openvpn') 
                               shutil.copyfile('/etc/cfg_conf', '/etc/openvpn/cfg.conf')
                               shutil.copyfile('/etc/vpnsolution/client_conf4', '/etc/openvpn/client.conf')
                               ip = compat_urlopen("http://ip.42.pl/raw").read()  
                               with open(LINKFILE1, "wb") as f: f.write(ip)                                   
                               f = open(LINKFILE1, 'r')
                               for line in f.readlines():
                                   IP = line.strip('\n')
                                   os.system('/etc/init.d/openvpn start > /dev/null 2>&1')
                                   time.sleep(8)
                                   ip2 = compat_urlopen("http://ip.42.pl/raw").read()  
                                   with open(LINKFILE2, "wb") as f: f.write(ip2)                                       
                                   f = open(LINKFILE2, 'r')
                                   for line in f.readlines():
                                       IP2 = line.strip('\n')
                                       if ip == ip2:
                                           self.session.open(MessageBox, _('VPN Not Working?...'), MessageBox.TYPE_INFO, timeout=5)
                                       else:
                                           self.session.open(MessageBox, _('Your Ip Address is :  ' + str(IP) + '\nYour New Ip Address is :  ' + str(IP2) + '\nYour Ip Location is :  CANADA 121'), MessageBox.TYPE_INFO, timeout=10)
                            else:
                                self.session.open(MessageBox, _('Cannot connect (or server is down) !'), MessageBox.TYPE_INFO, timeout=5)
                            return
                        elif returnValue =="com_5":
                            if connected_to_internet():
                               os.system('/etc/init.d/openvpn stop > /dev/null 2>&1')
                               os.system('rm -r %s > /dev/null 2>&1 && rm -f %s > /dev/null 2>&1' % (LINKFILE1, LINKFILE2))
                               os.system('rm -r -f /etc/openvpn; mkdir /etc/openvpn') 
                               shutil.copyfile('/etc/cfg_conf', '/etc/openvpn/cfg.conf')
                               shutil.copyfile('/etc/vpnsolution/client_conf5', '/etc/openvpn/client.conf')
                               ip = compat_urlopen("http://ip.42.pl/raw").read()  
                               with open(LINKFILE1, "wb") as f: f.write(ip)                                   
                               f = open(LINKFILE1, 'r')
                               for line in f.readlines():
                                   IP = line.strip('\n')
                                   os.system('/etc/init.d/openvpn start > /dev/null 2>&1')
                                   time.sleep(8)
                                   ip2 = compat_urlopen("http://ip.42.pl/raw").read()  
                                   with open(LINKFILE2, "wb") as f: f.write(ip2)                                       
                                   f = open(LINKFILE2, 'r')
                                   for line in f.readlines():
                                       IP2 = line.strip('\n')
                                       if ip == ip2:
                                           self.session.open(MessageBox, _('VPN Not Working?...'), MessageBox.TYPE_INFO, timeout=5)
                                       else:
                                           self.session.open(MessageBox, _('Your Ip Address is :  ' + str(IP) + '\nYour New Ip Address is :  ' + str(IP2) + '\nYour Ip Location is :  VIRGINIA 240'), MessageBox.TYPE_INFO, timeout=10)
                            else:
                                self.session.open(MessageBox, _('Cannot connect (or server is down) !'), MessageBox.TYPE_INFO, timeout=5)
                            return
                        elif returnValue =="com_6":
                            if connected_to_internet():
                               os.system('/etc/init.d/openvpn stop > /dev/null 2>&1')
                               os.system('rm -r %s > /dev/null 2>&1 && rm -f %s > /dev/null 2>&1' % (LINKFILE1, LINKFILE2))
                               os.system('rm -r -f /etc/openvpn; mkdir /etc/openvpn') 
                               shutil.copyfile('/etc/cfg_conf', '/etc/openvpn/cfg.conf')
                               shutil.copyfile('/etc/vpnsolution/client_conf6', '/etc/openvpn/client.conf')
                               ip = compat_urlopen("http://ip.42.pl/raw").read()  
                               with open(LINKFILE1, "wb") as f: f.write(ip)                                   
                               f = open(LINKFILE1, 'r')
                               for line in f.readlines():
                                   IP = line.strip('\n')
                                   os.system('/etc/init.d/openvpn start > /dev/null 2>&1')
                                   time.sleep(8)
                                   ip2 = compat_urlopen("http://ip.42.pl/raw").read()  
                                   with open(LINKFILE2, "wb") as f: f.write(ip2)                                       
                                   f = open(LINKFILE2, 'r')
                                   for line in f.readlines():
                                       IP2 = line.strip('\n')
                                       if ip == ip2:
                                           self.session.open(MessageBox, _('VPN Not Working?...'), MessageBox.TYPE_INFO, timeout=5)
                                       else:
                                           self.session.open(MessageBox, _('Your Ip Address is :  ' + str(IP) + '\nYour New Ip Address is :  ' + str(IP2) + '\nYour Ip Location is :  NEW YORK 184'), MessageBox.TYPE_INFO, timeout=10)
                            else:
                                self.session.open(MessageBox, _('Cannot connect (or server is down) !'), MessageBox.TYPE_INFO, timeout=5)
                            return                                                
                        elif returnValue =="com_7":
                            if connected_to_internet():
                               os.system('/etc/init.d/openvpn stop > /dev/null 2>&1')
                               os.system('rm -r %s > /dev/null 2>&1 && rm -f %s > /dev/null 2>&1' % (LINKFILE1, LINKFILE2))
                               os.system('rm -r -f /etc/openvpn; mkdir /etc/openvpn') 
                               shutil.copyfile('/etc/cfg_conf', '/etc/openvpn/cfg.conf')
                               shutil.copyfile('/etc/vpnsolution/client_conf7', '/etc/openvpn/client.conf')
                               ip = compat_urlopen("http://ip.42.pl/raw").read()  
                               with open(LINKFILE1, "wb") as f: f.write(ip)                                   
                               f = open(LINKFILE1, 'r')
                               for line in f.readlines():
                                   IP = line.strip('\n')
                                   os.system('/etc/init.d/openvpn start > /dev/null 2>&1')
                                   time.sleep(8)
                                   ip2 = compat_urlopen("http://ip.42.pl/raw").read()  
                                   with open(LINKFILE2, "wb") as f: f.write(ip2)                                       
                                   f = open(LINKFILE2, 'r')
                                   for line in f.readlines():
                                       IP2 = line.strip('\n')
                                       if ip == ip2:
                                           self.session.open(MessageBox, _('VPN Not Working?...'), MessageBox.TYPE_INFO, timeout=5)
                                       else:
                                           self.session.open(MessageBox, _('Your Ip Address is :  ' + str(IP) + '\nYour New Ip Address is :  ' + str(IP2) + '\nYour Ip Location is :  NUREMBURG 851'), MessageBox.TYPE_INFO, timeout=10)
                            else:
                                self.session.open(MessageBox, _('Cannot connect (or server is down) !'), MessageBox.TYPE_INFO, timeout=5)
                            return 
                        elif returnValue =="com_8":
                            if connected_to_internet():
                               os.system('/etc/init.d/openvpn stop > /dev/null 2>&1')
                               os.system('rm -r %s > /dev/null 2>&1 && rm -f %s > /dev/null 2>&1' % (LINKFILE1, LINKFILE2))
                               os.system('rm -r -f /etc/openvpn; mkdir /etc/openvpn') 
                               shutil.copyfile('/etc/cfg_conf', '/etc/openvpn/cfg.conf')
                               shutil.copyfile('/etc/vpnsolution/client_conf8', '/etc/openvpn/client.conf')
                               ip = compat_urlopen("http://ip.42.pl/raw").read()  
                               with open(LINKFILE1, "wb") as f: f.write(ip)                                   
                               f = open(LINKFILE1, 'r')
                               for line in f.readlines():
                                   IP = line.strip('\n')
                                   os.system('/etc/init.d/openvpn start > /dev/null 2>&1')
                                   time.sleep(8)
                                   ip2 = compat_urlopen("http://ip.42.pl/raw").read()  
                                   with open(LINKFILE2, "wb") as f: f.write(ip2)                                       
                                   f = open(LINKFILE2, 'r')
                                   for line in f.readlines():
                                       IP2 = line.strip('\n')
                                       if ip == ip2:
                                           self.session.open(MessageBox, _('VPN Not Working?...'), MessageBox.TYPE_INFO, timeout=5)
                                       else:
                                           self.session.open(MessageBox, _('Your Ip Address is :  ' + str(IP) + '\nYour New Ip Address is :  ' + str(IP2) + '\nYour Ip Location is :  MISSOURI 473'), MessageBox.TYPE_INFO, timeout=10)
                            else:
                                self.session.open(MessageBox, _('Cannot connect (or server is down) !'), MessageBox.TYPE_INFO, timeout=5)
                            return
                        elif returnValue =="com_9":
                            if connected_to_internet():
                               os.system('/etc/init.d/openvpn stop > /dev/null 2>&1')
                               os.system('rm -r %s > /dev/null 2>&1 && rm -f %s > /dev/null 2>&1' % (LINKFILE1, LINKFILE2))
                               os.system('rm -r -f /etc/openvpn; mkdir /etc/openvpn') 
                               shutil.copyfile('/etc/cfg_conf', '/etc/openvpn/cfg.conf')
                               shutil.copyfile('/etc/vpnsolution/client_conf9', '/etc/openvpn/client.conf')
                               ip = compat_urlopen("http://ip.42.pl/raw").read()  
                               with open(LINKFILE1, "wb") as f: f.write(ip)                                   
                               f = open(LINKFILE1, 'r')
                               for line in f.readlines():
                                   IP = line.strip('\n')
                                   os.system('/etc/init.d/openvpn start > /dev/null 2>&1')
                                   time.sleep(8)
                                   ip2 = compat_urlopen("http://ip.42.pl/raw").read()  
                                   with open(LINKFILE2, "wb") as f: f.write(ip2)                                       
                                   f = open(LINKFILE2, 'r')
                                   for line in f.readlines():
                                       IP2 = line.strip('\n')
                                       if ip == ip2:
                                           self.session.open(MessageBox, _('VPN Not Working?...'), MessageBox.TYPE_INFO, timeout=5)
                                       else:
                                           self.session.open(MessageBox, _('Your Ip Address is :  ' + str(IP) + '\nYour New Ip Address is :  ' + str(IP2) + '\nYour Ip Location is :  EUROPE 230'), MessageBox.TYPE_INFO, timeout=10)
                            else:
                                self.session.open(MessageBox, _('Cannot connect (or server is down) !'), MessageBox.TYPE_INFO, timeout=5)
                            return
                        elif returnValue =="com_10":
                            if connected_to_internet():
                               os.system('/etc/init.d/openvpn stop > /dev/null 2>&1')
                               os.system('rm -r %s > /dev/null 2>&1 && rm -f %s > /dev/null 2>&1' % (LINKFILE1, LINKFILE2))
                               os.system('rm -r -f /etc/openvpn; mkdir /etc/openvpn') 
                               shutil.copyfile('/etc/cfg_conf', '/etc/openvpn/cfg.conf')
                               shutil.copyfile('/etc/vpnsolution/client_conf10', '/etc/openvpn/client.conf')
                               ip = compat_urlopen("http://ip.42.pl/raw").read()  
                               with open(LINKFILE1, "wb") as f: f.write(ip)                                   
                               f = open(LINKFILE1, 'r')
                               for line in f.readlines():
                                   IP = line.strip('\n')
                                   os.system('/etc/init.d/openvpn start > /dev/null 2>&1')
                                   time.sleep(8)
                                   ip2 = compat_urlopen("http://ip.42.pl/raw").read()  
                                   with open(LINKFILE2, "wb") as f: f.write(ip2)                                       
                                   f = open(LINKFILE2, 'r')
                                   for line in f.readlines():
                                       IP2 = line.strip('\n')
                                       if ip == ip2:
                                           self.session.open(MessageBox, _('VPN Not Working?...'), MessageBox.TYPE_INFO, timeout=5)
                                       else:
                                           self.session.open(MessageBox, _('Your Ip Address is :  ' + str(IP) + '\nYour New Ip Address is :  ' + str(IP2) + '\nYour Ip Location is :  ATLANTA 118'), MessageBox.TYPE_INFO, timeout=10)
                            else:
                                self.session.open(MessageBox, _('Cannot connect (or server is down) !'), MessageBox.TYPE_INFO, timeout=5)
                            return
                        elif returnValue =="com_11":
                            if connected_to_internet():
                               os.system('/etc/init.d/openvpn stop > /dev/null 2>&1')
                               os.system('rm -r %s > /dev/null 2>&1 && rm -f %s > /dev/null 2>&1' % (LINKFILE1, LINKFILE2))
                               os.system('rm -r -f /etc/openvpn; mkdir /etc/openvpn') 
                               shutil.copyfile('/etc/cfg_conf', '/etc/openvpn/cfg.conf')
                               shutil.copyfile('/etc/vpnsolution/client_conf11', '/etc/openvpn/client.conf')
                               ip = compat_urlopen("http://ip.42.pl/raw").read()  
                               with open(LINKFILE1, "wb") as f: f.write(ip)                                   
                               f = open(LINKFILE1, 'r')
                               for line in f.readlines():
                                   IP = line.strip('\n')
                                   os.system('/etc/init.d/openvpn start > /dev/null 2>&1')
                                   time.sleep(8)
                                   ip2 = compat_urlopen("http://ip.42.pl/raw").read()  
                                   with open(LINKFILE2, "wb") as f: f.write(ip2)                                       
                                   f = open(LINKFILE2, 'r')
                                   for line in f.readlines():
                                       IP2 = line.strip('\n')
                                       if ip == ip2:
                                           self.session.open(MessageBox, _('VPN Not Working?...'), MessageBox.TYPE_INFO, timeout=5)
                                       else:
                                           self.session.open(MessageBox, _('Your Ip Address is :  ' + str(IP) + '\nYour New Ip Address is :  ' + str(IP2) + '\nYour Ip Location is :  NEW JERSEY 120'), MessageBox.TYPE_INFO, timeout=10)
                            else:
                                self.session.open(MessageBox, _('Cannot connect (or server is down) !'), MessageBox.TYPE_INFO, timeout=5)
                            return
                        elif returnValue =="com_12":
                            if connected_to_internet():
                               os.system('/etc/init.d/openvpn stop > /dev/null 2>&1')
                               os.system('rm -r %s > /dev/null 2>&1 && rm -f %s > /dev/null 2>&1' % (LINKFILE1, LINKFILE2))
                               os.system('rm -r -f /etc/openvpn; mkdir /etc/openvpn') 
                               shutil.copyfile('/etc/cfg_conf', '/etc/openvpn/cfg.conf')
                               shutil.copyfile('/etc/vpnsolution/client_conf12', '/etc/openvpn/client.conf')
                               ip = compat_urlopen("http://ip.42.pl/raw").read()  
                               with open(LINKFILE1, "wb") as f: f.write(ip)                                   
                               f = open(LINKFILE1, 'r')
                               for line in f.readlines():
                                   IP = line.strip('\n')
                                   os.system('/etc/init.d/openvpn start > /dev/null 2>&1')
                                   time.sleep(8)
                                   ip2 = compat_urlopen("http://ip.42.pl/raw").read()  
                                   with open(LINKFILE2, "wb") as f: f.write(ip2)                                       
                                   f = open(LINKFILE2, 'r')
                                   for line in f.readlines():
                                       IP2 = line.strip('\n')
                                       if ip == ip2:
                                           self.session.open(MessageBox, _('VPN Not Working?...'), MessageBox.TYPE_INFO, timeout=5)
                                       else:
                                           self.session.open(MessageBox, _('Your Ip Address is :  ' + str(IP) + '\nYour New Ip Address is :  ' + str(IP2) + '\nYour Ip Location is :  SEATTLE 521'), MessageBox.TYPE_INFO, timeout=10)
                            else:
                                self.session.open(MessageBox, _('Cannot connect (or server is down) !'), MessageBox.TYPE_INFO, timeout=5)
                            return
                        elif returnValue =="com_13":
                            if connected_to_internet():
                               os.system('/etc/init.d/openvpn stop > /dev/null 2>&1')
                               os.system('rm -r %s > /dev/null 2>&1 && rm -f %s > /dev/null 2>&1' % (LINKFILE1, LINKFILE2))
                               os.system('rm -r -f /etc/openvpn; mkdir /etc/openvpn') 
                               shutil.copyfile('/etc/cfg_conf', '/etc/openvpn/cfg.conf')
                               shutil.copyfile('/etc/vpnsolution/client_conf13', '/etc/openvpn/client.conf')
                               ip = compat_urlopen("http://ip.42.pl/raw").read()  
                               with open(LINKFILE1, "wb") as f: f.write(ip)                                   
                               f = open(LINKFILE1, 'r')
                               for line in f.readlines():
                                   IP = line.strip('\n')
                                   os.system('/etc/init.d/openvpn start > /dev/null 2>&1')
                                   time.sleep(8)
                                   ip2 = compat_urlopen("http://ip.42.pl/raw").read()  
                                   with open(LINKFILE2, "wb") as f: f.write(ip2)                                       
                                   f = open(LINKFILE2, 'r')
                                   for line in f.readlines():
                                       IP2 = line.strip('\n')
                                       if ip == ip2:
                                           self.session.open(MessageBox, _('VPN Not Working?...'), MessageBox.TYPE_INFO, timeout=5)
                                       else:
                                           self.session.open(MessageBox, _('Your Ip Address is :  ' + str(IP) + '\nYour New Ip Address is :  ' + str(IP2) + '\nYour Ip Location is :  CHICAGO 155'), MessageBox.TYPE_INFO, timeout=10)
                            else:
                                self.session.open(MessageBox, _('Cannot connect (or server is down) !'), MessageBox.TYPE_INFO, timeout=5)
                            return
                        elif returnValue =="com_14":
                            if connected_to_internet():
                               os.system('/etc/init.d/openvpn stop > /dev/null 2>&1')
                               os.system('rm -r %s > /dev/null 2>&1 && rm -f %s > /dev/null 2>&1' % (LINKFILE1, LINKFILE2))
                               os.system('rm -r -f /etc/openvpn; mkdir /etc/openvpn') 
                               shutil.copyfile('/etc/cfg_conf', '/etc/openvpn/cfg.conf')
                               shutil.copyfile('/etc/vpnsolution/client_conf14', '/etc/openvpn/client.conf')
                               ip = compat_urlopen("http://ip.42.pl/raw").read()  
                               with open(LINKFILE1, "wb") as f: f.write(ip)                                   
                               f = open(LINKFILE1, 'r')
                               for line in f.readlines():
                                   IP = line.strip('\n')
                                   os.system('/etc/init.d/openvpn start > /dev/null 2>&1')
                                   time.sleep(8)
                                   ip2 = compat_urlopen("http://ip.42.pl/raw").read()  
                                   with open(LINKFILE2, "wb") as f: f.write(ip2)                                       
                                   f = open(LINKFILE2, 'r')
                                   for line in f.readlines():
                                       IP2 = line.strip('\n')
                                       if ip == ip2:
                                           self.session.open(MessageBox, _('VPN Not Working?...'), MessageBox.TYPE_INFO, timeout=5)
                                       else:
                                           self.session.open(MessageBox, _('Your Ip Address is :  ' + str(IP) + '\nYour New Ip Address is :  ' + str(IP2) + '\nYour Ip Location is :  DALLAS 938'), MessageBox.TYPE_INFO, timeout=10)
                            else:
                                self.session.open(MessageBox, _('Cannot connect (or server is down) !'), MessageBox.TYPE_INFO, timeout=5)
                            return
                        elif returnValue =="com_15":
                            if connected_to_internet():
                               os.system('/etc/init.d/openvpn stop > /dev/null 2>&1')
                               os.system('rm -r %s > /dev/null 2>&1 && rm -f %s > /dev/null 2>&1' % (LINKFILE1, LINKFILE2))
                               os.system('rm -r -f /etc/openvpn; mkdir /etc/openvpn') 
                               shutil.copyfile('/etc/cfg_conf', '/etc/openvpn/cfg.conf')
                               shutil.copyfile('/etc/vpnsolution/client_conf15', '/etc/openvpn/client.conf')
                               ip = compat_urlopen("http://ip.42.pl/raw").read()  
                               with open(LINKFILE1, "wb") as f: f.write(ip)                                   
                               f = open(LINKFILE1, 'r')
                               for line in f.readlines():
                                   IP = line.strip('\n')
                                   os.system('/etc/init.d/openvpn start > /dev/null 2>&1')
                                   time.sleep(8)
                                   ip2 = compat_urlopen("http://ip.42.pl/raw").read()  
                                   with open(LINKFILE2, "wb") as f: f.write(ip2)                                       
                                   f = open(LINKFILE2, 'r')
                                   for line in f.readlines():
                                       IP2 = line.strip('\n')
                                       if ip == ip2:
                                           self.session.open(MessageBox, _('VPN Not Working?...'), MessageBox.TYPE_INFO, timeout=5)
                                       else:
                                           self.session.open(MessageBox, _('Your Ip Address is :  ' + str(IP) + '\nYour New Ip Address is :  ' + str(IP2) + '\nYour Ip Location is :  LONDON 103'), MessageBox.TYPE_INFO, timeout=10)
                            else:
                                self.session.open(MessageBox, _('Cannot connect (or server is down) !'), MessageBox.TYPE_INFO, timeout=5)
                            return
                        elif returnValue =="com_16":
                            if connected_to_internet():
                               os.system('/etc/init.d/openvpn stop > /dev/null 2>&1')
                               os.system('rm -r %s > /dev/null 2>&1 && rm -f %s > /dev/null 2>&1' % (LINKFILE1, LINKFILE2))
                               os.system('rm -r -f /etc/openvpn; mkdir /etc/openvpn') 
                               shutil.copyfile('/etc/cfg_conf', '/etc/openvpn/cfg.conf')
                               shutil.copyfile('/etc/vpnsolution/client_conf16', '/etc/openvpn/client.conf')
                               ip = compat_urlopen("http://ip.42.pl/raw").read()  
                               with open(LINKFILE1, "wb") as f: f.write(ip)                                   
                               f = open(LINKFILE1, 'r')
                               for line in f.readlines():
                                   IP = line.strip('\n')
                                   os.system('/etc/init.d/openvpn start > /dev/null 2>&1')
                                   time.sleep(8)
                                   ip2 = compat_urlopen("http://ip.42.pl/raw").read()  
                                   with open(LINKFILE2, "wb") as f: f.write(ip2)                                       
                                   f = open(LINKFILE2, 'r')
                                   for line in f.readlines():
                                       IP2 = line.strip('\n')
                                       if ip == ip2:
                                           self.session.open(MessageBox, _('VPN Not Working?...'), MessageBox.TYPE_INFO, timeout=5)
                                       else:
                                           self.session.open(MessageBox, _('Your Ip Address is :  ' + str(IP) + '\nYour New Ip Address is :  ' + str(IP2) + '\nYour Ip Location is :  PARIS 221'), MessageBox.TYPE_INFO, timeout=10)
                            else:
                                self.session.open(MessageBox, _('Cannot connect (or server is down) !'), MessageBox.TYPE_INFO, timeout=5)
                            return
                        elif returnValue =="com_17":
                            if connected_to_internet():
                               os.system('/etc/init.d/openvpn stop > /dev/null 2>&1')
                               os.system('rm -r %s > /dev/null 2>&1 && rm -f %s > /dev/null 2>&1' % (LINKFILE1, LINKFILE2))
                               os.system('rm -r -f /etc/openvpn; mkdir /etc/openvpn') 
                               shutil.copyfile('/etc/cfg_conf', '/etc/openvpn/cfg.conf')
                               shutil.copyfile('/etc/vpnsolution/client_conf17', '/etc/openvpn/client.conf')
                               ip = compat_urlopen("http://ip.42.pl/raw").read()  
                               with open(LINKFILE1, "wb") as f: f.write(ip)                                   
                               f = open(LINKFILE1, 'r')
                               for line in f.readlines():
                                   IP = line.strip('\n')
                                   os.system('/etc/init.d/openvpn start > /dev/null 2>&1')
                                   time.sleep(8)
                                   ip2 = compat_urlopen("http://ip.42.pl/raw").read()  
                                   with open(LINKFILE2, "a") as f: f.write(ip2)                                       
                                   f = open(LINKFILE2, 'r')
                                   for line in f.readlines():
                                       IP2 = line.strip('\n')
                                       if ip == ip2:
                                           self.session.open(MessageBox, _('VPN Not Working?...'), MessageBox.TYPE_INFO, timeout=5)
                                       else:
                                           self.session.open(MessageBox, _('Your Ip Address is :  ' + str(IP) + '\nYour New Ip Address is :  ' + str(IP2) + '\nYour Ip Location is :  LOS ANGELES 691'), MessageBox.TYPE_INFO, timeout=10)
                            else:
                                self.session.open(MessageBox, _('Cannot connect (or server is down) !'), MessageBox.TYPE_INFO, timeout=5)
                            return
                        elif returnValue =="com_18":
                            if connected_to_internet():
                               os.system('/etc/init.d/openvpn stop > /dev/null 2>&1')
                               os.system('rm -r %s > /dev/null 2>&1 && rm -f %s > /dev/null 2>&1' % (LINKFILE1, LINKFILE2))
                               os.system('rm -r -f /etc/openvpn; mkdir /etc/openvpn') 
                               shutil.copyfile('/etc/cfg_conf', '/etc/openvpn/cfg.conf')
                               shutil.copyfile('/etc/vpnsolution/client_conf18', '/etc/openvpn/client.conf')
                               ip = compat_urlopen("http://ip.42.pl/raw").read()  
                               with open(LINKFILE1, "wb") as f: f.write(ip)                                   
                               f = open(LINKFILE1, 'r')
                               for line in f.readlines():
                                   IP = line.strip('\n')
                                   os.system('/etc/init.d/openvpn start > /dev/null 2>&1')
                                   time.sleep(8)
                                   ip2 = compat_urlopen("http://ip.42.pl/raw").read()  
                                   with open(LINKFILE2, "wb") as f: f.write(ip2)                                       
                                   f = open(LINKFILE2, 'r')
                                   for line in f.readlines():
                                       IP2 = line.strip('\n')
                                       if ip == ip2:
                                           self.session.open(MessageBox, _('VPN Not Working?...'), MessageBox.TYPE_INFO, timeout=5)
                                       else:
                                           self.session.open(MessageBox, _('Your Ip Address is :  ' + str(IP) + '\nYour New Ip Address is :  ' + str(IP2) + '\nYour Ip Location is :  MIAMI 149'), MessageBox.TYPE_INFO, timeout=10)
                            else:
                                self.session.open(MessageBox, _('Cannot connect (or server is down) !'), MessageBox.TYPE_INFO, timeout=5)
                            return
                        elif returnValue =="com_19":
                            if connected_to_internet():
                               os.system('/etc/init.d/openvpn stop > /dev/null 2>&1')
                               os.system('rm -r %s > /dev/null 2>&1 && rm -f %s > /dev/null 2>&1' % (LINKFILE1, LINKFILE2))
                               os.system('rm -r -f /etc/openvpn; mkdir /etc/openvpn') 
                               shutil.copyfile('/etc/cfg_conf', '/etc/openvpn/cfg.conf')
                               shutil.copyfile('/etc/vpnsolution/client_conf19', '/etc/openvpn/client.conf')
                               ip = compat_urlopen("http://ip.42.pl/raw").read()  
                               with open(LINKFILE1, "wb") as f: f.write(ip)                                   
                               f = open(LINKFILE1, 'r')
                               for line in f.readlines():
                                   IP = line.strip('\n')
                                   os.system('/etc/init.d/openvpn start > /dev/null 2>&1')
                                   time.sleep(8)
                                   ip2 = compat_urlopen("http://ip.42.pl/raw").read()  
                                   with open(LINKFILE2, "wb") as f: f.write(ip2)                                       
                                   f = open(LINKFILE2, 'r')
                                   for line in f.readlines():
                                       IP2 = line.strip('\n')
                                       if ip == ip2:
                                           self.session.open(MessageBox, _('VPN Not Working?...'), MessageBox.TYPE_INFO, timeout=5)
                                       else:
                                           self.session.open(MessageBox, _('Your Ip Address is :  ' + str(IP) + '\nYour New Ip Address is :  ' + str(IP2) + '\nYour Ip Location is :  TORONTO 160'), MessageBox.TYPE_INFO, timeout=10)
                            else:
                                self.session.open(MessageBox, _('Cannot connect (or server is down) !'), MessageBox.TYPE_INFO, timeout=5)
                            return
                        elif returnValue =="com_20":
                            if connected_to_internet():
                               os.system('/etc/init.d/openvpn stop > /dev/null 2>&1')
                               os.system('rm -r %s > /dev/null 2>&1 && rm -f %s > /dev/null 2>&1' % (LINKFILE1, LINKFILE2))
                               os.system('rm -r -f /etc/openvpn; mkdir /etc/openvpn') 
                               shutil.copyfile('/etc/cfg_conf', '/etc/openvpn/cfg.conf')
                               shutil.copyfile('/etc/vpnsolution/client_conf20', '/etc/openvpn/client.conf')
                               ip = compat_urlopen("http://ip.42.pl/raw").read()  
                               with open(LINKFILE1, "wb") as f: f.write(ip)                                   
                               f = open(LINKFILE1, 'r')
                               for line in f.readlines():
                                   IP = line.strip('\n')
                                   os.system('/etc/init.d/openvpn start > /dev/null 2>&1')
                                   time.sleep(8)
                                   ip2 = compat_urlopen("http://ip.42.pl/raw").read()  
                                   with open(LINKFILE2, "wb") as f: f.write(ip2)                                       
                                   f = open(LINKFILE2, 'r')
                                   for line in f.readlines():
                                       IP2 = line.strip('\n')
                                       if ip == ip2:
                                           self.session.open(MessageBox, _('VPN Not Working?...'), MessageBox.TYPE_INFO, timeout=5)
                                       else:
                                           self.session.open(MessageBox, _('Your Ip Address is :  ' + str(IP) + '\nYour New Ip Address is :  ' + str(IP2) + '\nYour Ip Location is :  CHICAGO 132+'), MessageBox.TYPE_INFO, timeout=10)
                            else:
                                self.session.open(MessageBox, _('Cannot connect (or server is down) !'), MessageBox.TYPE_INFO, timeout=5)
                            return
                        elif returnValue =="com_21":
                            if connected_to_internet():
                               os.system('/etc/init.d/openvpn stop > /dev/null 2>&1')
                               os.system('rm -r %s > /dev/null 2>&1 && rm -f %s > /dev/null 2>&1' % (LINKFILE1, LINKFILE2))
                               os.system('rm -r -f /etc/openvpn; mkdir /etc/openvpn') 
                               shutil.copyfile('/etc/cfg_conf', '/etc/openvpn/cfg.conf')
                               shutil.copyfile('/etc/vpnsolution/client_conf21', '/etc/openvpn/client.conf')
                               ip = compat_urlopen("http://ip.42.pl/raw").read()  
                               with open(LINKFILE1, "wb") as f: f.write(ip)                                 
                               f = open(LINKFILE1, 'r')
                               for line in f.readlines():
                                   IP = line.strip('\n')
                                   os.system('/etc/init.d/openvpn start > /dev/null 2>&1')
                                   time.sleep(8)
                                   ip2 = compat_urlopen("http://ip.42.pl/raw").read()  
                                   with open(LINKFILE2, "wb") as f: f.write(ip2)                                         
                                   f = open(LINKFILE2, 'r')
                                   for line in f.readlines():
                                       IP2 = line.strip('\n')
                                       if ip == ip2:
                                           self.session.open(MessageBox, _('VPN Not Working?...'), MessageBox.TYPE_INFO, timeout=5)
                                       else:
                                           self.session.open(MessageBox, _('Your Ip Address is :  ' + str(IP) + '\nYour New Ip Address is :  ' + str(IP2) + '\nYour Ip Location is :  Sydney'), MessageBox.TYPE_INFO, timeout=10)
                            else:
                                self.session.open(MessageBox, _('Cannot connect (or server is down) !'), MessageBox.TYPE_INFO, timeout=5)
                            return
                        elif returnValue =="com_022":
                            if connected_to_internet():
                               os.system('/etc/init.d/openvpn stop > /dev/null 2>&1')
                               os.system('rm -r %s > /dev/null 2>&1 && rm -f %s > /dev/null 2>&1' % (LINKFILE1, LINKFILE2))
                               os.system('rm -r -f /etc/openvpn; mkdir /etc/openvpn') 
                               shutil.copyfile('/etc/cfg_conf', '/etc/openvpn/cfg.conf')
                               shutil.copyfile('/etc/vpnsolution/client_conf22', '/etc/openvpn/client.conf')
                               ip = compat_urlopen("http://ip.42.pl/raw").read()  
                               with open(LINKFILE1, "wb") as f: f.write(ip)                                   
                               f = open(LINKFILE1, 'r')
                               for line in f.readlines():
                                   IP = line.strip('\n')
                                   os.system('/etc/init.d/openvpn start > /dev/null 2>&1')
                                   time.sleep(8)
                                   ip2 = compat_urlopen("http://ip.42.pl/raw").read()  
                                   with open(LINKFILE2, "wb") as f: f.write(ip2)                                       
                                   f = open(LINKFILE2, 'r')
                                   for line in f.readlines():
                                       IP2 = line.strip('\n')
                                       if ip == ip2:
                                           self.session.open(MessageBox, _('VPN Not Working?...'), MessageBox.TYPE_INFO, timeout=5)
                                       else:
                                           self.session.open(MessageBox, _('Your Ip Address is :  ' + str(IP) + '\nYour New Ip Address is :  ' + str(IP2) + '\nYour Ip Location is :  LONDON 3000'), MessageBox.TYPE_INFO, timeout=10)
                            else:
                                self.session.open(MessageBox, _('Cannot connect (or server is down) !'), MessageBox.TYPE_INFO, timeout=5)
                            return
                        elif returnValue =="com_023":
                            if connected_to_internet():
                               os.system('/etc/init.d/openvpn stop > /dev/null 2>&1')
                               os.system('rm -r %s > /dev/null 2>&1 && rm -f %s > /dev/null 2>&1' % (LINKFILE1, LINKFILE2))
                               os.system('rm -r -f /etc/openvpn; mkdir /etc/openvpn') 
                               shutil.copyfile('/etc/cfg_conf', '/etc/openvpn/cfg.conf')
                               shutil.copyfile('/etc/vpnsolution/client_conf23', '/etc/openvpn/client.conf')
                               ip = compat_urlopen("http://ip.42.pl/raw").read()  
                               with open(LINKFILE1, "wb") as f: f.write(ip)                                   
                               f = open(LINKFILE1, 'r')
                               for line in f.readlines():
                                   IP = line.strip('\n')
                                   os.system('/etc/init.d/openvpn start > /dev/null 2>&1')
                                   time.sleep(8)
                                   ip2 = compat_urlopen("http://ip.42.pl/raw").read()  
                                   with open(LINKFILE2, "wb") as f: f.write(ip2)                                       
                                   f = open(LINKFILE2, 'r')
                                   for line in f.readlines():
                                       IP2 = line.strip('\n')
                                       if ip == ip2:
                                           self.session.open(MessageBox, _('VPN Not Working?...'), MessageBox.TYPE_INFO, timeout=5)
                                       else:
                                           self.session.open(MessageBox, _('Your Ip Address is :  ' + str(IP) + '\nYour New Ip Address is :  ' + str(IP2) + '\nYour Ip Location is :  UK LONDON 136'), MessageBox.TYPE_INFO, timeout=10)
                            else:
                                self.session.open(MessageBox, _('Cannot connect (or server is down) !'), MessageBox.TYPE_INFO, timeout=5)
                            return
                        elif returnValue =="com_024":
                            if connected_to_internet():
                               os.system('/etc/init.d/openvpn stop > /dev/null 2>&1')
                               os.system('rm -r %s > /dev/null 2>&1 && rm -f %s > /dev/null 2>&1' % (LINKFILE1, LINKFILE2))
                               os.system('rm -r -f /etc/openvpn; mkdir /etc/openvpn') 
                               shutil.copyfile('/etc/cfg_conf', '/etc/openvpn/cfg.conf')
                               shutil.copyfile('/etc/vpnsolution/client_conf24', '/etc/openvpn/client.conf')
                               ip = compat_urlopen("http://ip.42.pl/raw").read()  
                               with open(LINKFILE1, "wb") as f: f.write(ip)                                   
                               f = open(LINKFILE1, 'r')
                               for line in f.readlines():
                                   IP = line.strip('\n')
                                   os.system('/etc/init.d/openvpn start > /dev/null 2>&1')
                                   time.sleep(8)
                                   ip2 = compat_urlopen("http://ip.42.pl/raw").read()  
                                   with open(LINKFILE2, "wb") as f: f.write(ip2)                                       
                                   f = open(LINKFILE2, 'r')
                                   for line in f.readlines():
                                       IP2 = line.strip('\n')
                                       if ip == ip2:
                                           self.session.open(MessageBox, _('VPN Not Working?...'), MessageBox.TYPE_INFO, timeout=5)
                                       else:
                                           self.session.open(MessageBox, _('Your Ip Address is :  ' + str(IP) + '\nYour New Ip Address is :  ' + str(IP2) + '\nYour Ip Location is :  FRANCE 165'), MessageBox.TYPE_INFO, timeout=10)
                            else:
                                self.session.open(MessageBox, _('Cannot connect (or server is down) !'), MessageBox.TYPE_INFO, timeout=5)
                            return
                        elif returnValue =="com_025":
                            if connected_to_internet():
                               os.system('/etc/init.d/openvpn stop > /dev/null 2>&1')
                               os.system('rm -r %s > /dev/null 2>&1 && rm -f %s > /dev/null 2>&1' % (LINKFILE1, LINKFILE2))
                               os.system('rm -r -f /etc/openvpn; mkdir /etc/openvpn') 
                               shutil.copyfile('/etc/cfg_conf', '/etc/openvpn/cfg.conf')
                               shutil.copyfile('/etc/vpnsolution/client_conf25', '/etc/openvpn/client.conf')
                               ip = compat_urlopen("http://ip.42.pl/raw").read()  
                               with open(LINKFILE1, "wb") as f: f.write(ip)                                   
                               f = open(LINKFILE1, 'r')
                               for line in f.readlines():
                                   IP = line.strip('\n')
                                   os.system('/etc/init.d/openvpn start > /dev/null 2>&1')
                                   time.sleep(8)
                                   ip2 = compat_urlopen("http://ip.42.pl/raw").read()  
                                   with open(LINKFILE2, "wb") as f: f.write(ip2)                                       
                                   f = open(LINKFILE2, 'r')
                                   for line in f.readlines():
                                       IP2 = line.strip('\n')
                                       if ip == ip2:
                                           self.session.open(MessageBox, _('VPN Not Working?...'), MessageBox.TYPE_INFO, timeout=5)
                                       else:
                                           self.session.open(MessageBox, _('Your Ip Address is :  ' + str(IP) + '\nYour New Ip Address is :  ' + str(IP2) + '\nYour Ip Location is :  CHICAGO (High Speed)'), MessageBox.TYPE_INFO, timeout=10)
                            else:
                                self.session.open(MessageBox, _('Cannot connect (or server is down) !'), MessageBox.TYPE_INFO, timeout=5)
                            return
                        elif returnValue =="com_026":
                            if connected_to_internet():
                               os.system('/etc/init.d/openvpn stop > /dev/null 2>&1')
                               os.system('rm -r %s > /dev/null 2>&1 && rm -f %s > /dev/null 2>&1' % (LINKFILE1, LINKFILE2))
                               os.system('rm -r -f /etc/openvpn; mkdir /etc/openvpn') 
                               shutil.copyfile('/etc/cfg_conf', '/etc/openvpn/cfg.conf')
                               shutil.copyfile('/etc/vpnsolution/client_conf26', '/etc/openvpn/client.conf')
                               ip = compat_urlopen("http://ip.42.pl/raw").read()  
                               with open(LINKFILE1, "wb") as f: f.write(ip)                                   
                               f = open(LINKFILE1, 'r')
                               for line in f.readlines():
                                   IP = line.strip('\n')
                                   os.system('/etc/init.d/openvpn start > /dev/null 2>&1')
                                   time.sleep(8)
                                   ip2 = compat_urlopen("http://ip.42.pl/raw").read()  
                                   with open(LINKFILE2, "wb") as f: f.write(ip2)                                       
                                   f = open(LINKFILE2, 'r')
                                   for line in f.readlines():
                                       IP2 = line.strip('\n')
                                       if ip == ip2:
                                           self.session.open(MessageBox, _('VPN Not Working?...'), MessageBox.TYPE_INFO, timeout=5)
                                       else:
                                           self.session.open(MessageBox, _('Your Ip Address is :  ' + str(IP) + '\nYour New Ip Address is :  ' + str(IP2) + '\nYour Ip Location is :  NY / NJ (High Speed)'), MessageBox.TYPE_INFO, timeout=10)
                            else:
                                self.session.open(MessageBox, _('Cannot connect (or server is down) !'), MessageBox.TYPE_INFO, timeout=5)
                            return
                        elif returnValue =="com_027":
                            if connected_to_internet():
                               os.system('/etc/init.d/openvpn stop > /dev/null 2>&1')
                               os.system('rm -r %s > /dev/null 2>&1 && rm -f %s > /dev/null 2>&1' % (LINKFILE1, LINKFILE2))
                               os.system('rm -r -f /etc/openvpn; mkdir /etc/openvpn') 
                               shutil.copyfile('/etc/cfg_conf', '/etc/openvpn/cfg.conf')
                               shutil.copyfile('/etc/vpnsolution/client_conf27', '/etc/openvpn/client.conf')
                               ip = compat_urlopen("http://ip.42.pl/raw").read()  
                               with open(LINKFILE1, "wb") as f: f.write(ip)                                 
                               f = open(LINKFILE1, 'r')
                               for line in f.readlines():
                                   IP = line.strip('\n')
                                   os.system('/etc/init.d/openvpn start > /dev/null 2>&1')
                                   time.sleep(8)
                                   ip2 = compat_urlopen("http://ip.42.pl/raw").read()  
                                   with open(LINKFILE2, "wb") as f: f.write(ip2)                                         
                                   f = open(LINKFILE2, 'r')
                                   for line in f.readlines():
                                       IP2 = line.strip('\n')
                                       if ip == ip2:
                                           self.session.open(MessageBox, _('VPN Not Working?...'), MessageBox.TYPE_INFO, timeout=5)
                                       else:
                                           self.session.open(MessageBox, _('Your Ip Address is :  ' + str(IP) + '\nYour New Ip Address is :  ' + str(IP2) + '\nYour Ip Location is :  MIAMI (High Speed)'), MessageBox.TYPE_INFO, timeout=10)
                            else:
                                self.session.open(MessageBox, _('Cannot connect (or server is down) !'), MessageBox.TYPE_INFO, timeout=5)
                            return
                        elif returnValue =="com_02":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia801406.us.archive.org/25/items/iptvworld-24/IPTVWORLDVPN2.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='Free VPN', cmdlist=cmdlist, finishedCallback=None)
                        elif returnValue =="com_22":
                            if connected_to_internet():
                               os.system('/etc/init.d/openvpn stop > /dev/null 2>&1')
                               os.system('rm -r %s > /dev/null 2>&1 && rm -f %s > /dev/null 2>&1' % (LINKFILE1, LINKFILE2))
                               os.system('rm -r -f /etc/openvpn; mkdir /etc/openvpn') 
                               shutil.copyfile('/etc/pointvpn/cfg_conf', '/etc/openvpn/cfg.conf')
                               shutil.copyfile('/etc/pointvpn/client_conf1', '/etc/openvpn/client.conf')
                               ip = compat_urlopen("http://ip.42.pl/raw").read()                           
                               with open(LINKFILE1, "wb") as f: f.write(ip)                                   
                               f = open(LINKFILE1, 'r')
                               for line in f.readlines():
                                   IP = line.strip('\n')
                                   os.system('/etc/init.d/openvpn start > /dev/null 2>&1')
                                   time.sleep(8)
                                   ip2 = compat_urlopen("http://ip.42.pl/raw").read()  
                                   with open(LINKFILE2, "wb") as f: f.write(ip2)                                       
                                   f = open(LINKFILE2, 'r')
                                   for line in f.readlines():
                                       IP2 = line.strip('\n')
                                       if ip == ip2:
                                           self.session.open(MessageBox, _('VPN Not Working?...'), MessageBox.TYPE_INFO, timeout=5)
                                       else:
                                           self.session.open(MessageBox, _('Your Ip Address is :  ' + str(IP) + '\nYour New Ip Address is :  ' + str(IP2) + '\nYour Ip Location is :  Buenos Aires, Argentina'), MessageBox.TYPE_INFO, timeout=10)
                            else:
                                self.session.open(MessageBox, _('Cannot connect (or server is down) !'), MessageBox.TYPE_INFO, timeout=5)
                            return
                        elif returnValue =="com_23":
                            if connected_to_internet():
                               os.system('/etc/init.d/openvpn stop > /dev/null 2>&1')
                               os.system('rm -r %s > /dev/null 2>&1 && rm -f %s > /dev/null 2>&1' % (LINKFILE1, LINKFILE2))
                               os.system('rm -r -f /etc/openvpn; mkdir /etc/openvpn') 
                               shutil.copyfile('/etc/pointvpn/cfg_conf', '/etc/openvpn/cfg.conf')
                               shutil.copyfile('/etc/pointvpn/client_conf2', '/etc/openvpn/client.conf')
                               ip = compat_urlopen("http://ip.42.pl/raw").read()   
                               with open(LINKFILE1, "wb") as f: f.write(ip)                                   
                               f = open(LINKFILE1, 'r')
                               for line in f.readlines():
                                   IP = line.strip('\n')
                                   os.system('/etc/init.d/openvpn start > /dev/null 2>&1')
                                   time.sleep(8)
                                   ip2 = compat_urlopen("http://ip.42.pl/raw").read()  
                                   with open(LINKFILE2, "wb") as f: f.write(ip2)                                       
                                   f = open(LINKFILE2, 'r')
                                   for line in f.readlines():
                                       IP2 = line.strip('\n')
                                       if ip == ip2:
                                           self.session.open(MessageBox, _('VPN Not Working?...'), MessageBox.TYPE_INFO, timeout=5)
                                       else:
                                           self.session.open(MessageBox, _('Your Ip Address is :  ' + str(IP) + '\nYour New Ip Address is :  ' + str(IP2) + '\nYour Ip Location is :  Sydney 2, Australia'), MessageBox.TYPE_INFO, timeout=10)
                            else:
                                self.session.open(MessageBox, _('Cannot connect (or server is down) !'), MessageBox.TYPE_INFO, timeout=5)
                            return              
                        elif returnValue =="com_24":
                            if connected_to_internet():
                               os.system('/etc/init.d/openvpn stop > /dev/null 2>&1')
                               os.system('rm -r %s > /dev/null 2>&1 && rm -f %s > /dev/null 2>&1' % (LINKFILE1, LINKFILE2))
                               os.system('rm -r -f /etc/openvpn; mkdir /etc/openvpn') 
                               shutil.copyfile('/etc/pointvpn/cfg_conf', '/etc/openvpn/cfg.conf')
                               shutil.copyfile('/etc/pointvpn/client_conf3', '/etc/openvpn/client.conf')
                               ip = compat_urlopen("http://ip.42.pl/raw").read()   
                               with open(LINKFILE1, "wb") as f: f.write(ip)                                   
                               f = open(LINKFILE1, 'r')
                               for line in f.readlines():
                                   IP = line.strip('\n')
                                   os.system('/etc/init.d/openvpn start > /dev/null 2>&1')
                                   time.sleep(8)
                                   ip2 = compat_urlopen("http://ip.42.pl/raw").read()  
                                   with open(LINKFILE2, "wb") as f: f.write(ip2)                                       
                                   f = open(LINKFILE2, 'r')
                                   for line in f.readlines():
                                       IP2 = line.strip('\n')
                                       if ip == ip2:
                                           self.session.open(MessageBox, _('VPN Not Working?...'), MessageBox.TYPE_INFO, timeout=5)
                                       else:
                                           self.session.open(MessageBox, _('Your Ip Address is :  ' + str(IP) + '\nYour New Ip Address is :  ' + str(IP2) + '\nYour Ip Location is :  Sydney, Australia'), MessageBox.TYPE_INFO, timeout=10)
                            else:
                                self.session.open(MessageBox, _('Cannot connect (or server is down) !'), MessageBox.TYPE_INFO, timeout=5)
                            return                      
                        elif returnValue =="com_25":
                            if connected_to_internet():
                               os.system('/etc/init.d/openvpn stop > /dev/null 2>&1')
                               os.system('rm -r %s > /dev/null 2>&1 && rm -f %s > /dev/null 2>&1' % (LINKFILE1, LINKFILE2))
                               os.system('rm -r -f /etc/openvpn; mkdir /etc/openvpn') 
                               shutil.copyfile('/etc/pointvpn/cfg_conf', '/etc/openvpn/cfg.conf')
                               shutil.copyfile('/etc/pointvpn/client_conf4', '/etc/openvpn/client.conf')
                               ip = compat_urlopen("http://ip.42.pl/raw").read()   
                               with open(LINKFILE1, "wb") as f: f.write(ip)                                   
                               f = open(LINKFILE1, 'r')
                               for line in f.readlines():
                                   IP = line.strip('\n')
                                   os.system('/etc/init.d/openvpn start > /dev/null 2>&1')
                                   time.sleep(8)
                                   ip2 = compat_urlopen("http://ip.42.pl/raw").read()  
                                   with open(LINKFILE2, "wb") as f: f.write(ip2)                                       
                                   f = open(LINKFILE2, 'r')
                                   for line in f.readlines():
                                       IP2 = line.strip('\n')
                                       if ip == ip2:
                                           self.session.open(MessageBox, _('VPN Not Working?...'), MessageBox.TYPE_INFO, timeout=5)
                                       else:
                                           self.session.open(MessageBox, _('Your Ip Address is :  ' + str(IP) + '\nYour New Ip Address is :  ' + str(IP2) + '\nYour Ip Location is :  Brussels, Belgium'), MessageBox.TYPE_INFO, timeout=10)
                            else:
                                self.session.open(MessageBox, _('Cannot connect (or server is down) !'), MessageBox.TYPE_INFO, timeout=5)
                            return              
                        elif returnValue =="com_26":
                            if connected_to_internet():
                               os.system('/etc/init.d/openvpn stop > /dev/null 2>&1')
                               os.system('rm -r %s > /dev/null 2>&1 && rm -f %s > /dev/null 2>&1' % (LINKFILE1, LINKFILE2))
                               os.system('rm -r -f /etc/openvpn; mkdir /etc/openvpn') 
                               shutil.copyfile('/etc/pointvpn/cfg_conf', '/etc/openvpn/cfg.conf')
                               shutil.copyfile('/etc/pointvpn/client_conf5', '/etc/openvpn/client.conf')
                               ip = compat_urlopen("http://ip.42.pl/raw").read()   
                               with open(LINKFILE1, "wb") as f: f.write(ip)                                   
                               f = open(LINKFILE1, 'r')
                               for line in f.readlines():
                                   IP = line.strip('\n')
                                   os.system('/etc/init.d/openvpn start > /dev/null 2>&1')
                                   time.sleep(8)
                                   ip2 = compat_urlopen("http://ip.42.pl/raw").read()  
                                   with open(LINKFILE2, "wb") as f: f.write(ip2)                                       
                                   f = open(LINKFILE2, 'r')
                                   for line in f.readlines():
                                       IP2 = line.strip('\n')
                                       if ip == ip2:
                                           self.session.open(MessageBox, _('VPN Not Working?...'), MessageBox.TYPE_INFO, timeout=5)
                                       else:
                                           self.session.open(MessageBox, _('Your Ip Address is :  ' + str(IP) + '\nYour New Ip Address is :  ' + str(IP2) + '\nYour Ip Location is :  Sofia, Bulgaria'), MessageBox.TYPE_INFO, timeout=10)
                            else:
                                self.session.open(MessageBox, _('Cannot connect (or server is down) !'), MessageBox.TYPE_INFO, timeout=5)
                            return
                        elif returnValue =="com_27":
                            if connected_to_internet():
                               os.system('/etc/init.d/openvpn stop > /dev/null 2>&1')
                               os.system('rm -r %s > /dev/null 2>&1 && rm -f %s > /dev/null 2>&1' % (LINKFILE1, LINKFILE2))
                               os.system('rm -r -f /etc/openvpn; mkdir /etc/openvpn') 
                               shutil.copyfile('/etc/pointvpn/cfg_conf', '/etc/openvpn/cfg.conf')
                               shutil.copyfile('/etc/pointvpn/client_conf6', '/etc/openvpn/client.conf')
                               ip = compat_urlopen("http://ip.42.pl/raw").read()   
                               with open(LINKFILE1, "wb") as f: f.write(ip)                                   
                               f = open(LINKFILE1, 'r')
                               for line in f.readlines():
                                   IP = line.strip('\n')
                                   os.system('/etc/init.d/openvpn start > /dev/null 2>&1')
                                   time.sleep(8)
                                   ip2 = compat_urlopen("http://ip.42.pl/raw").read()  
                                   with open(LINKFILE2, "wb") as f: f.write(ip2)                                       
                                   f = open(LINKFILE2, 'r')
                                   for line in f.readlines():
                                       IP2 = line.strip('\n')
                                       if ip == ip2:
                                           self.session.open(MessageBox, _('VPN Not Working?...'), MessageBox.TYPE_INFO, timeout=5)
                                       else:
                                           self.session.open(MessageBox, _('Your Ip Address is :  ' + str(IP) + '\nYour New Ip Address is :  ' + str(IP2) + '\nYour Ip Location is :  Sao Paulo, Brazil'), MessageBox.TYPE_INFO, timeout=10)
                            else:
                                self.session.open(MessageBox, _('Cannot connect (or server is down) !'), MessageBox.TYPE_INFO, timeout=5)
                            return              
                        elif returnValue =="com_28":
                            if connected_to_internet():
                               os.system('/etc/init.d/openvpn stop > /dev/null 2>&1')
                               os.system('rm -r %s > /dev/null 2>&1 && rm -f %s > /dev/null 2>&1' % (LINKFILE1, LINKFILE2))
                               os.system('rm -r -f /etc/openvpn; mkdir /etc/openvpn') 
                               shutil.copyfile('/etc/pointvpn/cfg_conf', '/etc/openvpn/cfg.conf')
                               shutil.copyfile('/etc/pointvpn/client_conf7', '/etc/openvpn/client.conf')
                               ip = compat_urlopen("http://ip.42.pl/raw").read()   
                               with open(LINKFILE1, "wb") as f: f.write(ip)                                   
                               f = open(LINKFILE1, 'r')
                               for line in f.readlines():
                                   IP = line.strip('\n')
                                   os.system('/etc/init.d/openvpn start > /dev/null 2>&1')
                                   time.sleep(8)
                                   ip2 = compat_urlopen("http://ip.42.pl/raw").read()  
                                   with open(LINKFILE2, "wb") as f: f.write(ip2)                                       
                                   f = open(LINKFILE2, 'r')
                                   for line in f.readlines():
                                       IP2 = line.strip('\n')
                                       if ip == ip2:
                                           self.session.open(MessageBox, _('VPN Not Working?...'), MessageBox.TYPE_INFO, timeout=5)
                                       else:
                                           self.session.open(MessageBox, _('Your Ip Address is :  ' + str(IP) + '\nYour New Ip Address is :  ' + str(IP2) + '\nYour Ip Location is :  Toronto, Canada'), MessageBox.TYPE_INFO, timeout=10)
                            else:
                                self.session.open(MessageBox, _('Cannot connect (or server is down) !'), MessageBox.TYPE_INFO, timeout=5)
                            return              
                        elif returnValue =="com_29":
                            if connected_to_internet():
                               os.system('/etc/init.d/openvpn stop > /dev/null 2>&1')
                               os.system('rm -r %s > /dev/null 2>&1 && rm -f %s > /dev/null 2>&1' % (LINKFILE1, LINKFILE2))
                               os.system('rm -r -f /etc/openvpn; mkdir /etc/openvpn') 
                               shutil.copyfile('/etc/pointvpn/cfg_conf', '/etc/openvpn/cfg.conf')
                               shutil.copyfile('/etc/pointvpn/client_conf8', '/etc/openvpn/client.conf')
                               ip = compat_urlopen("http://ip.42.pl/raw").read()   
                               with open(LINKFILE1, "wb") as f: f.write(ip)                                   
                               f = open(LINKFILE1, 'r')
                               for line in f.readlines():
                                   IP = line.strip('\n')
                                   os.system('/etc/init.d/openvpn start > /dev/null 2>&1')
                                   time.sleep(8)
                                   ip2 = compat_urlopen("http://ip.42.pl/raw").read()  
                                   with open(LINKFILE2, "wb") as f: f.write(ip2)                                       
                                   f = open(LINKFILE2, 'r')
                                   for line in f.readlines():
                                       IP2 = line.strip('\n')
                                       if ip == ip2:
                                           self.session.open(MessageBox, _('VPN Not Working?...'), MessageBox.TYPE_INFO, timeout=5)
                                       else:
                                           self.session.open(MessageBox, _('Your Ip Address is :  ' + str(IP) + '\nYour New Ip Address is :  ' + str(IP2) + '\nYour Ip Location is :  Montreal, Canada'), MessageBox.TYPE_INFO, timeout=10)
                            else:
                                self.session.open(MessageBox, _('Cannot connect (or server is down) !'), MessageBox.TYPE_INFO, timeout=5)
                            return              
                        elif returnValue =="com_30":
                            if connected_to_internet():
                               os.system('/etc/init.d/openvpn stop > /dev/null 2>&1')
                               os.system('rm -r %s > /dev/null 2>&1 && rm -f %s > /dev/null 2>&1' % (LINKFILE1, LINKFILE2))
                               os.system('rm -r -f /etc/openvpn; mkdir /etc/openvpn') 
                               shutil.copyfile('/etc/pointvpn/cfg_conf', '/etc/openvpn/cfg.conf')
                               shutil.copyfile('/etc/pointvpn/client_conf9', '/etc/openvpn/client.conf')
                               ip = compat_urlopen("http://ip.42.pl/raw").read()   
                               with open(LINKFILE1, "wb") as f: f.write(ip)                                   
                               f = open(LINKFILE1, 'r')
                               for line in f.readlines():
                                   IP = line.strip('\n')
                                   os.system('/etc/init.d/openvpn start > /dev/null 2>&1')
                                   time.sleep(8)
                                   ip2 = compat_urlopen("http://ip.42.pl/raw").read()  
                                   with open(LINKFILE2, "wb") as f: f.write(ip2)                                       
                                   f = open(LINKFILE2, 'r')
                                   for line in f.readlines():
                                       IP2 = line.strip('\n')
                                       if ip == ip2:
                                           self.session.open(MessageBox, _('VPN Not Working?...'), MessageBox.TYPE_INFO, timeout=5)
                                       else:
                                           self.session.open(MessageBox, _('Your Ip Address is :  ' + str(IP) + '\nYour New Ip Address is :  ' + str(IP2) + '\nYour Ip Location is :  Vancouver, Canada'), MessageBox.TYPE_INFO, timeout=10)
                            else:
                                self.session.open(MessageBox, _('Cannot connect (or server is down) !'), MessageBox.TYPE_INFO, timeout=5)
                            return              
                        elif returnValue =="com_31":
                            if connected_to_internet():
                               os.system('/etc/init.d/openvpn stop > /dev/null 2>&1')
                               os.system('rm -r %s > /dev/null 2>&1 && rm -f %s > /dev/null 2>&1' % (LINKFILE1, LINKFILE2))
                               os.system('rm -r -f /etc/openvpn; mkdir /etc/openvpn') 
                               shutil.copyfile('/etc/pointvpn/cfg_conf', '/etc/openvpn/cfg.conf')
                               shutil.copyfile('/etc/pointvpn/client_conf10', '/etc/openvpn/client.conf')
                               ip = compat_urlopen("http://ip.42.pl/raw").read()   
                               with open(LINKFILE1, "wb") as f: f.write(ip)                                   
                               f = open(LINKFILE1, 'r')
                               for line in f.readlines():
                                   IP = line.strip('\n')
                                   os.system('/etc/init.d/openvpn start > /dev/null 2>&1')
                                   time.sleep(8)
                                   ip2 = compat_urlopen("http://ip.42.pl/raw").read()  
                                   with open(LINKFILE2, "wb") as f: f.write(ip2)                                       
                                   f = open(LINKFILE2, 'r')
                                   for line in f.readlines():
                                       IP2 = line.strip('\n')
                                       if ip == ip2:
                                           self.session.open(MessageBox, _('VPN Not Working?...'), MessageBox.TYPE_INFO, timeout=5)
                                       else:
                                           self.session.open(MessageBox, _('Your Ip Address is :  ' + str(IP) + '\nYour New Ip Address is :  ' + str(IP2) + '\nYour Ip Location is :  Zurich, Switzerland'), MessageBox.TYPE_INFO, timeout=10)
                            else:
                                self.session.open(MessageBox, _('Cannot connect (or server is down) !'), MessageBox.TYPE_INFO, timeout=5)
                            return              
                        elif returnValue =="com_32":
                            if connected_to_internet():
                               os.system('/etc/init.d/openvpn stop > /dev/null 2>&1')
                               os.system('rm -r %s > /dev/null 2>&1 && rm -f %s > /dev/null 2>&1' % (LINKFILE1, LINKFILE2))
                               os.system('rm -r -f /etc/openvpn; mkdir /etc/openvpn') 
                               shutil.copyfile('/etc/pointvpn/cfg_conf', '/etc/openvpn/cfg.conf')
                               shutil.copyfile('/etc/pointvpn/client_conf11', '/etc/openvpn/client.conf')
                               ip = compat_urlopen("http://ip.42.pl/raw").read()   
                               with open(LINKFILE1, "wb") as f: f.write(ip)                                   
                               f = open(LINKFILE1, 'r')
                               for line in f.readlines():
                                   IP = line.strip('\n')
                                   os.system('/etc/init.d/openvpn start > /dev/null 2>&1')
                                   time.sleep(8)
                                   ip2 = compat_urlopen("http://ip.42.pl/raw").read()  
                                   with open(LINKFILE2, "wb") as f: f.write(ip2)                                       
                                   f = open(LINKFILE2, 'r')
                                   for line in f.readlines():
                                       IP2 = line.strip('\n')
                                       if ip == ip2:
                                           self.session.open(MessageBox, _('VPN Not Working?...'), MessageBox.TYPE_INFO, timeout=5)
                                       else:
                                           self.session.open(MessageBox, _('Your Ip Address is :  ' + str(IP) + '\nYour New Ip Address is :  ' + str(IP2) + '\nYour Ip Location is :  Prague, Czech Republic'), MessageBox.TYPE_INFO, timeout=10)
                            else:
                                self.session.open(MessageBox, _('Cannot connect (or server is down) !'), MessageBox.TYPE_INFO, timeout=5)
                            return
                        elif returnValue =="com_33":                            
                            if connected_to_internet():
                               os.system('/etc/init.d/openvpn stop > /dev/null 2>&1')
                               os.system('rm -r %s > /dev/null 2>&1 && rm -f %s > /dev/null 2>&1' % (LINKFILE1, LINKFILE2))
                               os.system('rm -r -f /etc/openvpn; mkdir /etc/openvpn') 
                               shutil.copyfile('/etc/pointvpn/cfg_conf', '/etc/openvpn/cfg.conf')
                               shutil.copyfile('/etc/pointvpn/client_conf12', '/etc/openvpn/client.conf')
                               ip = compat_urlopen("http://ip.42.pl/raw").read()   
                               with open(LINKFILE1, "wb") as f: f.write(ip)                                   
                               f = open(LINKFILE1, 'r')
                               for line in f.readlines():
                                   IP = line.strip('\n')
                                   os.system('/etc/init.d/openvpn start > /dev/null 2>&1')
                                   time.sleep(8)
                                   ip2 = compat_urlopen("http://ip.42.pl/raw").read()  
                                   with open(LINKFILE2, "wb") as f: f.write(ip2)                                       
                                   f = open(LINKFILE2, 'r')
                                   for line in f.readlines():
                                       IP2 = line.strip('\n')
                                       if ip == ip2:
                                           self.session.open(MessageBox, _('VPN Not Working?...'), MessageBox.TYPE_INFO, timeout=5)
                                       else:
                                           self.session.open(MessageBox, _('Your Ip Address is :  ' + str(IP) + '\nYour New Ip Address is :  ' + str(IP2) + '\nYour Ip Location is :  Frankfurt, Germany'), MessageBox.TYPE_INFO, timeout=10)
                            else:
                                self.session.open(MessageBox, _('Cannot connect (or server is down) !'), MessageBox.TYPE_INFO, timeout=5)
                            return
                        elif returnValue =="com_34":
                            if connected_to_internet():
                               os.system('/etc/init.d/openvpn stop > /dev/null 2>&1')
                               os.system('rm -r %s > /dev/null 2>&1 && rm -f %s > /dev/null 2>&1' % (LINKFILE1, LINKFILE2))
                               os.system('rm -r -f /etc/openvpn; mkdir /etc/openvpn') 
                               shutil.copyfile('/etc/pointvpn/cfg_conf', '/etc/openvpn/cfg.conf')
                               shutil.copyfile('/etc/pointvpn/client_conf13', '/etc/openvpn/client.conf')
                               ip = compat_urlopen("http://ip.42.pl/raw").read()   
                               with open(LINKFILE1, "wb") as f: f.write(ip)                                   
                               f = open(LINKFILE1, 'r')
                               for line in f.readlines():
                                   IP = line.strip('\n')
                                   os.system('/etc/init.d/openvpn start > /dev/null 2>&1')
                                   time.sleep(8)
                                   ip2 = compat_urlopen("http://ip.42.pl/raw").read()  
                                   with open(LINKFILE2, "wb") as f: f.write(ip2)                                       
                                   f = open(LINKFILE2, 'r')
                                   for line in f.readlines():
                                       IP2 = line.strip('\n')
                                       if ip == ip2:
                                           self.session.open(MessageBox, _('VPN Not Working?...'), MessageBox.TYPE_INFO, timeout=5)
                                       else:
                                           self.session.open(MessageBox, _('Your Ip Address is :  ' + str(IP) + '\nYour New Ip Address is :  ' + str(IP2) + '\nYour Ip Location is :  Dusseldorf, Germany'), MessageBox.TYPE_INFO, timeout=10)
                            else:
                                self.session.open(MessageBox, _('Cannot connect (or server is down) !'), MessageBox.TYPE_INFO, timeout=5)
                            return
                        elif returnValue =="com_35":
                            if connected_to_internet():
                               os.system('/etc/init.d/openvpn stop > /dev/null 2>&1')
                               os.system('rm -r %s > /dev/null 2>&1 && rm -f %s > /dev/null 2>&1' % (LINKFILE1, LINKFILE2))
                               os.system('rm -r -f /etc/openvpn; mkdir /etc/openvpn') 
                               shutil.copyfile('/etc/pointvpn/cfg_conf', '/etc/openvpn/cfg.conf')
                               shutil.copyfile('/etc/pointvpn/client_conf14', '/etc/openvpn/client.conf')
                               ip = compat_urlopen("http://ip.42.pl/raw").read()   
                               with open(LINKFILE1, "wb") as f: f.write(ip)                                   
                               f = open(LINKFILE1, 'r')
                               for line in f.readlines():
                                   IP = line.strip('\n')
                                   os.system('/etc/init.d/openvpn start > /dev/null 2>&1')
                                   time.sleep(8)
                                   ip2 = compat_urlopen("http://ip.42.pl/raw").read()  
                                   with open(LINKFILE2, "wb") as f: f.write(ip2)                                       
                                   f = open(LINKFILE2, 'r')
                                   for line in f.readlines():
                                       IP2 = line.strip('\n')
                                       if ip == ip2:
                                           self.session.open(MessageBox, _('VPN Not Working?...'), MessageBox.TYPE_INFO, timeout=5)
                                       else:
                                           self.session.open(MessageBox, _('Your Ip Address is :  ' + str(IP) + '\nYour New Ip Address is :  ' + str(IP2) + '\nYour Ip Location is :  Seville, Spain'), MessageBox.TYPE_INFO, timeout=10)
                            else:
                                self.session.open(MessageBox, _('Cannot connect (or server is down) !'), MessageBox.TYPE_INFO, timeout=5)
                            return
                        elif returnValue =="com_36":
                            if connected_to_internet():
                               os.system('/etc/init.d/openvpn stop > /dev/null 2>&1')
                               os.system('rm -r %s > /dev/null 2>&1 && rm -f %s > /dev/null 2>&1' % (LINKFILE1, LINKFILE2))
                               os.system('rm -r -f /etc/openvpn; mkdir /etc/openvpn') 
                               shutil.copyfile('/etc/pointvpn/cfg_conf', '/etc/openvpn/cfg.conf')
                               shutil.copyfile('/etc/pointvpn/client_conf15', '/etc/openvpn/client.conf')
                               ip = compat_urlopen("http://ip.42.pl/raw").read()   
                               with open(LINKFILE1, "wb") as f: f.write(ip)                                   
                               f = open(LINKFILE1, 'r')
                               for line in f.readlines():
                                   IP = line.strip('\n')
                                   os.system('/etc/init.d/openvpn start > /dev/null 2>&1')
                                   time.sleep(8)
                                   ip2 = compat_urlopen("http://ip.42.pl/raw").read()  
                                   with open(LINKFILE2, "wb") as f: f.write(ip2)                                       
                                   f = open(LINKFILE2, 'r')
                                   for line in f.readlines():
                                       IP2 = line.strip('\n')
                                       if ip == ip2:
                                           self.session.open(MessageBox, _('VPN Not Working?...'), MessageBox.TYPE_INFO, timeout=5)
                                       else:
                                           self.session.open(MessageBox, _('Your Ip Address is :  ' + str(IP) + '\nYour New Ip Address is :  ' + str(IP2) + '\nYour Ip Location is :  Barcelona, Spain'), MessageBox.TYPE_INFO, timeout=10)
                            else:
                                self.session.open(MessageBox, _('Cannot connect (or server is down) !'), MessageBox.TYPE_INFO, timeout=5)
                            return              
                        elif returnValue =="com_37":
                            if connected_to_internet():
                               os.system('/etc/init.d/openvpn stop > /dev/null 2>&1')
                               os.system('rm -r %s > /dev/null 2>&1 && rm -f %s > /dev/null 2>&1' % (LINKFILE1, LINKFILE2))
                               os.system('rm -r -f /etc/openvpn; mkdir /etc/openvpn') 
                               shutil.copyfile('/etc/pointvpn/cfg_conf', '/etc/openvpn/cfg.conf')
                               shutil.copyfile('/etc/pointvpn/client_conf16', '/etc/openvpn/client.conf')
                               ip = compat_urlopen("http://ip.42.pl/raw").read()   
                               with open(LINKFILE1, "wb") as f: f.write(ip)                                   
                               f = open(LINKFILE1, 'r')
                               for line in f.readlines():
                                   IP = line.strip('\n')
                                   os.system('/etc/init.d/openvpn start > /dev/null 2>&1')
                                   time.sleep(8)
                                   ip2 = compat_urlopen("http://ip.42.pl/raw").read()  
                                   with open(LINKFILE2, "wb") as f: f.write(ip2)                                       
                                   f = open(LINKFILE2, 'r')
                                   for line in f.readlines():
                                       IP2 = line.strip('\n')
                                       if ip == ip2:
                                           self.session.open(MessageBox, _('VPN Not Working?...'), MessageBox.TYPE_INFO, timeout=5)
                                       else:
                                           self.session.open(MessageBox, _('Your Ip Address is :  ' + str(IP) + '\nYour New Ip Address is :  ' + str(IP2) + '\nYour Ip Location is :  Helsinki, Finland'), MessageBox.TYPE_INFO, timeout=10)
                            else:
                                self.session.open(MessageBox, _('Cannot connect (or server is down) !'), MessageBox.TYPE_INFO, timeout=5)
                            return                      
                        elif returnValue =="com_38":
                            if connected_to_internet():
                               os.system('/etc/init.d/openvpn stop > /dev/null 2>&1')
                               os.system('rm -r %s > /dev/null 2>&1 && rm -f %s > /dev/null 2>&1' % (LINKFILE1, LINKFILE2))
                               os.system('rm -r -f /etc/openvpn; mkdir /etc/openvpn') 
                               shutil.copyfile('/etc/pointvpn/cfg_conf', '/etc/openvpn/cfg.conf')
                               shutil.copyfile('/etc/pointvpn/client_conf17', '/etc/openvpn/client.conf')
                               ip = compat_urlopen("http://ip.42.pl/raw").read()   
                               with open(LINKFILE1, "wb") as f: f.write(ip)                                   
                               f = open(LINKFILE1, 'r')
                               for line in f.readlines():
                                   IP = line.strip('\n')
                                   os.system('/etc/init.d/openvpn start > /dev/null 2>&1')
                                   time.sleep(8)
                                   ip2 = compat_urlopen("http://ip.42.pl/raw").read()  
                                   with open(LINKFILE2, "wb") as f: f.write(ip2)                                       
                                   f = open(LINKFILE2, 'r')
                                   for line in f.readlines():
                                       IP2 = line.strip('\n')
                                       if ip == ip2:
                                           self.session.open(MessageBox, _('VPN Not Working?...'), MessageBox.TYPE_INFO, timeout=5)
                                       else:
                                           self.session.open(MessageBox, _('Your Ip Address is :  ' + str(IP) + '\nYour New Ip Address is :  ' + str(IP2) + '\nYour Ip Location is :  Helsinki 2, Finland'), MessageBox.TYPE_INFO, timeout=10)
                            else:
                                self.session.open(MessageBox, _('Cannot connect (or server is down) !'), MessageBox.TYPE_INFO, timeout=5)
                            return                      
                        elif returnValue =="com_39":
                            if connected_to_internet():
                               os.system('/etc/init.d/openvpn stop > /dev/null 2>&1')
                               os.system('rm -r %s > /dev/null 2>&1 && rm -f %s > /dev/null 2>&1' % (LINKFILE1, LINKFILE2))
                               os.system('rm -r -f /etc/openvpn; mkdir /etc/openvpn') 
                               shutil.copyfile('/etc/pointvpn/cfg_conf', '/etc/openvpn/cfg.conf')
                               shutil.copyfile('/etc/pointvpn/client_conf18', '/etc/openvpn/client.conf')
                               ip = compat_urlopen("http://ip.42.pl/raw").read()   
                               with open(LINKFILE1, "wb") as f: f.write(ip)                                   
                               f = open(LINKFILE1, 'r')
                               for line in f.readlines():
                                   IP = line.strip('\n')
                                   os.system('/etc/init.d/openvpn start > /dev/null 2>&1')
                                   time.sleep(8)
                                   ip2 = compat_urlopen("http://ip.42.pl/raw").read()  
                                   with open(LINKFILE2, "wb") as f: f.write(ip2)                                       
                                   f = open(LINKFILE2, 'r')
                                   for line in f.readlines():
                                       IP2 = line.strip('\n')
                                       if ip == ip2:
                                           self.session.open(MessageBox, _('VPN Not Working?...'), MessageBox.TYPE_INFO, timeout=5)
                                       else:
                                           self.session.open(MessageBox, _('Your Ip Address is :  ' + str(IP) + '\nYour New Ip Address is :  ' + str(IP2) + '\nYour Ip Location is :  Paris, France'), MessageBox.TYPE_INFO, timeout=10)
                            else:
                                self.session.open(MessageBox, _('Cannot connect (or server is down) !'), MessageBox.TYPE_INFO, timeout=5)
                            return
                        elif returnValue =="com_40":
                            if connected_to_internet():
                               os.system('/etc/init.d/openvpn stop > /dev/null 2>&1')
                               os.system('rm -r %s > /dev/null 2>&1 && rm -f %s > /dev/null 2>&1' % (LINKFILE1, LINKFILE2))
                               os.system('rm -r -f /etc/openvpn; mkdir /etc/openvpn') 
                               shutil.copyfile('/etc/pointvpn/cfg_conf', '/etc/openvpn/cfg.conf')
                               shutil.copyfile('/etc/pointvpn/client_conf19', '/etc/openvpn/client.conf')
                               ip = compat_urlopen("http://ip.42.pl/raw").read()   
                               with open(LINKFILE1, "wb") as f: f.write(ip)                                   
                               f = open(LINKFILE1, 'r')
                               for line in f.readlines():
                                   IP = line.strip('\n')
                                   os.system('/etc/init.d/openvpn start > /dev/null 2>&1')
                                   time.sleep(8)
                                   ip2 = compat_urlopen("http://ip.42.pl/raw").read()  
                                   with open(LINKFILE2, "wb") as f: f.write(ip2)                                       
                                   f = open(LINKFILE2, 'r')
                                   for line in f.readlines():
                                       IP2 = line.strip('\n')
                                       if ip == ip2:
                                           self.session.open(MessageBox, _('VPN Not Working?...'), MessageBox.TYPE_INFO, timeout=5)
                                       else:
                                           self.session.open(MessageBox, _('Your Ip Address is :  ' + str(IP) + '\nYour New Ip Address is :  ' + str(IP2) + '\nYour Ip Location is :  London, United Kingdom'), MessageBox.TYPE_INFO, timeout=10)
                            else:
                                self.session.open(MessageBox, _('Cannot connect (or server is down) !'), MessageBox.TYPE_INFO, timeout=5)
                            return
                        elif returnValue =="com_41":
                            if connected_to_internet():
                               os.system('/etc/init.d/openvpn stop > /dev/null 2>&1')
                               os.system('rm -r %s > /dev/null 2>&1 && rm -f %s > /dev/null 2>&1' % (LINKFILE1, LINKFILE2))
                               os.system('rm -r -f /etc/openvpn; mkdir /etc/openvpn') 
                               shutil.copyfile('/etc/pointvpn/cfg_conf', '/etc/openvpn/cfg.conf')
                               shutil.copyfile('/etc/pointvpn/client_conf20', '/etc/openvpn/client.conf')
                               ip = compat_urlopen("http://ip.42.pl/raw").read()   
                               with open(LINKFILE1, "wb") as f: f.write(ip)                                   
                               f = open(LINKFILE1, 'r')
                               for line in f.readlines():
                                   IP = line.strip('\n')
                                   os.system('/etc/init.d/openvpn start > /dev/null 2>&1')
                                   time.sleep(8)
                                   ip2 = compat_urlopen("http://ip.42.pl/raw").read()  
                                   with open(LINKFILE2, "wb") as f: f.write(ip2)                                       
                                   f = open(LINKFILE2, 'r')
                                   for line in f.readlines():
                                       IP2 = line.strip('\n')
                                       if ip == ip2:
                                           self.session.open(MessageBox, _('VPN Not Working?...'), MessageBox.TYPE_INFO, timeout=5)
                                       else:
                                           self.session.open(MessageBox, _('Your Ip Address is :  ' + str(IP) + '\nYour New Ip Address is :  ' + str(IP2) + '\nYour Ip Location is :  London 2, United Kingdom'), MessageBox.TYPE_INFO, timeout=10)
                            else:
                                self.session.open(MessageBox, _('Cannot connect (or server is down) !'), MessageBox.TYPE_INFO, timeout=5)
                            return
                        elif returnValue =="com_42":
                            if connected_to_internet():
                               os.system('/etc/init.d/openvpn stop > /dev/null 2>&1')
                               os.system('rm -r %s > /dev/null 2>&1 && rm -f %s > /dev/null 2>&1' % (LINKFILE1, LINKFILE2))
                               os.system('rm -r -f /etc/openvpn; mkdir /etc/openvpn') 
                               shutil.copyfile('/etc/pointvpn/cfg_conf', '/etc/openvpn/cfg.conf')
                               shutil.copyfile('/etc/pointvpn/client_conf21', '/etc/openvpn/client.conf')
                               ip = compat_urlopen("http://ip.42.pl/raw").read()   
                               with open(LINKFILE1, "wb") as f: f.write(ip)                                   
                               f = open(LINKFILE1, 'r')
                               for line in f.readlines():
                                   IP = line.strip('\n')
                                   os.system('/etc/init.d/openvpn start > /dev/null 2>&1')
                                   time.sleep(8)
                                   ip2 = compat_urlopen("http://ip.42.pl/raw").read()  
                                   with open(LINKFILE2, "wb") as f: f.write(ip2)                                       
                                   f = open(LINKFILE2, 'r')
                                   for line in f.readlines():
                                       IP2 = line.strip('\n')
                                       if ip == ip2:
                                           self.session.open(MessageBox, _('VPN Not Working?...'), MessageBox.TYPE_INFO, timeout=5)
                                       else:
                                           self.session.open(MessageBox, _('Your Ip Address is :  ' + str(IP) + '\nYour New Ip Address is :  ' + str(IP2) + '\nYour Ip Location is :  Thessaloniki, Greece'), MessageBox.TYPE_INFO, timeout=10)
                            else:
                                self.session.open(MessageBox, _('Cannot connect (or server is down) !'), MessageBox.TYPE_INFO, timeout=5)
                            return
                        elif returnValue =="com_43":
                            if connected_to_internet():
                               os.system('/etc/init.d/openvpn stop > /dev/null 2>&1')
                               os.system('rm -r %s > /dev/null 2>&1 && rm -f %s > /dev/null 2>&1' % (LINKFILE1, LINKFILE2))
                               os.system('rm -r -f /etc/openvpn; mkdir /etc/openvpn') 
                               shutil.copyfile('/etc/pointvpn/cfg_conf', '/etc/openvpn/cfg.conf')
                               shutil.copyfile('/etc/pointvpn/client_conf22', '/etc/openvpn/client.conf')
                               ip = compat_urlopen("http://ip.42.pl/raw").read()   
                               with open(LINKFILE1, "wb") as f: f.write(ip)                                   
                               f = open(LINKFILE1, 'r')
                               for line in f.readlines():
                                   IP = line.strip('\n')
                                   os.system('/etc/init.d/openvpn start > /dev/null 2>&1')
                                   time.sleep(8)
                                   ip2 = compat_urlopen("http://ip.42.pl/raw").read()  
                                   with open(LINKFILE2, "wb") as f: f.write(ip2)                                       
                                   f = open(LINKFILE2, 'r')
                                   for line in f.readlines():
                                       IP2 = line.strip('\n')
                                       if ip == ip2:
                                           self.session.open(MessageBox, _('VPN Not Working?...'), MessageBox.TYPE_INFO, timeout=5)
                                       else:
                                           self.session.open(MessageBox, _('Your Ip Address is :  ' + str(IP) + '\nYour New Ip Address is :  ' + str(IP2) + '\nYour Ip Location is :  Hong Kong, Hong Kong'), MessageBox.TYPE_INFO, timeout=10)
                            else:
                                self.session.open(MessageBox, _('Cannot connect (or server is down) !'), MessageBox.TYPE_INFO, timeout=5)
                            return
                        elif returnValue =="com_44":
                            if connected_to_internet():
                               os.system('/etc/init.d/openvpn stop > /dev/null 2>&1')
                               os.system('rm -r %s > /dev/null 2>&1 && rm -f %s > /dev/null 2>&1' % (LINKFILE1, LINKFILE2))
                               os.system('rm -r -f /etc/openvpn; mkdir /etc/openvpn') 
                               shutil.copyfile('/etc/pointvpn/cfg_conf', '/etc/openvpn/cfg.conf')
                               shutil.copyfile('/etc/pointvpn/client_conf23', '/etc/openvpn/client.conf')
                               ip = compat_urlopen("http://ip.42.pl/raw").read()   
                               with open(LINKFILE1, "wb") as f: f.write(ip)                                   
                               f = open(LINKFILE1, 'r')
                               for line in f.readlines():
                                   IP = line.strip('\n')
                                   os.system('/etc/init.d/openvpn start > /dev/null 2>&1')
                                   time.sleep(8)
                                   ip2 = compat_urlopen("http://ip.42.pl/raw").read()  
                                   with open(LINKFILE2, "wb") as f: f.write(ip2)                                       
                                   f = open(LINKFILE2, 'r')
                                   for line in f.readlines():
                                       IP2 = line.strip('\n')
                                       if ip == ip2:
                                           self.session.open(MessageBox, _('VPN Not Working?...'), MessageBox.TYPE_INFO, timeout=5)
                                       else:
                                           self.session.open(MessageBox, _('Your Ip Address is :  ' + str(IP) + '\nYour New Ip Address is :  ' + str(IP2) + '\nYour Ip Location is :  Jakarta 6, Indonesia'), MessageBox.TYPE_INFO, timeout=10)
                            else:
                                self.session.open(MessageBox, _('Cannot connect (or server is down) !'), MessageBox.TYPE_INFO, timeout=5)
                            return
                        elif returnValue =="com_45":
                            if connected_to_internet():
                               os.system('/etc/init.d/openvpn stop > /dev/null 2>&1')
                               os.system('rm -r %s > /dev/null 2>&1 && rm -f %s > /dev/null 2>&1' % (LINKFILE1, LINKFILE2))
                               os.system('rm -r -f /etc/openvpn; mkdir /etc/openvpn') 
                               shutil.copyfile('/etc/pointvpn/cfg_conf', '/etc/openvpn/cfg.conf')
                               shutil.copyfile('/etc/pointvpn/client_conf24', '/etc/openvpn/client.conf')
                               ip = compat_urlopen("http://ip.42.pl/raw").read()   
                               with open(LINKFILE1, "wb") as f: f.write(ip)                                   
                               f = open(LINKFILE1, 'r')
                               for line in f.readlines():
                                   IP = line.strip('\n')
                                   os.system('/etc/init.d/openvpn start > /dev/null 2>&1')
                                   time.sleep(8)
                                   ip2 = compat_urlopen("http://ip.42.pl/raw").read()  
                                   with open(LINKFILE2, "wb") as f: f.write(ip2)                                       
                                   f = open(LINKFILE2, 'r')
                                   for line in f.readlines():
                                       IP2 = line.strip('\n')
                                       if ip == ip2:
                                           self.session.open(MessageBox, _('VPN Not Working?...'), MessageBox.TYPE_INFO, timeout=5)
                                       else:
                                           self.session.open(MessageBox, _('Your Ip Address is :  ' + str(IP) + '\nYour New Ip Address is :  ' + str(IP2) + '\nYour Ip Location is :  Jakarta 5, Indonesia'), MessageBox.TYPE_INFO, timeout=10)
                            else:
                                self.session.open(MessageBox, _('Cannot connect (or server is down) !'), MessageBox.TYPE_INFO, timeout=5)
                            return
                        elif returnValue =="com_46":
                            if connected_to_internet():
                               os.system('/etc/init.d/openvpn stop > /dev/null 2>&1')
                               os.system('rm -r %s > /dev/null 2>&1 && rm -f %s > /dev/null 2>&1' % (LINKFILE1, LINKFILE2))
                               os.system('rm -r -f /etc/openvpn; mkdir /etc/openvpn') 
                               shutil.copyfile('/etc/pointvpn/cfg_conf', '/etc/openvpn/cfg.conf')
                               shutil.copyfile('/etc/etc/pointvpn/client_conf25', '/etc/openvpn/client.conf')
                               ip = compat_urlopen("http://ip.42.pl/raw").read()   
                               with open(LINKFILE1, "wb") as f: f.write(ip)                                   
                               f = open(LINKFILE1, 'r')
                               for line in f.readlines():
                                   IP = line.strip('\n')
                                   os.system('/etc/init.d/openvpn start > /dev/null 2>&1')
                                   time.sleep(8)
                                   ip2 = compat_urlopen("http://ip.42.pl/raw").read()  
                                   with open(LINKFILE2, "wb") as f: f.write(ip2)                                       
                                   f = open(LINKFILE2, 'r')
                                   for line in f.readlines():
                                       IP2 = line.strip('\n')
                                       if ip == ip2:
                                           self.session.open(MessageBox, _('VPN Not Working?...'), MessageBox.TYPE_INFO, timeout=5)
                                       else:
                                           self.session.open(MessageBox, _('Your Ip Address is :  ' + str(IP) + '\nYour New Ip Address is :  ' + str(IP2) + '\nYour Ip Location is :  Dublin, Ireland'), MessageBox.TYPE_INFO, timeout=10)
                            else:
                                self.session.open(MessageBox, _('Cannot connect (or server is down) !'), MessageBox.TYPE_INFO, timeout=5)
                            return
                        elif returnValue =="com_47":
                            if connected_to_internet():
                               os.system('/etc/init.d/openvpn stop > /dev/null 2>&1')
                               os.system('rm -r %s > /dev/null 2>&1 && rm -f %s > /dev/null 2>&1' % (LINKFILE1, LINKFILE2))
                               os.system('rm -r -f /etc/openvpn; mkdir /etc/openvpn') 
                               shutil.copyfile('/etc/pointvpn/cfg_conf', '/etc/openvpn/cfg.conf')
                               shutil.copyfile('/etc/pointvpn/client_conf26', '/etc/openvpn/client.conf')
                               ip = compat_urlopen("http://ip.42.pl/raw").read()   
                               with open(LINKFILE1, "wb") as f: f.write(ip)                                   
                               f = open(LINKFILE1, 'r')
                               for line in f.readlines():
                                   IP = line.strip('\n')
                                   os.system('/etc/init.d/openvpn start > /dev/null 2>&1')
                                   time.sleep(8)
                                   ip2 = compat_urlopen("http://ip.42.pl/raw").read()  
                                   with open(LINKFILE2, "wb") as f: f.write(ip2)                                       
                                   f = open(LINKFILE2, 'r')
                                   for line in f.readlines():
                                       IP2 = line.strip('\n')
                                       if ip == ip2:
                                           self.session.open(MessageBox, _('VPN Not Working?...'), MessageBox.TYPE_INFO, timeout=5)
                                       else:
                                           self.session.open(MessageBox, _('Your Ip Address is :  ' + str(IP) + '\nYour New Ip Address is :  ' + str(IP2) + '\nYour Ip Location is :  Tel Aviv, Israel'), MessageBox.TYPE_INFO, timeout=10)
                            else:
                                self.session.open(MessageBox, _('Cannot connect (or server is down) !'), MessageBox.TYPE_INFO, timeout=5)
                            return
                        elif returnValue =="com_48":
                            if connected_to_internet():
                               os.system('/etc/init.d/openvpn stop > /dev/null 2>&1')
                               os.system('rm -r %s > /dev/null 2>&1 && rm -f %s > /dev/null 2>&1' % (LINKFILE1, LINKFILE2))
                               os.system('rm -r -f /etc/openvpn; mkdir /etc/openvpn') 
                               shutil.copyfile('/etc/pointvpn/cfg_conf', '/etc/openvpn/cfg.conf')
                               shutil.copyfile('/etc/pointvpn/client_conf27', '/etc/openvpn/client.conf')
                               ip = compat_urlopen("http://ip.42.pl/raw").read()   
                               with open(LINKFILE1, "wb") as f: f.write(ip)                                   
                               f = open(LINKFILE1, 'r')
                               for line in f.readlines():
                                   IP = line.strip('\n')
                                   os.system('/etc/init.d/openvpn start > /dev/null 2>&1')
                                   time.sleep(8)
                                   ip2 = compat_urlopen("http://ip.42.pl/raw").read()  
                                   with open(LINKFILE2, "wb") as f: f.write(ip2)                                       
                                   f = open(LINKFILE2, 'r')
                                   for line in f.readlines():
                                       IP2 = line.strip('\n')
                                       if ip == ip2:
                                           self.session.open(MessageBox, _('VPN Not Working?...'), MessageBox.TYPE_INFO, timeout=5)
                                       else:
                                           self.session.open(MessageBox, _('Your Ip Address is :  ' + str(IP) + '\nYour New Ip Address is :  ' + str(IP2) + '\nYour Ip Location is :  Mumbai, India'), MessageBox.TYPE_INFO, timeout=10)
                            else:
                                self.session.open(MessageBox, _('Cannot connect (or server is down) !'), MessageBox.TYPE_INFO, timeout=5)
                            return  
                        elif returnValue =="com_49":
                            if connected_to_internet():
                               os.system('/etc/init.d/openvpn stop > /dev/null 2>&1')
                               os.system('rm -r %s > /dev/null 2>&1 && rm -f %s > /dev/null 2>&1' % (LINKFILE1, LINKFILE2))
                               os.system('rm -r -f /etc/openvpn; mkdir /etc/openvpn') 
                               shutil.copyfile('/etc/pointvpn/cfg_conf', '/etc/openvpn/cfg.conf')
                               shutil.copyfile('/etc/pointvpn/client_conf28', '/etc/openvpn/client.conf')
                               ip = compat_urlopen("http://ip.42.pl/raw").read()   
                               with open(LINKFILE1, "wb") as f: f.write(ip)                                   
                               f = open(LINKFILE1, 'r')
                               for line in f.readlines():
                                   IP = line.strip('\n')
                                   os.system('/etc/init.d/openvpn start > /dev/null 2>&1')
                                   time.sleep(8)
                                   ip2 = compat_urlopen("http://ip.42.pl/raw").read()  
                                   with open(LINKFILE2, "wb") as f: f.write(ip2)                                       
                                   f = open(LINKFILE2, 'r')
                                   for line in f.readlines():
                                       IP2 = line.strip('\n')
                                       if ip == ip2:
                                           self.session.open(MessageBox, _('VPN Not Working?...'), MessageBox.TYPE_INFO, timeout=5)
                                       else:
                                           self.session.open(MessageBox, _('Your Ip Address is :  ' + str(IP) + '\nYour New Ip Address is :  ' + str(IP2) + '\nYour Ip Location is :  Palermo, Italy'), MessageBox.TYPE_INFO, timeout=10)
                            else:
                                self.session.open(MessageBox, _('Cannot connect (or server is down) !'), MessageBox.TYPE_INFO, timeout=5)
                            return                      
                        elif returnValue =="com_50":
                            if connected_to_internet():
                               os.system('/etc/init.d/openvpn stop > /dev/null 2>&1')
                               os.system('rm -r %s > /dev/null 2>&1 && rm -f %s > /dev/null 2>&1' % (LINKFILE1, LINKFILE2))
                               os.system('rm -r -f /etc/openvpn; mkdir /etc/openvpn') 
                               shutil.copyfile('/etc/pointvpn/cfg_conf', '/etc/openvpn/cfg.conf')
                               shutil.copyfile('/etc/pointvpn/client_conf29', '/etc/openvpn/client.conf')
                               ip = compat_urlopen("http://ip.42.pl/raw").read()   
                               with open(LINKFILE1, "wb") as f: f.write(ip)                                   
                               f = open(LINKFILE1, 'r')
                               for line in f.readlines():
                                   IP = line.strip('\n')
                                   os.system('/etc/init.d/openvpn start > /dev/null 2>&1')
                                   time.sleep(8)
                                   ip2 = compat_urlopen("http://ip.42.pl/raw").read()  
                                   with open(LINKFILE2, "wb") as f: f.write(ip2)                                       
                                   f = open(LINKFILE2, 'r')
                                   for line in f.readlines():
                                       IP2 = line.strip('\n')
                                       if ip == ip2:
                                           self.session.open(MessageBox, _('VPN Not Working?...'), MessageBox.TYPE_INFO, timeout=5)
                                       else:
                                           self.session.open(MessageBox, _('Your Ip Address is :  ' + str(IP) + '\nYour New Ip Address is :  ' + str(IP2) + '\nYour Ip Location is :  Tokyo 6, Japan'), MessageBox.TYPE_INFO, timeout=10)
                            else:
                                self.session.open(MessageBox, _('Cannot connect (or server is down) !'), MessageBox.TYPE_INFO, timeout=5)
                            return              
                        elif returnValue =="com_51":
                            if connected_to_internet():
                               os.system('/etc/init.d/openvpn stop > /dev/null 2>&1')
                               os.system('rm -r %s > /dev/null 2>&1 && rm -f %s > /dev/null 2>&1' % (LINKFILE1, LINKFILE2))
                               os.system('rm -r -f /etc/openvpn; mkdir /etc/openvpn') 
                               shutil.copyfile('/etc/pointvpn/cfg_conf', '/etc/openvpn/cfg.conf')
                               shutil.copyfile('/etc/pointvpn/client_conf30', '/etc/openvpn/client.conf')
                               ip = compat_urlopen("http://ip.42.pl/raw").read()   
                               with open(LINKFILE1, "wb") as f: f.write(ip)                                   
                               f = open(LINKFILE1, 'r')
                               for line in f.readlines():
                                   IP = line.strip('\n')
                                   os.system('/etc/init.d/openvpn start > /dev/null 2>&1')
                                   time.sleep(8)
                                   ip2 = compat_urlopen("http://ip.42.pl/raw").read()  
                                   with open(LINKFILE2, "wb") as f: f.write(ip2)                                       
                                   f = open(LINKFILE2, 'r')
                                   for line in f.readlines():
                                       IP2 = line.strip('\n')
                                       if ip == ip2:
                                           self.session.open(MessageBox, _('VPN Not Working?...'), MessageBox.TYPE_INFO, timeout=5)
                                       else:
                                           self.session.open(MessageBox, _('Your Ip Address is :  ' + str(IP) + '\nYour New Ip Address is :  ' + str(IP2) + '\nYour Ip Location is :  Tokyo 2, Japan'), MessageBox.TYPE_INFO, timeout=10)
                            else:
                                self.session.open(MessageBox, _('Cannot connect (or server is down) !'), MessageBox.TYPE_INFO, timeout=5)
                            return
                        elif returnValue =="com_52":
                            if connected_to_internet():
                               os.system('/etc/init.d/openvpn stop > /dev/null 2>&1')
                               os.system('rm -r %s > /dev/null 2>&1 && rm -f %s > /dev/null 2>&1' % (LINKFILE1, LINKFILE2))
                               os.system('rm -r -f /etc/openvpn; mkdir /etc/openvpn') 
                               shutil.copyfile('/etc/pointvpn/cfg_conf', '/etc/openvpn/cfg.conf')
                               shutil.copyfile('/etc/pointvpn/client_conf31', '/etc/openvpn/client.conf')
                               ip = compat_urlopen("http://ip.42.pl/raw").read()   
                               with open(LINKFILE1, "wb") as f: f.write(ip)                                   
                               f = open(LINKFILE1, 'r')
                               for line in f.readlines():
                                   IP = line.strip('\n')
                                   os.system('/etc/init.d/openvpn start > /dev/null 2>&1')
                                   time.sleep(8)
                                   ip2 = compat_urlopen("http://ip.42.pl/raw").read()  
                                   with open(LINKFILE2, "wb") as f: f.write(ip2)                                       
                                   f = open(LINKFILE2, 'r')
                                   for line in f.readlines():
                                       IP2 = line.strip('\n')
                                       if ip == ip2:
                                           self.session.open(MessageBox, _('VPN Not Working?...'), MessageBox.TYPE_INFO, timeout=5)
                                       else:
                                           self.session.open(MessageBox, _('Your Ip Address is :  ' + str(IP) + '\nYour New Ip Address is :  ' + str(IP2) + '\nYour Ip Location is :  Tokyo, Japan'), MessageBox.TYPE_INFO, timeout=10)
                            else:
                                self.session.open(MessageBox, _('Cannot connect (or server is down) !'), MessageBox.TYPE_INFO, timeout=5)
                            return
                        elif returnValue =="com_53":
                            if connected_to_internet():
                               os.system('/etc/init.d/openvpn stop > /dev/null 2>&1')
                               os.system('rm -r %s > /dev/null 2>&1 && rm -f %s > /dev/null 2>&1' % (LINKFILE1, LINKFILE2))
                               os.system('rm -r -f /etc/openvpn; mkdir /etc/openvpn') 
                               shutil.copyfile('/etc/pointvpn/cfg_conf', '/etc/openvpn/cfg.conf')
                               shutil.copyfile('/etc/pointvpn/client_conf32', '/etc/openvpn/client.conf')
                               ip = compat_urlopen("http://ip.42.pl/raw").read()   
                               with open(LINKFILE1, "wb") as f: f.write(ip)                                   
                               f = open(LINKFILE1, 'r')
                               for line in f.readlines():
                                   IP = line.strip('\n')
                                   os.system('/etc/init.d/openvpn start > /dev/null 2>&1')
                                   time.sleep(8)
                                   ip2 = compat_urlopen("http://ip.42.pl/raw").read()  
                                   with open(LINKFILE2, "wb") as f: f.write(ip2)                                       
                                   f = open(LINKFILE2, 'r')
                                   for line in f.readlines():
                                       IP2 = line.strip('\n')
                                       if ip == ip2:
                                           self.session.open(MessageBox, _('VPN Not Working?...'), MessageBox.TYPE_INFO, timeout=5)
                                       else:
                                           self.session.open(MessageBox, _('Your Ip Address is :  ' + str(IP) + '\nYour New Ip Address is :  ' + str(IP2) + '\nYour Ip Location is :  Rotterdam, Netherlands'), MessageBox.TYPE_INFO, timeout=10)
                            else:
                                self.session.open(MessageBox, _('Cannot connect (or server is down) !'), MessageBox.TYPE_INFO, timeout=5)
                            return
                        elif returnValue =="com_54":
                            if connected_to_internet():
                               os.system('/etc/init.d/openvpn stop > /dev/null 2>&1')
                               os.system('rm -r %s > /dev/null 2>&1 && rm -f %s > /dev/null 2>&1' % (LINKFILE1, LINKFILE2))
                               os.system('rm -r -f /etc/openvpn; mkdir /etc/openvpn') 
                               shutil.copyfile('/etc/pointvpn/cfg_conf', '/etc/openvpn/cfg.conf')
                               shutil.copyfile('/etc/pointvpn/client_conf33', '/etc/openvpn/client.conf')
                               ip = compat_urlopen("http://ip.42.pl/raw").read()   
                               with open(LINKFILE1, "wb") as f: f.write(ip)                                   
                               f = open(LINKFILE1, 'r')
                               for line in f.readlines():
                                   IP = line.strip('\n')
                                   os.system('/etc/init.d/openvpn start > /dev/null 2>&1')
                                   time.sleep(8)
                                   ip2 = compat_urlopen("http://ip.42.pl/raw").read()  
                                   with open(LINKFILE2, "wb") as f: f.write(ip2)                                       
                                   f = open(LINKFILE2, 'r')
                                   for line in f.readlines():
                                       IP2 = line.strip('\n')
                                       if ip == ip2:
                                           self.session.open(MessageBox, _('VPN Not Working?...'), MessageBox.TYPE_INFO, timeout=5)
                                       else:
                                           self.session.open(MessageBox, _('Your Ip Address is :  ' + str(IP) + '\nYour New Ip Address is :  ' + str(IP2) + '\nYour Ip Location is :  Amsterdam, Netherlands'), MessageBox.TYPE_INFO, timeout=10)
                            else:
                                self.session.open(MessageBox, _('Cannot connect (or server is down) !'), MessageBox.TYPE_INFO, timeout=5)
                            return
                        elif returnValue =="com_55":
                            if connected_to_internet():
                               os.system('/etc/init.d/openvpn stop > /dev/null 2>&1')
                               os.system('rm -r %s > /dev/null 2>&1 && rm -f %s > /dev/null 2>&1' % (LINKFILE1, LINKFILE2))
                               os.system('rm -r -f /etc/openvpn; mkdir /etc/openvpn') 
                               shutil.copyfile('/etc/pointvpn/cfg_conf', '/etc/openvpn/cfg.conf')
                               shutil.copyfile('/etc/pointvpn/client_conf34', '/etc/openvpn/client.conf')
                               ip = compat_urlopen("http://ip.42.pl/raw").read()                                  
                               with open(LINKFILE1, "wb") as f: f.write(ip)                                   
                               f = open(LINKFILE1, 'r')
                               for line in f.readlines():
                                   IP = line.strip('\n')
                                   os.system('/etc/init.d/openvpn start > /dev/null 2>&1')
                                   time.sleep(8)
                                   ip2 = compat_urlopen("http://ip.42.pl/raw").read()  
                                   with open(LINKFILE2, "wb") as f: f.write(ip2)                                       
                                   f = open(LINKFILE2, 'r')
                                   for line in f.readlines():
                                       IP2 = line.strip('\n')
                                       if ip == ip2:
                                           self.session.open(MessageBox, _('VPN Not Working?...'), MessageBox.TYPE_INFO, timeout=5)
                                       else:
                                           self.session.open(MessageBox, _('Your Ip Address is :  ' + str(IP) + '\nYour New Ip Address is :  ' + str(IP2) + '\nYour Ip Location is :  Manila, Philippines'), MessageBox.TYPE_INFO, timeout=10)
                            else:
                                self.session.open(MessageBox, _('Cannot connect (or server is down) !'), MessageBox.TYPE_INFO, timeout=5)
                            return              
                        elif returnValue =="com_56":
                            if connected_to_internet():
                               os.system('/etc/init.d/openvpn stop > /dev/null 2>&1')
                               os.system('rm -r %s > /dev/null 2>&1 && rm -f %s > /dev/null 2>&1' % (LINKFILE1, LINKFILE2))
                               os.system('rm -r -f /etc/openvpn; mkdir /etc/openvpn') 
                               shutil.copyfile('/etc/pointvpn/cfg_conf', '/etc/openvpn/cfg.conf')
                               shutil.copyfile('/etc/pointvpn/client_conf35', '/etc/openvpn/client.conf')
                               ip = compat_urlopen("http://ip.42.pl/raw").read()                                  
                               with open(LINKFILE1, "wb") as f: f.write(ip)                                   
                               f = open(LINKFILE1, 'r')
                               for line in f.readlines():
                                   IP = line.strip('\n')
                                   os.system('/etc/init.d/openvpn start > /dev/null 2>&1')
                                   time.sleep(8)
                                   ip2 = compat_urlopen("http://ip.42.pl/raw").read()  
                                   with open(LINKFILE2, "wb") as f: f.write(ip2)                                       
                                   f = open(LINKFILE2, 'r')
                                   for line in f.readlines():
                                       IP2 = line.strip('\n')
                                       if ip == ip2:
                                           self.session.open(MessageBox, _('VPN Not Working?...'), MessageBox.TYPE_INFO, timeout=5)
                                       else:
                                           self.session.open(MessageBox, _('Your Ip Address is :  ' + str(IP) + '\nYour New Ip Address is :  ' + str(IP2) + '\nYour Ip Location is :  Warsaw, Poland'), MessageBox.TYPE_INFO, timeout=10)
                            else:
                                self.session.open(MessageBox, _('Cannot connect (or server is down) !'), MessageBox.TYPE_INFO, timeout=5)
                            return
                        elif returnValue =="com_57":
                            if connected_to_internet():
                               os.system('/etc/init.d/openvpn stop > /dev/null 2>&1')
                               os.system('rm -r %s > /dev/null 2>&1 && rm -f %s > /dev/null 2>&1' % (LINKFILE1, LINKFILE2))
                               os.system('rm -r -f /etc/openvpn; mkdir /etc/openvpn') 
                               shutil.copyfile('/etc/pointvpn/cfg_conf', '/etc/openvpn/cfg.conf')
                               shutil.copyfile('/etc/pointvpn/client_conf36', '/etc/openvpn/client.conf')
                               ip = compat_urlopen("http://ip.42.pl/raw").read()   
                               with open(LINKFILE1, "wb") as f: f.write(ip)                                   
                               f = open(LINKFILE1, 'r')
                               for line in f.readlines():
                                   IP = line.strip('\n')
                                   os.system('/etc/init.d/openvpn start > /dev/null 2>&1')
                                   time.sleep(8)
                                   ip2 = compat_urlopen("http://ip.42.pl/raw").read()  
                                   with open(LINKFILE2, "wb") as f: f.write(ip2)                                       
                                   f = open(LINKFILE2, 'r')
                                   for line in f.readlines():
                                       IP2 = line.strip('\n')
                                       if ip == ip2:
                                           self.session.open(MessageBox, _('VPN Not Working?...'), MessageBox.TYPE_INFO, timeout=5)
                                       else:
                                           self.session.open(MessageBox, _('Your Ip Address is :  ' + str(IP) + '\nYour New Ip Address is :  ' + str(IP2) + '\nYour Ip Location is :  Bucharest, Romania'), MessageBox.TYPE_INFO, timeout=10)
                            else:
                                self.session.open(MessageBox, _('Cannot connect (or server is down) !'), MessageBox.TYPE_INFO, timeout=5)
                            return
                        elif returnValue =="com_58":
                            if connected_to_internet():
                               os.system('/etc/init.d/openvpn stop > /dev/null 2>&1')
                               os.system('rm -r %s > /dev/null 2>&1 && rm -f %s > /dev/null 2>&1' % (LINKFILE1, LINKFILE2))
                               os.system('rm -r -f /etc/openvpn; mkdir /etc/openvpn') 
                               shutil.copyfile('/etc/pointvpn/cfg_conf', '/etc/openvpn/cfg.conf')
                               shutil.copyfile('/etc/pointvpn/client_conf37', '/etc/openvpn/client.conf')
                               ip = compat_urlopen("http://ip.42.pl/raw").read()   
                               with open(LINKFILE1, "wb") as f: f.write(ip)                                   
                               f = open(LINKFILE1, 'r')
                               for line in f.readlines():
                                   IP = line.strip('\n')
                                   os.system('/etc/init.d/openvpn start > /dev/null 2>&1')
                                   time.sleep(8)
                                   ip2 = compat_urlopen("http://ip.42.pl/raw").read()  
                                   with open(LINKFILE2, "wb") as f: f.write(ip2)                                       
                                   f = open(LINKFILE2, 'r')
                                   for line in f.readlines():
                                       IP2 = line.strip('\n')
                                       if ip == ip2:
                                           self.session.open(MessageBox, _('VPN Not Working?...'), MessageBox.TYPE_INFO, timeout=5)
                                       else:
                                           self.session.open(MessageBox, _('Your Ip Address is :  ' + str(IP) + '\nYour New Ip Address is :  ' + str(IP2) + '\nYour Ip Location is :  St Petersburg, Russian Federation'), MessageBox.TYPE_INFO, timeout=10)
                            else:
                                self.session.open(MessageBox, _('Cannot connect (or server is down) !'), MessageBox.TYPE_INFO, timeout=5)
                            return                      
                        elif returnValue =="com_59":
                            if connected_to_internet():
                               os.system('/etc/init.d/openvpn stop > /dev/null 2>&1')
                               os.system('rm -r %s > /dev/null 2>&1 && rm -f %s > /dev/null 2>&1' % (LINKFILE1, LINKFILE2))
                               os.system('rm -r -f /etc/openvpn; mkdir /etc/openvpn') 
                               shutil.copyfile('/etc/pointvpn/cfg_conf', '/etc/openvpn/cfg.conf')
                               shutil.copyfile('/etc/pointvpn/client_conf38', '/etc/openvpn/client.conf')
                               ip = compat_urlopen("http://ip.42.pl/raw").read()   
                               with open(LINKFILE1, "wb") as f: f.write(ip)                                   
                               f = open(LINKFILE1, 'r')
                               for line in f.readlines():
                                   IP = line.strip('\n')
                                   os.system('/etc/init.d/openvpn start > /dev/null 2>&1')
                                   time.sleep(8)
                                   ip2 = compat_urlopen("http://ip.42.pl/raw").read()  
                                   with open(LINKFILE2, "wb") as f: f.write(ip2)                                       
                                   f = open(LINKFILE2, 'r')
                                   for line in f.readlines():
                                       IP2 = line.strip('\n')
                                       if ip == ip2:
                                           self.session.open(MessageBox, _('VPN Not Working?...'), MessageBox.TYPE_INFO, timeout=5)
                                       else:
                                           self.session.open(MessageBox, _('Your Ip Address is :  ' + str(IP) + '\nYour New Ip Address is :  ' + str(IP2) + '\nYour Ip Location is :  Stockholm, Swede'), MessageBox.TYPE_INFO, timeout=10)
                            else:
                                self.session.open(MessageBox, _('Cannot connect (or server is down) !'), MessageBox.TYPE_INFO, timeout=5)
                            return
                        elif returnValue =="com_60":
                            if connected_to_internet():
                               os.system('/etc/init.d/openvpn stop > /dev/null 2>&1')
                               os.system('rm -r %s > /dev/null 2>&1 && rm -f %s > /dev/null 2>&1' % (LINKFILE1, LINKFILE2))
                               os.system('rm -r -f /etc/openvpn; mkdir /etc/openvpn') 
                               shutil.copyfile('/etc/pointvpn/cfg_conf', '/etc/openvpn/cfg.conf')
                               shutil.copyfile('/etc/pointvpn/client_conf39', '/etc/openvpn/client.conf')
                               ip = compat_urlopen("http://ip.42.pl/raw").read()    
                               with open(LINKFILE1, "wb") as f: f.write(ip)                                   
                               f = open(LINKFILE1, 'r')
                               for line in f.readlines():
                                   IP = line.strip('\n')
                                   os.system('/etc/init.d/openvpn start > /dev/null 2>&1')
                                   time.sleep(8)
                                   ip2 = compat_urlopen("http://ip.42.pl/raw").read()  
                                   with open(LINKFILE2, "wb") as f: f.write(ip2)                                       
                                   f = open(LINKFILE2, 'r')
                                   for line in f.readlines():
                                       IP2 = line.strip('\n')
                                       if ip == ip2:
                                           self.session.open(MessageBox, _('VPN Not Working?...'), MessageBox.TYPE_INFO, timeout=5)
                                       else:
                                           self.session.open(MessageBox, _('Your Ip Address is :  ' + str(IP) + '\nYour New Ip Address is :  ' + str(IP2) + '\nYour Ip Location is :  Ljubljana, Slovenia'), MessageBox.TYPE_INFO, timeout=10)
                            else:
                                self.session.open(MessageBox, _('Cannot connect (or server is down) !'), MessageBox.TYPE_INFO, timeout=5)
                            return
                        elif returnValue =="com_61":
                            if connected_to_internet():
                               os.system('/etc/init.d/openvpn stop > /dev/null 2>&1')
                               os.system('rm -r %s > /dev/null 2>&1 && rm -f %s > /dev/null 2>&1' % (LINKFILE1, LINKFILE2))
                               os.system('rm -r -f /etc/openvpn; mkdir /etc/openvpn') 
                               shutil.copyfile('/etc/pointvpn/cfg_conf', '/etc/openvpn/cfg.conf')
                               shutil.copyfile('/etc/pointvpn/client_conf40', '/etc/openvpn/client.conf')
                               ip = compat_urlopen("http://ip.42.pl/raw").read()   
                               with open(LINKFILE1, "wb") as f: f.write(ip)                                   
                               f = open(LINKFILE1, 'r')
                               for line in f.readlines():
                                   IP = line.strip('\n')
                                   os.system('/etc/init.d/openvpn start > /dev/null 2>&1')
                                   time.sleep(8)
                                   ip2 = compat_urlopen("http://ip.42.pl/raw").read()  
                                   with open(LINKFILE2, "wb") as f: f.write(ip2)                                       
                                   f = open(LINKFILE2, 'r')
                                   for line in f.readlines():
                                       IP2 = line.strip('\n')
                                       if ip == ip2:
                                           self.session.open(MessageBox, _('VPN Not Working?...'), MessageBox.TYPE_INFO, timeout=5)
                                       else:
                                           self.session.open(MessageBox, _('Your Ip Address is :  ' + str(IP) + '\nYour New Ip Address is :  ' + str(IP2) + '\nYour Ip Location is :  Singapore, Singapore'), MessageBox.TYPE_INFO, timeout=10)
                            else:
                                self.session.open(MessageBox, _('Cannot connect (or server is down) !'), MessageBox.TYPE_INFO, timeout=5)
                            return
                        elif returnValue =="com_62":
                            if connected_to_internet():
                               os.system('/etc/init.d/openvpn stop > /dev/null 2>&1')
                               os.system('rm -r %s > /dev/null 2>&1 && rm -f %s > /dev/null 2>&1' % (LINKFILE1, LINKFILE2))
                               os.system('rm -r -f /etc/openvpn; mkdir /etc/openvpn') 
                               shutil.copyfile('/etc/pointvpn/cfg_conf', '/etc/openvpn/cfg.conf')
                               shutil.copyfile('/etc/pointvpn/client_conf41', '/etc/openvpn/client.conf')
                               ip = compat_urlopen("http://ip.42.pl/raw").read()   
                               with open(LINKFILE1, "wb") as f: f.write(ip)                                   
                               f = open(LINKFILE1, 'r')
                               for line in f.readlines():
                                   IP = line.strip('\n')
                                   os.system('/etc/init.d/openvpn start > /dev/null 2>&1')
                                   time.sleep(8)
                                   ip2 = compat_urlopen("http://ip.42.pl/raw").read()  
                                   with open(LINKFILE2, "wb") as f: f.write(ip2)                                       
                                   f = open(LINKFILE2, 'r')
                                   for line in f.readlines():
                                       IP2 = line.strip('\n')
                                       if ip == ip2:
                                           self.session.open(MessageBox, _('VPN Not Working?...'), MessageBox.TYPE_INFO, timeout=5)
                                       else:
                                           self.session.open(MessageBox, _('Your Ip Address is :  ' + str(IP) + '\nYour New Ip Address is :  ' + str(IP2) + '\nYour Ip Location is :  Bursa, Turkey'), MessageBox.TYPE_INFO, timeout=10)
                            else:           
                                self.session.open(MessageBox, _('Cannot connect (or server is down) !'), MessageBox.TYPE_INFO, timeout=5)
                            return
                        elif returnValue =="com_63":
                            if connected_to_internet():
                               os.system('/etc/init.d/openvpn stop > /dev/null 2>&1')
                               os.system('rm -r %s > /dev/null 2>&1 && rm -f %s > /dev/null 2>&1' % (LINKFILE1, LINKFILE2))
                               os.system('rm -r -f /etc/openvpn; mkdir /etc/openvpn') 
                               shutil.copyfile('/etc/pointvpn/cfg_conf', '/etc/openvpn/cfg.conf')
                               shutil.copyfile('/etc/pointvpn/client_conf42', '/etc/openvpn/client.conf')
                               ip = compat_urlopen("http://ip.42.pl/raw").read()   
                               with open(LINKFILE1, "wb") as f: f.write(ip)                                   
                               f = open(LINKFILE1, 'r')
                               for line in f.readlines():
                                   IP = line.strip('\n')
                                   os.system('/etc/init.d/openvpn start > /dev/null 2>&1')
                                   time.sleep(8)
                                   ip2 = compat_urlopen("http://ip.42.pl/raw").read()  
                                   with open(LINKFILE2, "wb") as f: f.write(ip2)                                       
                                   f = open(LINKFILE2, 'r')
                                   for line in f.readlines():
                                       IP2 = line.strip('\n')
                                       if ip == ip2:
                                           self.session.open(MessageBox, _('VPN Not Working?...'), MessageBox.TYPE_INFO, timeout=5)
                                       else:
                                           self.session.open(MessageBox, _('Your Ip Address is :  ' + str(IP) + '\nYour New Ip Address is :  ' + str(IP2) + '\nYour Ip Location is :  Ljubljana, Slovenia'), MessageBox.TYPE_INFO, timeout=10)
                            else:
                                self.session.open(MessageBox, _('Cannot connect (or server is down) !'), MessageBox.TYPE_INFO, timeout=5)
                            return
                        elif returnValue =="com_64":
                            if connected_to_internet():
                               os.system('/etc/init.d/openvpn stop > /dev/null 2>&1')
                               os.system('rm -r %s > /dev/null 2>&1 && rm -f %s > /dev/null 2>&1' % (LINKFILE1, LINKFILE2))
                               os.system('rm -r -f /etc/openvpn; mkdir /etc/openvpn') 
                               shutil.copyfile('/etc/pointvpn/cfg_conf', '/etc/openvpn/cfg.conf')
                               shutil.copyfile('/etc/pointvpn/client_conf43', '/etc/openvpn/client.conf')
                               ip = compat_urlopen("http://ip.42.pl/raw").read()   
                               with open(LINKFILE1, "wb") as f: f.write(ip)                                   
                               f = open(LINKFILE1, 'r')
                               for line in f.readlines():
                                   IP = line.strip('\n')
                                   os.system('/etc/init.d/openvpn start > /dev/null 2>&1')
                                   time.sleep(8)
                                   ip2 = compat_urlopen("http://ip.42.pl/raw").read()  
                                   with open(LINKFILE2, "wb") as f: f.write(ip2)                                       
                                   f = open(LINKFILE2, 'r')
                                   for line in f.readlines():
                                       IP2 = line.strip('\n')
                                       if ip == ip2:
                                           self.session.open(MessageBox, _('VPN Not Working?...'), MessageBox.TYPE_INFO, timeout=5)
                                       else:
                                           self.session.open(MessageBox, _('Your Ip Address is :  ' + str(IP) + '\nYour New Ip Address is :  ' + str(IP2) + '\nYour Ip Location is :  Bangkok, Thailand'), MessageBox.TYPE_INFO, timeout=10)
                            else:
                                self.session.open(MessageBox, _('Cannot connect (or server is down) !'), MessageBox.TYPE_INFO, timeout=5)
                            return
                        elif returnValue =="com_65":
                            if connected_to_internet():
                               os.system('/etc/init.d/openvpn stop > /dev/null 2>&1')
                               os.system('rm -r %s > /dev/null 2>&1 && rm -f %s > /dev/null 2>&1' % (LINKFILE1, LINKFILE2))
                               os.system('rm -r -f /etc/openvpn; mkdir /etc/openvpn') 
                               shutil.copyfile('/etc/pointvpn/cfg_conf', '/etc/openvpn/cfg.conf')
                               shutil.copyfile('/etc/pointvpn/client_conf44', '/etc/openvpn/client.conf')
                               ip = compat_urlopen("http://ip.42.pl/raw").read()   
                               with open(LINKFILE1, "wb") as f: f.write(ip)                                   
                               f = open(LINKFILE1, 'r')
                               for line in f.readlines():
                                   IP = line.strip('\n')
                                   os.system('/etc/init.d/openvpn start > /dev/null 2>&1')
                                   time.sleep(8)
                                   ip2 = compat_urlopen("http://ip.42.pl/raw").read()  
                                   with open(LINKFILE2, "wb") as f: f.write(ip2)                                       
                                   f = open(LINKFILE2, 'r')
                                   for line in f.readlines():
                                       IP2 = line.strip('\n')
                                       if ip == ip2:
                                           self.session.open(MessageBox, _('VPN Not Working?...'), MessageBox.TYPE_INFO, timeout=5)
                                       else:
                                           self.session.open(MessageBox, _('Your Ip Address is :  ' + str(IP) + '\nYour New Ip Address is :  ' + str(IP2) + '\nYour Ip Location is :  Miami, United States'), MessageBox.TYPE_INFO, timeout=10)
                            else:
                                self.session.open(MessageBox, _('Cannot connect (or server is down) !'), MessageBox.TYPE_INFO, timeout=5)
                            return
                        elif returnValue =="com_66":
                            if connected_to_internet():
                               os.system('/etc/init.d/openvpn stop > /dev/null 2>&1')
                               os.system('rm -r %s > /dev/null 2>&1 && rm -f %s > /dev/null 2>&1' % (LINKFILE1, LINKFILE2))
                               os.system('rm -r -f /etc/openvpn; mkdir /etc/openvpn') 
                               shutil.copyfile('/etc/pointvpn/cfg_conf', '/etc/openvpn/cfg.conf')
                               shutil.copyfile('/etc/pointvpn/client_conf45', '/etc/openvpn/client.conf')
                               ip = compat_urlopen("http://ip.42.pl/raw").read()   
                               with open(LINKFILE1, "wb") as f: f.write(ip)                                   
                               f = open(LINKFILE1, 'r')
                               for line in f.readlines():
                                   IP = line.strip('\n')
                                   os.system('/etc/init.d/openvpn start > /dev/null 2>&1')
                                   time.sleep(8)
                                   ip2 = compat_urlopen("http://ip.42.pl/raw").read()  
                                   with open(LINKFILE2, "wb") as f: f.write(ip2)                                       
                                   f = open(LINKFILE2, 'r')
                                   for line in f.readlines():
                                       IP2 = line.strip('\n')
                                       if ip == ip2:
                                           self.session.open(MessageBox, _('VPN Not Working?...'), MessageBox.TYPE_INFO, timeout=5)
                                       else:
                                           self.session.open(MessageBox, _('Your Ip Address is :  ' + str(IP) + '\nYour New Ip Address is :  ' + str(IP2) + '\nYour Ip Location is :  Bursa 2, Turkey'), MessageBox.TYPE_INFO, timeout=10)
                            else:
                                self.session.open(MessageBox, _('Cannot connect (or server is down) !'), MessageBox.TYPE_INFO, timeout=5)
                            return
                        elif returnValue =="com_67":
                            if connected_to_internet():
                               os.system('/etc/init.d/openvpn stop > /dev/null 2>&1')
                               os.system('rm -r %s > /dev/null 2>&1 && rm -f %s > /dev/null 2>&1' % (LINKFILE1, LINKFILE2))
                               os.system('rm -r -f /etc/openvpn; mkdir /etc/openvpn') 
                               shutil.copyfile('/etc/pointvpn/cfg_conf', '/etc/openvpn/cfg.conf')
                               shutil.copyfile('/etc/pointvpn/client_conf46', '/etc/openvpn/client.conf')
                               ip = compat_urlopen("http://ip.42.pl/raw").read()   
                               with open(LINKFILE1, "wb") as f: f.write(ip)                                   
                               f = open(LINKFILE1, 'r')
                               for line in f.readlines():
                                   IP = line.strip('\n')
                                   os.system('/etc/init.d/openvpn start > /dev/null 2>&1')
                                   time.sleep(8)
                                   ip2 = compat_urlopen("http://ip.42.pl/raw").read()  
                                   with open(LINKFILE2, "wb") as f: f.write(ip2)                                       
                                   f = open(LINKFILE2, 'r')
                                   for line in f.readlines():
                                       IP2 = line.strip('\n')
                                       if ip == ip2:
                                           self.session.open(MessageBox, _('VPN Not Working?...'), MessageBox.TYPE_INFO, timeout=5)
                                       else:
                                           self.session.open(MessageBox, _('Your Ip Address is :  ' + str(IP) + '\nYour New Ip Address is :  ' + str(IP2) + '\nYour Ip Location is :  Kiev, Ukraine'), MessageBox.TYPE_INFO, timeout=10)
                            else:
                                self.session.open(MessageBox, _('Cannot connect (or server is down) !'), MessageBox.TYPE_INFO, timeout=5)
                            return
                        elif returnValue =="com_68":
                            if connected_to_internet():
                               os.system('/etc/init.d/openvpn stop > /dev/null 2>&1')
                               os.system('rm -r %s > /dev/null 2>&1 && rm -f %s > /dev/null 2>&1' % (LINKFILE1, LINKFILE2))
                               os.system('rm -r -f /etc/openvpn; mkdir /etc/openvpn') 
                               shutil.copyfile('/etc/pointvpn/cfg_conf', '/etc/openvpn/cfg.conf')
                               shutil.copyfile('/etc/pointvpn/client_conf47', '/etc/openvpn/client.conf')
                               ip = compat_urlopen("http://ip.42.pl/raw").read()   
                               with open(LINKFILE1, "wb") as f: f.write(ip)                                   
                               f = open(LINKFILE1, 'r')
                               for line in f.readlines():
                                   IP = line.strip('\n')
                                   os.system('/etc/init.d/openvpn start > /dev/null 2>&1')
                                   time.sleep(8)
                                   ip2 = compat_urlopen("http://ip.42.pl/raw").read()  
                                   with open(LINKFILE2, "wb") as f: f.write(ip2)                                       
                                   f = open(LINKFILE2, 'r')
                                   for line in f.readlines():
                                       IP2 = line.strip('\n')
                                       if ip == ip2:
                                           self.session.open(MessageBox, _('VPN Not Working?...'), MessageBox.TYPE_INFO, timeout=5)
                                       else:
                                           self.session.open(MessageBox, _('Your Ip Address is :  ' + str(IP) + '\nYour New Ip Address is :  ' + str(IP2) + '\nYour Ip Location is :  Miami, United States'), MessageBox.TYPE_INFO, timeout=10)
                            else:
                                self.session.open(MessageBox, _('Cannot connect (or server is down) !'), MessageBox.TYPE_INFO, timeout=5)
                            return
                        elif returnValue =="com_69":
                            if connected_to_internet():
                               os.system('/etc/init.d/openvpn stop > /dev/null 2>&1')
                               os.system('rm -r %s > /dev/null 2>&1 && rm -f %s > /dev/null 2>&1' % (LINKFILE1, LINKFILE2))
                               os.system('rm -r -f /etc/openvpn; mkdir /etc/openvpn') 
                               shutil.copyfile('/etc/pointvpn/cfg_conf', '/etc/openvpn/cfg.conf')
                               shutil.copyfile('/etc/pointvpn/client_conf48', '/etc/openvpn/client.conf')
                               ip = compat_urlopen("http://ip.42.pl/raw").read()   
                               with open(LINKFILE1, "wb") as f: f.write(ip)                                   
                               f = open(LINKFILE1, 'r')
                               for line in f.readlines():
                                   IP = line.strip('\n')
                                   os.system('/etc/init.d/openvpn start > /dev/null 2>&1')
                                   time.sleep(8)
                                   ip2 = compat_urlopen("http://ip.42.pl/raw").read()  
                                   with open(LINKFILE2, "wb") as f: f.write(ip2)                                       
                                   f = open(LINKFILE2, 'r')
                                   for line in f.readlines():
                                       IP2 = line.strip('\n')
                                       if ip == ip2:
                                           self.session.open(MessageBox, _('VPN Not Working?...'), MessageBox.TYPE_INFO, timeout=5)
                                       else:
                                           self.session.open(MessageBox, _('Your Ip Address is :  ' + str(IP) + '\nYour New Ip Address is :  ' + str(IP2) + '\nYour Ip Location is :  Los Angeles, United States'), MessageBox.TYPE_INFO, timeout=10)
                            else:
                                self.session.open(MessageBox, _('Cannot connect (or server is down) !'), MessageBox.TYPE_INFO, timeout=5)
                            return
                        elif returnValue =="com_70":
                            if connected_to_internet():
                               os.system('/etc/init.d/openvpn stop > /dev/null 2>&1')
                               os.system('rm -r %s > /dev/null 2>&1 && rm -f %s > /dev/null 2>&1' % (LINKFILE1, LINKFILE2))
                               os.system('rm -r -f /etc/openvpn; mkdir /etc/openvpn') 
                               shutil.copyfile('/etc/pointvpn/cfg_conf', '/etc/openvpn/cfg.conf')
                               shutil.copyfile('/etc/pointvpn/client_conf49', '/etc/openvpn/client.conf')
                               ip = compat_urlopen("http://ip.42.pl/raw").read()   
                               with open(LINKFILE1, "wb") as f: f.write(ip)                                   
                               f = open(LINKFILE1, 'r')
                               for line in f.readlines():
                                   IP = line.strip('\n')
                                   os.system('/etc/init.d/openvpn start > /dev/null 2>&1')
                                   time.sleep(8)
                                   ip2 = compat_urlopen("http://ip.42.pl/raw").read()  
                                   with open(LINKFILE2, "wb") as f: f.write(ip2)                                       
                                   f = open(LINKFILE2, 'r')
                                   for line in f.readlines():
                                       IP2 = line.strip('\n')
                                       if ip == ip2:
                                           self.session.open(MessageBox, _('VPN Not Working?...'), MessageBox.TYPE_INFO, timeout=5)
                                       else:
                                           self.session.open(MessageBox, _('Your Ip Address is :  ' + str(IP) + '\nYour New Ip Address is :  ' + str(IP2) + '\nYour Ip Location is :  New York City, United States'), MessageBox.TYPE_INFO, timeout=10)
                            else:
                                self.session.open(MessageBox, _('Cannot connect (or server is down) !'), MessageBox.TYPE_INFO, timeout=5)
                            return
                        elif returnValue =="com_71":
                            if connected_to_internet():
                               os.system('/etc/init.d/openvpn stop > /dev/null 2>&1')
                               os.system('rm -r %s > /dev/null 2>&1 && rm -f %s > /dev/null 2>&1' % (LINKFILE1, LINKFILE2))
                               os.system('rm -r -f /etc/openvpn; mkdir /etc/openvpn') 
                               shutil.copyfile('/etc/pointvpn/cfg_conf', '/etc/openvpn/cfg.conf')
                               shutil.copyfile('/etc/client_conf50', '/etc/openvpn/client.conf')
                               ip = compat_urlopen("http://ip.42.pl/raw").read()   
                               with open(LINKFILE1, "wb") as f: f.write(ip)                                   
                               f = open(LINKFILE1, 'r')
                               for line in f.readlines():
                                   IP = line.strip('\n')
                                   os.system('/etc/init.d/openvpn start > /dev/null 2>&1')
                                   time.sleep(8)
                                   ip2 = compat_urlopen("http://ip.42.pl/raw").read()  
                                   with open(LINKFILE2, "wb") as f: f.write(ip2)                                       
                                   f = open(LINKFILE2, 'r')
                                   for line in f.readlines():
                                       IP2 = line.strip('\n')
                                       if ip == ip2:
                                           self.session.open(MessageBox, _('VPN Not Working?...'), MessageBox.TYPE_INFO, timeout=5)
                                       else:
                                           self.session.open(MessageBox, _('Your Ip Address is :  ' + str(IP) + '\nYour New Ip Address is :  ' + str(IP2) + '\nYour Ip Location is :  Miami 2, United States'), MessageBox.TYPE_INFO, timeout=10)
                            else:
                                self.session.open(MessageBox, _('Cannot connect (or server is down) !'), MessageBox.TYPE_INFO, timeout=5)
                            return
                        elif returnValue =="com_72":
                            if connected_to_internet():
                               os.system('/etc/init.d/openvpn stop > /dev/null 2>&1')
                               os.system('rm -r %s > /dev/null 2>&1 && rm -f %s > /dev/null 2>&1' % (LINKFILE1, LINKFILE2))
                               os.system('rm -r -f /etc/openvpn; mkdir /etc/openvpn') 
                               shutil.copyfile('/etc/pointvpn/cfg_conf', '/etc/openvpn/cfg.conf')
                               shutil.copyfile('/etc/pointvpn/client_conf51', '/etc/openvpn/client.conf')
                               ip = compat_urlopen("http://ip.42.pl/raw").read()   
                               with open(LINKFILE1, "wb") as f: f.write(ip)                                   
                               f = open(LINKFILE1, 'r')
                               for line in f.readlines():
                                   IP = line.strip('\n')
                                   os.system('/etc/init.d/openvpn start > /dev/null 2>&1')
                                   time.sleep(8)
                                   ip2 = compat_urlopen("http://ip.42.pl/raw").read()  
                                   with open(LINKFILE2, "wb") as f: f.write(ip2)                                       
                                   f = open(LINKFILE2, 'r')
                                   for line in f.readlines():
                                       IP2 = line.strip('\n')
                                       if ip == ip2:
                                           self.session.open(MessageBox, _('VPN Not Working?...'), MessageBox.TYPE_INFO, timeout=5)
                                       else:
                                           self.session.open(MessageBox, _('Your Ip Address is :  ' + str(IP) + '\nYour New Ip Address is :  ' + str(IP2) + '\nYour Ip Location is :  Miami 3, United States'), MessageBox.TYPE_INFO, timeout=10)
                            else:
                                self.session.open(MessageBox, _('Cannot connect (or server is down) !'), MessageBox.TYPE_INFO, timeout=5)
                            return
                        elif returnValue =="com_73":
                            if connected_to_internet():
                               os.system('/etc/init.d/openvpn stop > /dev/null 2>&1')
                               os.system('rm -r %s > /dev/null 2>&1 && rm -f %s > /dev/null 2>&1' % (LINKFILE1, LINKFILE2))
                               os.system('rm -r -f /etc/openvpn; mkdir /etc/openvpn') 
                               shutil.copyfile('/etc/pointvpn/cfg_conf', '/etc/openvpn/cfg.conf')
                               shutil.copyfile('/etc/client_conf52', '/etc/openvpn/client.conf')
                               ip = compat_urlopen("http://ip.42.pl/raw").read()   
                               with open(LINKFILE1, "wb") as f: f.write(ip)                                   
                               f = open(LINKFILE1, 'r')
                               for line in f.readlines():
                                   IP = line.strip('\n')
                                   os.system('/etc/init.d/openvpn start > /dev/null 2>&1')
                                   time.sleep(8)
                                   ip2 = compat_urlopen("http://ip.42.pl/raw").read()  
                                   with open(LINKFILE2, "wb") as f: f.write(ip2)                                       
                                   f = open(LINKFILE2, 'r')
                                   for line in f.readlines():
                                       IP2 = line.strip('\n')
                                       if ip == ip2:
                                           self.session.open(MessageBox, _('VPN Not Working?...'), MessageBox.TYPE_INFO, timeout=5)
                                       else:
                                           self.session.open(MessageBox, _('Your Ip Address is :  ' + str(IP) + '\nYour New Ip Address is :  ' + str(IP2) + '\nYour Ip Location is :  New York City 2, United States'), MessageBox.TYPE_INFO, timeout=10)
                            else:
                                self.session.open(MessageBox, _('Cannot connect (or server is down) !'), MessageBox.TYPE_INFO, timeout=5)
                            return  
                        elif returnValue =="com_74":
                            if connected_to_internet():
                               os.system('/etc/init.d/openvpn stop > /dev/null 2>&1')
                               os.system('rm -r %s > /dev/null 2>&1 && rm -f %s > /dev/null 2>&1' % (LINKFILE1, LINKFILE2))
                               os.system('rm -r -f /etc/openvpn; mkdir /etc/openvpn') 
                               shutil.copyfile('/etc/pointvpn/cfg_conf', '/etc/openvpn/cfg.conf')
                               shutil.copyfile('/etc/pointvpn/client_conf53', '/etc/openvpn/client.conf')
                               ip = compat_urlopen("http://ip.42.pl/raw").read()   
                               with open(LINKFILE1, "wb") as f: f.write(ip)                                   
                               f = open(LINKFILE1, 'r')
                               for line in f.readlines():
                                   IP = line.strip('\n')
                                   os.system('/etc/init.d/openvpn start > /dev/null 2>&1')
                                   time.sleep(8)
                                   ip2 = compat_urlopen("http://ip.42.pl/raw").read()  
                                   with open(LINKFILE2, "wb") as f: f.write(ip2)                                       
                                   f = open(LINKFILE2, 'r')
                                   for line in f.readlines():
                                       IP2 = line.strip('\n')
                                       if ip == ip2:
                                           self.session.open(MessageBox, _('VPN Not Working?...'), MessageBox.TYPE_INFO, timeout=5)
                                       else:
                                           self.session.open(MessageBox, _('Your Ip Address is :  ' + str(IP) + '\nYour New Ip Address is :  ' + str(IP2) + '\nYour Ip Location is :  Johannesburg 2, South Africa'), MessageBox.TYPE_INFO, timeout=10)
                            else:
                                self.session.open(MessageBox, _('Cannot connect (or server is down) !'), MessageBox.TYPE_INFO, timeout=5)
                            return
                        elif returnValue =="com_75":
                            if connected_to_internet():
                               os.system('/etc/init.d/openvpn stop > /dev/null 2>&1')
                               os.system('rm -r %s > /dev/null 2>&1 && rm -f %s > /dev/null 2>&1' % (LINKFILE1, LINKFILE2))
                               os.system('rm -r -f /etc/openvpn; mkdir /etc/openvpn') 
                               shutil.copyfile('/etc/pointvpn/cfg_conf', '/etc/openvpn/cfg.conf')
                               shutil.copyfile('/etc/pointvpn/client_conf54', '/etc/openvpn/client.conf')
                               ip = compat_urlopen("http://ip.42.pl/raw").read()   
                               with open(LINKFILE1, "wb") as f: f.write(ip)                                   
                               f = open(LINKFILE1, 'r')
                               for line in f.readlines():
                                   IP = line.strip('\n')
                                   os.system('/etc/init.d/openvpn start > /dev/null 2>&1')
                                   time.sleep(8)
                                   ip2 = compat_urlopen("http://ip.42.pl/raw").read()  
                                   with open(LINKFILE2, "wb") as f: f.write(ip2)                                       
                                   f = open(LINKFILE2, 'r')
                                   for line in f.readlines():
                                       IP2 = line.strip('\n')
                                       if ip == ip2:
                                           self.session.open(MessageBox, _('VPN Not Working?...'), MessageBox.TYPE_INFO, timeout=5)
                                       else:
                                           self.session.open(MessageBox, _('Your Ip Address is :  ' + str(IP) + '\nYour New Ip Address is :  ' + str(IP2) + '\nYour Ip Location is :  Johannesburg, South Africa'), MessageBox.TYPE_INFO, timeout=10)
                            else:
                                self.session.open(MessageBox, _('Cannot connect (or server is down) !'), MessageBox.TYPE_INFO, timeout=5)
                            return
                        #elif returnValue =="com_***":    
                                #cmdlist = []
                                #cmdlist.append("%s -qO - '" % self.wget + "'")
                                #cmdlist.append("%s https://ia801406.us.archive.org/25/items/iptvworld-24/IPTVWORLDVPN3.sh -qO - | /bin/sh" % self.wget)
                                #self.session.open(Console3, title='Free VPN', cmdlist=cmdlist, finishedCallback=None)
                        elif returnValue =="com_76":
                            if connected_to_internet():
                               os.system('/etc/init.d/openvpn stop > /dev/null 2>&1')
                               os.system('rm -r %s > /dev/null 2>&1 && rm -f %s > /dev/null 2>&1' % (LINKFILE1, LINKFILE2))
                               os.system('rm -r -f /etc/openvpn; mkdir /etc/openvpn') 
                               shutil.copyfile('/etc/pointvpn/cfg_conf', '/etc/openvpn/cfg.conf')
                               shutil.copyfile('/etc/pointvpn/client_conf55', '/etc/openvpn/client.conf')
                               ip = compat_urlopen("http://ip.42.pl/raw").read()   
                               with open(LINKFILE1, "wb") as f: f.write(ip)                                   
                               f = open(LINKFILE1, 'r')
                               for line in f.readlines():
                                   IP = line.strip('\n')
                                   os.system('/etc/init.d/openvpn start > /dev/null 2>&1')
                                   time.sleep(8)
                                   ip2 = compat_urlopen("http://ip.42.pl/raw").read()  
                                   with open(LINKFILE2, "wb") as f: f.write(ip2)                                       
                                   f = open(LINKFILE2, 'r')
                                   for line in f.readlines():
                                       IP2 = line.strip('\n')
                                       if ip == ip2:
                                           self.session.open(MessageBox, _('VPN Not Working?...'), MessageBox.TYPE_INFO, timeout=5)
                                       else:
                                           self.session.open(MessageBox, _('Your Ip Address is :  ' + str(IP) + '\nYour New Ip Address is :  ' + str(IP2) + '\nYour Ip Location is :  Buenos Aires, Argentina'), MessageBox.TYPE_INFO, timeout=10)
                            else:
                                self.session.open(MessageBox, _('Cannot connect (or server is down) !'), MessageBox.TYPE_INFO, timeout=5)
                            return
                        elif returnValue =="com_77":
                            if connected_to_internet():
                               os.system('/etc/init.d/openvpn stop > /dev/null 2>&1')
                               os.system('rm -r %s > /dev/null 2>&1 && rm -f %s > /dev/null 2>&1' % (LINKFILE1, LINKFILE2))
                               os.system('rm -r -f /etc/openvpn; mkdir /etc/openvpn') 
                               shutil.copyfile('/etc/pointvpn/cfg_conf', '/etc/openvpn/cfg.conf')
                               shutil.copyfile('/etc/pointvpn/client_conf56', '/etc/openvpn/client.conf')
                               ip = compat_urlopen("http://ip.42.pl/raw").read()   
                               with open(LINKFILE1, "wb") as f: f.write(ip)                                   
                               f = open(LINKFILE1, 'r')
                               for line in f.readlines():
                                   IP = line.strip('\n')
                                   os.system('/etc/init.d/openvpn start > /dev/null 2>&1')
                                   time.sleep(8)
                                   ip2 = compat_urlopen("http://ip.42.pl/raw").read()  
                                   with open(LINKFILE2, "wb") as f: f.write(ip2)                                       
                                   f = open(LINKFILE2, 'r')
                                   for line in f.readlines():
                                       IP2 = line.strip('\n')
                                       if ip == ip2:
                                           self.session.open(MessageBox, _('VPN Not Working?...'), MessageBox.TYPE_INFO, timeout=5)
                                       else:
                                           self.session.open(MessageBox, _('Your Ip Address is :  ' + str(IP) + '\nYour New Ip Address is :  ' + str(IP2) + '\nYour Ip Location is :  Sydney 2, Australia'), MessageBox.TYPE_INFO, timeout=10)
                            else:
                                self.session.open(MessageBox, _('Cannot connect (or server is down) !'), MessageBox.TYPE_INFO, timeout=5)
                            return
                        elif returnValue =="com_78":
                            if connected_to_internet():
                               os.system('/etc/init.d/openvpn stop > /dev/null 2>&1')
                               os.system('rm -r %s > /dev/null 2>&1 && rm -f %s > /dev/null 2>&1' % (LINKFILE1, LINKFILE2))
                               os.system('rm -r -f /etc/openvpn; mkdir /etc/openvpn') 
                               shutil.copyfile('/etc/pointvpn/cfg_conf', '/etc/openvpn/cfg.conf')
                               shutil.copyfile('/etc/pointvpn/client_conf57', '/etc/openvpn/client.conf')
                               ip = compat_urlopen("http://ip.42.pl/raw").read()   
                               with open(LINKFILE1, "wb") as f: f.write(ip)                                   
                               f = open(LINKFILE1, 'r')
                               for line in f.readlines():
                                   IP = line.strip('\n')
                                   os.system('/etc/init.d/openvpn start > /dev/null 2>&1')
                                   time.sleep(8)
                                   ip2 = compat_urlopen("http://ip.42.pl/raw").read()  
                                   with open(LINKFILE2, "wb") as f: f.write(ip2)                                       
                                   f = open(LINKFILE2, 'r')
                                   for line in f.readlines():
                                       IP2 = line.strip('\n')
                                       if ip == ip2:
                                           self.session.open(MessageBox, _('VPN Not Working?...'), MessageBox.TYPE_INFO, timeout=5)
                                       else:
                                           self.session.open(MessageBox, _('Your Ip Address is :  ' + str(IP) + '\nYour New Ip Address is :  ' + str(IP2) + '\nYour Ip Location is :  Sydney, Australia'), MessageBox.TYPE_INFO, timeout=10)
                            else:
                                self.session.open(MessageBox, _('Cannot connect (or server is down) !'), MessageBox.TYPE_INFO, timeout=5)
                            return
                        elif returnValue =="com_79":
                            if connected_to_internet():
                               os.system('/etc/init.d/openvpn stop > /dev/null 2>&1')
                               os.system('rm -r %s > /dev/null 2>&1 && rm -f %s > /dev/null 2>&1' % (LINKFILE1, LINKFILE2))
                               os.system('rm -r -f /etc/openvpn; mkdir /etc/openvpn') 
                               shutil.copyfile('/etc/pointvpn/cfg_conf', '/etc/openvpn/cfg.conf')
                               shutil.copyfile('/etc/pointvpn/client_conf58', '/etc/openvpn/client.conf')
                               ip = compat_urlopen("http://ip.42.pl/raw").read()   
                               with open(LINKFILE1, "wb") as f: f.write(ip)                                   
                               f = open(LINKFILE1, 'r')
                               for line in f.readlines():
                                   IP = line.strip('\n')
                                   os.system('/etc/init.d/openvpn start > /dev/null 2>&1')
                                   time.sleep(8)
                                   ip2 = compat_urlopen("http://ip.42.pl/raw").read()  
                                   with open(LINKFILE2, "wb") as f: f.write(ip2)                                       
                                   f = open(LINKFILE2, 'r')
                                   for line in f.readlines():
                                       IP2 = line.strip('\n')
                                       if ip == ip2:
                                           self.session.open(MessageBox, _('VPN Not Working?...'), MessageBox.TYPE_INFO, timeout=5)
                                       else:
                                           self.session.open(MessageBox, _('Your Ip Address is :  ' + str(IP) + '\nYour New Ip Address is :  ' + str(IP2) + '\nYour Ip Location is :  Brussels, Belgium'), MessageBox.TYPE_INFO, timeout=10)
                            else:
                                self.session.open(MessageBox, _('Cannot connect (or server is down) !'), MessageBox.TYPE_INFO, timeout=5)
                            return
                        elif returnValue =="com_80":
                            if connected_to_internet():
                               os.system('/etc/init.d/openvpn stop > /dev/null 2>&1')
                               os.system('rm -r %s > /dev/null 2>&1 && rm -f %s > /dev/null 2>&1' % (LINKFILE1, LINKFILE2))
                               os.system('rm -r -f /etc/openvpn; mkdir /etc/openvpn') 
                               shutil.copyfile('/etc/pointvpn/cfg_conf', '/etc/openvpn/cfg.conf')
                               shutil.copyfile('/etc/pointvpn/client_conf59', '/etc/openvpn/client.conf')
                               ip = compat_urlopen("http://ip.42.pl/raw").read()   
                               with open(LINKFILE1, "wb") as f: f.write(ip)                                   
                               f = open(LINKFILE1, 'r')
                               for line in f.readlines():
                                   IP = line.strip('\n')
                                   os.system('/etc/init.d/openvpn start > /dev/null 2>&1')
                                   time.sleep(8)
                                   ip2 = compat_urlopen("http://ip.42.pl/raw").read()  
                                   with open(LINKFILE2, "wb") as f: f.write(ip2)                                       
                                   f = open(LINKFILE2, 'r')
                                   for line in f.readlines():
                                       IP2 = line.strip('\n')
                                       if ip == ip2:
                                           self.session.open(MessageBox, _('VPN Not Working?...'), MessageBox.TYPE_INFO, timeout=5)
                                       else:
                                           self.session.open(MessageBox, _('Your Ip Address is :  ' + str(IP) + '\nYour New Ip Address is :  ' + str(IP2) + '\nYour Ip Location is :  Sofia, Bulgaria'), MessageBox.TYPE_INFO, timeout=10)
                            else:
                                self.session.open(MessageBox, _('Cannot connect (or server is down) !'), MessageBox.TYPE_INFO, timeout=5)
                            return
                        elif returnValue =="com_81":
                            if connected_to_internet():
                               os.system('/etc/init.d/openvpn stop > /dev/null 2>&1')
                               os.system('rm -r %s > /dev/null 2>&1 && rm -f %s > /dev/null 2>&1' % (LINKFILE1, LINKFILE2))
                               os.system('rm -r -f /etc/openvpn; mkdir /etc/openvpn') 
                               shutil.copyfile('/etc/pointvpn/cfg_conf', '/etc/openvpn/cfg.conf')
                               shutil.copyfile('/etc/pointvpn/client_conf60', '/etc/openvpn/client.conf')
                               ip = compat_urlopen("http://ip.42.pl/raw").read()   
                               with open(LINKFILE1, "wb") as f: f.write(ip)                                   
                               f = open(LINKFILE1, 'r')
                               for line in f.readlines():
                                   IP = line.strip('\n')
                                   os.system('/etc/init.d/openvpn start > /dev/null 2>&1')
                                   time.sleep(8)
                                   ip2 = compat_urlopen("http://ip.42.pl/raw").read()  
                                   with open(LINKFILE2, "wb") as f: f.write(ip2)                                       
                                   f = open(LINKFILE2, 'r')
                                   for line in f.readlines():
                                       IP2 = line.strip('\n')
                                       if ip == ip2:
                                           self.session.open(MessageBox, _('VPN Not Working?...'), MessageBox.TYPE_INFO, timeout=5)
                                       else:
                                           self.session.open(MessageBox, _('Your Ip Address is :  ' + str(IP) + '\nYour New Ip Address is :  ' + str(IP2) + '\nYour Ip Location is :  Sao Paulo, Brazil'), MessageBox.TYPE_INFO, timeout=10)
                            else:
                                self.session.open(MessageBox, _('Cannot connect (or server is down) !'), MessageBox.TYPE_INFO, timeout=5)
                            return
                        elif returnValue =="com_82":
                            if connected_to_internet():
                               os.system('/etc/init.d/openvpn stop > /dev/null 2>&1')
                               os.system('rm -r %s > /dev/null 2>&1 && rm -f %s > /dev/null 2>&1' % (LINKFILE1, LINKFILE2))
                               os.system('rm -r -f /etc/openvpn; mkdir /etc/openvpn') 
                               shutil.copyfile('/etc/pointvpn/cfg_conf', '/etc/openvpn/cfg.conf')
                               shutil.copyfile('/etc/pointvpn/client_conf61', '/etc/openvpn/client.conf')
                               ip = compat_urlopen("http://ip.42.pl/raw").read()  
                               with open(LINKFILE1, "wb") as f: f.write(ip)                                   
                               f = open(LINKFILE1, 'r')
                               for line in f.readlines():
                                   IP = line.strip('\n')
                                   os.system('/etc/init.d/openvpn start > /dev/null 2>&1')
                                   time.sleep(8)
                                   ip2 = compat_urlopen("http://ip.42.pl/raw").read()  
                                   with open(LINKFILE2, "wb") as f: f.write(ip2)                                       
                                   f = open(LINKFILE2, 'r')
                                   for line in f.readlines():
                                       IP2 = line.strip('\n')
                                       if ip == ip2:
                                           self.session.open(MessageBox, _('VPN Not Working?...'), MessageBox.TYPE_INFO, timeout=5)
                                       else:
                                           self.session.open(MessageBox, _('Your Ip Address is :  ' + str(IP) + '\nYour New Ip Address is :  ' + str(IP2) + '\nYour Ip Location is :  Toronto, Canada'), MessageBox.TYPE_INFO, timeout=10)
                            else:
                                self.session.open(MessageBox, _('Cannot connect (or server is down) !'), MessageBox.TYPE_INFO, timeout=5)
                            return
                        elif returnValue =="com_83":
                            if connected_to_internet():
                               os.system('/etc/init.d/openvpn stop > /dev/null 2>&1')
                               os.system('rm -r %s > /dev/null 2>&1 && rm -f %s > /dev/null 2>&1' % (LINKFILE1, LINKFILE2))
                               os.system('rm -r -f /etc/openvpn; mkdir /etc/openvpn') 
                               shutil.copyfile('/etc/pointvpn/cfg_conf', '/etc/openvpn/cfg.conf')
                               shutil.copyfile('/etc/pointvpn/client_conf62', '/etc/openvpn/client.conf')
                               ip = compat_urlopen("http://ip.42.pl/raw").read()  
                               with open(LINKFILE1, "wb") as f: f.write(ip)                                   
                               f = open(LINKFILE1, 'r')
                               for line in f.readlines():
                                   IP = line.strip('\n')
                                   os.system('/etc/init.d/openvpn start > /dev/null 2>&1')
                                   time.sleep(8)
                                   ip2 = compat_urlopen("http://ip.42.pl/raw").read()  
                                   with open(LINKFILE2, "wb") as f: f.write(ip2)                                       
                                   f = open(LINKFILE2, 'r')
                                   for line in f.readlines():
                                       IP2 = line.strip('\n')
                                       if ip == ip2:
                                           self.session.open(MessageBox, _('VPN Not Working?...'), MessageBox.TYPE_INFO, timeout=5)
                                       else:
                                           self.session.open(MessageBox, _('Your Ip Address is :  ' + str(IP) + '\nYour New Ip Address is :  ' + str(IP2) + '\nYour Ip Location is :  Montreal, Canada'), MessageBox.TYPE_INFO, timeout=10)
                            else:
                                self.session.open(MessageBox, _('Cannot connect (or server is down) !'), MessageBox.TYPE_INFO, timeout=5)
                            return
                        elif returnValue =="com_84":                            
                            if connected_to_internet():
                               os.system('/etc/init.d/openvpn stop > /dev/null 2>&1')
                               os.system('rm -r %s > /dev/null 2>&1 && rm -f %s > /dev/null 2>&1' % (LINKFILE1, LINKFILE2))
                               os.system('rm -r -f /etc/openvpn; mkdir /etc/openvpn') 
                               shutil.copyfile('/etc/pointvpn/cfg_conf', '/etc/openvpn/cfg.conf')
                               shutil.copyfile('/etc/pointvpn/client_conf63', '/etc/openvpn/client.conf')
                               ip = compat_urlopen("http://ip.42.pl/raw").read()  
                               with open(LINKFILE1, "wb") as f: f.write(ip)                                   
                               f = open(LINKFILE1, 'r')
                               for line in f.readlines():
                                   IP = line.strip('\n')
                                   os.system('/etc/init.d/openvpn start > /dev/null 2>&1')
                                   time.sleep(8)
                                   ip2 = compat_urlopen("http://ip.42.pl/raw").read()  
                                   with open(LINKFILE2, "wb") as f: f.write(ip2)                                       
                                   f = open(LINKFILE2, 'r')
                                   for line in f.readlines():
                                       IP2 = line.strip('\n')
                                       if ip == ip2:
                                           self.session.open(MessageBox, _('VPN Not Working?...'), MessageBox.TYPE_INFO, timeout=5)
                                       else:
                                           self.session.open(MessageBox, _('Your Ip Address is :  ' + str(IP) + '\nYour New Ip Address is :  ' + str(IP2) + '\nYour Ip Location is :  Vancouver, Canada'), MessageBox.TYPE_INFO, timeout=10)
                            else:
                                self.session.open(MessageBox, _('Cannot connect (or server is down) !'), MessageBox.TYPE_INFO, timeout=5)
                            return
                        elif returnValue =="com_85":
                            if connected_to_internet():
                               os.system('/etc/init.d/openvpn stop > /dev/null 2>&1')
                               os.system('rm -r %s > /dev/null 2>&1 && rm -f %s > /dev/null 2>&1' % (LINKFILE1, LINKFILE2))
                               os.system('rm -r -f /etc/openvpn; mkdir /etc/openvpn') 
                               shutil.copyfile('/etc/pointvpn/cfg_conf', '/etc/openvpn/cfg.conf')
                               shutil.copyfile('/etc/pointvpn/client_conf64', '/etc/openvpn/client.conf')
                               ip = compat_urlopen("http://ip.42.pl/raw").read()  
                               with open(LINKFILE1, "wb") as f: f.write(ip)                                   
                               f = open(LINKFILE1, 'r')
                               for line in f.readlines():
                                   IP = line.strip('\n')
                                   os.system('/etc/init.d/openvpn start > /dev/null 2>&1')
                                   time.sleep(8)
                                   ip2 = compat_urlopen("http://ip.42.pl/raw").read()  
                                   with open(LINKFILE2, "wb") as f: f.write(ip2)                                       
                                   f = open(LINKFILE2, 'r')
                                   for line in f.readlines():
                                       IP2 = line.strip('\n')
                                       if ip == ip2:
                                           self.session.open(MessageBox, _('VPN Not Working?...'), MessageBox.TYPE_INFO, timeout=5)
                                       else:
                                           self.session.open(MessageBox, _('Your Ip Address is :  ' + str(IP) + '\nYour New Ip Address is :  ' + str(IP2) + '\nYour Ip Location is :  Zurich, Switzerland'), MessageBox.TYPE_INFO, timeout=10)
                            else:
                                self.session.open(MessageBox, _('Cannot connect (or server is down) !'), MessageBox.TYPE_INFO, timeout=5)
                            return
                        elif returnValue =="com_86":
                            if connected_to_internet():
                               os.system('/etc/init.d/openvpn stop > /dev/null 2>&1')
                               os.system('rm -r %s > /dev/null 2>&1 && rm -f %s > /dev/null 2>&1' % (LINKFILE1, LINKFILE2))
                               os.system('rm -r -f /etc/openvpn; mkdir /etc/openvpn') 
                               shutil.copyfile('/etc/pointvpn/cfg_conf', '/etc/openvpn/cfg.conf')
                               shutil.copyfile('/etc/pointvpn/client_conf65', '/etc/openvpn/client.conf')
                               ip = compat_urlopen("http://ip.42.pl/raw").read()  
                               with open(LINKFILE1, "wb") as f: f.write(ip)                                   
                               f = open(LINKFILE1, 'r')
                               for line in f.readlines():
                                   IP = line.strip('\n')
                                   os.system('/etc/init.d/openvpn start > /dev/null 2>&1')
                                   time.sleep(8)
                                   ip2 = compat_urlopen("http://ip.42.pl/raw").read()  
                                   with open(LINKFILE2, "wb") as f: f.write(ip2)                                       
                                   f = open(LINKFILE2, 'r')
                                   for line in f.readlines():
                                       IP2 = line.strip('\n')
                                       if ip == ip2:
                                           self.session.open(MessageBox, _('VPN Not Working?...'), MessageBox.TYPE_INFO, timeout=5)
                                       else:
                                           self.session.open(MessageBox, _('Your Ip Address is :  ' + str(IP) + '\nYour New Ip Address is :  ' + str(IP2) + '\nYour Ip Location is :  Prague, Czech Republic'), MessageBox.TYPE_INFO, timeout=10)
                            else:
                                self.session.open(MessageBox, _('Cannot connect (or server is down) !'), MessageBox.TYPE_INFO, timeout=5)
                            return
                        elif returnValue =="com_87":
                            if connected_to_internet():
                               os.system('/etc/init.d/openvpn stop > /dev/null 2>&1')
                               os.system('rm -r %s > /dev/null 2>&1 && rm -f %s > /dev/null 2>&1' % (LINKFILE1, LINKFILE2))
                               os.system('rm -r -f /etc/openvpn; mkdir /etc/openvpn') 
                               shutil.copyfile('/etc/pointvpn/cfg_conf', '/etc/openvpn/cfg.conf')
                               shutil.copyfile('/etc/pointvpn/client_conf66', '/etc/openvpn/client.conf')
                               ip = compat_urlopen("http://ip.42.pl/raw").read()  
                               with open(LINKFILE1, "wb") as f: f.write(ip)                                   
                               f = open(LINKFILE1, 'r')
                               for line in f.readlines():
                                   IP = line.strip('\n')
                                   os.system('/etc/init.d/openvpn start > /dev/null 2>&1')
                                   time.sleep(8)
                                   ip2 = compat_urlopen("http://ip.42.pl/raw").read()  
                                   with open(LINKFILE2, "wb") as f: f.write(ip2)                                       
                                   f = open(LINKFILE2, 'r')
                                   for line in f.readlines():
                                       IP2 = line.strip('\n')
                                       if ip == ip2:
                                           self.session.open(MessageBox, _('VPN Not Working?...'), MessageBox.TYPE_INFO, timeout=5)
                                       else:
                                           self.session.open(MessageBox, _('Your Ip Address is :  ' + str(IP) + '\nYour New Ip Address is :  ' + str(IP2) + '\nYour Ip Location is :  Frankfurt, Germany'), MessageBox.TYPE_INFO, timeout=10)
                            else:
                                self.session.open(MessageBox, _('Cannot connect (or server is down) !'), MessageBox.TYPE_INFO, timeout=5)
                            return
                        elif returnValue =="com_88":
                            if connected_to_internet():
                               os.system('/etc/init.d/openvpn stop > /dev/null 2>&1')
                               os.system('rm -r %s > /dev/null 2>&1 && rm -f %s > /dev/null 2>&1' % (LINKFILE1, LINKFILE2))
                               os.system('rm -r -f /etc/openvpn; mkdir /etc/openvpn') 
                               shutil.copyfile('/etc/pointvpn/cfg_conf', '/etc/openvpn/cfg.conf')
                               shutil.copyfile('/etc/pointvpn/client_conf67', '/etc/openvpn/client.conf')
                               ip = compat_urlopen("http://ip.42.pl/raw").read()  
                               with open(LINKFILE1, "wb") as f: f.write(ip)                                   
                               f = open(LINKFILE1, 'r')
                               for line in f.readlines():
                                   IP = line.strip('\n')
                                   os.system('/etc/init.d/openvpn start > /dev/null 2>&1')
                                   time.sleep(8)
                                   ip2 = compat_urlopen("http://ip.42.pl/raw").read()  
                                   with open(LINKFILE2, "wb") as f: f.write(ip2)                                       
                                   f = open(LINKFILE2, 'r')
                                   for line in f.readlines():
                                       IP2 = line.strip('\n')
                                       if ip == ip2:
                                           self.session.open(MessageBox, _('VPN Not Working?...'), MessageBox.TYPE_INFO, timeout=5)
                                       else:
                                           self.session.open(MessageBox, _('Your Ip Address is :  ' + str(IP) + '\nYour New Ip Address is :  ' + str(IP2) + '\nYour Ip Location is :  Dusseldorf, Germany'), MessageBox.TYPE_INFO, timeout=10)
                            else:
                                self.session.open(MessageBox, _('Cannot connect (or server is down) !'), MessageBox.TYPE_INFO, timeout=5)
                            return
                        elif returnValue =="com_89":
                            if connected_to_internet():
                               os.system('/etc/init.d/openvpn stop > /dev/null 2>&1')
                               os.system('rm -r %s > /dev/null 2>&1 && rm -f %s > /dev/null 2>&1' % (LINKFILE1, LINKFILE2))
                               os.system('rm -r -f /etc/openvpn; mkdir /etc/openvpn') 
                               shutil.copyfile('/etc/pointvpn/cfg_conf', '/etc/openvpn/cfg.conf')
                               shutil.copyfile('/etc/pointvpn/client_conf68', '/etc/openvpn/client.conf')
                               ip = compat_urlopen("http://ip.42.pl/raw").read()  
                               with open(LINKFILE1, "wb") as f: f.write(ip)                                   
                               f = open(LINKFILE1, 'r')
                               for line in f.readlines():
                                   IP = line.strip('\n')
                                   os.system('/etc/init.d/openvpn start > /dev/null 2>&1')
                                   time.sleep(8)
                                   ip2 = compat_urlopen("http://ip.42.pl/raw").read()  
                                   with open(LINKFILE2, "wb") as f: f.write(ip2)                                       
                                   f = open(LINKFILE2, 'r')
                                   for line in f.readlines():
                                       IP2 = line.strip('\n')
                                       if ip == ip2:
                                           self.session.open(MessageBox, _('VPN Not Working?...'), MessageBox.TYPE_INFO, timeout=5)
                                       else:
                                           self.session.open(MessageBox, _('Your Ip Address is :  ' + str(IP) + '\nYour New Ip Address is :  ' + str(IP2) + '\nYour Ip Location is :  Seville, Spain'), MessageBox.TYPE_INFO, timeout=10)
                            else:
                                self.session.open(MessageBox, _('Cannot connect (or server is down) !'), MessageBox.TYPE_INFO, timeout=5)
                            return
                        elif returnValue =="com_90":
                            if connected_to_internet():
                               os.system('/etc/init.d/openvpn stop > /dev/null 2>&1')
                               os.system('rm -r %s > /dev/null 2>&1 && rm -f %s > /dev/null 2>&1' % (LINKFILE1, LINKFILE2))
                               os.system('rm -r -f /etc/openvpn; mkdir /etc/openvpn') 
                               shutil.copyfile('/etc/pointvpn/cfg_conf', '/etc/openvpn/cfg.conf')
                               shutil.copyfile('/etc/pointvpn/client_conf69', '/etc/openvpn/client.conf')
                               ip = compat_urlopen("http://ip.42.pl/raw").read()  
                               with open(LINKFILE1, "wb") as f: f.write(ip)                                   
                               f = open(LINKFILE1, 'r')
                               for line in f.readlines():
                                   IP = line.strip('\n')
                                   os.system('/etc/init.d/openvpn start > /dev/null 2>&1')
                                   time.sleep(8)
                                   ip2 = compat_urlopen("http://ip.42.pl/raw").read()  
                                   with open(LINKFILE2, "wb") as f: f.write(ip2)                                       
                                   f = open(LINKFILE2, 'r')
                                   for line in f.readlines():
                                       IP2 = line.strip('\n')
                                       if ip == ip2:
                                           self.session.open(MessageBox, _('VPN Not Working?...'), MessageBox.TYPE_INFO, timeout=5)
                                       else:
                                           self.session.open(MessageBox, _('Your Ip Address is :  ' + str(IP) + '\nYour New Ip Address is :  ' + str(IP2) + '\nYour Ip Location is :  Barcelona, Spain'), MessageBox.TYPE_INFO, timeout=10)
                            else:
                                self.session.open(MessageBox, _('Cannot connect (or server is down) !'), MessageBox.TYPE_INFO, timeout=5)
                            return
                        elif returnValue =="com_91":
                            if connected_to_internet():
                               os.system('/etc/init.d/openvpn stop > /dev/null 2>&1')
                               os.system('rm -r %s > /dev/null 2>&1 && rm -f %s > /dev/null 2>&1' % (LINKFILE1, LINKFILE2))
                               os.system('rm -r -f /etc/openvpn; mkdir /etc/openvpn') 
                               shutil.copyfile('/etc/pointvpn/cfg_conf', '/etc/openvpn/cfg.conf')
                               shutil.copyfile('/etc/pointvpn/client_conf70', '/etc/openvpn/client.conf')
                               ip = compat_urlopen("http://ip.42.pl/raw").read()  
                               with open(LINKFILE1, "wb") as f: f.write(ip)                                   
                               f = open(LINKFILE1, 'r')
                               for line in f.readlines():
                                   IP = line.strip('\n')
                                   os.system('/etc/init.d/openvpn start > /dev/null 2>&1')
                                   time.sleep(8)
                                   ip2 = compat_urlopen("http://ip.42.pl/raw").read()  
                                   with open(LINKFILE2, "wb") as f: f.write(ip2)                                       
                                   f = open(LINKFILE2, 'r')
                                   for line in f.readlines():
                                       IP2 = line.strip('\n')
                                       if ip == ip2:
                                           self.session.open(MessageBox, _('VPN Not Working?...'), MessageBox.TYPE_INFO, timeout=5)
                                       else:
                                           self.session.open(MessageBox, _('Your Ip Address is :  ' + str(IP) + '\nYour New Ip Address is :  ' + str(IP2) + '\nYour Ip Location is :  Helsinki, Finland'), MessageBox.TYPE_INFO, timeout=10)
                            else:
                                self.session.open(MessageBox, _('Cannot connect (or server is down) !'), MessageBox.TYPE_INFO, timeout=5)
                            return
                        elif returnValue =="com_92":
                            if connected_to_internet():
                               os.system('/etc/init.d/openvpn stop > /dev/null 2>&1')
                               os.system('rm -r %s > /dev/null 2>&1 && rm -f %s > /dev/null 2>&1' % (LINKFILE1, LINKFILE2))
                               os.system('rm -r -f /etc/openvpn; mkdir /etc/openvpn') 
                               shutil.copyfile('/etc/pointvpn/cfg_conf', '/etc/openvpn/cfg.conf')
                               shutil.copyfile('/etc/pointvpn/client_conf71', '/etc/openvpn/client.conf')
                               ip = compat_urlopen("http://ip.42.pl/raw").read()  
                               with open(LINKFILE1, "wb") as f: f.write(ip)                                   
                               f = open(LINKFILE1, 'r')
                               for line in f.readlines():
                                   IP = line.strip('\n')
                                   os.system('/etc/init.d/openvpn start > /dev/null 2>&1')
                                   time.sleep(8)
                                   ip2 = compat_urlopen("http://ip.42.pl/raw").read()  
                                   with open(LINKFILE2, "wb") as f: f.write(ip2)                                       
                                   f = open(LINKFILE2, 'r')
                                   for line in f.readlines():
                                       IP2 = line.strip('\n')
                                       if ip == ip2:
                                           self.session.open(MessageBox, _('VPN Not Working?...'), MessageBox.TYPE_INFO, timeout=5)
                                       else:
                                           self.session.open(MessageBox, _('Your Ip Address is :  ' + str(IP) + '\nYour New Ip Address is :  ' + str(IP2) + '\nYour Ip Location is :  Helsinki 2, Finland'), MessageBox.TYPE_INFO, timeout=10)
                            else:
                                self.session.open(MessageBox, _('Cannot connect (or server is down) !'), MessageBox.TYPE_INFO, timeout=5)
                            return
                        elif returnValue =="com_93":
                            if connected_to_internet():
                               os.system('/etc/init.d/openvpn stop > /dev/null 2>&1')
                               os.system('rm -r %s > /dev/null 2>&1 && rm -f %s > /dev/null 2>&1' % (LINKFILE1, LINKFILE2))
                               os.system('rm -r -f /etc/openvpn; mkdir /etc/openvpn') 
                               shutil.copyfile('/etc/pointvpn/cfg_conf', '/etc/openvpn/cfg.conf')
                               shutil.copyfile('/etc/pointvpn/client_conf72', '/etc/openvpn/client.conf')
                               ip = compat_urlopen("http://ip.42.pl/raw").read()  
                               with open(LINKFILE1, "wb") as f: f.write(ip)                                   
                               f = open(LINKFILE1, 'r')
                               for line in f.readlines():
                                   IP = line.strip('\n')
                                   os.system('/etc/init.d/openvpn start > /dev/null 2>&1')
                                   time.sleep(8)
                                   ip2 = compat_urlopen("http://ip.42.pl/raw").read()  
                                   with open(LINKFILE2, "wb") as f: f.write(ip2)                                       
                                   f = open(LINKFILE2, 'r')
                                   for line in f.readlines():
                                       IP2 = line.strip('\n')
                                       if ip == ip2:
                                           self.session.open(MessageBox, _('VPN Not Working?...'), MessageBox.TYPE_INFO, timeout=5)
                                       else:
                                           self.session.open(MessageBox, _('Your Ip Address is :  ' + str(IP) + '\nYour New Ip Address is :  ' + str(IP2) + '\nYour Ip Location is :  Paris, France'), MessageBox.TYPE_INFO, timeout=10)
                            else:
                                self.session.open(MessageBox, _('Cannot connect (or server is down) !'), MessageBox.TYPE_INFO, timeout=5)
                            return
                        elif returnValue =="com_94":
                            if connected_to_internet():
                               os.system('/etc/init.d/openvpn stop > /dev/null 2>&1')
                               os.system('rm -r %s > /dev/null 2>&1 && rm -f %s > /dev/null 2>&1' % (LINKFILE1, LINKFILE2))
                               os.system('rm -r -f /etc/openvpn; mkdir /etc/openvpn') 
                               shutil.copyfile('/etc/pointvpn/cfg_conf', '/etc/openvpn/cfg.conf')
                               shutil.copyfile('/etc/pointvpn/client_conf73', '/etc/openvpn/client.conf')
                               ip = compat_urlopen("http://ip.42.pl/raw").read()  
                               with open(LINKFILE1, "wb") as f: f.write(ip)                                   
                               f = open(LINKFILE1, 'r')
                               for line in f.readlines():
                                   IP = line.strip('\n')
                                   os.system('/etc/init.d/openvpn start > /dev/null 2>&1')
                                   time.sleep(8)
                                   ip2 = compat_urlopen("http://ip.42.pl/raw").read()  
                                   with open(LINKFILE2, "wb") as f: f.write(ip2)                                       
                                   f = open(LINKFILE2, 'r')
                                   for line in f.readlines():
                                       IP2 = line.strip('\n')
                                       if ip == ip2:
                                           self.session.open(MessageBox, _('VPN Not Working?...'), MessageBox.TYPE_INFO, timeout=5)
                                       else:
                                           self.session.open(MessageBox, _('Your Ip Address is :  ' + str(IP) + '\nYour New Ip Address is :  ' + str(IP2) + '\nYour Ip Location is :  London, United Kingdom'), MessageBox.TYPE_INFO, timeout=10)
                            else:
                                self.session.open(MessageBox, _('Cannot connect (or server is down) !'), MessageBox.TYPE_INFO, timeout=5)
                            return
                        elif returnValue =="com_95":
                            if connected_to_internet():
                               os.system('/etc/init.d/openvpn stop > /dev/null 2>&1')
                               os.system('rm -r %s > /dev/null 2>&1 && rm -f %s > /dev/null 2>&1' % (LINKFILE1, LINKFILE2))
                               os.system('rm -r -f /etc/openvpn; mkdir /etc/openvpn') 
                               shutil.copyfile('/etc/pointvpn/cfg_conf', '/etc/openvpn/cfg.conf')
                               shutil.copyfile('/etc/pointvpn/client_conf74', '/etc/openvpn/client.conf')
                               ip = compat_urlopen("http://ip.42.pl/raw").read()  
                               with open(LINKFILE1, "wb") as f: f.write(ip)                                   
                               f = open(LINKFILE1, 'r')
                               for line in f.readlines():
                                   IP = line.strip('\n')
                                   os.system('/etc/init.d/openvpn start > /dev/null 2>&1')
                                   time.sleep(8)
                                   ip2 = compat_urlopen("http://ip.42.pl/raw").read()  
                                   with open(LINKFILE2, "wb") as f: f.write(ip2)                                       
                                   f = open(LINKFILE2, 'r')
                                   for line in f.readlines():
                                       IP2 = line.strip('\n')
                                       if ip == ip2:
                                           self.session.open(MessageBox, _('VPN Not Working?...'), MessageBox.TYPE_INFO, timeout=5)
                                       else:
                                           self.session.open(MessageBox, _('Your Ip Address is :  ' + str(IP) + '\nYour New Ip Address is :  ' + str(IP2) + '\nYour Ip Location is :  London 2, United Kingdom'), MessageBox.TYPE_INFO, timeout=10)
                            else:
                                self.session.open(MessageBox, _('Cannot connect (or server is down) !'), MessageBox.TYPE_INFO, timeout=5)
                            return
                        elif returnValue =="com_96":
                            if connected_to_internet():
                               os.system('/etc/init.d/openvpn stop > /dev/null 2>&1')
                               os.system('rm -r %s > /dev/null 2>&1 && rm -f %s > /dev/null 2>&1' % (LINKFILE1, LINKFILE2))
                               os.system('rm -r -f /etc/openvpn; mkdir /etc/openvpn') 
                               shutil.copyfile('/etc/pointvpn/cfg_conf', '/etc/openvpn/cfg.conf')
                               shutil.copyfile('/etc/pointvpn/client_conf75', '/etc/openvpn/client.conf')
                               ip = compat_urlopen("http://ip.42.pl/raw").read()  
                               with open(LINKFILE1, "wb") as f: f.write(ip)                                   
                               f = open(LINKFILE1, 'r')
                               for line in f.readlines():
                                   IP = line.strip('\n')
                                   os.system('/etc/init.d/openvpn start > /dev/null 2>&1')
                                   time.sleep(8)
                                   ip2 = compat_urlopen("http://ip.42.pl/raw").read()  
                                   with open(LINKFILE2, "wb") as f: f.write(ip2)                                       
                                   f = open(LINKFILE2, 'r')
                                   for line in f.readlines():
                                       IP2 = line.strip('\n')
                                       if ip == ip2:
                                           self.session.open(MessageBox, _('VPN Not Working?...'), MessageBox.TYPE_INFO, timeout=5)
                                       else:
                                           self.session.open(MessageBox, _('Your Ip Address is :  ' + str(IP) + '\nYour New Ip Address is :  ' + str(IP2) + '\nYour Ip Location is :  Thessaloniki, Greece'), MessageBox.TYPE_INFO, timeout=10)
                            else:
                                self.session.open(MessageBox, _('Cannot connect (or server is down) !'), MessageBox.TYPE_INFO, timeout=5)
                            return
                        elif returnValue =="com_97":
                            if connected_to_internet():
                               os.system('/etc/init.d/openvpn stop > /dev/null 2>&1')
                               os.system('rm -r %s > /dev/null 2>&1 && rm -f %s > /dev/null 2>&1' % (LINKFILE1, LINKFILE2))
                               os.system('rm -r -f /etc/openvpn; mkdir /etc/openvpn') 
                               shutil.copyfile('/etc/pointvpn/cfg_conf', '/etc/openvpn/cfg.conf')
                               shutil.copyfile('/etc/pointvpn/client_conf76', '/etc/openvpn/client.conf')
                               ip = compat_urlopen("http://ip.42.pl/raw").read()  
                               with open(LINKFILE1, "wb") as f: f.write(ip)                                   
                               f = open(LINKFILE1, 'r')
                               for line in f.readlines():
                                   IP = line.strip('\n')
                                   os.system('/etc/init.d/openvpn start > /dev/null 2>&1')
                                   time.sleep(8)
                                   ip2 = compat_urlopen("http://ip.42.pl/raw").read()  
                                   with open(LINKFILE2, "wb") as f: f.write(ip2)                                       
                                   f = open(LINKFILE2, 'r')
                                   for line in f.readlines():
                                       IP2 = line.strip('\n')
                                       if ip == ip2:
                                           self.session.open(MessageBox, _('VPN Not Working?...'), MessageBox.TYPE_INFO, timeout=5)
                                       else:
                                           self.session.open(MessageBox, _('Your Ip Address is :  ' + str(IP) + '\nYour New Ip Address is :  ' + str(IP2) + '\nYour Ip Location is :  Hong Kong, Hong Kong'), MessageBox.TYPE_INFO, timeout=10)
                            else:
                                self.session.open(MessageBox, _('Cannot connect (or server is down) !'), MessageBox.TYPE_INFO, timeout=5)
                            return
                        elif returnValue =="com_98":
                            if connected_to_internet():
                               os.system('/etc/init.d/openvpn stop > /dev/null 2>&1')
                               os.system('rm -r %s > /dev/null 2>&1 && rm -f %s > /dev/null 2>&1' % (LINKFILE1, LINKFILE2))
                               os.system('rm -r -f /etc/openvpn; mkdir /etc/openvpn') 
                               shutil.copyfile('/etc/pointvpn/cfg_conf', '/etc/openvpn/cfg.conf')
                               shutil.copyfile('/etc/pointvpn/client_conf77', '/etc/openvpn/client.conf')
                               ip = compat_urlopen("http://ip.42.pl/raw").read()  
                               with open(LINKFILE1, "wb") as f: f.write(ip)                                   
                               f = open(LINKFILE1, 'r')
                               for line in f.readlines():
                                   IP = line.strip('\n')
                                   os.system('/etc/init.d/openvpn start > /dev/null 2>&1')
                                   time.sleep(8)
                                   ip2 = compat_urlopen("http://ip.42.pl/raw").read()  
                                   with open(LINKFILE2, "wb") as f: f.write(ip2)                                       
                                   f = open(LINKFILE2, 'r')
                                   for line in f.readlines():
                                       IP2 = line.strip('\n')
                                       if ip == ip2:
                                           self.session.open(MessageBox, _('VPN Not Working?...'), MessageBox.TYPE_INFO, timeout=5)
                                       else:
                                           self.session.open(MessageBox, _('Your Ip Address is :  ' + str(IP) + '\nYour New Ip Address is :  ' + str(IP2) + '\nYour Ip Location is :  Jakarta 6, Indonesia'), MessageBox.TYPE_INFO, timeout=10)
                            else:
                                self.session.open(MessageBox, _('Cannot connect (or server is down) !'), MessageBox.TYPE_INFO, timeout=5)
                            return
                        elif returnValue =="com_99":
                            if connected_to_internet():
                               os.system('/etc/init.d/openvpn stop > /dev/null 2>&1')
                               os.system('rm -r %s > /dev/null 2>&1 && rm -f %s > /dev/null 2>&1' % (LINKFILE1, LINKFILE2))
                               os.system('rm -r -f /etc/openvpn; mkdir /etc/openvpn') 
                               shutil.copyfile('/etc/pointvpn/cfg_conf', '/etc/openvpn/cfg.conf')
                               shutil.copyfile('/etc/pointvpn/client_conf78', '/etc/openvpn/client.conf')
                               ip = compat_urlopen("http://ip.42.pl/raw").read()  
                               with open(LINKFILE1, "wb") as f: f.write(ip)                                   
                               f = open(LINKFILE1, 'r')
                               for line in f.readlines():
                                   IP = line.strip('\n')
                                   os.system('/etc/init.d/openvpn start > /dev/null 2>&1')
                                   time.sleep(8)
                                   ip2 = compat_urlopen("http://ip.42.pl/raw").read()  
                                   with open(LINKFILE2, "wb") as f: f.write(ip2)                                       
                                   f = open(LINKFILE2, 'r')
                                   for line in f.readlines():
                                       IP2 = line.strip('\n')
                                       if ip == ip2:
                                           self.session.open(MessageBox, _('VPN Not Working?...'), MessageBox.TYPE_INFO, timeout=5)
                                       else:
                                           self.session.open(MessageBox, _('Your Ip Address is :  ' + str(IP) + '\nYour New Ip Address is :  ' + str(IP2) + '\nYour Ip Location is :  Jakarta 5, Indonesia'), MessageBox.TYPE_INFO, timeout=10)
                            else:
                                self.session.open(MessageBox, _('Cannot connect (or server is down) !'), MessageBox.TYPE_INFO, timeout=5)
                            return
                        elif returnValue =="com_100":
                            if connected_to_internet():
                               os.system('/etc/init.d/openvpn stop > /dev/null 2>&1')
                               os.system('rm -r %s > /dev/null 2>&1 && rm -f %s > /dev/null 2>&1' % (LINKFILE1, LINKFILE2))
                               os.system('rm -r -f /etc/openvpn; mkdir /etc/openvpn') 
                               shutil.copyfile('/etc/pointvpn/cfg_conf', '/etc/openvpn/cfg.conf')
                               shutil.copyfile('/etc/pointvpn/client_conf79', '/etc/openvpn/client.conf')
                               ip = compat_urlopen("http://ip.42.pl/raw").read()  
                               with open(LINKFILE1, "wb") as f: f.write(ip)                                   
                               f = open(LINKFILE1, 'r')
                               for line in f.readlines():
                                   IP = line.strip('\n')
                                   os.system('/etc/init.d/openvpn start > /dev/null 2>&1')
                                   time.sleep(8)
                                   ip2 = compat_urlopen("http://ip.42.pl/raw").read()  
                                   with open(LINKFILE2, "wb") as f: f.write(ip2)                                       
                                   f = open(LINKFILE2, 'r')
                                   for line in f.readlines():
                                       IP2 = line.strip('\n')
                                       if ip == ip2:
                                           self.session.open(MessageBox, _('VPN Not Working?...'), MessageBox.TYPE_INFO, timeout=5)
                                       else:
                                           self.session.open(MessageBox, _('Your Ip Address is :  ' + str(IP) + '\nYour New Ip Address is :  ' + str(IP2) + '\nYour Ip Location is :  Dublin, Ireland'), MessageBox.TYPE_INFO, timeout=10)
                            else:
                                self.session.open(MessageBox, _('Cannot connect (or server is down) !'), MessageBox.TYPE_INFO, timeout=5)
                            return              
                        elif returnValue =="com_101":
                            if connected_to_internet():
                               os.system('/etc/init.d/openvpn stop > /dev/null 2>&1')
                               os.system('rm -r %s > /dev/null 2>&1 && rm -f %s > /dev/null 2>&1' % (LINKFILE1, LINKFILE2))
                               os.system('rm -r -f /etc/openvpn; mkdir /etc/openvpn') 
                               shutil.copyfile('/etc/pointvpn/cfg_conf', '/etc/openvpn/cfg.conf')
                               shutil.copyfile('/etc/pointvpn/client_conf80', '/etc/openvpn/client.conf')
                               ip = compat_urlopen("http://ip.42.pl/raw").read()  
                               with open(LINKFILE1, "wb") as f: f.write(ip)                                   
                               f = open(LINKFILE1, 'r')
                               for line in f.readlines():
                                   IP = line.strip('\n')
                                   os.system('/etc/init.d/openvpn start > /dev/null 2>&1')
                                   time.sleep(8)
                                   ip2 = compat_urlopen("http://ip.42.pl/raw").read()  
                                   with open(LINKFILE2, "wb") as f: f.write(ip2)                                       
                                   f = open(LINKFILE2, 'r')
                                   for line in f.readlines():
                                       IP2 = line.strip('\n')
                                       if ip == ip2:
                                           self.session.open(MessageBox, _('VPN Not Working?...'), MessageBox.TYPE_INFO, timeout=5)
                                       else:
                                           self.session.open(MessageBox, _('Your Ip Address is :  ' + str(IP) + '\nYour New Ip Address is :  ' + str(IP2) + '\nYour Ip Location is :  Tel Aviv, Israel'), MessageBox.TYPE_INFO, timeout=10)
                            else:
                                self.session.open(MessageBox, _('Cannot connect (or server is down) !'), MessageBox.TYPE_INFO, timeout=5)
                            return              
                        elif returnValue =="com_102":
                            if connected_to_internet():
                               os.system('/etc/init.d/openvpn stop > /dev/null 2>&1')
                               os.system('rm -r %s > /dev/null 2>&1 && rm -f %s > /dev/null 2>&1' % (LINKFILE1, LINKFILE2))
                               os.system('rm -r -f /etc/openvpn; mkdir /etc/openvpn') 
                               shutil.copyfile('/etc/pointvpn/cfg_conf', '/etc/openvpn/cfg.conf')
                               shutil.copyfile('/etc/pointvpn/client_conf81', '/etc/openvpn/client.conf')
                               ip = compat_urlopen("http://ip.42.pl/raw").read()  
                               with open(LINKFILE1, "wb") as f: f.write(ip)                                   
                               f = open(LINKFILE1, 'r')
                               for line in f.readlines():
                                   IP = line.strip('\n')
                                   os.system('/etc/init.d/openvpn start > /dev/null 2>&1')
                                   time.sleep(8)
                                   ip2 = compat_urlopen("http://ip.42.pl/raw").read()  
                                   with open(LINKFILE2, "wb") as f: f.write(ip2)                                       
                                   f = open(LINKFILE2, 'r')
                                   for line in f.readlines():
                                       IP2 = line.strip('\n')
                                       if ip == ip2:
                                           self.session.open(MessageBox, _('VPN Not Working?...'), MessageBox.TYPE_INFO, timeout=5)
                                       else:
                                           self.session.open(MessageBox, _('Your Ip Address is :  ' + str(IP) + '\nYour New Ip Address is :  ' + str(IP2) + '\nYour Ip Location is :  Mumbai, India'), MessageBox.TYPE_INFO, timeout=10)
                            else:
                                self.session.open(MessageBox, _('Cannot connect (or server is down) !'), MessageBox.TYPE_INFO, timeout=5)
                            return
                        elif returnValue =="com_103":
                            if connected_to_internet():
                               os.system('/etc/init.d/openvpn stop > /dev/null 2>&1')
                               os.system('rm -r %s > /dev/null 2>&1 && rm -f %s > /dev/null 2>&1' % (LINKFILE1, LINKFILE2))
                               os.system('rm -r -f /etc/openvpn; mkdir /etc/openvpn') 
                               shutil.copyfile('/etc/pointvpn/cfg_conf', '/etc/openvpn/cfg.conf')
                               shutil.copyfile('/etc/pointvpn/client_conf82', '/etc/openvpn/client.conf')
                               ip = compat_urlopen("http://ip.42.pl/raw").read()  
                               with open(LINKFILE1, "wb") as f: f.write(ip)                                   
                               f = open(LINKFILE1, 'r')
                               for line in f.readlines():
                                   IP = line.strip('\n')
                                   os.system('/etc/init.d/openvpn start > /dev/null 2>&1')
                                   time.sleep(8)
                                   ip2 = compat_urlopen("http://ip.42.pl/raw").read()  
                                   with open(LINKFILE2, "wb") as f: f.write(ip2)                                       
                                   f = open(LINKFILE2, 'r')
                                   for line in f.readlines():
                                       IP2 = line.strip('\n')
                                       if ip == ip2:
                                           self.session.open(MessageBox, _('VPN Not Working?...'), MessageBox.TYPE_INFO, timeout=5)
                                       else:
                                           self.session.open(MessageBox, _('Your Ip Address is :  ' + str(IP) + '\nYour New Ip Address is :  ' + str(IP2) + '\nYour Ip Location is :  Palermo, Italy'), MessageBox.TYPE_INFO, timeout=10)
                            else:
                                self.session.open(MessageBox, _('Cannot connect (or server is down) !'), MessageBox.TYPE_INFO, timeout=5)
                            return
                        elif returnValue =="com_104":
                            if connected_to_internet():
                               os.system('/etc/init.d/openvpn stop > /dev/null 2>&1')
                               os.system('rm -r %s > /dev/null 2>&1 && rm -f %s > /dev/null 2>&1' % (LINKFILE1, LINKFILE2))
                               os.system('rm -r -f /etc/openvpn; mkdir /etc/openvpn') 
                               shutil.copyfile('/etc/pointvpn/cfg_conf', '/etc/openvpn/cfg.conf')
                               shutil.copyfile('/etc/pointvpn/client_conf83', '/etc/openvpn/client.conf')
                               ip = compat_urlopen("http://ip.42.pl/raw").read()  
                               with open(LINKFILE1, "wb") as f: f.write(ip)                                   
                               f = open(LINKFILE1, 'r')
                               for line in f.readlines():
                                   IP = line.strip('\n')
                                   os.system('/etc/init.d/openvpn start > /dev/null 2>&1')
                                   time.sleep(8)
                                   ip2 = compat_urlopen("http://ip.42.pl/raw").read()  
                                   with open(LINKFILE2, "wb") as f: f.write(ip2)                                       
                                   f = open(LINKFILE2, 'r')
                                   for line in f.readlines():
                                       IP2 = line.strip('\n')
                                       if ip == ip2:
                                           self.session.open(MessageBox, _('VPN Not Working?...'), MessageBox.TYPE_INFO, timeout=5)
                                       else:
                                           self.session.open(MessageBox, _('Your Ip Address is :  ' + str(IP) + '\nYour New Ip Address is :  ' + str(IP2) + '\nYour Ip Location is :  Tokyo 6, Japan'), MessageBox.TYPE_INFO, timeout=10)
                            else:
                                self.session.open(MessageBox, _('Cannot connect (or server is down) !'), MessageBox.TYPE_INFO, timeout=5)
                            return
                        elif returnValue =="com_105":
                            if connected_to_internet():
                               os.system('/etc/init.d/openvpn stop > /dev/null 2>&1')
                               os.system('rm -r %s > /dev/null 2>&1 && rm -f %s > /dev/null 2>&1' % (LINKFILE1, LINKFILE2))
                               os.system('rm -r -f /etc/openvpn; mkdir /etc/openvpn') 
                               shutil.copyfile('/etc/pointvpn/cfg_conf', '/etc/openvpn/cfg.conf')
                               shutil.copyfile('/etc/pointvpn/client_conf84', '/etc/openvpn/client.conf')
                               ip = compat_urlopen("http://ip.42.pl/raw").read()  
                               with open(LINKFILE1, "wb") as f: f.write(ip)                                   
                               f = open(LINKFILE1, 'r')
                               for line in f.readlines():
                                   IP = line.strip('\n')
                                   os.system('/etc/init.d/openvpn start > /dev/null 2>&1')
                                   time.sleep(8)
                                   ip2 = compat_urlopen("http://ip.42.pl/raw").read()  
                                   with open(LINKFILE2, "wb") as f: f.write(ip2)                                       
                                   f = open(LINKFILE2, 'r')
                                   for line in f.readlines():
                                       IP2 = line.strip('\n')
                                       if ip == ip2:
                                           self.session.open(MessageBox, _('VPN Not Working?...'), MessageBox.TYPE_INFO, timeout=5)
                                       else:
                                           self.session.open(MessageBox, _('Your Ip Address is :  ' + str(IP) + '\nYour New Ip Address is :  ' + str(IP2) + '\nYour Ip Location is :  Tokyo 2, Japan'), MessageBox.TYPE_INFO, timeout=10)
                            else:
                                self.session.open(MessageBox, _('Cannot connect (or server is down) !'), MessageBox.TYPE_INFO, timeout=5)
                            return
                        elif returnValue =="com_106":
                            if connected_to_internet():
                               os.system('/etc/init.d/openvpn stop > /dev/null 2>&1')
                               os.system('rm -r %s > /dev/null 2>&1 && rm -f %s > /dev/null 2>&1' % (LINKFILE1, LINKFILE2))
                               os.system('rm -r -f /etc/openvpn; mkdir /etc/openvpn') 
                               shutil.copyfile('/etc/cfg.conf', '/etc/openvpn/cfg.conf')
                               shutil.copyfile('/etc/client.conf85', '/etc/openvpn/client.conf')
                               ip = compat_urlopen("http://ip.42.pl/raw").read()  
                               with open(LINKFILE1, "wb") as f: f.write(ip)                                   
                               f = open(LINKFILE1, 'r')
                               for line in f.readlines():
                                   IP = line.strip('\n')
                                   os.system('/etc/init.d/openvpn start > /dev/null 2>&1')
                                   time.sleep(8)
                                   ip2 = compat_urlopen("http://ip.42.pl/raw").read()  
                                   with open(LINKFILE2, "wb") as f: f.write(ip2)                                       
                                   f = open(LINKFILE2, 'r')
                                   for line in f.readlines():
                                       IP2 = line.strip('\n')
                                       if ip == ip2:
                                           self.session.open(MessageBox, _('VPN Not Working?...'), MessageBox.TYPE_INFO, timeout=5)
                                       else:
                                           self.session.open(MessageBox, _('Your Ip Address is :  ' + str(IP) + '\nYour New Ip Address is :  ' + str(IP2) + '\nYour Ip Location is :  Tokyo 2, Japan'), MessageBox.TYPE_INFO, timeout=10)
                            else:
                                self.session.open(MessageBox, _('Cannot connect (or server is down) !'), MessageBox.TYPE_INFO, timeout=5)
                            return
                        elif returnValue =="com_107":
                            if connected_to_internet():
                               os.system('/etc/init.d/openvpn stop > /dev/null 2>&1')
                               os.system('rm -r %s > /dev/null 2>&1 && rm -f %s > /dev/null 2>&1' % (LINKFILE1, LINKFILE2))
                               os.system('rm -r -f /etc/openvpn; mkdir /etc/openvpn') 
                               shutil.copyfile('/etc/pointvpn/cfg_conf', '/etc/openvpn/cfg.conf')
                               shutil.copyfile('/etc/pointvpn/client_conf86', '/etc/openvpn/client.conf')
                               ip = compat_urlopen("http://ip.42.pl/raw").read()  
                               with open(LINKFILE1, "wb") as f: f.write(ip)                                   
                               f = open(LINKFILE1, 'r')
                               for line in f.readlines():
                                   IP = line.strip('\n')
                                   os.system('/etc/init.d/openvpn start > /dev/null 2>&1')
                                   time.sleep(8)
                                   ip2 = compat_urlopen("http://ip.42.pl/raw").read()  
                                   with open(LINKFILE2, "wb") as f: f.write(ip2)                                       
                                   f = open(LINKFILE2, 'r')
                                   for line in f.readlines():
                                       IP2 = line.strip('\n')
                                       if ip == ip2:
                                           self.session.open(MessageBox, _('VPN Not Working?...'), MessageBox.TYPE_INFO, timeout=5)
                                       else:
                                           self.session.open(MessageBox, _('Your Ip Address is :  ' + str(IP) + '\nYour New Ip Address is :  ' + str(IP2) + '\nYour Ip Location is :  Rotterdam, Netherlands'), MessageBox.TYPE_INFO, timeout=10)
                            else:
                                self.session.open(MessageBox, _('Cannot connect (or server is down) !'), MessageBox.TYPE_INFO, timeout=5)
                            return
                        elif returnValue =="com_108":
                            if connected_to_internet():
                               os.system('/etc/init.d/openvpn stop > /dev/null 2>&1')
                               os.system('rm -r %s > /dev/null 2>&1 && rm -f %s > /dev/null 2>&1' % (LINKFILE1, LINKFILE2))
                               os.system('rm -r -f /etc/openvpn; mkdir /etc/openvpn') 
                               shutil.copyfile('/etc/pointvpn/cfg_conf', '/etc/openvpn/cfg.conf')
                               shutil.copyfile('/etc/pointvpn/client_conf87', '/etc/openvpn/client.conf')
                               ip = compat_urlopen("http://ip.42.pl/raw").read()  
                               with open(LINKFILE1, "wb") as f: f.write(ip)                                   
                               f = open(LINKFILE1, 'r')
                               for line in f.readlines():
                                   IP = line.strip('\n')
                                   os.system('/etc/init.d/openvpn start > /dev/null 2>&1')
                                   time.sleep(8)
                                   ip2 = compat_urlopen("http://ip.42.pl/raw").read()  
                                   with open(LINKFILE2, "wb") as f: f.write(ip2)                                       
                                   f = open(LINKFILE2, 'r')
                                   for line in f.readlines():
                                       IP2 = line.strip('\n')
                                       if ip == ip2:
                                           self.session.open(MessageBox, _('VPN Not Working?...'), MessageBox.TYPE_INFO, timeout=5)
                                       else:
                                           self.session.open(MessageBox, _('Your Ip Address is :  ' + str(IP) + '\nYour New Ip Address is :  ' + str(IP2) + '\nYour Ip Location is :  Amsterdam, Netherlands'), MessageBox.TYPE_INFO, timeout=10)
                            else:
                                self.session.open(MessageBox, _('Cannot connect (or server is down) !'), MessageBox.TYPE_INFO, timeout=5)
                            return
                        elif returnValue =="com_109":
                            if connected_to_internet():
                               os.system('/etc/init.d/openvpn stop > /dev/null 2>&1')
                               os.system('rm -r %s > /dev/null 2>&1 && rm -f %s > /dev/null 2>&1' % (LINKFILE1, LINKFILE2))
                               os.system('rm -r -f /etc/openvpn; mkdir /etc/openvpn') 
                               shutil.copyfile('/etc/pointvpn/cfg_conf', '/etc/openvpn/cfg.conf')
                               shutil.copyfile('/etc/pointvpn/client_conf88', '/etc/openvpn/client.conf')
                               ip = compat_urlopen("http://ip.42.pl/raw").read()  
                               with open(LINKFILE1, "wb") as f: f.write(ip)                                   
                               f = open(LINKFILE1, 'r')
                               for line in f.readlines():
                                   IP = line.strip('\n')
                                   os.system('/etc/init.d/openvpn start > /dev/null 2>&1')
                                   time.sleep(8)
                                   ip2 = compat_urlopen("http://ip.42.pl/raw").read()  
                                   with open(LINKFILE2, "wb") as f: f.write(ip2)                                       
                                   f = open(LINKFILE2, 'r')
                                   for line in f.readlines():
                                       IP2 = line.strip('\n')
                                       if ip == ip2:
                                           self.session.open(MessageBox, _('VPN Not Working?...'), MessageBox.TYPE_INFO, timeout=5)
                                       else:
                                           self.session.open(MessageBox, _('Your Ip Address is :  ' + str(IP) + '\nYour New Ip Address is :  ' + str(IP2) + '\nYour Ip Location is :  Manila, Philippines'), MessageBox.TYPE_INFO, timeout=10)
                            else:
                                self.session.open(MessageBox, _('Cannot connect (or server is down) !'), MessageBox.TYPE_INFO, timeout=5)
                            return
                        elif returnValue =="com_110":
                            if connected_to_internet():
                               os.system('/etc/init.d/openvpn stop > /dev/null 2>&1')
                               os.system('rm -r %s > /dev/null 2>&1 && rm -f %s > /dev/null 2>&1' % (LINKFILE1, LINKFILE2))
                               os.system('rm -r -f /etc/openvpn; mkdir /etc/openvpn') 
                               shutil.copyfile('/etc/pointvpn/cfg_conf', '/etc/openvpn/cfg.conf')
                               shutil.copyfile('/etc/pointvpn/client_conf89', '/etc/openvpn/client.conf')
                               ip = compat_urlopen("http://ip.42.pl/raw").read()  
                               with open(LINKFILE1, "wb") as f: f.write(ip)                                   
                               f = open(LINKFILE1, 'r')
                               for line in f.readlines():
                                   IP = line.strip('\n')
                                   os.system('/etc/init.d/openvpn start > /dev/null 2>&1')
                                   time.sleep(8)
                                   ip2 = compat_urlopen("http://ip.42.pl/raw").read()  
                                   with open(LINKFILE2, "wb") as f: f.write(ip2)                                       
                                   f = open(LINKFILE2, 'r')
                                   for line in f.readlines():
                                       IP2 = line.strip('\n')
                                       if ip == ip2:
                                           self.session.open(MessageBox, _('VPN Not Working?...'), MessageBox.TYPE_INFO, timeout=5)
                                       else:
                                           self.session.open(MessageBox, _('Your Ip Address is :  ' + str(IP) + '\nYour New Ip Address is :  ' + str(IP2) + '\nYour Ip Location is :  Warsaw, Poland'), MessageBox.TYPE_INFO, timeout=10)
                            else:
                                self.session.open(MessageBox, _('Cannot connect (or server is down) !'), MessageBox.TYPE_INFO, timeout=5)
                            return
                        elif returnValue =="com_111":
                            if connected_to_internet():
                               os.system('/etc/init.d/openvpn stop > /dev/null 2>&1')
                               os.system('rm -r %s > /dev/null 2>&1 && rm -f %s > /dev/null 2>&1' % (LINKFILE1, LINKFILE2))
                               os.system('rm -r -f /etc/openvpn; mkdir /etc/openvpn') 
                               shutil.copyfile('/etc/pointvpn/cfg_conf', '/etc/openvpn/cfg.conf')
                               shutil.copyfile('/etc/pointvpn/client_conf90', '/etc/openvpn/client.conf')
                               ip = compat_urlopen("http://ip.42.pl/raw").read()  
                               with open(LINKFILE1, "wb") as f: f.write(ip)                                   
                               f = open(LINKFILE1, 'r')
                               for line in f.readlines():
                                   IP = line.strip('\n')
                                   os.system('/etc/init.d/openvpn start > /dev/null 2>&1')
                                   time.sleep(8)
                                   ip2 = compat_urlopen("http://ip.42.pl/raw").read()  
                                   with open(LINKFILE2, "wb") as f: f.write(ip2)                                       
                                   f = open(LINKFILE2, 'r')
                                   for line in f.readlines():
                                       IP2 = line.strip('\n')
                                       if ip == ip2:
                                           self.session.open(MessageBox, _('VPN Not Working?...'), MessageBox.TYPE_INFO, timeout=5)
                                       else:
                                           self.session.open(MessageBox, _('Your Ip Address is :  ' + str(IP) + '\nYour New Ip Address is :  ' + str(IP2) + '\nYour Ip Location is :  Bucharest, Romania'), MessageBox.TYPE_INFO, timeout=10)
                            else:
                                self.session.open(MessageBox, _('Cannot connect (or server is down) !'), MessageBox.TYPE_INFO, timeout=5)
                            return
                        elif returnValue =="com_112":
                            if connected_to_internet():
                               os.system('/etc/init.d/openvpn stop > /dev/null 2>&1')
                               os.system('rm -r %s > /dev/null 2>&1 && rm -f %s > /dev/null 2>&1' % (LINKFILE1, LINKFILE2))
                               os.system('rm -r -f /etc/openvpn; mkdir /etc/openvpn') 
                               shutil.copyfile('/etc/pointvpn/cfg_conf', '/etc/openvpn/cfg.conf')
                               shutil.copyfile('/etc/pointvpn/client_conf91', '/etc/openvpn/client.conf')
                               ip = compat_urlopen("http://ip.42.pl/raw").read()  
                               with open(LINKFILE1, "wb") as f: f.write(ip)                                   
                               f = open(LINKFILE1, 'r')
                               for line in f.readlines():
                                   IP = line.strip('\n')
                                   os.system('/etc/init.d/openvpn start > /dev/null 2>&1')
                                   time.sleep(8)
                                   ip2 = compat_urlopen("http://ip.42.pl/raw").read()  
                                   with open(LINKFILE2, "wb") as f: f.write(ip2)                                       
                                   f = open(LINKFILE2, 'r')
                                   for line in f.readlines():
                                       IP2 = line.strip('\n')
                                       if ip == ip2:
                                           self.session.open(MessageBox, _('VPN Not Working?...'), MessageBox.TYPE_INFO, timeout=5)
                                       else:
                                           self.session.open(MessageBox, _('Your Ip Address is :  ' + str(IP) + '\nYour New Ip Address is :  ' + str(IP2) + '\nYour Ip Location is :  St Petersburg, Russian Federation'), MessageBox.TYPE_INFO, timeout=10)
                            else:
                                self.session.open(MessageBox, _('Cannot connect (or server is down) !'), MessageBox.TYPE_INFO, timeout=5)
                            return
                        elif returnValue =="com_113":
                            if connected_to_internet():
                               os.system('/etc/init.d/openvpn stop > /dev/null 2>&1')
                               os.system('rm -r %s > /dev/null 2>&1 && rm -f %s > /dev/null 2>&1' % (LINKFILE1, LINKFILE2))
                               os.system('rm -r -f /etc/openvpn; mkdir /etc/openvpn') 
                               shutil.copyfile('/etc/pointvpn/cfg_conf', '/etc/openvpn/cfg.conf')
                               shutil.copyfile('/etc/pointvpn/client_conf92', '/etc/openvpn/client.conf')
                               ip = compat_urlopen("http://ip.42.pl/raw").read()  
                               with open(LINKFILE1, "wb") as f: f.write(ip)                                   
                               f = open(LINKFILE1, 'r')
                               for line in f.readlines():
                                   IP = line.strip('\n')
                                   os.system('/etc/init.d/openvpn start > /dev/null 2>&1')
                                   time.sleep(8)
                                   ip2 = compat_urlopen("http://ip.42.pl/raw").read()  
                                   with open(LINKFILE2, "wb") as f: f.write(ip2)                                       
                                   f = open(LINKFILE2, 'r')
                                   for line in f.readlines():
                                       IP2 = line.strip('\n')
                                       if ip == ip2:
                                           self.session.open(MessageBox, _('VPN Not Working?...'), MessageBox.TYPE_INFO, timeout=5)
                                       else:
                                           self.session.open(MessageBox, _('Your Ip Address is :  ' + str(IP) + '\nYour New Ip Address is :  ' + str(IP2) + '\nYour Ip Location is :  Moscow, Russian Federation'), MessageBox.TYPE_INFO, timeout=10)
                            else:
                                self.session.open(MessageBox, _('Cannot connect (or server is down) !'), MessageBox.TYPE_INFO, timeout=5)
                            return
                        elif returnValue =="com_114":
                            if connected_to_internet():
                               os.system('/etc/init.d/openvpn stop > /dev/null 2>&1')
                               os.system('rm -r %s > /dev/null 2>&1 && rm -f %s > /dev/null 2>&1' % (LINKFILE1, LINKFILE2))
                               os.system('rm -r -f /etc/openvpn; mkdir /etc/openvpn') 
                               shutil.copyfile('/etc/pointvpn/cfg_conf', '/etc/openvpn/cfg.conf')
                               shutil.copyfile('/etc/pointvpn/client_conf93', '/etc/openvpn/client.conf')
                               ip = compat_urlopen("http://ip.42.pl/raw").read()  
                               with open(LINKFILE1, "wb") as f: f.write(ip)                                   
                               f = open(LINKFILE1, 'r')
                               for line in f.readlines():
                                   IP = line.strip('\n')
                                   os.system('/etc/init.d/openvpn start > /dev/null 2>&1')
                                   time.sleep(8)
                                   ip2 = compat_urlopen("http://ip.42.pl/raw").read()  
                                   with open(LINKFILE2, "wb") as f: f.write(ip2)                                       
                                   f = open(LINKFILE2, 'r')
                                   for line in f.readlines():
                                       IP2 = line.strip('\n')
                                       if ip == ip2:
                                           self.session.open(MessageBox, _('VPN Not Working?...'), MessageBox.TYPE_INFO, timeout=5)
                                       else:
                                           self.session.open(MessageBox, _('Your Ip Address is :  ' + str(IP) + '\nYour New Ip Address is :  ' + str(IP2) + '\nYour Ip Location is :  Stockholm, Sweden'), MessageBox.TYPE_INFO, timeout=10)
                            else:
                                self.session.open(MessageBox, _('Cannot connect (or server is down) !'), MessageBox.TYPE_INFO, timeout=5)
                            return
                        elif returnValue =="com_115":
                            if connected_to_internet():
                               os.system('/etc/init.d/openvpn stop > /dev/null 2>&1')
                               os.system('rm -r %s > /dev/null 2>&1 && rm -f %s > /dev/null 2>&1' % (LINKFILE1, LINKFILE2))
                               os.system('rm -r -f /etc/openvpn; mkdir /etc/openvpn') 
                               shutil.copyfile('/etc/pointvpn/cfg_conf', '/etc/openvpn/cfg.conf')
                               shutil.copyfile('/etc/pointvpn/client_conf94', '/etc/openvpn/client.conf')
                               ip = compat_urlopen("http://ip.42.pl/raw").read()  
                               with open(LINKFILE1, "wb") as f: f.write(ip)                                   
                               f = open(LINKFILE1, 'r')
                               for line in f.readlines():
                                   IP = line.strip('\n')
                                   os.system('/etc/init.d/openvpn start > /dev/null 2>&1')
                                   time.sleep(8)
                                   ip2 = compat_urlopen("http://ip.42.pl/raw").read()  
                                   with open(LINKFILE2, "wb") as f: f.write(ip2)                                       
                                   f = open(LINKFILE2, 'r')
                                   for line in f.readlines():
                                       IP2 = line.strip('\n')
                                       if ip == ip2:
                                           self.session.open(MessageBox, _('VPN Not Working?...'), MessageBox.TYPE_INFO, timeout=5)
                                       else:
                                           self.session.open(MessageBox, _('Your Ip Address is :  ' + str(IP) + '\nYour New Ip Address is :  ' + str(IP2) + '\nYour Ip Location is :  Singapore, Singapore'), MessageBox.TYPE_INFO, timeout=10)
                            else:
                                self.session.open(MessageBox, _('Cannot connect (or server is down) !'), MessageBox.TYPE_INFO, timeout=5)
                            return
                        elif returnValue =="com_116":
                            if connected_to_internet():
                               os.system('/etc/init.d/openvpn stop > /dev/null 2>&1')
                               os.system('rm -r %s > /dev/null 2>&1 && rm -f %s > /dev/null 2>&1' % (LINKFILE1, LINKFILE2))
                               os.system('rm -r -f /etc/openvpn; mkdir /etc/openvpn') 
                               shutil.copyfile('/etc/pointvpn/cfg_conf', '/etc/openvpn/cfg.conf')
                               shutil.copyfile('/etc/pointvpn/client_conf95', '/etc/openvpn/client.conf')
                               ip = compat_urlopen("http://ip.42.pl/raw").read()  
                               with open(LINKFILE1, "wb") as f: f.write(ip)                                   
                               f = open(LINKFILE1, 'r')
                               for line in f.readlines():
                                   IP = line.strip('\n')
                                   os.system('/etc/init.d/openvpn start > /dev/null 2>&1')
                                   time.sleep(8)
                                   ip2 = compat_urlopen("http://ip.42.pl/raw").read()  
                                   with open(LINKFILE2, "wb") as f: f.write(ip2)                                       
                                   f = open(LINKFILE2, 'r')
                                   for line in f.readlines():
                                       IP2 = line.strip('\n')
                                       if ip == ip2:
                                           self.session.open(MessageBox, _('VPN Not Working?...'), MessageBox.TYPE_INFO, timeout=5)
                                       else:
                                           self.session.open(MessageBox, _('Your Ip Address is :  ' + str(IP) + '\nYour New Ip Address is :  ' + str(IP2) + '\nYour Ip Location is :  Singapore, Singapore'), MessageBox.TYPE_INFO, timeout=10)
                            else:
                                self.session.open(MessageBox, _('Cannot connect (or server is down) !'), MessageBox.TYPE_INFO, timeout=5)
                            return
                        elif returnValue =="com_117":
                            if connected_to_internet():
                               os.system('/etc/init.d/openvpn stop > /dev/null 2>&1')
                               os.system('rm -r %s > /dev/null 2>&1 && rm -f %s > /dev/null 2>&1' % (LINKFILE1, LINKFILE2))
                               os.system('rm -r -f /etc/openvpn; mkdir /etc/openvpn') 
                               shutil.copyfile('/etc/pointvpn/cfg_conf', '/etc/openvpn/cfg.conf')
                               shutil.copyfile('/etc/pointvpn/client_conf96', '/etc/openvpn/client.conf')
                               ip = compat_urlopen("http://ip.42.pl/raw").read()  
                               with open(LINKFILE1, "wb") as f: f.write(ip)                                   
                               f = open(LINKFILE1, 'r')
                               for line in f.readlines():
                                   IP = line.strip('\n')
                                   os.system('/etc/init.d/openvpn start > /dev/null 2>&1')
                                   time.sleep(8)
                                   ip2 = compat_urlopen("http://ip.42.pl/raw").read()  
                                   with open(LINKFILE2, "wb") as f: f.write(ip2)                                       
                                   f = open(LINKFILE2, 'r')
                                   for line in f.readlines():
                                       IP2 = line.strip('\n')
                                       if ip == ip2:
                                           self.session.open(MessageBox, _('VPN Not Working?...'), MessageBox.TYPE_INFO, timeout=5)
                                       else:
                                           self.session.open(MessageBox, _('Your Ip Address is :  ' + str(IP) + '\nYour New Ip Address is :  ' + str(IP2) + '\nYour Ip Location is :  Ljubljana, Slovenia'), MessageBox.TYPE_INFO, timeout=10)
                            else:
                                self.session.open(MessageBox, _('Cannot connect (or server is down) !'), MessageBox.TYPE_INFO, timeout=5)
                            return
                        elif returnValue =="com_118":
                            if connected_to_internet():
                               os.system('/etc/init.d/openvpn stop > /dev/null 2>&1')
                               os.system('rm -r %s > /dev/null 2>&1 && rm -f %s > /dev/null 2>&1' % (LINKFILE1, LINKFILE2))
                               os.system('rm -r -f /etc/openvpn; mkdir /etc/openvpn') 
                               shutil.copyfile('/etc/pointvpn/cfg_conf', '/etc/openvpn/cfg.conf')
                               shutil.copyfile('/etc/pointvpn/client_conf97', '/etc/openvpn/client.conf')
                               ip = compat_urlopen("http://ip.42.pl/raw").read()  
                               with open(LINKFILE1, "wb") as f: f.write(ip)                                   
                               f = open(LINKFILE1, 'r')
                               for line in f.readlines():
                                   IP = line.strip('\n')
                                   os.system('/etc/init.d/openvpn start > /dev/null 2>&1')
                                   time.sleep(8)
                                   ip2 = compat_urlopen("http://ip.42.pl/raw").read()  
                                   with open(LINKFILE2, "wb") as f: f.write(ip2)                                       
                                   f = open(LINKFILE2, 'r')
                                   for line in f.readlines():
                                       IP2 = line.strip('\n')
                                       if ip == ip2:
                                           self.session.open(MessageBox, _('VPN Not Working?...'), MessageBox.TYPE_INFO, timeout=5)
                                       else:
                                           self.session.open(MessageBox, _('Your Ip Address is :  ' + str(IP) + '\nYour New Ip Address is :  ' + str(IP2) + '\nYour Ip Location is :  Bangkok, Thailand'), MessageBox.TYPE_INFO, timeout=10)
                            else:
                                self.session.open(MessageBox, _('Cannot connect (or server is down) !'), MessageBox.TYPE_INFO, timeout=5)
                            return
                        elif returnValue =="com_119":
                            if connected_to_internet():
                               os.system('/etc/init.d/openvpn stop > /dev/null 2>&1')
                               os.system('rm -r %s > /dev/null 2>&1 && rm -f %s > /dev/null 2>&1' % (LINKFILE1, LINKFILE2))
                               os.system('rm -r -f /etc/openvpn; mkdir /etc/openvpn') 
                               shutil.copyfile('/etc/pointvpn/cfg_conf', '/etc/openvpn/cfg.conf')
                               shutil.copyfile('/etc/pointvpn/client_conf98', '/etc/openvpn/client.conf')
                               ip = compat_urlopen("http://ip.42.pl/raw").read()  
                               with open(LINKFILE1, "wb") as f: f.write(ip)                                   
                               f = open(LINKFILE1, 'r')
                               for line in f.readlines():
                                   IP = line.strip('\n')
                                   os.system('/etc/init.d/openvpn start > /dev/null 2>&1')
                                   time.sleep(8)
                                   ip2 = compat_urlopen("http://ip.42.pl/raw").read()  
                                   with open(LINKFILE2, "wb") as f: f.write(ip2)                                       
                                   f = open(LINKFILE2, 'r')
                                   for line in f.readlines():
                                       IP2 = line.strip('\n')
                                       if ip == ip2:
                                           self.session.open(MessageBox, _('VPN Not Working?...'), MessageBox.TYPE_INFO, timeout=5)
                                       else:
                                           self.session.open(MessageBox, _('Your Ip Address is :  ' + str(IP) + '\nYour New Ip Address is :  ' + str(IP2) + '\nYour Ip Location is :  Bursa, Turkey'), MessageBox.TYPE_INFO, timeout=10)
                            else:
                                self.session.open(MessageBox, _('Cannot connect (or server is down) !'), MessageBox.TYPE_INFO, timeout=5)
                            return
                        elif returnValue =="com_120":
                            if connected_to_internet():
                               os.system('/etc/init.d/openvpn stop > /dev/null 2>&1')
                               os.system('rm -r %s > /dev/null 2>&1 && rm -f %s > /dev/null 2>&1' % (LINKFILE1, LINKFILE2))
                               os.system('rm -r -f /etc/openvpn; mkdir /etc/openvpn') 
                               shutil.copyfile('/etc/pointvpn/cfg_conf', '/etc/openvpn/cfg.conf')
                               shutil.copyfile('/etc/pointvpn/client_conf99', '/etc/openvpn/client.conf')
                               ip = compat_urlopen("http://ip.42.pl/raw").read()  
                               with open(LINKFILE1, "wb") as f: f.write(ip)                                   
                               f = open(LINKFILE1, 'r')
                               for line in f.readlines():
                                   IP = line.strip('\n')
                                   os.system('/etc/init.d/openvpn start > /dev/null 2>&1')
                                   time.sleep(8)
                                   ip2 = compat_urlopen("http://ip.42.pl/raw").read()  
                                   with open(LINKFILE2, "wb") as f: f.write(ip2)                                       
                                   f = open(LINKFILE2, 'r')
                                   for line in f.readlines():
                                       IP2 = line.strip('\n')
                                       if ip == ip2:
                                           self.session.open(MessageBox, _('VPN Not Working?...'), MessageBox.TYPE_INFO, timeout=5)
                                       else:
                                           self.session.open(MessageBox, _('Your Ip Address is :  ' + str(IP) + '\nYour New Ip Address is :  ' + str(IP2) + '\nYour Ip Location is :  Bursa 2, Turkey'), MessageBox.TYPE_INFO, timeout=10)
                            else:
                                self.session.open(MessageBox, _('Cannot connect (or server is down) !'), MessageBox.TYPE_INFO, timeout=5)
                            return
                        elif returnValue =="com_121":
                            if connected_to_internet():
                               os.system('/etc/init.d/openvpn stop > /dev/null 2>&1')
                               os.system('rm -r %s > /dev/null 2>&1 && rm -f %s > /dev/null 2>&1' % (LINKFILE1, LINKFILE2))
                               os.system('rm -r -f /etc/openvpn; mkdir /etc/openvpn') 
                               shutil.copyfile('/etc/pointvpn/cfg_conf', '/etc/openvpn/cfg.conf')
                               shutil.copyfile('/etc/pointvpn/client_conf100', '/etc/openvpn/client.conf')
                               ip = compat_urlopen("http://ip.42.pl/raw").read()  
                               with open(LINKFILE1, "wb") as f: f.write(ip)                                   
                               f = open(LINKFILE1, 'r')
                               for line in f.readlines():
                                   IP = line.strip('\n')
                                   os.system('/etc/init.d/openvpn start > /dev/null 2>&1')
                                   time.sleep(8)
                                   ip2 = compat_urlopen("http://ip.42.pl/raw").read()  
                                   with open(LINKFILE2, "wb") as f: f.write(ip2)                                       
                                   f = open(LINKFILE2, 'r')
                                   for line in f.readlines():
                                       IP2 = line.strip('\n')
                                       if ip == ip2:
                                           self.session.open(MessageBox, _('VPN Not Working?...'), MessageBox.TYPE_INFO, timeout=5)
                                       else:
                                           self.session.open(MessageBox, _('Your Ip Address is :  ' + str(IP) + '\nYour New Ip Address is :  ' + str(IP2) + '\nYour Ip Location is :  Kiev, Ukraine'), MessageBox.TYPE_INFO, timeout=10)
                            else:
                                self.session.open(MessageBox, _('Cannot connect (or server is down) !'), MessageBox.TYPE_INFO, timeout=5)
                            return
                        elif returnValue =="com_122":
                            if connected_to_internet():
                               os.system('/etc/init.d/openvpn stop > /dev/null 2>&1')
                               os.system('rm -r %s > /dev/null 2>&1 && rm -f %s > /dev/null 2>&1' % (LINKFILE1, LINKFILE2))
                               os.system('rm -r -f /etc/openvpn; mkdir /etc/openvpn') 
                               shutil.copyfile('/etc/pointvpn/cfg_conf', '/etc/openvpn/cfg.conf')
                               shutil.copyfile('/etc/pointvpn/client_conf101', '/etc/openvpn/client.conf')
                               ip = compat_urlopen("http://ip.42.pl/raw").read()  
                               with open(LINKFILE1, "wb") as f: f.write(ip)                                   
                               f = open(LINKFILE1, 'r')
                               for line in f.readlines():
                                   IP = line.strip('\n')
                                   os.system('/etc/init.d/openvpn start > /dev/null 2>&1')
                                   time.sleep(8)
                                   ip2 = compat_urlopen("http://ip.42.pl/raw").read()  
                                   with open(LINKFILE2, "wb") as f: f.write(ip2)                                       
                                   f = open(LINKFILE2, 'r')
                                   for line in f.readlines():
                                       IP2 = line.strip('\n')
                                       if ip == ip2:
                                           self.session.open(MessageBox, _('VPN Not Working?...'), MessageBox.TYPE_INFO, timeout=5)
                                       else:
                                           self.session.open(MessageBox, _('Your Ip Address is :  ' + str(IP) + '\nYour New Ip Address is :  ' + str(IP2) + '\nYour Ip Location is :  Miami, United States'), MessageBox.TYPE_INFO, timeout=10)
                            else:
                                self.session.open(MessageBox, _('Cannot connect (or server is down) !'), MessageBox.TYPE_INFO, timeout=5)
                            return
                        elif returnValue =="com_123":
                            if connected_to_internet():
                               os.system('/etc/init.d/openvpn stop > /dev/null 2>&1')
                               os.system('rm -r %s > /dev/null 2>&1 && rm -f %s > /dev/null 2>&1' % (LINKFILE1, LINKFILE2))
                               os.system('rm -r -f /etc/openvpn; mkdir /etc/openvpn') 
                               shutil.copyfile('/etc/pointvpn/cfg_conf', '/etc/openvpn/cfg.conf')
                               shutil.copyfile('/etc/pointvpn/client_conf102', '/etc/openvpn/client.conf')
                               ip = compat_urlopen("http://ip.42.pl/raw").read()  
                               with open(LINKFILE1, "wb") as f: f.write(ip)                                   
                               f = open(LINKFILE1, 'r')
                               for line in f.readlines():
                                   IP = line.strip('\n')
                                   os.system('/etc/init.d/openvpn start > /dev/null 2>&1')
                                   time.sleep(8)
                                   ip2 = compat_urlopen("http://ip.42.pl/raw").read()  
                                   with open(LINKFILE2, "wb") as f: f.write(ip2)                                       
                                   f = open(LINKFILE2, 'r')
                                   for line in f.readlines():
                                       IP2 = line.strip('\n')
                                       if ip == ip2:
                                           self.session.open(MessageBox, _('VPN Not Working?...'), MessageBox.TYPE_INFO, timeout=5)
                                       else:
                                           self.session.open(MessageBox, _('Your Ip Address is :  ' + str(IP) + '\nYour New Ip Address is :  ' + str(IP2) + '\nYour Ip Location is :  Los Angeles, United States'), MessageBox.TYPE_INFO, timeout=10)
                            else:
                                self.session.open(MessageBox, _('Cannot connect (or server is down) !'), MessageBox.TYPE_INFO, timeout=5)
                            return
                        elif returnValue =="com_124":
                            if connected_to_internet():
                               os.system('/etc/init.d/openvpn stop > /dev/null 2>&1')
                               os.system('rm -r %s > /dev/null 2>&1 && rm -f %s > /dev/null 2>&1' % (LINKFILE1, LINKFILE2))
                               os.system('rm -r -f /etc/openvpn; mkdir /etc/openvpn') 
                               shutil.copyfile('/etc/pointvpn/cfg_conf', '/etc/openvpn/cfg.conf')
                               shutil.copyfile('/etc/pointvpn/client_conf103', '/etc/openvpn/client.conf')
                               ip = compat_urlopen("http://ip.42.pl/raw").read()  
                               with open(LINKFILE1, "wb") as f: f.write(ip)                                   
                               f = open(LINKFILE1, 'r')
                               for line in f.readlines():
                                   IP = line.strip('\n')
                                   os.system('/etc/init.d/openvpn start > /dev/null 2>&1')
                                   time.sleep(8)
                                   ip2 = compat_urlopen("http://ip.42.pl/raw").read()  
                                   with open(LINKFILE2, "wb") as f: f.write(ip2)                                       
                                   f = open(LINKFILE2, 'r')
                                   for line in f.readlines():
                                       IP2 = line.strip('\n')
                                       if ip == ip2:
                                           self.session.open(MessageBox, _('VPN Not Working?...'), MessageBox.TYPE_INFO, timeout=5)
                                       else:
                                           self.session.open(MessageBox, _('Your Ip Address is :  ' + str(IP) + '\nYour New Ip Address is :  ' + str(IP2) + '\nYour Ip Location is :  New York City, United States'), MessageBox.TYPE_INFO, timeout=10)
                            else:
                                self.session.open(MessageBox, _('Cannot connect (or server is down) !'), MessageBox.TYPE_INFO, timeout=5)
                            return
                        elif returnValue =="com_125":
                            if connected_to_internet():
                               os.system('/etc/init.d/openvpn stop > /dev/null 2>&1')
                               os.system('rm -r %s > /dev/null 2>&1 && rm -f %s > /dev/null 2>&1' % (LINKFILE1, LINKFILE2))
                               os.system('rm -r -f /etc/openvpn; mkdir /etc/openvpn') 
                               shutil.copyfile('/etc/pointvpn/cfg_conf', '/etc/openvpn/cfg.conf')
                               shutil.copyfile('/etc/pointvpn/client_conf104', '/etc/openvpn/client.conf')
                               ip = compat_urlopen("http://ip.42.pl/raw").read()  
                               with open(LINKFILE1, "wb") as f: f.write(ip)                                   
                               f = open(LINKFILE1, 'r')
                               for line in f.readlines():
                                   IP = line.strip('\n')
                                   os.system('/etc/init.d/openvpn start > /dev/null 2>&1')
                                   time.sleep(8)
                                   ip2 = compat_urlopen("http://ip.42.pl/raw").read()  
                                   with open(LINKFILE2, "wb") as f: f.write(ip2)                                       
                                   f = open(LINKFILE2, 'r')
                                   for line in f.readlines():
                                       IP2 = line.strip('\n')
                                       if ip == ip2:
                                           self.session.open(MessageBox, _('VPN Not Working?...'), MessageBox.TYPE_INFO, timeout=5)
                                       else:
                                           self.session.open(MessageBox, _('Your Ip Address is :  ' + str(IP) + '\nYour New Ip Address is :  ' + str(IP2) + '\nYour Ip Location is :  Miami 2, United States'), MessageBox.TYPE_INFO, timeout=10)
                            else:
                                self.session.open(MessageBox, _('Cannot connect (or server is down) !'), MessageBox.TYPE_INFO, timeout=5)
                            return
                        elif returnValue =="com_126":
                            if connected_to_internet():
                               os.system('/etc/init.d/openvpn stop > /dev/null 2>&1')
                               os.system('rm -r %s > /dev/null 2>&1 && rm -f %s > /dev/null 2>&1' % (LINKFILE1, LINKFILE2))
                               os.system('rm -r -f /etc/openvpn; mkdir /etc/openvpn') 
                               shutil.copyfile('/etc/pointvpn/cfg_conf', '/etc/openvpn/cfg.conf')
                               shutil.copyfile('/etc/pointvpn/client_conf105', '/etc/openvpn/client.conf')
                               ip = compat_urlopen("http://ip.42.pl/raw").read()  
                               with open(LINKFILE1, "wb") as f: f.write(ip)                                   
                               f = open(LINKFILE1, 'r')
                               for line in f.readlines():
                                   IP = line.strip('\n')
                                   os.system('/etc/init.d/openvpn start > /dev/null 2>&1')
                                   time.sleep(8)
                                   ip2 = compat_urlopen("http://ip.42.pl/raw").read()  
                                   with open(LINKFILE2, "wb") as f: f.write(ip2)                                       
                                   f = open(LINKFILE2, 'r')
                                   for line in f.readlines():
                                       IP2 = line.strip('\n')
                                       if ip == ip2:
                                           self.session.open(MessageBox, _('VPN Not Working?...'), MessageBox.TYPE_INFO, timeout=5)
                                       else:
                                           self.session.open(MessageBox, _('Your Ip Address is :  ' + str(IP) + '\nYour New Ip Address is :  ' + str(IP2) + '\nYour Ip Location is :  Miami 3, United States'), MessageBox.TYPE_INFO, timeout=10)
                            else:
                                self.session.open(MessageBox, _('Cannot connect (or server is down) !'), MessageBox.TYPE_INFO, timeout=5)
                            return
                        elif returnValue =="com_127":
                            if connected_to_internet():
                               os.system('/etc/init.d/openvpn stop > /dev/null 2>&1')
                               os.system('rm -r %s > /dev/null 2>&1 && rm -f %s > /dev/null 2>&1' % (LINKFILE1, LINKFILE2))
                               os.system('rm -r -f /etc/openvpn; mkdir /etc/openvpn') 
                               shutil.copyfile('/etc/pointvpn/cfg_conf', '/etc/openvpn/cfg.conf')
                               shutil.copyfile('/etc/pointvpn/client_conf106', '/etc/openvpn/client.conf')
                               ip = compat_urlopen("http://ip.42.pl/raw").read()  
                               with open(LINKFILE1, "wb") as f: f.write(ip)                                   
                               f = open(LINKFILE1, 'r')
                               for line in f.readlines():
                                   IP = line.strip('\n')
                                   os.system('/etc/init.d/openvpn start > /dev/null 2>&1')
                                   time.sleep(8)
                                   ip2 = compat_urlopen("http://ip.42.pl/raw").read()  
                                   with open(LINKFILE2, "wb") as f: f.write(ip2)                                       
                                   f = open(LINKFILE2, 'r')
                                   for line in f.readlines():
                                       IP2 = line.strip('\n')
                                       if ip == ip2:
                                           self.session.open(MessageBox, _('VPN Not Working?...'), MessageBox.TYPE_INFO, timeout=5)
                                       else:
                                           self.session.open(MessageBox, _('Your Ip Address is :  ' + str(IP) + '\nYour New Ip Address is :  ' + str(IP2) + '\nYour Ip Location is :  New York City 2, United States'), MessageBox.TYPE_INFO, timeout=10)
                            else:
                                self.session.open(MessageBox, _('Cannot connect (or server is down) !'), MessageBox.TYPE_INFO, timeout=5)
                            return
                        elif returnValue =="com_128":
                            if connected_to_internet():
                               os.system('/etc/init.d/openvpn stop > /dev/null 2>&1')
                               os.system('rm -r %s > /dev/null 2>&1 && rm -f %s > /dev/null 2>&1' % (LINKFILE1, LINKFILE2))
                               os.system('rm -r -f /etc/openvpn; mkdir /etc/openvpn') 
                               shutil.copyfile('/etc/pointvpn/cfg_conf', '/etc/openvpn/cfg.conf')
                               shutil.copyfile('/etc/pointvpn/client_conf107', '/etc/openvpn/client.conf')
                               ip = compat_urlopen("http://ip.42.pl/raw").read()  
                               with open(LINKFILE1, "wb") as f: f.write(ip)                                   
                               f = open(LINKFILE1, 'r')
                               for line in f.readlines():
                                   IP = line.strip('\n')
                                   os.system('/etc/init.d/openvpn start > /dev/null 2>&1')
                                   time.sleep(8)
                                   ip2 = compat_urlopen("http://ip.42.pl/raw").read()  
                                   with open(LINKFILE2, "wb") as f: f.write(ip2)                                       
                                   f = open(LINKFILE2, 'r')
                                   for line in f.readlines():
                                       IP2 = line.strip('\n')
                                       if ip == ip2:
                                           self.session.open(MessageBox, _('VPN Not Working?...'), MessageBox.TYPE_INFO, timeout=5)
                                       else:
                                           self.session.open(MessageBox, _('Your Ip Address is :  ' + str(IP) + '\nYour New Ip Address is :  ' + str(IP2) + '\nYour Ip Location is :  Johannesburg 2, South Africa'), MessageBox.TYPE_INFO, timeout=10)
                            else:
                                self.session.open(MessageBox, _('Cannot connect (or server is down) !'), MessageBox.TYPE_INFO, timeout=5)
                            return
                        elif returnValue =="com_129":
                            if connected_to_internet():
                               os.system('/etc/init.d/openvpn stop > /dev/null 2>&1')
                               os.system('rm -r %s > /dev/null 2>&1 && rm -f %s > /dev/null 2>&1' % (LINKFILE1, LINKFILE2))
                               os.system('rm -r -f /etc/openvpn; mkdir /etc/openvpn') 
                               shutil.copyfile('/etc/pointvpn/cfg_conf', '/etc/openvpn/cfg.conf')
                               shutil.copyfile('/etc/pointvpn/client_conf108', '/etc/openvpn/client.conf')
                               ip = compat_urlopen("http://ip.42.pl/raw").read()  
                               with open(LINKFILE1, "wb") as f: f.write(ip)                                   
                               f = open(LINKFILE1, 'r')
                               for line in f.readlines():
                                   IP = line.strip('\n')
                                   os.system('/etc/init.d/openvpn start > /dev/null 2>&1')
                                   time.sleep(8)
                                   ip2 = compat_urlopen("http://ip.42.pl/raw").read()  
                                   with open(LINKFILE2, "wb") as f: f.write(ip2)                                       
                                   f = open(LINKFILE2, 'r')
                                   for line in f.readlines():
                                       IP2 = line.strip('\n')
                                       if ip == ip2:
                                           self.session.open(MessageBox, _('VPN Not Working?...'), MessageBox.TYPE_INFO, timeout=5)
                                       else:
                                           self.session.open(MessageBox, _('Your Ip Address is :  ' + str(IP) + '\nYour New Ip Address is :  ' + str(IP2) + '\nYour Ip Location is :  Johannesburg, South Africa'), MessageBox.TYPE_INFO, timeout=10)
                            else:
                                self.session.open(MessageBox, _('Cannot connect (or server is down) !'), MessageBox.TYPE_INFO, timeout=5)
                            return
                        if returnValue =="com_03":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia801406.us.archive.org/25/items/iptvworld-24/IPTVWORLDVPN4.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='Free VPN', cmdlist=cmdlist, finishedCallback=None)
                        elif returnValue =="com_130":
                            if connected_to_internet():
                               os.system('/etc/init.d/openvpn stop > /dev/null 2>&1')
                               os.system('rm -r %s > /dev/null 2>&1 && rm -f %s > /dev/null 2>&1' % (LINKFILE1, LINKFILE2))
                               os.system('rm -r -f /etc/openvpn; mkdir /etc/openvpn') 
                               shutil.copyfile('/etc/cfg_conf', '/etc/openvpn/cfg.conf')
                               shutil.copyfile('/etc/client_conf1', '/etc/openvpn/client.conf')
                               ip = compat_urlopen("http://ip.42.pl/raw").read()  
                               with open(LINKFILE1, "wb") as f: f.write(ip)                                   
                               f = open(LINKFILE1, 'r')
                               for line in f.readlines():
                                   IP = line.strip('\n')
                                   os.system('/etc/init.d/openvpn start > /dev/null 2>&1')
                                   time.sleep(8)
                                   ip2 = compat_urlopen("http://ip.42.pl/raw").read()  
                                   with open(LINKFILE2, "wb") as f: f.write(ip2)                                       
                                   f = open(LINKFILE2, 'r')
                                   for line in f.readlines():
                                       IP2 = line.strip('\n')
                                       if ip == ip2:
                                           self.session.open(MessageBox, _('VPN Not Working?...'), MessageBox.TYPE_INFO, timeout=5)
                                       else:
                                           self.session.open(MessageBox, _('Your Ip Address is :  ' + str(IP) + '\nYour New Ip Address is :  ' + str(IP2) + '\nYour Ip Location is :  Ashburn'), MessageBox.TYPE_INFO, timeout=10)
                            else:
                                self.session.open(MessageBox, _('Cannot connect (or server is down) !'), MessageBox.TYPE_INFO, timeout=5)
                            return
                        elif returnValue =="com_131":
                            if connected_to_internet():
                               os.system('/etc/init.d/openvpn stop > /dev/null 2>&1')
                               os.system('rm -r %s > /dev/null 2>&1 && rm -f %s > /dev/null 2>&1' % (LINKFILE1, LINKFILE2))
                               os.system('rm -r -f /etc/openvpn; mkdir /etc/openvpn') 
                               shutil.copyfile('/etc/cfg_conf', '/etc/openvpn/cfg.conf')
                               shutil.copyfile('/etc/client_conf2', '/etc/openvpn/client.conf')
                               ip = compat_urlopen("http://ip.42.pl/raw").read()  
                               with open(LINKFILE1, "wb") as f: f.write(ip)                                   
                               f = open(LINKFILE1, 'r')
                               for line in f.readlines():
                                   IP = line.strip('\n')
                                   os.system('/etc/init.d/openvpn start > /dev/null 2>&1')
                                   time.sleep(8)
                                   ip2 = compat_urlopen("http://ip.42.pl/raw").read()  
                                   with open(LINKFILE2, "wb") as f: f.write(ip2)                                       
                                   f = open(LINKFILE2, 'r')
                                   for line in f.readlines():
                                       IP2 = line.strip('\n')
                                       if ip == ip2:
                                           self.session.open(MessageBox, _('VPN Not Working?...'), MessageBox.TYPE_INFO, timeout=5)
                                       else:
                                           self.session.open(MessageBox, _('Your Ip Address is :  ' + str(IP) + '\nYour New Ip Address is :  ' + str(IP2) + '\nYour Ip Location is :  Bangalore'), MessageBox.TYPE_INFO, timeout=10)
                            else:
                                self.session.open(MessageBox, _('Cannot connect (or server is down) !'), MessageBox.TYPE_INFO, timeout=5)
                            return
                        elif returnValue =="com_132":
                            if connected_to_internet():
                               os.system('/etc/init.d/openvpn stop > /dev/null 2>&1')
                               os.system('rm -r %s > /dev/null 2>&1 && rm -f %s > /dev/null 2>&1' % (LINKFILE1, LINKFILE2))
                               os.system('rm -r -f /etc/openvpn; mkdir /etc/openvpn') 
                               shutil.copyfile('/etc/cfg_conf', '/etc/openvpn/cfg.conf')
                               shutil.copyfile('/etc/client_conf3', '/etc/openvpn/client.conf')
                               ip = compat_urlopen("http://ip.42.pl/raw").read()  
                               with open(LINKFILE1, "wb") as f: f.write(ip)                                   
                               f = open(LINKFILE1, 'r')
                               for line in f.readlines():
                                   IP = line.strip('\n')
                                   os.system('/etc/init.d/openvpn start > /dev/null 2>&1')
                                   time.sleep(8)
                                   ip2 = compat_urlopen("http://ip.42.pl/raw").read()  
                                   with open(LINKFILE2, "wb") as f: f.write(ip2)                                       
                                   f = open(LINKFILE2, 'r')
                                   for line in f.readlines():
                                       IP2 = line.strip('\n')
                                       if ip == ip2:
                                           self.session.open(MessageBox, _('VPN Not Working?...'), MessageBox.TYPE_INFO, timeout=5)
                                       else:
                                           self.session.open(MessageBox, _('Your Ip Address is :  ' + str(IP) + '\nYour New Ip Address is :  ' + str(IP2) + '\nYour Ip Location is :  Frankfurt'), MessageBox.TYPE_INFO, timeout=10)
                            else:
                                self.session.open(MessageBox, _('Cannot connect (or server is down) !'), MessageBox.TYPE_INFO, timeout=5)
                            return
                        elif returnValue =="com_133":
                            if connected_to_internet():
                               os.system('/etc/init.d/openvpn stop > /dev/null 2>&1')
                               os.system('rm -r %s > /dev/null 2>&1 && rm -f %s > /dev/null 2>&1' % (LINKFILE1, LINKFILE2))
                               os.system('rm -r -f /etc/openvpn; mkdir /etc/openvpn') 
                               shutil.copyfile('/etc/cfg_conf', '/etc/openvpn/cfg.conf')
                               shutil.copyfile('/etc/client_conf4', '/etc/openvpn/client.conf')
                               ip = compat_urlopen("http://ip.42.pl/raw").read()  
                               with open(LINKFILE1, "wb") as f: f.write(ip)                                   
                               f = open(LINKFILE1, 'r')
                               for line in f.readlines():
                                   IP = line.strip('\n')
                                   os.system('/etc/init.d/openvpn start > /dev/null 2>&1')
                                   time.sleep(8)
                                   ip2 = compat_urlopen("http://ip.42.pl/raw").read()  
                                   with open(LINKFILE2, "wb") as f: f.write(ip2)                                       
                                   f = open(LINKFILE2, 'r')
                                   for line in f.readlines():
                                       IP2 = line.strip('\n')
                                       if ip == ip2:
                                           self.session.open(MessageBox, _('VPN Not Working?...'), MessageBox.TYPE_INFO, timeout=5)
                                       else:
                                           self.session.open(MessageBox, _('Your Ip Address is :  ' + str(IP) + '\nYour New Ip Address is :  ' + str(IP2) + '\nYour Ip Location is :  London'), MessageBox.TYPE_INFO, timeout=10)
                            else:
                                self.session.open(MessageBox, _('Cannot connect (or server is down) !'), MessageBox.TYPE_INFO, timeout=5)
                            return
                        elif returnValue =="com_134":
                            if connected_to_internet():
                               os.system('/etc/init.d/openvpn stop > /dev/null 2>&1')
                               os.system('rm -r %s > /dev/null 2>&1 && rm -f %s > /dev/null 2>&1' % (LINKFILE1, LINKFILE2))
                               os.system('rm -r -f /etc/openvpn; mkdir /etc/openvpn') 
                               shutil.copyfile('/etc/cfg_conf', '/etc/openvpn/cfg.conf')
                               shutil.copyfile('/etc/client_conf5', '/etc/openvpn/client.conf')
                               ip = compat_urlopen("http://ip.42.pl/raw").read()  
                               with open(LINKFILE1, "wb") as f: f.write(ip)                                   
                               f = open(LINKFILE1, 'r')
                               for line in f.readlines():
                                   IP = line.strip('\n')
                                   os.system('/etc/init.d/openvpn start > /dev/null 2>&1')
                                   time.sleep(8)
                                   ip2 = compat_urlopen("http://ip.42.pl/raw").read()  
                                   with open(LINKFILE2, "wb") as f: f.write(ip2)                                       
                                   f = open(LINKFILE2, 'r')
                                   for line in f.readlines():
                                       IP2 = line.strip('\n')
                                       if ip == ip2:
                                           self.session.open(MessageBox, _('VPN Not Working?...'), MessageBox.TYPE_INFO, timeout=5)
                                       else:
                                           self.session.open(MessageBox, _('Your Ip Address is :  ' + str(IP) + '\nYour New Ip Address is :  ' + str(IP2) + '\nYour Ip Location is :  New York City, United States'), MessageBox.TYPE_INFO, timeout=10)
                            else:
                                self.session.open(MessageBox, _('Cannot connect (or server is down) !'), MessageBox.TYPE_INFO, timeout=5)
                            return
                        elif returnValue =="com_135":
                            if connected_to_internet():
                               os.system('/etc/init.d/openvpn stop > /dev/null 2>&1')
                               os.system('rm -r %s > /dev/null 2>&1 && rm -f %s > /dev/null 2>&1' % (LINKFILE1, LINKFILE2))
                               os.system('rm -r -f /etc/openvpn; mkdir /etc/openvpn') 
                               shutil.copyfile('/etc/cfg_conf', '/etc/openvpn/cfg.conf')
                               shutil.copyfile('/etc/client_conf6', '/etc/openvpn/client.conf')
                               ip = compat_urlopen("http://ip.42.pl/raw").read()  
                               with open(LINKFILE1, "wb") as f: f.write(ip)                                   
                               f = open(LINKFILE1, 'r')
                               for line in f.readlines():
                                   IP = line.strip('\n')
                                   os.system('/etc/init.d/openvpn start > /dev/null 2>&1')
                                   time.sleep(8)
                                   ip2 = compat_urlopen("http://ip.42.pl/raw").read()  
                                   with open(LINKFILE2, "wb") as f: f.write(ip2)                                       
                                   f = open(LINKFILE2, 'r')
                                   for line in f.readlines():
                                       IP2 = line.strip('\n')
                                       if ip == ip2:
                                           self.session.open(MessageBox, _('VPN Not Working?...'), MessageBox.TYPE_INFO, timeout=5)
                                       else:
                                           self.session.open(MessageBox, _('Your Ip Address is :  ' + str(IP) + '\nYour New Ip Address is :  ' + str(IP2) + '\nYour Ip Location is :  Singapore'), MessageBox.TYPE_INFO, timeout=10)
                            else:
                                self.session.open(MessageBox, _('Cannot connect (or server is down) !'), MessageBox.TYPE_INFO, timeout=5)
                            return
                        elif returnValue =="com_136":
                            if connected_to_internet():
                               os.system('/etc/init.d/openvpn stop > /dev/null 2>&1')
                               os.system('rm -r %s > /dev/null 2>&1 && rm -f %s > /dev/null 2>&1' % (LINKFILE1, LINKFILE2))
                               os.system('rm -r -f /etc/openvpn; mkdir /etc/openvpn') 
                               shutil.copyfile('/etc/cfg_conf', '/etc/openvpn/cfg.conf')
                               shutil.copyfile('/etc/client_conf7', '/etc/openvpn/client.conf')
                               ip = compat_urlopen("http://ip.42.pl/raw").read()  
                               with open(LINKFILE1, "wb") as f: f.write(ip)                                   
                               f = open(LINKFILE1, 'r')
                               for line in f.readlines():
                                   IP = line.strip('\n')
                                   os.system('/etc/init.d/openvpn start > /dev/null 2>&1')
                                   time.sleep(8)
                                   ip2 = compat_urlopen("http://ip.42.pl/raw").read()  
                                   with open(LINKFILE2, "wb") as f: f.write(ip2)                                       
                                   f = open(LINKFILE2, 'r')
                                   for line in f.readlines():
                                       IP2 = line.strip('\n')
                                       if ip == ip2:
                                           self.session.open(MessageBox, _('VPN Not Working?...'), MessageBox.TYPE_INFO, timeout=5)
                                       else:
                                           self.session.open(MessageBox, _('Your Ip Address is :  ' + str(IP) + '\nYour New Ip Address is :  ' + str(IP2) + '\nYour Ip Location is :  Singapore2'), MessageBox.TYPE_INFO, timeout=10)
                            else:
                                self.session.open(MessageBox, _('Cannot connect (or server is down) !'), MessageBox.TYPE_INFO, timeout=5)
                            return
                        elif returnValue =="com_137":
                            if connected_to_internet():
                               os.system('/etc/init.d/openvpn stop > /dev/null 2>&1')
                               os.system('rm -r %s > /dev/null 2>&1 && rm -f %s > /dev/null 2>&1' % (LINKFILE1, LINKFILE2))
                               os.system('rm -r -f /etc/openvpn; mkdir /etc/openvpn') 
                               shutil.copyfile('/etc/cfg_conf', '/etc/openvpn/cfg.conf')
                               shutil.copyfile('/etc/client_conf8', '/etc/openvpn/client.conf')
                               ip = compat_urlopen("http://ip.42.pl/raw").read()  
                               with open(LINKFILE1, "wb") as f: f.write(ip)                                   
                               f = open(LINKFILE1, 'r')
                               for line in f.readlines():
                                   IP = line.strip('\n')
                                   os.system('/etc/init.d/openvpn start > /dev/null 2>&1')
                                   time.sleep(8)
                                   ip2 = compat_urlopen("http://ip.42.pl/raw").read()  
                                   with open(LINKFILE2, "wb") as f: f.write(ip2)                                       
                                   f = open(LINKFILE2, 'r')
                                   for line in f.readlines():
                                       IP2 = line.strip('\n')
                                       if ip == ip2:
                                           self.session.open(MessageBox, _('VPN Not Working?...'), MessageBox.TYPE_INFO, timeout=5)
                                       else:
                                           self.session.open(MessageBox, _('Your Ip Address is :  ' + str(IP) + '\nYour New Ip Address is :  ' + str(IP2) + '\nYour Ip Location is :  Toronto'), MessageBox.TYPE_INFO, timeout=10)
                            else:
                                self.session.open(MessageBox, _('Cannot connect (or server is down) !'), MessageBox.TYPE_INFO, timeout=5)
                            return
                        if returnValue =="com_04":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia801406.us.archive.org/25/items/iptvworld-24/IPTVWORLDVPN6.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='Free VPN', cmdlist=cmdlist, finishedCallback=None)
                        elif returnValue =="com_138":
                            if connected_to_internet():
                               os.system('/etc/init.d/openvpn stop > /dev/null 2>&1')
                               os.system('rm -r %s > /dev/null 2>&1 && rm -f %s > /dev/null 2>&1' % (LINKFILE1, LINKFILE2))
                               os.system('rm -r -f /etc/openvpn; mkdir /etc/openvpn') 
                               shutil.copyfile('/etc/cfg_conf', '/etc/openvpn/cfg.conf')
                               shutil.copyfile('/etc/dollarovpn/client_conf1', '/etc/openvpn/client.conf')
                               ip = compat_urlopen("http://ip.42.pl/raw").read()  
                               with open(LINKFILE1, "wb") as f: f.write(ip)                                   
                               f = open(LINKFILE1, 'r')
                               for line in f.readlines():
                                   IP = line.strip('\n')
                                   os.system('/etc/init.d/openvpn start > /dev/null 2>&1')
                                   time.sleep(8)
                                   ip2 = compat_urlopen("http://ip.42.pl/raw").read()  
                                   with open(LINKFILE2, "wb") as f: f.write(ip2)                                       
                                   f = open(LINKFILE2, 'r')
                                   for line in f.readlines():
                                       IP2 = line.strip('\n')
                                       if ip == ip2:
                                           self.session.open(MessageBox, _('VPN Not Working?...'), MessageBox.TYPE_INFO, timeout=5)
                                       else:
                                           self.session.open(MessageBox, _('Your Ip Address is :  ' + str(IP) + '\nYour New Ip Address is :  ' + str(IP2) + '\nYour Ip Location is :  USA Vint Hill VA (2Gbit)'), MessageBox.TYPE_INFO, timeout=10)
                            else:
                                self.session.open(MessageBox, _('Cannot connect (or server is down) !'), MessageBox.TYPE_INFO, timeout=5)
                            return
                        elif returnValue =="com_139":
                            if connected_to_internet():
                               os.system('/etc/init.d/openvpn stop > /dev/null 2>&1')
                               os.system('rm -r %s > /dev/null 2>&1 && rm -f %s > /dev/null 2>&1' % (LINKFILE1, LINKFILE2))
                               os.system('rm -r -f /etc/openvpn; mkdir /etc/openvpn') 
                               shutil.copyfile('/etc/cfg_conf', '/etc/openvpn/cfg.conf')
                               shutil.copyfile('/etc/dollarovpn/client_conf2', '/etc/openvpn/client.conf')
                               ip = compat_urlopen("http://ip.42.pl/raw").read()  
                               with open(LINKFILE1, "wb") as f: f.write(ip)                                   
                               f = open(LINKFILE1, 'r')
                               for line in f.readlines():
                                   IP = line.strip('\n')
                                   os.system('/etc/init.d/openvpn start > /dev/null 2>&1')
                                   time.sleep(8)
                                   ip2 = compat_urlopen("http://ip.42.pl/raw").read()  
                                   with open(LINKFILE2, "wb") as f: f.write(ip2)                                       
                                   f = open(LINKFILE2, 'r')
                                   for line in f.readlines():
                                       IP2 = line.strip('\n')
                                       if ip == ip2:
                                           self.session.open(MessageBox, _('VPN Not Working?...'), MessageBox.TYPE_INFO, timeout=5)
                                       else:
                                           self.session.open(MessageBox, _('Your Ip Address is :  ' + str(IP) + '\nYour New Ip Address is :  ' + str(IP2) + '\nYour Ip Location is :  USA Hillsboro OR (2Gbit)'), MessageBox.TYPE_INFO, timeout=10)
                            else:
                                self.session.open(MessageBox, _('Cannot connect (or server is down) !'), MessageBox.TYPE_INFO, timeout=5)
                            return
                        elif returnValue =="com_140":
                            if connected_to_internet():
                               os.system('/etc/init.d/openvpn stop > /dev/null 2>&1')
                               os.system('rm -r %s > /dev/null 2>&1 && rm -f %s > /dev/null 2>&1' % (LINKFILE1, LINKFILE2))
                               os.system('rm -r -f /etc/openvpn; mkdir /etc/openvpn') 
                               shutil.copyfile('/etc/cfg_conf', '/etc/openvpn/cfg.conf')
                               shutil.copyfile('/etc/dollarovpn/client_conf3', '/etc/openvpn/client.conf')
                               ip = compat_urlopen("http://ip.42.pl/raw").read()  
                               with open(LINKFILE1, "wb") as f: f.write(ip)                                   
                               f = open(LINKFILE1, 'r')
                               for line in f.readlines():
                                   IP = line.strip('\n')
                                   os.system('/etc/init.d/openvpn start > /dev/null 2>&1')
                                   time.sleep(8)
                                   ip2 = compat_urlopen("http://ip.42.pl/raw").read()  
                                   with open(LINKFILE2, "wb") as f: f.write(ip2)                                       
                                   f = open(LINKFILE2, 'r')
                                   for line in f.readlines():
                                       IP2 = line.strip('\n')
                                       if ip == ip2:
                                           self.session.open(MessageBox, _('VPN Not Working?...'), MessageBox.TYPE_INFO, timeout=5)
                                       else:
                                           self.session.open(MessageBox, _('Your Ip Address is :  ' + str(IP) + '\nYour New Ip Address is :  ' + str(IP2) + '\nYour Ip Location is :  CAN Vancouver BC (1Gbit)'), MessageBox.TYPE_INFO, timeout=10)
                            else:
                                self.session.open(MessageBox, _('Cannot connect (or server is down) !'), MessageBox.TYPE_INFO, timeout=5)
                            return
                        elif returnValue =="com_141":
                            if connected_to_internet():
                               os.system('/etc/init.d/openvpn stop > /dev/null 2>&1')
                               os.system('rm -r %s > /dev/null 2>&1 && rm -f %s > /dev/null 2>&1' % (LINKFILE1, LINKFILE2))
                               os.system('rm -r -f /etc/openvpn; mkdir /etc/openvpn') 
                               shutil.copyfile('/etc/cfg_conf', '/etc/openvpn/cfg.conf')
                               shutil.copyfile('/etc/dollarovpn/client_conf4', '/etc/openvpn/client.conf')
                               ip = compat_urlopen("http://ip.42.pl/raw").read()  
                               with open(LINKFILE1, "wb") as f: f.write(ip)                                   
                               f = open(LINKFILE1, 'r')
                               for line in f.readlines():
                                   IP = line.strip('\n')
                                   os.system('/etc/init.d/openvpn start > /dev/null 2>&1')
                                   time.sleep(8)
                                   ip2 = compat_urlopen("http://ip.42.pl/raw").read()  
                                   with open(LINKFILE2, "wb") as f: f.write(ip2)                                       
                                   f = open(LINKFILE2, 'r')
                                   for line in f.readlines():
                                       IP2 = line.strip('\n')
                                       if ip == ip2:
                                           self.session.open(MessageBox, _('VPN Not Working?...'), MessageBox.TYPE_INFO, timeout=5)
                                       else:
                                           self.session.open(MessageBox, _('Your Ip Address is :  ' + str(IP) + '\nYour New Ip Address is :  ' + str(IP2) + '\nYour Ip Location is :  Sydney AU (1Gbit)'), MessageBox.TYPE_INFO, timeout=10)
                            else:
                                self.session.open(MessageBox, _('Cannot connect (or server is down) !'), MessageBox.TYPE_INFO, timeout=5)
                            return
                        elif returnValue =="com_142":
                            if connected_to_internet():
                               os.system('/etc/init.d/openvpn stop > /dev/null 2>&1')
                               os.system('rm -r %s > /dev/null 2>&1 && rm -f %s > /dev/null 2>&1' % (LINKFILE1, LINKFILE2))
                               os.system('rm -r -f /etc/openvpn; mkdir /etc/openvpn') 
                               shutil.copyfile('/etc/cfg_conf', '/etc/openvpn/cfg.conf')
                               shutil.copyfile('/etc/dollarovpn/client_conf5', '/etc/openvpn/client.conf')
                               ip = compat_urlopen("http://ip.42.pl/raw").read()  
                               with open(LINKFILE1, "wb") as f: f.write(ip)                                   
                               f = open(LINKFILE1, 'r')
                               for line in f.readlines():
                                   IP = line.strip('\n')
                                   os.system('/etc/init.d/openvpn start > /dev/null 2>&1')
                                   time.sleep(8)
                                   ip2 = compat_urlopen("http://ip.42.pl/raw").read()  
                                   with open(LINKFILE2, "wb") as f: f.write(ip2)                                       
                                   f = open(LINKFILE2, 'r')
                                   for line in f.readlines():
                                       IP2 = line.strip('\n')
                                       if ip == ip2:
                                           self.session.open(MessageBox, _('VPN Not Working?...'), MessageBox.TYPE_INFO, timeout=5)
                                       else:
                                           self.session.open(MessageBox, _('Your Ip Address is :  ' + str(IP) + '\nYour New Ip Address is :  ' + str(IP2) + '\nYour Ip Location is :  Sofia BG (1Gbit)'), MessageBox.TYPE_INFO, timeout=10)
                            else:
                                self.session.open(MessageBox, _('Cannot connect (or server is down) !'), MessageBox.TYPE_INFO, timeout=5)
                            return
                        elif returnValue =="com_143":
                            if connected_to_internet():
                               os.system('/etc/init.d/openvpn stop > /dev/null 2>&1')
                               os.system('rm -r %s > /dev/null 2>&1 && rm -f %s > /dev/null 2>&1' % (LINKFILE1, LINKFILE2))
                               os.system('rm -r -f /etc/openvpn; mkdir /etc/openvpn') 
                               shutil.copyfile('/etc/cfg_conf', '/etc/openvpn/cfg.conf')
                               shutil.copyfile('/etc/dollarovpn/client_conf6', '/etc/openvpn/client.conf')
                               ip = compat_urlopen("http://ip.42.pl/raw").read()  
                               with open(LINKFILE1, "wb") as f: f.write(ip)                                   
                               f = open(LINKFILE1, 'r')
                               for line in f.readlines():
                                   IP = line.strip('\n')
                                   os.system('/etc/init.d/openvpn start > /dev/null 2>&1')
                                   time.sleep(8)
                                   ip2 = compat_urlopen("http://ip.42.pl/raw").read()  
                                   with open(LINKFILE2, "wb") as f: f.write(ip2)                                       
                                   f = open(LINKFILE2, 'r')
                                   for line in f.readlines():
                                       IP2 = line.strip('\n')
                                       if ip == ip2:
                                           self.session.open(MessageBox, _('VPN Not Working?...'), MessageBox.TYPE_INFO, timeout=5)
                                       else:
                                           self.session.open(MessageBox, _('Your Ip Address is :  ' + str(IP) + '\nYour New Ip Address is :  ' + str(IP2) + '\nYour Ip Location is :  Singapore SG (1Gbit)'), MessageBox.TYPE_INFO, timeout=10)
                            else:
                                self.session.open(MessageBox, _('Cannot connect (or server is down) !'), MessageBox.TYPE_INFO, timeout=5)
                            return
                        elif returnValue =="com_144":
                            if connected_to_internet():
                               os.system('/etc/init.d/openvpn stop > /dev/null 2>&1')
                               os.system('rm -r %s > /dev/null 2>&1 && rm -f %s > /dev/null 2>&1' % (LINKFILE1, LINKFILE2))
                               os.system('rm -r -f /etc/openvpn; mkdir /etc/openvpn') 
                               shutil.copyfile('/etc/cfg_conf', '/etc/openvpn/cfg.conf')
                               shutil.copyfile('/etc/dollarovpn/client_conf7', '/etc/openvpn/client.conf')
                               ip = compat_urlopen("http://ip.42.pl/raw").read()  
                               with open(LINKFILE1, "wb") as f: f.write(ip)                                   
                               f = open(LINKFILE1, 'r')
                               for line in f.readlines():
                                   IP = line.strip('\n')
                                   os.system('/etc/init.d/openvpn start > /dev/null 2>&1')
                                   time.sleep(8)
                                   ip2 = compat_urlopen("http://ip.42.pl/raw").read()  
                                   with open(LINKFILE2, "wb") as f: f.write(ip2)                                       
                                   f = open(LINKFILE2, 'r')
                                   for line in f.readlines():
                                       IP2 = line.strip('\n')
                                       if ip == ip2:
                                           self.session.open(MessageBox, _('VPN Not Working?...'), MessageBox.TYPE_INFO, timeout=5)
                                       else:
                                           self.session.open(MessageBox, _('Your Ip Address is :  ' + str(IP) + '\nYour New Ip Address is :  ' + str(IP2) + '\nYour Ip Location is :  USA Piscataway NJ (10Gbit)'), MessageBox.TYPE_INFO, timeout=10)
                            else:
                                self.session.open(MessageBox, _('Cannot connect (or server is down) !'), MessageBox.TYPE_INFO, timeout=5)
                            return
                        elif returnValue =="com_145":
                            if connected_to_internet():
                               os.system('/etc/init.d/openvpn stop > /dev/null 2>&1')
                               os.system('rm -r %s > /dev/null 2>&1 && rm -f %s > /dev/null 2>&1' % (LINKFILE1, LINKFILE2))
                               os.system('rm -r -f /etc/openvpn; mkdir /etc/openvpn') 
                               shutil.copyfile('/etc/cfg_conf', '/etc/openvpn/cfg.conf')
                               shutil.copyfile('/etc/dollarovpn/client_conf8', '/etc/openvpn/client.conf')
                               ip = compat_urlopen("http://ip.42.pl/raw").read()  
                               with open(LINKFILE1, "wb") as f: f.write(ip)                                   
                               f = open(LINKFILE1, 'r')
                               for line in f.readlines():
                                   IP = line.strip('\n')
                                   os.system('/etc/init.d/openvpn start > /dev/null 2>&1')
                                   time.sleep(8)
                                   ip2 = compat_urlopen("http://ip.42.pl/raw").read()  
                                   with open(LINKFILE2, "wb") as f: f.write(ip2)                                       
                                   f = open(LINKFILE2, 'r')
                                   for line in f.readlines():
                                       IP2 = line.strip('\n')
                                       if ip == ip2:
                                           self.session.open(MessageBox, _('VPN Not Working?...'), MessageBox.TYPE_INFO, timeout=5)
                                       else:
                                           self.session.open(MessageBox, _('Your Ip Address is :  ' + str(IP) + '\nYour New Ip Address is :  ' + str(IP2) + '\nYour Ip Location is :  USA Pheonix AZ (1Gbit)'), MessageBox.TYPE_INFO, timeout=10)
                            else:
                                self.session.open(MessageBox, _('Cannot connect (or server is down) !'), MessageBox.TYPE_INFO, timeout=5)
                            return
                        elif returnValue =="com_146":
                            if connected_to_internet():
                               os.system('/etc/init.d/openvpn stop > /dev/null 2>&1')
                               os.system('rm -r %s > /dev/null 2>&1 && rm -f %s > /dev/null 2>&1' % (LINKFILE1, LINKFILE2))
                               os.system('rm -r -f /etc/openvpn; mkdir /etc/openvpn') 
                               shutil.copyfile('/etc/cfg_conf', '/etc/openvpn/cfg.conf')
                               shutil.copyfile('/etc/dollarovpn/client_conf9', '/etc/openvpn/client.conf')
                               ip = compat_urlopen("http://ip.42.pl/raw").read()  
                               with open(LINKFILE1, "wb") as f: f.write(ip)                                   
                               f = open(LINKFILE1, 'r')
                               for line in f.readlines():
                                   IP = line.strip('\n')
                                   os.system('/etc/init.d/openvpn start > /dev/null 2>&1')
                                   time.sleep(8)
                                   ip2 = compat_urlopen("http://ip.42.pl/raw").read()  
                                   with open(LINKFILE2, "wb") as f: f.write(ip2)                                       
                                   f = open(LINKFILE2, 'r')
                                   for line in f.readlines():
                                       IP2 = line.strip('\n')
                                       if ip == ip2:
                                           self.session.open(MessageBox, _('VPN Not Working?...'), MessageBox.TYPE_INFO, timeout=5)
                                       else:
                                           self.session.open(MessageBox, _('Your Ip Address is :  ' + str(IP) + '\nYour New Ip Address is :  ' + str(IP2) + '\nYour Ip Location is :  Bucharest RO (1Gbit)'), MessageBox.TYPE_INFO, timeout=10)
                            else:
                                self.session.open(MessageBox, _('Cannot connect (or server is down) !'), MessageBox.TYPE_INFO, timeout=5)
                            return
                        elif returnValue =="com_147":
                            if connected_to_internet():
                               os.system('/etc/init.d/openvpn stop > /dev/null 2>&1')
                               os.system('rm -r %s > /dev/null 2>&1 && rm -f %s > /dev/null 2>&1' % (LINKFILE1, LINKFILE2))
                               os.system('rm -r -f /etc/openvpn; mkdir /etc/openvpn') 
                               shutil.copyfile('/etc/cfg_conf', '/etc/openvpn/cfg.conf')
                               shutil.copyfile('/etc/dollarovpn/client_conf10', '/etc/openvpn/client.conf')
                               ip = compat_urlopen("http://ip.42.pl/raw").read()  
                               with open(LINKFILE1, "wb") as f: f.write(ip)                                   
                               f = open(LINKFILE1, 'r')
                               for line in f.readlines():
                                   IP = line.strip('\n')
                                   os.system('/etc/init.d/openvpn start > /dev/null 2>&1')
                                   time.sleep(8)
                                   ip2 = compat_urlopen("http://ip.42.pl/raw").read()  
                                   with open(LINKFILE2, "wb") as f: f.write(ip2)                                       
                                   f = open(LINKFILE2, 'r')
                                   for line in f.readlines():
                                       IP2 = line.strip('\n')
                                       if ip == ip2:
                                           self.session.open(MessageBox, _('VPN Not Working?...'), MessageBox.TYPE_INFO, timeout=5)
                                       else:
                                           self.session.open(MessageBox, _('Your Ip Address is :  ' + str(IP) + '\nYour New Ip Address is :  ' + str(IP2) + '\nYour Ip Location is :  Oslo NO (1Gbit)'), MessageBox.TYPE_INFO, timeout=10)
                            else:
                                self.session.open(MessageBox, _('Cannot connect (or server is down) !'), MessageBox.TYPE_INFO, timeout=5)
                            return
                        elif returnValue =="com_148":
                            if connected_to_internet():
                               os.system('/etc/init.d/openvpn stop > /dev/null 2>&1')
                               os.system('rm -r %s > /dev/null 2>&1 && rm -f %s > /dev/null 2>&1' % (LINKFILE1, LINKFILE2))
                               os.system('rm -r -f /etc/openvpn; mkdir /etc/openvpn') 
                               shutil.copyfile('/etc/cfg_conf', '/etc/openvpn/cfg.conf')
                               shutil.copyfile('/etc/dollarovpn/client_conf11', '/etc/openvpn/client.conf')
                               ip = compat_urlopen("http://ip.42.pl/raw").read()  
                               with open(LINKFILE1, "wb") as f: f.write(ip)                                   
                               f = open(LINKFILE1, 'r')
                               for line in f.readlines():
                                   IP = line.strip('\n')
                                   os.system('/etc/init.d/openvpn start > /dev/null 2>&1')
                                   time.sleep(8)
                                   ip2 = compat_urlopen("http://ip.42.pl/raw").read()  
                                   with open(LINKFILE2, "wb") as f: f.write(ip2)                                       
                                   f = open(LINKFILE2, 'r')
                                   for line in f.readlines():
                                       IP2 = line.strip('\n')
                                       if ip == ip2:
                                           self.session.open(MessageBox, _('VPN Not Working?...'), MessageBox.TYPE_INFO, timeout=5)
                                       else:
                                           self.session.open(MessageBox, _('Your Ip Address is :  ' + str(IP) + '\nYour New Ip Address is :  ' + str(IP2) + '\nYour Ip Location is :  North Holland NL (10Gbit)'), MessageBox.TYPE_INFO, timeout=10)
                            else:
                                self.session.open(MessageBox, _('Cannot connect (or server is down) !'), MessageBox.TYPE_INFO, timeout=5)
                            return
                        elif returnValue =="com_149":
                            if connected_to_internet():
                               os.system('/etc/init.d/openvpn stop > /dev/null 2>&1')
                               os.system('rm -r %s > /dev/null 2>&1 && rm -f %s > /dev/null 2>&1' % (LINKFILE1, LINKFILE2))
                               os.system('rm -r -f /etc/openvpn; mkdir /etc/openvpn') 
                               shutil.copyfile('/etc/cfg_conf', '/etc/openvpn/cfg.conf')
                               shutil.copyfile('/etc/dollarovpn/client_conf12', '/etc/openvpn/client.conf')
                               ip = compat_urlopen("http://ip.42.pl/raw").read()  
                               with open(LINKFILE1, "wb") as f: f.write(ip)                                   
                               f = open(LINKFILE1, 'r')
                               for line in f.readlines():
                                   IP = line.strip('\n')
                                   os.system('/etc/init.d/openvpn start > /dev/null 2>&1')
                                   time.sleep(8)
                                   ip2 = compat_urlopen("http://ip.42.pl/raw").read()  
                                   with open(LINKFILE2, "wb") as f: f.write(ip2)                                       
                                   f = open(LINKFILE2, 'r')
                                   for line in f.readlines():
                                       IP2 = line.strip('\n')
                                       if ip == ip2:
                                           self.session.open(MessageBox, _('VPN Not Working?...'), MessageBox.TYPE_INFO, timeout=5)
                                       else:
                                           self.session.open(MessageBox, _('Your Ip Address is :  ' + str(IP) + '\nYour New Ip Address is :  ' + str(IP2) + '\nYour Ip Location is :  CAN Montreal QC (1Gbit)'), MessageBox.TYPE_INFO, timeout=10)
                            else:
                                self.session.open(MessageBox, _('Cannot connect (or server is down) !'), MessageBox.TYPE_INFO, timeout=5)
                            return
                        elif returnValue =="com_150":
                            if connected_to_internet():
                               os.system('/etc/init.d/openvpn stop > /dev/null 2>&1')
                               os.system('rm -r %s > /dev/null 2>&1 && rm -f %s > /dev/null 2>&1' % (LINKFILE1, LINKFILE2))
                               os.system('rm -r -f /etc/openvpn; mkdir /etc/openvpn') 
                               shutil.copyfile('/etc/cfg_conf', '/etc/openvpn/cfg.conf')
                               shutil.copyfile('/etc/dollarovpn/client_conf13', '/etc/openvpn/client.conf')
                               ip = compat_urlopen("http://ip.42.pl/raw").read()  
                               with open(LINKFILE1, "wb") as f: f.write(ip)                                   
                               f = open(LINKFILE1, 'r')
                               for line in f.readlines():
                                   IP = line.strip('\n')
                                   os.system('/etc/init.d/openvpn start > /dev/null 2>&1')
                                   time.sleep(8)
                                   ip2 = compat_urlopen("http://ip.42.pl/raw").read()  
                                   with open(LINKFILE2, "wb") as f: f.write(ip2)                                       
                                   f = open(LINKFILE2, 'r')
                                   for line in f.readlines():
                                       IP2 = line.strip('\n')
                                       if ip == ip2:
                                           self.session.open(MessageBox, _('VPN Not Working?...'), MessageBox.TYPE_INFO, timeout=5)
                                       else:
                                           self.session.open(MessageBox, _('Your Ip Address is :  ' + str(IP) + '\nYour New Ip Address is :  ' + str(IP2) + '\nYour Ip Location is :  USA Miami FL (10Gbit)'), MessageBox.TYPE_INFO, timeout=10)
                            else:
                                self.session.open(MessageBox, _('Cannot connect (or server is down) !'), MessageBox.TYPE_INFO, timeout=5)
                            return
                        elif returnValue =="com_151":
                            if connected_to_internet():
                               os.system('/etc/init.d/openvpn stop > /dev/null 2>&1')
                               os.system('rm -r %s > /dev/null 2>&1 && rm -f %s > /dev/null 2>&1' % (LINKFILE1, LINKFILE2))
                               os.system('rm -r -f /etc/openvpn; mkdir /etc/openvpn') 
                               shutil.copyfile('/etc/cfg_conf', '/etc/openvpn/cfg.conf')
                               shutil.copyfile('/etc/dollarovpn/client_conf14', '/etc/openvpn/client.conf')
                               ip = compat_urlopen("http://ip.42.pl/raw").read()  
                               with open(LINKFILE1, "wb") as f: f.write(ip)                                   
                               f = open(LINKFILE1, 'r')
                               for line in f.readlines():
                                   IP = line.strip('\n')
                                   os.system('/etc/init.d/openvpn start > /dev/null 2>&1')
                                   time.sleep(8)
                                   ip2 = compat_urlopen("http://ip.42.pl/raw").read()  
                                   with open(LINKFILE2, "wb") as f: f.write(ip2)                                       
                                   f = open(LINKFILE2, 'r')
                                   for line in f.readlines():
                                       IP2 = line.strip('\n')
                                       if ip == ip2:
                                           self.session.open(MessageBox, _('VPN Not Working?...'), MessageBox.TYPE_INFO, timeout=5)
                                       else:
                                           self.session.open(MessageBox, _('Your Ip Address is :  ' + str(IP) + '\nYour New Ip Address is :  ' + str(IP2) + '\nYour Ip Location is :  Madrid ES (1Gbit)'), MessageBox.TYPE_INFO, timeout=10)
                            else:
                                self.session.open(MessageBox, _('Cannot connect (or server is down) !'), MessageBox.TYPE_INFO, timeout=5)
                            return
                        elif returnValue =="com_152":
                            if connected_to_internet():
                               os.system('/etc/init.d/openvpn stop > /dev/null 2>&1')
                               os.system('rm -r %s > /dev/null 2>&1 && rm -f %s > /dev/null 2>&1' % (LINKFILE1, LINKFILE2))
                               os.system('rm -r -f /etc/openvpn; mkdir /etc/openvpn') 
                               shutil.copyfile('/etc/cfg_conf', '/etc/openvpn/cfg.conf')
                               shutil.copyfile('/etc/dollarovpn/client_conf15', '/etc/openvpn/client.conf')
                               ip = compat_urlopen("http://ip.42.pl/raw").read()  
                               with open(LINKFILE1, "wb") as f: f.write(ip)                                   
                               f = open(LINKFILE1, 'r')
                               for line in f.readlines():
                                   IP = line.strip('\n')
                                   os.system('/etc/init.d/openvpn start > /dev/null 2>&1')
                                   time.sleep(8)
                                   ip2 = compat_urlopen("http://ip.42.pl/raw").read()  
                                   with open(LINKFILE2, "wb") as f: f.write(ip2)                                       
                                   f = open(LINKFILE2, 'r')
                                   for line in f.readlines():
                                       IP2 = line.strip('\n')
                                       if ip == ip2:
                                           self.session.open(MessageBox, _('VPN Not Working?...'), MessageBox.TYPE_INFO, timeout=5)
                                       else:
                                           self.session.open(MessageBox, _('Your Ip Address is :  ' + str(IP) + '\nYour New Ip Address is :  ' + str(IP2) + '\nYour Ip Location is :  USA Los Angels CA (10Gbit)'), MessageBox.TYPE_INFO, timeout=10)
                            else:
                                self.session.open(MessageBox, _('Cannot connect (or server is down) !'), MessageBox.TYPE_INFO, timeout=5)
                            return
                        elif returnValue =="com_153":
                            if connected_to_internet():
                               os.system('/etc/init.d/openvpn stop > /dev/null 2>&1')
                               os.system('rm -r %s > /dev/null 2>&1 && rm -f %s > /dev/null 2>&1' % (LINKFILE1, LINKFILE2))
                               os.system('rm -r -f /etc/openvpn; mkdir /etc/openvpn') 
                               shutil.copyfile('/etc/cfg_conf', '/etc/openvpn/cfg.conf')
                               shutil.copyfile('/etc/dollarovpn/client_conf16', '/etc/openvpn/client.conf')
                               ip = compat_urlopen("http://ip.42.pl/raw").read()  
                               with open(LINKFILE1, "wb") as f: f.write(ip)                                   
                               f = open(LINKFILE1, 'r')
                               for line in f.readlines():
                                   IP = line.strip('\n')
                                   os.system('/etc/init.d/openvpn start > /dev/null 2>&1')
                                   time.sleep(8)
                                   ip2 = compat_urlopen("http://ip.42.pl/raw").read()  
                                   with open(LINKFILE2, "wb") as f: f.write(ip2)                                       
                                   f = open(LINKFILE2, 'r')
                                   for line in f.readlines():
                                       IP2 = line.strip('\n')
                                       if ip == ip2:
                                           self.session.open(MessageBox, _('VPN Not Working?...'), MessageBox.TYPE_INFO, timeout=5)
                                       else:
                                           self.session.open(MessageBox, _('Your Ip Address is :  ' + str(IP) + '\nYour New Ip Address is :  ' + str(IP2) + '\nYour Ip Location is :  USA New York NY (10Gbit)'), MessageBox.TYPE_INFO, timeout=10)
                            else:
                                self.session.open(MessageBox, _('Cannot connect (or server is down) !'), MessageBox.TYPE_INFO, timeout=5)
                            return
                        elif returnValue =="com_154":
                            if connected_to_internet():
                               os.system('/etc/init.d/openvpn stop > /dev/null 2>&1')
                               os.system('rm -r %s > /dev/null 2>&1 && rm -f %s > /dev/null 2>&1' % (LINKFILE1, LINKFILE2))
                               os.system('rm -r -f /etc/openvpn; mkdir /etc/openvpn') 
                               shutil.copyfile('/etc/cfg_conf', '/etc/openvpn/cfg.conf')
                               shutil.copyfile('/etc/dollarovpn/client_conf17', '/etc/openvpn/client.conf')
                               ip = compat_urlopen("http://ip.42.pl/raw").read()  
                               with open(LINKFILE1, "wb") as f: f.write(ip)                                   
                               f = open(LINKFILE1, 'r')
                               for line in f.readlines():
                                   IP = line.strip('\n')
                                   os.system('/etc/init.d/openvpn start > /dev/null 2>&1')
                                   time.sleep(8)
                                   ip2 = compat_urlopen("http://ip.42.pl/raw").read()  
                                   with open(LINKFILE2, "wb") as f: f.write(ip2)                                       
                                   f = open(LINKFILE2, 'r')
                                   for line in f.readlines():
                                       IP2 = line.strip('\n')
                                       if ip == ip2:
                                           self.session.open(MessageBox, _('VPN Not Working?...'), MessageBox.TYPE_INFO, timeout=5)
                                       else:
                                           self.session.open(MessageBox, _('Your Ip Address is :  ' + str(IP) + '\nYour New Ip Address is :  ' + str(IP2) + '\nYour Ip Location is :   USA Las Vegas NV (1Gbit)'), MessageBox.TYPE_INFO, timeout=10)
                            else:
                                self.session.open(MessageBox, _('Cannot connect (or server is down) !'), MessageBox.TYPE_INFO, timeout=5)
                            return
                        elif returnValue =="com_155":
                            if connected_to_internet():
                               os.system('/etc/init.d/openvpn stop > /dev/null 2>&1')
                               os.system('rm -r %s > /dev/null 2>&1 && rm -f %s > /dev/null 2>&1' % (LINKFILE1, LINKFILE2))
                               os.system('rm -r -f /etc/openvpn; mkdir /etc/openvpn') 
                               shutil.copyfile('/etc/cfg_conf', '/etc/openvpn/cfg.conf')
                               shutil.copyfile('/etc/dollarovpn/client_conf18', '/etc/openvpn/client.conf')
                               ip = compat_urlopen("http://ip.42.pl/raw").read()  
                               with open(LINKFILE1, "wb") as f: f.write(ip)                                   
                               f = open(LINKFILE1, 'r')
                               for line in f.readlines():
                                   IP = line.strip('\n')
                                   os.system('/etc/init.d/openvpn start > /dev/null 2>&1')
                                   time.sleep(8)
                                   ip2 = compat_urlopen("http://ip.42.pl/raw").read()  
                                   with open(LINKFILE2, "wb") as f: f.write(ip2)                                       
                                   f = open(LINKFILE2, 'r')
                                   for line in f.readlines():
                                       IP2 = line.strip('\n')
                                       if ip == ip2:
                                           self.session.open(MessageBox, _('VPN Not Working?...'), MessageBox.TYPE_INFO, timeout=5)
                                       else:
                                           self.session.open(MessageBox, _('Your Ip Address is :  ' + str(IP) + '\nYour New Ip Address is :  ' + str(IP2) + '\nYour Ip Location is :  USA Kansas City MO (1Gbit)'), MessageBox.TYPE_INFO, timeout=10)
                            else:
                                self.session.open(MessageBox, _('Cannot connect (or server is down) !'), MessageBox.TYPE_INFO, timeout=5)
                            return
                        elif returnValue =="com_156":
                            if connected_to_internet():
                               os.system('/etc/init.d/openvpn stop > /dev/null 2>&1')
                               os.system('rm -r %s > /dev/null 2>&1 && rm -f %s > /dev/null 2>&1' % (LINKFILE1, LINKFILE2))
                               os.system('rm -r -f /etc/openvpn; mkdir /etc/openvpn') 
                               shutil.copyfile('/etc/cfg_conf', '/etc/openvpn/cfg.conf')
                               shutil.copyfile('/etc/dollarovpn/client_conf19', '/etc/openvpn/client.conf')
                               ip = compat_urlopen("http://ip.42.pl/raw").read()  
                               with open(LINKFILE1, "wb") as f: f.write(ip)                                   
                               f = open(LINKFILE1, 'r')
                               for line in f.readlines():
                                   IP = line.strip('\n')
                                   os.system('/etc/init.d/openvpn start > /dev/null 2>&1')
                                   time.sleep(8)
                                   ip2 = compat_urlopen("http://ip.42.pl/raw").read()  
                                   with open(LINKFILE2, "wb") as f: f.write(ip2)                                       
                                   f = open(LINKFILE2, 'r')
                                   for line in f.readlines():
                                       IP2 = line.strip('\n')
                                       if ip == ip2:
                                           self.session.open(MessageBox, _('VPN Not Working?...'), MessageBox.TYPE_INFO, timeout=5)
                                       else:
                                           self.session.open(MessageBox, _('Your Ip Address is :  ' + str(IP) + '\nYour New Ip Address is :  ' + str(IP2) + '\nYour Ip Location is :  Hong Kong HK (1Gbit)'), MessageBox.TYPE_INFO, timeout=10)
                            else:
                                self.session.open(MessageBox, _('Cannot connect (or server is down) !'), MessageBox.TYPE_INFO, timeout=5)
                            return
                        elif returnValue =="com_157":
                            if connected_to_internet():
                               os.system('/etc/init.d/openvpn stop > /dev/null 2>&1')
                               os.system('rm -r %s > /dev/null 2>&1 && rm -f %s > /dev/null 2>&1' % (LINKFILE1, LINKFILE2))
                               os.system('rm -r -f /etc/openvpn; mkdir /etc/openvpn') 
                               shutil.copyfile('/etc/cfg_conf', '/etc/openvpn/cfg.conf')
                               shutil.copyfile('/etc/dollarovpn/client_conf20', '/etc/openvpn/client.conf')
                               ip = compat_urlopen("http://ip.42.pl/raw").read()  
                               with open(LINKFILE1, "wb") as f: f.write(ip)                                   
                               f = open(LINKFILE1, 'r')
                               for line in f.readlines():
                                   IP = line.strip('\n')
                                   os.system('/etc/init.d/openvpn start > /dev/null 2>&1')
                                   time.sleep(8)
                                   ip2 = compat_urlopen("http://ip.42.pl/raw").read()  
                                   with open(LINKFILE2, "wb") as f: f.write(ip2)                                       
                                   f = open(LINKFILE2, 'r')
                                   for line in f.readlines():
                                       IP2 = line.strip('\n')
                                       if ip == ip2:
                                           self.session.open(MessageBox, _('VPN Not Working?...'), MessageBox.TYPE_INFO, timeout=5)
                                       else:
                                           self.session.open(MessageBox, _('Your Ip Address is :  ' + str(IP) + '\nYour New Ip Address is :  ' + str(IP2) + '\nYour Ip Location is :  Helsinki FI (1Gbit)'), MessageBox.TYPE_INFO, timeout=10)
                            else:
                                self.session.open(MessageBox, _('Cannot connect (or server is down) !'), MessageBox.TYPE_INFO, timeout=5)
                            return
                        elif returnValue =="com_158":
                            if connected_to_internet():
                               os.system('/etc/init.d/openvpn stop > /dev/null 2>&1')
                               os.system('rm -r %s > /dev/null 2>&1 && rm -f %s > /dev/null 2>&1' % (LINKFILE1, LINKFILE2))
                               os.system('rm -r -f /etc/openvpn; mkdir /etc/openvpn') 
                               shutil.copyfile('/etc/cfg_conf', '/etc/openvpn/cfg.conf')
                               shutil.copyfile('/etc/dollarovpn/client_conf21', '/etc/openvpn/client.conf')
                               ip = compat_urlopen("http://ip.42.pl/raw").read()  
                               with open(LINKFILE1, "wb") as f: f.write(ip)                                   
                               f = open(LINKFILE1, 'r')
                               for line in f.readlines():
                                   IP = line.strip('\n')
                                   os.system('/etc/init.d/openvpn start > /dev/null 2>&1')
                                   time.sleep(8)
                                   ip2 = compat_urlopen("http://ip.42.pl/raw").read()  
                                   with open(LINKFILE2, "wb") as f: f.write(ip2)                                       
                                   f = open(LINKFILE2, 'r')
                                   for line in f.readlines():
                                       IP2 = line.strip('\n')
                                       if ip == ip2:
                                           self.session.open(MessageBox, _('VPN Not Working?...'), MessageBox.TYPE_INFO, timeout=5)
                                       else:
                                           self.session.open(MessageBox, _('Your Ip Address is :  ' + str(IP) + '\nYour New Ip Address is :  ' + str(IP2) + '\nYour Ip Location is :  Florence IT (1Gbit)'), MessageBox.TYPE_INFO, timeout=10)
                            else:
                                self.session.open(MessageBox, _('Cannot connect (or server is down) !'), MessageBox.TYPE_INFO, timeout=5)
                            return
                        elif returnValue =="com_159":
                            if connected_to_internet():
                               os.system('/etc/init.d/openvpn stop > /dev/null 2>&1')
                               os.system('rm -r %s > /dev/null 2>&1 && rm -f %s > /dev/null 2>&1' % (LINKFILE1, LINKFILE2))
                               os.system('rm -r -f /etc/openvpn; mkdir /etc/openvpn') 
                               shutil.copyfile('/etc/cfg_conf', '/etc/openvpn/cfg.conf')
                               shutil.copyfile('/etc/dollarovpn/client_conf22', '/etc/openvpn/client.conf')
                               ip = compat_urlopen("http://ip.42.pl/raw").read()  
                               with open(LINKFILE1, "wb") as f: f.write(ip)                                   
                               f = open(LINKFILE1, 'r')
                               for line in f.readlines():
                                   IP = line.strip('\n')
                                   os.system('/etc/init.d/openvpn start > /dev/null 2>&1')
                                   time.sleep(8)
                                   ip2 = compat_urlopen("http://ip.42.pl/raw").read()  
                                   with open(LINKFILE2, "wb") as f: f.write(ip2)                                       
                                   f = open(LINKFILE2, 'r')
                                   for line in f.readlines():
                                       IP2 = line.strip('\n')
                                       if ip == ip2:
                                           self.session.open(MessageBox, _('VPN Not Working?...'), MessageBox.TYPE_INFO, timeout=5)
                                       else:
                                           self.session.open(MessageBox, _('Your Ip Address is :  ' + str(IP) + '\nYour New Ip Address is :  ' + str(IP2) + '\nYour Ip Location is :  Dusseldorf DE (1Gbit)'), MessageBox.TYPE_INFO, timeout=10)
                            else:
                                self.session.open(MessageBox, _('Cannot connect (or server is down) !'), MessageBox.TYPE_INFO, timeout=5)
                            return
                        elif returnValue =="com_160":
                            if connected_to_internet():
                               os.system('/etc/init.d/openvpn stop > /dev/null 2>&1')
                               os.system('rm -r %s > /dev/null 2>&1 && rm -f %s > /dev/null 2>&1' % (LINKFILE1, LINKFILE2))
                               os.system('rm -r -f /etc/openvpn; mkdir /etc/openvpn') 
                               shutil.copyfile('/etc/cfg_conf', '/etc/openvpn/cfg.conf')
                               shutil.copyfile('/etc/dollarovpn/client_conf23', '/etc/openvpn/client.conf')
                               ip = compat_urlopen("http://ip.42.pl/raw").read()  
                               with open(LINKFILE1, "wb") as f: f.write(ip)                                   
                               f = open(LINKFILE1, 'r')
                               for line in f.readlines():
                                   IP = line.strip('\n')
                                   os.system('/etc/init.d/openvpn start > /dev/null 2>&1')
                                   time.sleep(8)
                                   ip2 = compat_urlopen("http://ip.42.pl/raw").read()  
                                   with open(LINKFILE2, "wb") as f: f.write(ip2)                                       
                                   f = open(LINKFILE2, 'r')
                                   for line in f.readlines():
                                       IP2 = line.strip('\n')
                                       if ip == ip2:
                                           self.session.open(MessageBox, _('VPN Not Working?...'), MessageBox.TYPE_INFO, timeout=5)
                                       else:
                                           self.session.open(MessageBox, _('Your Ip Address is :  ' + str(IP) + '\nYour New Ip Address is :  ' + str(IP2) + '\nYour Ip Location is :  USA Dallas TX (1Gbit)'), MessageBox.TYPE_INFO, timeout=10)
                            else:
                                self.session.open(MessageBox, _('Cannot connect (or server is down) !'), MessageBox.TYPE_INFO, timeout=5)
                            return
                        elif returnValue =="com_161":
                            if connected_to_internet():
                               os.system('/etc/init.d/openvpn stop > /dev/null 2>&1')
                               os.system('rm -r %s > /dev/null 2>&1 && rm -f %s > /dev/null 2>&1' % (LINKFILE1, LINKFILE2))
                               os.system('rm -r -f /etc/openvpn; mkdir /etc/openvpn') 
                               shutil.copyfile('/etc/cfg_conf', '/etc/openvpn/cfg.conf')
                               shutil.copyfile('/etc/dollarovpn/client_conf24', '/etc/openvpn/client.conf')
                               ip = compat_urlopen("http://ip.42.pl/raw").read()  
                               with open(LINKFILE1, "wb") as f: f.write(ip)                                   
                               f = open(LINKFILE1, 'r')
                               for line in f.readlines():
                                   IP = line.strip('\n')
                                   os.system('/etc/init.d/openvpn start > /dev/null 2>&1')
                                   time.sleep(8)
                                   ip2 = compat_urlopen("http://ip.42.pl/raw").read()  
                                   with open(LINKFILE2, "wb") as f: f.write(ip2)                                       
                                   f = open(LINKFILE2, 'r')
                                   for line in f.readlines():
                                       IP2 = line.strip('\n')
                                       if ip == ip2:
                                           self.session.open(MessageBox, _('VPN Not Working?...'), MessageBox.TYPE_INFO, timeout=5)
                                       else:
                                           self.session.open(MessageBox, _('Your Ip Address is :  ' + str(IP) + '\nYour New Ip Address is :  ' + str(IP2) + '\nYour Ip Location is :  USA Ashburn VA (1Gbit)'), MessageBox.TYPE_INFO, timeout=10)
                            else:
                                self.session.open(MessageBox, _('Cannot connect (or server is down) !'), MessageBox.TYPE_INFO, timeout=5)
                            return    
                            
                        elif returnValue =="com_162":
                            if connected_to_internet():
                               os.system('/etc/init.d/openvpn stop > /dev/null 2>&1')
                               os.system('rm -r %s > /dev/null 2>&1 && rm -f %s > /dev/null 2>&1' % (LINKFILE1, LINKFILE2))
                               os.system('rm -r -f /etc/openvpn; mkdir /etc/openvpn') 
                               shutil.copyfile('/etc/cfg_conf', '/etc/openvpn/cfg.conf')
                               shutil.copyfile('/etc/dollarovpn/client_conf25', '/etc/openvpn/client.conf')
                               ip = compat_urlopen("http://ip.42.pl/raw").read()  
                               with open(LINKFILE1, "wb") as f: f.write(ip)                                   
                               f = open(LINKFILE1, 'r')
                               for line in f.readlines():
                                   IP = line.strip('\n')
                                   os.system('/etc/init.d/openvpn start > /dev/null 2>&1')
                                   time.sleep(8)
                                   ip2 = compat_urlopen("http://ip.42.pl/raw").read()  
                                   with open(LINKFILE2, "wb") as f: f.write(ip2)                                       
                                   f = open(LINKFILE2, 'r')
                                   for line in f.readlines():
                                       IP2 = line.strip('\n')
                                       if ip == ip2:
                                           self.session.open(MessageBox, _('VPN Not Working?...'), MessageBox.TYPE_INFO, timeout=5)
                                       else:
                                           self.session.open(MessageBox, _('Your Ip Address is :  ' + str(IP) + '\nYour New Ip Address is :  ' + str(IP2) + '\nYour Ip Location is :  USA Chicago IL (10Gbit)'), MessageBox.TYPE_INFO, timeout=10)
                            else:
                                self.session.open(MessageBox, _('Cannot connect (or server is down) !'), MessageBox.TYPE_INFO, timeout=5)
                            return
                        elif returnValue =="com_163":
                            if connected_to_internet():
                               os.system('/etc/init.d/openvpn stop > /dev/null 2>&1')
                               os.system('rm -r %s > /dev/null 2>&1 && rm -f %s > /dev/null 2>&1' % (LINKFILE1, LINKFILE2))
                               os.system('rm -r -f /etc/openvpn; mkdir /etc/openvpn') 
                               shutil.copyfile('/etc/cfg_conf', '/etc/openvpn/cfg.conf')
                               shutil.copyfile('/etc/dollarovpn/client_conf26', '/etc/openvpn/client.conf')
                               ip = compat_urlopen("http://ip.42.pl/raw").read()  
                               with open(LINKFILE1, "wb") as f: f.write(ip)                                   
                               f = open(LINKFILE1, 'r')
                               for line in f.readlines():
                                   IP = line.strip('\n')
                                   os.system('/etc/init.d/openvpn start > /dev/null 2>&1')
                                   time.sleep(8)
                                   ip2 = compat_urlopen("http://ip.42.pl/raw").read()  
                                   with open(LINKFILE2, "wb") as f: f.write(ip2)                                       
                                   f = open(LINKFILE2, 'r')
                                   for line in f.readlines():
                                       IP2 = line.strip('\n')
                                       if ip == ip2:
                                           self.session.open(MessageBox, _('VPN Not Working?...'), MessageBox.TYPE_INFO, timeout=5)
                                       else:
                                           self.session.open(MessageBox, _('Your Ip Address is :  ' + str(IP) + '\nYour New Ip Address is :  ' + str(IP2) + '\nYour Ip Location is :  Brussels BE (1Gbit)'), MessageBox.TYPE_INFO, timeout=10)
                            else:
                                self.session.open(MessageBox, _('Cannot connect (or server is down) !'), MessageBox.TYPE_INFO, timeout=5)
                            return
                        elif returnValue =="com_164":
                            if connected_to_internet():
                               os.system('/etc/init.d/openvpn stop > /dev/null 2>&1')
                               os.system('rm -r %s > /dev/null 2>&1 && rm -f %s > /dev/null 2>&1' % (LINKFILE1, LINKFILE2))
                               os.system('rm -r -f /etc/openvpn; mkdir /etc/openvpn') 
                               shutil.copyfile('/etc/cfg_conf', '/etc/openvpn/cfg.conf')
                               shutil.copyfile('/etc/dollarovpn/client_conf27', '/etc/openvpn/client.conf')
                               ip = compat_urlopen("http://ip.42.pl/raw").read()  
                               with open(LINKFILE1, "wb") as f: f.write(ip)                                   
                               f = open(LINKFILE1, 'r')
                               for line in f.readlines():
                                   IP = line.strip('\n')
                                   os.system('/etc/init.d/openvpn start > /dev/null 2>&1')
                                   time.sleep(8)
                                   ip2 = compat_urlopen("http://ip.42.pl/raw").read()  
                                   with open(LINKFILE2, "wb") as f: f.write(ip2)                                       
                                   f = open(LINKFILE2, 'r')
                                   for line in f.readlines():
                                       IP2 = line.strip('\n')
                                       if ip == ip2:
                                           self.session.open(MessageBox, _('VPN Not Working?...'), MessageBox.TYPE_INFO, timeout=5)
                                       else:
                                           self.session.open(MessageBox, _('Your Ip Address is :  ' + str(IP) + '\nYour New Ip Address is :  ' + str(IP2) + '\nYour Ip Location is :  USA Atlanta GA (1Gbit)'), MessageBox.TYPE_INFO, timeout=10)
                            else:
                                self.session.open(MessageBox, _('Cannot connect (or server is down) !'), MessageBox.TYPE_INFO, timeout=5)
                            return
                        elif returnValue =="com_165":
                            if connected_to_internet():
                               os.system('/etc/init.d/openvpn stop > /dev/null 2>&1')
                               os.system('rm -r %s > /dev/null 2>&1 && rm -f %s > /dev/null 2>&1' % (LINKFILE1, LINKFILE2))
                               os.system('rm -r -f /etc/openvpn; mkdir /etc/openvpn') 
                               shutil.copyfile('/etc/cfg_conf', '/etc/openvpn/cfg.conf')
                               shutil.copyfile('/etc/dollarovpn/client_conf28', '/etc/openvpn/client.conf')
                               ip = compat_urlopen("http://ip.42.pl/raw").read()  
                               with open(LINKFILE1, "wb") as f: f.write(ip)                                   
                               f = open(LINKFILE1, 'r')
                               for line in f.readlines():
                                   IP = line.strip('\n')
                                   os.system('/etc/init.d/openvpn start > /dev/null 2>&1')
                                   time.sleep(8)
                                   ip2 = compat_urlopen("http://ip.42.pl/raw").read()  
                                   with open(LINKFILE2, "wb") as f: f.write(ip2)                                       
                                   f = open(LINKFILE2, 'r')
                                   for line in f.readlines():
                                       IP2 = line.strip('\n')
                                       if ip == ip2:
                                           self.session.open(MessageBox, _('VPN Not Working?...'), MessageBox.TYPE_INFO, timeout=5)
                                       else:
                                           self.session.open(MessageBox, _('Your Ip Address is :  ' + str(IP) + '\nYour New Ip Address is :  ' + str(IP2) + '\nYour Ip Location is :  USA Detroit MI (1Gbit)'), MessageBox.TYPE_INFO, timeout=10)
                            else:
                                self.session.open(MessageBox, _('Cannot connect (or server is down) !'), MessageBox.TYPE_INFO, timeout=5)
                            return
                        elif returnValue =="com_166":
                            if connected_to_internet():
                               os.system('/etc/init.d/openvpn stop > /dev/null 2>&1')
                               os.system('rm -r %s > /dev/null 2>&1 && rm -f %s > /dev/null 2>&1' % (LINKFILE1, LINKFILE2))
                               os.system('rm -r -f /etc/openvpn; mkdir /etc/openvpn') 
                               shutil.copyfile('/etc/cfg_conf', '/etc/openvpn/cfg.conf')
                               shutil.copyfile('/etc/dollarovpn/client_conf29', '/etc/openvpn/client.conf')
                               ip = compat_urlopen("http://ip.42.pl/raw").read()  
                               with open(LINKFILE1, "wb") as f: f.write(ip)                                   
                               f = open(LINKFILE1, 'r')
                               for line in f.readlines():
                                   IP = line.strip('\n')
                                   os.system('/etc/init.d/openvpn start > /dev/null 2>&1')
                                   time.sleep(8)
                                   ip2 = compat_urlopen("http://ip.42.pl/raw").read()  
                                   with open(LINKFILE2, "wb") as f: f.write(ip2)                                       
                                   f = open(LINKFILE2, 'r')
                                   for line in f.readlines():
                                       IP2 = line.strip('\n')
                                       if ip == ip2:
                                           self.session.open(MessageBox, _('VPN Not Working?...'), MessageBox.TYPE_INFO, timeout=5)
                                       else:
                                           self.session.open(MessageBox, _('Your Ip Address is :  ' + str(IP) + '\nYour New Ip Address is :  ' + str(IP2) + '\nYour Ip Location is :  Stockholm SE (1Gbit)'), MessageBox.TYPE_INFO, timeout=10)
                            else:
                                self.session.open(MessageBox, _('Cannot connect (or server is down) !'), MessageBox.TYPE_INFO, timeout=5)
                            return
                        elif returnValue =="com_167":
                            if connected_to_internet():
                               os.system('/etc/init.d/openvpn stop > /dev/null 2>&1')
                               os.system('rm -r %s > /dev/null 2>&1 && rm -f %s > /dev/null 2>&1' % (LINKFILE1, LINKFILE2))
                               os.system('rm -r -f /etc/openvpn; mkdir /etc/openvpn') 
                               shutil.copyfile('/etc/cfg_conf', '/etc/openvpn/cfg.conf')
                               shutil.copyfile('/etc/dollarovpn/client_conf30', '/etc/openvpn/client.conf')
                               ip = compat_urlopen("http://ip.42.pl/raw").read()  
                               with open(LINKFILE1, "wb") as f: f.write(ip)                                   
                               f = open(LINKFILE1, 'r')
                               for line in f.readlines():
                                   IP = line.strip('\n')
                                   os.system('/etc/init.d/openvpn start > /dev/null 2>&1')
                                   time.sleep(8)
                                   ip2 = compat_urlopen("http://ip.42.pl/raw").read()  
                                   with open(LINKFILE2, "wb") as f: f.write(ip2)                                       
                                   f = open(LINKFILE2, 'r')
                                   for line in f.readlines():
                                       IP2 = line.strip('\n')
                                       if ip == ip2:
                                           self.session.open(MessageBox, _('VPN Not Working?...'), MessageBox.TYPE_INFO, timeout=5)
                                       else:
                                           self.session.open(MessageBox, _('Your Ip Address is :  ' + str(IP) + '\nYour New Ip Address is :  ' + str(IP2) + '\nYour Ip Location is :  USA Colorado Springs CO (10Gbit)'), MessageBox.TYPE_INFO, timeout=10)
                            else:
                                self.session.open(MessageBox, _('Cannot connect (or server is down) !'), MessageBox.TYPE_INFO, timeout=5)
                            return
                        elif returnValue =="com_168":
                            if connected_to_internet():
                               os.system('/etc/init.d/openvpn stop > /dev/null 2>&1')
                               os.system('rm -r %s > /dev/null 2>&1 && rm -f %s > /dev/null 2>&1' % (LINKFILE1, LINKFILE2))
                               os.system('rm -r -f /etc/openvpn; mkdir /etc/openvpn') 
                               shutil.copyfile('/etc/cfg_conf', '/etc/openvpn/cfg.conf')
                               shutil.copyfile('/etc/dollarovpn/client_conf31', '/etc/openvpn/client.conf')
                               ip = compat_urlopen("http://ip.42.pl/raw").read()  
                               with open(LINKFILE1, "wb") as f: f.write(ip)                                   
                               f = open(LINKFILE1, 'r')
                               for line in f.readlines():
                                   IP = line.strip('\n')
                                   os.system('/etc/init.d/openvpn start > /dev/null 2>&1')
                                   time.sleep(8)
                                   ip2 = compat_urlopen("http://ip.42.pl/raw").read()  
                                   with open(LINKFILE2, "wb") as f: f.write(ip2)                                       
                                   f = open(LINKFILE2, 'r')
                                   for line in f.readlines():
                                       IP2 = line.strip('\n')
                                       if ip == ip2:
                                           self.session.open(MessageBox, _('VPN Not Working?...'), MessageBox.TYPE_INFO, timeout=5)
                                       else:
                                           self.session.open(MessageBox, _('Your Ip Address is :  ' + str(IP) + '\nYour New Ip Address is :  ' + str(IP2) + '\nYour Ip Location is :  London GB (10Gbit)'), MessageBox.TYPE_INFO, timeout=10)
                            else:
                                self.session.open(MessageBox, _('Cannot connect (or server is down) !'), MessageBox.TYPE_INFO, timeout=5)
                            return
                        elif returnValue =="com_169":
                            if connected_to_internet():
                               os.system('/etc/init.d/openvpn stop > /dev/null 2>&1')
                               os.system('rm -r %s > /dev/null 2>&1 && rm -f %s > /dev/null 2>&1' % (LINKFILE1, LINKFILE2))
                               os.system('rm -r -f /etc/openvpn; mkdir /etc/openvpn') 
                               shutil.copyfile('/etc/cfg_conf', '/etc/openvpn/cfg.conf')
                               shutil.copyfile('/etc/dollarovpn/client_conf32', '/etc/openvpn/client.conf')
                               ip = compat_urlopen("http://ip.42.pl/raw").read()  
                               with open(LINKFILE1, "wb") as f: f.write(ip)                                   
                               f = open(LINKFILE1, 'r')
                               for line in f.readlines():
                                   IP = line.strip('\n')
                                   os.system('/etc/init.d/openvpn start > /dev/null 2>&1')
                                   time.sleep(8)
                                   ip2 = compat_urlopen("http://ip.42.pl/raw").read()  
                                   with open(LINKFILE2, "wb") as f: f.write(ip2)                                       
                                   f = open(LINKFILE2, 'r')
                                   for line in f.readlines():
                                       IP2 = line.strip('\n')
                                       if ip == ip2:
                                           self.session.open(MessageBox, _('VPN Not Working?...'), MessageBox.TYPE_INFO, timeout=5)
                                       else:
                                           self.session.open(MessageBox, _('Your Ip Address is :  ' + str(IP) + '\nYour New Ip Address is :  ' + str(IP2) + '\nYour Ip Location is :  USA Seattle WA (1Gbit)'), MessageBox.TYPE_INFO, timeout=10)
                            else:
                                self.session.open(MessageBox, _('Cannot connect (or server is down) !'), MessageBox.TYPE_INFO, timeout=5)
                            return
                        elif returnValue =="com_170":
                            if connected_to_internet():
                               os.system('/etc/init.d/openvpn stop > /dev/null 2>&1')
                               os.system('rm -r %s > /dev/null 2>&1 && rm -f %s > /dev/null 2>&1' % (LINKFILE1, LINKFILE2))
                               os.system('rm -r -f /etc/openvpn; mkdir /etc/openvpn') 
                               shutil.copyfile('/etc/cfg_conf', '/etc/openvpn/cfg.conf')
                               shutil.copyfile('/etc/dollarovpn/client_conf33', '/etc/openvpn/client.conf')
                               ip = compat_urlopen("http://ip.42.pl/raw").read()  
                               with open(LINKFILE1, "wb") as f: f.write(ip)                                   
                               f = open(LINKFILE1, 'r')
                               for line in f.readlines():
                                   IP = line.strip('\n')
                                   os.system('/etc/init.d/openvpn start > /dev/null 2>&1')
                                   time.sleep(8)
                                   ip2 = compat_urlopen("http://ip.42.pl/raw").read()  
                                   with open(LINKFILE2, "wb") as f: f.write(ip2)                                       
                                   f = open(LINKFILE2, 'r')
                                   for line in f.readlines():
                                       IP2 = line.strip('\n')
                                       if ip == ip2:
                                           self.session.open(MessageBox, _('VPN Not Working?...'), MessageBox.TYPE_INFO, timeout=5)
                                       else:
                                           self.session.open(MessageBox, _('Your Ip Address is :  ' + str(IP) + '\nYour New Ip Address is :  ' + str(IP2) + '\nYour Ip Location is :  Paris FR (1Gbit)'), MessageBox.TYPE_INFO, timeout=10)
                            else:
                                self.session.open(MessageBox, _('Cannot connect (or server is down) !'), MessageBox.TYPE_INFO, timeout=5)
                            return
                        elif returnValue =="com_171":
                            if connected_to_internet():
                               os.system('/etc/init.d/openvpn stop > /dev/null 2>&1')
                               os.system('rm -r %s > /dev/null 2>&1 && rm -f %s > /dev/null 2>&1' % (LINKFILE1, LINKFILE2))
                               os.system('rm -r -f /etc/openvpn; mkdir /etc/openvpn') 
                               shutil.copyfile('/etc/cfg_conf', '/etc/openvpn/cfg.conf')
                               shutil.copyfile('/etc/dollarovpn/client_conf32', '/etc/openvpn/client.conf')
                               ip = compat_urlopen("http://ip.42.pl/raw").read()  
                               with open(LINKFILE1, "wb") as f: f.write(ip)                                   
                               f = open(LINKFILE1, 'r')
                               for line in f.readlines():
                                   IP = line.strip('\n')
                                   os.system('/etc/init.d/openvpn start > /dev/null 2>&1')
                                   time.sleep(8)
                                   ip2 = compat_urlopen("http://ip.42.pl/raw").read()  
                                   with open(LINKFILE2, "wb") as f: f.write(ip2)                                       
                                   f = open(LINKFILE2, 'r')
                                   for line in f.readlines():
                                       IP2 = line.strip('\n')
                                       if ip == ip2:
                                           self.session.open(MessageBox, _('VPN Not Working?...'), MessageBox.TYPE_INFO, timeout=5)
                                       else:
                                           self.session.open(MessageBox, _('Your Ip Address is :  ' + str(IP) + '\nYour New Ip Address is :  ' + str(IP2) + '\nYour Ip Location is :  CAN Toronto ON (1Gbit)'), MessageBox.TYPE_INFO, timeout=10)
                            else:
                                self.session.open(MessageBox, _('Cannot connect (or server is down) !'), MessageBox.TYPE_INFO, timeout=5)
                            return
                        elif returnValue =="com_172":
                            if connected_to_internet():
                               os.system('/etc/init.d/openvpn stop > /dev/null 2>&1')
                               os.system('rm -r %s > /dev/null 2>&1 && rm -f %s > /dev/null 2>&1' % (LINKFILE1, LINKFILE2))
                               os.system('rm -r -f /etc/openvpn; mkdir /etc/openvpn') 
                               shutil.copyfile('/etc/cfg_conf', '/etc/openvpn/cfg.conf')
                               shutil.copyfile('/etc/dollarovpn/client_conf33', '/etc/openvpn/client.conf')
                               ip = compat_urlopen("http://ip.42.pl/raw").read()  
                               with open(LINKFILE1, "wb") as f: f.write(ip)                                   
                               f = open(LINKFILE1, 'r')
                               for line in f.readlines():
                                   IP = line.strip('\n')
                                   os.system('/etc/init.d/openvpn start > /dev/null 2>&1')
                                   time.sleep(8)
                                   ip2 = compat_urlopen("http://ip.42.pl/raw").read()  
                                   with open(LINKFILE2, "wb") as f: f.write(ip2)                                       
                                   f = open(LINKFILE2, 'r')
                                   for line in f.readlines():
                                       IP2 = line.strip('\n')
                                       if ip == ip2:
                                           self.session.open(MessageBox, _('VPN Not Working?...'), MessageBox.TYPE_INFO, timeout=5)
                                       else:
                                           self.session.open(MessageBox, _('Your Ip Address is :  ' + str(IP) + '\nYour New Ip Address is :  ' + str(IP2) + '\nYour Ip Location is :  CAN Beauharnois QC (1Gbit)'), MessageBox.TYPE_INFO, timeout=10)
                            else:
                                self.session.open(MessageBox, _('Cannot connect (or server is down) !'), MessageBox.TYPE_INFO, timeout=5)
                            return
                        elif returnValue =="com_173":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia800702.us.archive.org/26/items/dreamosat/find_myCurrent-ip.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='Free VPN', cmdlist=cmdlist, finishedCallback=None)
                        elif returnValue =="com_174":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia800702.us.archive.org/26/items/dreamosat/OpenVPN_STOP.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='Free VPN', cmdlist=cmdlist, finishedCallback=None)
                        elif returnValue =="com_175":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia800702.us.archive.org/26/items/dreamosat/OpenVPN_START.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='Free VPN', cmdlist=cmdlist, finishedCallback=None)
                        elif returnValue =="com_176":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia800702.us.archive.org/26/items/dreamosat/OpenVPN_AUTO.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='Free VPN', cmdlist=cmdlist, finishedCallback=None)

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
