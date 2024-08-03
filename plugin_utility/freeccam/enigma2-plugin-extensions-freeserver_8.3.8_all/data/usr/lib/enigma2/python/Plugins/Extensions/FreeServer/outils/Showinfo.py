# -*- coding: utf-8 -*-
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
from Components.Pixmap import Pixmap  
from Components.ConfigList import ConfigList
from Screens.Console import Console
from Plugins.Plugin import PluginDescriptor
from Screens.ServiceInfo import *
from Plugins.Plugin import PluginDescriptor
from Tools import Notifications
from Components.config import *
from Tools.Directories import fileExists
from enigma import getDesktop

def DreamOS():
    if os.path.exists('/var/lib/dpkg/status'):
        return DreamOS

def getDesktopSize():
    s = getDesktop(0).size()
    return (s.width(), s.height())

def isHD():
    desktopSize = getDesktopSize()
    return desktopSize[0] == 1280

######################################################################################################
plugin_path = '/usr/lib/enigma2/python/Plugins/Extensions/FreeServer/fonts'
skin_path = '/usr/lib/enigma2/python/Plugins/Extensions/FreeServer/Skin/'
p_path = '/usr/lib/enigma2/python/Plugins/Extensions/FreeServer'   
from enigma import addFont
try:
    #addFont('%s/Raleway-Black.ttf' % plugin_path, 'Rale', 100, 1)
    addFont('%s/bpmono.ttf' % plugin_path, 'Play', 100, 1)
    #addFont('%s/slyk-medium.ttf' % plugin_path, 'slyk', 100, 1)
except Exception as ex:
    print(ex)
#########################################################################################################
global info_lines
if isHD():
    info_lines=22
    info_lines_Showinfo=22
    info_lines_Showinfo1=22
    info_lines_Showinfo2=22
    info_lines_Showinfo5=27
    info_lines_Showinfo7=22
else:
    info_lines=30
    info_lines_Showinfo=24
    info_lines_Showinfo1=24
    info_lines_Showinfo2=22
    info_lines_Showinfo5=28
    info_lines_Showinfo7=22
global info_bottomline
info_bottomline=0
global info_topline
info_topline=0
global infofile
#########################################################################################################
class Showinfo(Screen):
#### Edit By RAED
        if isHD():
            skin = """
                <screen position="0,0" size="1280,720" title="Schedule to football matchs this week" backgroundColor="#16000000" flags="wfNoBorder">
                      <widget source="Title" render="Label" position="12,7" size="600,32" font="Play;28" backgroundColor="#16000000" foregroundColor="#FFE375" valign="center" halign="center" zPosition="2"/>
                      <eLabel text="Move Up/Down or Left/Right to move list/page" position="600,7" size="680,32" font="Play;28" foregroundColor="#FC0000" backgroundColor="#16000000" zPosition="2"/>
                      <widget name="Showinfo" position="50,86" size="1229,625" font="Play;26" backgroundColor="#16000000" foregroundColor="#00ffffff"/>
                      <eLabel text="Number" position="0,44" size="150,32" font="Play;26" valign="center" backgroundColor="#00666666" halign="center" zPosition="3"/>
                      <eLabel text="Country" position="195,44" size="200,32" font="Play;26" valign="center" backgroundColor="#00666666" halign="center" zPosition="3"/>
                      <eLabel text="Address IP" position="430,44" size="250,32" font="Play;26" valign="center" backgroundColor="#00666666" halign="center" zPosition="4"/>
                      <eLabel text="Ping" position="655,44" size="150,32" font="Play;26" valign="center" backgroundColor="#00666666" halign="center" zPosition="3"/>
                      <eLabel text="Port" position="810,44" size="200,32" font="Play;26" valign="center" backgroundColor="#00666666" halign="center" zPosition="3"/>
                      <eLabel name="Top_Background" position="0,44" size="1280,34" backgroundColor="#00666666" zPosition="2"/>
                      <eLabel name="Ver1_long" position="165,45" size="5,685" backgroundColor="#00666666" zPosition="3"/>
                      <eLabel name="Ver2_long" position="430,45" size="5,685" backgroundColor="#00666666" zPosition="3"/>
                      <eLabel name="Ver3_long" position="670,45" size="5,685" backgroundColor="#00666666" zPosition="3"/>
                      <eLabel name="Ver4_long" position="830,45" size="5,685" backgroundColor="#00666666" zPosition="3"/>
                      <eLabel name="Ver1_short" position="165,45" size="5,32" backgroundColor="#16000000" zPosition="4"/>
                      <eLabel name="Ver2_short" position="430,45" size="5,32" backgroundColor="#16000000" zPosition="4"/>
                      <eLabel name="Ver3_short" position="670,45" size="5,32" backgroundColor="#16000000" zPosition="4"/>
                      <eLabel name="Ver4_short" position="830,45" size="5,32" backgroundColor="#16000000" zPosition="4"/>
                </screen>"""
        else:
           skin = """
                <screen position="0,0" size="1920,1080" title="Schedule to football matchs this week" backgroundColor="#16000000" flags="wfNoBorder">
                      <widget source="Title" render="Label" position="20,5" size="900,50" font="Play;40" backgroundColor="#16000000" foregroundColor="#FFE375" valign="center" halign="center" zPosition="2"/>
                      <eLabel text="Move Up/Down or Left/Right to move list/page" position="895,5" size="1000,50" font="Play;45" foregroundColor="#FC0000" backgroundColor="#16000000" zPosition="2" valign="center" halign="center"/>
                      <widget name="Showinfo" position="140,125" size="1835,940" font="Play;36" backgroundColor="#16000000" foregroundColor="#00ffffff"/>
                      <eLabel text="Number" position="15,65" size="300,50" font="Play;40" backgroundColor="#00666666" valign="center" halign="center" zPosition="3"/>
                      <eLabel text="Country" position="330,65" size="300,50" font="Play;40" backgroundColor="#00666666" valign="center" halign="center" zPosition="3"/>
                      <eLabel text="Address IP" position="675,65" size="320,50" font="Play;40" backgroundColor="#00666666" valign="center" halign="center" zPosition="4"/>
                      <eLabel text="Ping" position="930,65" size="300,50" font="Play;40" backgroundColor="#00666666" valign="center" halign="center" zPosition="3"/>
                      <eLabel text="Port" position="1180,65" size="300,50" font="Play;40" backgroundColor="#00666666" valign="center" halign="center" zPosition="3"/>
                      <eLabel name="Top_Background" position="0,65" size="1920,50" backgroundColor="#00666666" zPosition="2"/>
                      <eLabel name="Ver1_long" position="330,65" size="10,1000" backgroundColor="#00666666" zPosition="3"/>
                      <eLabel name="Ver2_long" position="680,65" size="10,1000" backgroundColor="#00666666" zPosition="3"/>
                      <eLabel name="Ver3_long" position="1000,65" size="10,1000" backgroundColor="#00666666" zPosition="3"/>
                      <eLabel name="Ver4_long" position="1210,65" size="10,1000" backgroundColor="#00666666" zPosition="3"/>
                      <eLabel name="Ver1_short" position="330,65" size="10,50" backgroundColor="#16000000" zPosition="4"/>
                      <eLabel name="Ver2_short" position="680,65" size="10,50" backgroundColor="#16000000" zPosition="4"/>
                      <eLabel name="Ver3_short" position="1000,65" size="10,50" backgroundColor="#16000000" zPosition="4"/>
                      <eLabel name="Ver4_short" position="1210,65" size="10,50" backgroundColor="#16000000" zPosition="4"/>
                </screen>"""
