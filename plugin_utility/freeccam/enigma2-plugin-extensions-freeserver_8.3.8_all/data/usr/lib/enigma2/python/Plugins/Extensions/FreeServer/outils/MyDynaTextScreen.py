# -*- coding: UTF-8 -*-
from __future__ import print_function

Version_1 = 'Plese Wait whIle your EmU is being updated... Plese be patient...'
from enigma import eTimer
from datetime import date, datetime
from Screens.Screen import Screen
from Components.Label import Label
from Components.ActionMap import ActionMap
from Screens.Standby import TryQuitMainloop
from Screens.Console import Console
from Components.MenuList import MenuList
from Components.ActionMap import ActionMap
from Components.ActionMap import NumberActionMap, ActionMap
from Plugins.Plugin import PluginDescriptor
from Plugins.Extensions.FreeServer.outils.Update import Consolo
from Plugins.Extensions.FreeServer.outils.MyShPrombt import *
from Plugins.Extensions.FreeServer.outils.Showinfo import *
from struct import pack
from enigma import *
from Screens.MessageBox import MessageBox
from Screens.InputBox import InputBox
from Screens.ChoiceBox import ChoiceBox
from Components.ActionMap import ActionMap, NumberActionMap
from Components.ScrollLabel import ScrollLabel
from Components.Label import Label, MultiColorLabel
from Components.GUIComponent import *
from Components.Input import Input
from Components.ConfigList import ConfigList
from Plugins.Plugin import PluginDescriptor
from Screens.ServiceInfo import *
from Tools import Notifications
from Components.config import *
session = None
from time import *
import time
import datetime
import sys,os
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
class MyDynaTextScreen(Screen):
#### Edit By RAED
        from enigma import getDesktop
        dwidth = getDesktop(0).size().width()
        if dwidth == 1280:
            skin = """  
                <screen position="167,center" size="939,636" title=" Last Oscam Ncam Bin Update" flags="wfNoBorder" backgroundColor="#16000000">
                          <widget name="icon" render="Pixmap" pixmap="/usr/lib/enigma2/python/Plugins/Extensions/FreeServer/Cimages/Freeservers_2.jpg" zPosition="5" position="10,70" size="224,224" alphatest="blend" borderWidth="2" borderColor="white" backgroundColor="#16000000"/>
                          <widget name="icon2" render="Pixmap" pixmap="/usr/lib/enigma2/python/Plugins/Extensions/FreeServer/Cimages/Freeservers_3.png" zPosition="5" position="240,70" size="224,224" alphatest="blend" borderWidth="2" borderColor="white" backgroundColor="#16000000"/>
                          <widget name="icon3" render="Pixmap" pixmap="/usr/lib/enigma2/python/Plugins/Extensions/FreeServer/Cimages/Freeservers_4.png" zPosition="5" position="470,70" size="224,224" alphatest="blend" borderWidth="2" borderColor="white" backgroundColor="#16000000"/>
                          <widget name="icon4" render="Pixmap" pixmap="/usr/lib/enigma2/python/Plugins/Extensions/FreeServer/Cimages/Freeservers_5.png" zPosition="5" position="700,70" size="224,224" alphatest="blend" borderWidth="2" borderColor="white" backgroundColor="#16000000"/>
                          <widget name="Btn" render="Pixmap" pixmap="/usr/lib/enigma2/python/Plugins/Extensions/FreeServer/Deco/button_blue.png" position="45,590" size="40,20" zPosition="10" alphatest="blend"/>
                          <eLabel text="Gcam" zPosition="3" position="61,580" size="160,40" font="Play;22" transparent="1" backgroundColor="#16000000" halign="center" valign="center"/>
                          <widget name="Bt1" render="Pixmap" pixmap="/usr/lib/enigma2/python/Plugins/Extensions/FreeServer/Deco/button_yellow.png" position="283,590" size="40,20" zPosition="10" alphatest="blend"/>
                          <eLabel text="OScam" zPosition="3" position="501,580" size="160,40" font="Play;22" transparent="1" backgroundColor="#16000000" halign="center" valign="center"/>
                          <widget name="Bt2" render="Pixmap" pixmap="/usr/lib/enigma2/python/Plugins/Extensions/FreeServer/Deco/button_green.png" position="493,590" size="40,20" zPosition="10" alphatest="blend"/>
                          <eLabel text="Ncam" zPosition="3" position="287,580" size="160,40" font="Play;22" transparent="1" backgroundColor="#16000000" halign="center" valign="center"/>
                          <widget name="Bt3" render="Pixmap" pixmap="/usr/lib/enigma2/python/Plugins/Extensions/FreeServer/Deco/button_red.png" position="706,590" size="40,20" zPosition="10" alphatest="blend"/>
                          <eLabel text="Exit" zPosition="3" position="700,580" size="160,40" font="Play;22" transparent="1" backgroundColor="#16000000" halign="center" valign="center"/>
                          <widget name="Bt4" render="Pixmap" pixmap="/usr/lib/enigma2/python/Plugins/Extensions/FreeServer/Deco/key_info.png" position="176,523" size="35,25" zPosition="10" alphatest="blend"/>
                          <eLabel text="info" zPosition="3" position="181,515" size="127,40" font="Play;22" transparent="1" backgroundColor="#16000000" halign="center" valign="center"/>
                          <widget name="Bt5" render="Pixmap" pixmap="/usr/lib/enigma2/python/Plugins/Extensions/FreeServer/Deco/key_0.png" position="370,523" size="30,29" zPosition="10" alphatest="blend"/>
                          <eLabel text="Restart" zPosition="3" position="370,515" size="177,40" font="Play;22" transparent="1" backgroundColor="#16000000" halign="center" valign="center"/>
                          <widget name="Bt6" render="Pixmap" pixmap="/usr/lib/enigma2/python/Plugins/Extensions/FreeServer/Deco/key_1.png" position="573,523" size="30,29" zPosition="10" alphatest="blend"/>
                          <eLabel text="CCcam" zPosition="3" position="567,515" size="173,40" font="Play;22" transparent="1" backgroundColor="#16000000" halign="center" valign="center"/>
                          <widget name="myText" position="7,318" size="923,145" font="Play;32" foregroundColor="#00bab329" transparent="1" zPosition="2" valign="center" halign="center"/>
                </screen>"""
        else:
            skin = """
                  <screen position="center,center" size="1135,636" title=" Last Oscam Ncam Bin Update" flags="wfNoBorder" backgroundColor="#20000000">
                          <widget name="icon" render="Pixmap" pixmap="/usr/lib/enigma2/python/Plugins/Extensions/FreeServer/Cimages/Freeservers_2.jpg" zPosition="5" position="30,70" size="224,224" alphatest="blend" borderWidth="2" borderColor="white" backgroundColor="#16000000"/>
                          <widget name="icon2" render="Pixmap" pixmap="/usr/lib/enigma2/python/Plugins/Extensions/FreeServer/Cimages/Freeservers_3.png" zPosition="5" position="310,70" size="224,224" alphatest="blend" borderWidth="2" borderColor="white" backgroundColor="#16000000"/>
                          <widget name="icon3" render="Pixmap" pixmap="/usr/lib/enigma2/python/Plugins/Extensions/FreeServer/Cimages/Freeservers_4.png" zPosition="5" position="585,70" size="224,224" alphatest="blend" borderWidth="2" borderColor="white" backgroundColor="#16000000"/>
                          <widget name="icon4" render="Pixmap" pixmap="/usr/lib/enigma2/python/Plugins/Extensions/FreeServer/Cimages/Freeservers_5.png" zPosition="5" position="865,70" size="224,224" alphatest="blend" borderWidth="2" borderColor="white" backgroundColor="#16000000"/>
                          <widget name="Btn" render="Pixmap" pixmap="/usr/lib/enigma2/python/Plugins/Extensions/FreeServer/Deco/button_blue.png" position="140,590" size="40,20" zPosition="10" alphatest="blend"/>
                          <eLabel text="Gcam" zPosition="3" position="156,578" size="160,40" font="Play;32" transparent="1" backgroundColor="#16000000" halign="center" valign="center"/>
                          <widget name="Bt1" render="Pixmap" pixmap="/usr/lib/enigma2/python/Plugins/Extensions/FreeServer/Deco/button_yellow.png" position="387,590" size="40,20" zPosition="10" alphatest="blend"/>
                          <eLabel text="OScam" zPosition="3" position="640,578" size="160,40" font="Play;32" transparent="1" backgroundColor="#16000000" halign="center" valign="center"/>
                          <widget name="Bt2" render="Pixmap" pixmap="/usr/lib/enigma2/python/Plugins/Extensions/FreeServer/Deco/button_green.png" position="620,590" size="40,20" zPosition="10" alphatest="blend"/>
                          <eLabel text="Ncam" zPosition="3" position="404,578" size="160,40" font="Play;32" transparent="1" backgroundColor="#16000000" halign="center" valign="center"/>
                          <widget name="Bt3" render="Pixmap" pixmap="/usr/lib/enigma2/python/Plugins/Extensions/FreeServer/Deco/button_red.png" position="837,590" size="40,20" zPosition="10" alphatest="blend"/>
                          <eLabel text="Exit" zPosition="3" position="850,578" size="160,40" font="Play;32" transparent="1" backgroundColor="#16000000" halign="center" valign="center"/>
                          <widget name="Bt4" render="Pixmap" pixmap="/usr/lib/enigma2/python/Plugins/Extensions/FreeServer/Deco/key_info.png" position="291,502" size="35,25" zPosition="10" alphatest="blend"/>
                          <eLabel text="info" zPosition="3" position="312,494" size="120,40" font="Play;32" transparent="1" backgroundColor="#16000000" halign="center" valign="center"/>
                          <widget name="Bt5" render="Pixmap" pixmap="/usr/lib/enigma2/python/Plugins/Extensions/FreeServer/Deco/key_0.png" position="480,502" size="35,25" zPosition="10" alphatest="blend"/>
                          <eLabel text="Restart" zPosition="3" position="504,494" size="163,40" font="Play;32" transparent="1" backgroundColor="#16000000" halign="center" valign="center"/>
                          <widget name="Bt6" render="Pixmap" pixmap="/usr/lib/enigma2/python/Plugins/Extensions/FreeServer/Deco/key_1.png" position="718,502" size="35,25" zPosition="10" alphatest="blend"/>
                          <eLabel text="CCcam" zPosition="3" position="746,494" size="140,40" font="Play;32" transparent="1" backgroundColor="#16000000" halign="center" valign="center"/>
                          <widget name="myText" position="center,315" size="1115,136" font="Play;35" foregroundColor="#00bab329" transparent="1" zPosition="2" halign="center" valign="center"/>
                  </screen>"""

        def __init__(self, session, args = 0):
                self.session = session
                Screen.__init__(self, session)
                self.text=""
                self.text="Emu OScam, Ncam, Gcam and CCcam arm mips All ipk and deb For enigma2"
