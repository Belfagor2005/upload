# -*- coding: UTF-8 -*-
from __future__ import print_function

from struct import pack
from enigma import *
from Screens.Screen import Screen
from Screens.MessageBox import MessageBox
from Screens.InputBox import InputBox
from Screens.ChoiceBox import ChoiceBox
from Components.ActionMap import ActionMap, NumberActionMap
from Components.ScrollLabel import ScrollLabel
from Components.Label import Label, MultiColorLabel
from Components.GUIComponent import *
from Components.MenuList import MenuList        
from Components.Input import Input
from Components.ConfigList import ConfigList
from Screens.Console import Console
from Plugins.Plugin import PluginDescriptor
from Screens.ServiceInfo import *
from Plugins.Plugin import PluginDescriptor
from Tools import Notifications
from Components.config import *
from Tools.Directories import fileExists 
from Plugins.Extensions.FreeServer.outils.MyStatus import *
from Plugins.Extensions.FreeServer.outils.MyShPrombt import *
from Plugins.Extensions.FreeServer.outils.NetworkMacsetup import *
from Plugins.Extensions.FreeServer.outils.MyDynaTextScreen import *
from Plugins.Extensions.FreeServer.outils.MyDynaTextScreen2 import *
from Plugins.Extensions.FreeServer.outils.Myiptvservices import *
from Plugins.Extensions.FreeServer.outils.Myvpnservices import *
from Plugins.Extensions.FreeServer.outils.MyKoraScreen import *
from Plugins.Extensions.FreeServer.outils.MyKoraScreen2 import *
from Plugins.Extensions.FreeServer.outils.CronTimers import *
from Plugins.Extensions.FreeServer.outils.LiseScreencccam import *
from Plugins.Extensions.FreeServer.outils.LiseScreencccam2 import *
from Plugins.Extensions.FreeServer.outils.Update import *
from Plugins.Extensions.FreeServer.outils.Showinfo import Showinfo, Showinfo1, Showinfo2, Showinfo3, Showinfo4, Showinfo5
import os, sys
from enigma import getDesktop
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
def connected_to_internet():
    import requests
    try:
        _ = requests.get('http://www.google.com', timeout=5)
        print("internet connection available.")
        return True
    except requests.ConnectionError:
        print("No internet connection available.")
        return False
    print(connected_to_internet())
#### end

class Input(Screen):
#### Edit By RAED
    if isHD():
        skin = """
                <screen position="center,center" size="600,360" title="Input" >
                    <widget name="menu" position="10,10" size="600,360" scrollbarMode="showOnDemand" />
                </screen>"""
    else:
        if DreamOS():
            skin = """
                    <screen position="center,center" size="900,610" title="Input" >
                        <widget name="menu" position="8,8" size="890,600" scrollbarMode="showOnDemand" />
                    </screen>"""
        else:
            skin = """
                    <screen position="center,center" size="900,610" title="Input" >
                        <widget name="menu" position="8,8" size="890,600" font="Regular;37" itemHeight="50" scrollbarMode="showOnDemand" />
                    </screen>"""