### End
        def __init__(self, session):
                Screen.__init__(self, session)
                self.skin = Showinfo.skin
                self.setTitle("List of VPN server avilable")
                self['icon'] = Pixmap() 
                global infofile
                global info_topline
                info_topline=0
                global info_bottomline
                infofile = "/tmp/freeservre79"
                f = open(infofile,"r")                   
                info_bottomline=1
                line=f.readline()
                print(line)
                while (line):
                        if len(line) > 1:
                                info_bottomline=info_bottomline+1     
                        line=f.readline()
                        print(line)
                f.close()
                if info_bottomline < info_lines_Showinfo:
                        info_topline=0
                        info_bottomline=info_lines_Showinfo
                self["Showinfo"] = MultiColorLabel("\n")
                self.ShowinfoPage()
                self.pagebackward
                self["setupActions"] = ActionMap([ "ColorActions", "SetupActions", "InfobarMovieListActions" ],                         
                        {                                                                                    
                        "red": self.cancel,                                                                  
                        "cancel": self.cancel,                                                               
                        "ok": self.cancel,                                                                     
                        "left": self.pagebackward,                                                                           
                        "right": self.pageforward,                                                                       
                        "up": self.backward,                                                                           
                        "down": self.forward,                                                                       
                        })                                                                                   

        def setWindowTitle(self):
                self.setTitle(_("Display info logfile %s") % infofile)
       
        def ShowinfoPage(self):                                                                     
                        global info_topline
                        global info_bottomline
                        global info_lines_Showinfo
                        global infofile
                        f = open(infofile,"r")               
                        infotext = ""                            
                        i=0
                        while i<(info_topline+info_lines_Showinfo):
                                if i>(info_topline-1):
                                        text=f.readline()
                                        if len(text) > 1:
                                                infotext = infotext+text                           
                                else:
                                        text=f.readline()
                                i=i+1
                        f.close
                        self["Showinfo"].setText(infotext)    

        def cancel(self):
                self.close(False)

        def backward(self):      
                global info_topline
                global info_lines_Showinfo
                info_topline=info_topline-1
                if info_topline<0:
                        info_topline=0
                self.ShowinfoPage()

        def forward(self):      
                global info_topline
                info_topline=info_topline+1
                if info_topline>info_bottomline-info_lines_Showinfo:
                        info_topline=info_bottomline-info_lines_Showinfo
                self.ShowinfoPage()

        def pagebackward(self):      
                global info_topline
                global info_lines_Showinfo
                info_topline=info_topline-info_lines_Showinfo
                if info_topline<0:
                        info_topline=0
                self.ShowinfoPage()

        def pageforward(self):      
                global info_topline
                global info_bottomline
                global info_lines_Showinfo
                info_topline=info_topline+info_lines_Showinfo
                if info_topline>info_bottomline-info_lines_Showinfo:
                        info_topline=info_bottomline-info_lines_Showinfo
                self.ShowinfoPage()

class Showinfo1(Screen):
#### Edit By RAED
        if isHD():
            skin = """
                <screen position="center,center" size="1280,720" title="Ncam Log Info" backgroundColor="#16000000" flags="wfNoBorder" >
                <widget source="Title" render="Label" position="0,2" size="380,35" zPosition="3" halign="center" valign="center" font="Play;33" backgroundColor="#20000000" transparent="1" foregroundColor="#bab329"/>
                <eLabel text="Move Up/Down or Left/Right to move list/page" position="430,2" size="900,35" font="Play;33" halign="center" valign="center" foregroundColor="#FC0000" backgroundColor="#16000000" zPosition="2"/>
                <widget name="Showinfo" position="15,40" size="1255,668" font="Play;24" valign="left" halign="left" transparent="1"/>
                </screen>"""
        else:
            skin = """
                <screen position="center,center" size="1920,1080" title="Ncam Log Info" backgroundColor="#16000000" flags="wfNoBorder" >
                <widget source="Title" render="Label" position="0,2" size="700,55" zPosition="3" halign="center" valign="center" font="Play;50" backgroundColor="#20000000" transparent="1" foregroundColor="#bab329"/>
                <eLabel text="Move Up/Down or Left/Right to move list/page" position="700,2" size="1200,55" font="Play;50" halign="center" valign="center" foregroundColor="#FC0000" backgroundColor="#16000000" zPosition="2"/>
                <widget name="Showinfo" position="15,70" size="1920,980" font="Play;35" valign="left" halign="left" transparent="1"/>
                </screen>"""
