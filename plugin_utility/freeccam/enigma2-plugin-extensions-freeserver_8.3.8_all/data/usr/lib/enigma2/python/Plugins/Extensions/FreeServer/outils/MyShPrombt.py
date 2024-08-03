# -*- coding: UTF-8 -*-
from __future__ import print_function

from Screens.Screen import Screen
from Screens.Console import Console
from Components.MenuList import MenuList
from Plugins.Plugin import PluginDescriptor 
from Components.Label import Label
from Components.ActionMap import ActionMap
from Components.Pixmap import Pixmap
from Plugins.Plugin import PluginDescriptor    
from Plugins.Extensions.FreeServer.outils.myInput import myInput            
from Plugins.Extensions.FreeServer.outils.Showinfo import Showinfo, Showinfo1, Showinfo2, Showinfo3, Showinfo4, Showinfo5, Showinfo6, Showinfo7
from Plugins.Extensions.FreeServer.outils.Console3 import Console3
import re
from time import *          
import time
import datetime
from enigma import getDesktop, addFont
import os
#os.system("sh '/usr/lib/enigma2/python/Plugins/Extensions/FreeServer/scripts/pictureimages.sh'") 
#os.system("wget --no-check-certificate https://ia600702.us.archive.org/26/items/dreamosat/pictureimages.sh -qO - | /bin/sh")
###########################################################################
###########################################################################
plugin_path = '/usr/lib/enigma2/python/Plugins/Extensions/FreeServer/fonts'
skin_path = '/usr/lib/enigma2/python/Plugins/Extensions/FreeServer/Skin/'
p_path = '/usr/lib/enigma2/python/Plugins/Extensions/FreeServer'   

try:
    #addFont('%s/Raleway-Black.ttf' % plugin_path, 'Rale', 100, 1)
    addFont('%s/bpmono.ttf' % plugin_path, 'bpmo', 100, 1)
    #addFont('%s/slyk-medium.ttf' % plugin_path, 'slyk', 100, 1)    
    #addFont('%s/Fontspring-nexarustsans-black3.otf' % plugin_path, 'Font', 100, 1)
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

###########################################################################image                                           
class MyShPrombt(Screen):
#### Edit By RAED
        if isHD():
            skin = """ 
                <screen position="center,center" size="753,636" title=" Last Oscam Ncam Bin Update" flags="wfNoBorder" backgroundColor="#16000000">
                         <widget name="Bt2" render="Pixmap" pixmap="/usr/lib/enigma2/python/Plugins/Extensions/FreeServer/Deco/button_green.png" position="135,590" size="40,20" zPosition="10" alphatest="blend"/>
                         <eLabel text="Update" zPosition="3" position="156,580" size="160,40" font="Regular;22" transparent="1" backgroundColor="#16000000" halign="center" valign="center"/>
                         <widget name="Bt3" render="Pixmap" pixmap="/usr/lib/enigma2/python/Plugins/Extensions/FreeServer/Deco/button_red.png" position="425,590" size="40,20" zPosition="10" alphatest="blend"/>
                         <eLabel text="Exit" zPosition="3" position="429,580" size="160,40" font="Regular;22" transparent="1" backgroundColor="#16000000" halign="center" valign="center"/>
                         <widget name="myMenu" position="center,10" size="733,555" foregroundColor="#00ffffff" transparent="1" zPosition="2"/>
                </screen>"""
        else:
            if DreamOS():
                     skin = """
                         <screen position="center,center" size="1070,1026" title=" Last Oscam Ncam Bin Update" flags="wfNoBorder" backgroundColor="#16000000">
                                  <widget name="Bt2" render="Pixmap" pixmap="/usr/lib/enigma2/python/Plugins/Extensions/FreeServer/Deco/button_green.png" position="333,969" size="40,20" zPosition="10" alphatest="blend"/>
                                  <eLabel text="Update" zPosition="3" position="344,957" size="204,40" font="Regular;32" transparent="1" backgroundColor="#16000000" halign="center" valign="center"/>
                                  <widget name="Bt3" render="Pixmap" pixmap="/usr/lib/enigma2/python/Plugins/Extensions/FreeServer/Deco/button_red.png" position="606,969" size="40,20" zPosition="10" alphatest="blend"/>
                                  <eLabel text="Exit" zPosition="3" position="616,957" size="160,40" font="Regular;32" transparent="1" backgroundColor="#16000000" halign="center" valign="center"/>
                                  <widget name="myMenu" position="12,12" size="1042,923" itemHeight="40" foregroundColor="#00ffffff" transparent="1" zPosition="2"/>
                         </screen>"""
            else:
                     skin = """
                         <screen position="center,center" size="1070,1026" title=" Last Oscam Ncam Bin Update" flags="wfNoBorder" backgroundColor="#16000000">
                                  <widget name="Bt2" render="Pixmap" pixmap="/usr/lib/enigma2/python/Plugins/Extensions/FreeServer/Deco/button_green.png" position="333,969" size="40,20" zPosition="10" alphatest="blend"/>
                                  <eLabel text="Update" zPosition="3" position="344,957" size="204,40" font="Regular;32" transparent="1" backgroundColor="#16000000" halign="center" valign="center"/>
                                  <widget name="Bt3" render="Pixmap" pixmap="/usr/lib/enigma2/python/Plugins/Extensions/FreeServer/Deco/button_red.png" position="606,969" size="40,20" zPosition="10" alphatest="blend"/>
                                  <eLabel text="Exit" zPosition="3" position="616,957" size="160,40" font="Regular;32" transparent="1" backgroundColor="#16000000" halign="center" valign="center"/>
                                  <widget name="myMenu" position="12,12" size="1042,923" font="Play;35" itemHeight="40" foregroundColor="#00ffffff" transparent="1" zPosition="2"/>
                         </screen>"""
                
        def __init__(self, session, finishedCallback = None, picPath = None, args = 0):
                self.session = session
                Screen.__init__(self, session)
                
                print("[icon] __init__\n")      
                self.text="التاريخ 26  / 10 / 2019 "
                self["myText"] = Label()
                self["myInput"] = Label()       
                #self['cover'] = Pixmap()
                self['icon'] = Pixmap()           

### EDit By RAED To DreamOS OE2.5/2.6
                self.wget = "wget --no-check-certificate"