#### end
    def __init__(self, session, args = 0):
        if config.plugins.FreeServerminoo.lang.value == "EN":
                title1="CronTimers"
                title2="Show Ncam details"
                title3="Show Oscam details"
                title4="Mac address changer"
                title5="Download some of file to (Vpn, server ..etc)"
                title6="Last Oscam/Ncam Update IPK/DEB"
                title7="lists_world"
                title8="Schedule to football matchs this week"
                title9="Download sharing server as you select #1"
                title10="Download sharing server as you select #2"
                title11="IPTV For Smart TV enigma2"
                title12="VPN Solution For enigma2"              
                title13="Football Match ON LINE #1"
                title14="Football Match ON LINE #2"
                title15="Update plugin"
                title16="Radio"
                title17="About"
        elif config.plugins.FreeServerminoo.lang.value == "AR":
                title1="المؤقت الآلي"
                title2="Ncam عرض معلومات أيمو"
                title3="Oscam عرض معلومات أيمو"
                title4="'MAC تغير عنوان"
                title5="تحميل ملفات مختلفة مثل سيرفرات الشيرنج و تغير عنوان الجهاز وغيرها"
                title6="deb/ipk تحميل تحديثات ايمو الانكام والاوسكام ملفات ذاتية التثبيت"
                title7="lists_world"
                title8="عرض جدول مباريات كرة القدم لهذا الإسبوع"
                title9="تحميل سيرفرات الشيرنج #1"
                title10="تحميل سيرفرات الشيرنج #2"
                title11="IPTV For Smart TV enigma2"
                title12="VPN Solution For enigma2" 
                title13="مشاهدة المباريات مباشرة بواسطة الإنترنيت #1"
                title14="مشاهدة المباريات مباشرة بواسطة الإنترنيت #2"
                title15="تحديث البلجن"
                title16="Radio"
                title17="معلمات عن البلجن"
        elif config.plugins.FreeServerminoo.lang.value == "FR":
                title1="CronTimers"
                title2="Afficher les détails de la Ncam"
                title3="Afficher les détails de la Oscam"
                title4="Changeur d'adresse Mac"
                title5="Téléchargez une partie du fichier sur (Vpn, server ..etc)"
                title6="Dernière Oscam/Ncam Mise à jour IPK/DEB"
                title7="lists_world"
                title8="Calendrier des matchs de football cette semaine"
                title9="Téléchargez le serveur de partage que vous sélectionnez #1"
                title10="Téléchargez le serveur de partage que vous sélectionnez #2"
                title11="IPTV For Smart TV enigma2"
                title12="VPN Solution For enigma2" 
                title13="Match de football en ligne #1"
                title14="Match de football en ligne #2"
                title15="Mise à jour brancher"
                title16="Radio"
                title17="Sur"
        self.skin = Input.skin
        self.session = session
        Screen.__init__(self, session)
### EDit By RAED To DreamOS OE2.5/2.6
        #if fileExists('/var/lib/dpkg/status'):
        #     self.wget = "/usr/bin/wget2 --no-check-certificate"
        #else:
        #     self.wget = "/usr/bin/wget"
        self.wget = "wget --no-check-certificate"
        self.menu = args
        list = []               
        list.append((_("%s") % title1, "CronTimers"))
        if fileExists('/tmp/ncam.log'):
              list.append((_("%s") % title2, "Showinfo1"))
        if fileExists('/tmp/oscam.log'):
              list.append((_("%s") % title3, "Showinfo4"))
        list.append((_("%s") % title4, "NetworkMacsetup"))
        if connected_to_internet() == True:  ## Code to find connection internet or not
              list.append((_("%s") % title5, "MyShPrombt"))
              list.append((_("%s") % title6, "MyDynaTextScreen"))
              if fileExists('/tmp/freeservre79'):
                   list.append((_("%s") % title7, "Showinfo"))
              list.append((_("%s") % title8, "Showinfo2"))
              list.append((_("%s") % title9, "LiseScreencccam"))
              list.append((_("%s") % title10, "LiseScreencccam2"))
              list.append((_("%s") % title11, "Myiptvservices"))
              list.append((_("%s") % title12, "Myvpnservices"))
              list.append((_("%s") % title13, "MyKoraScreen"))
              list.append((_("%s") % title14, "MyKoraScreen2"))
              #list.append((_("%s") % title15, "Update")) # No need it any more as the update plugin in in the different mwthod
              list.append((_("%s") % title16, "Radio"))
        list.append((_("%s") % title17, "about"))
        self["menu"] = MenuList(list)
        self["actions"] = ActionMap(["WizardActions", "DirectionActions"],{"ok": self.go,"back": self.close,}, -1)