### End
        def __init__(self, session):
                Screen.__init__(self, session)
                self.skin = Showinfo1.skin
                self.setTitle("Ncam Log Info Details")
                global infofile
                global info_topline
                info_topline=0
                global info_bottomline
                infofile = "/tmp/ncam.log"
                f = open(infofile,"r")                   
                info_bottomline=1
                line=f.readline()
                print(line)
                while (line):
                        if len(line) > 1:
                                info_bottomline=info_bottomline+1     
                        line=f.readline()
                        print(line)
                f.close()
                if info_bottomline < info_lines_Showinfo1:
                        info_topline=0
                        info_bottomline=info_lines_Showinfo1
                self["Showinfo"] = MultiColorLabel("\n")
                self.ShowinfoPage()
                self.pagebackward                                                                      
                self["setupActions"] = ActionMap([ "ColorActions", "SetupActions", "InfobarMovieListActions" ],                         
                        {                                                                                    
                        "red": self.cancel,
                        "cancel": self.cancel,
                        "ok": self.cancel,
                        "left": self.pagebackward,
                        "right": self.pageforward,
                        "up": self.backward,
                        "down": self.forward,
                        })                                                                                   

        def setWindowTitle(self):
                self.setTitle(_("Display info logfile %s") % infofile)

        def ShowinfoPage(self):                                                                     
                        global info_topline
                        global info_bottomline
                        global info_lines_Showinfo1
                        global infofile
                        f = open(infofile,"r")               
                        infotext = ""                            
                        i=0
                        while i<(info_topline+info_lines_Showinfo1):
                                if i>(info_topline-1):
                                        text=f.readline()
                                        if len(text) > 1:
                                                infotext = infotext+text                           
                                else:
                                        text=f.readline()
                                i=i+1
                        f.close
                        self["Showinfo"].setText(infotext)    

        def cancel(self):
                self.close(False)

        def backward(self):      
                global info_topline
                global info_lines_Showinfo1
                info_topline=info_topline-1
                if info_topline<0:
                        info_topline=0
                self.ShowinfoPage()

        def forward(self):      
                global info_topline
                info_topline=info_topline+1
                if info_topline>info_bottomline-info_lines_Showinfo1:
                        info_topline=info_bottomline-info_lines_Showinfo1
                self.ShowinfoPage()

        def pagebackward(self):      
                global info_topline
                global info_lines_Showinfo1
                info_topline=info_topline-info_lines_Showinfo1
                if info_topline<0:
                        info_topline=0
                self.ShowinfoPage()

        def pageforward(self):      
                global info_topline
                global info_bottomline
                global info_lines_Showinfo1
                info_topline=info_topline+info_lines_Showinfo1
                if info_topline>info_bottomline-info_lines_Showinfo1:
                        info_topline=info_bottomline-info_lines_Showinfo1
                self.ShowinfoPage()