### EDit By RAED To DreamOS OE2.5/2.6
                #if fileExists('/var/lib/dpkg/status'):
                #     self.wget = "/usr/bin/wget2 --no-check-certificate"
                #else:
                #     self.wget = "/usr/bin/wget"
                self.wget = "wget --no-check-certificate"

### End
                self["myText"] = Label()
                self["go"] = Label()    
                self["goto"] = Label()          
                self["prombt"] = Label()              
                self["myRedBtn"] = Label(_("Cancel"))
                self["myGreenBtn"] = Label(_("OSCAM"))
                self["myYellowBtn"] = Label(_("NCAM"))
                self["myBlueBtn"] = Label(_("GCAM"))                            
                self.cmdlist = []
                self['text'] = Label()
                self["key_blue"] = Label()
                self["key_yellow"] = Label()
                self["key_green"] = Label()
                self["key_red"] = Label()       
                self['icon'] = Pixmap()  
                self['icon2'] = Pixmap()                  
                self['icon3'] = Pixmap() 
                self['icon4'] = Pixmap()                                           
                self['Btn'] = Pixmap()
                self['Bt1'] = Pixmap()
                self['Bt2'] = Pixmap()
                self['Bt3'] = Pixmap()    
                self['Bt4'] = Pixmap() 
                self['Bt5'] = Pixmap()  
                self['Bt6'] = Pixmap()                                          
                #self["myMenu"] = MenuList(list)
                self['actions'] = ActionMap(['MovieSelectionActions', 'SetupActions', 'DirectionActions', 'ColorActions'], {'ok': self.close,
                        "showEventInfo": self.gotoa,    
                        '0': self.restart, 
                        '1': self.goc,                                          
                        'blue': self.got,   
                        'yellow': self.goto,                        
                        #'ok': self.go,                                    
                        'red': self.close,
                        'cancel': self.cancel,
                        'green': self.go}, -1)
                self.onShown.append(self.setMyText)
                self.go               
                self.goto
                self.got               
                self.goc
                self.prombt
                self.onChangedEntry = []
                self.timer_list = []
                self.processed_timers = [] 
                self.timer = eTimer()
                self.initialservice = session.nav.getCurrentlyPlayingServiceReference()
                self.updateTimer = eTimer()
                self.timer.start(2000, True)

            
        def info(self):
            self.session.open(Showinfo)          
             
        def go(self):    
                cmdlist = []