#    def Cronmanager_OS(self):
#        if fileExists('/usr/lib/enigma2/python/Plugins/Extensions/Cronmanager/plugin.pyo'):
#           from Plugins.Extensions.Cronmanager.plugin.py import Cronmanager
#           self.session.open(Cronmanager)
#        else:
#           from Components.Console import Console
#           self.Console = Console()
#           wget = "/usr/bin/wget2"
#           crt = "--debug --no-check-certificate"
#           tmpfile = "/tmp/cron.deb"
#           myurl = 'https://ia600702.us.archive.org/26/items/dreamosat/enigma2-plugin-extensions-cronmanager_3.0_all.deb'
#           command = '%s -q %s %s %s' % (wget, crt, tmpfile, myurl)
#           command1 = 'depk -i %s' % (tmpfile)
#           self.Console.ePopen(command, command1)
#           self.close(self.Cronmanager_OS)

    def go(self):
        returnValue = self["menu"].l.getCurrentSelection()[1]
        if returnValue is not None:
### EDit By RAED
            if returnValue is "CronTimers":
                if fileExists('/var/lib/dpkg/status'):
                     from Plugins.Extensions.Cronmanager.plugin import Cronmanager
                     self.session.open(Cronmanager) 
                else:
                     if connected_to_internet() == True: ## Code to find connection internet or not
                          self.session.open(CronTimers)
                     else:
                          self.session.open(MessageBox, _('Error: connection failed !'), MessageBox.TYPE_INFO, timeout=5)
            elif returnValue is "about":
                self.session.open(MyStatus)
            elif returnValue is "Showinfo1":
                #if fileExists('/tmp/ncam.log'):
                      self.session.open(Showinfo1)
                #else:
                #      self.session.open(MessageBox,_('NCam Log Not Found'), MessageBox.TYPE_INFO, timeout=15)  
            elif returnValue is "Showinfo4":
                #if fileExists('/tmp/oscam.log'):
                      self.session.open(Showinfo4)
                #else:
                #      self.session.open(MessageBox,_('OScam Log Not Found'), MessageBox.TYPE_INFO, timeout=15)  
            elif returnValue is "NetworkMacsetup":
                self.session.open(NetworkMacsetup)
            elif returnValue is "MyDynaTextScreen":
                   self.session.open(MyDynaTextScreen)                            
            elif returnValue is "LiseScreencccam":
                   self.session.open(LiseScreencccam)
            elif returnValue is "LiseScreencccam2":
                   self.session.open(LiseScreencccam2)
            elif returnValue is "Myiptvservices":
                   self.session.open(Myiptvservices)  
            elif returnValue is "Myvpnservices":
                   self.session.open(Myvpnservices)  
            elif returnValue is "MyKoraScreen":
                   self.session.open(MyKoraScreen)   
            elif returnValue is "MyKoraScreen2":
                   self.session.open(MyKoraScreen2)                       
            elif returnValue is "Showinfo":
                  try:
                      os.system("%s https://ia800702.us.archive.org/26/items/dreamosat/lists_world.sh -qO - | /bin/sh" % self.wget) 
                      self.session.open(Showinfo)
                  #else:
                  except:
                      self.session.open(MessageBox,_('lists_world not found'), MessageBox.TYPE_INFO, timeout=10)
            elif returnValue is "Showinfo2":
                  #if not fileExists('/tmp/freeservre80'):
                  try:
                      os.system("%s https://ia601500.us.archive.org/32/items/FoulFreecccamserver/Programetvfoot.sh -qO - | /bin/sh" % self.wget) 
                      os.system("sed -i '1d' /tmp/freeservre80") ## Edit By RAED To Remove First line no need it
                      self.session.open(Showinfo2)
                  #else:
                  except:
                      self.session.open(MessageBox,_('Schedule to football match to day not found'), MessageBox.TYPE_INFO, timeout=10)
            elif returnValue is "MyShPrombt":
                   self.session.open(MyShPrombt) 
            elif returnValue is "Radio":
                   self.session.open(MyDynaTextScreen2)                   
            elif returnValue is "Update":
                   self.session.open(Update)
            #else:
            #    self.session.open(MessageBox, _('Error: connection failed !'), MessageBox.TYPE_INFO, timeout=5)
### End 