class Showinfo2(Screen):
        if isHD():
            skin = """
                <screen position="0,0" size="1280,720" title="Schedule to football matchs this week" backgroundColor="#16000000" flags="wfNoBorder">
                      <widget source="Title" render="Label" position="12,7" size="600,32" font="Play;28" backgroundColor="#16000000" foregroundColor="#FFE375" valign="center" halign="center" zPosition="2"/>
                      <eLabel text="Move Up/Down or Left/Right to move list/page" position="600,7" size="680,32" font="Play;28" foregroundColor="#FC0000" backgroundColor="#16000000" zPosition="2"/>
                      <widget name="Showinfo" position="28,84" size="1229,635" font="Play;26" backgroundColor="#16000000" foregroundColor="#00ffffff"/>

                      <eLabel text="Date" position="10,44" size="150,32" font="Play;26" valign="center" backgroundColor="#00666666" halign="center" zPosition="3"/>
                      <eLabel text="Time" position="158,44" size="100,32" font="Play;26" valign="center" backgroundColor="#00666666" halign="center" zPosition="3"/>
                      <eLabel text="Matche" position="300,44" size="150,32" font="Play;26" valign="center" backgroundColor="#00666666" halign="center" zPosition="4"/>
                      <eLabel name="Top_Background" position="0,44" size="1280,34" backgroundColor="#00666666" zPosition="2"/>
                      <eLabel name="Ver1_Long" position="165,45" size="5,665" backgroundColor="#00666666" zPosition="3"/>
                      <eLabel name="Ver2_Long" position="253,45" size="5,665" backgroundColor="#00666666" zPosition="3"/>
                      <eLabel name="Ver1_short" position="165,45" size="5,32" backgroundColor="#16000000" zPosition="4"/>
                      <eLabel name="Ver2_short" position="253,45" size="5,32" backgroundColor="#16000000" zPosition="4"/>
                      <!--eLabel name="Top" position="0,44" size="1280,5" backgroundColor="#00666666" zPosition="3"/>
                      <eLabel name="Down" position="0,709" size="1280,5" backgroundColor="#00666666" zPosition="3"/-->
                </screen>"""
        else:
           skin = """
                <screen position="0,0" size="1920,1080" title="Schedule to football matchs this week" backgroundColor="#16000000" flags="wfNoBorder">
                      <widget source="Title" render="Label" position="20,3" size="900,50" font="Play;40" backgroundColor="#16000000" foregroundColor="#FFE375" valign="center" halign="center" zPosition="2"/>
                      <eLabel text="Move Up/Down or Left/Right to move list/page" position="895,3" size="1000,50" font="Play;45" foregroundColor="#FC0000" backgroundColor="#16000000" zPosition="2" valign="center" halign="center"/>
                      <widget name="Showinfo" position="39,115" size="1835,960" font="Play;38" backgroundColor="#16000000" foregroundColor="#00ffffff"/>

                      <eLabel text="Date" position="15,60" size="230,50" font="Play;40" backgroundColor="#00666666" valign="center" halign="center" zPosition="3"/>
                      <eLabel text="Time" position="265,60" size="100,50" font="Play;40" backgroundColor="#00666666" valign="center" halign="center" zPosition="3"/>
                      <eLabel text="Matche" position="440,60" size="320,50" font="Play;40" backgroundColor="#00666666" valign="center" halign="center" zPosition="3"/>
                      <eLabel name="Top_Background" position="0,60" size="1920,50" backgroundColor="#00666666" zPosition="2"/>
                      <eLabel name="Ver1_Long" position="250,60" size="10,1100" backgroundColor="#00666666" zPosition="3"/>
                      <eLabel name="Ver2_Long" position="378,60" size="10,1100" backgroundColor="#00666666" zPosition="3"/>
                      <eLabel name="Ver1_short" position="250,60" size="10,50" backgroundColor="#16000000" zPosition="4"/>
                      <eLabel name="Ver2_short" position="378,60" size="10,50" backgroundColor="#16000000" zPosition="4"/>
                      <!--eLabel name="Top" position="0,64" size="1920,10" backgroundColor="#00666666" zPosition="3"/>
                      <eLabel name="Down" position="0,1055" size="1920,10" backgroundColor="#00666666" zPosition="3"/-->
                </screen>"""

        def __init__(self, session):
                Screen.__init__(self, session)
                self.setTitle("Schedule to football matchs this week")
                self.skin = Showinfo2.skin
                global infofile
                global info_topline
                info_topline=0
                global info_bottomline
                infofile = "/tmp/freeservre80"
                f = open(infofile,"r")  
                info_bottomline=1
                line=f.readline()
                print(line)
                while (line):
                        if len(line) > 1:
                                info_bottomline=info_bottomline+1
                        line=f.readline()
                        print(line)
                f.close()
                if info_bottomline < info_lines_Showinfo2:
                        info_topline=0
                        info_bottomline=info_lines_Showinfo2
                self["Showinfo"] = MultiColorLabel("\n")
                self.ShowinfoPage()
                self.pagebackward                                                                      
                self["setupActions"] = ActionMap([ "ColorActions", "SetupActions", "InfobarMovieListActions" ],                         
                        {                                                                                    
                        "red": self.cancel,                                                                  
                        "cancel": self.cancel,                                                               
                        "ok": self.cancel,                                                                     
                        "left": self.pagebackward,                                                                           
                        "right": self.pageforward,                                                                       
                        "up": self.backward,                                                                           
                        "down": self.forward,                                                                       
                        })                                                                                   

        def setWindowTitle(self):
                self.setTitle(_("Display info logfile %s") % infofile)

        def ShowinfoPage(self):                                                                     
                        global info_topline
                        global info_bottomline
                        global info_lines_Showinfo2
                        global infofile
                        f = open(infofile,"r")               
                        infotext = ""                            
                        i=0
                        while i<(info_topline+info_lines_Showinfo2):
                                if i>(info_topline-1):
                                        text=f.readline()
                                        if len(text) > 1:
                                                infotext = infotext+text                           
                                else:
                                        text=f.readline()
                                i=i+1
                        f.close
                        self["Showinfo"].setText(infotext)    

        def cancel(self):
                self.close(False)

        def backward(self):      
                global info_topline
                global info_lines_Showinfo2
                info_topline=info_topline-1
                if info_topline<0:
                        info_topline=0
                self.ShowinfoPage()

        def forward(self):      
                global info_topline
                info_topline=info_topline+1
                if info_topline>info_bottomline-info_lines_Showinfo2:
                        info_topline=info_bottomline-info_lines_Showinfo2
                self.ShowinfoPage()

        def pagebackward(self):      
                global info_topline
                global info_lines_Showinfo2
                info_topline=info_topline-info_lines_Showinfo2
                if info_topline<0:
                        info_topline=0
                self.ShowinfoPage()

        def pageforward(self):      
                global info_topline
                global info_bottomline
                global info_lines_Showinfo2
                info_topline=info_topline+info_lines_Showinfo2
                if info_topline>info_bottomline-info_lines_Showinfo2:
                        info_topline=info_bottomline-info_lines_Showinfo2
                self.ShowinfoPage()

               