### EDit By RAED To DreamOS OE2.5/2.6
                cmdlist.append("%s -qO - '" % self.wget + "'")
                if DreamOS():
                       cmdlist.append("%s https://ia601502.us.archive.org/4/items/FreeServerinfo/oscam-all-images-arm+mips_all.deb.sh -qO - | /bin/sh" % self.wget)
                else:
                       cmdlist.append("%s https://ia601502.us.archive.org/4/items/FreeServerinfo/OSCamEmus_all.ipk.sh -qO - | /bin/sh" % self.wget)
                self.session.open(Consolo, title='OSCamEmus_all', cmdlist=cmdlist, finishedCallback=self.message) 
                from enigma import eServiceReference
                from Plugins.Extensions.FreeServer.outils.InfoBar import ALAJREStream3
                url = 'https://ia601508.us.archive.org/3/items/11_20210417_20210417/11.mp3'
                ref = eServiceReference(4097, 0, url)
                ref.setName(Version_1)         
                self.session.openWithCallback(self.backToIntialService, ALAJREStream3, ref)
                
        def backToIntialService(self, ret = None):
            self.session.nav.stopService()
            self.session.nav.playService(self.initialservice)
            self.fast()

        def fast(self):   
            self.timer.stop()
            
        def message(self):            
            time.sleep(5)
            self.session.openWithCallback(self.restartenigma, MessageBox, _('Restart Enigma2 To Load New Update?'), MessageBox.TYPE_YESNO, timeout=15)                  
                                    
        def Update(self):
            Update = "afile"
            afile = open('/tmp/monfichier.txt', 'w')
            self.session.openWithCallback(self.restartenigma, MessageBox, _('Free Server V_' + str(Update) + '\nRestart Enigma2 To Load New Settings?'), MessageBox.TYPE_YESNO)            
            
        def setMyText(self):
            self["myText"].setText(self.text)
                                        
        def goto(self):
                cmdlist = []