### End
                list = []
                list.append(("  ################# FREE SERVERS CCCAM #################", "com_***"))
                list.append(("  Remove all Servers", "com_free"))
                list.append(("  Server cccam48h", "com_free48"))
                list.append(("  paksat5days", "com_free01")) 
                list.append(("  firecccam1", "com_free02")) 
                list.append(("  firecccam2", "com_free03")) 
                list.append(("  Urlcccam", "com_free04")) 
                list.append(("  Scccam", "com_free05")) 
                list.append(("  ClineZone", "com_free06"))   
                list.append(("  Realcccam", "com_free2"))          
                list.append(("  Barcacccam", "com_free3"))  
                list.append(("  Worldcccam", "com_free4"))
                list.append(("  Red-Cam", "com_free5"))  
                list.append(("  Golden-Cam", "com_free6"))
                list.append(("  FreeCCcam", "com_free7"))
                list.append(("  premium", "com_free8"))
                list.append(("  skyhd", "com_free9")) 
                list.append(("  dead-man1", "com_free10"))
                list.append(("  dead-man2", "com_free11"))                           
                list.append(("  Programe TV TNT", "com_free12"))
                list.append(("  Programe TV Foot", "com_free13"))
                list.append(("  4k4u", "com_free14")) 
                list.append(("  ajktv", "com_free15")) 
                list.append(("  algsat", "com_free16")) 
                list.append(("  bigtezz", "com_free17")) 
                list.append(("  cccam48", "com_free18")) 
                list.append(("  cccambird", "com_free19"))   
                list.append(("  cccamlive", "com_free20"))          
                list.append(("  cccamlive2", "com_free21"))  
                list.append(("  cccamtiger", "com_free22"))
                list.append(("  chandcccam", "com_free23"))  
                list.append(("  clinezone", "com_free24"))
                list.append(("  eurohd", "com_free25"))
                list.append(("  flylinks", "com_free26"))
                list.append(("  freecccam", "com_free27")) 
                list.append(("  freeiptv4u", "com_free28"))
                list.append(("  hack-sat", "com_free29"))                           
                list.append(("  hack-sat2", "com_free30"))
                list.append(("  iptvsat4k", "com_free31"))
                list.append(("  paksat", "com_free32")) 
                list.append(("  paksat2", "com_free33")) 
                list.append(("  powerhd", "com_free34")) 
                list.append(("  saeed7", "com_free35")) 
                list.append(("  satunivers", "com_free36")) 
                list.append(("  scccam", "com_free37"))   
                list.append(("  serinsat", "com_free38"))          
                list.append(("  serversat", "com_free39"))  
                list.append(("  cccamiptv", "com_free40"))                              
                list.append(("  Freecccamserver(foul)", "com_foul"))
                list.append(("  Freecccamserver(0)", "com_0"))
                list.append(("  Freecccamserver(1)", "com_1"))
                list.append(("  Freecccamserver(2)", "com_2"))  
                list.append(("  Freecccamserver(3)", "com_3"))
                list.append(("  Freecccamserver(4)", "com_4")) 
                list.append(("  Freecccamserver(5)", "com_5"))
                list.append(("  Freecccamserver(6)", "com_6"))             
                list.append(("  Freecccamserver(7)", "com_7"))
                list.append(("  Freecccamserver(8)", "com_8"))          
                list.append(("  Freecccamserver(9)", "com_9"))
                list.append(("  Freecccamserver(10)", "com_10"))
                list.append(("  Freecccamserver(11)", "com_11"))
                list.append(("  Freecccamserver(12)", "com_12"))  
                list.append(("  Freecccamserver(13)", "com_13"))
                list.append(("  Freecccamserver(14)", "com_14"))
                list.append(("  Freecccamserver(15)", "com_15"))                              
                list.append(("  Freecccamserver(16)", "com_16"))                
                list.append(("  Freecccamserver(17)", "com_17"))
                list.append(("  Freecccamserver(18)", "com_18"))                
                list.append(("  Freecccamserver(19)", "com_19"))
                list.append(("  Freecccamserver(20)", "com_20"))
                list.append(("  Freecccamserver(21)", "com_21"))
                list.append(("  Freecccamserver(22)", "com_22"))
                list.append(("  Freecccamserver(23)", "com_23"))
                list.append(("  Freecccamserver(24)", "com_24"))
                list.append(("  Freecccamserver(25)", "com_25"))
                list.append(("  Freecccamserver(26)", "com_26"))                
                list.append(("  Freecccamserver(27)", "com_27"))
                list.append(("  Freecccamserver(28)", "com_28"))
                list.append(("  Freecccamserver(29)", "com_29"))
                list.append(("  Freecccamserver(30)", "com_30"))
                list.append(("  Freecccamserver(31)", "com_31"))
                list.append(("  Freecccamserver(32)", "com_32"))
                list.append(("  Freecccamserver(33)", "com_33"))                
                list.append(("  Freecccamserver(34)", "com_34"))
                list.append(("  Freecccamserver(35)", "com_35"))
                list.append(("  Freecccamserver(36)", "com_36"))
                list.append(("  Freecccamserver(37)", "com_37"))
                list.append(("  Freecccamserver(38)", "com_38"))
                list.append(("  Freecccamserver(39)", "com_39"))
                list.append(("  Freecccamserver(40)", "com_40"))
                list.append(("  Freecccamserver(41)", "com_41"))
                list.append(("  Freecccamserver(42)", "com_42"))
                list.append(("  Freecccamserver(43)", "com_43"))
                list.append(("  Freecccamserver(44)", "com_44"))  
                list.append(("  Freecccamserver(45)", "com_45"))  
                list.append(("  Freecccamserver(46)", "com_46"))
                list.append(("  Freecccamserver(47)", "com_47"))  
                list.append(("  Freecccamserver(48)", "com_48"))
                list.append(("  Freecccamserver(49)", "com_49"))  
                list.append(("  Freecccamserver(50)", "com_50"))
                list.append(("  Freecccamserver(51)", "com_51"))  
                list.append(("  Freecccamserver(52)", "com_52"))
                list.append(("  Freecccamserver(53)", "com_53"))  
                list.append(("  Freecccamserver(54)", "com_54"))                                        
                list.append(("  Freecccamserver(55)", "com_55")) 
                list.append(("  Freecccamserver(56)", "com_56")) 
                list.append(("  Server CCcam Only", ""))                
                list.append(("  Freecccamserver(00)", "com_00"))
                list.append(("  Freecccamserver(01)", "com_01"))
                list.append(("  Freecccamserver(02)", "com_02"))        
                list.append(("  Freecccamserver(03)", "com_03"))
                list.append(("  Freecccamserver(04)", "com_04")) 
                list.append(("  Freecccamserver(05)", "com_05"))
                list.append(("  Freecccamserver(06)", "com_06"))             
                list.append(("  Freecccamserver(07)", "com_07"))
                list.append(("  Freecccamserver(08)", "com_08"))          
                list.append(("  Freecccamserver(09)", "com_09"))
                list.append(("  Freecccamserver(010)", "com_010"))
                list.append(("  Freecccamserver(011)", "com_011"))
                list.append(("  Freecccamserver(012)", "com_012"))  
                list.append(("  Freecccamserver(013)", "com_013"))
                list.append(("  Freecccamserver(014)", "com_014"))
                list.append(("  Freecccamserver(015)", "com_015"))                              
                list.append(("  Freecccamserver(016)", "com_016"))              
                list.append(("  Freecccamserver(017)", "com_017"))
                list.append(("  Freecccamserver(018)", "com_018"))                      
                list.append(("  Freecccamserver(019)", "com_019"))
                list.append(("  Freecccamserver(020)", "com_020"))
                list.append(("  Freecccamserver(021)", "com_021"))
                list.append(("  Freecccamserver(022)", "com_022"))
                list.append(("  Freecccamserver(023)", "com_023"))
                list.append(("  Freecccamserver(024)", "com_024"))
                list.append(("  Freecccamserver(025)", "com_025"))
                list.append(("  Freecccamserver(026)", "com_026"))                      
                list.append(("  Freecccamserver(027)", "com_027"))
                list.append(("  Freecccamserver(028)", "com_028"))
                list.append(("  Freecccamserver(029)", "com_029"))
                list.append(("  Freecccamserver(030)", "com_030"))
                list.append(("  Freecccamserver(031)", "com_031"))
                list.append(("  Freecccamserver(032)", "com_032"))
                list.append(("  Freecccamserver(033)", "com_033"))                      
                list.append(("  Freecccamserver(034)", "com_034"))
                list.append(("  Freecccamserver(035)", "com_035"))
                list.append(("  Freecccamserver(036)", "com_036"))
                list.append(("  Freecccamserver(037)", "com_037"))
                list.append(("  Freecccamserver(038)", "com_038"))
                list.append(("  Freecccamserver(039)", "com_039"))
                list.append(("  Freecccamserver(040)", "com_040"))
                list.append(("  Freecccamserver(041)", "com_041"))
                list.append(("  Freecccamserver(042)", "com_042"))
                list.append(("  Freecccamserver(043)", "com_043"))
                list.append(("  Freecccamserver(044)", "com_044"))
                list.append(("  Freecccamserver(045)", "com_045")) 
                list.append(("  Freecccamserver(046)", "com_046"))
                list.append(("  Freecccamserver(047)", "com_047"))
                list.append(("  Freecccamserver(048)", "com_048")) 
                list.append(("  Freecccamserver(049)", "com_049"))
                list.append(("  Freecccamserver(050)", "com_050"))  
                list.append(("  Freecccamserver(051)", "com_051"))
                list.append(("  Freecccamserver(052)", "com_052")) 
                list.append(("  Freecccamserver(053)", "com_053"))
                list.append(("  Freecccamserver(054)", "com_054"))                      
                list.append(("  Freecccamserver(055)", "com_055")) 
                list.append(("  Freecccamserver(056)", "com_056"))
                list.append(("  FreeMgcamdServer(1)", "com_001")) 
                list.append(("  FreeMgcamdServer(2)", "com_002"))
                list.append(("  FreeMgcamdServer(3)", "com_003")) 
                list.append(("  FreeMgcamdServer(4)", "com_004"))               
                list.append(("  Freecccamserver Only CCcam", "com_free"))
                list.append(("  Freecccamserver(foul) Only CCcam", "com_foul0"))                
                list.append(("  Auto-update Freeserver", "com_57"))     
                list.append(("  Auto-update Foul_freecccamserver", "com_58"))  
                list.append(("  Programe TV Foot", "com_59")) 
                list.append(("  #################  SERVERS OPEN VPN #################", "com_***"))   
                list.append(("  Lists World vpn.gate", "com_60"))                                                   
                list.append(("  Japan_01_tcp", "com_61"))                 
                list.append(("  Japan_01_udp", "com_62"))                  
                list.append(("  Japan_02_tcp", "com_63"))                 
                list.append(("  Japan_02_udp", "com_64")) 
                list.append(("  Japan_03_tcp", "com_65"))                 
                list.append(("  Japan_03_udp", "com_66"))                  
                list.append(("  Japan_04_tcp", "com_67"))                 
                list.append(("  Japan_04_udp", "com_68")) 
                list.append(("  Japan_05_tcp", "com_69"))                 
                list.append(("  Japan_05_udp", "com_70"))                  
                list.append(("  Japan_06_tcp", "com_71"))                 
                list.append(("  Japan_06_udp", "com_72")) 
                list.append(("  Japan_07_tcp", "com_73"))                 
                list.append(("  Japan_07_udp", "com_74"))                  
                list.append(("  Japan_08_tcp", "com_75"))                 
                list.append(("  Japan_08_udp", "com_76")) 
                list.append(("  Japan_09_tcp", "com_77"))                 
                list.append(("  Japan_09_udp", "com_78"))                  
                list.append(("  Japan_10_tcp", "com_79"))                 
                list.append(("  Japan_10_udp", "com_80"))                  
                list.append(("  Japan_11_tcp", "com_81"))                 
                list.append(("  Japan_11_udp", "com_82")) 
                list.append(("  Japan_12_tcp", "com_83"))                 
                list.append(("  Japan_12_udp", "com_84"))                  
                list.append(("  Japan_13_tcp", "com_85"))                 
                list.append(("  Japan_13_udp", "com_86")) 
                list.append(("  Japan_14_tcp", "com_87"))                 
                list.append(("  Japan_14_udp", "com_88"))                  
                list.append(("  Japan_15_tcp", "com_89"))                 
                list.append(("  Japan_15_udp", "com_90")) 
                list.append(("  Japan_16_tcp", "com_91"))                 
                list.append(("  Japan_16_udp", "com_92"))                  
                list.append(("  Japan_17_tcp", "com_93"))                 
                list.append(("  Japan_17_udp", "com_94")) 
                list.append(("  Japan_18_tcp", "com_95"))                 
                list.append(("  Japan_18_udp", "com_96"))                  
                list.append(("  Japan_19_tcp", "com_97"))                 
                list.append(("  Japan_19_udp", "com_98")) 
                list.append(("  Japan_20_tcp", "com_99")) 
                list.append(("  Japan_20_udp", "com_100"))                                    
                list.append(("  Japan_21_tcp", "com_101"))                 
                list.append(("  Japan_21_udp", "com_102")) 
                list.append(("  Japan_22_tcp", "com_103"))                 
                list.append(("  Japan_22_udp", "com_104"))                  
                list.append(("  Japan_23_tcp", "com_105"))                 
                list.append(("  Japan_23_udp", "com_106")) 
                list.append(("  Japan_24_tcp", "com_107"))                 
                list.append(("  Japan_24_udp", "com_108"))                  
                list.append(("  Japan_25_tcp", "com_109"))                 
                list.append(("  Japan_25_udp", "com_110")) 
                list.append(("  Japan_26_tcp", "com_111"))                 
                list.append(("  Japan_26_udp", "com_112"))                  
                list.append(("  Japan_27_tcp", "com_113"))                 
                list.append(("  Japan_27_udp", "com_114")) 
                list.append(("  Japan_28_tcp", "com_115"))                 
                list.append(("  Japan_28_udp", "com_116"))                  
                list.append(("  Japan_29_tcp", "com_117"))                 
                list.append(("  Japan_29_udp", "com_118")) 
                list.append(("  Japan_30_tcp", "com_119"))                 
                list.append(("  Japan_30_udp", "com_120")) 
                list.append(("  Korea_01_tcp", "com_121"))
                list.append(("  Korea_01_udp", "com_122"))
                list.append(("  Korea_02_tcp", "com_123"))
                list.append(("  Korea_02_udp", "com_124"))
                list.append(("  Korea_03_tcp", "com_125"))
                list.append(("  Korea_03_udp", "com_126"))
                list.append(("  Korea_04_tcp", "com_127"))
                list.append(("  Korea_04_udp", "com_128"))
                list.append(("  Korea_05_tcp", "com_129"))
                list.append(("  Korea_05_udp", "com_130"))
                list.append(("  Korea_06_tcp", "com_131"))
                list.append(("  Korea_06_udp", "com_132"))
                list.append(("  Korea_07_tcp", "com_133"))
                list.append(("  Korea_07_udp", "com_134"))
                list.append(("  Korea_08_tcp", "com_135"))
                list.append(("  Korea_08_udp", "com_136"))
                list.append(("  Korea_09_tcp", "com_137"))
                list.append(("  Korea_09_udp", "com_138"))
                list.append(("  Korea_10_tcp", "com_139"))
                list.append(("  Korea_10_udp", "com_140"))
                list.append(("  Korea_11_tcp", "com_141"))
                list.append(("  Korea_11_udp", "com_142"))
                list.append(("  Korea_12_tcp", "com_143"))
                list.append(("  Korea_12_udp", "com_144"))
                list.append(("  Korea_13_tcp", "com_145"))
                list.append(("  Korea_13_udp", "com_146"))
                list.append(("  Korea_14_tcp", "com_147"))
                list.append(("  Korea_14_udp", "com_148"))
                list.append(("  Korea_15_tcp", "com_149"))
                list.append(("  Korea_15_udp", "com_150"))
                list.append(("  Korea_16_tcp", "com_151"))
                list.append(("  Korea_16_udp", "com_152"))
                list.append(("  Korea_17_tcp", "com_153"))
                list.append(("  Korea_17_udp", "com_154"))
                list.append(("  Korea_18_tcp", "com_155"))
                list.append(("  Korea_18_udp", "com_156"))
                list.append(("  Korea_19_tcp", "com_157"))
                list.append(("  Korea_19_udp", "com_158"))
                list.append(("  Korea_20_tcp", "com_159"))
                list.append(("  Korea_20_udp", "com_160"))
                list.append(("  Korea_21_tcp", "com_161"))
                list.append(("  Korea_21_udp", "com_162"))
                list.append(("  Korea_22_tcp", "com_163"))
                list.append(("  Korea_22_udp", "com_164"))
                list.append(("  Korea_23_tcp", "com_165"))
                list.append(("  Korea_23_udp", "com_166"))
                list.append(("  Korea_24_tcp", "com_167"))
                list.append(("  Korea_24_udp", "com_168"))
                list.append(("  Korea_25_tcp", "com_169"))
                list.append(("  Korea_25_udp", "com_170"))
                list.append(("  Korea_26_tcp", "com_171"))
                list.append(("  Korea_26_udp", "com_172"))
                list.append(("  Korea_27_tcp", "com_173"))
                list.append(("  Korea_27_udp", "com_174"))
                list.append(("  Korea_28_tcp", "com_175"))
                list.append(("  Korea_28_udp", "com_176"))
                list.append(("  Korea_29_tcp", "com_177"))
                list.append(("  Korea_29_udp", "com_178"))
                list.append(("  Korea_30_tcp", "com_179"))
                list.append(("  Korea_30_udp", "com_180"))
                list.append(("  Korea_31_tcp", "com_181"))
                list.append(("  Korea_31_udp", "com_182"))
                list.append(("  Korea_32_tcp", "com_183"))
                list.append(("  Korea_32_udp", "com_184"))
                list.append(("  Korea_33_tcp", "com_185"))
                list.append(("  Korea_33_udp", "com_186"))
                list.append(("  Korea_34_tcp", "com_187"))
                list.append(("  Korea_34_udp", "com_188"))
                list.append(("  Korea_35_tcp", "com_189"))
                list.append(("  Korea_35_udp", "com_190"))
                list.append(("  Korea_36_tcp", "com_191"))
                list.append(("  Korea_36_udp", "com_192"))
                list.append(("  Korea_37_tcp", "com_193"))
                list.append(("  Korea_37_udp", "com_194"))
                list.append(("  Korea_38_tcp", "com_195"))
                list.append(("  Korea_38_udp", "com_196"))
                list.append(("  Korea_39_tcp", "com_197"))
                list.append(("  Korea_39_udp", "com_198"))
                list.append(("  Korea_40_tcp", "com_199"))
                list.append(("  Korea_40_udp", "com_200"))
                list.append(("  Korea_41_tcp", "com_201"))
                list.append(("  Korea_41_udp", "com_202"))
                list.append(("  Korea_42_tcp", "com_203"))
                list.append(("  Korea_42_udp", "com_204"))
                list.append(("  Korea_43_tcp", "com_205"))
                list.append(("  Korea_43_udp", "com_206"))
                list.append(("  Korea_44_tcp", "com_207"))
                list.append(("  Korea_44_udp", "com_208"))
                list.append(("  Korea_45_tcp", "com_209"))
                list.append(("  Korea_45_udp", "com_210"))
                list.append(("  Korea_46_tcp", "com_211"))
                list.append(("  Korea_46_udp", "com_212"))
                list.append(("  Korea_47_tcp", "com_213"))
                list.append(("  Korea_47_udp", "com_214"))
                list.append(("  Korea_48_tcp", "com_215"))
                list.append(("  Korea_48_udp", "com_216"))
                list.append(("  Korea_49_tcp", "com_217"))
                list.append(("  Korea_49_udp", "com_218"))
                list.append(("  Korea_50_tcp", "com_219"))
                list.append(("  Korea_50_udp", "com_220"))  
                list.append(("(1)_Korea_tcp", "com_221"))
                list.append(("      Korea_udp", "com_222"))
                list.append(("(2)-USA_tcp", "com_223"))
                list.append(("      USA_udp", "com_224"))
                list.append(("(3)-Taiwan_tcp", "com_225")) 
                list.append(("      Taiwan_udp", "com_226"))
                list.append(("(4)-China_tcp", "com_227"))
                list.append(("      China_udp", "com_228"))
                list.append(("(5)-Japan_tcp", "com_229"))
                list.append(("      Japan_udp", "com_230"))
                list.append(("(6)-France_tcp", "com_231"))
                list.append(("      France_udp", "com_232"))
                list.append(("(7)-Indonesia_tcp", "com_233"))
                list.append(("      Indonesia_udp", "com_234"))
                list.append(("(8)-Thailand_tcp", "com_235"))
                list.append(("      Thailand_udp", "com_236"))
                list.append(("(9)-UAE_tcp", "com_237"))
                list.append(("      UAE_udp", "com_238"))
                list.append(("(10)-Malaysia_tcp", "com_239"))
                list.append(("        Malaysia_udp", "com_240"))
                list.append(("(11)_Iran_tcp", "com_241"))
                list.append(("        Iran_udp", "com_242"))
                list.append(("(12)-Russia_tcp", "com_243"))
                list.append(("        Russia_udp", "com_244"))
                list.append(("(13)-Viet Nam_tcp", "com_245")) 
                list.append(("        Viet Nam_udp", "com_246"))
                list.append(("(14)-Hong Kong_tcp", "com_247"))
                list.append(("        Hong Kong_udp", "com_248"))
                list.append(("(15)-India_tcp", "com_249"))
                list.append(("        India_udp", "com_250"))
                list.append(("(16)-Turkmenistan_tcp", "com_251"))
                list.append(("        Turkmenistan_udp", "com_252"))
                list.append(("(17)-Canada_tcp", "com_253"))
                list.append(("        Canada_udp", "com_254"))
                list.append(("(18)-Saudi Arabia_tcp", "com_255"))
                list.append(("        Saudi Arabia_udp", "com_256"))
                list.append(("(19)-Philippines_tcp", "com_257"))
                list.append(("        Philippines_udp", "com_258"))
                list.append(("(20)-Ukraine_tcp", "com_259"))
                list.append(("        Ukraine_udp", "com_260"))
                list.append(("(21)_Singapore_tcp", "com_261"))
                list.append(("        Singapore_udp", "com_262"))
                list.append(("(22)-UK_tcp", "com_263"))
                list.append(("        UK_udp", "com_264"))
                list.append(("(23)-Germany_tcp", "com_265")) 
                list.append(("        Germany_udp", "com_266"))
                list.append(("(24)-Australia_tcp", "com_267"))
                list.append(("        Australia_udp", "com_268"))
                list.append(("(25)-Turkey_tcp", "com_269"))
                list.append(("        Turkey_udp", "com_270"))
                list.append(("(26)-Brazil_tcp", "com_271"))
                list.append(("        Brazil_udp", "com_272"))
                list.append(("(27)-Mexico_tcp", "com_273"))
                list.append(("        Mexico_udp", "com_274"))
                list.append(("(28)-Syria_tcp", "com_275"))
                list.append(("        Syria_udp", "com_276"))
                list.append(("(29)-Pakistan_tcp", "com_277"))
                list.append(("        Pakistan_udp", "com_278"))
                list.append(("(30)-Nigeria_tcp", "com_279"))
                list.append(("        Nigeria_udp", "com_280"))
                list.append(("(31)_Austria_tcp", "com_281"))
                list.append(("        Austria_udp", "com_282"))
                list.append(("(32)-Colombia_tcp", "com_283"))
                list.append(("          Colombia_udp", "com_284"))
                list.append(("(33)-Spain_tcp", "com_285")) 
                list.append(("        Spain_udp", "com_286"))
                list.append(("(34)-Iraq_tcp", "com_287"))
                list.append(("        Iraq_udp", "com_288"))
                list.append(("(35)-Ecuador_tcp", "com_289"))
                list.append(("        Ecuador_udp", "com_290"))
                list.append(("(36)-Bangladesh_tcp", "com_291"))
                list.append(("        Bangladesh_udp", "com_292"))
                list.append(("(37)-Italy_tcp", "com_293"))
                list.append(("        Italy_udp", "com_294"))
                list.append(("(38)-Oman_tcp", "com_295"))
                list.append(("        Oman_udp", "com_296"))
                list.append(("(39)-Netherlands_tcp", "com_297"))
                list.append(("        Netherlands_udp", "com_298"))
                list.append(("(40)-Argentina_tcp", "com_299"))
                list.append(("        Argentina_udp", "com_300"))
                list.append(("(41)_Egypt_tcp", "com_301"))
                list.append(("        Egypt_udp", "com_302"))
                list.append(("(42)-Kazakhstan_tcp", "com_303"))
                list.append(("        Kazakhstan_udp", "com_304"))
                list.append(("(43)-Venezuela_tcp", "com_305")) 
                list.append(("        Venezuela_udp", "com_306"))
                list.append(("(44)-Macau_tcp", "com_307"))
                list.append(("        Macau_udp", "com_308"))
                list.append(("(45)-Qatar_tcp", "com_309"))
                list.append(("        Qatar_udp", "com_310"))
                list.append(("(46)-Chile_tcp", "com_311"))
                list.append(("        Chile_udp", "com_312"))
                list.append(("(47)-Peru_tcp", "com_313"))
                list.append(("        Peru_udp", "com_314"))
                list.append(("(48)-Algeria_tcp", "com_315"))
                list.append(("        Algeria_udp", "com_316"))
                list.append(("(49)-New Zealand_tcp", "com_317"))
                list.append(("        New Zealand_udp", "com_318"))
                list.append(("(50)-Morocco_tcp", "com_319"))
                list.append(("        Morocco_udp", "com_320"))
                list.append(("(51)_Romania_tcp", "com_321"))
                list.append(("        Romania_udp", "com_322"))
                list.append(("(52)-Poland_tcp", "com_323"))
                list.append(("        Poland_udp", "com_324"))
                list.append(("(53)-South Africa_tcp", "com_325")) 
                list.append(("        South Africa_udp", "com_326"))
                list.append(("(54)-Lao_tcp", "com_327"))
                list.append(("        Lao_udp", "com_328"))
                list.append(("(55)-Sweden_tcp", "com_329"))
                list.append(("        Sweden_udp", "com_330"))
                list.append(("(56)-Finland_tcp", "com_331"))
                list.append(("        Finland_udp", "com_332"))
                list.append(("(57)-Sudan_tcp", "com_333"))
                list.append(("        Sudan_udp", "com_334"))
                list.append(("(58)-Belgium_tcp", "com_335"))
                list.append(("        Belgium_udp", "com_336"))
                list.append(("(59)-Ghana_tcp", "com_337"))
                list.append(("        Ghana_udp", "com_338"))
                list.append(("(60)-Norway_tcp", "com_339"))
                list.append(("        Norway_udp", "com_340"))
                list.append(("(61)_Cambodia_tcp", "com_341"))
                list.append(("        Cambodia_udp", "com_342"))
                list.append(("(62)-Kuwait_tcp", "com_343"))
                list.append(("        Kuwait_udp", "com_344"))
                list.append(("(63)-Belarus_tcp", "com_345")) 
                list.append(("        Belarus_udp", "com_346"))
                list.append(("(64)-Myanmar_tcp", "com_347"))
                list.append(("        Myanmar_udp", "com_348"))
                list.append(("(65)-Denmark_tcp", "com_349"))
                list.append(("        Denmark_udp", "com_350"))
                list.append(("(66)-Tunisia_tcp", "com_351"))
                list.append(("        Tunisia_udp", "com_352"))
                list.append(("(67)-Portugal_tcp", "com_353"))
                list.append(("        Portugal_udp", "com_354"))
                list.append(("(68)-Czech Republic_tcp", "com_355"))
                list.append(("        Czech Republic_udp", "com_356"))
                list.append(("(69)-Switzerland_tcp", "com_357"))
                list.append(("        Switzerland_udp", "com_358"))
                list.append(("(70)-Israel_tcp", "com_359"))
                list.append(("        Israel_udp", "com_360"))
                list.append(("(71)_Hungary_tcp", "com_361"))
                list.append(("        Hungary_udp", "com_362"))
                list.append(("(72)-Dominican_tcp", "com_363"))
                list.append(("        Dominican_udp", "com_364"))
                list.append(("(73)-Djibouti_tcp", "com_365")) 
                list.append(("        Djibouti_udp", "com_366"))
                list.append(("(74)-Jordan_tcp", "com_367"))
                list.append(("        Jordan_udp", "com_368"))
                list.append(("(75)-Nepal_tcp", "com_369"))
                list.append(("        Nepal_udp", "com_370"))
                list.append(("(76)-Lithuania_tcp", "com_371"))
                list.append(("        Lithuania_udp", "com_372"))
                list.append(("(77)-Guatemala_tcp", "com_373"))
                list.append(("        Guatemala_udp", "com_374"))
                list.append(("(78)-Bahrain_tcp", "com_375"))
                list.append(("        Bahrain_udp", "com_376"))
                list.append(("(79)-Greece_tcp", "com_377"))
                list.append(("        Greece_udp", "com_378"))
                list.append(("(80)-Palestine_tcp", "com_379"))
                list.append(("        Palestine_udp", "com_380"))
                list.append(("(81)_Sri Lanka_tcp", "com_381"))
                list.append(("        Sri Lanka_udp", "com_382"))
                list.append(("(82)-Bolivia_tcp", "com_383"))
                list.append(("        Bolivia_udp", "com_384"))
                list.append(("(83)-Serbia_tcp", "com_385")) 
                list.append(("        Serbia_udp", "com_386"))
                list.append(("(84)-Mongolia_tcp", "com_387"))
                list.append(("        Mongolia_udp", "com_388"))
                list.append(("(85)-Kenya_tcp", "com_389"))
                list.append(("        Kenya_udp", "com_390"))
                list.append(("(86)-Darussalam_tcp", "com_391"))
                list.append(("        Darussalam_udp", "com_392"))
                list.append(("(87)-Latvia_tcp", "com_393"))
                list.append(("        Latvia_udp", "com_394"))
                list.append(("(88)-Libya_tcp", "com_395"))
                list.append(("        Libya_udp", "com_396"))
                list.append(("(89)-Bulgaria_tcp", "com_397"))
                list.append(("        Bulgaria_udp", "com_398"))
                list.append(("(90)-Croatia_tcp", "com_399"))
                list.append(("        Croatia_udp", "com_400"))
                list.append(("(91)_Cote D'ivoire_tcp", "com_401"))
                list.append(("        Cote D'ivoire_udp", "com_402"))
                list.append(("(92)-Ireland_tcp", "com_403"))
                list.append(("        Ireland_udp", "com_404"))
                list.append(("(93)-Yemen_tcp", "com_405")) 
                list.append(("        Yemen_udp", "com_406"))
                list.append(("(94)-Uzbekistan_tcp", "com_407"))
                list.append(("        Uzbekistan_udp", "com_408"))
                list.append(("(95)-Lebanon_tcp", "com_409"))
                list.append(("        Lebanon_udp", "com_410"))
                list.append(("(96)-Ethiopia_tcp", "com_411"))
                list.append(("        Ethiopia_udp", "com_412"))
                list.append(("(97)-Estonia_tcp", "com_413"))
                list.append(("        Estonia_udp", "com_414"))
                list.append(("(98)-Costa Rica_tcp", "com_415"))
                list.append(("        Costa Rica_udp", "com_416"))
                list.append(("(99)-Panama_tcp", "com_417"))
                list.append(("        Panama_udp", "com_418"))          
                list.append(("(100)-Afghanistan_tcp", "com_419"))
                list.append(("          Afghanistan_udp", "com_420"))
                list.append(("(101)_Korea Democratic_tcp", "com_421"))
                list.append(("          Korea Democratic_udp", "com_422"))
                list.append(("(102)-Jamaica_tcp", "com_423"))
                list.append(("          Jamaica_udp", "com_424"))
                list.append(("(103)-Georgia_tcp", "com_425")) 
                list.append(("          Georgia_udp", "com_426"))
                list.append(("(104)-Moldova_tcp", "com_427"))
                list.append(("          Moldova_udp", "com_428"))
                list.append(("(105)-Uruguay_tcp", "com_429"))
                list.append(("          Uruguay_udp", "com_430"))
                list.append(("(106)-Slovenia_tcp", "com_431"))
                list.append(("          Slovenia_udp", "com_432"))
                list.append(("(107)-Slovakia_tcp", "com_433"))
                list.append(("          Slovakia_udp", "com_434"))
                list.append(("(108)-Paraguay_tcp", "com_435"))
                list.append(("          Paraguay_udp", "com_436"))
                list.append(("(109)-Honduras_tcp", "com_437"))
                list.append(("          Honduras_udp", "com_438"))
                list.append(("(110)-Azerbaijan_tcp", "com_439"))
                list.append(("          Azerbaijan_udp", "com_440"))
                list.append(("(111)_Trinidad_tcp", "com_441"))
                list.append(("          Trinidad_udp", "com_442"))
                list.append(("(112)-Cameroon_tcp", "com_443"))
                list.append(("          Cameroon_udp", "com_444"))
                list.append(("(113)-Benin_tcp", "com_445")) 
                list.append(("          Benin_udp", "com_446"))
                list.append(("(114)-Cuba_tcp", "com_447"))
                list.append(("          Cuba_udp", "com_448"))
                list.append(("(115)-Barbados_tcp", "com_449"))
                list.append(("          Barbados_udp", "com_450"))
                list.append(("(116)-Bosnia_tcp", "com_451"))
                list.append(("          Bosnia_udp", "com_452"))
                list.append(("(117)-Senegal_tcp", "com_453"))
                list.append(("          Senegal_udp", "com_454"))
                list.append(("(118)-El Salvador_tcp", "com_455"))
                list.append(("          El Salvador_udp", "com_456"))
                list.append(("(119)-Puerto Rico_tcp", "com_457"))
                list.append(("          Puerto Rico_udp", "com_458"))
                list.append(("(120)-Cyprus_tcp", "com_459"))
                list.append(("          Cyprus_udp", "com_460"))
                list.append(("(121)_Albania_tcp", "com_461"))
                list.append(("          Albania_udp", "com_462"))
                list.append(("(122)-Somalia_tcp", "com_463"))
                list.append(("          Somalia_udp", "com_464"))
                list.append(("(123)-Macedonia_tcp", "com_465")) 
                list.append(("          Macedonia_udp", "com_466"))
                list.append(("(124)-Tanzania_tcp", "com_467"))
                list.append(("          Tanzania_udp", "com_468"))
                list.append(("(125)-Mauritius_tcp", "com_469"))
                list.append(("          Mauritius_udp", "com_470"))
                list.append(("(126)-Kyrgyzstan_tcp", "com_471"))
                list.append(("          Kyrgyzstan_udp", "com_472"))
                list.append(("(127)-Armenia_tcp", "com_473"))
                list.append(("          Armenia_udp", "com_474"))
                list.append(("(128)-Madagascar_tcp", "com_475"))
                list.append(("          Madagascar_udp", "com_476"))
                list.append(("(129)-Maldives_tcp", "com_477"))
                list.append(("          Maldives_udp", "com_478"))
                list.append(("(130)-Rwanda_tcp", "com_479"))
                list.append(("          Rwanda_udp", "com_480"))
                list.append(("(131)_Luxembourg_tcp", "com_481"))
                list.append(("          Luxembourg_udp", "com_482"))
                list.append(("(132)-Uganda_tcp", "com_483"))
                list.append(("          Uganda_udp", "com_484"))
                list.append(("(133)-Guam_tcp", "com_485")) 
                list.append(("          Guam_udp", "com_486"))
                list.append(("(134)-Bahamas_tcp", "com_487"))
                list.append(("          Bahamas_udp", "com_488"))
                list.append(("(135)-Nicaragua_tcp", "com_489"))
                list.append(("          Nicaragua_udp", "com_490"))
                list.append(("(136)-Mali_tcp", "com_491"))
                list.append(("          Mali_udp", "com_492"))
                list.append(("(137)-Zimbabwe_tcp", "com_493"))
                list.append(("          Zimbabwe_udp", "com_494"))
                list.append(("(138)-Fiji_tcp", "com_495"))
                list.append(("          Fiji_udp", "com_496"))
                list.append(("(139)-Chad_tcp", "com_497"))
                list.append(("          Chad_udp", "com_498"))
                list.append(("(140)-Gambia_tcp", "com_499"))
                list.append(("          Gambia_udp", "com_500"))
                list.append(("(141)_Samoa_tcp", "com_501"))
                list.append(("          Samoa_tcp", "com_502"))
                list.append(("(142)-Iceland_tcp", "com_503"))
                list.append(("          Iceland_udp", "com_504"))
                list.append(("(143)-Aruba_tcp", "com_505")) 
                list.append(("          Aruba_udp", "com_506"))
                list.append(("(144)-Angola_tcp", "com_507"))
                list.append(("          Angola_udp", "com_508"))
                list.append(("(145)-Liberia_tcp", "com_509"))
                list.append(("          Liberia_udp", "com_510"))
                list.append(("(146)-Malta_tcp", "com_511"))
                list.append(("          Malta_udp", "com_512"))
                list.append(("(147)-New Caledonia_tcp", "com_513"))
                list.append(("          New Caledonia_udp", "com_514"))
                list.append(("(148)-New Guinea_tcp", "com_515"))
                list.append(("          New Guinea_udp", "com_516"))
                list.append(("(149)-Bhutan_tcp", "com_517"))
                list.append(("          Bhutan_udp", "com_518"))
                list.append(("(150)-Zambia_tcp", "com_519"))
                list.append(("          Zambia_udp", "com_520"))
                list.append(("(151)_Mozambique_tcp", "com_521"))
                list.append(("          Mozambique_udp", "com_522"))
                list.append(("(152)-Tajikistan_tcp", "com_523"))
                list.append(("          Tajikistan_udp", "com_524"))
                list.append(("(153)-Gabon_tcp", "com_525")) 
                list.append(("          Gabon_udp", "com_526"))
                list.append(("(154)-Reunion_tcp", "com_527"))
                list.append(("          Reunion_udp", "com_528"))
                list.append(("(155)-Namibia_tcp", "com_529"))
                list.append(("          Namibia_udp", "com_530"))
                list.append(("(156)-Montenegro_tcp", "com_531"))
                list.append(("          Montenegro_udp", "com_532"))
                list.append(("(157)-Belize_tcp", "com_533"))
                list.append(("          Belize_udp", "com_534"))
                list.append(("(158)-Equatorial Guinea_tcp", "com_535"))
                list.append(("          Equatorial Guinea_udp", "com_536"))
                list.append(("(159)-Malawi_tcp", "com_537"))
                list.append(("          Malawi_udp", "com_538"))
                list.append(("(160)-Comoros_tcp", "com_539"))
                list.append(("          Comoros_udp", "com_540"))
                list.append(("(161)_Dominica_tcp", "com_541"))
                list.append(("          Dominica_tcp", "com_542"))
                list.append(("(162)-Suriname_tcp", "com_543"))
                list.append(("          Suriname_udp", "com_544"))
                list.append(("(163)-Saint Vincent_tcp", "com_545")) 
                list.append(("          Saint Vincent_udp", "com_546"))
                list.append(("(164)-Togo_tcp", "com_547"))
                list.append(("          Togo_udp", "com_548"))
                list.append(("(165)-Congo_tcp", "com_549"))
                list.append(("          Congo_udp", "com_550"))
                list.append(("(166)-Seychelles_tcp", "com_551"))
                list.append(("          Seychelles_udp", "com_552"))
                list.append(("(167)-Guyana_tcp", "com_553"))
                list.append(("          Guyana_udp", "com_554"))
                list.append(("(168)-Wallis_tcp", "com_555"))
                list.append(("          Wallis_udp", "com_556"))
                list.append(("(169)-Congo Democratic_tcp", "com_557"))
                list.append(("          Congo Democratic_udp", "com_558"))
                list.append(("(170)-Botswana_tcp", "com_559"))
                list.append(("          Botswana_udp", "com_560"))
                list.append(("(171)_French Polynesia_tcp", "com_561"))
                list.append(("          French Polynesia_tcp", "com_562"))
                list.append(("(172)-Haiti_tcp", "com_563"))
                list.append(("          Haiti_udp", "com_564"))
                list.append(("(173)-Curacao_tcp", "com_565")) 
                list.append(("          Curacao_udp", "com_566"))
                list.append(("(174)-Saint Lucia_tcp", "com_567"))
                list.append(("          Saint Lucia_udp", "com_568"))
                list.append(("(175)-Palau_tcp", "com_569"))
                list.append(("          Palau_udp", "com_570"))
                list.append(("(176)-Grenada_tcp", "com_571"))
                list.append(("          Grenada_udp", "com_572"))
                list.append(("(177)-Marshall Islands_tcp", "com_573"))
                list.append(("          Marshall Islands_udp", "com_574"))
                list.append(("(178)-Burkina Faso_tcp", "com_575"))
                list.append(("          Burkina Faso_udp", "com_576"))
                list.append(("(179)-Timor-leste_tcp", "com_577"))
                list.append(("          Timor-leste_udp", "com_578"))
                list.append(("(180)-Cayman Islands_tcp", "com_579"))
                list.append(("          Cayman Islands_udp", "com_580"))
                list.append(("(181)_Mauritania_tcp", "com_581"))
                list.append(("          Mauritania_udp", "com_582"))
                list.append(("(182)-Niger_tcp", "com_583"))
                list.append(("          Niger_udp", "com_584"))
                list.append(("(183)-Micronesia_tcp", "com_585")) 
                list.append(("          Micronesia_udp", "com_586"))
                list.append(("(184)-Swaziland_tcp", "com_587"))
                list.append(("          Swaziland_udp", "com_588"))
                list.append(("(185)-Guinea_tcp", "com_589"))
                list.append(("          Guinea_udp", "com_590"))
                list.append(("(186)-Saint Kitts_tcp", "com_591"))
                list.append(("          Saint Kitts_udp", "com_592"))
                list.append(("(187)-Burundi_tcp", "com_593"))
                list.append(("          Burundi_udp", "com_594"))
                list.append(("(188)-Lesotho_tcp", "com_595"))
                list.append(("          Lesotho_udp", "com_596"))
                list.append(("(189)-Sierra Leone_tcp", "com_597"))
                list.append(("          Sierra Leone_udp", "com_598"))
                list.append(("(190)-Sint Maarten_tcp", "com_599"))
                list.append(("          Sint Maarten_udp", "com_600"))
                list.append(("(191)_Bermuda_tcp", "com_601"))
                list.append(("          Bermuda_tcp", "com_602"))
                list.append(("(192)-Virgin Islands_tcp", "com_603"))
                list.append(("          Virgin Islands_udp", "com_604"))
                list.append(("(193)-Jersey_tcp", "com_605")) 
                list.append(("          Jersey_udp", "com_606"))
                list.append(("(194)-Andorra_tcp", "com_607"))
                list.append(("          Andorra_udp", "com_608"))
                list.append(("(195)-Faroe Islands_tcp", "com_609"))
                list.append(("          Faroe Islands_udp", "com_610"))
                list.append(("(196)-Cape Verde_tcp", "com_611"))
                list.append(("          Cape Verde_udp", "com_612"))
                list.append(("(197)-Antigua and Barbuda_tcp", "com_613"))
                list.append(("          Antigua and Barbuda_udp", "com_614"))
                list.append(("(198)-Monaco_tcp", "com_615"))
                list.append(("          Monaco_udp", "com_616"))
                list.append(("(199)-American Samoa_tcp", "com_617"))
                list.append(("          American Samoa_udp", "com_618"))
                list.append(("(200)-Gibraltar_tcp", "com_619"))
                list.append(("          Gibraltar_udp", "com_620"))
                list.append(("(201)_Vanuatu_tcp", "com_621"))
                list.append(("          Vanuatu_tcp", "com_622"))
                list.append(("(202)-Turks and Caicos Islands_tcp", "com_623"))
                list.append(("          Turks and Caicos Islands_udp", "com_624"))
                list.append(("(203)-San Marino_tcp", "com_625")) 
                list.append(("          San Marino_udp", "com_626"))
                list.append(("(204)-Liechtenstein_tcp", "com_627"))
                list.append(("          Liechtenstein_udp", "com_628"))
                list.append(("(205)-Guadeloupe_tcp", "com_629"))
                list.append(("          Guadeloupe_udp", "com_630"))
                list.append(("(206)-Nauru_tcp", "com_631"))
                list.append(("          Nauru_udp", "com_632"))
                list.append(("(207)-South Sudan_tcp", "com_633"))
                list.append(("          South Sudan_udp", "com_634"))
                list.append(("(208)-Solomon Islands_tcp", "com_635"))
                list.append(("          Solomon Islands_udp", "com_636"))
                list.append(("(209)-Bonaire_tcp", "com_637"))
                list.append(("          Bonaire_udp", "com_638"))
                list.append(("(210)-Anguilla_tcp", "com_639"))
                list.append(("          Anguilla_udp", "com_640"))
                list.append(("(211)_St. Pierre_tcp", "com_641"))
                list.append(("          St. Pierre_udp", "com_642"))
                list.append(("(212)-Tonga_tcp", "com_643"))
                list.append(("          Tonga_udp", "com_644"))
                list.append(("(213)-Saint Martin_tcp", "com_645")) 
                list.append(("          Saint Martin_udp", "com_646"))
                list.append(("(214)-Guinea-bissau_tcp", "com_647"))
                list.append(("          Guinea-bissau_udp", "com_648"))
                list.append(("(215)-Virgin Islands (BRITISH)_tcp", "com_649"))
                list.append(("          Virgin Islands (BRITISH)_udp", "com_650"))
                list.append(("(216)-Eritrea_tcp", "com_651"))
                list.append(("          Eritrea_udp", "com_652"))
                list.append(("(217)-Central African_tcp", "com_653"))
                list.append(("          Central African_udp", "com_654"))
                list.append(("(218)-Kiribati_tcp", "com_655"))
                list.append(("          Kiribati_udp", "com_656"))
                list.append(("(219)-Sao Tome_tcp", "com_657"))
                list.append(("          Sao Tome_udp", "com_658"))
                list.append(("(220)-French Guiana_tcp", "com_659"))
                list.append(("          French Guiana_udp", "com_660"))
                list.append(("(211)_Mayotte_tcp", "com_661"))
                list.append(("          Mayotte_tcp", "com_662"))
                list.append(("(222)-Cook Islands_tcp", "com_663"))
                list.append(("          Cook Islands_udp", "com_664"))
                list.append(("(223)-Saint Barthelemy_tcp", "com_665")) 
                list.append(("          Saint Barthelemy_udp", "com_666"))
                list.append(("(224)-Tuvalu_tcp", "com_667"))
                list.append(("          Tuvalu_udp", "com_668"))
                list.append(("(225)-Holy See_tcp", "com_669"))
                list.append(("          Holy See_udp", "com_670"))
                list.append(("(226)-Isle of Man_tcp", "com_671"))
                list.append(("          Isle of Man_udp", "com_672")) 
                list.append((" Ncam-cortexa9hf-vfp-neon-ARM DreamoxUHD", "com_673"))
                list.append((" Ncam-aarch64-ARM VU+4K Duo4K + osmio4k", "com_674"))
                list.append((" Ncam-build-mips (Gigablue-Dream-VU+-Xtrend-Formuler)", "com_675"))
                list.append((" Ncam-build-sh4 (Golden Media-Galaxy innovations-Amiko)", "com_676"))
                list.append((" softcams-oscam-all-images-emu-arm+mips_all.ipk", "com_677"))
                list.append((" softcams-oscam-all-images-emu-arm+mips_all.deb", "com_677*"))
                list.append((" softcams-ncam-all-images-emu-arm+mips_all.ipk", "com_678"))
                list.append((" softcams-ncam-all-images-emu-arm+mips_all.deb", "com_678*"))
                list.append((" ncam.config", "com_679"))
                list.append((" oscam.config", "com_0680"))
                list.append((" gcam.config", "com_680"))
                list.append((" autokeys", "com_681"))
                list.append((" CCcam_Speed_Update", "com_682"))
                list.append(("  VPNbook.ca222-TCP443", "com_683"))                
                list.append(("  VPNbook.ca222-TCP80", "com_684"))                
                list.append(("  VPNbook.ca222-UDP25000", "com_685"))                
                list.append(("  VPNbook.ca222-UDP53", "com_686"))                
                list.append(("  vpn-us", "com_687")) 
                list.append(("  Find My Current ip Address", "com_688"))
                list.append(("  OpenVPN_STOP", "com_689"))              
                list.append(("  VPNbook.de4-TCP443", "com_690"))                
                list.append(("  VPNbook.de4-TCP80", "com_691"))                
                list.append(("  VPNbook.de4-UDP25000", "com_692"))                
                list.append(("  VPNbook.de4-UDP53", "com_693"))                
                list.append(("  VPNbook.fr1-TCP443", "com_694"))                                
                list.append(("  VPNbook.fr1-TCP80", "com_695"))
                list.append(("  VPNbook.fr1-UDP25000", "com_696"))                  
                list.append(("  VPNbook.fr1-UDP53", "com_697"))                
                list.append(("  VPNbook.fr8-TCP443", "com_698"))                
                list.append(("  VPNbook.fr8-TCP80", "com_699"))                
                list.append(("  VPNbook.fr8-UDP25000", "com_700"))                
                list.append(("  VPNbook.fr8-UDP53", "com_701"))                         
                list.append(("  VPNbook.pl226-TCP443", "com_702")) 
                list.append(("  VPNbook.pl226-TCP80", "com_703"))               
                list.append(("  VPNbook.pl226-UDP25000", "com_704"))                
                list.append(("  VPNbook.pl226-UDP53", "com_705"))                
                list.append(("  VPNbook.us1-TCP443", "com_706"))                
                list.append(("  VPNbook.us1-TCP80", "com_707"))                
                list.append(("  VPNbook.us1-UDP25000", "com_708"))                              
                list.append(("  VPNbook.us1-UDP53", "com_709"))
                list.append(("  VPNbook.us2-TCP443", "com_710"))                
                list.append(("  VPNbook.us2-TCP80", "com_711"))                
                list.append(("  VPNbook.us2-UDP53", "com_712"))                
                list.append(("  VPNbook.us2-UDP53", "com_713"))                
                list.append(("  FreeVPN.me-UDP-53", "com_714"))                
                list.append(("  FreeVPN.me-UDP-53", "com_715"))                         
                list.append(("  FreeVPN.me-UDP-53", "com_716"))
                list.append(("  FreeVPN.me-UDP-53", "com_717")) 
                list.append(("  USA_1_tcp", "com_718"))                 
                list.append(("  USA_1_udp", "com_719"))                  
                list.append(("  USA_2_tcp", "com_720"))                 
                list.append(("  USA_2_udp", "com_721")) 
                list.append(("  USA_3_tcp", "com_722"))                 
                list.append(("  USA_3_udp", "com_723"))                  
                list.append(("  USA_4_tcp", "com_724"))                 
                list.append(("  USA_4_udp", "com_725")) 
                list.append(("  USA_5_tcp", "com_726"))                 
                list.append(("  USA_5_udp", "com_727"))                  
                list.append(("  USA_6_tcp", "com_728"))                 
                list.append(("  USA_6_udp", "com_729")) 
                list.append(("  USA_7_tcp", "com_730"))                 
                list.append(("  USA_7_udp", "com_731"))                  
                list.append(("  USA_8_tcp", "com_732"))                 
                list.append(("  USA_8_udp", "com_733")) 
                list.append(("  USA_9_tcp", "com_734"))                 
                list.append(("  USA_9_udp", "com_735"))                  
                list.append(("  USA_10_tcp", "com_736"))                 
                list.append(("  USA_10_udp", "com_737"))  
                list.append(("  Canada_1_tcp", "com_738"))                 
                list.append(("  Canada_1_udp", "com_739"))  
                list.append(("  Canada_2_tcp", "com_740"))  
                list.append(("  Canada_2_udp", "com_741"))      
                list.append((_("Exit"), "exit"))
                Screen.__init__(self, session)
                self.cmdlist = []
                #self['text'] = Label()
                #self["key_yellow"] = Label()
                self["key_green"] = Label()
                self["key_red"] = Label()       
                #self['icon'] = Pixmap()           
                #self['Bt1'] = Pixmap()
                self['Bt2'] = Pixmap()
                self['Bt3'] = Pixmap()                          
                self["myMenu"] = MenuList(list)
                self['actions'] = ActionMap(['SetupActions', 'DirectionActions', 'ColorActions'], {'ok': self.close,
                        #'blue': self.info,         
                        'yellow': self.Freeserver,
                        "0": self.myInput,
                        "ok": self.go,                                     
                        'red': self.close,
                        'cancel': self.cancel,
                        'green': self.Freeserver}, -1)

        
                #self.onShown.append(self.setMyText)   
                                                         
        def go(self):
                returnValue = self["myMenu"].l.getCurrentSelection()[1]
                print("\n[MyShPrombt] returnValue: " + returnValue + "\n")