class Showinfo3(Screen):
        def __init__(self, session):
                Screen.__init__(self, session)
                #self.setTitle("log Info")
                self.skin = Showinfo.skin
                global infofile
                global info_topline
                info_topline=0
                global info_bottomline
                infofile = "/tmp/freeservre78"
                f = open(infofile,"r")                   
                info_bottomline=1
                line=f.readline()
                print(line)
                while (line):
                        if len(line) > 1:
                                info_bottomline=info_bottomline+1     
                        line=f.readline()
                        print(line)
                f.close()
                if info_bottomline < info_lines:
                        info_topline=0
                        info_bottomline=info_lines
                self["Showinfo"] = MultiColorLabel("\n")
                self.ShowinfoPage()
                self.pagebackward                                                                      
                self["setupActions"] = ActionMap([ "ColorActions", "SetupActions", "InfobarMovieListActions" ],                         
                        {                                                                                    
                        "red": self.cancel,                                                                  
                        "cancel": self.cancel,                                                               
                        "ok": self.cancel,                                                                     
                        "left": self.pagebackward,                                                                           
                        "right": self.pageforward,                                                                       
                        "up": self.backward,                                                                           
                        "down": self.forward,                                                                       
                        })                                                                                   

        def setWindowTitle(self):
                self.setTitle(_("Display info logfile %s") % infofile)

        def ShowinfoPage(self):                                                                     
                        global info_topline
                        global info_bottomline
                        global info_lines
                        global infofile
                        f = open(infofile,"r")               
                        infotext = ""                            
                        i=0
                        while i<(info_topline+info_lines):
                                if i>(info_topline-1):
                                        text=f.readline()
                                        if len(text) > 1:
                                                infotext = infotext+text                           
                                else:
                                        text=f.readline()
                                i=i+1
                        f.close
                        self["Showinfo"].setText(infotext)    

        def cancel(self):
                self.close(False)

        def backward(self):      
                global info_topline
                global info_lines
                info_topline=info_topline-1
                if info_topline<0:
                        info_topline=0
                self.ShowinfoPage()

        def forward(self):      
                global info_topline
                info_topline=info_topline+1
                if info_topline>info_bottomline-info_lines:
                        info_topline=info_bottomline-info_lines
                self.ShowinfoPage()

        def pagebackward(self):      
                global info_topline
                global info_lines
                info_topline=info_topline-info_lines
                if info_topline<0:
                        info_topline=0
                self.ShowinfoPage()

        def pageforward(self):      
                global info_topline
                global info_bottomline
                global info_lines
                info_topline=info_topline+info_lines
                if info_topline>info_bottomline-info_lines:
                        info_topline=info_bottomline-info_lines
                self.ShowinfoPage()

class Showinfo4(Screen):
#### Edit By RAED
        if isHD():
            skin = """
                <screen position="center,center" size="1280,720" title="OScam Log Info" backgroundColor="#16000000" flags="wfNoBorder" >
                <widget source="Title" render="Label" position="0,2" size="380,35" zPosition="3" halign="center" valign="center" font="Play;33" backgroundColor="#20000000" transparent="1" foregroundColor="#bab329"/>
                <eLabel text="Move Up/Down or Left/Right to move list/page" position="430,2" size="900,35" font="Play;33" halign="center" valign="center" foregroundColor="#FC0000" backgroundColor="#16000000" zPosition="2"/>
                <widget name="Showinfo" position="15,40" size="1255,668" font="Play;24" valign="left" halign="left" transparent="1"/>
                </screen>"""
        else:
            skin = """
                <screen position="center,center" size="1920,1080" title="OScam Log Info" backgroundColor="#16000000" flags="wfNoBorder" >
                <widget source="Title" render="Label" position="0,2" size="700,55" zPosition="3" halign="center" valign="center" font="Play;50" backgroundColor="#20000000" transparent="1" foregroundColor="#bab329"/>
                <eLabel text="Move Up/Down or Left/Right to move list/page" position="700,2" size="1200,55" font="Play;50" halign="center" valign="center" foregroundColor="#FC0000" backgroundColor="#16000000" zPosition="2"/>
                <widget name="Showinfo" position="15,70" size="1920,980" font="Play;35" valign="left" halign="left" transparent="1"/>
                </screen>"""
### End
        def __init__(self, session):
                Screen.__init__(self, session)
                self.setTitle("OScam Log Info Details")
                self.skin = Showinfo4.skin
                global infofile
                global info_topline
                info_topline=0
                global info_bottomline
                infofile = "/tmp/oscam.log"
                f = open(infofile,"r")                   
                info_bottomline=1
                line=f.readline()
                print(line)
                while (line):
                        if len(line) > 1:
                                info_bottomline=info_bottomline+1     
                        line=f.readline()
                        print(line)
                f.close()
                if info_bottomline < info_lines_Showinfo1:
                        info_topline=0
                        info_bottomline=info_lines_Showinfo1
                self["Showinfo"] = MultiColorLabel("\n")
                self.ShowinfoPage()
                self.pagebackward                                                                      
                self["setupActions"] = ActionMap([ "ColorActions", "SetupActions", "InfobarMovieListActions" ],                         
                        {                                                                                    
                        "red": self.cancel,                                                                  
                        "cancel": self.cancel,                                                               
                        "ok": self.cancel,                                                                     
                        "left": self.pagebackward,                                                                           
                        "right": self.pageforward,                                                                       
                        "up": self.backward,                                                                           
                        "down": self.forward,                                                                       
                        })                                                                                   

        def setWindowTitle(self):
                self.setTitle(_("Display info logfile %s") % infofile)

        def ShowinfoPage(self):                                                                     
                        global info_topline
                        global info_bottomline
                        global info_lines_Showinfo1
                        global infofile
                        f = open(infofile,"r")               
                        infotext = ""                            
                        i=0
                        while i<(info_topline+info_lines_Showinfo1):
                                if i>(info_topline-1):
                                        text=f.readline()
                                        if len(text) > 1:
                                                infotext = infotext+text                           
                                else:
                                        text=f.readline()
                                i=i+1
                        f.close
                        self["Showinfo"].setText(infotext)    

        def cancel(self):
                self.close(False)

        def backward(self):      
                global info_topline
                global info_lines_Showinfo1
                info_topline=info_topline-1
                if info_topline<0:
                        info_topline=0
                self.ShowinfoPage()

        def forward(self):      
                global info_topline
                info_topline=info_topline+1
                if info_topline>info_bottomline-info_lines_Showinfo1:
                        info_topline=info_bottomline-info_lines_Showinfo1
                self.ShowinfoPage()

        def pagebackward(self):      
                global info_topline
                global info_lines_Showinfo1
                info_topline=info_topline-info_lines_Showinfo1
                if info_topline<0:
                        info_topline=0
                self.ShowinfoPage()

        def pageforward(self):      
                global info_topline
                global info_bottomline
                global info_lines_Showinfo1
                info_topline=info_topline+info_lines_Showinfo1
                if info_topline>info_bottomline-info_lines_Showinfo1:
                        info_topline=info_bottomline-info_lines_Showinfo1
                self.ShowinfoPage()
                