### EDit By RAED To DreamOS OE2.5/2.6
                cmdlist.append("%s -qO - '" % self.wget + "'")
                if DreamOS():
                       cmdlist.append("%s https://ia801502.us.archive.org/4/items/FreeServerinfo/NCamEmus_all.deb.sh -qO - | /bin/sh" % self.wget)
                else:
                       cmdlist.append("%s https://ia801502.us.archive.org/4/items/FreeServerinfo/NCamEmus_all.ipk.sh -qO - | /bin/sh" % self.wget)
                self.session.open(Consolo, title='NCamEmus_all', cmdlist=cmdlist, finishedCallback=self.message)
                from enigma import eServiceReference
                from Plugins.Extensions.FreeServer.outils.InfoBar import ALAJREStream2
                url = 'https://ia902507.us.archive.org/18/items/Arrayfaded/leningrad-big-lovkaya-zhopa-i-leningradskiy-bolt.mp3'
                ref = eServiceReference(4097, 0, url)
                ref.setName(Version_1)         
                self.session.openWithCallback(self.backToIntialService, ALAJREStream2, ref)
                
        def got(self):
                cmdlist = []
### EDit By RAED To DreamOS OE2.5/2.6
                cmdlist.append("%s -qO - '" % self.wget + "'")
                if DreamOS():
                       cmdlist.append("%s https://ia801502.us.archive.org/4/items/FreeServerinfo/GCamEmus_all.deb.sh -qO - | /bin/sh" % self.wget)
                else:
                       cmdlist.append("%s https://ia801502.us.archive.org/4/items/FreeServerinfo/GCamEmus_all.ipk.sh -qO - | /bin/sh" % self.wget)
                self.session.open(Consolo, title='GCamEmus_all.ipk', cmdlist=cmdlist, finishedCallback=self.message)
                from enigma import eServiceReference
                from Plugins.Extensions.FreeServer.outils.InfoBar import ALAJREStream4
                url = 'https://ia601508.us.archive.org/3/items/11_20210417_20210417/11.mp3'
                ref = eServiceReference(4097, 0, url)
                ref.setName(Version_1)         
                self.session.openWithCallback(self.backToIntialService, ALAJREStream4, ref)

        def goc(self):    
                cmdlist = []