### EDit By RAED To DreamOS OE2.5/2.6
                if returnValue is not None:
                        if returnValue == "com_free":                   
                                cmdlist = []
                                cmdlist.append("wget -qO - '" + "'")
                                cmdlist.append("wget https://ia600702.us.archive.org/26/items/dreamosat/cccam48.sh -qO - | /bin/sh")
                                self.session.open(Console3, title='Server CCCAM48H', cmdlist=cmdlist, finishedCallback=None)
                                return
                        elif returnValue == "com_free48":                   
                                #cmdlist = []
                                #cmdlist.append("wget -qO - '" + "'")
                                #cmdlist.append("wget https://ia600702.us.archive.org/26/items/dreamosat/cccam48.sh -qO - | /bin/sh")
                                #self.session.open(Console3, title='Server CCCAM48H', cmdlist=cmdlist, finishedCallback=None)
                                self.session.open(myInput)
                        elif returnValue == "com_free01":                       
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia600702.us.archive.org/26/items/dreamosat/paksat5days.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='Server paksat5days', cmdlist=cmdlist, finishedCallback=None)
                                return

                        elif returnValue == "com_free02":                       
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia601506.us.archive.org/33/items/freecccamserver_201906/firecccam.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='Free firecccam', cmdlist=cmdlist, finishedCallback=None)
                                return

                        elif returnValue == "com_free03":                       
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia601506.us.archive.org/33/items/freecccamserver_201906/firecccam2.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='Free firecccam2', cmdlist=cmdlist, finishedCallback=None)
                                return

                        elif returnValue == "com_free04":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia601506.us.archive.org/33/items/freecccamserver_201906/urliptv.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='Free urlcccam', cmdlist=cmdlist, finishedCallback=None)
                                return

                        elif returnValue == "com_free05":                       
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia601506.us.archive.org/33/items/freecccamserver_201906/scccam.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='Free Scccam', cmdlist=cmdlist, finishedCallback=None)
                                return

                        elif returnValue == "com_free06":                       
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia601506.us.archive.org/33/items/freecccamserver_201906/clinezone.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='Free ClineZone', cmdlist=cmdlist, finishedCallback=None)
                                return

                        elif returnValue == "com_free2":                        
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia601506.us.archive.org/33/items/freecccamserver_201906/realcccam.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='Free CCcam 5 days', cmdlist=cmdlist, finishedCallback=None)
                                return

                        elif returnValue == "com_free3":                        
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia601506.us.archive.org/33/items/freecccamserver_201906/barcacccam.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='Free CCcam 5 days', cmdlist=cmdlist, finishedCallback=None)
                                return

                        elif returnValue == "com_free4":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia601506.us.archive.org/33/items/freecccamserver_201906/cccamserverworldsat.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='Free CCcam 5 days', cmdlist=cmdlist, finishedCallback=None)
                                return

                        elif returnValue == "com_free5":                        
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia601506.us.archive.org/33/items/freecccamserver_201906/redcam.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='Red-Cam', cmdlist=cmdlist, finishedCallback=None)
                                return

                        elif returnValue == "com_free6":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia601506.us.archive.org/33/items/freecccamserver_201906/goldencam.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='Golden-Cam', cmdlist=cmdlist, finishedCallback=None)
                                return

                        elif returnValue == "com_free7":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia601506.us.archive.org/33/items/freecccamserver_201906/freecccam.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='FreeCCcam', cmdlist=cmdlist, finishedCallback=None)
                                return

                        elif returnValue == "com_free8":                        
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia601506.us.archive.org/33/items/freecccamserver_201906/freecccamserver27.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='premium', cmdlist=cmdlist, finishedCallback=None)
                                return

                        elif returnValue == "com_free9":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia601506.us.archive.org/33/items/freecccamserver_201906/freecccamserver49.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='skyhd', cmdlist=cmdlist, finishedCallback=None)
                                return

                        elif returnValue == "com_free10":                       
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia601506.us.archive.org/33/items/freecccamserver_201906/freecccamserver47.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='deadman1', cmdlist=cmdlist, finishedCallback=None)
                                return

                        elif returnValue == "com_free11":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia601506.us.archive.org/33/items/freecccamserver_201906/freecccamserver48.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='deadman2', cmdlist=cmdlist, finishedCallback=None)
                                return

                        elif returnValue == "com_free12":      
                                import sys,os  
                                os.system("%s https://ia601500.us.archive.org/32/items/FoulFreecccamserver/Programetvfoots.sh -qO - | /bin/sh" % self.wget) 
                                self.session.open(Showinfo7)
                                
                        elif returnValue == "com_free13":      
                                import sys,os  
                                os.system("%s https://ia601500.us.archive.org/32/items/FoulFreecccamserver/Programetvfoot.sh -qO - | /bin/sh" % self.wget) 
                                self.session.open(Showinfo2)

                        elif returnValue == "com_free14":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia902904.us.archive.org/21/items/urliptv/4k44u.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='4k4u', cmdlist=cmdlist, finishedCallback=None)
                                return

                        elif returnValue == "com_free15":                       
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia902904.us.archive.org/21/items/urliptv/ajktv.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='ajktv', cmdlist=cmdlist, finishedCallback=None)
                                return

                        elif returnValue == "com_free16":                       
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia902904.us.archive.org/21/items/urliptv/algsat.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='algsat', cmdlist=cmdlist, finishedCallback=None)
                                return

                        elif returnValue == "com_free17":                       
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia902904.us.archive.org/21/items/urliptv/bigtezz.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='bigtezz', cmdlist=cmdlist, finishedCallback=None)
                                return

                        elif returnValue == "com_free18":                       
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia902904.us.archive.org/21/items/urliptv/cccam48.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='cccam48', cmdlist=cmdlist, finishedCallback=None)
                                return

                        elif returnValue == "com_free19":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia902904.us.archive.org/21/items/urliptv/cccambird.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='cccambird', cmdlist=cmdlist, finishedCallback=None)
                                return

                        elif returnValue == "com_free20":                       
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia902904.us.archive.org/21/items/urliptv/cccamlive.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='cccamlive', cmdlist=cmdlist, finishedCallback=None)
                                return

                        elif returnValue == "com_free21":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia902904.us.archive.org/21/items/urliptv/cccamlive2.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='cccamlive2', cmdlist=cmdlist, finishedCallback=None)
                                return

                        elif returnValue == "com_free22":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia902904.us.archive.org/21/items/urliptv/cccamtiger.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='cccamtiger', cmdlist=cmdlist, finishedCallback=None)
                                return

                        elif returnValue == "com_free23":                       
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia902904.us.archive.org/21/items/urliptv/chandcccam.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='chandcccam', cmdlist=cmdlist, finishedCallback=None)
                                return

                        elif returnValue == "com_free24":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia902904.us.archive.org/21/items/urliptv/clinezone.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='clinezone', cmdlist=cmdlist, finishedCallback=None)
                                return

                        elif returnValue == "com_free25":                       
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia902904.us.archive.org/21/items/urliptv/eurohd.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='eurohd', cmdlist=cmdlist, finishedCallback=None)
                                return

                        elif returnValue == "com_free26":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia902904.us.archive.org/21/items/urliptv/flylinks.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='flylinks', cmdlist=cmdlist, finishedCallback=None)
                                return

                        elif returnValue == "com_free27":                       
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia902904.us.archive.org/21/items/urliptv/freecccam.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='freecccam', cmdlist=cmdlist, finishedCallback=None)
                                return

                        elif returnValue == "com_free28":      
                                cmdlist = [] 
                                cmdlist.append("%s https://ia902904.us.archive.org/21/items/urliptv/freeiptv4u.sh -qO - | /bin/sh" % self.wget) 
                                self.session.open(Console3, title='freeiptv4u', cmdlist=cmdlist, finishedCallback=None)
                                return
                             
                        elif returnValue == "com_free29":      
                                cmdlist = [] 
                                cmdlist.append("%s https://ia902904.us.archive.org/21/items/urliptv/hack-sat.sh -qO - | /bin/sh" % self.wget) 
                                self.session.open(Console3, title='hack-sat', cmdlist=cmdlist, finishedCallback=None)
                                return

                        elif returnValue == "com_free30":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia902904.us.archive.org/21/items/urliptv/hack-sat2.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='hack-sat2', cmdlist=cmdlist, finishedCallback=None)
                                return

                        elif returnValue == "com_free31":                       
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia902904.us.archive.org/21/items/urliptv/iptvsat4k.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='iptvsat4k', cmdlist=cmdlist, finishedCallback=None)
                                return

                        elif returnValue == "com_free32":                       
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia902904.us.archive.org/21/items/urliptv/paksat.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='paksat', cmdlist=cmdlist, finishedCallback=None)
                                return

                        elif returnValue == "com_free33":                       
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia902904.us.archive.org/21/items/urliptv/paksat5days.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='paksat2', cmdlist=cmdlist, finishedCallback=None)
                                return

                        elif returnValue == "com_free34":                       
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia902904.us.archive.org/21/items/urliptv/powerhd.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='powerhd', cmdlist=cmdlist, finishedCallback=None)
                                return

                        elif returnValue == "com_free35":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia902904.us.archive.org/21/items/urliptv/saeed7.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='saeed7', cmdlist=cmdlist, finishedCallback=None)
                                return

                        elif returnValue == "com_free36":                       
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia902904.us.archive.org/21/items/urliptv/satunivers.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='satunivers', cmdlist=cmdlist, finishedCallback=None)
                                return

                        elif returnValue == "com_free37":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia902904.us.archive.org/21/items/urliptv/scccam.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='scccam', cmdlist=cmdlist, finishedCallback=None)
                                return

                        elif returnValue == "com_free38":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia902904.us.archive.org/21/items/urliptv/serinsat.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='serinsat', cmdlist=cmdlist, finishedCallback=None)
                                return

                        elif returnValue == "com_free39":                       
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia902904.us.archive.org/21/items/urliptv/serversat.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='serversat', cmdlist=cmdlist, finishedCallback=None)
                                return

                        elif returnValue == "com_free40":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia902904.us.archive.org/21/items/urliptv/urliptv.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='urliptv', cmdlist=cmdlist, finishedCallback=None)
                                return
                                                                                               
                        elif returnValue == "com_foul":                 
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia801504.us.archive.org/16/items/freecccamserver/Foul_freecccamserver.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='Foul Freecccamserver', cmdlist=cmdlist, finishedCallback=None)
                                return

                        elif returnValue == "com_0":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia601506.us.archive.org/33/items/freecccamserver_201906/freecccamserver0.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='Free CCcambird48H', cmdlist=cmdlist, finishedCallback=None)
                                return

                        elif returnValue == "com_1":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia601506.us.archive.org/33/items/freecccamserver_201906/freecccamserver1.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='Free CCcam webtechdz48H', cmdlist=cmdlist, finishedCallback=None)
                                return

                        elif returnValue == "com_2":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia601506.us.archive.org/33/items/freecccamserver_201906/freecccamserver2.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='Free cccam hiberlo', cmdlist=cmdlist, finishedCallback=None)
                                return

                        elif returnValue == "com_3":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia601506.us.archive.org/33/items/freecccamserver_201906/freecccamserver3.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='Free cccamserver4u', cmdlist=cmdlist, finishedCallback=None)
                                return
                                                                                 
                        elif returnValue == "com_4":                              
                                cmdlist = []                                      
                                cmdlist.append("%s -qO - '" % self.wget + "'") 
                                cmdlist.append("%s https://ia601506.us.archive.org/33/items/freecccamserver_201906/freecccamserver4.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='Free cccam-server.de', cmdlist=cmdlist, finishedCallback=None)
                                return

                        elif returnValue == "com_5":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")                   
                                cmdlist.append("%s https://ia601506.us.archive.org/33/items/freecccamserver_201906/freecccamserver5.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='Free paycccam', cmdlist=cmdlist, finishedCallback=None)
                                return
                                                                      
                        elif returnValue == "com_6":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia601506.us.archive.org/33/items/freecccamserver_201906/freecccamserver6.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='Free freeiptv4u', cmdlist=cmdlist, finishedCallback=None)
                                return

                        elif returnValue == "com_7":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia601506.us.archive.org/33/items/freecccamserver_201906/freecccamserver7.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='Free flylinks', cmdlist=cmdlist, finishedCallback=None)
                                return

                        elif returnValue == "com_8":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")    
                                cmdlist.append("%s https://ia601506.us.archive.org/33/items/freecccamserver_201906/freecccamserver8.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='Free 4k4u.top', cmdlist=cmdlist, finishedCallback=None)
                                return
                        
                        elif returnValue == "com_9":
                                cmdlist = []                                        
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia601506.us.archive.org/33/items/freecccamserver_201906/freecccamserver9.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='Free pakface', cmdlist=cmdlist, finishedCallback=None)
                                return
                        
                        elif returnValue == "com_10":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia601506.us.archive.org/33/items/freecccamserver_201906/freecccamserver10.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='Free fcccam (5 days)*', cmdlist=cmdlist, finishedCallback=None)
                                return

                        elif returnValue == "com_11":
                                cmdlist = []                           
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia601506.us.archive.org/33/items/freecccamserver_201906/freecccamserver11.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='Free cccam eurohd', cmdlist=cmdlist, finishedCallback=None)
                                return
                                                
                        elif returnValue == "com_12":
                                cmdlist = []                           
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia601506.us.archive.org/33/items/freecccamserver_201906/freecccamserver12.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='Free cccam clineworlds', cmdlist=cmdlist, finishedCallback=None)
                                return

                        elif returnValue == "com_13":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia601506.us.archive.org/33/items/freecccamserver_201906/freecccamserver13.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='Free cccam clinepk', cmdlist=cmdlist, finishedCallback=None)
                                return
                                                
                        elif returnValue == "com_14":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia601506.us.archive.org/33/items/freecccamserver_201906/freecccamserver14.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='Free realcccam (5 days)**', cmdlist=cmdlist, finishedCallback=None)
                                return

                        elif returnValue == "com_15":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia601506.us.archive.org/33/items/freecccamserver_201906/freecccamserver15.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='Free cccam paksat', cmdlist=cmdlist, finishedCallback=None)
                                return
                                                        
                                                
                        elif returnValue == "com_16":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia601506.us.archive.org/33/items/freecccamserver_201906/freecccamserver16.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='Free satunivers', cmdlist=cmdlist, finishedCallback=None)
                                return

                        elif returnValue == "com_17":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia601506.us.archive.org/33/items/freecccamserver_201906/freecccamserver17.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='Free cccam scccam', cmdlist=cmdlist, finishedCallback=None)
                                return

                        elif returnValue == "com_18":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia601506.us.archive.org/33/items/freecccamserver_201906/freecccamserver18.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='Free cccam satunivers', cmdlist=cmdlist, finishedCallback=None)
                                return

                        elif returnValue == "com_19":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia601506.us.archive.org/33/items/freecccamserver_201906/freecccamserver19.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='Free cccam azaanhd.top', cmdlist=cmdlist, finishedCallback=None)
                                return

                        elif returnValue == "com_20":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia601506.us.archive.org/33/items/freecccamserver_201906/freecccamserver20.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='Free cccam clinefree', cmdlist=cmdlist, finishedCallback=None)
                                return

                        elif returnValue == "com_21":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia601506.us.archive.org/33/items/freecccamserver_201906/freecccamserver21.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='Free cccam clinefree**', cmdlist=cmdlist, finishedCallback=None)
                                return

                        elif returnValue == "com_22":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia601506.us.archive.org/33/items/freecccamserver_201906/freecccamserver22.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='Free cccam serversat*', cmdlist=cmdlist, finishedCallback=None)
                                return

                        elif returnValue == "com_23":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia601506.us.archive.org/33/items/freecccamserver_201906/freecccamserver23.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='Free cccam hdpak', cmdlist=cmdlist, finishedCallback=None)
                                return

                        elif returnValue == "com_24":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia601506.us.archive.org/33/items/freecccamserver_201906/freecccamserver24.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='Free cccam tezzpak', cmdlist=cmdlist, finishedCallback=None)
                                return

                        elif returnValue == "com_25":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia601506.us.archive.org/33/items/freecccamserver_201906/freecccamserver25.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='Free Free cccam4g (5 days)**', cmdlist=cmdlist, finishedCallback=None)
                                return

                        elif returnValue == "com_26":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia601506.us.archive.org/33/items/freecccamserver_201906/freecccamserver26.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='Free dreamcccam (5 days)*', cmdlist=cmdlist, finishedCallback=None)
                                return

                        elif returnValue == "com_27":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia601506.us.archive.org/33/items/freecccamserver_201906/freecccamserver27.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='Free premium bszsat (5 days)**', cmdlist=cmdlist, finishedCallback=None)
                                return

                        elif returnValue == "com_28":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia601506.us.archive.org/33/items/freecccamserver_201906/freecccamserver28.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='Free cccam worldcccam', cmdlist=cmdlist, finishedCallback=None)
                                return

                        elif returnValue == "com_29":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia601506.us.archive.org/33/items/freecccamserver_201906/freecccamserver29.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='Free anwarcccam', cmdlist=cmdlist, finishedCallback=None)
                                return

                        elif returnValue == "com_30":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia601506.us.archive.org/33/items/freecccamserver_201906/freecccamserver30.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='Free cccamhd', cmdlist=cmdlist, finishedCallback=None)
                                return

                        elif returnValue == "com_31":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia601506.us.archive.org/33/items/freecccamserver_201906/freecccamserver31.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='Free cccam clinezone (5 days)*', cmdlist=cmdlist, finishedCallback=None)
                                return

                        elif returnValue == "com_32":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia601506.us.archive.org/33/items/freecccamserver_201906/freecccamserver32.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='Free cccam tounfite', cmdlist=cmdlist, finishedCallback=None)
                                return

                        elif returnValue == "com_33":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia601506.us.archive.org/33/items/freecccamserver_201906/freecccamserver33.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='Free cccampk', cmdlist=cmdlist, finishedCallback=None)
                                return

                        elif returnValue == "com_34":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia601506.us.archive.org/33/items/freecccamserver_201906/freecccamserver34.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='Free cccam ajktv', cmdlist=cmdlist, finishedCallback=None)
                                return

                        elif returnValue == "com_35":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia601506.us.archive.org/33/items/freecccamserver_201906/freecccamserver35.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='Free cccam iptvsmarttv*', cmdlist=cmdlist, finishedCallback=None)
                                return

                        elif returnValue == "com_36":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia601506.us.archive.org/33/items/freecccamserver_201906/freecccamserver36.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='Free cccam iptvsat4k', cmdlist=cmdlist, finishedCallback=None)
                                return

                        elif returnValue == "com_37":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia601506.us.archive.org/33/items/freecccamserver_201906/freecccamserver37.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='Free cccam iptvsmarttv', cmdlist=cmdlist, finishedCallback=None)
                                return
                                         
                        elif returnValue == "com_38":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia601506.us.archive.org/33/items/freecccamserver_201906/freecccamserver38.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='Free cccamboss', cmdlist=cmdlist, finishedCallback=None)
                                return

                        elif returnValue == "com_39":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia601506.us.archive.org/33/items/freecccamserver_201906/freecccamserver39.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='Free cccamtiger', cmdlist=cmdlist, finishedCallback=None)
                                return

                        elif returnValue == "com_40":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia601506.us.archive.org/33/items/freecccamserver_201906/freecccamserver40.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='Free cccam world', cmdlist=cmdlist, finishedCallback=None)
                                return

                        elif returnValue == "com_41":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia601506.us.archive.org/33/items/freecccamserver_201906/freecccamserver41.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='Free cccam world', cmdlist=cmdlist, finishedCallback=None)
                                return

                        elif returnValue == "com_42":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia601506.us.archive.org/33/items/freecccamserver_201906/freecccamserver42.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='Free cccam world', cmdlist=cmdlist, finishedCallback=None)
                                return

                        elif returnValue == "com_43":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia601506.us.archive.org/33/items/freecccamserver_201906/freecccamserver43.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='Free cccam world', cmdlist=cmdlist, finishedCallback=None)
                                return

                        elif returnValue == "com_44":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia601506.us.archive.org/33/items/freecccamserver_201906/freecccamserver44.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='Free cccam world', cmdlist=cmdlist, finishedCallback=None)
                                return

                        elif returnValue == "com_45":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia601506.us.archive.org/33/items/freecccamserver_201906/freecccamserver45.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='Free cccam world', cmdlist=cmdlist, finishedCallback=None)
                                return

                        elif returnValue == "com_46":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia601506.us.archive.org/33/items/freecccamserver_201906/freecccamserver46.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='Free cccam deadman', cmdlist=cmdlist, finishedCallback=None)
                                return

                        elif returnValue == "com_47":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia601506.us.archive.org/33/items/freecccamserver_201906/freecccamserver47.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='Free cccam deadman', cmdlist=cmdlist, finishedCallback=None)
                                return

                        elif returnValue == "com_48":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia601506.us.archive.org/33/items/freecccamserver_201906/freecccamserver48.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='Free cccam deadman', cmdlist=cmdlist, finishedCallback=None)
                                return

                        elif returnValue == "com_49":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia601506.us.archive.org/33/items/freecccamserver_201906/freecccamserver49.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='Free cccam serinsat', cmdlist=cmdlist, finishedCallback=None)
                                return

                        elif returnValue == "com_50":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia601506.us.archive.org/33/items/freecccamserver_201906/freecccamserver50.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='Free cccam serinsat', cmdlist=cmdlist, finishedCallback=None)
                                return

                        elif returnValue == "com_51":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia601506.us.archive.org/33/items/freecccamserver_201906/freecccamserver51.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='Free cccam chandcccam', cmdlist=cmdlist, finishedCallback=None)
                                return

                        elif returnValue == "com_52":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia601506.us.archive.org/33/items/freecccamserver_201906/freecccamserver52.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='Free cccam hacksat', cmdlist=cmdlist, finishedCallback=None)
                                return

                        elif returnValue == "com_53":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia601506.us.archive.org/33/items/freecccamserver_201906/freecccamserver53.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='Free cccam hacksat', cmdlist=cmdlist, finishedCallback=None)
                                return

                        elif returnValue == "com_54":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia601506.us.archive.org/33/items/freecccamserver_201906/freecccamserver54.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='Free cccam realcccam', cmdlist=cmdlist, finishedCallback=None)
                                return

                        elif returnValue == "com_55":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia601506.us.archive.org/33/items/freecccamserver_201906/freecccamserver55.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='Free cccam saeed', cmdlist=cmdlist, finishedCallback=None)
                                return

                        elif returnValue == "com_56":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia601506.us.archive.org/33/items/freecccamserver_201906/freecccamserver56.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='Free cccam test', cmdlist=cmdlist, finishedCallback=None)
                                return
                                                                                                                                                                                                                                                                                                                                                 
                        elif returnValue == "com_00":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia801402.us.archive.org/18/items/freecccamserver0/freecccamserver0.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='Free CCcambird48H', cmdlist=cmdlist, finishedCallback=None)
                                return

                        elif returnValue == "com_01":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia601402.us.archive.org/18/items/freecccamserver0/freecccamserver1.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='Free CCcam webtechdz48H', cmdlist=cmdlist, finishedCallback=None)
                                return

                        elif returnValue == "com_02":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia601402.us.archive.org/18/items/freecccamserver0/freecccamserver2.sh.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='Free cccam hiberlo', cmdlist=cmdlist, finishedCallback=None)
                                return

                        elif returnValue == "com_03":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia601402.us.archive.org/18/items/freecccamserver0/freecccamserver3.sh.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='Free cccamserver4u', cmdlist=cmdlist, finishedCallback=None)
                                return

                        elif returnValue == "com_04":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia601402.us.archive.org/18/items/freecccamserver0/freecccamserver4.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='Free cccam-server.de', cmdlist=cmdlist, finishedCallback=None)
                                return

                        elif returnValue == "com_05":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia601402.us.archive.org/18/items/freecccamserver0/freecccamserver5.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='Free paycccam', cmdlist=cmdlist, finishedCallback=None)
                                return
                                                                      
                        elif returnValue == "com_06":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia601402.us.archive.org/18/items/freecccamserver0/freecccamserver6.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='Free freeiptv4u', cmdlist=cmdlist, finishedCallback=None)
                                return

                        elif returnValue == "com_07":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia601402.us.archive.org/18/items/freecccamserver0/freecccamserver7.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='Free flylinks', cmdlist=cmdlist, finishedCallback=None)
                                return

                        elif returnValue == "com_08":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia601402.us.archive.org/18/items/freecccamserver0/freecccamserver8.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='Free 4k4u.top', cmdlist=cmdlist, finishedCallback=None)
                                return
                        
                        elif returnValue == "com_09":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia601402.us.archive.org/18/items/freecccamserver0/freecccamserver9.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='Free pakface', cmdlist=cmdlist, finishedCallback=None)
                                return
                        
                        elif returnValue == "com_010":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia601402.us.archive.org/18/items/freecccamserver0/freecccamserver10.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='Free fcccam (5 days)*', cmdlist=cmdlist, finishedCallback=None)
                                return

                        elif returnValue == "com_011":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia601402.us.archive.org/18/items/freecccamserver0/freecccamserver11.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='Free cccam eurohd', cmdlist=cmdlist, finishedCallback=None)
                                return
                                                
                        elif returnValue == "com_012":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia601402.us.archive.org/18/items/freecccamserver0/freecccamserver12.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='Free cccam clineworlds', cmdlist=cmdlist, finishedCallback=None)
                                return

                        elif returnValue == "com_013":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia601402.us.archive.org/18/items/freecccamserver0/freecccamserver13.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='Free cccam clinepk', cmdlist=cmdlist, finishedCallback=None)
                                return
                                                
                        elif returnValue == "com_014":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia601402.us.archive.org/18/items/freecccamserver0/freecccamserver14.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='Free realcccam (5 days)**', cmdlist=cmdlist, finishedCallback=None)
                                return

                        elif returnValue == "com_015":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia601402.us.archive.org/18/items/freecccamserver0/freecccamserver15.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='Free cccam paksat', cmdlist=cmdlist, finishedCallback=None)
                                return
                                                                                
                        elif returnValue == "com_016":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia601402.us.archive.org/18/items/freecccamserver0/freecccamserver16.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='Free satunivers', cmdlist=cmdlist, finishedCallback=None)
                                return

                        elif returnValue == "com_017":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia601402.us.archive.org/18/items/freecccamserver0/freecccamserver17.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='Free cccam scccam', cmdlist=cmdlist, finishedCallback=None)
                                return

                        elif returnValue == "com_018":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia601402.us.archive.org/18/items/freecccamserver0/freecccamserver18.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='Free cccam satunivers', cmdlist=cmdlist, finishedCallback=None)
                                return

                        elif returnValue == "com_019":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia601402.us.archive.org/18/items/freecccamserver0/freecccamserver19.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='Free cccam azaanhd.top', cmdlist=cmdlist, finishedCallback=None)
                                return

                        elif returnValue == "com_020":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia601402.us.archive.org/18/items/freecccamserver0/freecccamserver20.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='Free cccam', cmdlist=cmdlist, finishedCallback=None)
                                return

                        elif returnValue == "com_021":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia601402.us.archive.org/18/items/freecccamserver0/freecccamserver21.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='Free cccam clinefree**', cmdlist=cmdlist, finishedCallback=None)
                                return

                        elif returnValue == "com_022":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia601402.us.archive.org/18/items/freecccamserver0/freecccamserver22.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='Free cccam serversat*', cmdlist=cmdlist, finishedCallback=None)
                                return

                        elif returnValue == "com_023":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia601402.us.archive.org/18/items/freecccamserver0/freecccamserver23.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='Free cccam hdpak', cmdlist=cmdlist, finishedCallback=None)
                                return

                        elif returnValue == "com_024":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia601402.us.archive.org/18/items/freecccamserver0/freecccamserver24.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='Free cccam tezzpak', cmdlist=cmdlist, finishedCallback=None)
                                return

                        elif returnValue == "com_025":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia601402.us.archive.org/18/items/freecccamserver0/freecccamserver25.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='Free cccam4g (5 days)**', cmdlist=cmdlist, finishedCallback=None)
                                return

                        elif returnValue == "com_026":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia601402.us.archive.org/18/items/freecccamserver0/freecccamserver26.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='Free dreamcccam (5 days)*', cmdlist=cmdlist, finishedCallback=None)
                                return

                        elif returnValue == "com_027":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia601402.us.archive.org/18/items/freecccamserver0/freecccamserver27.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='Free premium bszsat (5 days)**', cmdlist=cmdlist, finishedCallback=None)
                                return

                        elif returnValue == "com_028":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia601402.us.archive.org/18/items/freecccamserver0/freecccamserver28.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='Free cccam worldcccam', cmdlist=cmdlist, finishedCallback=None)
                                return

                        elif returnValue == "com_029":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia601402.us.archive.org/18/items/freecccamserver0/freecccamserver29.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='Free anwarcccam', cmdlist=cmdlist, finishedCallback=None)
                                return

                        elif returnValue == "com_030":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia601402.us.archive.org/18/items/freecccamserver0/freecccamserver30.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='Free cccamhd', cmdlist=cmdlist, finishedCallback=None)
                                return

                        elif returnValue == "com_031":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia601402.us.archive.org/18/items/freecccamserver0/freecccamserver31.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='Free cccam clinezone (5 days)*', cmdlist=cmdlist, finishedCallback=None)
                                return

                        elif returnValue == "com_032":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia601402.us.archive.org/18/items/freecccamserver0/freecccamserver32.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='Free cccam tounfite', cmdlist=cmdlist, finishedCallback=None)
                                return

                        elif returnValue == "com_033":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia601402.us.archive.org/18/items/freecccamserver0/freecccamserver33.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='Free cccampk', cmdlist=cmdlist, finishedCallback=None)
                                return

                        elif returnValue == "com_034":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia601402.us.archive.org/18/items/freecccamserver0/freecccamserver34.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='Free cccam ajktv', cmdlist=cmdlist, finishedCallback=None)
                                return

                        elif returnValue == "com_035":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia601402.us.archive.org/18/items/freecccamserver0/freecccamserver35.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='Free cccam iptvsmarttv*', cmdlist=cmdlist, finishedCallback=None)
                                return

                        elif returnValue == "com_036":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia601402.us.archive.org/18/items/freecccamserver0/freecccamserver36.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='Free cccam iptvsat4k', cmdlist=cmdlist, finishedCallback=None)
                                return

                        elif returnValue == "com_037":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia601402.us.archive.org/18/items/freecccamserver0/freecccamserver37.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='Free cccam iptvsmarttv', cmdlist=cmdlist, finishedCallback=None)
                                return

                        elif returnValue == "com_038":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia601402.us.archive.org/18/items/freecccamserver0/freecccamserver38.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='Free cccamboss', cmdlist=cmdlist, finishedCallback=None)
                                return

                        elif returnValue == "com_039":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia601402.us.archive.org/18/items/freecccamserver0/freecccamserver39.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='Free cccamtiger', cmdlist=cmdlist, finishedCallback=None)
                                return

                        elif returnValue == "com_040":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia601402.us.archive.org/18/items/freecccamserver0/freecccamserver40.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='Free cccam world', cmdlist=cmdlist, finishedCallback=None)
                                return

                        elif returnValue == "com_041":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia601402.us.archive.org/18/items/freecccamserver0/freecccamserver41.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='Free cccam world', cmdlist=cmdlist, finishedCallback=None)
                                return

                        elif returnValue == "com_042":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia601402.us.archive.org/18/items/freecccamserver0/freecccamserver42.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='Free cccam world', cmdlist=cmdlist, finishedCallback=None)
                                return

                        elif returnValue == "com_043":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia601402.us.archive.org/18/items/freecccamserver0/freecccamserver43.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='Free cccam world', cmdlist=cmdlist, finishedCallback=None)
                                return

                        elif returnValue == "com_044":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia601402.us.archive.org/18/items/freecccamserver0/freecccamserver44.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='Free cccam world', cmdlist=cmdlist, finishedCallback=None)
                                return

                        elif returnValue == "com_045":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia601402.us.archive.org/18/items/freecccamserver0/freecccamserver45.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='Free cccam world', cmdlist=cmdlist, finishedCallback=None)
                                return

                        elif returnValue == "com_046":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia601402.us.archive.org/18/items/freecccamserver0/freecccamserver46.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='Free cccam deadman', cmdlist=cmdlist, finishedCallback=None)
                                return

                        elif returnValue == "com_047":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia601402.us.archive.org/18/items/freecccamserver0/freecccamserver47.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='Free cccam deadman', cmdlist=cmdlist, finishedCallback=None)
                                return

                        elif returnValue == "com_048":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia601402.us.archive.org/18/items/freecccamserver0/freecccamserver48.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='Free cccam deadman', cmdlist=cmdlist, finishedCallback=None)
                                return

                        elif returnValue == "com_049":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia601402.us.archive.org/18/items/freecccamserver0/freecccamserver49.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='Free cccam serinsat', cmdlist=cmdlist, finishedCallback=None)
                                return

                        elif returnValue == "com_050":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia601402.us.archive.org/18/items/freecccamserver0/freecccamserver50.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='Free cccam serinsat', cmdlist=cmdlist, finishedCallback=None)
                                return

                        elif returnValue == "com_051":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia601402.us.archive.org/18/items/freecccamserver0/freecccamserver51.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='Free cccam chandcccam', cmdlist=cmdlist, finishedCallback=None)
                                return

                        elif returnValue == "com_052":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia601402.us.archive.org/18/items/freecccamserver0/freecccamserver52.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='Free cccam hacksat', cmdlist=cmdlist, finishedCallback=None)
                                return

                        elif returnValue == "com_053":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia601402.us.archive.org/18/items/freecccamserver0/freecccamserver53.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='Free cccam hacksat', cmdlist=cmdlist, finishedCallback=None)
                                return

                        elif returnValue == "com_054":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia601402.us.archive.org/18/items/freecccamserver0/freecccamserver54.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='Free cccam realcccam', cmdlist=cmdlist, finishedCallback=None)
                                return

                        elif returnValue == "com_055":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia601402.us.archive.org/18/items/freecccamserver0/freecccamserver55.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='Free cccam saeed', cmdlist=cmdlist, finishedCallback=None)
                                return

                        elif returnValue == "com_056":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia601402.us.archive.org/18/items/freecccamserver0/freecccamserver56.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='Free cccam test', cmdlist=cmdlist, finishedCallback=None)
                                return

                        elif returnValue == "com_001":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia601402.us.archive.org/18/items/freecccamserver0/freemgcamdserver1.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='Free Mgcamd cccamdz', cmdlist=cmdlist, finishedCallback=None)
                                return

                        elif returnValue == "com_002":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia601402.us.archive.org/18/items/freecccamserver0/freemgcamdserver2.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='Free Mgcamd serversat', cmdlist=cmdlist, finishedCallback=None)
                                return

                        elif returnValue == "com_003":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia601402.us.archive.org/18/items/freecccamserver0/freemgcamdserver3.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='Free Mgcamd firecccam', cmdlist=cmdlist, finishedCallback=None)
                                return

                        elif returnValue == "com_004":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia601402.us.archive.org/18/items/freecccamserver0/freemgcamdserver4.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='Free Mgcamd firecccam', cmdlist=cmdlist, finishedCallback=None)
                                return

                        if returnValue == "com_free":                   
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia601402.us.archive.org/18/items/freecccamserver0/FreeServer.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='FreeServer Only', cmdlist=cmdlist, finishedCallback=None)
                                return

                        if returnValue == "com_foul0":                  
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia601402.us.archive.org/18/items/freecccamserver0/Foul_freecccamserver.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='Foul Freecccamserver Only', cmdlist=cmdlist, finishedCallback=None)
                                return

                        elif returnValue == "com_57":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia801500.us.archive.org/32/items/FoulFreecccamserver/Auto_update_FreeServer.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='Auto_update_FreeServer', cmdlist=cmdlist, finishedCallback=None)
                                return
            
                        elif returnValue == "com_58":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia801502.us.archive.org/4/items/FreeServerinfo/Auto_update_Foul_freecccamserver.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='Auto_update_Foul_freecccamserver', cmdlist=cmdlist, finishedCallback=None)
                                return
            
                        elif returnValue == "com_59":      
                                import sys,os  
                                os.system("%s https://ia601500.us.archive.org/32/items/FoulFreecccamserver/Programetvfoot.sh -qO - | /bin/sh" % self.wget) 
                                self.session.open(Showinfo2)
                                                                                            
                        elif returnValue == "com_60":                         
                                import sys,os  
                                os.system("%s https://ia800702.us.archive.org/26/items/dreamosat/lists_world.sh -qO - | /bin/sh" % self.wget) 
                                self.session.open(Showinfo)
                                
                        elif returnValue == "com_61":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia801504.us.archive.org/28/items/JapanTcpUdp/Japan_01_tcp.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='Japan_01_tcp', cmdlist=cmdlist, finishedCallback=None)
                                return

                        elif returnValue == "com_62":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia801504.us.archive.org/28/items/JapanTcpUdp/Japan_01_udp.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='Japan_01_udp', cmdlist=cmdlist, finishedCallback=None)
                                return
                                
                        elif returnValue == "com_63":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia801504.us.archive.org/28/items/JapanTcpUdp/Japan_02_tcp.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='Japan_02_tcp', cmdlist=cmdlist, finishedCallback=None)
                                return

                        elif returnValue == "com_64":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia801504.us.archive.org/28/items/JapanTcpUdp/Japan_02_udp.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='Japan_02_udp', cmdlist=cmdlist, finishedCallback=None)
                                return

                        elif returnValue == "com_65":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia801504.us.archive.org/28/items/JapanTcpUdp/Japan_03_tcp.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='Japan_03_tcp', cmdlist=cmdlist, finishedCallback=None)
                                return

                        elif returnValue == "com_66":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia801504.us.archive.org/28/items/JapanTcpUdp/Japan_03_udp.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='Japan_03_udp', cmdlist=cmdlist, finishedCallback=None)
                                return

                        elif returnValue == "com_67":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia801504.us.archive.org/28/items/JapanTcpUdp/Japan_04_tcp.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='Japan_04_tcp', cmdlist=cmdlist, finishedCallback=None)
                                return

                        elif returnValue == "com_68":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia801504.us.archive.org/28/items/JapanTcpUdp/Japan_04_udp.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='Japan_04_udp', cmdlist=cmdlist, finishedCallback=None)
                                return

                        elif returnValue == "com_69":
                                cmdlist = []                                      
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia801504.us.archive.org/28/items/JapanTcpUdp/Japan_05_tcp.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='Japan_05_tcp', cmdlist=cmdlist, finishedCallback=None)
                                return

                        elif returnValue == "com_70":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia801504.us.archive.org/28/items/JapanTcpUdp/Japan_05_udp.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='Japan_05_udp', cmdlist=cmdlist, finishedCallback=None)
                                return

                        elif returnValue == "com_71":
                                cmdlist = []                                      
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia801504.us.archive.org/28/items/JapanTcpUdp/Japan_06_tcp.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='Japan_06_tcp', cmdlist=cmdlist, finishedCallback=None)
                                return

                        elif returnValue == "com_72":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia801504.us.archive.org/28/items/JapanTcpUdp/Japan_06_udp.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='Japan_06_udp', cmdlist=cmdlist, finishedCallback=None)
                                return

                        elif returnValue == "com_73":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia801504.us.archive.org/28/items/JapanTcpUdp/Japan_07_tcp.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='Japan_07_tcp', cmdlist=cmdlist, finishedCallback=None)
                                return

                        elif returnValue == "com_74":
                                cmdlist = []                                      
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia801504.us.archive.org/28/items/JapanTcpUdp/Japan_07_udp.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='Japan_07_udp', cmdlist=cmdlist, finishedCallback=None)
                                return

                        elif returnValue == "com_75":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia801504.us.archive.org/28/items/JapanTcpUdp/Japan_08_tcp.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='Japan_08_tcp', cmdlist=cmdlist, finishedCallback=None)
                                return

                        elif returnValue == "com_76":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia801504.us.archive.org/28/items/JapanTcpUdp/Japan_08_udp.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='Japan_08_udp', cmdlist=cmdlist, finishedCallback=None)
                                return

                        elif returnValue == "com_77":
                                cmdlist = []                                      
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia801504.us.archive.org/28/items/JapanTcpUdp/Japan_09_tcp.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='Japan_09_tcp', cmdlist=cmdlist, finishedCallback=None)
                                return

                        elif returnValue == "com_78":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia801504.us.archive.org/28/items/JapanTcpUdp/Japan_09_udp.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='Japan_09_udp', cmdlist=cmdlist, finishedCallback=None)
                                return

                        elif returnValue == "com_79":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia801504.us.archive.org/28/items/JapanTcpUdp/Japan_10_tcp.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='Japan_10_tcp', cmdlist=cmdlist, finishedCallback=None)
                                return

                        elif returnValue == "com_80":
                                cmdlist = []                                      
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia801504.us.archive.org/28/items/JapanTcpUdp/Japan_10_udp.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='Japan_10_udp', cmdlist=cmdlist, finishedCallback=None)
                                return

                        elif returnValue == "com_81":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia801504.us.archive.org/28/items/JapanTcpUdp/Japan_11_tcp.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='Japan_11_tcp', cmdlist=cmdlist, finishedCallback=None)
                                return

                        elif returnValue == "com_82":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia801504.us.archive.org/28/items/JapanTcpUdp/Japan_11_udp.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='Japan_11_udp', cmdlist=cmdlist, finishedCallback=None)
                                return

                        elif returnValue == "com_83":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia801504.us.archive.org/28/items/JapanTcpUdp/Japan_12_tcp.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='Japan_12_tcp', cmdlist=cmdlist, finishedCallback=None)
                                return

                        elif returnValue == "com_84":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia801504.us.archive.org/28/items/JapanTcpUdp/Japan_12_udp.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='Japan_12_udp', cmdlist=cmdlist, finishedCallback=None)
                                return

                        elif returnValue == "com_85":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia801504.us.archive.org/28/items/JapanTcpUdp/Japan_13_tcp.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='Japan_13_tcp', cmdlist=cmdlist, finishedCallback=None)
                                return

                        elif returnValue == "com_86":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia801504.us.archive.org/28/items/JapanTcpUdp/Japan_13_udp.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='Japan_13_udp', cmdlist=cmdlist, finishedCallback=None)
                                return

                        elif returnValue == "com_87":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia801504.us.archive.org/28/items/JapanTcpUdp/Japan_14_tcp.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='Japan_14_tcp', cmdlist=cmdlist, finishedCallback=None)
                                return

                        elif returnValue == "com_88":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia801504.us.archive.org/28/items/JapanTcpUdp/Japan_14_udp.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='Japan_14_udp', cmdlist=cmdlist, finishedCallback=None)
                                return

                        elif returnValue == "com_89":
                                cmdlist = []                                      
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia801504.us.archive.org/28/items/JapanTcpUdp/Japan_15_tcp.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='Japan_15_tcp', cmdlist=cmdlist, finishedCallback=None)
                                return

                        elif returnValue == "com_90":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia801504.us.archive.org/28/items/JapanTcpUdp/Japan_15_udp.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='Japan_15_udp', cmdlist=cmdlist, finishedCallback=None)
                                return

                        elif returnValue == "com_91":
                                cmdlist = []                                      
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia801504.us.archive.org/28/items/JapanTcpUdp/Japan_16_tcp.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='Japan_16_tcp', cmdlist=cmdlist, finishedCallback=None)
                                return

                        elif returnValue == "com_92":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia801504.us.archive.org/28/items/JapanTcpUdp/Japan_16_udp.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='Japan_16_udp', cmdlist=cmdlist, finishedCallback=None)
                                return

                        elif returnValue == "com_93":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia801504.us.archive.org/28/items/JapanTcpUdp/Japan_17_tcp.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='Japan_17_tcp', cmdlist=cmdlist, finishedCallback=None)
                                return

                        elif returnValue == "com_94":
                                cmdlist = []                                      
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia801504.us.archive.org/28/items/JapanTcpUdp/Japan_17_udp.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='Japan_17_udp', cmdlist=cmdlist, finishedCallback=None)
                                return
                                
                        elif returnValue == "com_95":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia801504.us.archive.org/28/items/JapanTcpUdp/Japan_18_tcp.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='Japan_18_tcp', cmdlist=cmdlist, finishedCallback=None)
                                return

                        elif returnValue == "com_96":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia801504.us.archive.org/28/items/JapanTcpUdp/Japan_18_udp.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='Japan_18_udp', cmdlist=cmdlist, finishedCallback=None)
                                return

                        elif returnValue == "com_97":
                                cmdlist = []                                      
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia801504.us.archive.org/28/items/JapanTcpUdp/Japan_19_tcp.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='Japan_19_tcp', cmdlist=cmdlist, finishedCallback=None)
                                return

                        elif returnValue == "com_98":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia801504.us.archive.org/28/items/JapanTcpUdp/Japan_19_udp.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='Japan_19_udp', cmdlist=cmdlist, finishedCallback=None)
                                return

                        elif returnValue == "com_99":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia801504.us.archive.org/28/items/JapanTcpUdp/Japan_20_tcp.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='Japan_20_tcp', cmdlist=cmdlist, finishedCallback=None)
                                return

                        elif returnValue == "com_100":
                                cmdlist = []                                      
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia801504.us.archive.org/28/items/JapanTcpUdp/Japan_20_udp.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='Japan_20_udp', cmdlist=cmdlist, finishedCallback=None)
                                return
                        elif returnValue == "com_101":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia801504.us.archive.org/28/items/JapanTcpUdp/Japan_21_tcp.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='Japan_21_tcp', cmdlist=cmdlist, finishedCallback=None)
                                return

                        elif returnValue == "com_102":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia801504.us.archive.org/28/items/JapanTcpUdp/Japan_21_udp.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='Japan_21_udp', cmdlist=cmdlist, finishedCallback=None)
                                return

                        elif returnValue == "com_103":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia801504.us.archive.org/28/items/JapanTcpUdp/Japan_22_tcp.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='Japan_22_tcp', cmdlist=cmdlist, finishedCallback=None)
                                return

                        elif returnValue == "com_104":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia801504.us.archive.org/28/items/JapanTcpUdp/Japan_22_udp.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='Japan_22_udp', cmdlist=cmdlist, finishedCallback=None)
                                return

                        elif returnValue == "com_105":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia801504.us.archive.org/28/items/JapanTcpUdp/Japan_23_tcp.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='Japan_23_tcp', cmdlist=cmdlist, finishedCallback=None)
                                return

                        elif returnValue == "com_106":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia801504.us.archive.org/28/items/JapanTcpUdp/Japan_23_udp.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='Japan_23_udp', cmdlist=cmdlist, finishedCallback=None)
                                return

                        elif returnValue == "com_107":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia801504.us.archive.org/28/items/JapanTcpUdp/Japan_24_tcp.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='Japan_24_tcp', cmdlist=cmdlist, finishedCallback=None)
                                return

                        elif returnValue == "com_108":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia801504.us.archive.org/28/items/JapanTcpUdp/Japan_24_udp.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='Japan_24_udp', cmdlist=cmdlist, finishedCallback=None)
                                return

                        elif returnValue == "com_109":
                                cmdlist = []                                      
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia801504.us.archive.org/28/items/JapanTcpUdp/Japan_25_tcp.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='Japan_25_tcp', cmdlist=cmdlist, finishedCallback=None)
                                return

                        elif returnValue == "com_110":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia801504.us.archive.org/28/items/JapanTcpUdp/Japan_25_udp.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='Japan_25_udp', cmdlist=cmdlist, finishedCallback=None)
                                return

                        elif returnValue == "com_111":
                                cmdlist = []                                      
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia801504.us.archive.org/28/items/JapanTcpUdp/Japan_26_tcp.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='Japan_26_tcp', cmdlist=cmdlist, finishedCallback=None)
                                return

                        elif returnValue == "com_112":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia801504.us.archive.org/28/items/JapanTcpUdp/Japan_26_udp.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='Japan_26_udp', cmdlist=cmdlist, finishedCallback=None)
                                return

                        elif returnValue == "com_113":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia801504.us.archive.org/28/items/JapanTcpUdp/Japan_27_tcp.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='Japan_27_tcp', cmdlist=cmdlist, finishedCallback=None)
                                return

                        elif returnValue == "com_114":
                                cmdlist = []                                      
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia801504.us.archive.org/28/items/JapanTcpUdp/Japan_27_udp.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='Japan_27_udp', cmdlist=cmdlist, finishedCallback=None)
                                return
                                
                        elif returnValue == "com_115":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia801504.us.archive.org/28/items/JapanTcpUdp/Japan_28_tcp.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='Japan_28_tcp', cmdlist=cmdlist, finishedCallback=None)
                                return

                        elif returnValue == "com_116":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia801504.us.archive.org/28/items/JapanTcpUdp/Japan_28_udp.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='Japan_28_udp', cmdlist=cmdlist, finishedCallback=None)
                                return

                        elif returnValue == "com_117":
                                cmdlist = []                                      
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia801504.us.archive.org/28/items/JapanTcpUdp/Japan_29_tcp.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='Japan_29_tcp', cmdlist=cmdlist, finishedCallback=None)
                                return

                        elif returnValue == "com_118":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia801504.us.archive.org/28/items/JapanTcpUdp/Japan_29_udp.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='Japan_29_udp', cmdlist=cmdlist, finishedCallback=None)
                                return

                        elif returnValue == "com_119":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia801504.us.archive.org/28/items/JapanTcpUdp/Japan_30_tcp.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='Japan_30_tcp', cmdlist=cmdlist, finishedCallback=None)
                                return

                        elif returnValue == "com_120":
                                cmdlist = []                                      
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia801504.us.archive.org/28/items/JapanTcpUdp/Japan_30_udp.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='Japan_30_udp', cmdlist=cmdlist, finishedCallback=None)
                                return
        
                        elif returnValue == "com_121":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia801501.us.archive.org/14/items/aminovitchi5050_yahoo_Files/Korea_01_tcp.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='Korea_01_tcp', cmdlist=cmdlist, finishedCallback=None)
                                return

                        elif returnValue == "com_122":
                                cmdlist = []                                      
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia801501.us.archive.org/14/items/aminovitchi5050_yahoo_Files/Korea_01_udp.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='Korea_01_udp', cmdlist=cmdlist, finishedCallback=None)
                                return

                        elif returnValue == "com_123":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia801501.us.archive.org/14/items/aminovitchi5050_yahoo_Files/Korea_02_tcp.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='Korea_02_tcp', cmdlist=cmdlist, finishedCallback=None)
                                return

                        elif returnValue == "com_124":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia801501.us.archive.org/14/items/aminovitchi5050_yahoo_Files/Korea_02_udp.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='Korea_02_udp', cmdlist=cmdlist, finishedCallback=None)
                                return

                        elif returnValue == "com_125":
                                cmdlist = []                                      
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia801501.us.archive.org/14/items/aminovitchi5050_yahoo_Files/Korea_03_tcp.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='Korea_03_tcp', cmdlist=cmdlist, finishedCallback=None)
                                return

                        elif returnValue == "com_126":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia801501.us.archive.org/14/items/aminovitchi5050_yahoo_Files/Korea_03_udp.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='Korea_03_udp', cmdlist=cmdlist, finishedCallback=None)
                                return

                        elif returnValue == "com_127":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia801501.us.archive.org/14/items/aminovitchi5050_yahoo_Files/Korea_04_tcp.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='Korea_04_tcp', cmdlist=cmdlist, finishedCallback=None)
                                return

                        elif returnValue == "com_128":
                                cmdlist = []                                      
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia801501.us.archive.org/14/items/aminovitchi5050_yahoo_Files/Korea_04_udp.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='Korea_04_udp', cmdlist=cmdlist, finishedCallback=None)
                                return

                        elif returnValue == "com_129":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia801501.us.archive.org/14/items/aminovitchi5050_yahoo_Files/Korea_05_tcp.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='Korea_05_tcp', cmdlist=cmdlist, finishedCallback=None)
                                return

                        elif returnValue == "com_130":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia801501.us.archive.org/14/items/aminovitchi5050_yahoo_Files/Korea_05_udp.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='Korea_05_udp', cmdlist=cmdlist, finishedCallback=None)
                                return

                        elif returnValue == "com_131":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia801501.us.archive.org/14/items/aminovitchi5050_yahoo_Files/Korea_06_tcp.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='Korea_06_tcp', cmdlist=cmdlist, finishedCallback=None)
                                return

                        elif returnValue == "com_132":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia801501.us.archive.org/14/items/aminovitchi5050_yahoo_Files/Korea_06_udp.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='Korea_06_udp', cmdlist=cmdlist, finishedCallback=None)
                                return

                        elif returnValue == "com_133":
                                cmdlist = []                                      
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia801501.us.archive.org/14/items/aminovitchi5050_yahoo_Files/Korea_07_tcp.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='Korea_07_tcp', cmdlist=cmdlist, finishedCallback=None)
                                return

                        elif returnValue == "com_134":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia801501.us.archive.org/14/items/aminovitchi5050_yahoo_Files/Korea_07_udp.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='Korea_07_udp', cmdlist=cmdlist, finishedCallback=None)
                                return

                        elif returnValue == "com_135":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia801501.us.archive.org/14/items/aminovitchi5050_yahoo_Files/Korea_08_tcp.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='Korea_08_tcp', cmdlist=cmdlist, finishedCallback=None)
                                return

                        elif returnValue == "com_136":
                                cmdlist = []                                      
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia801501.us.archive.org/14/items/aminovitchi5050_yahoo_Files/Korea_08_udp.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='Korea_08_udp', cmdlist=cmdlist, finishedCallback=None)
                                return

                        elif returnValue == "com_137":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia801501.us.archive.org/14/items/aminovitchi5050_yahoo_Files/Korea_09_tcp.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='Korea_09_tcp', cmdlist=cmdlist, finishedCallback=None)
                                return

                        elif returnValue == "com_138":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia801501.us.archive.org/14/items/aminovitchi5050_yahoo_Files/Korea_09_udp.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='Korea_09_udp', cmdlist=cmdlist, finishedCallback=None)
                                return

                        elif returnValue == "com_139":
                                cmdlist = []                                      
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia801501.us.archive.org/14/items/aminovitchi5050_yahoo_Files/Korea_10_tcp.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='Korea_10_tcp', cmdlist=cmdlist, finishedCallback=None)
                                return

                        elif returnValue == "com_140":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia801501.us.archive.org/14/items/aminovitchi5050_yahoo_Files/Korea_10_udp.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='Korea_10_udp', cmdlist=cmdlist, finishedCallback=None)
                                return

                        elif returnValue == "com_141":
                                cmdlist = []                                      
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia801501.us.archive.org/14/items/aminovitchi5050_yahoo_Files/Korea_11_tcp.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='Korea_11_tcp', cmdlist=cmdlist, finishedCallback=None)
                                return

                        elif returnValue == "com_142":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia801501.us.archive.org/14/items/aminovitchi5050_yahoo_Files/Korea_11_udp.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='Korea_11_udp', cmdlist=cmdlist, finishedCallback=None)
                                return

                        elif returnValue == "com_143":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia801501.us.archive.org/14/items/aminovitchi5050_yahoo_Files/Korea_12_tcp.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='Korea_12_tcp', cmdlist=cmdlist, finishedCallback=None)
                                return

                        elif returnValue == "com_144":
                                cmdlist = []                                      
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia801501.us.archive.org/14/items/aminovitchi5050_yahoo_Files/Korea_12_udp.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='Korea_12_udp', cmdlist=cmdlist, finishedCallback=None)
                                return

                        elif returnValue == "com_145":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia801501.us.archive.org/14/items/aminovitchi5050_yahoo_Files/Korea_13_tcp.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='Korea_13_tcp', cmdlist=cmdlist, finishedCallback=None)
                                return

                        elif returnValue == "com_146":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia801501.us.archive.org/14/items/aminovitchi5050_yahoo_Files/Korea_13_udp.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='Korea_13_udp', cmdlist=cmdlist, finishedCallback=None)
                                return

                        elif returnValue == "com_147":
                                cmdlist = []                                      
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia801501.us.archive.org/14/items/aminovitchi5050_yahoo_Files/Korea_14_tcp.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='Korea_14_tcp', cmdlist=cmdlist, finishedCallback=None)
                                return

                        elif returnValue == "com_148":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia801501.us.archive.org/14/items/aminovitchi5050_yahoo_Files/Korea_14_udp.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='Korea_14_udp', cmdlist=cmdlist, finishedCallback=None)
                                return

                        elif returnValue == "com_149":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia801501.us.archive.org/14/items/aminovitchi5050_yahoo_Files/Korea_15_tcp.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='Korea_15_tcp', cmdlist=cmdlist, finishedCallback=None)
                                return

                        elif returnValue == "com_150":
                                cmdlist = []                                      
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia801501.us.archive.org/14/items/aminovitchi5050_yahoo_Files/Korea_15_udp.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='Korea_15_udp', cmdlist=cmdlist, finishedCallback=None)
                                return

                        elif returnValue == "com_151":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia801501.us.archive.org/14/items/aminovitchi5050_yahoo_Files/Korea_16_tcp.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='Korea_16_tcp', cmdlist=cmdlist, finishedCallback=None)
                                return

                        elif returnValue == "com_152":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia801501.us.archive.org/14/items/aminovitchi5050_yahoo_Files/Korea_16_udp.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='Korea_16_udp', cmdlist=cmdlist, finishedCallback=None)
                                return

                        elif returnValue == "com_153":
                                cmdlist = []                                      
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia801501.us.archive.org/14/items/aminovitchi5050_yahoo_Files/Korea_17_tcp.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='Korea_17_tcp', cmdlist=cmdlist, finishedCallback=None)
                                return

                        elif returnValue == "com_154":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia801501.us.archive.org/14/items/aminovitchi5050_yahoo_Files/Korea_17_udp.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='Korea_17_udp', cmdlist=cmdlist, finishedCallback=None)
                                return

                        elif returnValue == "com_155":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia801501.us.archive.org/14/items/aminovitchi5050_yahoo_Files/Korea_18_tcp.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='Korea_18_tcp', cmdlist=cmdlist, finishedCallback=None)
                                return

                        elif returnValue == "com_156":
                                cmdlist = []                                      
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia801501.us.archive.org/14/items/aminovitchi5050_yahoo_Files/Korea_18_udp.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='Korea_18_udp', cmdlist=cmdlist, finishedCallback=None)
                                return

                        elif returnValue == "com_157":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia801501.us.archive.org/14/items/aminovitchi5050_yahoo_Files/Korea_189_tcp.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='Korea_19_tcp', cmdlist=cmdlist, finishedCallback=None)
                                return

                        elif returnValue == "com_158":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia801501.us.archive.org/14/items/aminovitchi5050_yahoo_Files/Korea_19_udp.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='Korea_19_udp', cmdlist=cmdlist, finishedCallback=None)
                                return

                        elif returnValue == "com_159":
                                cmdlist = []                                      
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia801501.us.archive.org/14/items/aminovitchi5050_yahoo_Files/Korea_20_tcp.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='Korea_20_tcp', cmdlist=cmdlist, finishedCallback=None)
                                return

                        elif returnValue == "com_160":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia801501.us.archive.org/14/items/aminovitchi5050_yahoo_Files/Korea_20_udp.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='Korea_20_udp', cmdlist=cmdlist, finishedCallback=None)
                                return

                        elif returnValue == "com_161":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia801501.us.archive.org/14/items/aminovitchi5050_yahoo_Files/Korea_21_tcp.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='Korea_21_tcp', cmdlist=cmdlist, finishedCallback=None)
                                return

                        elif returnValue == "com_162":
                                cmdlist = []                                      
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia801501.us.archive.org/14/items/aminovitchi5050_yahoo_Files/Korea_21_udp.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='Korea_21_udp', cmdlist=cmdlist, finishedCallback=None)
                                return

                        elif returnValue == "com_163":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia801501.us.archive.org/14/items/aminovitchi5050_yahoo_Files/Korea_22_tcp.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='Korea_22_tcp', cmdlist=cmdlist, finishedCallback=None)
                                return

                        elif returnValue == "com_164":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia801501.us.archive.org/14/items/aminovitchi5050_yahoo_Files/Korea_22_udp.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='Korea_22_udp', cmdlist=cmdlist, finishedCallback=None)
                                return

                        elif returnValue == "com_165":
                                cmdlist = []                                      
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia801501.us.archive.org/14/items/aminovitchi5050_yahoo_Files/Korea_23_tcp.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='Korea_23_tcp', cmdlist=cmdlist, finishedCallback=None)
                                return
                                
                        elif returnValue == "com_166":
                                cmdlist = []                                      
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia801501.us.archive.org/14/items/aminovitchi5050_yahoo_Files/Korea_23_udp.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='Korea_23_udp', cmdlist=cmdlist, finishedCallback=None)
                                return

                        elif returnValue == "com_167":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia801501.us.archive.org/14/items/aminovitchi5050_yahoo_Files/Korea_24_tcp.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='Korea_24_tcp', cmdlist=cmdlist, finishedCallback=None)
                                return

                        elif returnValue == "com_168":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia801501.us.archive.org/14/items/aminovitchi5050_yahoo_Files/Korea_24_udp.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='Korea_24_udp', cmdlist=cmdlist, finishedCallback=None)
                                return

                        elif returnValue == "com_169":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia801501.us.archive.org/14/items/aminovitchi5050_yahoo_Files/Korea_25_tcp.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='Korea_25_tcp', cmdlist=cmdlist, finishedCallback=None)
                                return

                        elif returnValue == "com_170":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia801501.us.archive.org/14/items/aminovitchi5050_yahoo_Files/Korea_25_udp.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='Korea_25_udp', cmdlist=cmdlist, finishedCallback=None)
                                return

                        elif returnValue == "com_171":
                                cmdlist = []                                      
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia801501.us.archive.org/14/items/aminovitchi5050_yahoo_Files/Korea_26_tcp.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='Korea_26_tcp', cmdlist=cmdlist, finishedCallback=None)
                                return

                        elif returnValue == "com_172":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia801501.us.archive.org/14/items/aminovitchi5050_yahoo_Files/Korea_26_udp.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='Korea_26_udp', cmdlist=cmdlist, finishedCallback=None)
                                return

                        elif returnValue == "com_173":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia801501.us.archive.org/14/items/aminovitchi5050_yahoo_Files/Korea_27_tcp.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='Korea_27_tcp', cmdlist=cmdlist, finishedCallback=None)
                                return

                        elif returnValue == "com_174":
                                cmdlist = []                                      
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia801501.us.archive.org/14/items/aminovitchi5050_yahoo_Files/Korea_27_udp.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='Korea_27_udp', cmdlist=cmdlist, finishedCallback=None)
                                return

                        elif returnValue == "com_175":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia801501.us.archive.org/14/items/aminovitchi5050_yahoo_Files/Korea_28_tcp.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='Korea_28_tcp', cmdlist=cmdlist, finishedCallback=None)
                                return

                        elif returnValue == "com_176":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia801501.us.archive.org/14/items/aminovitchi5050_yahoo_Files/Korea_28_udp.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='Korea_28_udp', cmdlist=cmdlist, finishedCallback=None)
                                return

                        elif returnValue == "com_177":
                                cmdlist = []                                      
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia801501.us.archive.org/14/items/aminovitchi5050_yahoo_Files/Korea_29_tcp.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='Korea_29_tcp', cmdlist=cmdlist, finishedCallback=None)
                                return

                        elif returnValue == "com_178":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia801501.us.archive.org/14/items/aminovitchi5050_yahoo_Files/Korea_29_udp.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='Korea_29_udp', cmdlist=cmdlist, finishedCallback=None)
                                return

                        elif returnValue == "com_179":
                                cmdlist = []                                      
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia801501.us.archive.org/14/items/aminovitchi5050_yahoo_Files/Korea_30_tcp.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='Korea_30_tcp', cmdlist=cmdlist, finishedCallback=None)
                                return

                        elif returnValue == "com_180":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia801501.us.archive.org/14/items/aminovitchi5050_yahoo_Files/Korea_30_udp.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='Korea_30_udp', cmdlist=cmdlist, finishedCallback=None)
                                return

                        elif returnValue == "com_181":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia801501.us.archive.org/14/items/aminovitchi5050_yahoo_Files/Korea_31_tcp.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='Korea_31_tcp', cmdlist=cmdlist, finishedCallback=None)
                                return

                        elif returnValue == "com_182":
                                cmdlist = []                                      
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia801501.us.archive.org/14/items/aminovitchi5050_yahoo_Files/Korea_31_udp.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='Korea_31_udp', cmdlist=cmdlist, finishedCallback=None)
                                return

                        elif returnValue == "com_183":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia801501.us.archive.org/14/items/aminovitchi5050_yahoo_Files/Korea_32_tcp.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='Korea_32_tcp', cmdlist=cmdlist, finishedCallback=None)
                                return

                        elif returnValue == "com_184":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia801501.us.archive.org/14/items/aminovitchi5050_yahoo_Files/Korea_32_udp.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='Korea_32_udp', cmdlist=cmdlist, finishedCallback=None)
                                return

                        elif returnValue == "com_185":
                                cmdlist = []                                      
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia801501.us.archive.org/14/items/aminovitchi5050_yahoo_Files/Korea_33_tcp.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='Korea_33_tcp', cmdlist=cmdlist, finishedCallback=None)
                                return

                        elif returnValue == "com_186":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia801501.us.archive.org/14/items/aminovitchi5050_yahoo_Files/Korea_33_udp.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='Korea_33_udp', cmdlist=cmdlist, finishedCallback=None)
                                return

                        elif returnValue == "com_187":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia801501.us.archive.org/14/items/aminovitchi5050_yahoo_Files/Korea_34_tcp.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='Korea_34_tcp', cmdlist=cmdlist, finishedCallback=None)
                                return

                        elif returnValue == "com_188":
                                cmdlist = []                                      
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia801501.us.archive.org/14/items/aminovitchi5050_yahoo_Files/Korea_34_udp.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='Korea_34_udp', cmdlist=cmdlist, finishedCallback=None)
                                return

                        elif returnValue == "com_189":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia801501.us.archive.org/14/items/aminovitchi5050_yahoo_Files/Korea_35_tcp.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='Korea_35_tcp', cmdlist=cmdlist, finishedCallback=None)
                                return

                        elif returnValue == "com_190":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia801501.us.archive.org/14/items/aminovitchi5050_yahoo_Files/Korea_35_udp.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='Korea_35_udp', cmdlist=cmdlist, finishedCallback=None)
                                return

                        elif returnValue == "com_191":
                                cmdlist = []                                      
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia801501.us.archive.org/14/items/aminovitchi5050_yahoo_Files/Korea_36_tcp.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='Korea_36_tcp', cmdlist=cmdlist, finishedCallback=None)
                                return

                        elif returnValue == "com_192":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia801501.us.archive.org/14/items/aminovitchi5050_yahoo_Files/Korea_36_udp.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='Korea_36_udp', cmdlist=cmdlist, finishedCallback=None)
                                return

                        elif returnValue == "com_193":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia801501.us.archive.org/14/items/aminovitchi5050_yahoo_Files/Korea_37_tcp.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='Korea_37_tcp', cmdlist=cmdlist, finishedCallback=None)
                                return

                        elif returnValue == "com_194":
                                cmdlist = []                                      
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia801501.us.archive.org/14/items/aminovitchi5050_yahoo_Files/Korea_37_udp.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='Korea_37_udp', cmdlist=cmdlist, finishedCallback=None)
                                return

                        elif returnValue == "com_195":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia801501.us.archive.org/14/items/aminovitchi5050_yahoo_Files/Korea_38_tcp.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='Korea_38_tcp', cmdlist=cmdlist, finishedCallback=None)
                                return

                        elif returnValue == "com_196":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia801501.us.archive.org/14/items/aminovitchi5050_yahoo_Files/Korea_38_udp.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='Korea_38_udp', cmdlist=cmdlist, finishedCallback=None)
                                return

                        elif returnValue == "com_197":
                                cmdlist = []                                      
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia801501.us.archive.org/14/items/aminovitchi5050_yahoo_Files/Korea_39_tcp.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='Korea_39_tcp', cmdlist=cmdlist, finishedCallback=None)
                                return

                        elif returnValue == "com_198":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia801501.us.archive.org/14/items/aminovitchi5050_yahoo_Files/Korea_39_udp.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='Korea_39_udp', cmdlist=cmdlist, finishedCallback=None)
                                return

                        elif returnValue == "com_199":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia801501.us.archive.org/14/items/aminovitchi5050_yahoo_Files/Korea_40_tcp.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='Korea_40_tcp', cmdlist=cmdlist, finishedCallback=None)
                                return

                        elif returnValue == "com_200":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia801501.us.archive.org/14/items/aminovitchi5050_yahoo_Files/Korea_40_udp.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='Korea_40_udp', cmdlist=cmdlist, finishedCallback=None)
                                return

                        elif returnValue == "com_201":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia801501.us.archive.org/14/items/aminovitchi5050_yahoo_Files/Korea_41_tcp.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='Korea_41_tcp', cmdlist=cmdlist, finishedCallback=None)
                                return

                        elif returnValue == "com_202":
                                cmdlist = []                                      
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia801501.us.archive.org/14/items/aminovitchi5050_yahoo_Files/Korea_41_udp.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='Korea_41_udp', cmdlist=cmdlist, finishedCallback=None)
                                return

                        elif returnValue == "com_203":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia801501.us.archive.org/14/items/aminovitchi5050_yahoo_Files/Korea_42_tcp.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='Korea_42_tcp', cmdlist=cmdlist, finishedCallback=None)
                                return

                        elif returnValue == "com_204":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia801501.us.archive.org/14/items/aminovitchi5050_yahoo_Files/Korea_42_udp.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='Korea_42_udp', cmdlist=cmdlist, finishedCallback=None)
                                return

                        elif returnValue == "com_205":
                                cmdlist = []                                      
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia801501.us.archive.org/14/items/aminovitchi5050_yahoo_Files/Korea_43_tcp.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='Korea_43_tcp', cmdlist=cmdlist, finishedCallback=None)
                                return

                        elif returnValue == "com_206":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia801501.us.archive.org/14/items/aminovitchi5050_yahoo_Files/Korea_43_udp.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='Korea_43_udp', cmdlist=cmdlist, finishedCallback=None)
                                return

                        elif returnValue == "com_207":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia801501.us.archive.org/14/items/aminovitchi5050_yahoo_Files/Korea_44_tcp.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='Korea_44_tcp', cmdlist=cmdlist, finishedCallback=None)
                                return

                        elif returnValue == "com_208":
                                cmdlist = []                                      
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia801501.us.archive.org/14/items/aminovitchi5050_yahoo_Files/Korea_44_udp.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='Korea_44_udp', cmdlist=cmdlist, finishedCallback=None)
                                return

                        elif returnValue == "com_209":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia801501.us.archive.org/14/items/aminovitchi5050_yahoo_Files/Korea_45_tcp.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='Korea_45_tcp', cmdlist=cmdlist, finishedCallback=None)
                                return

                        elif returnValue == "com_210":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia801501.us.archive.org/14/items/aminovitchi5050_yahoo_Files/Korea_45_udp.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='Korea_45_udp', cmdlist=cmdlist, finishedCallback=None)
                                return

                        elif returnValue == "com_211":
                                cmdlist = []                                      
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia801501.us.archive.org/14/items/aminovitchi5050_yahoo_Files/Korea_46_tcp.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='Korea_46_tcp', cmdlist=cmdlist, finishedCallback=None)
                                return

                        elif returnValue == "com_212":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia801501.us.archive.org/14/items/aminovitchi5050_yahoo_Files/Korea_46_udp.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='Korea_46_udp', cmdlist=cmdlist, finishedCallback=None)
                                return

                        elif returnValue == "com_213":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia801501.us.archive.org/14/items/aminovitchi5050_yahoo_Files/Korea_47_tcp.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='Korea_47_tcp', cmdlist=cmdlist, finishedCallback=None)
                                return

                        elif returnValue == "com_214":
                                cmdlist = []                                      
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia801501.us.archive.org/14/items/aminovitchi5050_yahoo_Files/Korea_47_udp.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='Korea_47_udp', cmdlist=cmdlist, finishedCallback=None)
                                return

                        elif returnValue == "com_215":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia801501.us.archive.org/14/items/aminovitchi5050_yahoo_Files/Korea_48_tcp.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='Korea_48_tcp', cmdlist=cmdlist, finishedCallback=None)
                                return

                        elif returnValue == "com_216":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia801501.us.archive.org/14/items/aminovitchi5050_yahoo_Files/Korea_48_udp.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='Korea_48_udp', cmdlist=cmdlist, finishedCallback=None)
                                return

                        elif returnValue == "com_217":
                                cmdlist = []                                      
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia801501.us.archive.org/14/items/aminovitchi5050_yahoo_Files/Korea_49_tcp.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='Korea_49_tcp', cmdlist=cmdlist, finishedCallback=None)
                                return

                        elif returnValue == "com_218":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia801501.us.archive.org/14/items/aminovitchi5050_yahoo_Files/Korea_49_udp.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='Korea_49_udp', cmdlist=cmdlist, finishedCallback=None)
                                return

                        elif returnValue == "com_219":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia801501.us.archive.org/14/items/aminovitchi5050_yahoo_Files/Korea_50_tcp.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='Korea_50_tcp', cmdlist=cmdlist, finishedCallback=None)
                                return

                        elif returnValue == "com_220":
                                cmdlist = []                                      
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia801501.us.archive.org/14/items/aminovitchi5050_yahoo_Files/Korea_50_udp.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='Korea_50_udp', cmdlist=cmdlist, finishedCallback=None)
                                return

                        elif returnValue == "com_221":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia801508.us.archive.org/19/items/world_201904/Korea_tcp.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='Korea_tcp', cmdlist=cmdlist, finishedCallback=None)
                                return

                        elif returnValue == "com_222":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia801508.us.archive.org/19/items/world_201904/Korea_udp.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='Korea_udp', cmdlist=cmdlist, finishedCallback=None)
                                return

                        elif returnValue == "com_223":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia801508.us.archive.org/19/items/world_201904/USA_tcp.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='USA_tcp', cmdlist=cmdlist, finishedCallback=None)
                                return

                        elif returnValue == "com_224":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia801508.us.archive.org/19/items/world_201904/USA_udp.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='USA_udp', cmdlist=cmdlist, finishedCallback=None)
                                return

                        elif returnValue == "com_225":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia801508.us.archive.org/19/items/world_201904/Taiwan_tcp.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='Taiwan_tcp', cmdlist=cmdlist, finishedCallback=None)
                                return

                        elif returnValue == "com_226":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia801508.us.archive.org/19/items/world_201904/Taiwan_udp.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='Taiwan_udp', cmdlist=cmdlist, finishedCallback=None)
                                return

                        elif returnValue == "com_227":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia801508.us.archive.org/19/items/world_201904/China_tcp.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='China_tcp', cmdlist=cmdlist, finishedCallback=None)
                                return

                        elif returnValue == "com_228":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia801508.us.archive.org/19/items/world_201904/China_udp.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='China_udp', cmdlist=cmdlist, finishedCallback=None)
                                return

                        elif returnValue == "com_229":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia801508.us.archive.org/19/items/world_201904/Japan_tcp.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='Japan_tcp', cmdlist=cmdlist, finishedCallback=None)
                                return
                                
                        elif returnValue == "com_230":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia801508.us.archive.org/19/items/world_201904/Japan_udp.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='Japan_udp', cmdlist=cmdlist, finishedCallback=None)
                                return

                        elif returnValue == "com_231":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia801508.us.archive.org/19/items/world_201904/France_tcp.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='France_tcp', cmdlist=cmdlist, finishedCallback=None)
                                return

                        elif returnValue == "com_232":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia801508.us.archive.org/19/items/world_201904/France_udp.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='France_udp', cmdlist=cmdlist, finishedCallback=None)
                                return

                        elif returnValue == "com_233":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia801508.us.archive.org/19/items/world_201904/Indonesia_tcp.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='Indonesia_tcp', cmdlist=cmdlist, finishedCallback=None)
                                return

                        elif returnValue == "com_234":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia801508.us.archive.org/19/items/world_201904/Indonesia_udp.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='Indonesia_udp', cmdlist=cmdlist, finishedCallback=None)
                                return

                        elif returnValue == "com_235":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia801508.us.archive.org/19/items/world_201904/Thailand_tcp.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='Thailand_tcp', cmdlist=cmdlist, finishedCallback=None)
                                return

                        elif returnValue == "com_236":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia801508.us.archive.org/19/items/world_201904/Thailand_udp.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='Thailand_udp', cmdlist=cmdlist, finishedCallback=None)
                                return

                        elif returnValue == "com_237":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia801508.us.archive.org/19/items/world_201904/UAE_tcp.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='UAE_tcp', cmdlist=cmdlist, finishedCallback=None)
                                return

                        elif returnValue == "com_238":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia801508.us.archive.org/19/items/world_201904/UAE_udp.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='UAE_udp', cmdlist=cmdlist, finishedCallback=None)
                                return

                        elif returnValue == "com_239":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia801508.us.archive.org/19/items/world_201904/Malaysia_tcp.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='Malaysia_tcp', cmdlist=cmdlist, finishedCallback=None)
                                return

                        elif returnValue == "com_240":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia801508.us.archive.org/19/items/world_201904/Malaysia_udp.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='Malaysia_udp', cmdlist=cmdlist, finishedCallback=None)
                                return

                        elif returnValue == "com_241":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia801508.us.archive.org/19/items/world_201904/Iran_tcp.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='Iran_tcp', cmdlist=cmdlist, finishedCallback=None)
                                return

                        elif returnValue == "com_242":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia801508.us.archive.org/19/items/world_201904/Iran_udp.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='Iran_udp', cmdlist=cmdlist, finishedCallback=None)
                                return

                        elif returnValue == "com_243":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia801508.us.archive.org/19/items/world_201904/Russia_tcp.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='Russia_tcp', cmdlist=cmdlist, finishedCallback=None)
                                return

                        elif returnValue == "com_244":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia801508.us.archive.org/19/items/world_201904/Russia_udp.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='Russia_udp', cmdlist=cmdlist, finishedCallback=None)
                                return

                        elif returnValue == "com_245":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia801508.us.archive.org/19/items/world_201904/Viet Nam_tcp.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='Viet Nam_tcp', cmdlist=cmdlist, finishedCallback=None)
                                return

                        elif returnValue == "com_246":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia801508.us.archive.org/19/items/world_201904/Viet Nam_udp.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='Viet Nam_udp', cmdlist=cmdlist, finishedCallback=None)
                                return

                        elif returnValue == "com_247":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia801508.us.archive.org/19/items/world_201904/Hong Kong_tcp.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='Hong Kong_tcp', cmdlist=cmdlist, finishedCallback=None)
                                return

                        elif returnValue == "com_248":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia801508.us.archive.org/19/items/world_201904/Hong Kong_udp.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='Hong Kong_udp', cmdlist=cmdlist, finishedCallback=None)
                                return

                        elif returnValue == "com_249":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia801508.us.archive.org/19/items/world_201904/India_tcp.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='India_tcp', cmdlist=cmdlist, finishedCallback=None)
                                return

                        elif returnValue == "com_250":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia801508.us.archive.org/19/items/world_201904/India_udp.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='India_udp', cmdlist=cmdlist, finishedCallback=None)
                                return

                        elif returnValue == "com_251":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia801508.us.archive.org/19/items/world_201904/Turkmenistan_tcp.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='Turkmenistan_tcp', cmdlist=cmdlist, finishedCallback=None)
                                return

                        elif returnValue == "com_252":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia801508.us.archive.org/19/items/world_201904/Turkmenistan_udp.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='Turkmenistan_udp', cmdlist=cmdlist, finishedCallback=None)
                                return

                        elif returnValue == "com_253":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia801508.us.archive.org/19/items/world_201904/Canada_tcp.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='Canada_tcp', cmdlist=cmdlist, finishedCallback=None)
                                return

                        elif returnValue == "com_254":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia801508.us.archive.org/19/items/world_201904/Canada_udp.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='Canada_udp', cmdlist=cmdlist, finishedCallback=None)
                                return

                        elif returnValue == "com_255":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia801508.us.archive.org/19/items/world_201904/Saudi Arabia_tcp.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='Saudi Arabia_tcp', cmdlist=cmdlist, finishedCallback=None)
                                return

                        elif returnValue == "com_256":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia801508.us.archive.org/19/items/world_201904/Saudi Arabia_udp.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='Saudi Arabia_udp', cmdlist=cmdlist, finishedCallback=None)
                                return

                        elif returnValue == "com_257":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia801508.us.archive.org/19/items/world_201904/Philippines_tcp.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='Philippines_tcp', cmdlist=cmdlist, finishedCallback=None)
                                return

                        elif returnValue == "com_258":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia801508.us.archive.org/19/items/world_201904/Philippines_udp.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='Philippines_udp', cmdlist=cmdlist, finishedCallback=None)
                                return

                        elif returnValue == "com_259":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia801508.us.archive.org/19/items/world_201904/Ukraine_tcp.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='Ukraine_tcp', cmdlist=cmdlist, finishedCallback=None)
                                return

                        elif returnValue == "com_260":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia801508.us.archive.org/19/items/world_201904/Ukraine_udp.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='Ukraine_udp', cmdlist=cmdlist, finishedCallback=None)
                                return

                        elif returnValue == "com_261":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia801508.us.archive.org/19/items/world_201904/Singapore_tcp.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='Singapore_tcp', cmdlist=cmdlist, finishedCallback=None)
                                return

                        elif returnValue == "com_262":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia801508.us.archive.org/19/items/world_201904/Singapore_udp.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='Singapore_udp', cmdlist=cmdlist, finishedCallback=None)
                                return

                        elif returnValue == "com_263":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia801508.us.archive.org/19/items/world_201904/UK_tcp.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='UK_tcp', cmdlist=cmdlist, finishedCallback=None)
                                return

                        elif returnValue == "com_264":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia801508.us.archive.org/19/items/world_201904/UK_tcp.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='UK_udp', cmdlist=cmdlist, finishedCallback=None)
                                return

                        elif returnValue == "com_265":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia801508.us.archive.org/19/items/world_201904/Germany_tcp.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='Germany_tcp', cmdlist=cmdlist, finishedCallback=None)
                                return

                        elif returnValue == "com_266":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia801508.us.archive.org/19/items/world_201904/Germany_udp.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='Germany_udp', cmdlist=cmdlist, finishedCallback=None)
                                return

                        elif returnValue == "com_267":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia801508.us.archive.org/19/items/world_201904/Australia_tcp.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='Australia_tcp', cmdlist=cmdlist, finishedCallback=None)
                                return

                        elif returnValue == "com_268":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia801508.us.archive.org/19/items/world_201904/Australia_udp.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='Australia_udp', cmdlist=cmdlist, finishedCallback=None)
                                return

                        elif returnValue == "com_269":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia801508.us.archive.org/19/items/world_201904/Turkey_tcp.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='Turkey_tcp', cmdlist=cmdlist, finishedCallback=None)
                                return

                        elif returnValue == "com_270":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia801508.us.archive.org/19/items/world_201904/Turkey_udp.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='Turkey_udp', cmdlist=cmdlist, finishedCallback=None)
                                return

                        elif returnValue == "com_271":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia801508.us.archive.org/19/items/world_201904/Brazil_tcp.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='Brazil_tcp', cmdlist=cmdlist, finishedCallback=None)
                                return

                        elif returnValue == "com_272":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia801508.us.archive.org/19/items/world_201904/Brazil_udp.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='Brazil_udp', cmdlist=cmdlist, finishedCallback=None)
                                return

                        elif returnValue == "com_273":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia801508.us.archive.org/19/items/world_201904/Mexico_tcp.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='Mexico_tcp', cmdlist=cmdlist, finishedCallback=None)
                                return

                        elif returnValue == "com_274":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia801508.us.archive.org/19/items/world_201904/Mexico_udp.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='Mexico_udp', cmdlist=cmdlist, finishedCallback=None)
                                return

                        elif returnValue == "com_275":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia801508.us.archive.org/19/items/world_201904/Syria_tcp.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='Syria_tcp', cmdlist=cmdlist, finishedCallback=None)
                                return

                        elif returnValue == "com_276":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia801508.us.archive.org/19/items/world_201904/Syria_udp.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='Syria_udp', cmdlist=cmdlist, finishedCallback=None)
                                return

                        elif returnValue == "com_277":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia801508.us.archive.org/19/items/world_201904/Pakistan_tcp.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='Pakistan_tcp', cmdlist=cmdlist, finishedCallback=None)
                                return

                        elif returnValue == "com_278":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia801508.us.archive.org/19/items/world_201904/Pakistan_udp.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='Pakistan_udp', cmdlist=cmdlist, finishedCallback=None)
                                return

                        elif returnValue == "com_279":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia801508.us.archive.org/19/items/world_201904/Nigeria_tcp.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='Nigeria_tcp', cmdlist=cmdlist, finishedCallback=None)
                                return

                        elif returnValue == "com_280":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia801508.us.archive.org/19/items/world_201904/Nigeria_udp.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='Nigeria_udp', cmdlist=cmdlist, finishedCallback=None)
                                return

                        elif returnValue == "com_281":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia801508.us.archive.org/19/items/world_201904/Austria_tcp.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='Austria_tcp', cmdlist=cmdlist, finishedCallback=None)
                                return

                        elif returnValue == "com_282":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia801508.us.archive.org/19/items/world_201904/Austria_udp.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='Austria_udp', cmdlist=cmdlist, finishedCallback=None)
                                return

                        elif returnValue == "com_283":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia801508.us.archive.org/19/items/world_201904/Colombia_tcp.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='Colombia_tcp', cmdlist=cmdlist, finishedCallback=None)
                                return

                        elif returnValue == "com_284":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia801508.us.archive.org/19/items/world_201904/Colombia_udp.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='Colombia_udp', cmdlist=cmdlist, finishedCallback=None)
                                return

                        elif returnValue == "com_285":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia801508.us.archive.org/19/items/world_201904/Spain_tcp.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='Spain_tcp', cmdlist=cmdlist, finishedCallback=None)
                                return

                        elif returnValue == "com_286":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia801508.us.archive.org/19/items/world_201904/Spain_udp.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='Spain_udp', cmdlist=cmdlist, finishedCallback=None)
                                return

                        elif returnValue == "com_287":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia801508.us.archive.org/19/items/world_201904/Iraq_tcp.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='Iraq_tcp', cmdlist=cmdlist, finishedCallback=None)
                                return

                        elif returnValue == "com_288":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia801508.us.archive.org/19/items/world_201904/Iraq_udp.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='Iraq_udp', cmdlist=cmdlist, finishedCallback=None)
                                return

                        elif returnValue == "com_289":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia801508.us.archive.org/19/items/world_201904/Ecuador_tcp.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='Ecuador_tcp', cmdlist=cmdlist, finishedCallback=None)
                                return

                        elif returnValue == "com_290":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia801508.us.archive.org/19/items/world_201904/Ecuador_udp.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='Ecuador_udp', cmdlist=cmdlist, finishedCallback=None)
                                return

                        elif returnValue == "com_291":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia801508.us.archive.org/19/items/world_201904/Bangladesh_tcp.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='Bangladesh_tcp', cmdlist=cmdlist, finishedCallback=None)
                                return

                        elif returnValue == "com_292":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia801508.us.archive.org/19/items/world_201904/Bangladesh_udp.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='Bangladesh_udp', cmdlist=cmdlist, finishedCallback=None)
                                return

                        elif returnValue == "com_293":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia801508.us.archive.org/19/items/world_201904/Italy_tcp.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='Italy_tcp', cmdlist=cmdlist, finishedCallback=None)
                                return

                        elif returnValue == "com_294":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia801508.us.archive.org/19/items/world_201904/Italy_udp.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='Italy_udp', cmdlist=cmdlist, finishedCallback=None)
                                return

                        elif returnValue == "com_295":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia801508.us.archive.org/19/items/world_201904/Oman_tcp.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='Oman_tcp', cmdlist=cmdlist, finishedCallback=None)
                                return

                        elif returnValue == "com_296":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia801508.us.archive.org/19/items/world_201904/Oman_udp.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='Oman_udp', cmdlist=cmdlist, finishedCallback=None)
                                return

                        elif returnValue == "com_297":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia801508.us.archive.org/19/items/world_201904/Netherlands_tcp.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='Netherlands_tcp', cmdlist=cmdlist, finishedCallback=None)
                                return

                        elif returnValue == "com_298":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia801508.us.archive.org/19/items/world_201904/Netherlands_udp.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='Netherlands_udp', cmdlist=cmdlist, finishedCallback=None)
                                return

                        elif returnValue == "com_299":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia801508.us.archive.org/19/items/world_201904/Argentina_tcp.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='Argentina_tcp', cmdlist=cmdlist, finishedCallback=None)
                                return

                        elif returnValue == "com_300":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia801508.us.archive.org/19/items/world_201904/Argentina_udp.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='Argentina_udp', cmdlist=cmdlist, finishedCallback=None)
                                return

                        elif returnValue == "com_301":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia801508.us.archive.org/19/items/world_201904/Egypt_tcp.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='Egypt_tcp', cmdlist=cmdlist, finishedCallback=None)
                                return

                        elif returnValue == "com_302":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia801508.us.archive.org/19/items/world_201904/Egypt_udp.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='Egypt_udp', cmdlist=cmdlist, finishedCallback=None)
                                return

                        elif returnValue == "com_303":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia801508.us.archive.org/19/items/world_201904/Kazakhstan_tcp.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='Kazakhstan_tcp', cmdlist=cmdlist, finishedCallback=None)
                                return

                        elif returnValue == "com_304":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia801508.us.archive.org/19/items/world_201904/Kazakhstan_udp.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='Kazakhstan_udp', cmdlist=cmdlist, finishedCallback=None)
                                return

                        elif returnValue == "com_305":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia801508.us.archive.org/19/items/world_201904/Venezuela_tcp.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='Venezuela_tcp', cmdlist=cmdlist, finishedCallback=None)
                                return

                        elif returnValue == "com_306":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia801508.us.archive.org/19/items/world_201904/Venezuela_udp.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='Venezuela_udp', cmdlist=cmdlist, finishedCallback=None)
                                return

                        elif returnValue == "com_307":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia801508.us.archive.org/19/items/world_201904/Macau_tcp.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='Macau_tcp', cmdlist=cmdlist, finishedCallback=None)
                                return

                        elif returnValue == "com_308":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia801508.us.archive.org/19/items/world_201904/Macau_udp.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='Macau_udp', cmdlist=cmdlist, finishedCallback=None)
                                return

                        elif returnValue == "com_309":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia801508.us.archive.org/19/items/world_201904/Qatar_tcp.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='Qatar_tcp', cmdlist=cmdlist, finishedCallback=None)
                                return

                        elif returnValue == "com_310":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia801508.us.archive.org/19/items/world_201904/Qatar_udp.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='Qatar_udp', cmdlist=cmdlist, finishedCallback=None)
                                return

                        elif returnValue == "com_311":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia801508.us.archive.org/19/items/world_201904/Chile_tcp.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='Chile_tcp', cmdlist=cmdlist, finishedCallback=None)
                                return

                        elif returnValue == "com_312":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia801508.us.archive.org/19/items/world_201904/Chile_udp.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='Chile_udp', cmdlist=cmdlist, finishedCallback=None)
                                return

                        elif returnValue == "com_313":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia801508.us.archive.org/19/items/world_201904/Peru_tcp.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='Peru_tcp', cmdlist=cmdlist, finishedCallback=None)
                                return

                        elif returnValue == "com_314":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia801508.us.archive.org/19/items/world_201904/Peru_udp.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='Peru_udp', cmdlist=cmdlist, finishedCallback=None)
                                return

                        elif returnValue == "com_315":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia801508.us.archive.org/19/items/world_201904/Algeria_tcp.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='Algeria_tcp', cmdlist=cmdlist, finishedCallback=None)
                                return

                        elif returnValue == "com_316":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia801508.us.archive.org/19/items/world_201904/Algeria_udp.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='Algeria_udp', cmdlist=cmdlist, finishedCallback=None)
                                return

                        elif returnValue == "com_317":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia801508.us.archive.org/19/items/world_201904/New Zealand_tcp.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='New Zealand_tcp', cmdlist=cmdlist, finishedCallback=None)
                                return

                        elif returnValue == "com_318":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia801508.us.archive.org/19/items/world_201904/New Zealand_udp.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='New Zealand_udp', cmdlist=cmdlist, finishedCallback=None)
                                return

                        elif returnValue == "com_319":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia801508.us.archive.org/19/items/world_201904/Morocco_tcp.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='Morocco_tcp', cmdlist=cmdlist, finishedCallback=None)
                                return

                        elif returnValue == "com_320":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia801508.us.archive.org/19/items/world_201904/Morocco_udp.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='Morocco_udp', cmdlist=cmdlist, finishedCallback=None)
                                return

                        elif returnValue == "com_321":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia801508.us.archive.org/19/items/world_201904/Romania_tcp.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='Romania_tcp', cmdlist=cmdlist, finishedCallback=None)
                                return

                        elif returnValue == "com_322":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia801508.us.archive.org/19/items/world_201904/Romania_udp.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='Romania_udp', cmdlist=cmdlist, finishedCallback=None)
                                return

                        elif returnValue == "com_323":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia801508.us.archive.org/19/items/world_201904/Poland_tcp.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='Poland_tcp', cmdlist=cmdlist, finishedCallback=None)
                                return

                        elif returnValue == "com_324":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia801508.us.archive.org/19/items/world_201904/Poland_udp.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='Poland_udp', cmdlist=cmdlist, finishedCallback=None)
                                return

                        elif returnValue == "com_325":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia801508.us.archive.org/19/items/world_201904/South Africa_tcp.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='South Africa_tcp', cmdlist=cmdlist, finishedCallback=None)
                                return

                        elif returnValue == "com_326":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia801508.us.archive.org/19/items/world_201904/South Africa_udp.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='South Africa_udp', cmdlist=cmdlist, finishedCallback=None)
                                return

                        elif returnValue == "com_327":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia801508.us.archive.org/19/items/world_201904/Lao_tcp.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='Lao_tcp', cmdlist=cmdlist, finishedCallback=None)
                                return

                        elif returnValue == "com_328":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia801508.us.archive.org/19/items/world_201904/Lao_udp.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='Lao_udp', cmdlist=cmdlist, finishedCallback=None)
                                return

                        elif returnValue == "com_329":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia801508.us.archive.org/19/items/world_201904/Sweden_tcp.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='Sweden_tcp', cmdlist=cmdlist, finishedCallback=None)
                                return

                        elif returnValue == "com_330":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia801508.us.archive.org/19/items/world_201904/USA_udp.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='Sweden_udp', cmdlist=cmdlist, finishedCallback=None)
                                return

                        elif returnValue == "com_331":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia801508.us.archive.org/19/items/world_201904/Finland_tcp.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='Finland_tcp', cmdlist=cmdlist, finishedCallback=None)
                                return

                        elif returnValue == "com_332":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia801508.us.archive.org/19/items/world_201904/Finland_udp.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='Finland_udp', cmdlist=cmdlist, finishedCallback=None)
                                return

                        elif returnValue == "com_333":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia801508.us.archive.org/19/items/world_201904/Sudan_tcp.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='Sudan_tcp', cmdlist=cmdlist, finishedCallback=None)
                                return

                        elif returnValue == "com_334":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia801508.us.archive.org/19/items/world_201904/Sudan_udp.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='Sudan_udp', cmdlist=cmdlist, finishedCallback=None)
                                return

                        elif returnValue == "com_335":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia801508.us.archive.org/19/items/world_201904/Belgium_tcp.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='Belgium_tcp', cmdlist=cmdlist, finishedCallback=None)
                                return

                        elif returnValue == "com_336":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia801508.us.archive.org/19/items/world_201904/Belgium_udp.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='Belgium_udp', cmdlist=cmdlist, finishedCallback=None)
                                return

                        elif returnValue == "com_337":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia801508.us.archive.org/19/items/world_201904/Ghana_tcp.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='Ghana_tcp', cmdlist=cmdlist, finishedCallback=None)
                                return

                        elif returnValue == "com_338":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia801508.us.archive.org/19/items/world_201904/Ghana_udp.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='Ghana_udp', cmdlist=cmdlist, finishedCallback=None)
                                return

                        elif returnValue == "com_339":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia801508.us.archive.org/19/items/world_201904/Norway_tcp.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='Norway_tcp', cmdlist=cmdlist, finishedCallback=None)
                                return

                        elif returnValue == "com_340":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia801508.us.archive.org/19/items/world_201904/Norway_udp.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='Norway_udp', cmdlist=cmdlist, finishedCallback=None)
                                return

                        elif returnValue == "com_341":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia801508.us.archive.org/19/items/world_201904/Cambodia_tcp.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='Cambodia_tcp', cmdlist=cmdlist, finishedCallback=None)
                                return

                        elif returnValue == "com_342":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia801508.us.archive.org/19/items/world_201904/Cambodia_udp.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='Cambodia_udp', cmdlist=cmdlist, finishedCallback=None)
                                return

                        elif returnValue == "com_343":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia801508.us.archive.org/19/items/world_201904/Kuwait_tcp.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='Kuwait_tcp', cmdlist=cmdlist, finishedCallback=None)
                                return

                        elif returnValue == "com_344":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia801508.us.archive.org/19/items/world_201904/Kuwait_udp.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='Kuwait_udp', cmdlist=cmdlist, finishedCallback=None)
                                return

                        elif returnValue == "com_345":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia801508.us.archive.org/19/items/world_201904/Belarus_tcp.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='Belarus_tcp', cmdlist=cmdlist, finishedCallback=None)
                                return

                        elif returnValue == "com_346":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia801508.us.archive.org/19/items/world_201904/Belarus_udp.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='Belarus_udp', cmdlist=cmdlist, finishedCallback=None)
                                return

                        elif returnValue == "com_347":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia801508.us.archive.org/19/items/world_201904/Myanmar_tcp.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='Myanmar_tcp', cmdlist=cmdlist, finishedCallback=None)
                                return

                        elif returnValue == "com_348":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia801508.us.archive.org/19/items/world_201904/Myanmar_udp.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='Myanmar_udp', cmdlist=cmdlist, finishedCallback=None)
                                return

                        elif returnValue == "com_349":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia801508.us.archive.org/19/items/world_201904/Denmark_tcp.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='Denmark_tcp', cmdlist=cmdlist, finishedCallback=None)
                                return

                        elif returnValue == "com_350":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia801508.us.archive.org/19/items/world_201904/Denmark_udp.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='Denmark_udp', cmdlist=cmdlist, finishedCallback=None)
                                return

                        elif returnValue == "com_351":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia801508.us.archive.org/19/items/world_201904/Tunisia_tcp.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='Tunisia_tcp', cmdlist=cmdlist, finishedCallback=None)
                                return
                                
                        elif returnValue == "com_352":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia801508.us.archive.org/19/items/world_201904/Tunisia_udp.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='Tunisia_udp', cmdlist=cmdlist, finishedCallback=None)
                                return

                        elif returnValue == "com_353":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia801508.us.archive.org/19/items/world_201904/Portugal_tcp.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='Portugal_tcp', cmdlist=cmdlist, finishedCallback=None)
                                return

                        elif returnValue == "com_354":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia801508.us.archive.org/19/items/world_201904/Portugal_udp.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='Portugal_udp', cmdlist=cmdlist, finishedCallback=None)
                                return

                        elif returnValue == "com_355":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia801508.us.archive.org/19/items/world_201904/Czech Republic_tcp.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='Czech Republic_tcp', cmdlist=cmdlist, finishedCallback=None)
                                return

                        elif returnValue == "com_356":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia801508.us.archive.org/19/items/world_201904/Czech Republic_udp.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='Czech Republic_udp', cmdlist=cmdlist, finishedCallback=None)
                                return

                        elif returnValue == "com_357":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia801508.us.archive.org/19/items/world_201904/Switzerland_tcp.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='Switzerland_tcp', cmdlist=cmdlist, finishedCallback=None)
                                return

                        elif returnValue == "com_358":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia801508.us.archive.org/19/items/world_201904/Switzerland_udp.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='Switzerland_udp', cmdlist=cmdlist, finishedCallback=None)
                                return

                        elif returnValue == "com_359":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia801508.us.archive.org/19/items/world_201904/Israel_tcp.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='Israel_tcp', cmdlist=cmdlist, finishedCallback=None)
                                return

                        elif returnValue == "com_360":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia801508.us.archive.org/19/items/world_201904/Israel_udp.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='Israel_udp', cmdlist=cmdlist, finishedCallback=None)
                                return

                        elif returnValue == "com_361":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia801508.us.archive.org/19/items/world_201904/Hungary_tcp.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='Hungary_tcp', cmdlist=cmdlist, finishedCallback=None)
                                return

                        elif returnValue == "com_362":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia801508.us.archive.org/19/items/world_201904/Hungary_udp.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='Hungary_udp', cmdlist=cmdlist, finishedCallback=None)
                                return

                        elif returnValue == "com_363":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia801508.us.archive.org/19/items/world_201904/Dominican_tcp.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='Dominican_tcp', cmdlist=cmdlist, finishedCallback=None)
                                return

                        elif returnValue == "com_364":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia801508.us.archive.org/19/items/world_201904/Dominican_udp.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='Dominican_udp', cmdlist=cmdlist, finishedCallback=None)
                                return

                        elif returnValue == "com_365":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia801508.us.archive.org/19/items/world_201904/Djibouti_tcp.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='Djibouti_tcp', cmdlist=cmdlist, finishedCallback=None)
                                return

                        elif returnValue == "com_366":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia801508.us.archive.org/19/items/world_201904/Djibouti_udp.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='Djibouti_udp', cmdlist=cmdlist, finishedCallback=None)
                                return

                        elif returnValue == "com_367":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia801508.us.archive.org/19/items/world_201904/Jordan_tcp.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='Jordan_tcp', cmdlist=cmdlist, finishedCallback=None)
                                return

                        elif returnValue == "com_368":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia801508.us.archive.org/19/items/world_201904/Jordan_udp.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='Jordan_udp', cmdlist=cmdlist, finishedCallback=None)
                                return

                        elif returnValue == "com_369":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia801508.us.archive.org/19/items/world_201904/Nepal_tcp.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='Nepal_tcp', cmdlist=cmdlist, finishedCallback=None)
                                return

                        elif returnValue == "com_370":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia801508.us.archive.org/19/items/world_201904/Nepal_udp.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='Nepal_udp', cmdlist=cmdlist, finishedCallback=None)
                                return

                        elif returnValue == "com_371":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia801508.us.archive.org/19/items/world_201904/Lithuania_tcp.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='Lithuania_tcp', cmdlist=cmdlist, finishedCallback=None)
                                return

                        elif returnValue == "com_372":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia801508.us.archive.org/19/items/world_201904/Lithuania_udp.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='Lithuania_udp', cmdlist=cmdlist, finishedCallback=None)
                                return

                        elif returnValue == "com_373":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia801508.us.archive.org/19/items/world_201904/Guatemala_tcp.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='Guatemala_tcp', cmdlist=cmdlist, finishedCallback=None)
                                return

                        elif returnValue == "com_374":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia801508.us.archive.org/19/items/world_201904/Guatemala_udp.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='Guatemala_udp', cmdlist=cmdlist, finishedCallback=None)
                                return

                        elif returnValue == "com_375":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia801508.us.archive.org/19/items/world_201904/Bahrain_tcp.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='Bahrain_tcp', cmdlist=cmdlist, finishedCallback=None)
                                return

                        elif returnValue == "com_376":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia801508.us.archive.org/19/items/world_201904/Bahrain_udp.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='Bahrain_udp', cmdlist=cmdlist, finishedCallback=None)
                                return

                        elif returnValue == "com_377":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia801508.us.archive.org/19/items/world_201904/Greece_tcp.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='Greece_tcp', cmdlist=cmdlist, finishedCallback=None)
                                return

                        elif returnValue == "com_378":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia801508.us.archive.org/19/items/world_201904/Greece_udp.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='Greece_udp', cmdlist=cmdlist, finishedCallback=None)
                                return

                        elif returnValue == "com_379":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia801508.us.archive.org/19/items/world_201904/Palestine_tcp.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='Palestine_tcp', cmdlist=cmdlist, finishedCallback=None)
                                return

                        elif returnValue == "com_380":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia801508.us.archive.org/19/items/world_201904/Palestine_udp.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='Palestine_udp', cmdlist=cmdlist, finishedCallback=None)
                                return

                        elif returnValue == "com_381":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia801508.us.archive.org/19/items/world_201904/Sri Lanka_tcp.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='Sri Lanka_tcp', cmdlist=cmdlist, finishedCallback=None)
                                return

                        elif returnValue == "com_382":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia801508.us.archive.org/19/items/world_201904/Sri Lanka_udp.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='Sri Lanka_udp', cmdlist=cmdlist, finishedCallback=None)
                                return

                        elif returnValue == "com_383":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia801508.us.archive.org/19/items/world_201904/Bolivia_tcp.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='Bolivia_tcp', cmdlist=cmdlist, finishedCallback=None)
                                return

                        elif returnValue == "com_384":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia801508.us.archive.org/19/items/world_201904/Bolivia_udp.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='Bolivia_udp', cmdlist=cmdlist, finishedCallback=None)
                                return

                        elif returnValue == "com_385":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia801508.us.archive.org/19/items/world_201904/Serbia_tcp.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='Serbia_tcp', cmdlist=cmdlist, finishedCallback=None)
                                return

                        elif returnValue == "com_386":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia801508.us.archive.org/19/items/world_201904/Serbia_udp.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='Serbia_udp', cmdlist=cmdlist, finishedCallback=None)
                                return

                        elif returnValue == "com_387":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia801508.us.archive.org/19/items/world_201904/Mongolia_tcp.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='Mongolia_tcp', cmdlist=cmdlist, finishedCallback=None)
                                return

                        elif returnValue == "com_388":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia801508.us.archive.org/19/items/world_201904/Mongolia_udp.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='Mongolia_udp', cmdlist=cmdlist, finishedCallback=None)
                                return

                        elif returnValue == "com_389":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia801508.us.archive.org/19/items/world_201904/Kenya_tcp.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='Kenya_tcp', cmdlist=cmdlist, finishedCallback=None)
                                return

                        elif returnValue == "com_390":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia801508.us.archive.org/19/items/world_201904/Kenya_udp.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='Kenya_udp', cmdlist=cmdlist, finishedCallback=None)
                                return

                        elif returnValue == "com_391":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia801508.us.archive.org/19/items/world_201904/Darussalam_tcp.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='Darussalam_tcp', cmdlist=cmdlist, finishedCallback=None)
                                return

                        elif returnValue == "com_392":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia801508.us.archive.org/19/items/world_201904/Darussalam_udp.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='Darussalam_udp', cmdlist=cmdlist, finishedCallback=None)
                                return

                        elif returnValue == "com_393":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia801508.us.archive.org/19/items/world_201904/Latvia_tcp.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='Latvia_tcp', cmdlist=cmdlist, finishedCallback=None)
                                return

                        elif returnValue == "com_394":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia801508.us.archive.org/19/items/world_201904/Latvia_udp.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='Latvia_udp', cmdlist=cmdlist, finishedCallback=None)
                                return

                        elif returnValue == "com_395":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia801508.us.archive.org/19/items/world_201904/Libya_tcp.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='Libya_tcp', cmdlist=cmdlist, finishedCallback=None)
                                return

                        elif returnValue == "com_396":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia801508.us.archive.org/19/items/world_201904/Libya_udp.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='Libya_udp', cmdlist=cmdlist, finishedCallback=None)
                                return

                        elif returnValue == "com_397":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia801508.us.archive.org/19/items/world_201904/Bulgaria_tcp.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='Bulgaria_tcp', cmdlist=cmdlist, finishedCallback=None)
                                return

                        elif returnValue == "com_398":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia801508.us.archive.org/19/items/world_201904/Bulgaria_udp.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='Bulgaria_udp', cmdlist=cmdlist, finishedCallback=None)
                                return

                        elif returnValue == "com_399":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia801508.us.archive.org/19/items/world_201904/Croatia_tcp.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='Croatia_tcp', cmdlist=cmdlist, finishedCallback=None)
                                return

                        elif returnValue == "com_400":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia801508.us.archive.org/19/items/world_201904/Croatia_udp.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='Croatia_udp', cmdlist=cmdlist, finishedCallback=None)
                                return

                        elif returnValue == "com_401":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia801508.us.archive.org/19/items/world_201904/Cote D'ivoire_tcp.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='Cote Divoire_tcp', cmdlist=cmdlist, finishedCallback=None)
                                return

                        elif returnValue == "com_402":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia801508.us.archive.org/19/items/world_201904/Cote D'ivoire_udp.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='Cote Divoire_udp', cmdlist=cmdlist, finishedCallback=None)
                                return

                        elif returnValue == "com_403":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia801508.us.archive.org/19/items/world_201904/Ireland_tcp.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='Ireland_tcp', cmdlist=cmdlist, finishedCallback=None)
                                return

                        elif returnValue == "com_404":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia801508.us.archive.org/19/items/world_201904/Ireland_udp.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='Ireland_udp', cmdlist=cmdlist, finishedCallback=None)
                                return

                        elif returnValue == "com_405":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia801508.us.archive.org/19/items/world_201904/Yemen_tcp.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='Yemen_tcp', cmdlist=cmdlist, finishedCallback=None)
                                return

                        elif returnValue == "com_406":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia801508.us.archive.org/19/items/world_201904/Yemen_udp.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='Yemen_udp', cmdlist=cmdlist, finishedCallback=None)
                                return

                        elif returnValue == "com_407":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia801508.us.archive.org/19/items/world_201904/Uzbekistan_tcp.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='Uzbekistan_tcp', cmdlist=cmdlist, finishedCallback=None)
                                return

                        elif returnValue == "com_408":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia801508.us.archive.org/19/items/world_201904/Uzbekistan_udp.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='Uzbekistan_udp', cmdlist=cmdlist, finishedCallback=None)
                                return

                        elif returnValue == "com_409":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia801508.us.archive.org/19/items/world_201904/Lebanon_tcp.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='Lebanon_tcp', cmdlist=cmdlist, finishedCallback=None)
                                return

                        elif returnValue == "com_410":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia801508.us.archive.org/19/items/world_201904/Lebanon_udp.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='Lebanon_udp', cmdlist=cmdlist, finishedCallback=None)
                                return

                        elif returnValue == "com_411":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia801508.us.archive.org/19/items/world_201904/Ethiopia_tcp.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='Ethiopia_tcp', cmdlist=cmdlist, finishedCallback=None)
                                return

                        elif returnValue == "com_412":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia801508.us.archive.org/19/items/world_201904/Ethiopia_udp.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='Ethiopia_udp', cmdlist=cmdlist, finishedCallback=None)
                                return

                        elif returnValue == "com_413":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia801508.us.archive.org/19/items/world_201904/Estonia_tcp.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='Estonia_tcp', cmdlist=cmdlist, finishedCallback=None)
                                return

                        elif returnValue == "com_414":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia801508.us.archive.org/19/items/world_201904/Estonia_udp.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='Estonia_udp', cmdlist=cmdlist, finishedCallback=None)
                                return

                        elif returnValue == "com_415":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia801508.us.archive.org/19/items/world_201904/Costa Rica_tcp.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='Costa Rica_tcp', cmdlist=cmdlist, finishedCallback=None)
                                return

                        elif returnValue == "com_416":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia801508.us.archive.org/19/items/world_201904/Costa Rica_udp.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='Costa Rica_udp', cmdlist=cmdlist, finishedCallback=None)
                                return

                        elif returnValue == "com_417":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia801508.us.archive.org/19/items/world_201904/Panama_tcp.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='Panama_tcp', cmdlist=cmdlist, finishedCallback=None)
                                return

                        elif returnValue == "com_418":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia801508.us.archive.org/19/items/world_201904/Panama_udp.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='Panama_udp', cmdlist=cmdlist, finishedCallback=None)
                                return

                        elif returnValue == "com_419":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia801508.us.archive.org/19/items/world_201904/Afghanistan_tcp.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='Afghanistan_tcp', cmdlist=cmdlist, finishedCallback=None)
                                return

                        elif returnValue == "com_420":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia801508.us.archive.org/19/items/world_201904/Afghanistan_udp.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='Afghanistan_udp', cmdlist=cmdlist, finishedCallback=None)
                                return

                        elif returnValue == "com_421":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia801508.us.archive.org/19/items/world_201904/Korea Democratic_tcp.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='Korea Democratic_tcp', cmdlist=cmdlist, finishedCallback=None)
                                return

                        elif returnValue == "com_422":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia801508.us.archive.org/19/items/world_201904/Korea Democratic_udp.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='Korea Democratic_udp', cmdlist=cmdlist, finishedCallback=None)
                                return

                        elif returnValue == "com_423":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia801508.us.archive.org/19/items/world_201904/Jamaica_tcp.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='Jamaica_tcp', cmdlist=cmdlist, finishedCallback=None)
                                return

                        elif returnValue == "com_424":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia801508.us.archive.org/19/items/world_201904/Jamaica_udp.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='Jamaica_udp', cmdlist=cmdlist, finishedCallback=None)
                                return

                        elif returnValue == "com_425":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia801508.us.archive.org/19/items/world_201904/Georgia_tcp.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='Georgia_tcp', cmdlist=cmdlist, finishedCallback=None)
                                return

                        elif returnValue == "com_426":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia801508.us.archive.org/19/items/world_201904/Georgia_udp.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='Georgia_udp', cmdlist=cmdlist, finishedCallback=None)
                                return

                        elif returnValue == "com_427":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia801508.us.archive.org/19/items/world_201904/Moldova_tcp.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='Moldova_tcp', cmdlist=cmdlist, finishedCallback=None)
                                return

                        elif returnValue == "com_428":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia801508.us.archive.org/19/items/world_201904/Moldova_udp.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='Moldova_udp', cmdlist=cmdlist, finishedCallback=None)
                                return

                        elif returnValue == "com_429":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia801508.us.archive.org/19/items/world_201904/Uruguay_tcp.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='Uruguay_tcp', cmdlist=cmdlist, finishedCallback=None)
                                return

                        elif returnValue == "com_430":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia801508.us.archive.org/19/items/world_201904/Uruguay_udp.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='Uruguay_udp', cmdlist=cmdlist, finishedCallback=None)
                                return

                        elif returnValue == "com_431":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia801508.us.archive.org/19/items/world_201904/Slovenia_tcp.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='Slovenia_tcp', cmdlist=cmdlist, finishedCallback=None)
                                return

                        elif returnValue == "com_432":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia801508.us.archive.org/19/items/world_201904/Slovenia_udp.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='Slovenia_udp', cmdlist=cmdlist, finishedCallback=None)
                                return

                        elif returnValue == "com_433":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia801508.us.archive.org/19/items/world_201904/Slovakia_tcp.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='Slovakia_tcp', cmdlist=cmdlist, finishedCallback=None)
                                return

                        elif returnValue == "com_434":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia801508.us.archive.org/19/items/world_201904/Slovakia_udp.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='Slovakia_udp', cmdlist=cmdlist, finishedCallback=None)
                                return

                        elif returnValue == "com_435":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia801508.us.archive.org/19/items/world_201904/Paraguay_tcp.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='Paraguay_tcp', cmdlist=cmdlist, finishedCallback=None)
                                return

                        elif returnValue == "com_436":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia801508.us.archive.org/19/items/world_201904/Paraguay_udp.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='Paraguay_udp', cmdlist=cmdlist, finishedCallback=None)
                                return

                        elif returnValue == "com_437":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia801508.us.archive.org/19/items/world_201904/Honduras_tcp.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='Honduras_tcp', cmdlist=cmdlist, finishedCallback=None)
                                return

                        elif returnValue == "com_438":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia801508.us.archive.org/19/items/world_201904/Honduras_udp.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='Honduras_udp', cmdlist=cmdlist, finishedCallback=None)
                                return

                        elif returnValue == "com_439":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia801508.us.archive.org/19/items/world_201904/Azerbaijan_tcp.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='Azerbaijan_tcp', cmdlist=cmdlist, finishedCallback=None)
                                return

                        elif returnValue == "com_440":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia801508.us.archive.org/19/items/world_201904/Azerbaijan_udp.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='Azerbaijan_udp', cmdlist=cmdlist, finishedCallback=None)
                                return

                        elif returnValue == "com_441":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia801508.us.archive.org/19/items/world_201904/Trinidad_tcp.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='Trinidad_tcp', cmdlist=cmdlist, finishedCallback=None)
                                return

                        elif returnValue == "com_442":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia801508.us.archive.org/19/items/world_201904/Trinidad_udp.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='Trinidad_udp', cmdlist=cmdlist, finishedCallback=None)
                                return

                        elif returnValue == "com_443":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia801508.us.archive.org/19/items/world_201904/Cameroon_tcp.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='Cameroon_tcp', cmdlist=cmdlist, finishedCallback=None)
                                return

                        elif returnValue == "com_444":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia801508.us.archive.org/19/items/world_201904/Cameroon_udp.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='Cameroon_udp', cmdlist=cmdlist, finishedCallback=None)
                                return

                        elif returnValue == "com_445":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia801508.us.archive.org/19/items/world_201904/Benin_tcp.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='Benin_tcp', cmdlist=cmdlist, finishedCallback=None)
                                return

                        elif returnValue == "com_446":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia801508.us.archive.org/19/items/world_201904/Benin_udp.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='Benin_udp', cmdlist=cmdlist, finishedCallback=None)
                                return

                        elif returnValue == "com_447":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia801508.us.archive.org/19/items/world_201904/Cuba_tcp.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='Cuba_tcp', cmdlist=cmdlist, finishedCallback=None)
                                return

                        elif returnValue == "com_448":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia801508.us.archive.org/19/items/world_201904/Cuba_udp.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='Cuba_udp', cmdlist=cmdlist, finishedCallback=None)
                                return

                        elif returnValue == "com_449":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia801508.us.archive.org/19/items/world_201904/Barbados_tcp.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='Barbados_tcp', cmdlist=cmdlist, finishedCallback=None)
                                return

                        elif returnValue == "com_450":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia801508.us.archive.org/19/items/world_201904/Barbados_udp.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='Barbados_udp', cmdlist=cmdlist, finishedCallback=None)
                                return

                        elif returnValue == "com_451":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia801508.us.archive.org/19/items/world_201904/Bosnia_tcp.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='Bosnia_tcp', cmdlist=cmdlist, finishedCallback=None)
                                return

                        elif returnValue == "com_452":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia801508.us.archive.org/19/items/world_201904/Bosnia_udp.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='Bosnia_udp', cmdlist=cmdlist, finishedCallback=None)
                                return

                        elif returnValue == "com_453":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia801508.us.archive.org/19/items/world_201904/Senegal_tcp.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='Senegal_tcp', cmdlist=cmdlist, finishedCallback=None)
                                return

                        elif returnValue == "com_454":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia801508.us.archive.org/19/items/world_201904/Senegal_udp.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='Senegal_udp', cmdlist=cmdlist, finishedCallback=None)
                                return

                        elif returnValue == "com_455":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia801508.us.archive.org/19/items/world_201904/El Salvador_tcp.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='El Salvador_tcp', cmdlist=cmdlist, finishedCallback=None)
                                return

                        elif returnValue == "com_456":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia801508.us.archive.org/19/items/world_201904/El Salvador_udp.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='El Salvador_udp', cmdlist=cmdlist, finishedCallback=None)
                                return

                        elif returnValue == "com_457":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia801508.us.archive.org/19/items/world_201904/Puerto Rico_tcp.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='Puerto Rico_tcp', cmdlist=cmdlist, finishedCallback=None)
                                return

                        elif returnValue == "com_458":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia801508.us.archive.org/19/items/world_201904/Puerto Rico_udp.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='Puerto Rico_udp', cmdlist=cmdlist, finishedCallback=None)
                                return

                        elif returnValue == "com_459":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia801508.us.archive.org/19/items/world_201904/Cyprus_tcp.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='Cyprus_tcp', cmdlist=cmdlist, finishedCallback=None)
                                return

                        elif returnValue == "com_460":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia801508.us.archive.org/19/items/world_201904/Cyprus_udp.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='Cyprus_udp', cmdlist=cmdlist, finishedCallback=None)
                                return

                        elif returnValue == "com_461":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia801508.us.archive.org/19/items/world_201904/Albania_tcp.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='Albania_tcp', cmdlist=cmdlist, finishedCallback=None)
                                return

                        elif returnValue == "com_462":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia801508.us.archive.org/19/items/world_201904/Albania_udp.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='Albania_udp', cmdlist=cmdlist, finishedCallback=None)
                                return

                        elif returnValue == "com_463":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia801508.us.archive.org/19/items/world_201904/Somalia_tcp.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='Somalia_tcp', cmdlist=cmdlist, finishedCallback=None)
                                return

                        elif returnValue == "com_464":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia801508.us.archive.org/19/items/world_201904/Somalia_udp.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='Somalia_udp', cmdlist=cmdlist, finishedCallback=None)
                                return

                        elif returnValue == "com_465":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia801508.us.archive.org/19/items/world_201904/Macedonia_tcp.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='Macedonia_tcp', cmdlist=cmdlist, finishedCallback=None)
                                return

                        elif returnValue == "com_466":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia801508.us.archive.org/19/items/world_201904/Macedonia_udp.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='Macedonia_udp', cmdlist=cmdlist, finishedCallback=None)
                                return

                        elif returnValue == "com_467":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia801508.us.archive.org/19/items/world_201904/Tanzania_tcp.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='Tanzania_tcp', cmdlist=cmdlist, finishedCallback=None)
                                return

                        elif returnValue == "com_468":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia801508.us.archive.org/19/items/world_201904/Tanzania_udp.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='Tanzania_udp', cmdlist=cmdlist, finishedCallback=None)
                                return

                        elif returnValue == "com_469":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia801508.us.archive.org/19/items/world_201904/Mauritius_tcp.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='Mauritius_tcp', cmdlist=cmdlist, finishedCallback=None)
                                return

                        elif returnValue == "com_470":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia801508.us.archive.org/19/items/world_201904/Mauritius_udp.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='Mauritius_udp', cmdlist=cmdlist, finishedCallback=None)
                                return

                        elif returnValue == "com_471":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia801508.us.archive.org/19/items/world_201904/Kyrgyzstan_tcp.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='Kyrgyzstan_tcp', cmdlist=cmdlist, finishedCallback=None)
                                return

                        elif returnValue == "com_472":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia801508.us.archive.org/19/items/world_201904/Kyrgyzstan_udp.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='Kyrgyzstan_udp', cmdlist=cmdlist, finishedCallback=None)
                                return

                        elif returnValue == "com_473":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia801508.us.archive.org/19/items/world_201904/Armenia_tcp.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='Armenia_tcp', cmdlist=cmdlist, finishedCallback=None)
                                return

                        elif returnValue == "com_474":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia801508.us.archive.org/19/items/world_201904/Armenia_udp.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='Armenia_udp', cmdlist=cmdlist, finishedCallback=None)
                                return

                        elif returnValue == "com_475":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia801508.us.archive.org/19/items/world_201904/Madagascar_tcp.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='Madagascar_tcp', cmdlist=cmdlist, finishedCallback=None)
                                return

                        elif returnValue == "com_476":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia801508.us.archive.org/19/items/world_201904/Madagascar_udp.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='Madagascar_udp', cmdlist=cmdlist, finishedCallback=None)
                                return

                        elif returnValue == "com_477":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia801508.us.archive.org/19/items/world_201904/Maldives_tcp.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='Maldives_tcp', cmdlist=cmdlist, finishedCallback=None)
                                return

                        elif returnValue == "com_478":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia801508.us.archive.org/19/items/world_201904/Maldives_udp.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='Maldives_udp', cmdlist=cmdlist, finishedCallback=None)
                                return

                        elif returnValue == "com_479":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia801508.us.archive.org/19/items/world_201904/Rwanda_tcp.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='Rwanda_tcp', cmdlist=cmdlist, finishedCallback=None)
                                return

                        elif returnValue == "com_480":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia801508.us.archive.org/19/items/world_201904/Rwanda_udp.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='Rwanda_udp', cmdlist=cmdlist, finishedCallback=None)
                                return

                        elif returnValue == "com_481":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia801508.us.archive.org/19/items/world_201904/Hong Kong_tcp.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='Hong Kong_tcp', cmdlist=cmdlist, finishedCallback=None)
                                return

                        elif returnValue == "com_482":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia801508.us.archive.org/19/items/world_201904/Hong Kong_udp.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='Hong Kong_udp', cmdlist=cmdlist, finishedCallback=None)
                                return

                        elif returnValue == "com_483":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia801508.us.archive.org/19/items/world_201904/Uganda_tcp.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='Uganda_tcp', cmdlist=cmdlist, finishedCallback=None)
                                return

                        elif returnValue == "com_484":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia801508.us.archive.org/19/items/world_201904/Uganda_udp.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='Uganda_udp', cmdlist=cmdlist, finishedCallback=None)
                                return

                        elif returnValue == "com_485":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia801508.us.archive.org/19/items/world_201904/Guam_tcp.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='Guam_tcp', cmdlist=cmdlist, finishedCallback=None)
                                return

                        elif returnValue == "com_486":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia801508.us.archive.org/19/items/world_201904/Guam_udp.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='Guam_udp', cmdlist=cmdlist, finishedCallback=None)
                                return

                        elif returnValue == "com_487":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia801508.us.archive.org/19/items/world_201904/Bahamas_tcp.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='Bahamas_tcp', cmdlist=cmdlist, finishedCallback=None)
                                return

                        elif returnValue == "com_488":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia801508.us.archive.org/19/items/world_201904/Bahamas_udp.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='Bahamas_udp', cmdlist=cmdlist, finishedCallback=None)
                                return

                        elif returnValue == "com_489":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia801508.us.archive.org/19/items/world_201904/Nicaragua_tcp.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='Nicaragua_tcp', cmdlist=cmdlist, finishedCallback=None)
                                return

                        elif returnValue == "com_490":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia801508.us.archive.org/19/items/world_201904/Nicaragua_udp.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='Nicaragua_udp', cmdlist=cmdlist, finishedCallback=None)
                                return

                        elif returnValue == "com_491":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia801508.us.archive.org/19/items/world_201904/Mali_tcp.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='Mali_tcp', cmdlist=cmdlist, finishedCallback=None)
                                return

                        elif returnValue == "com_492":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia801508.us.archive.org/19/items/world_201904/Mali_udp.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='Mali_udp', cmdlist=cmdlist, finishedCallback=None)
                                return

                        elif returnValue == "com_493":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia801508.us.archive.org/19/items/world_201904/Zimbabwe_tcp.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='Zimbabwe_tcp', cmdlist=cmdlist, finishedCallback=None)
                                return

                        elif returnValue == "com_494":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia801508.us.archive.org/19/items/world_201904/Zimbabwe_udp.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='Zimbabwe_udp', cmdlist=cmdlist, finishedCallback=None)
                                return

                        elif returnValue == "com_495":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia801508.us.archive.org/19/items/world_201904/Fiji_tcp.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='Fiji_tcp', cmdlist=cmdlist, finishedCallback=None)
                                return

                        elif returnValue == "com_496":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia801508.us.archive.org/19/items/world_201904/Fiji_udp.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='Fiji_udp', cmdlist=cmdlist, finishedCallback=None)
                                return

                        elif returnValue == "com_497":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia801508.us.archive.org/19/items/world_201904/Chad_tcp.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='Chad_tcp', cmdlist=cmdlist, finishedCallback=None)
                                return

                        elif returnValue == "com_498":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia801508.us.archive.org/19/items/world_201904/Chad_udp.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='Chad_udp', cmdlist=cmdlist, finishedCallback=None)
                                return

                        elif returnValue == "com_499":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia801508.us.archive.org/19/items/world_201904/Gambia_tcp.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='Gambia_tcp', cmdlist=cmdlist, finishedCallback=None)
                                return

                        elif returnValue == "com_500":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia801508.us.archive.org/19/items/world_201904/Gambia_udp.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='Gambia_udp', cmdlist=cmdlist, finishedCallback=None)
                                return

                        elif returnValue == "com_501":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia801508.us.archive.org/19/items/world_201904/Samoa_tcp.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='Samoa_tcp', cmdlist=cmdlist, finishedCallback=None)
                                return

                        elif returnValue == "com_502":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia801508.us.archive.org/19/items/world_201904/Samoa_udp.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='Samoa_udp', cmdlist=cmdlist, finishedCallback=None)
                                return

                        elif returnValue == "com_503":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia801508.us.archive.org/19/items/world_201904/Iceland_tcp.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='Iceland_tcp', cmdlist=cmdlist, finishedCallback=None)
                                return

                        elif returnValue == "com_504":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia801508.us.archive.org/19/items/world_201904/Iceland_udp.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='Iceland_udp', cmdlist=cmdlist, finishedCallback=None)
                                return

                        elif returnValue == "com_505":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia801508.us.archive.org/19/items/world_201904/Aruba_tcp.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='Aruba_tcp', cmdlist=cmdlist, finishedCallback=None)
                                return

                        elif returnValue == "com_506":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia801508.us.archive.org/19/items/world_201904/Aruba_udp.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='Aruba_udp', cmdlist=cmdlist, finishedCallback=None)
                                return

                        elif returnValue == "com_507":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia801508.us.archive.org/19/items/world_201904/Angola_tcp.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='Angola_tcp', cmdlist=cmdlist, finishedCallback=None)
                                return

                        elif returnValue == "com_508":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia801508.us.archive.org/19/items/world_201904/Angola_udp.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='Angola_udp', cmdlist=cmdlist, finishedCallback=None)
                                return

                        elif returnValue == "com_509":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia801508.us.archive.org/19/items/world_201904/Liberia_tcp.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='Liberia_tcp', cmdlist=cmdlist, finishedCallback=None)
                                return

                        elif returnValue == "com_510":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia801508.us.archive.org/19/items/world_201904/Liberia_udp.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='Liberia_udp', cmdlist=cmdlist, finishedCallback=None)
                                return

                        elif returnValue == "com_511":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia801508.us.archive.org/19/items/world_201904/Malta_tcp.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='Malta_tcp', cmdlist=cmdlist, finishedCallback=None)
                                return

                        elif returnValue == "com_512":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia801508.us.archive.org/19/items/world_201904/Malta_udp.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='Malta_udp', cmdlist=cmdlist, finishedCallback=None)
                                return

                        elif returnValue == "com_513":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia801508.us.archive.org/19/items/world_201904/New Caledonia_tcp.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='New Caledonia_tcp', cmdlist=cmdlist, finishedCallback=None)
                                return

                        elif returnValue == "com_514":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia801508.us.archive.org/19/items/world_201904/New Caledonia_udp.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='New Caledonia_udp', cmdlist=cmdlist, finishedCallback=None)
                                return

                        elif returnValue == "com_515":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia801508.us.archive.org/19/items/world_201904/New Guinea_tcp.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='New Guinea_tcp', cmdlist=cmdlist, finishedCallback=None)
                                return

                        elif returnValue == "com_516":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia801508.us.archive.org/19/items/world_201904/New Guinea_udp.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='New Guinea_udp', cmdlist=cmdlist, finishedCallback=None)
                                return

                        elif returnValue == "com_517":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia801508.us.archive.org/19/items/world_201904/Bhutan_tcp.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='Bhutan_tcp', cmdlist=cmdlist, finishedCallback=None)
                                return

                        elif returnValue == "com_518":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia801508.us.archive.org/19/items/world_201904/Bhutan_udp.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='Bhutan_udp', cmdlist=cmdlist, finishedCallback=None)
                                return

                        elif returnValue == "com_519":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia801508.us.archive.org/19/items/world_201904/Zambia_tcp.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='Zambia_tcp', cmdlist=cmdlist, finishedCallback=None)
                                return

                        elif returnValue == "com_520":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia801508.us.archive.org/19/items/world_201904/Zambia_udp.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='Zambia_udp', cmdlist=cmdlist, finishedCallback=None)
                                return

                        elif returnValue == "com_521":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia801508.us.archive.org/19/items/world_201904/Mozambique_tcp.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='Mozambique_tcp', cmdlist=cmdlist, finishedCallback=None)
                                return

                        elif returnValue == "com_522":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia801508.us.archive.org/19/items/world_201904/Mozambique_udp.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='Mozambique_udp', cmdlist=cmdlist, finishedCallback=None)
                                return

                        elif returnValue == "com_523":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia801508.us.archive.org/19/items/world_201904/Tajikistan_tcp.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='Tajikistan_tcp', cmdlist=cmdlist, finishedCallback=None)
                                return

                        elif returnValue == "com_524":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia801508.us.archive.org/19/items/world_201904/Tajikistan_udp.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='Tajikistan_udp', cmdlist=cmdlist, finishedCallback=None)
                                return

                        elif returnValue == "com_525":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia801508.us.archive.org/19/items/world_201904/Gabon_tcp.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='Gabon_tcp', cmdlist=cmdlist, finishedCallback=None)
                                return

                        elif returnValue == "com_526":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia801508.us.archive.org/19/items/world_201904/Gabon_udp.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='Gabon_udp', cmdlist=cmdlist, finishedCallback=None)
                                return

                        elif returnValue == "com_527":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia801508.us.archive.org/19/items/world_201904/Reunion_tcp.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='Reunion_tcp', cmdlist=cmdlist, finishedCallback=None)
                                return

                        elif returnValue == "com_528":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia801508.us.archive.org/19/items/world_201904/Reunion_udp.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='Reunion_udp', cmdlist=cmdlist, finishedCallback=None)
                                return

                        elif returnValue == "com_529":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia801508.us.archive.org/19/items/world_201904/Namibia_tcp.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='Namibia_tcp', cmdlist=cmdlist, finishedCallback=None)
                                return

                        elif returnValue == "com_530":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia801508.us.archive.org/19/items/world_201904/Namibia_udp.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='Namibia_udp', cmdlist=cmdlist, finishedCallback=None)
                                return

                        elif returnValue == "com_531":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia801508.us.archive.org/19/items/world_201904/Montenegro_tcp.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='Montenegro_tcp', cmdlist=cmdlist, finishedCallback=None)
                                return

                        elif returnValue == "com_532":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia801508.us.archive.org/19/items/world_201904/Montenegro_udp.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='Montenegro_udp', cmdlist=cmdlist, finishedCallback=None)
                                return

                        elif returnValue == "com_533":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia801508.us.archive.org/19/items/world_201904/Belize_tcp.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='Belize_tcp', cmdlist=cmdlist, finishedCallback=None)
                                return

                        elif returnValue == "com_534":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia801508.us.archive.org/19/items/world_201904/Belize_udp.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='Belize_udp', cmdlist=cmdlist, finishedCallback=None)
                                return

                        elif returnValue == "com_535":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia801508.us.archive.org/19/items/world_201904/Equatorial Guinea_tcp.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='Equatorial Guinea_tcp', cmdlist=cmdlist, finishedCallback=None)
                                return

                        elif returnValue == "com_536":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia801508.us.archive.org/19/items/world_201904/Equatorial Guinea_udp.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='Equatorial Guinea_udp', cmdlist=cmdlist, finishedCallback=None)
                                return

                        elif returnValue == "com_537":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia801508.us.archive.org/19/items/world_201904/Malawi_tcp.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='Malawi_tcp', cmdlist=cmdlist, finishedCallback=None)
                                return

                        elif returnValue == "com_538":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia801508.us.archive.org/19/items/world_201904/Malawi_udp.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='Malawi_udp', cmdlist=cmdlist, finishedCallback=None)
                                return

                        elif returnValue == "com_539":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia801508.us.archive.org/19/items/world_201904/Comoros_tcp.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='Comoros_tcp', cmdlist=cmdlist, finishedCallback=None)
                                return

                        elif returnValue == "com_540":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia801508.us.archive.org/19/items/world_201904/Comoros_udp.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='Comoros_udp', cmdlist=cmdlist, finishedCallback=None)
                                return

                        elif returnValue == "com_541":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia801508.us.archive.org/19/items/world_201904/Dominica_tcp.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='Dominica_tcp', cmdlist=cmdlist, finishedCallback=None)
                                return

                        elif returnValue == "com_542":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia801508.us.archive.org/19/items/world_201904/Dominica_udp.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='Dominica_udp', cmdlist=cmdlist, finishedCallback=None)
                                return

                        elif returnValue == "com_543":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia801508.us.archive.org/19/items/world_201904/Suriname_tcp.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='Suriname_tcp', cmdlist=cmdlist, finishedCallback=None)
                                return

                        elif returnValue == "com_544":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia801508.us.archive.org/19/items/world_201904/Suriname_udp.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='Suriname_udp', cmdlist=cmdlist, finishedCallback=None)
                                return

                        elif returnValue == "com_545":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia801508.us.archive.org/19/items/world_201904/Saint Vincent_tcp.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='Saint Vincent_tcp', cmdlist=cmdlist, finishedCallback=None)
                                return

                        elif returnValue == "com_546":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia801508.us.archive.org/19/items/world_201904/Saint Vincent_udp.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='Saint Vincent_udp', cmdlist=cmdlist, finishedCallback=None)
                                return

                        elif returnValue == "com_547":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia801508.us.archive.org/19/items/world_201904/Togo_tcp.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='Togo_tcp', cmdlist=cmdlist, finishedCallback=None)
                                return

                        elif returnValue == "com_548":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia801508.us.archive.org/19/items/world_201904/Togo_udp.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='Togo_udp', cmdlist=cmdlist, finishedCallback=None)
                                return

                        elif returnValue == "com_549":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia801508.us.archive.org/19/items/world_201904/Congo_tcp.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='Congo_tcp', cmdlist=cmdlist, finishedCallback=None)
                                return

                        elif returnValue == "com_550":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia801508.us.archive.org/19/items/world_201904/Congo_udp.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='Congo_udp', cmdlist=cmdlist, finishedCallback=None)
                                return

                        elif returnValue == "com_551":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia801508.us.archive.org/19/items/world_201904/Seychelles_tcp.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='Seychelles_tcp', cmdlist=cmdlist, finishedCallback=None)
                                return

                        elif returnValue == "com_552":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia801508.us.archive.org/19/items/world_201904/Seychelles_udp.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='Seychelles_udp', cmdlist=cmdlist, finishedCallback=None)
                                return

                        elif returnValue == "com_553":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia801508.us.archive.org/19/items/world_201904/Guyana_tcp.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='Guyana_tcp', cmdlist=cmdlist, finishedCallback=None)
                                return

                        elif returnValue == "com_554":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia801508.us.archive.org/19/items/world_201904/Guyana_udp.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='Guyana_udp', cmdlist=cmdlist, finishedCallback=None)
                                return

                        elif returnValue == "com_555":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia801508.us.archive.org/19/items/world_201904/Wallis_tcp.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='Wallis_tcp', cmdlist=cmdlist, finishedCallback=None)
                                return

                        elif returnValue == "com_556":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia801508.us.archive.org/19/items/world_201904/Wallis_udp.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='Wallis_udp', cmdlist=cmdlist, finishedCallback=None)
                                return

                        elif returnValue == "com_557":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia801508.us.archive.org/19/items/world_201904/Congo Democratic_tcp.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='Congo Democratic_tcp', cmdlist=cmdlist, finishedCallback=None)
                                return

                        elif returnValue == "com_558":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia801508.us.archive.org/19/items/world_201904/Congo Democratic_udp.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='Congo Democratic_udp', cmdlist=cmdlist, finishedCallback=None)
                                return

                        elif returnValue == "com_559":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia801508.us.archive.org/19/items/world_201904/Botswana_tcp.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='Botswana_tcp', cmdlist=cmdlist, finishedCallback=None)
                                return

                        elif returnValue == "com_560":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia801508.us.archive.org/19/items/world_201904/Botswana_udp.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='Botswana_udp', cmdlist=cmdlist, finishedCallback=None)
                                return

                        elif returnValue == "com_561":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia801508.us.archive.org/19/items/world_201904/French Polynesia_tcp.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='French Polynesia_tcp', cmdlist=cmdlist, finishedCallback=None)
                                return

                        elif returnValue == "com_562":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia801508.us.archive.org/19/items/world_201904/French Polynesia_udp.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='French Polynesia_udp', cmdlist=cmdlist, finishedCallback=None)
                                return

                        elif returnValue == "com_563":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia801508.us.archive.org/19/items/world_201904/Haiti_tcp.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='Haiti_tcp', cmdlist=cmdlist, finishedCallback=None)
                                return

                        elif returnValue == "com_564":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia801508.us.archive.org/19/items/world_201904/Haiti_udp.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='Haiti_udp', cmdlist=cmdlist, finishedCallback=None)
                                return

                        elif returnValue == "com_565":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia801508.us.archive.org/19/items/world_201904/Curacao_tcp.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='Curacao_tcp', cmdlist=cmdlist, finishedCallback=None)
                                return

                        elif returnValue == "com_566":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia801508.us.archive.org/19/items/world_201904/Curacao_udp.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='Curacao_udp', cmdlist=cmdlist, finishedCallback=None)
                                return

                        elif returnValue == "com_567":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia801508.us.archive.org/19/items/world_201904/Saint Lucia_tcp.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='Saint Lucia_tcp', cmdlist=cmdlist, finishedCallback=None)
                                return

                        elif returnValue == "com_568":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia801508.us.archive.org/19/items/world_201904/Saint Lucia_udp.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='Saint Lucia_udp', cmdlist=cmdlist, finishedCallback=None)
                                return

                        elif returnValue == "com_569":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia801508.us.archive.org/19/items/world_201904/Palau_tcp.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='Palau_tcp', cmdlist=cmdlist, finishedCallback=None)
                                return

                        elif returnValue == "com_570":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia801508.us.archive.org/19/items/world_201904/Palau_udp.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='Palau_udp', cmdlist=cmdlist, finishedCallback=None)
                                return

                        elif returnValue == "com_571":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia801508.us.archive.org/19/items/world_201904/Grenada_tcp.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='Grenada_tcp', cmdlist=cmdlist, finishedCallback=None)
                                return

                        elif returnValue == "com_572":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia801508.us.archive.org/19/items/world_201904/Grenada_udp.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='Grenada_udp', cmdlist=cmdlist, finishedCallback=None)
                                return

                        elif returnValue == "com_573":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia801508.us.archive.org/19/items/world_201904/Marshall Islands_tcp.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='Marshall Islands_tcp', cmdlist=cmdlist, finishedCallback=None)
                                return

                        elif returnValue == "com_574":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia801508.us.archive.org/19/items/world_201904/Marshall Islands_udp.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='Marshall Islands_udp', cmdlist=cmdlist, finishedCallback=None)
                                return

                        elif returnValue == "com_575":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia801508.us.archive.org/19/items/world_201904/Burkina Faso_tcp.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='Burkina Faso_tcp', cmdlist=cmdlist, finishedCallback=None)
                                return

                        elif returnValue == "com_576":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia801508.us.archive.org/19/items/world_201904/Burkina Faso_udp.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='Burkina Faso_udp', cmdlist=cmdlist, finishedCallback=None)
                                return

                        elif returnValue == "com_577":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia801508.us.archive.org/19/items/world_201904/Timor-leste_tcp.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='Timor-leste_tcp', cmdlist=cmdlist, finishedCallback=None)
                                return

                        elif returnValue == "com_578":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia801508.us.archive.org/19/items/world_201904/Timor-leste_udp.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='Timor-leste_udp', cmdlist=cmdlist, finishedCallback=None)
                                return

                        elif returnValue == "com_579":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia801508.us.archive.org/19/items/world_201904/Cayman Islands_tcp.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='Cayman Islands_tcp', cmdlist=cmdlist, finishedCallback=None)
                                return

                        elif returnValue == "com_580":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia801508.us.archive.org/19/items/world_201904/Cayman Islands_udp.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='Cayman Islands_udp', cmdlist=cmdlist, finishedCallback=None)
                                return

                        elif returnValue == "com_581":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia801508.us.archive.org/19/items/world_201904/Mauritania_tcp.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='Mauritania_tcp', cmdlist=cmdlist, finishedCallback=None)
                                return

                        elif returnValue == "com_582":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia801508.us.archive.org/19/items/world_201904/Mauritania_udp.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='Mauritania_udp', cmdlist=cmdlist, finishedCallback=None)
                                return

                        elif returnValue == "com_583":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia801508.us.archive.org/19/items/world_201904/Niger_tcp.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='Niger_tcp', cmdlist=cmdlist, finishedCallback=None)
                                return

                        elif returnValue == "com_584":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia801508.us.archive.org/19/items/world_201904/Niger_udp.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='Niger_udp', cmdlist=cmdlist, finishedCallback=None)
                                return

                        elif returnValue == "com_585":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia801508.us.archive.org/19/items/world_201904/Micronesia_tcp.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='Micronesia_tcp', cmdlist=cmdlist, finishedCallback=None)
                                return
                                
                        elif returnValue == "com_586":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia801508.us.archive.org/19/items/world_201904/Micronesia_udp.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='Micronesia_udp', cmdlist=cmdlist, finishedCallback=None)
                                return

                        elif returnValue == "com_587":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia801508.us.archive.org/19/items/world_201904/Swaziland_tcp.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='Swaziland_tcp', cmdlist=cmdlist, finishedCallback=None)
                                return

                        elif returnValue == "com_588":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia801508.us.archive.org/19/items/world_201904/Swaziland_udp.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='Swaziland_udp', cmdlist=cmdlist, finishedCallback=None)
                                return

                        elif returnValue == "com_589":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia801508.us.archive.org/19/items/world_201904/Guinea_tcp.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='Guinea_tcp', cmdlist=cmdlist, finishedCallback=None)
                                return

                        elif returnValue == "com_590":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia801508.us.archive.org/19/items/world_201904/Guinea_udp.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='Guinea_udp', cmdlist=cmdlist, finishedCallback=None)
                                return

                        elif returnValue == "com_591":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia801508.us.archive.org/19/items/world_201904/Saint Kitts_tcp.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='Saint Kitts_tcp', cmdlist=cmdlist, finishedCallback=None)
                                return

                        elif returnValue == "com_592":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia801508.us.archive.org/19/items/world_201904/Saint Kitts_udp.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='Saint Kitts_udp', cmdlist=cmdlist, finishedCallback=None)
                                return

                        elif returnValue == "com_593":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia801508.us.archive.org/19/items/world_201904/Burundi_tcp.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='Burundi_tcp', cmdlist=cmdlist, finishedCallback=None)
                                return

                        elif returnValue == "com_594":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia801508.us.archive.org/19/items/world_201904/Burundi_udp.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='Burundi_udp', cmdlist=cmdlist, finishedCallback=None)
                                return

                        elif returnValue == "com_595":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia801508.us.archive.org/19/items/world_201904/Lesotho_tcp.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='Lesotho_tcp', cmdlist=cmdlist, finishedCallback=None)
                                return

                        elif returnValue == "com_596":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia801508.us.archive.org/19/items/world_201904/Lesotho_udp.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='Lesotho_udp', cmdlist=cmdlist, finishedCallback=None)
                                return

                        elif returnValue == "com_597":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia801508.us.archive.org/19/items/world_201904/Sierra Leone_tcp.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='Sierra Leone_tcp', cmdlist=cmdlist, finishedCallback=None)
                                return

                        elif returnValue == "com_598":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia801508.us.archive.org/19/items/world_201904/Sierra Leone_udp.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='Sierra Leone_udp', cmdlist=cmdlist, finishedCallback=None)
                                return

                        elif returnValue == "com_599":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia801508.us.archive.org/19/items/world_201904/Sint Maarten_tcp.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='Sint Maarten_tcp', cmdlist=cmdlist, finishedCallback=None)
                                return

                        elif returnValue == "com_600":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia801508.us.archive.org/19/items/world_201904/Sint Maarten_udp.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='Sint Maarten_udp', cmdlist=cmdlist, finishedCallback=None)
                                return

                        elif returnValue == "com_601":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia801508.us.archive.org/19/items/world_201904/Bermuda_tcp.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='Bermuda_tcp', cmdlist=cmdlist, finishedCallback=None)
                                return

                        elif returnValue == "com_602":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia801508.us.archive.org/19/items/world_201904/Bermuda_udp.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='Bermuda_udp', cmdlist=cmdlist, finishedCallback=None)
                                return

                        elif returnValue == "com_603":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia801508.us.archive.org/19/items/world_201904/Virgin Islands_tcp.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='Virgin Islands_tcp', cmdlist=cmdlist, finishedCallback=None)
                                return

                        elif returnValue == "com_604":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia801508.us.archive.org/19/items/world_201904/Virgin Islands_udp.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='Virgin Islands_udp', cmdlist=cmdlist, finishedCallback=None)
                                return

                        elif returnValue == "com_605":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia801508.us.archive.org/19/items/world_201904/Jersey_tcp.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='Jersey_tcp', cmdlist=cmdlist, finishedCallback=None)
                                return

                        elif returnValue == "com_606":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia801508.us.archive.org/19/items/world_201904/Jersey_udp.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='Jersey_udp', cmdlist=cmdlist, finishedCallback=None)
                                return

                        elif returnValue == "com_607":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia801508.us.archive.org/19/items/world_201904/Andorra_tcp.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='Andorra_tcp', cmdlist=cmdlist, finishedCallback=None)
                                return

                        elif returnValue == "com_608":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia801508.us.archive.org/19/items/world_201904/Andorra_udp.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='Andorra_udp', cmdlist=cmdlist, finishedCallback=None)
                                return

                        elif returnValue == "com_609":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia801508.us.archive.org/19/items/world_201904/Faroe Islands_tcp.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='Faroe Islands_tcp', cmdlist=cmdlist, finishedCallback=None)
                                return

                        elif returnValue == "com_610":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia801508.us.archive.org/19/items/world_201904/Faroe Islands.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='Faroe Islands_udp', cmdlist=cmdlist, finishedCallback=None)
                                return

                        elif returnValue == "com_611":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia801508.us.archive.org/19/items/world_201904/Cape Verde_tcp.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='Cape Verde_tcp', cmdlist=cmdlist, finishedCallback=None)
                                return

                        elif returnValue == "com_612":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia801508.us.archive.org/19/items/world_201904/Cape Verde_udp.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='Cape Verde_udp', cmdlist=cmdlist, finishedCallback=None)
                                return

                        elif returnValue == "com_613":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia801508.us.archive.org/19/items/world_201904/Antigua and Barbuda_tcp.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='Antigua and Barbuda_tcp', cmdlist=cmdlist, finishedCallback=None)
                                return

                        elif returnValue == "com_614":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia801508.us.archive.org/19/items/world_201904/Antigua and Barbuda_udp.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='Antigua and Barbuda_udp', cmdlist=cmdlist, finishedCallback=None)
                                return

                        elif returnValue == "com_615":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia801508.us.archive.org/19/items/world_201904/Monaco_tcp.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='Monaco_tcp', cmdlist=cmdlist, finishedCallback=None)
                                return

                        elif returnValue == "com_616":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia801508.us.archive.org/19/items/world_201904/Monaco_udp.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='Monaco_udp', cmdlist=cmdlist, finishedCallback=None)
                                return

                        elif returnValue == "com_617":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia801508.us.archive.org/19/items/world_201904/American Samoa_tcp.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='American Samoa_tcp', cmdlist=cmdlist, finishedCallback=None)
                                return

                        elif returnValue == "com_618":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia801508.us.archive.org/19/items/world_201904/American Samoa_udp.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='American Samoa_udp', cmdlist=cmdlist, finishedCallback=None)
                                return

                        elif returnValue == "com_619":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia801508.us.archive.org/19/items/world_201904/Gibraltar_tcp.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='Gibraltar_tcp', cmdlist=cmdlist, finishedCallback=None)
                                return

                        elif returnValue == "com_620":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia801508.us.archive.org/19/items/world_201904/Gibraltar_udp.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='Gibraltar_udp', cmdlist=cmdlist, finishedCallback=None)
                                return

                        elif returnValue == "com_621":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia801508.us.archive.org/19/items/world_201904/Vanuatu_tcp.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='Vanuatu_tcp', cmdlist=cmdlist, finishedCallback=None)
                                return

                        elif returnValue == "com_622":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia801508.us.archive.org/19/items/world_201904/Vanuatu_udp.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='Vanuatu_udp', cmdlist=cmdlist, finishedCallback=None)
                                return

                        elif returnValue == "com_623":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia801508.us.archive.org/19/items/world_201904/Turks and Caicos Islands_tcp.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='Turks and Caicos Islands_tcp', cmdlist=cmdlist, finishedCallback=None)
                                return

                        elif returnValue == "com_624":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia801508.us.archive.org/19/items/world_201904/Turks and Caicos Islands_udp.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='Turks and Caicos Islands_udp', cmdlist=cmdlist, finishedCallback=None)
                                return

                        elif returnValue == "com_625":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia801508.us.archive.org/19/items/world_201904/San Marino_tcp.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='San Marino_tcp', cmdlist=cmdlist, finishedCallback=None)
                                return

                        elif returnValue == "com_626":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia801508.us.archive.org/19/items/world_201904/San Marino_udp.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='San Marino_udp', cmdlist=cmdlist, finishedCallback=None)
                                return

                        elif returnValue == "com_627":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia801508.us.archive.org/19/items/world_201904/Liechtenstein_tcp.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='Liechtenstein_tcp', cmdlist=cmdlist, finishedCallback=None)
                                return

                        elif returnValue == "com_628":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia801508.us.archive.org/19/items/world_201904/Liechtenstein_udp.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='Liechtenstein_udp', cmdlist=cmdlist, finishedCallback=None)
                                return

                        elif returnValue == "com_629":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia801508.us.archive.org/19/items/world_201904/Guadeloupe_tcp.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='Guadeloupe_tcp', cmdlist=cmdlist, finishedCallback=None)
                                return

                        elif returnValue == "com_630":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia801508.us.archive.org/19/items/world_201904/Guadeloupe_udp.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='Guadeloupe_udp', cmdlist=cmdlist, finishedCallback=None)
                                return

                        elif returnValue == "com_631":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia801508.us.archive.org/19/items/world_201904/Nauru_tcp.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='Nauru_tcp', cmdlist=cmdlist, finishedCallback=None)
                                return

                        elif returnValue == "com_632":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia801508.us.archive.org/19/items/world_201904/Nauru_udp.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='Nauru_udp', cmdlist=cmdlist, finishedCallback=None)
                                return

                        elif returnValue == "com_633":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia801508.us.archive.org/19/items/world_201904/South Sudan_tcp.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='South Sudan_tcp', cmdlist=cmdlist, finishedCallback=None)
                                return

                        elif returnValue == "com_634":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia801508.us.archive.org/19/items/world_201904/South Sudan_udp.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='South Sudan_udp', cmdlist=cmdlist, finishedCallback=None)
                                return

                        elif returnValue == "com_635":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia801508.us.archive.org/19/items/world_201904/Solomon Islands_tcp.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='Solomon Islands_tcp', cmdlist=cmdlist, finishedCallback=None)
                                return

                        elif returnValue == "com_636":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia801508.us.archive.org/19/items/world_201904/Solomon Islands_udp.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='Solomon Islands_udp', cmdlist=cmdlist, finishedCallback=None)
                                return

                        elif returnValue == "com_637":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia801508.us.archive.org/19/items/world_201904/Bonaire_tcp.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='Bonaire_tcp', cmdlist=cmdlist, finishedCallback=None)
                                return

                        elif returnValue == "com_638":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia801508.us.archive.org/19/items/world_201904/Bonaire_udp.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='Bonaire_udp', cmdlist=cmdlist, finishedCallback=None)
                                return

                        elif returnValue == "com_639":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia801508.us.archive.org/19/items/world_201904/Anguilla_tcp.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='Anguilla_tcp', cmdlist=cmdlist, finishedCallback=None)
                                return

                        elif returnValue == "com_640":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia801508.us.archive.org/19/items/world_201904/Anguilla_udp.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='Anguilla_udp', cmdlist=cmdlist, finishedCallback=None)
                                return

                        elif returnValue == "com_641":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia801508.us.archive.org/19/items/world_201904/St. Pierre_tcp.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='St. Pierre_tcp', cmdlist=cmdlist, finishedCallback=None)
                                return

                        elif returnValue == "com_642":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia801508.us.archive.org/19/items/world_201904/St. Pierre_udp.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='St. Pierre_udp', cmdlist=cmdlist, finishedCallback=None)
                                return

                        elif returnValue == "com_643":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia801508.us.archive.org/19/items/world_201904/Tonga_tcp.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='Tonga_tcp', cmdlist=cmdlist, finishedCallback=None)
                                return

                        elif returnValue == "com_644":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia801508.us.archive.org/19/items/world_201904/Tonga_udp.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='Tonga_udp', cmdlist=cmdlist, finishedCallback=None)
                                return

                        elif returnValue == "com_645":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia801508.us.archive.org/19/items/world_201904/Saint Martin_tcp.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='Saint Martin_tcp', cmdlist=cmdlist, finishedCallback=None)
                                return

                        elif returnValue == "com_646":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia801508.us.archive.org/19/items/world_201904/Saint Martin_udp.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='Saint Martin_udp', cmdlist=cmdlist, finishedCallback=None)
                                return

                        elif returnValue == "com_647":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia801508.us.archive.org/19/items/world_201904/Guinea-bissau_tcp.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='Guinea-bissau_tcp', cmdlist=cmdlist, finishedCallback=None)
                                return

                        elif returnValue == "com_648":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia801508.us.archive.org/19/items/world_201904/'Guinea-bissau_udp.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='Guinea-bissau_udp', cmdlist=cmdlist, finishedCallback=None)
                                return

                        elif returnValue == "com_649":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia801508.us.archive.org/19/items/world_201904/Virgin Islands (BRITISH)_tcp.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='Virgin Islands (BRITISH)_tcp', cmdlist=cmdlist, finishedCallback=None)
                                return

                        elif returnValue == "com_650":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia801508.us.archive.org/19/items/world_201904/Virgin Islands (BRITISH)_udp.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='Virgin Islands (BRITISH)_udp', cmdlist=cmdlist, finishedCallback=None)
                                return

                        elif returnValue == "com_651":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia801508.us.archive.org/19/items/world_201904/Eritrea_tcp.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='Eritrea_tcp', cmdlist=cmdlist, finishedCallback=None)
                                return

                        elif returnValue == "com_652":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia801508.us.archive.org/19/items/world_201904/Eritrea_udp.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='Eritrea_udp', cmdlist=cmdlist, finishedCallback=None)
                                return

                        elif returnValue == "com_653":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia801508.us.archive.org/19/items/world_201904/Central African_tcp.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='Central African_tcp', cmdlist=cmdlist, finishedCallback=None)
                                return

                        elif returnValue == "com_654":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia801508.us.archive.org/19/items/world_201904/Central African_udp.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='Central African_udp', cmdlist=cmdlist, finishedCallback=None)
                                return

                        elif returnValue == "com_655":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia801508.us.archive.org/19/items/world_201904/Kiribati_tcp.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='Kiribati_tcp', cmdlist=cmdlist, finishedCallback=None)
                                return

                        elif returnValue == "com_656":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia801508.us.archive.org/19/items/world_201904/Kiribati_udp.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='Kiribati_udp', cmdlist=cmdlist, finishedCallback=None)
                                return

                        elif returnValue == "com_657":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia801508.us.archive.org/19/items/world_201904/Sao Tome_tcp.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='Sao Tome_tcp', cmdlist=cmdlist, finishedCallback=None)
                                return

                        elif returnValue == "com_658":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia801508.us.archive.org/19/items/world_201904/Sao Tome_udp.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='Sao Tome_udp', cmdlist=cmdlist, finishedCallback=None)
                                return

                        elif returnValue == "com_659":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia801508.us.archive.org/19/items/world_201904/French Guiana_tcp.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='French Guiana_tcp', cmdlist=cmdlist, finishedCallback=None)
                                return

                        elif returnValue == "com_660":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia801508.us.archive.org/19/items/world_201904/French Guiana_udp.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='French Guiana_udp', cmdlist=cmdlist, finishedCallback=None)
                                return

                        elif returnValue == "com_661":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia801508.us.archive.org/19/items/world_201904/Mayotte_tcp.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='Mayotte_tcp', cmdlist=cmdlist, finishedCallback=None)
                                return

                        elif returnValue == "com_662":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia801508.us.archive.org/19/items/world_201904/Mayotte_udp.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='Mayotte_udp', cmdlist=cmdlist, finishedCallback=None)
                                return

                        elif returnValue == "com_663":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia801508.us.archive.org/19/items/world_201904/Cook Islands_tcp.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='Cook Islands_tcp', cmdlist=cmdlist, finishedCallback=None)
                                return

                        elif returnValue == "com_664":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia801508.us.archive.org/19/items/world_201904/Cook Islands_udp.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='Cook Islands_udp', cmdlist=cmdlist, finishedCallback=None)
                                return

                        elif returnValue == "com_665":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia801508.us.archive.org/19/items/world_201904/Saint Barthelemy_tcp.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='Saint Barthelemy_tcp', cmdlist=cmdlist, finishedCallback=None)
                                return

                        elif returnValue == "com_666":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia801508.us.archive.org/19/items/world_201904/Saint Barthelemy_udp.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='Saint Barthelemy_udp', cmdlist=cmdlist, finishedCallback=None)
                                return

                        elif returnValue == "com_667":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia801508.us.archive.org/19/items/world_201904/Tuvalu_tcp.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='Tuvalu_tcp', cmdlist=cmdlist, finishedCallback=None)
                                return

                        elif returnValue == "com_668":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia801508.us.archive.org/19/items/world_201904/Tuvalu_udp.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='Tuvalu_udp', cmdlist=cmdlist, finishedCallback=None)
                                return

                        elif returnValue == "com_669":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia801508.us.archive.org/19/items/world_201904/Holy See_tcp.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='Holy See_tcp', cmdlist=cmdlist, finishedCallback=None)
                                return

                        elif returnValue == "com_670":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia801508.us.archive.org/19/items/world_201904/Holy See_udp.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='Holy See_udp', cmdlist=cmdlist, finishedCallback=None)
                                return

                        elif returnValue == "com_671":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia801508.us.archive.org/19/items/world_201904/Isle of Man_tcp.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='Isle of Man_tcp', cmdlist=cmdlist, finishedCallback=None)
                                return

                        elif returnValue == "com_672":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia801508.us.archive.org/19/items/world_201904/Isle of Man_udp.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='Isle of Man_udp', cmdlist=cmdlist, finishedCallback=None)
                                return

                        elif returnValue == "com_673":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia801502.us.archive.org/4/items/FreeServerinfo/cortexa9hf-vfp-neon-ARM.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='Ncam-cortexa9hf-vfp-neon-ARM DreamoxUHD', cmdlist=cmdlist, finishedCallback=None)
                                return

                        elif returnValue == "com_674":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia801502.us.archive.org/4/items/FreeServerinfo/ncam.aarch64.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='Ncam-aarch64-ARM VU+4K Duo4K + osmio4k', cmdlist=cmdlist, finishedCallback=None)
                                return

                        elif returnValue == "com_675":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia801502.us.archive.org/4/items/FreeServerinfo/ncam.mips.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='Ncam-build-mips Gigablue-Dream-VU+-Xtrend-Formuler', cmdlist=cmdlist, finishedCallback=None)
                                return

                        elif returnValue == "com_676":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia801502.us.archive.org/4/items/FreeServerinfo/ncam.sh4.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='Ncam-build-sh4 (Golden Media-Galaxy innovations-Amiko', cmdlist=cmdlist, finishedCallback=None)
                                return

                        elif returnValue == "com_677":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia801502.us.archive.org/4/items/FreeServerinfo/oscam-all-images-arm+mips_all.ipk.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='softcams-oscam-all-images-emu-arm+mips_all.ipk', cmdlist=cmdlist, finishedCallback=None)
                                return
                                
                        elif returnValue == "com_677*":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia801502.us.archive.org/4/items/FreeServerinfo/oscam-all-images-arm+mips_all.deb.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='softcams-oscam-all-images-emu-arm+mips_all.deb', cmdlist=cmdlist, finishedCallback=None)
                                return
                                
                        elif returnValue == "com_678":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia801502.us.archive.org/4/items/FreeServerinfo/NCamEmus_all.ipk.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='softcams-ncam-all-images-emu-arm+mips_all.ipk', cmdlist=cmdlist, finishedCallback=None)
                                return
                                
                        elif returnValue == "com_678*":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia801502.us.archive.org/4/items/FreeServerinfo/NCamEmus_all.deb.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='softcams-ncam-all-images-emu-arm+mips_all.deb', cmdlist=cmdlist, finishedCallback=None)
                                return

                        elif returnValue == "com_679":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia801502.us.archive.org/4/items/FreeServerinfo/ncam.config.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='ncam.config', cmdlist=cmdlist, finishedCallback=None)
                                return

                        elif returnValue == "com_0680":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia801502.us.archive.org/4/items/FreeServerinfo/oscam.config.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='oscam.config', cmdlist=cmdlist, finishedCallback=None)
                                return

                        elif returnValue == "com_680":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia801502.us.archive.org/4/items/FreeServerinfo/gcam.config.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='gcam.config', cmdlist=cmdlist, finishedCallback=None)
                                return

                        elif returnValue == "com_681":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia801502.us.archive.org/4/items/FreeServerinfo/autokeys.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='autokeys', cmdlist=cmdlist, finishedCallback=None)
                                return

                        elif returnValue == "com_682":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia801502.us.archive.org/4/items/FreeServerinfo/cccamspeed.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='cccamspeed', cmdlist=cmdlist, finishedCallback=None)
                                return

                        elif returnValue == "com_683":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia601707.us.archive.org/24/items/dreamosat/VPNbook.ca222-TCP443.ovpn.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='vpn-ca', cmdlist=cmdlist, finishedCallback=None)
                                return

                        elif returnValue == "com_684":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia601707.us.archive.org/24/items/dreamosat/VPNbook.ca222-TCP80.ovpn.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='vpn-de', cmdlist=cmdlist, finishedCallback=None)
                                return

                        elif returnValue == "com_685":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia601707.us.archive.org/24/items/dreamosat/VPNbook.ca222-UDP25000.ovpn.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='vpn-fr', cmdlist=cmdlist, finishedCallback=None)
                                return

                        elif returnValue == "com_686":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia601707.us.archive.org/24/items/dreamosat/VPNbook.ca222-UDP53.ovpn.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='vpn-pl', cmdlist=cmdlist, finishedCallback=None)
                                return

                        elif returnValue == "com_687":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia601707.us.archive.org/24/items/dreamosat/VPNbook.de4-TCP443.ovpn.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='vpn-us', cmdlist=cmdlist, finishedCallback=None)
                                return

                        elif returnValue == "com_688":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")    
                                cmdlist.append("%s https://ia800702.us.archive.org/26/items/dreamosat/find_myCurrent-ip.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='Find My Current ip Address', cmdlist=cmdlist, finishedCallback=None)
                                return

                        elif returnValue == "com_689":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia800702.us.archive.org/26/items/dreamosat/OpenVPN_STOP.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='OpenVPN_STOP', cmdlist=cmdlist, finishedCallback=None)
                                return

                        elif returnValue == "com_690":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia601707.us.archive.org/24/items/dreamosat/VPNbook.de4-TCP443.ovpn.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='FreeVPN.be-TCP443', cmdlist=cmdlist, finishedCallback=None)
                                return

                        elif returnValue == "com_691":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia601707.us.archive.org/24/items/dreamosat/VPNbook.de4-TCP80.ovpn.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='FreeVPN.co,uk-TCP443', cmdlist=cmdlist, finishedCallback=None)
                                return

                        elif returnValue == "com_692":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia601707.us.archive.org/24/items/dreamosat/VPNbook.de4-UDP25000.ovpn.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='FreeVPN.im-TCP443', cmdlist=cmdlist, finishedCallback=None)
                                return

                        elif returnValue == "com_693":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia601707.us.archive.org/24/items/dreamosat/VPNbook.de4-UDP53.ovpn.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='FreeVPN.it-TCP443', cmdlist=cmdlist, finishedCallback=None)
                                return

                        elif returnValue == "com_694":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia601707.us.archive.org/24/items/dreamosat/VPNbook.fr1-TCP443.ovpn.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='FreeVPN.me-TCP443', cmdlist=cmdlist, finishedCallback=None)
                                return

                        elif returnValue == "com_695":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia601707.us.archive.org/24/items/dreamosat/VPNbook.fr1-TCP80.ovpn.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='FreeVPN.se-TCP443', cmdlist=cmdlist, finishedCallback=None)
                                return

                        elif returnValue == "com_696":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia601707.us.archive.org/24/items/dreamosat/VPNbook.fr1-UDP25000.ovpn.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='FreeVPN.eu-TCP443', cmdlist=cmdlist, finishedCallback=None)
                                return

                        elif returnValue == "com_697":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia601707.us.archive.org/24/items/dreamosat/VPNbook.fr1-UDP53.ovpn.sh-qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='FreeVPN.be-TCP80', cmdlist=cmdlist, finishedCallback=None)
                                return

                        elif returnValue == "com_698":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia601707.us.archive.org/24/items/dreamosat/VPNbook.fr8-TCP443.ovpn.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='FreeVPN.co.uk-TCP80', cmdlist=cmdlist, finishedCallback=None)
                                return

                        elif returnValue == "com_699":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia601707.us.archive.org/24/items/dreamosat/VPNbook.fr8-TCP80.ovpn.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='FreeVPN.im-TCP80', cmdlist=cmdlist, finishedCallback=None)
                                return

                        elif returnValue == "com_700":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia601707.us.archive.org/24/items/dreamosat/VPNbook.fr8-UDP25000.ovpn.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='FreeVPN.it-TCP80', cmdlist=cmdlist, finishedCallback=None)
                                return

                        elif returnValue == "com_701":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia601707.us.archive.org/24/items/dreamosat/VPNbook.fr8-UDP53.ovpn.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='FreeVPN.me-TCP80', cmdlist=cmdlist, finishedCallback=None)
                                return

                        elif returnValue == "com_702":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia601707.us.archive.org/24/items/dreamosat/VPNbook.pl226-TCP443.ovpn.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='FreeVPN.se-TCP80', cmdlist=cmdlist, finishedCallback=None)
                                return

                        elif returnValue == "com_703":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia601707.us.archive.org/24/items/dreamosat/VPNbook.pl226-TCP80.ovpn.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='FreeVPN.eu-TCP80', cmdlist=cmdlist, finishedCallback=None)
                                return

                        elif returnValue == "com_704":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia601707.us.archive.org/24/items/dreamosat/VPNbook.pl226-UDP25000.ovpn.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='FreeVPN.be-UDP-40000', cmdlist=cmdlist, finishedCallback=None)
                                return

                        elif returnValue == "com_705":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia601707.us.archive.org/24/items/dreamosat/VPNbook.pl226-UDP53.ovpn.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='FreeVPN.co.uk-UDP-40000', cmdlist=cmdlist, finishedCallback=None)
                                return

                        elif returnValue == "com_706":
                                cmdlist = []                                                                
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia601707.us.archive.org/24/items/dreamosat/VPNbook.us1-TCP443.ovpn.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='FreeVPN.im-UDP-40000', cmdlist=cmdlist, finishedCallback=None)
                                return

                        elif returnValue == "com_707":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia601707.us.archive.org/24/items/dreamosat/VPNbook.us1-TCP80.ovpn.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='FreeVPN.it-UDP-40000', cmdlist=cmdlist, finishedCallback=None)
                                return

                        elif returnValue == "com_708":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia601707.us.archive.org/24/items/dreamosat/VPNbook.us1-UDP25000.ovpn.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='FreeVPN.me-UDP-40000', cmdlist=cmdlist, finishedCallback=None)
                                return

                        elif returnValue == "com_709":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia601707.us.archive.org/24/items/dreamosat/VPNbook.us1-UDP53.ovpn.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='FreeVPN.se-UDP-40000', cmdlist=cmdlist, finishedCallback=None)
                                return

                        elif returnValue == "com_710":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia601707.us.archive.org/24/items/dreamosat/VPNbook.us2-TCP443.ovpn.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='FreeVPN.eu-UDP-40000', cmdlist=cmdlist, finishedCallback=None)
                                return

                        elif returnValue == "com_711":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia601707.us.archive.org/24/items/dreamosat/VPNbook.us2-TCP80.ovpn.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='FreeVPN.be-UDP-53', cmdlist=cmdlist, finishedCallback=None)
                                return

                        elif returnValue == "com_712":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia601707.us.archive.org/24/items/dreamosat/VPNbook.us2-UDP25000.ovpn.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='FreeVPN.co.uk-UDP-53', cmdlist=cmdlist, finishedCallback=None)
                                return

                        elif returnValue == "com_713":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia601707.us.archive.org/24/items/dreamosat/VPNbook.us2-UDP53.ovpn.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='FreeVPN.im-UDP-53', cmdlist=cmdlist, finishedCallback=None)
                                return

                        elif returnValue == "com_714":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia800702.us.archive.org/26/items/dreamosat/FreeVPN.me-TCP443.ovpn.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='FreeVPN.it-UDP-53', cmdlist=cmdlist, finishedCallback=None)
                                return

                        elif returnValue == "com_715":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia800702.us.archive.org/26/items/dreamosat/FreeVPN.me-TCP80.ovpn.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='FreeVPN.me-UDP-53', cmdlist=cmdlist, finishedCallback=None)
                                return

                        elif returnValue == "com_716":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia800702.us.archive.org/26/items/dreamosat/FreeVPN.me-UDP-40000.ovpn.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='FreeVPN.se-UDP-53', cmdlist=cmdlist, finishedCallback=None)
                                return

                        elif returnValue == "com_717":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia800702.us.archive.org/26/items/dreamosat/FreeVPN.me-UDP-53.ovpn.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='FreeVPN.eu-UDP-53', cmdlist=cmdlist, finishedCallback=None)
                                return

                        elif returnValue == "com_718":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia903002.us.archive.org/34/items/world_201904/USA_1_tcp.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='FreeVPN.co.uk-UDP-40000', cmdlist=cmdlist, finishedCallback=None)
                                return

                        elif returnValue == "com_719":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia903002.us.archive.org/34/items/world_201904/USA_1_udp.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='FreeVPN.im-UDP-40000', cmdlist=cmdlist, finishedCallback=None)
                                return

                        elif returnValue == "com_720":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia903002.us.archive.org/34/items/world_201904/USA_2_tcp.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='FreeVPN.it-UDP-40000', cmdlist=cmdlist, finishedCallback=None)
                                return

                        elif returnValue == "com_721":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia903002.us.archive.org/34/items/world_201904/USA_2_udp.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='FreeVPN.me-UDP-40000', cmdlist=cmdlist, finishedCallback=None)
                                return

                        elif returnValue == "com_722":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia903002.us.archive.org/34/items/world_201904/USA_3_tcp.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='FreeVPN.se-UDP-40000', cmdlist=cmdlist, finishedCallback=None)
                                return

                        elif returnValue == "com_723":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia903002.us.archive.org/34/items/world_201904/USA_3_udp.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='FreeVPN.eu-UDP-40000', cmdlist=cmdlist, finishedCallback=None)
                                return

                        elif returnValue == "com_724":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia903002.us.archive.org/34/items/world_201904/USA_4_tcp.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='FreeVPN.be-UDP-53', cmdlist=cmdlist, finishedCallback=None)
                                return

                        elif returnValue == "com_725":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia903002.us.archive.org/34/items/world_201904/USA_4_udp.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='FreeVPN.co.uk-UDP-53', cmdlist=cmdlist, finishedCallback=None)
                                return

                        elif returnValue == "com_726":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia903002.us.archive.org/34/items/world_201904/USA_5_tcp.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='FreeVPN.im-UDP-53', cmdlist=cmdlist, finishedCallback=None)
                                return

                        elif returnValue == "com_727":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia903002.us.archive.org/34/items/world_201904/USA_5_udp.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='FreeVPN.it-UDP-53', cmdlist=cmdlist, finishedCallback=None)
                                return

                        elif returnValue == "com_728":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia903002.us.archive.org/34/items/world_201904/USA_6_tcp.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='FreeVPN.me-UDP-53', cmdlist=cmdlist, finishedCallback=None)
                                return

                        elif returnValue == "com_729":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia903002.us.archive.org/34/items/world_201904/USA_6_udp.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='FreeVPN.se-UDP-53', cmdlist=cmdlist, finishedCallback=None)
                                return

                        elif returnValue == "com_730":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia903002.us.archive.org/34/items/world_201904/USA_7_tcp.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='FreeVPN.eu-UDP-53', cmdlist=cmdlist, finishedCallback=None)
                                return

                        elif returnValue == "com_731":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia903002.us.archive.org/34/items/world_201904/USA_7_udp.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='FreeVPN.me-UDP-40000', cmdlist=cmdlist, finishedCallback=None)
                                return

                        elif returnValue == "com_732":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia903002.us.archive.org/34/items/world_201904/USA_8_tcp.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='FreeVPN.se-UDP-40000', cmdlist=cmdlist, finishedCallback=None)
                                return

                        elif returnValue == "com_733":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia903002.us.archive.org/34/items/world_201904/USA_8_udp.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='FreeVPN.eu-UDP-40000', cmdlist=cmdlist, finishedCallback=None)
                                return

                        elif returnValue == "com_734":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia903002.us.archive.org/34/items/world_201904/USA_9_tcp.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='FreeVPN.be-UDP-53', cmdlist=cmdlist, finishedCallback=None)
                                return

                        elif returnValue == "com_735":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia903002.us.archive.org/34/items/world_201904/USA_9_udp.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='FreeVPN.co.uk-UDP-53', cmdlist=cmdlist, finishedCallback=None)
                                return

                        elif returnValue == "com_736":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia903002.us.archive.org/34/items/world_201904/USA_10_tcp.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='FreeVPN.im-UDP-53', cmdlist=cmdlist, finishedCallback=None)
                                return

                        elif returnValue == "com_737":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia903002.us.archive.org/34/items/world_201904/USA_10_udp.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='FreeVPN.it-UDP-53', cmdlist=cmdlist, finishedCallback=None)
                                return

                        elif returnValue == "com_738":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia903002.us.archive.org/34/items/world_201904/Canada_1_tcp.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='FreeVPN.me-UDP-53', cmdlist=cmdlist, finishedCallback=None)
                                return

                        elif returnValue == "com_739":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia903002.us.archive.org/34/items/world_201904/Canada_1_udp.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='FreeVPN.se-UDP-53', cmdlist=cmdlist, finishedCallback=None)
                                return

                        elif returnValue == "com_740":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia903002.us.archive.org/34/items/world_201904/Canada_2_tcp.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='FreeVPN.eu-UDP-53', cmdlist=cmdlist, finishedCallback=None)
                                return

                        elif returnValue == "com_741":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia903002.us.archive.org/34/items/world_201904/Canada_2_udp.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='FreeVPN.eu-UDP-53', cmdlist=cmdlist, finishedCallback=None)
                                return

                        else:
                                print("\n[MyShPrombt] cancel\n")
                                self.close(None)

                                
        #def setMyText(self):
                #self["myText"].setText(self.text)
                #self["myText"].setText(str(text))
                
        def prombt(self, com):
            scripts = "/usr/lib/enigma2/python/Plugins/Extensions/FreeServer/scripts/"
            os.chmod(scripts, 755)
            self.session.open(Console3,_("Executing: %s") % (com), ["%s" % com])
                                                
        def myInput(self):
            from Plugins.Extensions.FreeServer.outils.myInput import myInput
            self.session.open(myInput)   
            
        def Freeserver(self):
                self.session.open(Console3, title='Free Server', cmdlist=["sh '/usr/lib/enigma2/python/Plugins/Extensions/FreeServer/FreeServer.sh'"]) 
                                                
        def cancel(self):
                print("\n[MyShPrombt] cancel\n")
                self.close(None)

def main(session, **kwargs):
        print("\n[MyShPrombt] start\n")
        session.open(MyShPrombt)