class Showinfo5(Screen):
#### Edit By RAED
        if isHD():
            skin = """
                <screen position="center,center" size="1280,720" title="Last Update Info Details" backgroundColor="#16000000" flags="wfNoBorder" >
                <widget source="Title" render="Label" position="0,2" size="380,35" zPosition="3" halign="center" valign="center" font="Play;33" backgroundColor="#20000000" transparent="1" foregroundColor="#bab329"/>
                <eLabel text="Move Up/Down or Left/Right to move list/page" position="430,2" size="900,35" font="Play;33" halign="center" valign="center" foregroundColor="#FC0000" backgroundColor="#16000000" zPosition="2"/>
                <widget name="Showinfo" position="15,40" size="1255,668" font="Play;24" valign="left" halign="left" backgroundColor="#16000000" transparent="1"/>
                </screen>"""
        else:
            skin = """
                <screen position="center,center" size="1920,1080" title="Last Update Info Details" backgroundColor="#16000000" flags="wfNoBorder" >
                <widget source="Title" render="Label" position="0,2" size="700,55" zPosition="3" halign="center" valign="center" font="Play;50" backgroundColor="#16000000" transparent="1" foregroundColor="#bab329"/>
                <eLabel text="Move Up/Down or Left/Right to move list/page" position="700,2" size="1200,55" font="Play;50" halign="center" valign="center" foregroundColor="#FC0000" backgroundColor="#16000000" zPosition="2"/>
                <widget name="Showinfo" position="15,70" size="1920,966" font="Play;35" valign="left" halign="left" backgroundColor="#16000000"  transparent="1"/>
                </screen>"""
### End
        def __init__(self, session):
                Screen.__init__(self, session)
                self.setTitle("Last Update Info Details")
                self.skin = Showinfo5.skin
                global infofile
                global info_topline
                info_topline=0
                global info_bottomline
                infofile = "/tmp/freeservre88"
                f = open(infofile,"r")                   
                info_bottomline=1
                line=f.readline()
                print(line)
                while (line):
                        if len(line) > 1:
                                info_bottomline=info_bottomline+1     
                        line=f.readline()
                        print(line)
                f.close()
                if info_bottomline < info_lines_Showinfo5:
                        info_topline=0
                        info_bottomline=info_lines_Showinfo5
                self["Showinfo"] = MultiColorLabel("\n")
                self.ShowinfoPage()
                self.pagebackward                                                                      
                self["setupActions"] = ActionMap([ "ColorActions", "SetupActions", "InfobarMovieListActions" ],                         
                        {                                                                                    
                        "red": self.cancel,                                                                  
                        "cancel": self.cancel,                                                               
                        "ok": self.cancel,                                                                     
                        "left": self.pagebackward,                                                                           
                        "right": self.pageforward,                                                                       
                        "up": self.backward,                                                                           
                        "down": self.forward,                                                                       
                        })                                                                                   

        def setWindowTitle(self):
                self.setTitle(_("Display info logfile %s") % infofile)

        def ShowinfoPage(self):                                                                     
                        global info_topline
                        global info_bottomline
                        global info_lines_Showinfo5
                        global infofile
                        f = open(infofile,"r")               
                        infotext = ""                            
                        i=0
                        while i<(info_topline+info_lines_Showinfo5):
                                if i>(info_topline-1):
                                        text=f.readline()
                                        if len(text) > 1:
                                                infotext = infotext+text                           
                                else:
                                        text=f.readline()
                                i=i+1
                        f.close
                        self["Showinfo"].setText(infotext)    

        def cancel(self):
                self.close(False)

        def backward(self):      
                global info_topline
                global info_lines_Showinfo5
                info_topline=info_topline-1
                if info_topline<0:
                        info_topline=0
                self.ShowinfoPage()

        def forward(self):      
                global info_topline
                info_topline=info_topline+1
                if info_topline>info_bottomline-info_lines_Showinfo5:
                        info_topline=info_bottomline-info_lines_Showinfo5
                self.ShowinfoPage()

        def pagebackward(self):      
                global info_topline
                global info_lines_Showinfo5
                info_topline=info_topline-info_lines_Showinfo5
                if info_topline<0:
                        info_topline=0
                self.ShowinfoPage()

        def pageforward(self):      
                global info_topline
                global info_bottomline
                global info_lines_Showinfo5
                info_topline=info_topline+info_lines_Showinfo5
                if info_topline>info_bottomline-info_lines_Showinfo5:
                        info_topline=info_bottomline-info_lines_Showinfo5
                self.ShowinfoPage()
                
