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
from Components.ActionMap import ActionMap, NumberActionMap
from Components.config import config, configfile, ConfigInteger, ConfigPassword, ConfigSelection, ConfigSubsection, ConfigText, getConfigListEntry
from Components.ConfigList import ConfigListScreen
from Components.Label import Label
from Components.MenuList import MenuList
from Components.MultiContent import MultiContentEntryText
from Components.Slider import Slider
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
######################################################################################################
plugin_path = '/usr/lib/enigma2/python/Plugins/Extensions/FreeServer/fonts'
skin_path = '/usr/lib/enigma2/python/Plugins/Extensions/FreeServer/Skin/'
p_path = '/usr/lib/enigma2/python/Plugins/Extensions/FreeServer'   
from enigma import addFont
try:
    addFont('%s/bpmono.ttf' % plugin_path, 'bpmo', 100, 1)
    #addFont('%s/Sans.ttf' % plugin_path, 'Sans', 100, 1)
    #addFont('%s/PlayfairDisplay-Black.otf' % plugin_path, 'Play', 100, 1)
    #addFont('%s/slyk-medium.ttf' % plugin_path, 'slyk', 100, 1)
except Exception as ex:
    print(ex)
#########################################################################################################
global info_lines                               
info_lines=15                  
global info_bottomline                                
info_bottomline=0          
global info_topline                                
info_topline=0          
global infofile
version = '8.3.8 by mino60'
#########################################################################################################
class MyStatus(Screen):
        skin = """\n\t\t\t\t<screen position="center,center" size="425,425" title=" " >\n\t\t\t\t\t<ePixmap position="0,0" size="425,425" pixmap="/usr/lib/enigma2/python/Plugins/Extensions/FreeServer/Deco/info.png" zPosition="1"/>\n\t\t\t\t\t<widget name="label" position="10,100" size="425,325" font="bpmo;20" valign="left" halign="left" foregroundColor="#FFFFFF" backgroundColor="#000000" transparent="1" zPosition="2" />\n\t\t\t\t</screen>"""


        def __init__(self, session):
                Screen.__init__(self, session)
                self.skin = MyStatus.skin
                self.version =  version
                self.setTitle('FreeServer %s' % self.version)
                #self.setTitle('PayPal Info')
                #self["label"] = label()        
                global infofile
                global info_topline
                info_topline=0
                global info_bottomline
                infofile = "/usr/lib/enigma2/python/Plugins/Extensions/FreeServer/config/status.txt"
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
                self["MyStatus"] = MultiColorLabel("\n")
                self.MyStatusPage()
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
                self['label'] = Label('\n\nDo you like the plugin?\nWould you like to support development and make a donation?\nPlease proceed as follows:\n1. Log in to PayPal\n2. Click on: send money\n3. Send money to your friends and family\n4. E-mail address: aminovitch1187@yahoo.com\n5. Amount: 5 euro\n6. Send money\nOr go to the next link: http://bit.ly/2Piar1L\nhttp://bit.ly/2Piar1L\nThank you!')
        def setWindowTitle(self):
                self.setTitle(_("Display info logfile %s") % infofile)

        def MyStatusPage(self):                                                                     
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
                        self["MyStatus"].setText(infotext)    

        def cancel(self):
                self.close(False)

        def backward(self):      
                global info_topline
                global info_lines
                info_topline=info_topline-1
                if info_topline<0:
                        info_topline=0
                self.statusPage()

        def forward(self):      
                global info_topline
                info_topline=info_topline+1
                if info_topline>info_bottomline-info_lines:
                        info_topline=info_bottomline-info_lines
                self.MyStatusPage()

        def pagebackward(self):      
                global info_topline
                global info_lines
                info_topline=info_topline-info_lines
                if info_topline<0:
                        info_topline=0
                self.oscamstatusPage()

        def pageforward(self):      
                global info_topline
                global info_bottomline
                global info_lines
                info_topline=info_topline+info_lines
                if info_topline>info_bottomline-info_lines:
                        info_topline=info_bottomline-info_lines
                self.MyStatusPage()

 