### EDit By RAED To DreamOS OE2.5/2.6
                cmdlist.append("%s -qO - '" % self.wget + "'")
                if DreamOS():
                       cmdlist.append("%s https://ia803000.us.archive.org/30/items/FreeServerinfo/CCcamEmus_all.deb.sh -qO - | /bin/sh" % self.wget)
                else:
                       cmdlist.append("%s https://ia803000.us.archive.org/30/items/FreeServerinfo/CCcamEmus_all.ipk.sh -qO - | /bin/sh" % self.wget)
                self.session.open(Consolo, title='CCCamEmus_all.ipk', cmdlist=cmdlist, finishedCallback=self.message)
                from enigma import eServiceReference
                from Plugins.Extensions.FreeServer.outils.InfoBar import ALAJREStream
                url = 'https://ia902507.us.archive.org/18/items/Arrayfaded/leningrad-big-lovkaya-zhopa-i-leningradskiy-bolt.mp3'
                ref = eServiceReference(4097, 0, url)
                ref.setName(Version_1)         
                self.session.openWithCallback(self.backToIntialService, ALAJREStream, ref)
     
        def gotoa(self):
### EDit By RAED To DreamOS OE2.5/2.6
                os.system("%s https://ia801502.us.archive.org/4/items/FreeServerinfo/FreeServerinfoo.sh -qO - | /bin/sh" % self.wget) 
                self.session.open(Showinfo5)
                
        def prombt(self, com):
                scripts = "/usr/lib/enigma2/python/Plugins/Extensions/FreeServer/scripts/"
                os.chmod(scripts, 755)
                self.session.open(Console,_("Executing: %s") % (com), ["%s" % com])
                                                        
        def key8(self):
            self.session.open(Showinfo5) 
                                                        
        def restart(self):
            self.session.openWithCallback(self.restartenigma, MessageBox, _('Restart Enigma2 To Load New Update?'), MessageBox.TYPE_YESNO, timeout=20)            
        
        def restartenigma(self, result):
            if result:
                self.session.open(TryQuitMainloop, 3)
                
        def cancel(self):
                print("\n[MyShPrombt] cancel\n")
                self.close(None)
                        
def main(session, **kwargs):
        session.open(MyDynaTextScreen)