class Showinfo6(Screen):
#### Edit By RAED
        if isHD():
            skin = """
                <screen position="center,center" size="1280,720" title="Last Update Info Details" backgroundColor="#16000000" flags="wfNoBorder" >
                <widget source="Title" render="Label" position="0,2" size="380,35" zPosition="3" halign="center" valign="center" font="Play;33" backgroundColor="#20000000" transparent="1" foregroundColor="#bab329"/>
                <eLabel text="Move Up/Down or Left/Right to move list/page" position="430,2" size="900,35" font="Play;33" halign="center" valign="center" foregroundColor="#FC0000" backgroundColor="#16000000" zPosition="2"/>
                <widget name="Showinfo" position="15,40" size="1255,668" font="Play;24" valign="left" halign="left" backgroundColor="#16000000" transparent="1"/>
                </screen>"""
        else:
            skin = """
                <screen position="center,center" size="1920,1080" title="Last Update Info Details" backgroundColor="#16000000" flags="wfNoBorder" >
                <widget source="Title" render="Label" position="0,2" size="700,55" zPosition="3" halign="center" valign="center" font="Play;50" backgroundColor="#16000000" transparent="1" foregroundColor="#bab329"/>
                <eLabel text="Move Up/Down or Left/Right to move list/page" position="700,2" size="1200,55" font="Play;50" halign="center" valign="center" foregroundColor="#FC0000" backgroundColor="#16000000" zPosition="2"/>
                <widget name="Showinfo" position="15,70" size="1920,966" font="Play;35" valign="left" halign="left" backgroundColor="#16000000"  transparent="1"/>
                </screen>"""
### End
        def __init__(self, session):
                Screen.__init__(self, session)
                self.setTitle("Last Update Info Details")
                self.skin = Showinfo5.skin
                global infofile
                global info_topline
                info_topline=0
                global info_bottomline
                infofile = "/tmp/freeservre88"
                f = open(infofile,"r")                   
                info_bottomline=1
                line=f.readline()
                print(line)
                while (line):
                        if len(line) > 1:
                                info_bottomline=info_bottomline+1     
                        line=f.readline()
                        print(line)
                f.close()
                if info_bottomline < info_lines_Showinfo5:
                        info_topline=0
                        info_bottomline=info_lines_Showinfo5
                self["Showinfo"] = MultiColorLabel("\n")
                self.ShowinfoPage()
                self.pagebackward                                                                      
                self["setupActions"] = ActionMap([ "ColorActions", "SetupActions", "InfobarMovieListActions" ],                         
                        {                                                                                    
                        "red": self.cancel,                                                                  
                        "cancel": self.cancel,                                                               
                        "ok": self.cancel,                                                                     
                        "left": self.pagebackward,                                                                           
                        "right": self.pageforward,                                                                       
                        "up": self.backward,                                                                           
                        "down": self.forward,                                                                       
                        })                                                                                   

        def setWindowTitle(self):
                self.setTitle(_("Display info logfile %s") % infofile)

        def ShowinfoPage(self):                                                                     
                        global info_topline
                        global info_bottomline
                        global info_lines_Showinfo5
                        global infofile
                        f = open(infofile,"r")               
                        infotext = ""                            
                        i=0
                        while i<(info_topline+info_lines_Showinfo5):
                                if i>(info_topline-1):
                                        text=f.readline()
                                        if len(text) > 1:
                                                infotext = infotext+text                           
                                else:
                                        text=f.readline()
                                i=i+1
                        f.close
                        self["Showinfo"].setText(infotext)    

        def cancel(self):
                self.close(False)

        def backward(self):      
                global info_topline
                global info_lines_Showinfo5
                info_topline=info_topline-1
                if info_topline<0:
                        info_topline=0
                self.ShowinfoPage()

        def forward(self):      
                global info_topline
                info_topline=info_topline+1
                if info_topline>info_bottomline-info_lines_Showinfo5:
                        info_topline=info_bottomline-info_lines_Showinfo5
                self.ShowinfoPage()

        def pagebackward(self):      
                global info_topline
                global info_lines_Showinfo5
                info_topline=info_topline-info_lines_Showinfo5
                if info_topline<0:
                        info_topline=0
                self.ShowinfoPage()

        def pageforward(self):      
                global info_topline
                global info_bottomline
                global info_lines_Showinfo5
                info_topline=info_topline+info_lines_Showinfo5
                if info_topline>info_bottomline-info_lines_Showinfo5:
                        info_topline=info_bottomline-info_lines_Showinfo5
                self.ShowinfoPage()
                
class Showinfo7(Screen):
        if isHD():
            skin = """
                <screen position="0,0" size="1280,720" title="Programme TV TNT Tonight" backgroundColor="#16000000" flags="wfNoBorder">
                      <widget source="Title" render="Label" position="12,7" size="600,32" font="Play;28" backgroundColor="#16000000" foregroundColor="#FFE375" valign="center" halign="center" zPosition="2"/>
                      <eLabel text="Move Up/Down or Left/Right to move list/page" position="600,7" size="680,32" font="Play;28" foregroundColor="#FC0000" backgroundColor="#16000000" zPosition="2"/>
                      <widget name="Showinfo" position="35,84" size="1229,635" font="Play;26" backgroundColor="#16000000" foregroundColor="#00ffffff"/>

                      <eLabel text="Time" position="0,44" size="150,32" font="Play;26" valign="center" backgroundColor="#00666666" halign="center" zPosition="3"/>
                      <eLabel text="Channel" position="135,44" size="150,32" font="Play;26" valign="center" backgroundColor="#00666666" halign="center" zPosition="3"/>
                      <eLabel text="Title" position="530,44" size="150,32" font="Play;26" valign="center" backgroundColor="#00666666" halign="center" zPosition="4"/>
                      <eLabel name="Top_Background" position="0,44" size="1280,34" backgroundColor="#00666666" zPosition="2"/>
                      <eLabel name="Ver1_Long" position="120,45" size="5,665" backgroundColor="#00666666" zPosition="3"/>
                      <eLabel name="Ver2_Long" position="438,45" size="5,665" backgroundColor="#00666666" zPosition="3"/>
                      <eLabel name="Ver1_short" position="120,45" size="5,32" backgroundColor="#16000000" zPosition="4"/>
                      <eLabel name="Ver2_short" position="438,45" size="5,32" backgroundColor="#16000000" zPosition="4"/>
                      <!--eLabel name="Top" position="0,44" size="1280,5" backgroundColor="#00666666" zPosition="3"/>
                      <eLabel name="Down" position="0,709" size="1280,5" backgroundColor="#00666666" zPosition="3"/-->
                </screen>"""
        else:
           skin = """
                <screen position="0,0" size="1920,1080" title="Programme TV TNT Tonight" backgroundColor="#16000000" flags="wfNoBorder">
                      <widget source="Title" render="Label" position="20,3" size="900,50" font="Play;40" backgroundColor="#16000000" foregroundColor="#FFE375" valign="center" halign="center" zPosition="2"/>
                      <eLabel text="Move Up/Down or Left/Right to move list/page" position="895,3" size="1000,50" font="Play;45" foregroundColor="#FC0000" backgroundColor="#16000000" zPosition="2" valign="center" halign="center"/>
                      <widget name="Showinfo" position="50,115" size="1835,960" font="Play;38" backgroundColor="#16000000" foregroundColor="#00ffffff"/>

                      <eLabel text="Time" position="0,60" size="230,50" font="Play;40" backgroundColor="#00666666" valign="center" halign="center" zPosition="3"/>
                      <eLabel text="Channel" position="235,60" size="250,50" font="Play;40" backgroundColor="#00666666" valign="center" halign="center" zPosition="3"/>
                      <eLabel text="Title" position="600,60" size="320,50" font="Play;40" backgroundColor="#00666666" valign="center" halign="center" zPosition="3"/>
                      <eLabel name="Top_Background" position="0,60" size="1920,50" backgroundColor="#00666666" zPosition="2"/>
                      <eLabel name="Ver1_Long" position="180,60" size="10,1100" backgroundColor="#00666666" zPosition="3"/>
                      <eLabel name="Ver2_Long" position="642,60" size="10,1100" backgroundColor="#00666666" zPosition="3"/>
                      <eLabel name="Ver1_short" position="180,60" size="10,50" backgroundColor="#16000000" zPosition="4"/>
                      <eLabel name="Ver2_short" position="642,60" size="10,50" backgroundColor="#16000000" zPosition="4"/>
                      <!--eLabel name="Top" position="0,64" size="1920,10" backgroundColor="#00666666" zPosition="3"/>
                      <eLabel name="Down" position="0,1055" size="1920,10" backgroundColor="#00666666" zPosition="3"/-->
                </screen>"""

        def __init__(self, session):
                Screen.__init__(self, session)
                self.setTitle("Programme TV TNT Tonight")
                self.skin = Showinfo7.skin
                global infofile
                global info_topline
                info_topline=0
                global info_bottomline
                infofile = "/tmp/freeservre90"
                f = open(infofile,"r")
                info_bottomline=1
                line=f.readline()
                print(line)
                while (line):
                        if len(line) > 1:
                                info_bottomline=info_bottomline+1
                        line=f.readline()
                        print(line)
                f.close()
                if info_bottomline < info_lines_Showinfo7:
                        info_topline=0
                        info_bottomline=info_lines_Showinfo7
                self["Showinfo"] = MultiColorLabel("\n")
                self.ShowinfoPage()
                self.pagebackward                                                                      
                self["setupActions"] = ActionMap([ "ColorActions", "SetupActions", "InfobarMovieListActions" ],                         
                        {                                                                                    
                        "red": self.cancel,                                                                  
                        "cancel": self.cancel,                                                               
                        "ok": self.cancel,                                                                     
                        "left": self.pagebackward,                                                                           
                        "right": self.pageforward,                                                                       
                        "up": self.backward,                                                                           
                        "down": self.forward,                                                                       
                        })                                                                                   

        def setWindowTitle(self):
                self.setTitle(_("Display info logfile %s") % infofile)

        def ShowinfoPage(self):                                                                     
                        global info_topline
                        global info_bottomline
                        global info_lines_Showinfo7
                        global infofile
                        f = open(infofile,"r")
                        infotext = ""                            
                        i=0
                        while i<(info_topline+info_lines_Showinfo7):
                                if i>(info_topline-1):
                                        text=f.readline().replace('&#039;','')
                                        if len(text) > 1:
                                                infotext = infotext+text                           
                                else:
                                        text=f.readline().replace('&#039;','')
                                i=i+1
                        f.close
                        self["Showinfo"].setText(infotext)    

        def cancel(self):
                self.close(False)

        def backward(self):      
                global info_topline
                global info_lines_Showinfo7
                info_topline=info_topline-1
                if info_topline<0:
                        info_topline=0
                self.ShowinfoPage()

        def forward(self):      
                global info_topline
                info_topline=info_topline+1
                if info_topline>info_bottomline-info_lines_Showinfo7:
                        info_topline=info_bottomline-info_lines_Showinfo7
                self.ShowinfoPage()

        def pagebackward(self):      
                global info_topline
                global info_lines_Showinfo7
                info_topline=info_topline-info_lines_Showinfo7
                if info_topline<0:
                        info_topline=0
                self.ShowinfoPage()

        def pageforward(self):      
                global info_topline
                global info_bottomline
                global info_lines_Showinfo7
                info_topline=info_topline+info_lines_Showinfo7
                if info_topline>info_bottomline-info_lines_Showinfo7:
                        info_topline=info_bottomline-info_lines_Showinfo7
                self.ShowinfoPage()
        
