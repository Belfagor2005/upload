# -*- coding: UTF-8 -*-
from __future__ import print_function

from Plugins.Plugin import PluginDescriptor
from Screens.Screen import Screen
from Components.ScrollLabel import ScrollLabel
from enigma import eTimer, getDesktop
version = '8.3.8'
from enigma import eTimer
from datetime import date, datetime
from Components.Label import Label, MultiColorLabel
from Screens.Standby import TryQuitMainloop
from Components.MenuList import MenuList
from Components.ActionMap import NumberActionMap, ActionMap
from Plugins.Extensions.FreeServer.outils.MyShPrombt import *
from Components.MediaPlayer import *
import os
from struct import pack
from enigma import *
from Screens.MessageBox import MessageBox
from Screens.InputBox import InputBox
from Screens.ChoiceBox import ChoiceBox
from Components.Pixmap import Pixmap  
from Components.GUIComponent import *
from Components.Input import Input
from Components.ConfigList import ConfigList
from Screens.ServiceInfo import *
from Tools import Notifications
from Components.config import *
from enigma import eServiceReference
import re
session = None
from time import *
import time
import datetime
### EDit By RAED To DreamOS OE2.5/2.6
from Tools.Directories import fileExists
from Plugins.Extensions.FreeServer.outils.Console3 import *

######################################################################################################
plugin_path = '/usr/lib/enigma2/python/Plugins/Extensions/FreeServer/fonts'
skin_path = '/usr/lib/enigma2/python/Plugins/Extensions/FreeServer/Skin/'
p_path = '/usr/lib/enigma2/python/Plugins/Extensions/FreeServer'   
from enigma import addFont
try:
    #addFont('%s/Raleway-Black.ttf' % plugin_path, 'Rale', 100, 1)
    addFont('%s/bpmono.ttf' % plugin_path, 'bpmo', 100, 1)
    #addFont('%s/slyk-medium.ttf' % plugin_path, 'slyk', 100, 1)
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
class MyKoraScreen2(Screen):
#### Edit By RAED
        if isHD():
            skin = """
                 <screen position="40,50" size="1200,636" title="IPTV WORLD SPORT MOVIES        CHANNELS" flags="wfNoBorder" backgroundColor="#20000000">
                      <widget source="Title" render="Label" position="0,3" size="1200,28" zPosition="3" halign="center" valign="center" font="Regular;26" backgroundColor="#20000000" transparent="1" foregroundColor="#bab329"/>       
                      <widget name="myRedBtn" position="10,556" size="100,40" backgroundColor="red" valign="center" halign="center" zPosition="2"  foregroundColor="white" font="Regular;20"/>
                      <widget name="myGreenBtn" position="120,556" size="100,40" backgroundColor="green" valign="center" halign="center" zPosition="2"  foregroundColor="white" font="Regular;20"/>
                      <!--widget name="myYellowBtn" position="230,556" size="100,40" backgroundColor="yellow" valign="center" halign="center" zPosition="2"  foregroundColor="white" font="Regular;20">
                      <widget name="myBlueBtn" position="340,556" size="100,40" backgroundColor="blue" valign="center" halign="center" zPosition="2"  foregroundColor="white" font="Regular;20"/>                       
                      <widget font="Regular; 16" halign="center" name="tries" position="856,175" size="680,150" zPosition="1" /-->
                      <widget name="myMenu" position="0,40" size="620,500" foregroundColor="#FEFEFE" transparent="1" zPosition="2" />
                      <!--ePixmap position="0,0" size="1920,1080" pixmap="/usr/lib/enigma2/python/Plugins/Extensions/FreeServer/Deco/mainbj.jpg" alphatest="blend" transparent="1" />
                      <widget name="myMenu2" position="0,0" size="620,500" flags="wfNoBorder" backgroundColor="#00000000" halign="right"/-->
                 </screen>"""
        else:
            skin = """
                 <screen position="0,0" size="1920,1080" title="IPTV WORLD SPORT MOVIES        CHANNELS" flags="wfNoBorder" backgroundColor="#20000000">
                      <widget source="Title" render="Label" position="0,3" size="1920,32" zPosition="3" halign="center" valign="center" font="Regular;30" backgroundColor="#20000000" transparent="1" foregroundColor="#bab329" />      
                      <widget name="myRedBtn" position="30,1030" size="130,40" backgroundColor="red" valign="center" halign="center" zPosition="2"  foregroundColor="white" font="Regular;33"/>
                      <widget name="myGreenBtn" position="170,1030" size="130,40" backgroundColor="green" valign="center" halign="center" zPosition="2"  foregroundColor="white" font="Regular;33"/>
                      <!--widget name="myYellowBtn" position="260,556" size="130,40" backgroundColor="yellow" valign="center" halign="center" zPosition="2"  foregroundColor="white" font="Regular;20"/>
                      <widget name="myBlueBtn" position="340,556" size="100,40" backgroundColor="blue" valign="center" halign="center" zPosition="2"  foregroundColor="white" font="Regular;20"/>                       
                      <widget font="Regular; 26" halign="center" name="tries" position="856,175" size="680,150" zPosition="1" /-->
                      <widget name="myMenu" position="5,40" size="1690,1000" foregroundColor="#FEFEFE" transparent="1" zPosition="2" />
                      <!--ePixmap position="0,0" size="1920,1080" pixmap="/usr/lib/enigma2/python/Plugins/Extensions/FreeServer/Deco/mainbjfhd.jpg" alphatest="blend" transparent="1" />
                      <widget name="myMenu2" position="0,0" size="620,500" flags="wfNoBorder" backgroundColor="#00000000" halign="right"/-->
                 </screen>"""

        def __init__(self, session, picPath = None, args = 0):
                Screen.__init__(self, session)  
                #self.text=""
                #self.text="IPTV WORLD SPORT MOVIES        CHANNELS"
### EDit By RAED3 To DreamOS OE2.5/2.6
                #if fileExists('/var/lib/dpkg/status'):
                #     self.wget = "/usr/bin/wget2 --no-check-certificate"
                #else:
                #     self.wget = "/usr/bin/wget"
                self.wget = "wget --no-check-certificate"
### End
                list = []
                list.append(("  LISTS IPTV SPORTS", "com_***"))         
                list.append(("  IPTVFree001", "com_1"))
                list.append(("  IPTVFree002", "com_2")) 
                list.append(("  IPTVFree003", "com_3"))
                list.append(("  IPTVFree004", "com_4")) 
                list.append(("  IPTVFree005", "com_5"))
                list.append(("  IPTVFree006", "com_6"))             
                list.append(("  IPTVFree007", "com_7"))
                list.append(("  IPTVFree008", "com_8"))          
                list.append(("  IPTVFree009", "com_9"))
                list.append(("  IPTVFree010", "com_10"))
                list.append(("  IPTVFree011", "com_11"))
                list.append(("  IPTVFree012", "com_12"))  
                list.append(("  IPTVFree013", "com_13"))
                list.append(("  IPTVFree014", "com_14"))
                list.append(("  IPTVFree015", "com_15"))                              
                list.append(("  IPTVFree016", "com_16"))                
                list.append(("  IPTVFree017", "com_17"))
                list.append(("  IPTVFree018", "com_18"))                
                list.append(("  IPTVFree019", "com_19"))
                list.append(("  IPTVFree020", "com_20"))
                list.append(("  IPTVFree021", "com_21"))
                list.append(("  IPTVFree022", "com_22"))
                list.append(("  IPTVFree023", "com_23"))
                list.append(("  IPTVFree024", "com_24"))
                list.append(("  IPTVFree025", "com_25"))
                list.append(("  IPTVFree026", "com_26"))                
                list.append(("  IPTVFree027", "com_27"))
                list.append(("  IPTVFree028", "com_28"))
                list.append(("  IPTVFree029", "com_29"))
                list.append(("  IPTVFree030", "com_30"))
                list.append(("  IPTVFree031", "com_31"))
                list.append(("  IPTVFree032", "com_32"))
                list.append(("  IPTVFree033", "com_33"))                
                list.append(("  IPTVFree034", "com_34"))
                list.append(("  IPTVFree035", "com_35"))
                list.append(("  IPTVFree036", "com_36"))
                list.append(("  IPTVFree037", "com_37"))
                list.append(("  IPTVFree038", "com_38"))
                list.append(("  IPTVFree039", "com_39"))
                list.append(("  IPTVFree040", "com_40"))
                list.append(("  IPTVFree041", "com_41"))
                list.append(("  IPTVFree042", "com_42"))
                list.append(("  IPTVFree043", "com_43"))
                list.append(("  IPTVFree044", "com_44"))  
                list.append(("  IPTVFree045", "com_45"))  
                list.append(("  IPTVFree046", "com_46"))
                list.append(("  IPTVFree047", "com_47"))  
                list.append(("  IPTVFree048", "com_48"))
                list.append(("  IPTVFree049", "com_49"))                  
                list.append(("  IPTVFree050", "com_50"))
                list.append(("  IPTVFree051", "com_51"))
                list.append(("  IPTVFree052", "com_52"))
                list.append(("  IPTVFree053", "com_53"))
                list.append(("  IPTVFree054", "com_54"))
                list.append(("  IPTVFree055", "com_55"))  
                list.append(("  IPTVFree056", "com_56"))  
                list.append(("  IPTVFree057", "com_57"))
                list.append(("  IPTVFree058", "com_58"))  
                list.append(("  IPTVFree059", "com_59"))
                list.append(("  IPTVFree060", "com_60")) 
                list.append(("  IPTVFree061", "com_61"))
                list.append(("  IPTVFree062", "com_62"))
                list.append(("  IPTVFree063", "com_63"))
                list.append(("  IPTVFree064", "com_64"))
                list.append(("  IPTVFree065", "com_65"))  
                list.append(("  IPTVFree066", "com_66"))  
                list.append(("  IPTVFree067", "com_67"))
                list.append(("  IPTVFree068", "com_68"))  
                list.append(("  IPTVFree069", "com_69"))
                list.append(("  IPTVFree070", "com_70")) 
                list.append(("  IPTVFree071", "com_71"))
                list.append(("  IPTVFree072", "com_72"))
                list.append(("  IPTVFree073", "com_73"))
                list.append(("  IPTVFree074", "com_74"))
                list.append(("  IPTVFree075", "com_75"))  
                list.append(("  IPTVFree076", "com_76"))  
                list.append(("  IPTVFree077", "com_77"))
                list.append(("  IPTVFree078", "com_78"))  
                list.append(("  IPTVFree079", "com_79"))
                list.append(("  IPTVFree080", "com_80")) 
                list.append(("  IPTVFree081", "com_81"))
                list.append(("  IPTVFree082", "com_82"))
                list.append(("  IPTVFree083", "com_83"))
                list.append(("  IPTVFree084", "com_84"))
                list.append(("  IPTVFree085", "com_85"))  
                list.append(("  IPTVFree086", "com_86"))  
                list.append(("  IPTVFree087", "com_87"))
                list.append(("  IPTVFree088", "com_88"))  
                list.append(("  IPTVFree089", "com_89"))
                list.append(("  IPTVFree090", "com_90")) 
                list.append(("  IPTVFree091", "com_91"))
                list.append(("  IPTVFree092", "com_92"))
                list.append(("  IPTVFree093", "com_93"))
                list.append(("  IPTVFree094", "com_94"))
                list.append(("  IPTVFree095", "com_95"))  
                list.append(("  IPTVFree096", "com_96"))  
                list.append(("  IPTVFree097", "com_97"))
                list.append(("  IPTVFree098", "com_98"))  
                list.append(("  IPTVFree099", "com_99"))
                list.append(("  IPTVFree100", "com_100"))
                list.append(("  IPTV WORLD CHANNELS", "com_***"))
                list.append(("  SPRORTWORLD001", "com_101"))
                list.append(("  SPRORTWORLD002", "com_102"))    
                list.append(("  SPRORTWORLD003", "com_103"))
                list.append(("  SPRORTWORLD004", "com_104")) 
                list.append(("  SPRORTWORLD005", "com_105"))
                list.append(("  SPRORTWORLD006", "com_106"))             
                list.append(("  SPRORTWORLD007", "com_107"))
                list.append(("  SPRORTWORLD008", "com_108"))          
                list.append(("  SPRORTWORLD009", "com_109"))
                list.append(("  SPRORTWORLD010", "com_110"))
                list.append(("  SPRORTWORLD011", "com_111"))
                list.append(("  SPRORTWORLD012", "com_112"))  
                list.append(("  SPRORTWORLD013", "com_113"))
                list.append(("  SPRORTWORLD014", "com_114"))
                list.append(("  SPRORTWORLD015", "com_115"))                              
                list.append(("  SPRORTWORLD016", "com_116"))            
                list.append(("  SPRORTWORLD017", "com_117"))
                list.append(("  SPRORTWORLD018", "com_118"))                    
                list.append(("  SPRORTWORLD019", "com_119"))
                list.append(("  SPRORTWORLD020", "com_120"))
                list.append(("  SPRORTWORLD021", "com_121"))
                list.append(("  SPRORTWORLD022", "com_122"))
                list.append(("  SPRORTWORLD023", "com_123"))
                list.append(("  SPRORTWORLD024", "com_124"))
                list.append(("  SPRORTWORLD025", "com_125"))
                list.append(("  SPRORTWORLD026", "com_126"))                    
                list.append(("  SPRORTWORLD027", "com_127"))
                list.append(("  SPRORTWORLD028", "com_128"))
                list.append(("  SPRORTWORLD029", "com_129"))
                list.append(("  SPRORTWORLD030", "com_130"))
                list.append(("  SPRORTWORLD031", "com_131"))
                list.append(("  SPRORTWORLD032", "com_132"))
                list.append(("  SPRORTWORLD033", "com_133"))                    
                list.append(("  SPRORTWORLD034", "com_134"))
                list.append(("  SPRORTWORLD035", "com_135"))
                list.append(("  SPRORTWORLD036", "com_136"))
                list.append(("  SPRORTWORLD037", "com_137"))
                list.append(("  SPRORTWORLD038", "com_138"))
                list.append(("  SPRORTWORLD039", "com_139"))
                list.append(("  SPRORTWORLD040", "com_140"))
                list.append(("  SPRORTWORLD041", "com_141"))
                list.append(("  SPRORTWORLD042", "com_142"))
                list.append(("  SPRORTWORLD043", "com_143"))
                list.append(("  SPRORTWORLD044", "com_144"))  
                list.append(("  SPRORTWORLD045", "com_145"))  
                list.append(("  SPRORTWORLD046", "com_146"))
                list.append(("  SPRORTWORLD047", "com_147"))  
                list.append(("  SPRORTWORLD048", "com_148"))
                list.append(("  SPRORTWORLD049", "com_149"))                  
                list.append(("  SPRORTWORLD050", "com_150"))
                list.append(("  SPRORTWORLD051", "com_151"))
                list.append(("  SPRORTWORLD052", "com_152"))
                list.append(("  SPRORTWORLD053", "com_153"))
                list.append(("  SPRORTWORLD054", "com_154"))
                list.append(("  SPRORTWORLD055", "com_155"))  
                list.append(("  SPRORTWORLD056", "com_156"))  
                list.append(("  SPRORTWORLD057", "com_157"))
                list.append(("  SPRORTWORLD058", "com_158"))  
                list.append(("  SPRORTWORLD059", "com_159"))
                list.append(("  SPRORTWORLD060", "com_160")) 
                list.append(("  SPRORTWORLD061", "com_161"))
                list.append(("  SPRORTWORLD062", "com_162"))
                list.append(("  SPRORTWORLD063", "com_163"))
                list.append(("  SPRORTWORLD064", "com_164"))
                list.append(("  SPRORTWORLD065", "com_165"))  
                list.append(("  SPRORTWORLD066", "com_166"))  
                list.append(("  SPRORTWORLD067", "com_167"))
                list.append(("  SPRORTWORLD068", "com_168"))  
                list.append(("  SPRORTWORLD069", "com_169"))
                list.append(("  SPRORTWORLD070", "com_170")) 
                list.append(("  SPRORTWORLD071", "com_171"))
                list.append(("  SPRORTWORLD072", "com_172"))
                list.append(("  SPRORTWORLD073", "com_173"))
                list.append(("  SPRORTWORLD074", "com_174"))
                list.append(("  SPRORTWORLD075", "com_175"))  
                list.append(("  SPRORTWORLD076", "com_176"))  
                list.append(("  SPRORTWORLD077", "com_177"))
                list.append(("  SPRORTWORLD078", "com_178"))  
                list.append(("  SPRORTWORLD079", "com_179"))
                list.append(("  SPRORTWORLD080", "com_180")) 
                list.append(("  SPRORTWORLD081", "com_181"))
                list.append(("  SPRORTWORLD082", "com_182"))
                list.append(("  SPRORTWORLD083", "com_183"))
                list.append(("  SPRORTWORLD084", "com_184"))
                list.append(("  SPRORTWORLD085", "com_185"))  
                list.append(("  SPRORTWORLD086", "com_186"))  
                list.append(("  SPRORTWORLD087", "com_187"))
                list.append(("  SPRORTWORLD088", "com_188"))  
                list.append(("  SPRORTWORLD089", "com_189"))
                list.append(("  SPRORTWORLD090", "com_190")) 
                list.append(("  SPRORTWORLD091", "com_191"))
                list.append(("  SPRORTWORLD092", "com_192"))
                list.append(("  SPRORTWORLD093", "com_193"))
                list.append(("  SPRORTWORLD094", "com_194"))
                list.append(("  SPRORTWORLD095", "com_195"))  
                list.append(("  SPRORTWORLD096", "com_196"))  
                list.append(("  SPRORTWORLD097", "com_197"))
                list.append(("  SPRORTWORLD098", "com_198"))  
                list.append(("  SPRORTWORLD099", "com_199"))
                list.append(("  SPRORTWORLD100", "com_200")) 
                list.append(("  **** ARABE ****  ", "com_***"))                 
                list.append(("  IPTVWORLDAR001", "com_201"))
                list.append(("  IPTVWORLDAR002", "com_202"))    
                list.append(("  IPTVWORLDAR003", "com_203"))
                list.append(("  IPTVWORLDAR004", "com_204")) 
                list.append(("  IPTVWORLDAR005", "com_205"))
                list.append(("  IPTVWORLDAR006", "com_206"))             
                list.append(("  IPTVWORLDAR007", "com_207"))
                list.append(("  IPTVWORLDAR008", "com_208"))          
                list.append(("  IPTVWORLDAR009", "com_209"))
                list.append(("  IPTVWORLDAR010", "com_210"))
                list.append(("  IPTVWORLDAR011", "com_211"))
                list.append(("  IPTVWORLDAR012", "com_212"))  
                list.append(("  IPTVWORLDAR013", "com_213"))
                list.append(("  IPTVWORLDAR014", "com_214"))
                list.append(("  IPTVWORLDAR015", "com_215"))                              
                list.append(("  IPTVWORLDAR016", "com_216"))            
                list.append(("  IPTVWORLDAR017", "com_217"))
                list.append(("  IPTVWORLDAR018", "com_218"))                    
                list.append(("  IPTVWORLDAR019", "com_219"))
                list.append(("  IPTVWORLDAR020", "com_220"))
                list.append(("  IPTVWORLDAR021", "com_221"))
                list.append(("  IPTVWORLDAR022", "com_222"))
                list.append(("  IPTVWORLDAR023", "com_223"))
                list.append(("  IPTVWORLDAR024", "com_224"))
                list.append(("  IPTVWORLDAR025", "com_225"))
                list.append(("  IPTVWORLDAR026", "com_226"))                    
                list.append(("  IPTVWORLDAR027", "com_227"))
                list.append(("  IPTVWORLDAR028", "com_228"))
                list.append(("  IPTVWORLDAR029", "com_229"))
                list.append(("  IPTVWORLDAR030", "com_230"))
                list.append(("  IPTVWORLDAR031", "com_231"))
                list.append(("  IPTVWORLDAR032", "com_232"))
                list.append(("  IPTVWORLDAR033", "com_233"))                    
                list.append(("  IPTVWORLDAR034", "com_234"))
                list.append(("  IPTVWORLDAR035", "com_235"))
                list.append(("  IPTVWORLDAR036", "com_236"))
                list.append(("  IPTVWORLDAR037", "com_237"))
                list.append(("  IPTVWORLDAR038", "com_238"))
                list.append(("  IPTVWORLDAR039", "com_239"))
                list.append(("  IPTVWORLDAR040", "com_240"))
                list.append(("  IPTVWORLDAR041", "com_241"))
                list.append(("  IPTVWORLDAR042", "com_242"))
                list.append(("  IPTVWORLDAR043", "com_243"))
                list.append(("  IPTVWORLDAR044", "com_244"))  
                list.append(("  IPTVWORLDAR045", "com_245"))  
                list.append(("  IPTVWORLDAR046", "com_246"))
                list.append(("  IPTVWORLDAR047", "com_247"))  
                list.append(("  IPTVWORLDAR048", "com_248"))
                list.append(("  IPTVWORLDAR049", "com_249"))                  
                list.append(("  IPTVWORLDAR050", "com_250"))
                list.append(("  IPTVWORLDAR051", "com_251"))
                list.append(("  IPTVWORLDAR052", "com_252"))
                list.append(("  IPTVWORLDAR053", "com_253"))
                list.append(("  IPTVWORLDAR054", "com_254"))
                list.append(("  IPTVWORLDAR055", "com_255"))  
                list.append(("  IPTVWORLDAR056", "com_256"))  
                list.append(("  IPTVWORLDAR057", "com_257"))
                list.append(("  IPTVWORLDAR058", "com_258"))  
                list.append(("  IPTVWORLDAR059", "com_259"))
                list.append(("  IPTVWORLDAR060", "com_260")) 
                list.append(("  IPTVWORLDAR061", "com_261"))
                list.append(("  IPTVWORLDAR062", "com_262"))
                list.append(("  IPTVWORLDAR063", "com_263"))
                list.append(("  IPTVWORLDAR064", "com_264"))
                list.append(("  IPTVWORLDAR065", "com_265"))  
                list.append(("  IPTVWORLDAR066", "com_266"))  
                list.append(("  IPTVWORLDAR067", "com_267"))
                list.append(("  IPTVWORLDAR068", "com_268"))  
                list.append(("  IPTVWORLDAR069", "com_269"))
                list.append(("  IPTVWORLDAR070", "com_270")) 
                list.append(("  IPTVWORLDAR071", "com_271"))
                list.append(("  IPTVWORLDAR072", "com_272"))
                list.append(("  IPTVWORLDAR073", "com_273"))
                list.append(("  IPTVWORLDAR074", "com_274"))
                list.append(("  IPTVWORLDAR075", "com_275"))  
                list.append(("  IPTVWORLDAR076", "com_276"))  
                list.append(("  IPTVWORLDAR077", "com_277"))
                list.append(("  IPTVWORLDAR078", "com_278"))  
                list.append(("  IPTVWORLDAR079", "com_279"))
                list.append(("  IPTVWORLDAR080", "com_280"))            
                list.append(("  **** FRANCE **** ", "com_***"))                 
                list.append(("  IPTVWORLDFR001", "com_281"))
                list.append(("  IPTVWORLDFR002", "com_282"))
                list.append(("  IPTVWORLDFR003", "com_283"))
                list.append(("  IPTVWORLDFR004", "com_284"))
                list.append(("  IPTVWORLDFR005", "com_285"))  
                list.append(("  IPTVWORLDFR006", "com_286"))  
                list.append(("  IPTVWORLDFR007", "com_287"))
                list.append(("  IPTVWORLDFR008", "com_288"))  
                list.append(("  IPTVWORLDFR009", "com_289"))
                list.append(("  IPTVWORLDFR010", "com_290")) 
                list.append(("  IPTVWORLDFR011", "com_291"))
                list.append(("  IPTVWORLDFR012", "com_292"))
                list.append(("  IPTVWORLDFR013", "com_293"))
                list.append(("  IPTVWORLDFR014", "com_294"))
                list.append(("  IPTVWORLDFR015", "com_295"))  
                list.append(("  IPTVWORLDFR016", "com_296"))  
                list.append(("  IPTVWORLDFR017", "com_297"))
                list.append(("  IPTVWORLDFR018", "com_298"))  
                list.append(("  IPTVWORLDFR019", "com_299"))
                list.append(("  IPTVWORLDFR020", "com_300"))  
                list.append(("  IPTVWORLDFR021", "com_301"))
                list.append(("  IPTVWORLDFR022", "com_302"))    
                list.append(("  IPTVWORLDFR023", "com_303"))
                list.append(("  IPTVWORLDFR024", "com_304")) 
                list.append(("  IPTVWORLDFR025", "com_305"))
                list.append(("  IPTVWORLDFR026", "com_306"))             
                list.append(("  IPTVWORLDFR027", "com_307"))
                list.append(("  IPTVWORLDFR028", "com_308"))          
                list.append(("  IPTVWORLDFR029", "com_309"))
                list.append(("  IPTVWORLDFR030", "com_310"))
                list.append(("  IPTVWORLDFR031", "com_311"))
                list.append(("  IPTVWORLDFR032", "com_312"))  
                list.append(("  IPTVWORLDFR033", "com_313"))
                list.append(("  IPTVWORLDFR034", "com_314"))
                list.append(("  IPTVWORLDFR035", "com_315"))                              
                list.append(("  IPTVWORLDFR036", "com_316"))            
                list.append(("  IPTVWORLDFR037", "com_317"))
                list.append(("  IPTVWORLDFR038", "com_318"))                    
                list.append(("  IPTVWORLDFR039", "com_319"))
                list.append(("  IPTVWORLDFR040", "com_320"))
                list.append(("  ***** USA *****  ", "com_***"))         
                list.append(("  IPTVWORLDUS001", "com_321"))
                list.append(("  IPTVWORLDUS002", "com_322"))
                list.append(("  IPTVWORLDUS003", "com_323"))
                list.append(("  IPTVWORLDUS004", "com_324"))
                list.append(("  IPTVWORLDUS005", "com_325"))
                list.append(("  IPTVWORLDUS006", "com_326"))                    
                list.append(("  IPTVWORLDUS007", "com_327"))
                list.append(("  IPTVWORLDUS008", "com_328"))
                list.append(("  IPTVWORLDUS009", "com_329"))
                list.append(("  IPTVWORLDUS010", "com_330"))
                list.append(("  IPTVWORLDUS011", "com_331"))
                list.append(("  IPTVWORLDUS012", "com_332"))
                list.append(("  IPTVWORLDUS013", "com_333"))                    
                list.append(("  IPTVWORLDUS014", "com_334"))
                list.append(("  IPTVWORLDUS015", "com_335"))
                list.append(("  IPTVWORLDUS016", "com_336"))
                list.append(("  IPTVWORLDUS017", "com_337"))
                list.append(("  IPTVWORLDUS018", "com_338"))
                list.append(("  IPTVWORLDUS019", "com_339"))
                list.append(("  IPTVWORLDUS020", "com_340"))
                list.append(("  IPTVWORLDUS021", "com_341"))
                list.append(("  IPTVWORLDUS022", "com_342"))
                list.append(("  ***** RUSSE *****  ", "com_***"))               
                list.append(("  IPTVWORLDRU001", "com_343"))
                list.append(("  IPTVWORLDRU002", "com_344"))  
                list.append(("  IPTVWORLDRU003", "com_345"))  
                list.append(("  IPTVWORLDRU004", "com_346"))
                list.append(("  IPTVWORLDRU005", "com_347"))  
                list.append(("  IPTVWORLDRU006", "com_348"))
                list.append(("  IPTVWORLDRU007", "com_349"))                  
                list.append(("  IPTVWORLDRU008", "com_350"))
                list.append(("  IPTVWORLDRU009", "com_351"))
                list.append(("  IPTVWORLDRU010", "com_352"))
                list.append(("  IPTVWORLDRU011", "com_353"))
                list.append(("  IPTVWORLDRU012", "com_354"))
                list.append(("  IPTVWORLDRU013", "com_355"))  
                list.append(("  IPTVWORLDRU014", "com_356"))  
                list.append(("  IPTVWORLDRU015", "com_357"))
                list.append(("  IPTVWORLDRU016", "com_358"))  
                list.append(("  IPTVWORLDRU017", "com_359"))
                list.append(("  IPTVWORLDRU018", "com_360")) 
                list.append(("  IPTVWORLDRU019", "com_361"))
                list.append(("  IPTVWORLDRU020", "com_362"))
                list.append(("  IPTVWORLDRU021", "com_363"))
                list.append(("  IPTVWORLDRU022", "com_364"))
                list.append(("  ***** POLAND *****  ", "com_***"))              
                list.append(("  IPTVWORLDPL001", "com_365"))  
                list.append(("  IPTVWORLDPL002", "com_366"))  
                list.append(("  IPTVWORLDPL003", "com_367"))
                list.append(("  IPTVWORLDPL004", "com_368"))  
                list.append(("  IPTVWORLDPL005", "com_369"))
                list.append(("  IPTVWORLDPL006", "com_370")) 
                list.append(("  IPTVWORLDPL007", "com_371"))
                list.append(("  ***** DEUTSHLAND *****  ", "com_***")) 
                list.append(("  IPTVWORLDDE001", "com_372"))
                list.append(("  IPTVWORLDDE002", "com_373"))
                list.append(("  IPTVWORLDDE003", "com_374"))
                list.append(("  IPTVWORLDDE004", "com_375"))  
                list.append(("  IPTVWORLDDE005", "com_376"))  
                list.append(("  IPTVWORLDDE006", "com_377"))
                list.append(("  IPTVWORLDDE007", "com_378"))  
                list.append(("  IPTVWORLDDE008", "com_379"))
                list.append(("  IPTVWORLDDE009", "com_380")) 
                list.append(("  IPTVWORLDDE010", "com_381"))
                list.append(("  IPTVWORLDDE011", "com_382"))
                list.append(("  IPTVWORLDDE012", "com_383"))
                list.append(("  IPTVWORLDDE013", "com_384"))  
                list.append(("  IPTVWORLDDE014", "com_385"))  
                list.append(("  IPTVWORLDDE015", "com_386"))
                list.append(("  IPTVWORLDDE016", "com_387"))               
                list.append(("  ***** NEDERLAND *****  ", "com_***")) 
                list.append(("  IPTVWORLDNE001", "com_388"))
                list.append(("  IPTVWORLDNE002", "com_389"))
                list.append(("  IPTVWORLDNE003", "com_390"))
                list.append(("  IPTVWORLDNE004", "com_391"))  
                list.append(("  IPTVWORLDNE005", "com_392"))  
                list.append(("  IPTVWORLDNE006", "com_393"))
                list.append(("  IPTVWORLDNE007", "com_394"))  
                list.append(("  IPTVWORLDNE008", "com_395"))
                list.append(("  IPTVWORLDNE009", "com_396")) 
                list.append(("  IPTVWORLDNE010", "com_397"))
                list.append(("  IPTVWORLDNE011", "com_398"))
                list.append(("  IPTVWORLDNE012", "com_399"))
                list.append(("  IPTVWORLDNE013", "com_400"))  
                list.append(("  IPTVWORLDNE014", "com_401"))  
                list.append(("  IPTVWORLDNE015", "com_402"))
                list.append(("  IPTVWORLDNE016", "com_403")) 
                list.append(("  IPTVWORLDNE017", "com_404"))                                                                                                 
                list.append(("  ***** TURKE *****  ", "com_***"))  
                list.append(("  IPTVWORLDTR001", "com_405")) 
                list.append(("  IPTVWORLDTR002", "com_406"))      
                list.append(("  IPTVWORLDTR003", "com_407"))
                list.append(("  IPTVWORLDTR004", "com_408"))  
                list.append(("  IPTVWORLDTR004", "com_409"))
                list.append(("  IPTVWORLDTR006", "com_410"))
                list.append(("  IPTVWORLDTR007", "com_411"))    
                list.append(("  IPTVWORLDTR008", "com_412"))
                list.append(("  IPTVWORLDTR009", "com_413")) 
                list.append(("  IPTVWORLDTR010", "com_414"))
                list.append(("  IPTVWORLDTR011", "com_415"))             
                list.append(("  IPTVWORLDTR012", "com_416"))                 
                list.append(("  ***** ALBANIA *****  ", "com_***"))  
                list.append(("  IPTVWORLDAL001", "com_417"))          
                list.append(("  IPTVWORLDAL002", "com_418"))
                list.append(("  IPTVWORLDAL003", "com_419"))
                list.append(("  IPTVWORLDAL004", "com_420"))
                list.append(("  IPTVWORLDAL005", "com_421"))  
                list.append(("  IPTVWORLDAL006", "com_422"))
                list.append(("  IPTVWORLDAL007", "com_423"))
                list.append(("  IPTVWORLDAL008", "com_424"))                              
                list.append(("  IPTVWORLDAL009", "com_425"))            
                list.append(("  IPTVWORLDAL010", "com_426"))
                list.append(("  IPTVWORLDAL011", "com_427"))                    
                list.append(("  IPTVWORLDAL012", "com_428"))              
                list.append(("  ***** ITALIA *****  ", "com_***"))  
                list.append(("  IPTVWORLDIT001", "com_429"))
                list.append(("  IPTVWORLDIT002", "com_430"))
                list.append(("  IPTVWORLDIT003", "com_431"))
                list.append(("  IPTVWORLDIT004", "com_432"))
                list.append(("  IPTVWORLDIT005", "com_433"))                    
                list.append(("  IPTVWORLDIT006", "com_434"))
                list.append(("  IPTVWORLDIT007", "com_435"))
                list.append(("  IPTVWORLDIT008", "com_436"))
                list.append(("  IPTVWORLDIT009", "com_437"))
                list.append(("  IPTVWORLDIT010", "com_438"))
                list.append(("  IPTVWORLDIT011", "com_439"))
                list.append(("  IPTVWORLDIT012", "com_440"))
                list.append(("  IPTVWORLDIT013", "com_441"))    
                list.append(("  ***** ENGLAND *****  ", "com_***"))     
                list.append(("  IPTVWORLDUK001", "com_442"))
                list.append(("  IPTVWORLDUK002", "com_443"))
                list.append(("  IPTVWORLDUK003", "com_444"))  
                list.append(("  IPTVWORLDUK004", "com_445"))  
                list.append(("  IPTVWORLDUK005", "com_446"))
                list.append(("  IPTVWORLDUK006", "com_447"))  
                list.append(("  IPTVWORLDUK007", "com_448"))
                list.append(("  IPTVWORLDUK008", "com_449"))                  
                list.append(("  IPTVWORLDUK009", "com_450"))
                list.append(("  IPTVWORLDUK010", "com_451"))
                list.append(("  IPTVWORLDUK011", "com_452"))
                list.append(("  IPTVWORLDUK012", "com_453"))
                list.append(("  IPTVWORLDUK013", "com_454"))
                list.append(("  IPTVWORLDUK014", "com_455"))  
                list.append(("  IPTVWORLDUK015", "com_456"))  
                list.append(("  IPTVWORLDUK016", "com_457"))
                list.append(("  IPTVWORLDUK017", "com_458"))  
                list.append(("  IPTVWORLDUK018", "com_459"))
                list.append(("  ***** ESPANIA *****  ", "com_***"))  
                list.append(("  IPTVWORLDES001", "com_460")) 
                list.append(("  IPTVWORLDES002", "com_461"))
                list.append(("  IPTVWORLDES003", "com_462"))
                list.append(("  IPTVWORLDES004", "com_463"))
                list.append(("  IPTVWORLDES005", "com_464"))
                list.append(("  IPTVWORLDES006", "com_465"))  
                list.append(("  IPTVWORLDES007", "com_466"))  
                list.append(("  IPTVWORLDES008", "com_467"))
                list.append(("  IPTVWORLDES009", "com_468"))  
                list.append(("  IPTVWORLDES010", "com_469"))
                list.append(("  IPTVWORLDES011", "com_470")) 
                list.append(("  IPTVWORLDES012", "com_471"))
                list.append(("  IPTVWORLDES013", "com_472"))
                list.append(("  IPTVWORLDES014", "com_473"))
                list.append(("  IPTVWORLDES015", "com_474"))
                list.append(("  IPTVWORLDES016", "com_475"))  
                list.append(("  IPTVWORLDES017", "com_476"))  
                list.append(("  IPTVWORLDES018", "com_477"))
                list.append(("  IPTVWORLDES019", "com_478"))  
                list.append(("  IPTVWORLDES020", "com_479"))
                list.append(("  IPTVWORLDES021", "com_480"))                             
                list.append(("  IPTVWORLDPO022", "com_481"))
                list.append(("  IPTVWORLDPO023", "com_482"))
                list.append(("  ***** PORTUGAL *****  ", "com_***")) 
                list.append(("  IPTVWORLDPO001", "com_483"))
                list.append(("  IPTVWORLDPO002", "com_484"))
                list.append(("  IPTVWORLDPO003", "com_485"))  
                list.append(("  IPTVWORLDPO004", "com_486"))  
                list.append(("  IPTVWORLDPO005", "com_487"))
                list.append(("  IPTVWORLDPO006", "com_488"))  
                list.append(("  IPTVWORLDPO007", "com_489"))
                list.append(("  IPTVWORLDPO008", "com_490")) 
                list.append(("  IPTVWORLDPO009", "com_491"))
                list.append(("  IPTVWORLDPO010", "com_492"))
                list.append(("  IPTVWORLDPO011", "com_493"))
                list.append(("  IPTVWORLDPO012", "com_494"))
                list.append(("  IPTVWORLDPO013", "com_495"))  
                list.append(("  IPTVWORLDPO014", "com_496"))  
                list.append(("  IPTVWORLDPO015", "com_497"))
                list.append(("  IPTVWORLDPO016", "com_498"))  
                list.append(("  IPTVWORLDPO017", "com_499"))
                list.append(("  IPTVWORLDPO018", "com_500"))  
                list.append(("  ***** ROMANIA *****  ", "com_***"))
                list.append(("  IPTVWORLDRO001", "com_501"))            
                list.append(("  IPTVWORLDRO002", "com_502"))  
                list.append(("  IPTVWORLDRO003", "com_503"))
                list.append(("  IPTVWORLDRO004", "com_504")) 
                list.append(("  IPTVWORLDRO005", "com_505"))                                                                                                 
                list.append(("  IPTVWORLDRO006", "com_506")) 
                list.append(("  IPTVWORLDRO007", "com_507"))      
                list.append(("  IPTVWORLDRO008", "com_508"))
                list.append(("  IPTVWORLDRO009", "com_509"))  
                list.append(("  IPTVWORLDRO010", "com_510"))
                list.append(("  IPTVWORLDRO011", "com_511"))
                list.append(("  IPTVWORLDRO012", "com_512"))    
                list.append(("  IPTVWORLDRO013", "com_513"))
                list.append(("  IPTVWORLDRO014", "com_514")) 
                list.append(("  ***** BULGARIA *****  ", "com_***"))  
                list.append(("  IPTVWORLDBU001", "com_515"))        
                list.append(("  IPTVWORLDBU001", "com_516"))                  
                list.append(("  IPTVWORLDBU003", "com_517"))          
                list.append(("  IPTVWORLDBU004", "com_518"))
                list.append(("  IPTVWORLDBU005", "com_519"))
                list.append(("  IPTVWORLDBU006", "com_520"))
                list.append(("  IPTVWORLDBU007", "com_521"))  
                list.append(("  IPTVWORLDBU008", "com_522"))
                list.append(("  IPTVWORLDBU009", "com_523"))
                list.append(("  IPTVWORLDBU010", "com_524"))                              
                list.append(("  IPTVWORLDBU011", "com_525"))            
                list.append(("  IPTVWORLDBU012", "com_526"))
                list.append(("  IPTVWORLDBU013", "com_527"))                    
                list.append(("  IPTVWORLDBU014", "com_528"))              
                list.append(("  IPTVWORLDBU015", "com_529"))
                list.append(("  IPTVWORLDBU016", "com_530"))
                list.append(("  IPTVWORLDBU017", "com_531"))
                list.append(("  IPTVWORLDBU018", "com_532"))
                list.append(("  IPTVWORLDBU019", "com_533"))                    
                list.append(("  IPTVWORLDBU020", "com_534"))
                list.append(("  IPTVWORLDBU021", "com_535"))
                list.append(("  IPTVWORLDBU022", "com_536"))
                list.append(("  IPTVWORLDBU023", "com_537"))
                list.append(("  IPTVWORLDBU024", "com_538"))
                list.append(("  IPTVWORLDBU025", "com_539"))
                list.append(("  IPTVWORLDBU026", "com_540"))
                list.append(("  IPTVWORLDBU027", "com_541"))    
                list.append(("  ***** GREECE *****  ", "com_***"))      
                list.append(("  IPTVWORLDGR001", "com_542"))
                list.append(("  IPTVWORLDGR002", "com_543"))
                list.append(("  IPTVWORLDGR003", "com_544"))  
                list.append(("  IPTVWORLDGR004", "com_545"))  
                list.append(("  IPTVWORLDGR005", "com_546"))
                list.append(("  IPTVWORLDGR006", "com_547"))  
                list.append(("  IPTVWORLDGR007", "com_548"))
                list.append(("  IPTVWORLDGR008", "com_549"))                  
                list.append(("  IPTVWORLDGR009", "com_550"))
                list.append(("  IPTVWORLDGR010", "com_551"))
                list.append(("  ***** SWEDEN *****  ", "com_***"))  
                list.append(("  IPTVWORLDSW001", "com_552"))
                list.append(("  IPTVWORLDSW002", "com_553"))
                list.append(("  IPTVWORLDSW003", "com_554"))
                list.append(("  IPTVWORLDSW004", "com_555"))  
                list.append(("  IPTVWORLDSW005", "com_556"))  
                list.append(("  IPTVWORLDSW006", "com_557"))
                list.append(("  IPTVWORLDSW007", "com_558"))  
                list.append(("  IPTVWORLDSW008", "com_559"))
                list.append(("  ***** YUGOSLAVIA *****  ", "com_***"))  
                list.append(("  IPTVWORLDYU001", "com_560")) 
                list.append(("  IPTVWORLDYU002", "com_561"))
                list.append(("  IPTVWORLDYU003", "com_562"))
                list.append(("  IPTVWORLDYU004", "com_563"))
                list.append(("  IPTVWORLDYU005", "com_564"))
                list.append(("  IPTVWORLDYU006", "com_565"))  
                list.append(("  IPTVWORLDYU007", "com_566"))  
                list.append(("  IPTVWORLDYU008", "com_567"))
                list.append(("  IPTVWORLDYU009", "com_568"))  
                list.append(("  IPTVWORLDYU010", "com_569"))
                list.append(("  IPTVWORLDYU011", "com_570")) 
                list.append(("  IPTVWORLDYU012", "com_571"))
                list.append(("  IPTVWORLDYU013", "com_572"))
                list.append(("  IPTVWORLDYU014", "com_573"))
                list.append(("  IPTVWORLDYU015", "com_574"))
                list.append(("  IPTVWORLDYU019", "com_575")) 
                list.append(("  IPTVWORLDYU020", "com_576"))
                list.append(("  IPTVWORLDYU021", "com_577"))
                list.append(("  IPTVWORLDYU022", "com_578"))
                list.append(("  IPTVWORLDYU023", "com_579"))
                list.append(("  IPTVWORLDYU024", "com_580"))  
                list.append(("  IPTVWORLDYU025", "com_581"))  
                list.append(("  IPTVWORLDYU026", "com_582"))
                list.append(("  IPTVWORLDYU027", "com_583"))  
                list.append(("  IPTVWORLDYU028", "com_584"))
                list.append(("  IPTVWORLDYU029", "com_585")) 
                list.append(("  IPTVWORLDYU030", "com_586"))
                list.append(("  IPTVWORLDYU031", "com_587"))
                list.append(("  IPTVWORLDYU032", "com_588"))
                list.append(("  IPTVWORLDYU033", "com_589"))
                list.append(("  IPTVWORLDYU034", "com_590")) 
                list.append(("  IPTVWORLDYU035", "com_591"))
                list.append(("  IPTVWORLDYU036", "com_592"))
                list.append(("  ***** CZECHIA *****  ", "com_***"))  
                list.append(("  IPTVWORLDCZ001", "com_593"))
                list.append(("  IPTVWORLDCZ002", "com_594"))
                list.append(("  IPTVWORLDCZ003", "com_595"))
                list.append(("  IPTVWORLDCZ004", "com_596"))  
                list.append(("  IPTVWORLDCZ005", "com_597")) 
                list.append(("  ***** CANADA *****  ", "com_***"))  
                list.append(("  IPTVWORLDCA001", "com_598"))
                list.append(("  IPTVWORLDCA002", "com_599"))
                list.append(("  IPTVWORLDCA003", "com_600"))
                list.append(("  IPTVWORLDCA004", "com_601"))  
                list.append(("  IPTVWORLDCA005", "com_602"))                 
                list.append(("  ***** BRAZIL *****  ", "com_***"))                  
                list.append(("  IPTVWORLDBR001", "com_603"))
                list.append(("  IPTVWORLDBR002", "com_604"))  
                list.append(("  IPTVWORLDBR003", "com_605"))
                list.append(("  IPTVWORLDBR004", "com_606"))
                list.append(("  IPTVWORLDBR005", "com_607"))
                list.append(("  IPTVWORLDBR006", "com_608"))  
                list.append(("  IPTVWORLDBR007", "com_609"))  
                list.append(("  IPTVWORLDBR008", "com_610"))
                list.append(("  IPTVWORLDBR009", "com_611"))  
                list.append(("  IPTVWORLDBR010", "com_612"))
                list.append(("  IPTVWORLDBR011", "com_613")) 
                list.append(("  IPTVWORLDBR012", "com_614"))
                list.append(("  IPTVWORLDBR013", "com_615"))
                list.append(("  IPTVWORLDBR014", "com_616"))
                list.append((_("Exit"), "exit"))
                Screen.__init__(self, session)
                self['icon3'] = Pixmap()                
                #self['icon'] = Pixmap() 
                self['icon2'] = Pixmap() 
                self["go"] = Label()    
                #self["goto"] = Label()         
                self["prombt"] = Label()
                self["myRedBtn"] = Label(_("Cancel"))
                self["myGreenBtn"] = Label(_("IPTV"))
                #self["myYellowBtn"] = Label(_("restart"))
                #self["myBlueBtn"] = Label(_("Preview"))
                self.cmdlist = []
                self.onChangedEntry = []
                self.initialservice = session.nav.getCurrentlyPlayingServiceReference()
### Edit By RAED To DreamOS
                #self.timer = eTimer()
                #try:
                #       self.timer.callback.append()
                #except:
                #       self.timer_conn = self.timer.timeout.connect()
                #self.timer.start(2000, True)           
### End EDit
                self["myMenu"] = MenuList(list)
                self["myActionMap"] = ActionMap(["SetupActions"],
                {
                    "0": self.AUTOUPD,

                    "green": self.IPTV,
                        #"yellow": self.goto,
                        #"blue": self.gotoa,
                        "red": self.close,
                        "cancel": self.close,
                        "ok": self.go,
                        "cancel": self.cancel
                }, -1)
                self.onLayoutFinish.append(self.layoutFinished)

        def layoutFinished(self):
                self.setTitle("IPTV WORLD SPORT MOVIES        CHANNELS")

        def go(self):
                returnValue = self["myMenu"].l.getCurrentSelection()[1]
                if returnValue != None:         
                        if returnValue =="com_1":
                                cmdlist = []
### EDit By RAED To DreamOS OE2.5/2.6
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia601501.us.archive.org/12/items/freeiptv001/IPTVWORLD001.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='Free IPTVFree001', cmdlist=cmdlist, finishedCallback=None)
                        elif returnValue =="com_2":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia601501.us.archive.org/12/items/freeiptv001/IPTVWORLD002.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='Free IPTVFree002', cmdlist=cmdlist, finishedCallback=None)
                        elif returnValue =="com_3":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia601501.us.archive.org/12/items/freeiptv001/IPTVWORLD003.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='Free IPTVFree003', cmdlist=cmdlist, finishedCallback=None)
                        elif returnValue =="com_4":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'") 
                                cmdlist.append("%s https://ia601501.us.archive.org/12/items/freeiptv001/IPTVWORLD004.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='Free IPTVFree004', cmdlist=cmdlist, finishedCallback=None)
                        elif returnValue =="com_5":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia601501.us.archive.org/12/items/freeiptv001/IPTVWORLD005.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='Free IPTVFree005', cmdlist=cmdlist, finishedCallback=None)
                        elif returnValue =="com_6":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia601501.us.archive.org/12/items/freeiptv001/IPTVWORLD006.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='Free IPTVFree006', cmdlist=cmdlist, finishedCallback=None)
                        elif returnValue =="com_7":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia601501.us.archive.org/12/items/freeiptv001/IPTVWORLD007.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='Free IPTVFree007', cmdlist=cmdlist, finishedCallback=None)
                        elif returnValue =="com_8":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")    
                                cmdlist.append("%s https://ia601501.us.archive.org/12/items/freeiptv001/IPTVWORLD008.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='Free IPTVFree008', cmdlist=cmdlist, finishedCallback=None)
                        elif returnValue =="com_9":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia601501.us.archive.org/12/items/freeiptv001/IPTVWORLD009.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='Free IPTVFree009', cmdlist=cmdlist, finishedCallback=None)
                        elif returnValue =="com_10":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia601501.us.archive.org/12/items/freeiptv001/IPTVWORLD010.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='Free IPTVFree010', cmdlist=cmdlist, finishedCallback=None)
                        elif returnValue =="com_11":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia601501.us.archive.org/12/items/freeiptv001/IPTVWORLD011.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='Free IPTVFree011', cmdlist=cmdlist, finishedCallback=None)
                        elif returnValue =="com_12":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia601501.us.archive.org/12/items/freeiptv001/IPTVWORLD012.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='Free IPTVFree012', cmdlist=cmdlist, finishedCallback=None)
                        elif returnValue =="com_13":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia601501.us.archive.org/12/items/freeiptv001/IPTVWORLD013.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='Free IPTVFree013', cmdlist=cmdlist, finishedCallback=None)
                        elif returnValue =="com_14":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia601501.us.archive.org/12/items/freeiptv001/IPTVWORLD014.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='Free IPTVFree014', cmdlist=cmdlist, finishedCallback=None)
                        elif returnValue =="com_15":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia601501.us.archive.org/12/items/freeiptv001/IPTVWORLD015.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='Free IPTVFree015', cmdlist=cmdlist, finishedCallback=None)
                        elif returnValue =="com_16":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia601501.us.archive.org/12/items/freeiptv001/IPTVWORLD016.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='Free IPTVFree016', cmdlist=cmdlist, finishedCallback=None)
                        elif returnValue =="com_17":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia601501.us.archive.org/12/items/freeiptv001/IPTVWORLD017.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='Free IPTVFree017', cmdlist=cmdlist, finishedCallback=None)
                        elif returnValue =="com_18":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia601501.us.archive.org/12/items/freeiptv001/IPTVWORLD018.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='Free IPTVFree018', cmdlist=cmdlist, finishedCallback=None)
                        elif returnValue =="com_19":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia601501.us.archive.org/12/items/freeiptv001/IPTVWORLD019.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='Free IPTVFree019', cmdlist=cmdlist, finishedCallback=None)
                        elif returnValue =="com_20":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia601501.us.archive.org/12/items/freeiptv001/IPTVWORLD020.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='Free IPTVFree020', cmdlist=cmdlist, finishedCallback=None)
                        elif returnValue =="com_21":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia601501.us.archive.org/12/items/freeiptv001/IPTVWORLD021.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='Free IPTVFree021', cmdlist=cmdlist, finishedCallback=None)
                        elif returnValue =="com_22":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia601501.us.archive.org/12/items/freeiptv001/IPTVWORLD022.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='Free IPTVFree022', cmdlist=cmdlist, finishedCallback=None)
                        elif returnValue =="com_23":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia601501.us.archive.org/12/items/freeiptv001/IPTVWORLD023.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='Free IPTVFree023', cmdlist=cmdlist, finishedCallback=None)
                        elif returnValue =="com_24":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia601501.us.archive.org/12/items/freeiptv001/IPTVWORLD024.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='Free IPTVFree024', cmdlist=cmdlist, finishedCallback=None)
                        elif returnValue =="com_25":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia601501.us.archive.org/12/items/freeiptv001/IPTVWORLD025.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='Free IPTVFree025', cmdlist=cmdlist, finishedCallback=None)
                        elif returnValue =="com_26":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia601501.us.archive.org/12/items/freeiptv001/IPTVWORLD026.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='Free IPTVFree026', cmdlist=cmdlist, finishedCallback=None)
                        elif returnValue =="com_27":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia601501.us.archive.org/12/items/freeiptv001/IPTVWORLD027.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='Free IPTVFree027', cmdlist=cmdlist, finishedCallback=None)
                        elif returnValue =="com_28":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia601501.us.archive.org/12/items/freeiptv001/IPTVWORLD028.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='Free IPTVFree028', cmdlist=cmdlist, finishedCallback=None)
                        elif returnValue =="com_29":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia601501.us.archive.org/12/items/freeiptv001/IPTVWORLD029.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='Free IPTVFree029', cmdlist=cmdlist, finishedCallback=None)
                        elif returnValue =="com_30":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia601501.us.archive.org/12/items/freeiptv001/IPTVWORLD030.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='Free IPTVFree030', cmdlist=cmdlist, finishedCallback=None)
                        elif returnValue =="com_31":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia601501.us.archive.org/12/items/freeiptv001/IPTVWORLD031.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='Free IPTVFree031', cmdlist=cmdlist, finishedCallback=None)
                        elif returnValue =="com_32":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia601501.us.archive.org/12/items/freeiptv001/IPTVWORLD032.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='Free IPTVFree032', cmdlist=cmdlist, finishedCallback=None)
                        elif returnValue =="com_33":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia601501.us.archive.org/12/items/freeiptv001/IPTVWORLD033.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='Free IPTVFree033', cmdlist=cmdlist, finishedCallback=None)
                        elif returnValue =="com_34":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia601501.us.archive.org/12/items/freeiptv001/IPTVWORLD034.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='Free IPTVFree034', cmdlist=cmdlist, finishedCallback=None)
                        elif returnValue =="com_35":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia601501.us.archive.org/12/items/freeiptv001/IPTVWORLD035.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='Free IPTVFree035', cmdlist=cmdlist, finishedCallback=None)
                        elif returnValue =="com_36":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia601501.us.archive.org/12/items/freeiptv001/IPTVWORLD036.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='Free IPTVFree036', cmdlist=cmdlist, finishedCallback=None)
                        elif returnValue =="com_37":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia601501.us.archive.org/12/items/freeiptv001/IPTVWORLD037.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='Free IPTVFree037', cmdlist=cmdlist, finishedCallback=None)
                        elif returnValue =="com_38":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia601501.us.archive.org/12/items/freeiptv001/IPTVWORLD038.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='Free IPTVFree038', cmdlist=cmdlist, finishedCallback=None)
                        elif returnValue =="com_39":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia601501.us.archive.org/12/items/freeiptv001/IPTVWORLD039.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='Free IPTVFree039', cmdlist=cmdlist, finishedCallback=None)
                        elif returnValue =="com_40":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia601501.us.archive.org/12/items/freeiptv001/IPTVWORLD040.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='Free IPTVFree040', cmdlist=cmdlist, finishedCallback=None)
                        elif returnValue =="com_41":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia601501.us.archive.org/12/items/freeiptv001/IPTVWORLD041.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='Free IPTVFree041', cmdlist=cmdlist, finishedCallback=None)
                        elif returnValue =="com_42":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia601501.us.archive.org/12/items/freeiptv001/IPTVWORLD042.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='Free IPTVFree042', cmdlist=cmdlist, finishedCallback=None)
                        elif returnValue =="com_43":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia601501.us.archive.org/12/items/freeiptv001/IPTVWORLD043.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='Free IPTVFree043', cmdlist=cmdlist, finishedCallback=None)
                        elif returnValue =="com_44":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia601501.us.archive.org/12/items/freeiptv001/IPTVWORLD044.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='Free IPTVFree044', cmdlist=cmdlist, finishedCallback=None)
                        elif returnValue =="com_45":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia601501.us.archive.org/12/items/freeiptv001/IPTVWORLD045.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='Free IPTVFree045', cmdlist=cmdlist, finishedCallback=None)
                        elif returnValue =="com_46":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia601501.us.archive.org/12/items/freeiptv001/IPTVWORLD046.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='Free IPTVFree046', cmdlist=cmdlist, finishedCallback=None)
                        elif returnValue =="com_47":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia601501.us.archive.org/12/items/freeiptv001/IPTVWORLD047.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='Free IPTVFree047', cmdlist=cmdlist, finishedCallback=None)
                        elif returnValue =="com_48":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia601501.us.archive.org/12/items/freeiptv001/IPTVWORLD048.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='Free IPTVFree048', cmdlist=cmdlist, finishedCallback=None)
                        elif returnValue =="com_49":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia601501.us.archive.org/12/items/freeiptv001/IPTVWORLD049.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='Free IPTVFree049', cmdlist=cmdlist, finishedCallback=None)
                        elif returnValue =="com_50":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia601501.us.archive.org/12/items/freeiptv001/IPTVWORLD050.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='Free IPTVFree050', cmdlist=cmdlist, finishedCallback=None)
                        elif returnValue =="com_51":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia601501.us.archive.org/12/items/freeiptv001/IPTVWORLD051.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='Free IPTVFree051', cmdlist=cmdlist, finishedCallback=None)
                        elif returnValue =="com_52":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia601501.us.archive.org/12/items/freeiptv001/IPTVWORLD052.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='Free IPTVFree052', cmdlist=cmdlist, finishedCallback=None)
                        elif returnValue =="com_53":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia601501.us.archive.org/12/items/freeiptv001/IPTVWORLD053.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='Free IPTVFree053', cmdlist=cmdlist, finishedCallback=None)
                        elif returnValue =="com_54":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia601501.us.archive.org/12/items/freeiptv001/IPTVWORLD054.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='Free IPTVFree054', cmdlist=cmdlist, finishedCallback=None)
                        elif returnValue =="com_55":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia601501.us.archive.org/12/items/freeiptv001/IPTVWORLD055.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='Free IPTVFree055', cmdlist=cmdlist, finishedCallback=None)
                        elif returnValue =="com_56":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia601501.us.archive.org/12/items/freeiptv001/IPTVWORLD056.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='Free IPTVFree056', cmdlist=cmdlist, finishedCallback=None)
                        elif returnValue =="com_57":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia601501.us.archive.org/12/items/freeiptv001/IPTVWORLD057.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='Free IPTVFree057', cmdlist=cmdlist, finishedCallback=None)
                        elif returnValue =="com_58":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia601501.us.archive.org/12/items/freeiptv001/IPTVWORLD058.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='Free IPTVFree058', cmdlist=cmdlist, finishedCallback=None)
                        elif returnValue =="com_59":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia601501.us.archive.org/12/items/freeiptv001/IPTVWORLD059.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='Free IPTVFree059', cmdlist=cmdlist, finishedCallback=None)
                        elif returnValue =="com_60":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia601501.us.archive.org/12/items/freeiptv001/IPTVWORLD060.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='Free IPTVFree060', cmdlist=cmdlist, finishedCallback=None)
                        elif returnValue =="com_61":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia601501.us.archive.org/12/items/freeiptv001/IPTVWORLD061.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='Free IPTVFree051', cmdlist=cmdlist, finishedCallback=None)
                        elif returnValue =="com_62":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia601501.us.archive.org/12/items/freeiptv001/IPTVWORLD062.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='Free IPTVFree052', cmdlist=cmdlist, finishedCallback=None)
                        elif returnValue =="com_63":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia601501.us.archive.org/12/items/freeiptv001/IPTVWORLD063.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='Free IPTVFree053', cmdlist=cmdlist, finishedCallback=None)
                        elif returnValue =="com_64":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia601501.us.archive.org/12/items/freeiptv001/IPTVWORLD064.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='Free IPTVFree054', cmdlist=cmdlist, finishedCallback=None)
                        elif returnValue =="com_65":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia601501.us.archive.org/12/items/freeiptv001/IPTVWORLD065.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='Free IPTVFree055', cmdlist=cmdlist, finishedCallback=None)
                        elif returnValue =="com_66":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia601501.us.archive.org/12/items/freeiptv001/IPTVWORLD066.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='Free IPTVFree056', cmdlist=cmdlist, finishedCallback=None)
                        elif returnValue =="com_67":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia601501.us.archive.org/12/items/freeiptv001/IPTVWORLD067.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='Free IPTVFree057', cmdlist=cmdlist, finishedCallback=None)
                        elif returnValue =="com_68":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia601501.us.archive.org/12/items/freeiptv001/IPTVWORLD068.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='Free IPTVFree058', cmdlist=cmdlist, finishedCallback=None)
                        elif returnValue =="com_69":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia601501.us.archive.org/12/items/freeiptv001/IPTVWORLD069.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='Free IPTVFree069', cmdlist=cmdlist, finishedCallback=None)
                        elif returnValue =="com_70":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia601501.us.archive.org/12/items/freeiptv001/IPTVWORLD070.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='Free IPTVFree070', cmdlist=cmdlist, finishedCallback=None)
                        elif returnValue =="com_71":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia601501.us.archive.org/12/items/freeiptv001/IPTVWORLD071.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='Free IPTVFree071', cmdlist=cmdlist, finishedCallback=None)
                        elif returnValue =="com_72":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia601501.us.archive.org/12/items/freeiptv001/IPTVWORLD072.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='Free IPTVFree072', cmdlist=cmdlist, finishedCallback=None)
                        elif returnValue =="com_73":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia601501.us.archive.org/12/items/freeiptv001/IPTVWORLD073.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='Free IPTVFree073', cmdlist=cmdlist, finishedCallback=None)
                        elif returnValue =="com_74":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia601501.us.archive.org/12/items/freeiptv001/IPTVWORLD074.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='Free IPTVFree074', cmdlist=cmdlist, finishedCallback=None)
                        elif returnValue =="com_75":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia601501.us.archive.org/12/items/freeiptv001/IPTVWORLD075.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='Free IPTVFree075', cmdlist=cmdlist, finishedCallback=None)
                        elif returnValue =="com_76":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia601501.us.archive.org/12/items/freeiptv001/IPTVWORLD076.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='Free IPTVFree076', cmdlist=cmdlist, finishedCallback=None)
                        elif returnValue =="com_77":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia601501.us.archive.org/12/items/freeiptv001/IPTVWORLD077.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='Free IPTVFree077', cmdlist=cmdlist, finishedCallback=None)
                        elif returnValue =="com_78":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia601501.us.archive.org/12/items/freeiptv001/IPTVWORLD078.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='Free IPTVFree078', cmdlist=cmdlist, finishedCallback=None)
                        elif returnValue =="com_79":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia601501.us.archive.org/12/items/freeiptv001/IPTVWORLD079.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='Free IPTVFree079', cmdlist=cmdlist, finishedCallback=None)
                        elif returnValue =="com_80":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia601501.us.archive.org/12/items/freeiptv001/IPTVWORLD080.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='Free IPTVFree080', cmdlist=cmdlist, finishedCallback=None)
                        elif returnValue =="com_81":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia601501.us.archive.org/12/items/freeiptv001/IPTVWORLD081.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='Free IPTVFree081', cmdlist=cmdlist, finishedCallback=None)
                        elif returnValue =="com_82":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia601501.us.archive.org/12/items/freeiptv001/IPTVWORLD082.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='Free IPTVFree082', cmdlist=cmdlist, finishedCallback=None)
                        elif returnValue =="com_83":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia601501.us.archive.org/12/items/freeiptv001/IPTVWORLD083.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='Free IPTVFree083', cmdlist=cmdlist, finishedCallback=None)
                        elif returnValue =="com_84":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia601501.us.archive.org/12/items/freeiptv001/IPTVWORLD084.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='Free IPTVFree084', cmdlist=cmdlist, finishedCallback=None)
                        elif returnValue =="com_85":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia601501.us.archive.org/12/items/freeiptv001/IPTVWORLD085.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='Free IPTVFree085', cmdlist=cmdlist, finishedCallback=None)
                        elif returnValue =="com_86":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia601501.us.archive.org/12/items/freeiptv001/IPTVWORLD086.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='Free IPTVFree086', cmdlist=cmdlist, finishedCallback=None)
                        elif returnValue =="com_87":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia601501.us.archive.org/12/items/freeiptv001/IPTVWORLD087.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='Free IPTVFree087', cmdlist=cmdlist, finishedCallback=None)
                        elif returnValue =="com_88":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia601501.us.archive.org/12/items/freeiptv001/IPTVWORLD088.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='Free IPTVFree088', cmdlist=cmdlist, finishedCallback=None)
                        elif returnValue =="com_89":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia601501.us.archive.org/12/items/freeiptv001/IPTVWORLD089.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='Free IPTVFree089', cmdlist=cmdlist, finishedCallback=None)
                        elif returnValue =="com_90":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia601501.us.archive.org/12/items/freeiptv001/IPTVWORLD090.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='Free IPTVFree090', cmdlist=cmdlist, finishedCallback=None)
                        elif returnValue =="com_91":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia601501.us.archive.org/12/items/freeiptv001/IPTVWORLD091.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='Free IPTVFree091', cmdlist=cmdlist, finishedCallback=None)
                        elif returnValue =="com_92":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia601501.us.archive.org/12/items/freeiptv001/IPTVWORLD092.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='Free IPTVFree092', cmdlist=cmdlist, finishedCallback=None)
                        elif returnValue =="com_93":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia601501.us.archive.org/12/items/freeiptv001/IPTVWORLD093.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='Free IPTVFree093', cmdlist=cmdlist, finishedCallback=None)
                        elif returnValue =="com_94":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia601501.us.archive.org/12/items/freeiptv001/IPTVWORLD094.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='Free IPTVFree094', cmdlist=cmdlist, finishedCallback=None)
                        elif returnValue =="com_95":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia601501.us.archive.org/12/items/freeiptv001/IPTVWORLD095.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='Free IPTVFree095', cmdlist=cmdlist, finishedCallback=None)
                        elif returnValue =="com_96":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia601501.us.archive.org/12/items/freeiptv001/IPTVWORLD096.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='Free IPTVFree096', cmdlist=cmdlist, finishedCallback=None)
                        elif returnValue =="com_97":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia601501.us.archive.org/12/items/freeiptv001/IPTVWORLD097.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='Free IPTVFree097', cmdlist=cmdlist, finishedCallback=None)
                        elif returnValue =="com_98":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia601501.us.archive.org/12/items/freeiptv001/IPTVWORLD098.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='Free IPTVFree098', cmdlist=cmdlist, finishedCallback=None)
                        elif returnValue =="com_99":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia601501.us.archive.org/12/items/freeiptv001/IPTVWORLD099.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='Free IPTVFree099', cmdlist=cmdlist, finishedCallback=None)
                        elif returnValue =="com_100":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia601501.us.archive.org/12/items/freeiptv001/IPTVWORLD100.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='Free IPTVFree100', cmdlist=cmdlist, finishedCallback=None)
                        elif returnValue =="com_101":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia601501.us.archive.org/12/items/freeiptv001/SPRORTWORLD001.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='Free IPTVFree001', cmdlist=cmdlist, finishedCallback=None)
                        elif returnValue =="com_102":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia601501.us.archive.org/12/items/freeiptv001/SPRORTWORLD002.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='Free IPTVFree002', cmdlist=cmdlist, finishedCallback=None)
                        elif returnValue =="com_103":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia601501.us.archive.org/12/items/freeiptv001/SPRORTWORLD003.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='Free IPTVFree003', cmdlist=cmdlist, finishedCallback=None)
                        elif returnValue =="com_104":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'") 
                                cmdlist.append("%s https://ia601501.us.archive.org/12/items/freeiptv001/SPRORTWORLD004.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='Free IPTVFree004', cmdlist=cmdlist, finishedCallback=None)
                        elif returnValue =="com_105":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia601501.us.archive.org/12/items/freeiptv001/SPRORTWORLD005.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='Free IPTVFree005', cmdlist=cmdlist, finishedCallback=None)
                        elif returnValue =="com_106":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia601501.us.archive.org/12/items/freeiptv001/SPRORTWORLD006.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='Free IPTVFree006', cmdlist=cmdlist, finishedCallback=None)
                        elif returnValue =="com_107":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia601501.us.archive.org/12/items/freeiptv001/SPRORTWORLD007.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='Free IPTVFree007', cmdlist=cmdlist, finishedCallback=None)
                        elif returnValue =="com_108":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")    
                                cmdlist.append("%s https://ia601501.us.archive.org/12/items/freeiptv001/SPRORTWORLD008.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='Free IPTVFree008', cmdlist=cmdlist, finishedCallback=None)
                        elif returnValue =="com_109":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia601501.us.archive.org/12/items/freeiptv001/SPRORTWORLD009.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='Free IPTVFree009', cmdlist=cmdlist, finishedCallback=None)
                        elif returnValue =="com_110":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia601501.us.archive.org/12/items/freeiptv001/SPRORTWORLD010.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='Free IPTVFree010', cmdlist=cmdlist, finishedCallback=None)
                        elif returnValue =="com_111":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia601501.us.archive.org/12/items/freeiptv001/SPRORTWORLD011.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='Free IPTVFree011', cmdlist=cmdlist, finishedCallback=None)
                        elif returnValue =="com_112":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia601501.us.archive.org/12/items/freeiptv001/SPRORTWORLD012.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='Free IPTVFree012', cmdlist=cmdlist, finishedCallback=None)
                        elif returnValue =="com_113":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia601501.us.archive.org/12/items/freeiptv001/SPRORTWORLD013.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='Free IPTVFree013', cmdlist=cmdlist, finishedCallback=None)
                        elif returnValue =="com_114":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia601501.us.archive.org/12/items/freeiptv001/SPRORTWORLD014.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='Free IPTVFree014', cmdlist=cmdlist, finishedCallback=None)
                        elif returnValue =="com_115":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia601501.us.archive.org/12/items/freeiptv001/SPRORTWORLD015.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='Free IPTVFree015', cmdlist=cmdlist, finishedCallback=None)
                        elif returnValue =="com_116":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia601501.us.archive.org/12/items/freeiptv001/SPRORTWORLD016.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='Free IPTVFree016', cmdlist=cmdlist, finishedCallback=None)
                        elif returnValue =="com_117":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia601501.us.archive.org/12/items/freeiptv001/SPRORTWORLD017.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='Free IPTVFree017', cmdlist=cmdlist, finishedCallback=None)
                        elif returnValue =="com_118":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia601501.us.archive.org/12/items/freeiptv001/SPRORTWORLD018.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='Free IPTVFree018', cmdlist=cmdlist, finishedCallback=None)
                        elif returnValue =="com_119":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia601501.us.archive.org/12/items/freeiptv001/SPRORTWORLD019.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='Free IPTVFree019', cmdlist=cmdlist, finishedCallback=None)
                        elif returnValue =="com_120":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia601501.us.archive.org/12/items/freeiptv001/SPRORTWORLD020.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='Free IPTVFree020', cmdlist=cmdlist, finishedCallback=None)
                        elif returnValue =="com_121":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia601501.us.archive.org/12/items/freeiptv001/SPRORTWORLD021.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='Free IPTVFree021', cmdlist=cmdlist, finishedCallback=None)
                        elif returnValue =="com_122":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia601501.us.archive.org/12/items/freeiptv001/SPRORTWORLD022.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='Free IPTVFree022', cmdlist=cmdlist, finishedCallback=None)
                        elif returnValue =="com_123":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia601501.us.archive.org/12/items/freeiptv001/SPRORTWORLD023.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='Free IPTVFree023', cmdlist=cmdlist, finishedCallback=None)
                        elif returnValue =="com_124":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia601501.us.archive.org/12/items/freeiptv001/SPRORTWORLD024.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='Free IPTVFree024', cmdlist=cmdlist, finishedCallback=None)
                        elif returnValue =="com_125":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia601501.us.archive.org/12/items/freeiptv001/SPRORTWORLD025.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='Free IPTVFree025', cmdlist=cmdlist, finishedCallback=None)
                        elif returnValue =="com_126":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia601501.us.archive.org/12/items/freeiptv001/SPRORTWORLD026.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='Free IPTVFree026', cmdlist=cmdlist, finishedCallback=None)
                        elif returnValue =="com_127":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia601501.us.archive.org/12/items/freeiptv001/SPRORTWORLD027.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='Free IPTVFree027', cmdlist=cmdlist, finishedCallback=None)
                        elif returnValue =="com_128":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia601501.us.archive.org/12/items/freeiptv001/SPRORTWORLD028.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='Free IPTVFree028', cmdlist=cmdlist, finishedCallback=None)
                        elif returnValue =="com_129":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia601501.us.archive.org/12/items/freeiptv001/SPRORTWORLD029.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='Free IPTVFree029', cmdlist=cmdlist, finishedCallback=None)
                        elif returnValue =="com_130":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia601501.us.archive.org/12/items/freeiptv001/SPRORTWORLD030.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='Free IPTVFree030', cmdlist=cmdlist, finishedCallback=None)
                        elif returnValue =="com_131":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia601501.us.archive.org/12/items/freeiptv001/SPRORTWORLD031.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='Free IPTVFree031', cmdlist=cmdlist, finishedCallback=None)
                        elif returnValue =="com_132":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia601501.us.archive.org/12/items/freeiptv001/SPRORTWORLD032.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='Free IPTVFree032', cmdlist=cmdlist, finishedCallback=None)
                        elif returnValue =="com_133":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia601501.us.archive.org/12/items/freeiptv001/SPRORTWORLD033.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='Free IPTVFree033', cmdlist=cmdlist, finishedCallback=None)
                        elif returnValue =="com_134":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia601501.us.archive.org/12/items/freeiptv001/SPRORTWORLD034.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='Free IPTVFree034', cmdlist=cmdlist, finishedCallback=None)
                        elif returnValue =="com_135":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia601501.us.archive.org/12/items/freeiptv001/SPRORTWORLD035.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='Free IPTVFree035', cmdlist=cmdlist, finishedCallback=None)
                        elif returnValue =="com_136":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia601501.us.archive.org/12/items/freeiptv001/SPRORTWORLD036.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='Free IPTVFree036', cmdlist=cmdlist, finishedCallback=None)
                        elif returnValue =="com_137":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia601501.us.archive.org/12/items/freeiptv001/SPRORTWORLD037.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='Free IPTVFree037', cmdlist=cmdlist, finishedCallback=None)
                        elif returnValue =="com_138":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia601501.us.archive.org/12/items/freeiptv001/SPRORTWORLD038.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='Free IPTVFree038', cmdlist=cmdlist, finishedCallback=None)
                        elif returnValue =="com_139":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia601501.us.archive.org/12/items/freeiptv001/SPRORTWORLD039.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='Free IPTVFree039', cmdlist=cmdlist, finishedCallback=None)
                        elif returnValue =="com_140":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia601501.us.archive.org/12/items/freeiptv001/SPRORTWORLD040.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='Free IPTVFree040', cmdlist=cmdlist, finishedCallback=None)
                        elif returnValue =="com_141":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia601501.us.archive.org/12/items/freeiptv001/SPRORTWORLD041.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='Free IPTVFree041', cmdlist=cmdlist, finishedCallback=None)
                        elif returnValue =="com_142":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia601501.us.archive.org/12/items/freeiptv001/SPRORTWORLD042.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='Free IPTVFree042', cmdlist=cmdlist, finishedCallback=None)
                        elif returnValue =="com_143":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia601501.us.archive.org/12/items/freeiptv001/SPRORTWORLD043.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='Free IPTVFree043', cmdlist=cmdlist, finishedCallback=None)
                        elif returnValue =="com_144":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia601501.us.archive.org/12/items/freeiptv001/SPRORTWORLD044.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='Free IPTVFree044', cmdlist=cmdlist, finishedCallback=None)
                        elif returnValue =="com_145":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia601501.us.archive.org/12/items/freeiptv001/SPRORTWORLD045.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='Free IPTVFree045', cmdlist=cmdlist, finishedCallback=None)
                        elif returnValue =="com_146":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia601501.us.archive.org/12/items/freeiptv001/SPRORTWORLD046.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='Free IPTVFree046', cmdlist=cmdlist, finishedCallback=None)
                        elif returnValue =="com_147":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia601501.us.archive.org/12/items/freeiptv001/SPRORTWORLD047.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='Free IPTVFree047', cmdlist=cmdlist, finishedCallback=None)
                        elif returnValue =="com_148":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia601501.us.archive.org/12/items/freeiptv001/SPRORTWORLD048.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='Free IPTVFree048', cmdlist=cmdlist, finishedCallback=None)
                        elif returnValue =="com_149":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia601501.us.archive.org/12/items/freeiptv001/SPRORTWORLD049.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='Free IPTVFree049', cmdlist=cmdlist, finishedCallback=None)
                        elif returnValue =="com_150":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia601501.us.archive.org/12/items/freeiptv001/SPRORTWORLD050.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='Free IPTVFree050', cmdlist=cmdlist, finishedCallback=None)
                        elif returnValue =="com_151":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia601501.us.archive.org/12/items/freeiptv001/SPRORTWORLD051.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='Free IPTVFree051', cmdlist=cmdlist, finishedCallback=None)
                        elif returnValue =="com_152":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia601501.us.archive.org/12/items/freeiptv001/SPRORTWORLD052.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='Free IPTVFree052', cmdlist=cmdlist, finishedCallback=None)
                        elif returnValue =="com_153":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia601501.us.archive.org/12/items/freeiptv001/SPRORTWORLD053.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='Free IPTVFree053', cmdlist=cmdlist, finishedCallback=None)
                        elif returnValue =="com_154":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia601501.us.archive.org/12/items/freeiptv001/SPRORTWORLD054.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='Free IPTVFree054', cmdlist=cmdlist, finishedCallback=None)
                        elif returnValue =="com_155":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia601501.us.archive.org/12/items/freeiptv001/SPRORTWORLD055.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='Free IPTVFree055', cmdlist=cmdlist, finishedCallback=None)
                        elif returnValue =="com_156":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia601501.us.archive.org/12/items/freeiptv001/SPRORTWORLD056.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='Free IPTVFree056', cmdlist=cmdlist, finishedCallback=None)
                        elif returnValue =="com_157":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia601501.us.archive.org/12/items/freeiptv001/SPRORTWORLD057.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='Free IPTVFree057', cmdlist=cmdlist, finishedCallback=None)
                        elif returnValue =="com_158":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia601501.us.archive.org/12/items/freeiptv001/SPRORTWORLD058.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='Free IPTVFree058', cmdlist=cmdlist, finishedCallback=None)
                        elif returnValue =="com_159":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia601501.us.archive.org/12/items/freeiptv001/SPRORTWORLD059.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='Free IPTVFree059', cmdlist=cmdlist, finishedCallback=None)
                        elif returnValue =="com_160":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia601501.us.archive.org/12/items/freeiptv001/SPRORTWORLD060.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='Free IPTVFree060', cmdlist=cmdlist, finishedCallback=None)
                        elif returnValue =="com_161":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia601501.us.archive.org/12/items/freeiptv001/SPRORTWORLD061.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='Free IPTVFree051', cmdlist=cmdlist, finishedCallback=None)
                        elif returnValue =="com_162":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia601501.us.archive.org/12/items/freeiptv001/SPRORTWORLD062.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='Free IPTVFree052', cmdlist=cmdlist, finishedCallback=None)
                        elif returnValue =="com_163":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia601501.us.archive.org/12/items/freeiptv001/SPRORTWORLD063.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='Free IPTVFree053', cmdlist=cmdlist, finishedCallback=None)
                        elif returnValue =="com_164":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia601501.us.archive.org/12/items/freeiptv001/SPRORTWORLD064.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='Free IPTVFree054', cmdlist=cmdlist, finishedCallback=None)
                        elif returnValue =="com_165":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia601501.us.archive.org/12/items/freeiptv001/SPRORTWORLD065.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='Free IPTVFree055', cmdlist=cmdlist, finishedCallback=None)
                        elif returnValue =="com_166":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia601501.us.archive.org/12/items/freeiptv001/SPRORTWORLD066.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='Free IPTVFree056', cmdlist=cmdlist, finishedCallback=None)
                        elif returnValue =="com_167":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia601501.us.archive.org/12/items/freeiptv001/SPRORTWORLD067.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='Free IPTVFree057', cmdlist=cmdlist, finishedCallback=None)
                        elif returnValue =="com_168":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia601501.us.archive.org/12/items/freeiptv001/SPRORTWORLD068.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='Free IPTVFree058', cmdlist=cmdlist, finishedCallback=None)
                        elif returnValue =="com_169":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia601501.us.archive.org/12/items/freeiptv001/SPRORTWORLD069.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='Free IPTVFree069', cmdlist=cmdlist, finishedCallback=None)
                        elif returnValue =="com_170":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia601501.us.archive.org/12/items/freeiptv001/SPRORTWORLD070.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='Free IPTVFree070', cmdlist=cmdlist, finishedCallback=None)
                        elif returnValue =="com_171":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia601501.us.archive.org/12/items/freeiptv001/SPRORTWORLD071.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='Free IPTVFree071', cmdlist=cmdlist, finishedCallback=None)
                        elif returnValue =="com_172":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia601501.us.archive.org/12/items/freeiptv001/SPRORTWORLD072.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='Free IPTVFree072', cmdlist=cmdlist, finishedCallback=None)
                        elif returnValue =="com_173":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia601501.us.archive.org/12/items/freeiptv001/SPRORTWORLD073.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='Free IPTVFree073', cmdlist=cmdlist, finishedCallback=None)
                        elif returnValue =="com_174":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia601501.us.archive.org/12/items/freeiptv001/SPRORTWORLD074.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='Free IPTVFree074', cmdlist=cmdlist, finishedCallback=None)
                        elif returnValue =="com_175":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia601501.us.archive.org/12/items/freeiptv001/SPRORTWORLD075.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='Free IPTVFree075', cmdlist=cmdlist, finishedCallback=None)
                        elif returnValue =="com_176":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia601501.us.archive.org/12/items/freeiptv001/SPRORTWORLD076.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='Free IPTVFree076', cmdlist=cmdlist, finishedCallback=None)
                        elif returnValue =="com_177":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia601501.us.archive.org/12/items/freeiptv001/SPRORTWORLD077.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='Free IPTVFree077', cmdlist=cmdlist, finishedCallback=None)
                        elif returnValue =="com_178":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia601501.us.archive.org/12/items/freeiptv001/SPRORTWORLD078.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='Free IPTVFree078', cmdlist=cmdlist, finishedCallback=None)
                        elif returnValue =="com_179":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia601501.us.archive.org/12/items/freeiptv001/SPRORTWORLD079.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='Free IPTVFree079', cmdlist=cmdlist, finishedCallback=None)
                        elif returnValue =="com_180":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia601501.us.archive.org/12/items/freeiptv001/SPRORTWORLD080.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='Free IPTVFree080', cmdlist=cmdlist, finishedCallback=None)
                        elif returnValue =="com_181":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia601501.us.archive.org/12/items/freeiptv001/SPRORTWORLD081.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='Free IPTVFree081', cmdlist=cmdlist, finishedCallback=None)
                        elif returnValue =="com_182":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia601501.us.archive.org/12/items/freeiptv001/SPRORTWORLD082.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='Free IPTVFree082', cmdlist=cmdlist, finishedCallback=None)
                        elif returnValue =="com_183":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia601501.us.archive.org/12/items/freeiptv001/SPRORTWORLD083.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='Free IPTVFree083', cmdlist=cmdlist, finishedCallback=None)
                        elif returnValue =="com_184":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia601501.us.archive.org/12/items/freeiptv001/SPRORTWORLD084.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='Free IPTVFree084', cmdlist=cmdlist, finishedCallback=None)
                        elif returnValue =="com_185":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia601501.us.archive.org/12/items/freeiptv001/SPRORTWORLD085.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='Free IPTVFree085', cmdlist=cmdlist, finishedCallback=None)
                        elif returnValue =="com_186":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia601501.us.archive.org/12/items/freeiptv001/SPRORTWORLD086.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='Free IPTVFree086', cmdlist=cmdlist, finishedCallback=None)
                        elif returnValue =="com_187":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia601501.us.archive.org/12/items/freeiptv001/SPRORTWORLD087.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='Free IPTVFree087', cmdlist=cmdlist, finishedCallback=None)
                        elif returnValue =="com_188":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia601501.us.archive.org/12/items/freeiptv001/SPRORTWORLD088.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='Free IPTVFree088', cmdlist=cmdlist, finishedCallback=None)
                        elif returnValue =="com_189":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia601501.us.archive.org/12/items/freeiptv001/SPRORTWORLD089.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='Free IPTVFree089', cmdlist=cmdlist, finishedCallback=None)
                        elif returnValue =="com_190":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia601501.us.archive.org/12/items/freeiptv001/SPRORTWORLD090.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='Free IPTVFree090', cmdlist=cmdlist, finishedCallback=None)
                        elif returnValue =="com_191":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia601501.us.archive.org/12/items/freeiptv001/SPRORTWORLD091.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='Free IPTVFree091', cmdlist=cmdlist, finishedCallback=None)
                        elif returnValue =="com_192":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia601501.us.archive.org/12/items/freeiptv001/SPRORTWORLD092.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='Free IPTVFree092', cmdlist=cmdlist, finishedCallback=None)
                        elif returnValue =="com_193":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia601501.us.archive.org/12/items/freeiptv001/SPRORTWORLD093.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='Free IPTVFree093', cmdlist=cmdlist, finishedCallback=None)
                        elif returnValue =="com_194":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia601501.us.archive.org/12/items/freeiptv001/SPRORTWORLD094.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='Free IPTVFree094', cmdlist=cmdlist, finishedCallback=None)
                        elif returnValue =="com_195":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia601501.us.archive.org/12/items/freeiptv001/SPRORTWORLD095.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='Free IPTVFree095', cmdlist=cmdlist, finishedCallback=None)
                        elif returnValue =="com_196":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia601501.us.archive.org/12/items/freeiptv001/SPRORTWORLD096.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='Free IPTVFree096', cmdlist=cmdlist, finishedCallback=None)
                        elif returnValue =="com_197":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia601501.us.archive.org/12/items/freeiptv001/SPRORTWORLD097.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='Free IPTVFree097', cmdlist=cmdlist, finishedCallback=None)
                        elif returnValue =="com_198":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia601501.us.archive.org/12/items/freeiptv001/SPRORTWORLD098.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='Free IPTVFree098', cmdlist=cmdlist, finishedCallback=None)
                        elif returnValue =="com_199":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia601501.us.archive.org/12/items/freeiptv001/SPRORTWORLD099.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='Free IPTVFree099', cmdlist=cmdlist, finishedCallback=None)
                        elif returnValue =="com_200":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia601501.us.archive.org/12/items/freeiptv001/SPRORTWORLD100.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='Free IPTVFree100', cmdlist=cmdlist, finishedCallback=None)
                        elif returnValue =="com_201":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia801508.us.archive.org/24/items/iptvworld_20191114/IPTVWORLDAR001.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='Free IPTVFree001', cmdlist=cmdlist, finishedCallback=None)
                        elif returnValue =="com_202":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia801508.us.archive.org/24/items/iptvworld_20191114/IPTVWORLDAR002.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='Free IPTVFree002', cmdlist=cmdlist, finishedCallback=None)
                        elif returnValue =="com_203":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia801508.us.archive.org/24/items/iptvworld_20191114/IPTVWORLDAR003.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='Free IPTVFree003', cmdlist=cmdlist, finishedCallback=None)
                        elif returnValue =="com_204":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'") 
                                cmdlist.append("%s https://ia801508.us.archive.org/24/items/iptvworld_20191114/IPTVWORLDAR004.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='Free IPTVFree004', cmdlist=cmdlist, finishedCallback=None)
                        elif returnValue =="com_205":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia801508.us.archive.org/24/items/iptvworld_20191114/IPTVWORLDAR005.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='Free IPTVFree005', cmdlist=cmdlist, finishedCallback=None)
                        elif returnValue =="com_206":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia801508.us.archive.org/24/items/iptvworld_20191114/IPTVWORLDAR006.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='Free IPTVFree006', cmdlist=cmdlist, finishedCallback=None)
                        elif returnValue =="com_207":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia801508.us.archive.org/24/items/iptvworld_20191114/IPTVWORLDAR007.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='Free IPTVFree007', cmdlist=cmdlist, finishedCallback=None)
                        elif returnValue =="com_208":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")    
                                cmdlist.append("%s https://ia801508.us.archive.org/24/items/iptvworld_20191114/IPTVWORLDAR008.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='Free IPTVFree008', cmdlist=cmdlist, finishedCallback=None)
                        elif returnValue =="com_209":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia801508.us.archive.org/24/items/iptvworld_20191114/IPTVWORLDAR009.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='Free IPTVFree009', cmdlist=cmdlist, finishedCallback=None)
                        elif returnValue =="com_210":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia801508.us.archive.org/24/items/iptvworld_20191114/IPTVWORLDAR010.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='Free IPTVFree010', cmdlist=cmdlist, finishedCallback=None)
                        elif returnValue =="com_211":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia801508.us.archive.org/24/items/iptvworld_20191114/IPTVWORLDAR011.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='Free IPTVFree011', cmdlist=cmdlist, finishedCallback=None)
                        elif returnValue =="com_212":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia801508.us.archive.org/24/items/iptvworld_20191114/IPTVWORLDAR012.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='Free IPTVFree012', cmdlist=cmdlist, finishedCallback=None)
                        elif returnValue =="com_213":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia801508.us.archive.org/24/items/iptvworld_20191114/IPTVWORLDAR013.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='Free IPTVFree013', cmdlist=cmdlist, finishedCallback=None)
                        elif returnValue =="com_214":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia801508.us.archive.org/24/items/iptvworld_20191114/IPTVWORLDAR014.shh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='Free IPTVFree014', cmdlist=cmdlist, finishedCallback=None)
                        elif returnValue =="com_215":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia801508.us.archive.org/24/items/iptvworld_20191114/IPTVWORLDAR015.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='Free IPTVFree015', cmdlist=cmdlist, finishedCallback=None)
                        elif returnValue =="com_216":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia801508.us.archive.org/24/items/iptvworld_20191114/IPTVWORLDAR016.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='Free IPTVFree016', cmdlist=cmdlist, finishedCallback=None)
                        elif returnValue =="com_217":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia801508.us.archive.org/24/items/iptvworld_20191114/IPTVWORLDAR017.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='Free IPTVFree017', cmdlist=cmdlist, finishedCallback=None)
                        elif returnValue =="com_218":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia801508.us.archive.org/24/items/iptvworld_20191114/IPTVWORLDAR018.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='Free IPTVFree018', cmdlist=cmdlist, finishedCallback=None)
                        elif returnValue =="com_219":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia801508.us.archive.org/24/items/iptvworld_20191114/IPTVWORLDAR019.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='Free IPTVFree019', cmdlist=cmdlist, finishedCallback=None)
                        elif returnValue =="com_220":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia801508.us.archive.org/24/items/iptvworld_20191114/IPTVWORLDAR020.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='Free IPTVFree020', cmdlist=cmdlist, finishedCallback=None)
                        elif returnValue =="com_221":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia801508.us.archive.org/24/items/iptvworld_20191114/IPTVWORLDAR021.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='Free IPTVFree021', cmdlist=cmdlist, finishedCallback=None)
                        elif returnValue =="com_222":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia801508.us.archive.org/24/items/iptvworld_20191114/IPTVWORLDAR022.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='Free IPTVFree022', cmdlist=cmdlist, finishedCallback=None)
                        elif returnValue =="com_223":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia801508.us.archive.org/24/items/iptvworld_20191114/IPTVWORLDAR023.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='Free IPTVFree023', cmdlist=cmdlist, finishedCallback=None)
                        elif returnValue =="com_224":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia801508.us.archive.org/24/items/iptvworld_20191114/IPTVWORLDAR024.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='Free IPTVFree024', cmdlist=cmdlist, finishedCallback=None)
                        elif returnValue =="com_225":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia801508.us.archive.org/24/items/iptvworld_20191114/IPTVWORLDAR025.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='Free IPTVFree025', cmdlist=cmdlist, finishedCallback=None)
                        elif returnValue =="com_226":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia801508.us.archive.org/24/items/iptvworld_20191114/IPTVWORLDAR026.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='Free IPTVFree026', cmdlist=cmdlist, finishedCallback=None)
                        elif returnValue =="com_227":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia801508.us.archive.org/24/items/iptvworld_20191114/IPTVWORLDAR027.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='Free IPTVFree027', cmdlist=cmdlist, finishedCallback=None)
                        elif returnValue =="com_228":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia801508.us.archive.org/24/items/iptvworld_20191114/IPTVWORLDAR028.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='Free IPTVFree028', cmdlist=cmdlist, finishedCallback=None)
                        elif returnValue =="com_229":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia801508.us.archive.org/24/items/iptvworld_20191114/IPTVWORLDAR029.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='Free IPTVFree029', cmdlist=cmdlist, finishedCallback=None)
                        elif returnValue =="com_230":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia801508.us.archive.org/24/items/iptvworld_20191114/IPTVWORLDAR030.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='Free IPTVFree030', cmdlist=cmdlist, finishedCallback=None)
                        elif returnValue =="com_231":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia801508.us.archive.org/24/items/iptvworld_20191114/IPTVWORLDAR031.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='Free IPTVFree031', cmdlist=cmdlist, finishedCallback=None)
                        elif returnValue =="com_232":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia801508.us.archive.org/24/items/iptvworld_20191114/IPTVWORLDAR032.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='Free IPTVFree032', cmdlist=cmdlist, finishedCallback=None)
                        elif returnValue =="com_233":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia801508.us.archive.org/24/items/iptvworld_20191114/IPTVWORLDAR033.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='Free IPTVFree033', cmdlist=cmdlist, finishedCallback=None)
                        elif returnValue =="com_234":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia801508.us.archive.org/24/items/iptvworld_20191114/IPTVWORLDAR034.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='Free IPTVFree034', cmdlist=cmdlist, finishedCallback=None)
                        elif returnValue =="com_235":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia801508.us.archive.org/24/items/iptvworld_20191114/IPTVWORLDAR035.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='Free IPTVFree035', cmdlist=cmdlist, finishedCallback=None)
                        elif returnValue =="com_236":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia801508.us.archive.org/24/items/iptvworld_20191114/IPTVWORLDAR036.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='Free IPTVFree036', cmdlist=cmdlist, finishedCallback=None)
                        elif returnValue =="com_237":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia801508.us.archive.org/24/items/iptvworld_20191114/IPTVWORLDAR037.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='Free IPTVFree037', cmdlist=cmdlist, finishedCallback=None)
                        elif returnValue =="com_238":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia801508.us.archive.org/24/items/iptvworld_20191114/IPTVWORLDAR038.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='Free IPTVFree038', cmdlist=cmdlist, finishedCallback=None)
                        elif returnValue =="com_239":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia801508.us.archive.org/24/items/iptvworld_20191114/IPTVWORLDAR039.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='Free IPTVFree039', cmdlist=cmdlist, finishedCallback=None)
                        elif returnValue =="com_240":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia801508.us.archive.org/24/items/iptvworld_20191114/IPTVWORLDAR040.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='Free IPTVFree040', cmdlist=cmdlist, finishedCallback=None)
                        elif returnValue =="com_241":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia801508.us.archive.org/24/items/iptvworld_20191114/IPTVWORLDAR041.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='Free IPTVFree041', cmdlist=cmdlist, finishedCallback=None)
                        elif returnValue =="com_242":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia801508.us.archive.org/24/items/iptvworld_20191114/IPTVWORLDAR042.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='Free IPTVFree042', cmdlist=cmdlist, finishedCallback=None)
                        elif returnValue =="com_243":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia801508.us.archive.org/24/items/iptvworld_20191114/IPTVWORLDAR043.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='Free IPTVFree043', cmdlist=cmdlist, finishedCallback=None)
                        elif returnValue =="com_244":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia801508.us.archive.org/24/items/iptvworld_20191114/IPTVWORLDAR044.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='Free IPTVFree044', cmdlist=cmdlist, finishedCallback=None)
                        elif returnValue =="com_245":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia801508.us.archive.org/24/items/iptvworld_20191114/IPTVWORLDAR045.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='Free IPTVFree045', cmdlist=cmdlist, finishedCallback=None)
                        elif returnValue =="com_246":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia801508.us.archive.org/24/items/iptvworld_20191114/IPTVWORLDAR046.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='Free IPTVFree046', cmdlist=cmdlist, finishedCallback=None)
                        elif returnValue =="com_247":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia801508.us.archive.org/24/items/iptvworld_20191114/IPTVWORLDAR047.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='Free IPTVFree047', cmdlist=cmdlist, finishedCallback=None)
                        elif returnValue =="com_248":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia801508.us.archive.org/24/items/iptvworld_20191114/IPTVWORLDAR048.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='Free IPTVFree048', cmdlist=cmdlist, finishedCallback=None)
                        elif returnValue =="com_249":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia801508.us.archive.org/24/items/iptvworld_20191114/IPTVWORLDAR049.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='Free IPTVFree049', cmdlist=cmdlist, finishedCallback=None)
                        elif returnValue =="com_250":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia801508.us.archive.org/24/items/iptvworld_20191114/IPTVWORLDAR050.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='Free IPTVFree050', cmdlist=cmdlist, finishedCallback=None)
                        elif returnValue =="com_251":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia801508.us.archive.org/24/items/iptvworld_20191114/IPTVWORLDAR051.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='Free IPTVFree051', cmdlist=cmdlist, finishedCallback=None)
                        elif returnValue =="com_252":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia801508.us.archive.org/24/items/iptvworld_20191114/IPTVWORLDAR052.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='Free IPTVFree052', cmdlist=cmdlist, finishedCallback=None)
                        elif returnValue =="com_253":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia801508.us.archive.org/24/items/iptvworld_20191114/IPTVWORLDAR053.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='Free IPTVFree053', cmdlist=cmdlist, finishedCallback=None)
                        elif returnValue =="com_254":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia801508.us.archive.org/24/items/iptvworld_20191114/IPTVWORLDAR054.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='Free IPTVFree054', cmdlist=cmdlist, finishedCallback=None)
                        elif returnValue =="com_255":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia801508.us.archive.org/24/items/iptvworld_20191114/IPTVWORLDAR055.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='Free IPTVFree055', cmdlist=cmdlist, finishedCallback=None)
                        elif returnValue =="com_256":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia801508.us.archive.org/24/items/iptvworld_20191114/IPTVWORLDAR056.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='Free IPTVFree056', cmdlist=cmdlist, finishedCallback=None)
                        elif returnValue =="com_257":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia801508.us.archive.org/24/items/iptvworld_20191114/IPTVWORLDAR057.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='Free IPTVFree057', cmdlist=cmdlist, finishedCallback=None)
                        elif returnValue =="com_258":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia801508.us.archive.org/24/items/iptvworld_20191114/IPTVWORLDAR058.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='Free IPTVFree058', cmdlist=cmdlist, finishedCallback=None)
                        elif returnValue =="com_259":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia801508.us.archive.org/24/items/iptvworld_20191114/IPTVWORLDAR059.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='Free IPTVFree059', cmdlist=cmdlist, finishedCallback=None)
                        elif returnValue =="com_260":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia801508.us.archive.org/24/items/iptvworld_20191114/IPTVWORLDAR060.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='Free IPTVFree060', cmdlist=cmdlist, finishedCallback=None)
                        elif returnValue =="com_261":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia801508.us.archive.org/24/items/iptvworld_20191114/IPTVWORLDAR061.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='Free IPTVFree051', cmdlist=cmdlist, finishedCallback=None)
                        elif returnValue =="com_262":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia801508.us.archive.org/24/items/iptvworld_20191114/IPTVWORLDAR062.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='Free IPTVFree052', cmdlist=cmdlist, finishedCallback=None)
                        elif returnValue =="com_263":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia801508.us.archive.org/24/items/iptvworld_20191114/IPTVWORLDAR063.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='Free IPTVFree053', cmdlist=cmdlist, finishedCallback=None)
                        elif returnValue =="com_264":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia801508.us.archive.org/24/items/iptvworld_20191114/IPTVWORLDAR064.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='Free IPTVFree054', cmdlist=cmdlist, finishedCallback=None)
                        elif returnValue =="com_265":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia801508.us.archive.org/24/items/iptvworld_20191114/IPTVWORLDAR065.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='Free IPTVFree055', cmdlist=cmdlist, finishedCallback=None)
                        elif returnValue =="com_266":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia801508.us.archive.org/24/items/iptvworld_20191114/IPTVWORLDAR066.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='Free IPTVFree056', cmdlist=cmdlist, finishedCallback=None)
                        elif returnValue =="com_267":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia801508.us.archive.org/24/items/iptvworld_20191114/IPTVWORLDAR067.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='Free IPTVFree057', cmdlist=cmdlist, finishedCallback=None)
                        elif returnValue =="com_268":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia801508.us.archive.org/24/items/iptvworld_20191114/IPTVWORLDAR068.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='Free IPTVFree058', cmdlist=cmdlist, finishedCallback=None)
                        elif returnValue =="com_269":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia801508.us.archive.org/24/items/iptvworld_20191114/IPTVWORLDAR069.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='Free IPTVFree069', cmdlist=cmdlist, finishedCallback=None)
                        elif returnValue =="com_270":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia801508.us.archive.org/24/items/iptvworld_20191114/IPTVWORLDAR070.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='Free IPTVFree070', cmdlist=cmdlist, finishedCallback=None)
                        elif returnValue =="com_271":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia801508.us.archive.org/24/items/iptvworld_20191114/IPTVWORLDAR071.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='Free IPTVFree071', cmdlist=cmdlist, finishedCallback=None)
                        elif returnValue =="com_272":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia801508.us.archive.org/24/items/iptvworld_20191114/IPTVWORLDAR072.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='Free IPTVFree072', cmdlist=cmdlist, finishedCallback=None)
                        elif returnValue =="com_273":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia801508.us.archive.org/24/items/iptvworld_20191114/IPTVWORLDAR073.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='Free IPTVFree073', cmdlist=cmdlist, finishedCallback=None)
                        elif returnValue =="com_274":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia801508.us.archive.org/24/items/iptvworld_20191114/IPTVWORLDAR074.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='Free IPTVFree074', cmdlist=cmdlist, finishedCallback=None)
                        elif returnValue =="com_275":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia801508.us.archive.org/24/items/iptvworld_20191114/IPTVWORLDAR075.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='Free IPTVFree075', cmdlist=cmdlist, finishedCallback=None)
                        elif returnValue =="com_276":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia801508.us.archive.org/24/items/iptvworld_20191114/IPTVWORLDAR076.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='Free IPTVFree076', cmdlist=cmdlist, finishedCallback=None)
                        elif returnValue =="com_277":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia801508.us.archive.org/24/items/iptvworld_20191114/IPTVWORLDAR077.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='Free IPTVFree077', cmdlist=cmdlist, finishedCallback=None)
                        elif returnValue =="com_278":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia801508.us.archive.org/24/items/iptvworld_20191114/IPTVWORLDAR078.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='Free IPTVFree078', cmdlist=cmdlist, finishedCallback=None)
                        elif returnValue =="com_279":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia801508.us.archive.org/24/items/iptvworld_20191114/IPTVWORLDAR079.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='Free IPTVFree079', cmdlist=cmdlist, finishedCallback=None)
                        elif returnValue =="com_280":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia801508.us.archive.org/24/items/iptvworld_20191114/IPTVWORLDAR080.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='Free IPTVFree080', cmdlist=cmdlist, finishedCallback=None)
                        elif returnValue =="com_281":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia801405.us.archive.org/15/items/iptvworld_20191114_1209/IPTVWORLDFR001.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='Free IPTVFree081', cmdlist=cmdlist, finishedCallback=None)
                        elif returnValue =="com_282":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia801405.us.archive.org/15/items/iptvworld_20191114_1209/IPTVWORLDFR002.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='Free IPTVFree082', cmdlist=cmdlist, finishedCallback=None)
                        elif returnValue =="com_283":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia801405.us.archive.org/15/items/iptvworld_20191114_1209/IPTVWORLDFR003.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='Free IPTVFree083', cmdlist=cmdlist, finishedCallback=None)
                        elif returnValue =="com_284":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia801405.us.archive.org/15/items/iptvworld_20191114_1209/IPTVWORLDFR004.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='Free IPTVFree084', cmdlist=cmdlist, finishedCallback=None)
                        elif returnValue =="com_285":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia801405.us.archive.org/15/items/iptvworld_20191114_1209/IPTVWORLDFR005.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='Free IPTVFree085', cmdlist=cmdlist, finishedCallback=None)
                        elif returnValue =="com_286":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia801405.us.archive.org/15/items/iptvworld_20191114_1209/IPTVWORLDFR006.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='Free IPTVFree086', cmdlist=cmdlist, finishedCallback=None)
                        elif returnValue =="com_287":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia801405.us.archive.org/15/items/iptvworld_20191114_1209/IPTVWORLDFR007.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='Free IPTVFree087', cmdlist=cmdlist, finishedCallback=None)
                        elif returnValue =="com_288":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia801405.us.archive.org/15/items/iptvworld_20191114_1209/IPTVWORLDFR008.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='Free IPTVFree088', cmdlist=cmdlist, finishedCallback=None)
                        elif returnValue =="com_289":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia801405.us.archive.org/15/items/iptvworld_20191114_1209/IPTVWORLDFR009.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='Free IPTVFree089', cmdlist=cmdlist, finishedCallback=None)
                        elif returnValue =="com_290":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia801405.us.archive.org/15/items/iptvworld_20191114_1209/IPTVWORLDFR010.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='Free IPTVFree090', cmdlist=cmdlist, finishedCallback=None)
                        elif returnValue =="com_291":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia801405.us.archive.org/15/items/iptvworld_20191114_1209/IPTVWORLDFR011.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='Free IPTVFree091', cmdlist=cmdlist, finishedCallback=None)
                        elif returnValue =="com_292":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia801405.us.archive.org/15/items/iptvworld_20191114_1209/IPTVWORLDFR012.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='Free IPTVFree092', cmdlist=cmdlist, finishedCallback=None)
                        elif returnValue =="com_293":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia801405.us.archive.org/15/items/iptvworld_20191114_1209/IPTVWORLDFR013.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='Free IPTVFree093', cmdlist=cmdlist, finishedCallback=None)
                        elif returnValue =="com_294":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia801405.us.archive.org/15/items/iptvworld_20191114_1209/IPTVWORLDFR014.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='Free IPTVFree094', cmdlist=cmdlist, finishedCallback=None)
                        elif returnValue =="com_295":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia801405.us.archive.org/15/items/iptvworld_20191114_1209/IPTVWORLDFR015.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='Free IPTVFree095', cmdlist=cmdlist, finishedCallback=None)
                        elif returnValue =="com_296":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia801405.us.archive.org/15/items/iptvworld_20191114_1209/IPTVWORLDFR016.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='Free IPTVFree096', cmdlist=cmdlist, finishedCallback=None)
                        elif returnValue =="com_297":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia801405.us.archive.org/15/items/iptvworld_20191114_1209/IPTVWORLDFR017.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='Free IPTVFree097', cmdlist=cmdlist, finishedCallback=None)
                        elif returnValue =="com_298":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia801405.us.archive.org/15/items/iptvworld_20191114_1209/IPTVWORLDFR018.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='Free IPTVFree098', cmdlist=cmdlist, finishedCallback=None)
                        elif returnValue =="com_299":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia801405.us.archive.org/15/items/iptvworld_20191114_1209/IPTVWORLDFR019.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='Free IPTVFree099', cmdlist=cmdlist, finishedCallback=None)
                        elif returnValue =="com_300":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia801405.us.archive.org/15/items/iptvworld_20191114_1209/IPTVWORLDFR020.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='Free IPTVFree100', cmdlist=cmdlist, finishedCallback=None)
                        elif returnValue =="com_301":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia801405.us.archive.org/15/items/iptvworld_20191114_1209/IPTVWORLDFR021.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='Free IPTVFree001', cmdlist=cmdlist, finishedCallback=None)
                        elif returnValue =="com_302":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia801405.us.archive.org/15/items/iptvworld_20191114_1209/IPTVWORLDFR022.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='Free IPTVFree002', cmdlist=cmdlist, finishedCallback=None)
                        elif returnValue =="com_303":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia801405.us.archive.org/15/items/iptvworld_20191114_1209/IPTVWORLDFR023.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='Free IPTVFree003', cmdlist=cmdlist, finishedCallback=None)
                        elif returnValue =="com_304":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'") 
                                cmdlist.append("%s https://ia801405.us.archive.org/15/items/iptvworld_20191114_1209/IPTVWORLDFR024.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='Free IPTVFree004', cmdlist=cmdlist, finishedCallback=None)
                        elif returnValue =="com_305":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia801405.us.archive.org/15/items/iptvworld_20191114_1209/IPTVWORLDFR025.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='Free IPTVFree005', cmdlist=cmdlist, finishedCallback=None)
                        elif returnValue =="com_306":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia801405.us.archive.org/15/items/iptvworld_20191114_1209/IPTVWORLDFR026.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='Free IPTVFree006', cmdlist=cmdlist, finishedCallback=None)
                        elif returnValue =="com_307":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia801405.us.archive.org/15/items/iptvworld_20191114_1209/IPTVWORLDFR027.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='Free IPTVFree007', cmdlist=cmdlist, finishedCallback=None)
                        elif returnValue =="com_308":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")    
                                cmdlist.append("%s https://ia801405.us.archive.org/15/items/iptvworld_20191114_1209/IPTVWORLDFR028.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='Free IPTVFree008', cmdlist=cmdlist, finishedCallback=None)
                        elif returnValue =="com_309":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia801405.us.archive.org/15/items/iptvworld_20191114_1209/IPTVWORLDFR029.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='Free IPTVFree009', cmdlist=cmdlist, finishedCallback=None)
                        elif returnValue =="com_310":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia801405.us.archive.org/15/items/iptvworld_20191114_1209/IPTVWORLDFR030.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='Free IPTVFree010', cmdlist=cmdlist, finishedCallback=None)
                        elif returnValue =="com_311":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia801405.us.archive.org/15/items/iptvworld_20191114_1209/IPTVWORLDFR031.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='Free IPTVFree011', cmdlist=cmdlist, finishedCallback=None)
                        elif returnValue =="com_312":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia801405.us.archive.org/15/items/iptvworld_20191114_1209/IPTVWORLDFR032.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='Free IPTVFree012', cmdlist=cmdlist, finishedCallback=None)
                        elif returnValue =="com_313":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia801405.us.archive.org/15/items/iptvworld_20191114_1209/IPTVWORLDFR033.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='Free IPTVFree013', cmdlist=cmdlist, finishedCallback=None)
                        elif returnValue =="com_314":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia801405.us.archive.org/15/items/iptvworld_20191114_1209/IPTVWORLDFR034.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='Free IPTVFree014', cmdlist=cmdlist, finishedCallback=None)
                        elif returnValue =="com_315":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia801405.us.archive.org/15/items/iptvworld_20191114_1209/IPTVWORLDFR035.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='Free IPTVFree015', cmdlist=cmdlist, finishedCallback=None)
                        elif returnValue =="com_316":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia801405.us.archive.org/15/items/iptvworld_20191114_1209/IPTVWORLDFR036.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='Free IPTVFree016', cmdlist=cmdlist, finishedCallback=None)
                        elif returnValue =="com_317":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia801405.us.archive.org/15/items/iptvworld_20191114_1209/IPTVWORLDFR037.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='Free IPTVFree017', cmdlist=cmdlist, finishedCallback=None)
                        elif returnValue =="com_318":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia801405.us.archive.org/15/items/iptvworld_20191114_1209/IPTVWORLDFR038.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='Free IPTVFree018', cmdlist=cmdlist, finishedCallback=None)
                        elif returnValue =="com_319":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia801405.us.archive.org/15/items/iptvworld_20191114_1209/IPTVWORLDFR039.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='Free IPTVFree019', cmdlist=cmdlist, finishedCallback=None)
                        elif returnValue =="com_320":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia801405.us.archive.org/15/items/iptvworld_20191114_1209/IPTVWORLDFR040.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='Free IPTVFree020', cmdlist=cmdlist, finishedCallback=None)
                        elif returnValue =="com_321":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia801405.us.archive.org/15/items/iptvworld_20191114_1209/IPTVWORLDUS001.sh -qO - | /bin/sh" % self.wget)    
                                self.session.open(Console3, title='Free IPTVFree021', cmdlist=cmdlist, finishedCallback=None)
                        elif returnValue =="com_322":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia801405.us.archive.org/15/items/iptvworld_20191114_1209/IPTVWORLDUS002.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='Free IPTVFree022', cmdlist=cmdlist, finishedCallback=None)
                        elif returnValue =="com_323":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia801405.us.archive.org/15/items/iptvworld_20191114_1209/IPTVWORLDUS003.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='Free IPTVFree023', cmdlist=cmdlist, finishedCallback=None)
                        elif returnValue =="com_324":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia801405.us.archive.org/15/items/iptvworld_20191114_1209/IPTVWORLDUS004.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='Free IPTVFree024', cmdlist=cmdlist, finishedCallback=None)
                        elif returnValue =="com_325":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia801405.us.archive.org/15/items/iptvworld_20191114_1209/IPTVWORLDUS005.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='Free IPTVFree025', cmdlist=cmdlist, finishedCallback=None)
                        elif returnValue =="com_326":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia801405.us.archive.org/15/items/iptvworld_20191114_1209/IPTVWORLDUS006.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='Free IPTVFree026', cmdlist=cmdlist, finishedCallback=None)
                        elif returnValue =="com_327":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia801405.us.archive.org/15/items/iptvworld_20191114_1209/IPTVWORLDUS007.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='Free IPTVFree027', cmdlist=cmdlist, finishedCallback=None)
                        elif returnValue =="com_328":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia801405.us.archive.org/15/items/iptvworld_20191114_1209/IPTVWORLDUS008.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='Free IPTVFree028', cmdlist=cmdlist, finishedCallback=None)
                        elif returnValue =="com_329":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia801405.us.archive.org/15/items/iptvworld_20191114_1209/IPTVWORLDUS009.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='Free IPTVFree029', cmdlist=cmdlist, finishedCallback=None)
                        elif returnValue =="com_330":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia801405.us.archive.org/15/items/iptvworld_20191114_1209/IPTVWORLDUS010.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='Free IPTVFree030', cmdlist=cmdlist, finishedCallback=None)
                        elif returnValue =="com_331":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia801405.us.archive.org/15/items/iptvworld_20191114_1209/IPTVWORLDUS011.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='Free IPTVFree031', cmdlist=cmdlist, finishedCallback=None)
                        elif returnValue =="com_332":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia801405.us.archive.org/15/items/iptvworld_20191114_1209/IPTVWORLDUS012.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='Free IPTVFree032', cmdlist=cmdlist, finishedCallback=None)
                        elif returnValue =="com_333":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia801405.us.archive.org/15/items/iptvworld_20191114_1209/IPTVWORLDUS013.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='Free IPTVFree033', cmdlist=cmdlist, finishedCallback=None)
                        elif returnValue =="com_334":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia801405.us.archive.org/15/items/iptvworld_20191114_1209/IPTVWORLDUS014.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='Free IPTVFree034', cmdlist=cmdlist, finishedCallback=None)
                        elif returnValue =="com_335":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia801405.us.archive.org/15/items/iptvworld_20191114_1209/IPTVWORLDUS015.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='Free IPTVFree035', cmdlist=cmdlist, finishedCallback=None)
                        elif returnValue =="com_336":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia801405.us.archive.org/15/items/iptvworld_20191114_1209/IPTVWORLDUS016.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='Free IPTVFree036', cmdlist=cmdlist, finishedCallback=None)
                        elif returnValue =="com_337":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia801405.us.archive.org/15/items/iptvworld_20191114_1209/IPTVWORLDUS017.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='Free IPTVFree037', cmdlist=cmdlist, finishedCallback=None)
                        elif returnValue =="com_338":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia801405.us.archive.org/15/items/iptvworld_20191114_1209/IPTVWORLDUS018.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='Free IPTVFree038', cmdlist=cmdlist, finishedCallback=None)
                        elif returnValue =="com_339":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia801405.us.archive.org/15/items/iptvworld_20191114_1209/IPTVWORLDUS019.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='Free IPTVFree039', cmdlist=cmdlist, finishedCallback=None)
                        elif returnValue =="com_340":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia801405.us.archive.org/15/items/iptvworld_20191114_1209/IPTVWORLDUS020.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='Free IPTVFree040', cmdlist=cmdlist, finishedCallback=None)
                        elif returnValue =="com_341":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia801405.us.archive.org/15/items/iptvworld_20191114_1209/IPTVWORLDUS021.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='Free IPTVFree041', cmdlist=cmdlist, finishedCallback=None)
                        elif returnValue =="com_342":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia801405.us.archive.org/15/items/iptvworld_20191114_1209/IPTVWORLDUS022.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='Free IPTVFree042', cmdlist=cmdlist, finishedCallback=None)
                        elif returnValue =="com_343":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia801405.us.archive.org/15/items/iptvworld_20191114_1209/IPTVWORLDRU001.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='Free IPTVFree043', cmdlist=cmdlist, finishedCallback=None)
                        elif returnValue =="com_344":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia801405.us.archive.org/15/items/iptvworld_20191114_1209/IPTVWORLDRU002.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='Free IPTVFree044', cmdlist=cmdlist, finishedCallback=None)
                        elif returnValue =="com_345":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia801405.us.archive.org/15/items/iptvworld_20191114_1209/IPTVWORLDRU003.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='Free IPTVFree045', cmdlist=cmdlist, finishedCallback=None)
                        elif returnValue =="com_346":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia801405.us.archive.org/15/items/iptvworld_20191114_1209/IPTVWORLDRU004.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='Free IPTVFree046', cmdlist=cmdlist, finishedCallback=None)
                        elif returnValue =="com_347":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia801405.us.archive.org/15/items/iptvworld_20191114_1209/IPTVWORLDRU005.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='Free IPTVFree047', cmdlist=cmdlist, finishedCallback=None)
                        elif returnValue =="com_348":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia801405.us.archive.org/15/items/iptvworld_20191114_1209/IPTVWORLDRU006.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='Free IPTVFree048', cmdlist=cmdlist, finishedCallback=None)
                        elif returnValue =="com_349":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia801405.us.archive.org/15/items/iptvworld_20191114_1209/IPTVWORLDRU007.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='Free IPTVFree049', cmdlist=cmdlist, finishedCallback=None)
                        elif returnValue =="com_350":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia801405.us.archive.org/15/items/iptvworld_20191114_1209/IPTVWORLDRU008.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='Free IPTVFree050', cmdlist=cmdlist, finishedCallback=None)
                        elif returnValue =="com_351":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia801405.us.archive.org/15/items/iptvworld_20191114_1209/IPTVWORLDRU009.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='Free IPTVFree051', cmdlist=cmdlist, finishedCallback=None)
                        elif returnValue =="com_352":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia801405.us.archive.org/15/items/iptvworld_20191114_1209/IPTVWORLDRU010.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='Free IPTVFree052', cmdlist=cmdlist, finishedCallback=None)
                        elif returnValue =="com_353":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia801405.us.archive.org/15/items/iptvworld_20191114_1209/IPTVWORLDRU011.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='Free IPTVFree053', cmdlist=cmdlist, finishedCallback=None)
                        elif returnValue =="com_354":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia801405.us.archive.org/15/items/iptvworld_20191114_1209/IPTVWORLDRU012.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='Free IPTVFree054', cmdlist=cmdlist, finishedCallback=None)
                        elif returnValue =="com_355":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia801405.us.archive.org/15/items/iptvworld_20191114_1209/IPTVWORLDRU013.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='Free IPTVFree055', cmdlist=cmdlist, finishedCallback=None)
                        elif returnValue =="com_356":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia801405.us.archive.org/15/items/iptvworld_20191114_1209/IPTVWORLDRU014.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='Free IPTVFree056', cmdlist=cmdlist, finishedCallback=None)
                        elif returnValue =="com_357":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia801405.us.archive.org/15/items/iptvworld_20191114_1209/IPTVWORLDRU015.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='Free IPTVFree057', cmdlist=cmdlist, finishedCallback=None)
                        elif returnValue =="com_358":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia801405.us.archive.org/15/items/iptvworld_20191114_1209/IPTVWORLDRU016.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='Free IPTVFree058', cmdlist=cmdlist, finishedCallback=None)
                        elif returnValue =="com_359":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia801405.us.archive.org/15/items/iptvworld_20191114_1209/IPTVWORLDRU017.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='Free IPTVFree059', cmdlist=cmdlist, finishedCallback=None)
                        elif returnValue =="com_360":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia801405.us.archive.org/15/items/iptvworld_20191114_1209/IPTVWORLDRU018.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='Free IPTVFree060', cmdlist=cmdlist, finishedCallback=None)
                        elif returnValue =="com_361":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia801405.us.archive.org/15/items/iptvworld_20191114_1209/IPTVWORLDRU019.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='Free IPTVFree051', cmdlist=cmdlist, finishedCallback=None)
                        elif returnValue =="com_362":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia801405.us.archive.org/15/items/iptvworld_20191114_1209/IPTVWORLDRU020.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='Free IPTVFree052', cmdlist=cmdlist, finishedCallback=None)
                        elif returnValue =="com_363":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia801405.us.archive.org/15/items/iptvworld_20191114_1209/IPTVWORLDRU021.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='Free IPTVFree053', cmdlist=cmdlist, finishedCallback=None)
                        elif returnValue =="com_364":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia801405.us.archive.org/15/items/iptvworld_20191114_1209/IPTVWORLDRU022.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='Free IPTVFree054', cmdlist=cmdlist, finishedCallback=None)
                        elif returnValue =="com_365":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia801405.us.archive.org/15/items/iptvworld_20191114_1209/IPTVWORLDPL001.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='Free IPTVFree055', cmdlist=cmdlist, finishedCallback=None)
                        elif returnValue =="com_366":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia801405.us.archive.org/15/items/iptvworld_20191114_1209/IPTVWORLDPL002.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='Free IPTVFree056', cmdlist=cmdlist, finishedCallback=None)
                        elif returnValue =="com_367":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia801405.us.archive.org/15/items/iptvworld_20191114_1209/IPTVWORLDPL003.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='Free IPTVFree057', cmdlist=cmdlist, finishedCallback=None)
                        elif returnValue =="com_368":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia801405.us.archive.org/15/items/iptvworld_20191114_1209/IPTVWORLDPL004.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='Free IPTVFree058', cmdlist=cmdlist, finishedCallback=None)
                        elif returnValue =="com_369":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia801405.us.archive.org/15/items/iptvworld_20191114_1209/IPTVWORLDPL005.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='Free IPTVFree069', cmdlist=cmdlist, finishedCallback=None)
                        elif returnValue =="com_370":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia801405.us.archive.org/15/items/iptvworld_20191114_1209/IPTVWORLDPL006.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='Free IPTVFree070', cmdlist=cmdlist, finishedCallback=None)
                        elif returnValue =="com_371":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia801405.us.archive.org/15/items/iptvworld_20191114_1209/IPTVWORLDPL007.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='Free IPTVFree071', cmdlist=cmdlist, finishedCallback=None)
                        elif returnValue =="com_372":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia801405.us.archive.org/15/items/iptvworld_20191114_1209/IPTVWORLDDE001.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='Free IPTVFree072', cmdlist=cmdlist, finishedCallback=None)
                        elif returnValue =="com_373":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia801405.us.archive.org/15/items/iptvworld_20191114_1209/IPTVWORLDDE002.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='Free IPTVFree073', cmdlist=cmdlist, finishedCallback=None)
                        elif returnValue =="com_374":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia801405.us.archive.org/15/items/iptvworld_20191114_1209/IPTVWORLDDE003.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='Free IPTVFree074', cmdlist=cmdlist, finishedCallback=None)
                        elif returnValue =="com_375":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia801405.us.archive.org/15/items/iptvworld_20191114_1209/IPTVWORLDDE004.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='Free IPTVFree075', cmdlist=cmdlist, finishedCallback=None)
                        elif returnValue =="com_376":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia801405.us.archive.org/15/items/iptvworld_20191114_1209/IPTVWORLDDE005.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='Free IPTVFree076', cmdlist=cmdlist, finishedCallback=None)
                        elif returnValue =="com_377":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia801405.us.archive.org/15/items/iptvworld_20191114_1209/IPTVWORLDDE006.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='Free IPTVFree077', cmdlist=cmdlist, finishedCallback=None)
                        elif returnValue =="com_378":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia801405.us.archive.org/15/items/iptvworld_20191114_1209/IPTVWORLDDE007.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='Free IPTVFree078', cmdlist=cmdlist, finishedCallback=None)
                        elif returnValue =="com_379":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia801405.us.archive.org/15/items/iptvworld_20191114_1209/IPTVWORLDDE008.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='Free IPTVFree079', cmdlist=cmdlist, finishedCallback=None)
                        elif returnValue =="com_380":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia801405.us.archive.org/15/items/iptvworld_20191114_1209/IPTVWORLDDE009.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='Free IPTVFree080', cmdlist=cmdlist, finishedCallback=None)
                        elif returnValue =="com_381":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia801405.us.archive.org/15/items/iptvworld_20191114_1209/IPTVWORLDDE010.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='Free IPTVFree081', cmdlist=cmdlist, finishedCallback=None)
                        elif returnValue =="com_382":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia801405.us.archive.org/15/items/iptvworld_20191114_1209/IPTVWORLDDE011.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='Free IPTVFree082', cmdlist=cmdlist, finishedCallback=None)
                        elif returnValue =="com_383":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia801405.us.archive.org/15/items/iptvworld_20191114_1209/IPTVWORLDDE012.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='Free IPTVFree083', cmdlist=cmdlist, finishedCallback=None)
                        elif returnValue =="com_384":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia801405.us.archive.org/15/items/iptvworld_20191114_1209/IPTVWORLDDE013.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='Free IPTVFree084', cmdlist=cmdlist, finishedCallback=None)
                        elif returnValue =="com_385":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia801405.us.archive.org/15/items/iptvworld_20191114_1209/IPTVWORLDDE014.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='Free IPTVFree085', cmdlist=cmdlist, finishedCallback=None)
                        elif returnValue =="com_386":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia801405.us.archive.org/15/items/iptvworld_20191114_1209/IPTVWORLDDE015.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='Free IPTVFree086', cmdlist=cmdlist, finishedCallback=None)
                        elif returnValue =="com_387":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia801405.us.archive.org/15/items/iptvworld_20191114_1209/IPTVWORLDDE016.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='Free IPTVFree087', cmdlist=cmdlist, finishedCallback=None)
                        elif returnValue =="com_388":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia801405.us.archive.org/15/items/iptvworld_20191114_1209/IPTVWORLDNE001.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='Free IPTVFree088', cmdlist=cmdlist, finishedCallback=None)
                        elif returnValue =="com_389":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia801405.us.archive.org/15/items/iptvworld_20191114_1209/IPTVWORLDNE002.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='Free IPTVFree089', cmdlist=cmdlist, finishedCallback=None)
                        elif returnValue =="com_390":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia801405.us.archive.org/15/items/iptvworld_20191114_1209/IPTVWORLDNE003.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='Free IPTVFree090', cmdlist=cmdlist, finishedCallback=None)
                        elif returnValue =="com_391":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia801405.us.archive.org/15/items/iptvworld_20191114_1209/IPTVWORLDNE004.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='Free IPTVFree091', cmdlist=cmdlist, finishedCallback=None)
                        elif returnValue =="com_392":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia801405.us.archive.org/15/items/iptvworld_20191114_1209/IPTVWORLDNE005.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='Free IPTVFree092', cmdlist=cmdlist, finishedCallback=None)
                        elif returnValue =="com_393":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia801405.us.archive.org/15/items/iptvworld_20191114_1209/IPTVWORLDNE006.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='Free IPTVFree093', cmdlist=cmdlist, finishedCallback=None)
                        elif returnValue =="com_394":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia801405.us.archive.org/15/items/iptvworld_20191114_1209/IPTVWORLDNE007.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='Free IPTVFree094', cmdlist=cmdlist, finishedCallback=None)
                        elif returnValue =="com_395":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia801405.us.archive.org/15/items/iptvworld_20191114_1209/IPTVWORLDNE008.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='Free IPTVFree095', cmdlist=cmdlist, finishedCallback=None)
                        elif returnValue =="com_396":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia801405.us.archive.org/15/items/iptvworld_20191114_1209/IPTVWORLDNE009.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='Free IPTVFree096', cmdlist=cmdlist, finishedCallback=None)
                        elif returnValue =="com_397":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia801405.us.archive.org/15/items/iptvworld_20191114_1209/IPTVWORLDNE010.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='Free IPTVFree097', cmdlist=cmdlist, finishedCallback=None)
                        elif returnValue =="com_398":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia801405.us.archive.org/15/items/iptvworld_20191114_1209/IPTVWORLDNE011.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='Free IPTVFree098', cmdlist=cmdlist, finishedCallback=None)
                        elif returnValue =="com_399":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia801405.us.archive.org/15/items/iptvworld_20191114_1209/IPTVWORLDNE012.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='Free IPTVFree099', cmdlist=cmdlist, finishedCallback=None)
                        elif returnValue =="com_400":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia801405.us.archive.org/15/items/iptvworld_20191114_1209/IPTVWORLDNE013.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='Free IPTVFree100', cmdlist=cmdlist, finishedCallback=None)
                        elif returnValue =="com_401":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia801405.us.archive.org/15/items/iptvworld_20191114_1209/IPTVWORLDNE014.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='Free IPTVFree001', cmdlist=cmdlist, finishedCallback=None)
                        elif returnValue =="com_402":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia801405.us.archive.org/15/items/iptvworld_20191114_1209/IPTVWORLDNE015.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='Free IPTVFree002', cmdlist=cmdlist, finishedCallback=None)
                        elif returnValue =="com_403":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia801405.us.archive.org/15/items/iptvworld_20191114_1209/IPTVWORLDNE016.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='Free IPTVFree003', cmdlist=cmdlist, finishedCallback=None)
                        elif returnValue =="com_404":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'") 
                                cmdlist.append("%s https://ia801405.us.archive.org/15/items/iptvworld_20191114_1209/IPTVWORLDNE017.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='Free IPTVFree004', cmdlist=cmdlist, finishedCallback=None)
                        elif returnValue =="com_405":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia801405.us.archive.org/15/items/iptvworld_20191114_1209/IPTVWORLDTR001.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='Free IPTVFree005', cmdlist=cmdlist, finishedCallback=None)
                        elif returnValue =="com_406":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia801405.us.archive.org/15/items/iptvworld_20191114_1209/IPTVWORLDTR002.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='Free IPTVFree006', cmdlist=cmdlist, finishedCallback=None)
                        elif returnValue =="com_407":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia801405.us.archive.org/15/items/iptvworld_20191114_1209/IPTVWORLDTR003.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='Free IPTVFree007', cmdlist=cmdlist, finishedCallback=None)
                        elif returnValue =="com_408":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")    
                                cmdlist.append("%s https://ia801405.us.archive.org/15/items/iptvworld_20191114_1209/IPTVWORLDTR004.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='Free IPTVFree008', cmdlist=cmdlist, finishedCallback=None)
                        elif returnValue =="com_409":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia801405.us.archive.org/15/items/iptvworld_20191114_1209/IPTVWORLDTR005.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='Free IPTVFree009', cmdlist=cmdlist, finishedCallback=None)
                        elif returnValue =="com_410":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia801405.us.archive.org/15/items/iptvworld_20191114_1209/IPTVWORLDTR006.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='Free IPTVFree010', cmdlist=cmdlist, finishedCallback=None)
                        elif returnValue =="com_411":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia801405.us.archive.org/15/items/iptvworld_20191114_1209/IPTVWORLDTR007.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='Free IPTVFree011', cmdlist=cmdlist, finishedCallback=None)
                        elif returnValue =="com_412":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia801405.us.archive.org/15/items/iptvworld_20191114_1209/IPTVWORLDTR008.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='Free IPTVFree012', cmdlist=cmdlist, finishedCallback=None)
                        elif returnValue =="com_413":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia801405.us.archive.org/15/items/iptvworld_20191114_1209/IPTVWORLDTR009.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='Free IPTVFree013', cmdlist=cmdlist, finishedCallback=None)
                        elif returnValue =="com_414":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia801405.us.archive.org/15/items/iptvworld_20191114_1209/IPTVWORLDTR010.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='Free IPTVFree014', cmdlist=cmdlist, finishedCallback=None)
                        elif returnValue =="com_415":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia801405.us.archive.org/15/items/iptvworld_20191114_1209/IPTVWORLDTR011.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='Free IPTVFree015', cmdlist=cmdlist, finishedCallback=None)
                        elif returnValue =="com_416":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia801405.us.archive.org/15/items/iptvworld_20191114_1209/IPTVWORLDTR012.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='Free IPTVFree016', cmdlist=cmdlist, finishedCallback=None)
                        elif returnValue =="com_417":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia801405.us.archive.org/15/items/iptvworld_20191114_1209/IPTVWORLDAL001.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='Free IPTVFree017', cmdlist=cmdlist, finishedCallback=None)
                        elif returnValue =="com_418":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia801405.us.archive.org/15/items/iptvworld_20191114_1209/IPTVWORLDAL002.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='Free IPTVFree018', cmdlist=cmdlist, finishedCallback=None)
                        elif returnValue =="com_419":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia801405.us.archive.org/15/items/iptvworld_20191114_1209/IPTVWORLDAL003.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='Free IPTVFree019', cmdlist=cmdlist, finishedCallback=None)
                        elif returnValue =="com_420":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia801405.us.archive.org/15/items/iptvworld_20191114_1209/IPTVWORLDAL004.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='Free IPTVFree020', cmdlist=cmdlist, finishedCallback=None)
                        elif returnValue =="com_421":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia801405.us.archive.org/15/items/iptvworld_20191114_1209/IPTVWORLDAL005.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='Free IPTVFree021', cmdlist=cmdlist, finishedCallback=None)
                        elif returnValue =="com_422":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia801405.us.archive.org/15/items/iptvworld_20191114_1209/IPTVWORLDAL006.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='Free IPTVFree022', cmdlist=cmdlist, finishedCallback=None)
                        elif returnValue =="com_423":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia801405.us.archive.org/15/items/iptvworld_20191114_1209/IPTVWORLDAL007.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='Free IPTVFree023', cmdlist=cmdlist, finishedCallback=None)
                        elif returnValue =="com_424":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia801405.us.archive.org/15/items/iptvworld_20191114_1209/IPTVWORLDAL008.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='Free IPTVFree024', cmdlist=cmdlist, finishedCallback=None)
                        elif returnValue =="com_425":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia801405.us.archive.org/15/items/iptvworld_20191114_1209/IPTVWORLDAL009.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='Free IPTVFree025', cmdlist=cmdlist, finishedCallback=None)
                        elif returnValue =="com_426":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia801405.us.archive.org/15/items/iptvworld_20191114_1209/IPTVWORLDAL010.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='Free IPTVFree026', cmdlist=cmdlist, finishedCallback=None)
                        elif returnValue =="com_427":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia801405.us.archive.org/15/items/iptvworld_20191114_1209/IPTVWORLDAL011.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='Free IPTVFree027', cmdlist=cmdlist, finishedCallback=None)
                        elif returnValue =="com_428":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia801405.us.archive.org/15/items/iptvworld_20191114_1209/IPTVWORLDAL012.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='Free IPTVFree028', cmdlist=cmdlist, finishedCallback=None)
                        elif returnValue =="com_429":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia601406.us.archive.org/29/items/iptvworldit/IPTVWORLDIT001.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='Free IPTVFree029', cmdlist=cmdlist, finishedCallback=None)
                        elif returnValue =="com_430":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia601406.us.archive.org/29/items/iptvworldit/IPTVWORLDIT002.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='Free IPTVFree030', cmdlist=cmdlist, finishedCallback=None)
                        elif returnValue =="com_431":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia601406.us.archive.org/29/items/iptvworldit/IPTVWORLDIT003.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='Free IPTVFree031', cmdlist=cmdlist, finishedCallback=None)
                        elif returnValue =="com_432":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia601406.us.archive.org/29/items/iptvworldit/IPTVWORLDIT004.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='Free IPTVFree032', cmdlist=cmdlist, finishedCallback=None)
                        elif returnValue =="com_433":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia601406.us.archive.org/29/items/iptvworldit/IPTVWORLDIT005.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='Free IPTVFree033', cmdlist=cmdlist, finishedCallback=None)
                        elif returnValue =="com_434":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia601406.us.archive.org/29/items/iptvworldit/IPTVWORLDIT006.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='Free IPTVFree034', cmdlist=cmdlist, finishedCallback=None)
                        elif returnValue =="com_435":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia601406.us.archive.org/29/items/iptvworldit/IPTVWORLDIT007.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='Free IPTVFree035', cmdlist=cmdlist, finishedCallback=None)
                        elif returnValue =="com_436":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia601406.us.archive.org/29/items/iptvworldit/IPTVWORLDIT008.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='Free IPTVFree036', cmdlist=cmdlist, finishedCallback=None)
                        elif returnValue =="com_437":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia601406.us.archive.org/29/items/iptvworldit/IPTVWORLDIT009.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='Free IPTVFree037', cmdlist=cmdlist, finishedCallback=None)
                        elif returnValue =="com_438":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia601406.us.archive.org/29/items/iptvworldit/IPTVWORLDIT010.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='Free IPTVFree038', cmdlist=cmdlist, finishedCallback=None)
                        elif returnValue =="com_439":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia601406.us.archive.org/29/items/iptvworldit/IPTVWORLDIT011.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='Free IPTVFree039', cmdlist=cmdlist, finishedCallback=None)
                        elif returnValue =="com_440":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia601406.us.archive.org/29/items/iptvworldit/IPTVWORLDIT012.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='Free IPTVFree040', cmdlist=cmdlist, finishedCallback=None)
                        elif returnValue =="com_441":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia601406.us.archive.org/29/items/iptvworldit/IPTVWORLDIT013.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='Free IPTVFree041', cmdlist=cmdlist, finishedCallback=None)
                        elif returnValue =="com_442":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia601406.us.archive.org/29/items/iptvworldit/IPTVWORLDUK001.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='Free IPTVFree042', cmdlist=cmdlist, finishedCallback=None)
                        elif returnValue =="com_443":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia601406.us.archive.org/29/items/iptvworldit/IPTVWORLDUK002.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='Free IPTVFree043', cmdlist=cmdlist, finishedCallback=None)
                        elif returnValue =="com_444":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia601406.us.archive.org/29/items/iptvworldit/IPTVWORLDUK003.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='Free IPTVFree044', cmdlist=cmdlist, finishedCallback=None)
                        elif returnValue =="com_445":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia601406.us.archive.org/29/items/iptvworldit/IPTVWORLDUK004.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='Free IPTVFree045', cmdlist=cmdlist, finishedCallback=None)
                        elif returnValue =="com_446":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia601406.us.archive.org/29/items/iptvworldit/IPTVWORLDUK005.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='Free IPTVFree046', cmdlist=cmdlist, finishedCallback=None)
                        elif returnValue =="com_447":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia601406.us.archive.org/29/items/iptvworldit/IPTVWORLDUK006.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='Free IPTVFree047', cmdlist=cmdlist, finishedCallback=None)
                        elif returnValue =="com_448":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia601406.us.archive.org/29/items/iptvworldit/IPTVWORLDUK007.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='Free IPTVFree048', cmdlist=cmdlist, finishedCallback=None)
                        elif returnValue =="com_449":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia601406.us.archive.org/29/items/iptvworldit/IPTVWORLDUK008.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='Free IPTVFree049', cmdlist=cmdlist, finishedCallback=None)
                        elif returnValue =="com_450":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia601406.us.archive.org/29/items/iptvworldit/IPTVWORLDUK009.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='Free IPTVFree050', cmdlist=cmdlist, finishedCallback=None)
                        elif returnValue =="com_451":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia601406.us.archive.org/29/items/iptvworldit/IPTVWORLDUK010.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='Free IPTVFree051', cmdlist=cmdlist, finishedCallback=None)
                        elif returnValue =="com_452":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia601406.us.archive.org/29/items/iptvworldit/IPTVWORLDUK011.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='Free IPTVFree052', cmdlist=cmdlist, finishedCallback=None)
                        elif returnValue =="com_453":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia601406.us.archive.org/29/items/iptvworldit/IPTVWORLDUK012.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='Free IPTVFree053', cmdlist=cmdlist, finishedCallback=None)
                        elif returnValue =="com_454":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia601406.us.archive.org/29/items/iptvworldit/IPTVWORLDUK013.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='Free IPTVFree054', cmdlist=cmdlist, finishedCallback=None)
                        elif returnValue =="com_455":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia601406.us.archive.org/29/items/iptvworldit/IPTVWORLDUK014.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='Free IPTVFree055', cmdlist=cmdlist, finishedCallback=None)
                        elif returnValue =="com_456":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia601406.us.archive.org/29/items/iptvworldit/IPTVWORLDUK015.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='Free IPTVFree056', cmdlist=cmdlist, finishedCallback=None)
                        elif returnValue =="com_457":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia601406.us.archive.org/29/items/iptvworldit/IPTVWORLDUK016.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='Free IPTVFree057', cmdlist=cmdlist, finishedCallback=None)
                        elif returnValue =="com_458":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia601406.us.archive.org/29/items/iptvworldit/IPTVWORLDUK017.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='Free IPTVFree058', cmdlist=cmdlist, finishedCallback=None)
                        elif returnValue =="com_459":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia601406.us.archive.org/29/items/iptvworldit/IPTVWORLDUK018.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='Free IPTVFree059', cmdlist=cmdlist, finishedCallback=None)
                        elif returnValue =="com_460":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia601406.us.archive.org/29/items/iptvworldit/IPTVWORLDES001.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='Free IPTVFree060', cmdlist=cmdlist, finishedCallback=None)
                        elif returnValue =="com_461":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia601406.us.archive.org/29/items/iptvworldit/IPTVWORLDES002.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='Free IPTVFree051', cmdlist=cmdlist, finishedCallback=None)
                        elif returnValue =="com_462":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia601406.us.archive.org/29/items/iptvworldit/IPTVWORLDES003.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='Free IPTVFree052', cmdlist=cmdlist, finishedCallback=None)
                        elif returnValue =="com_463":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia601406.us.archive.org/29/items/iptvworldit/IPTVWORLDES004.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='Free IPTVFree053', cmdlist=cmdlist, finishedCallback=None)
                        elif returnValue =="com_464":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia601406.us.archive.org/29/items/iptvworldit/IPTVWORLDES005.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='Free IPTVFree054', cmdlist=cmdlist, finishedCallback=None)
                        elif returnValue =="com_465":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia601406.us.archive.org/29/items/iptvworldit/IPTVWORLDES006.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='Free IPTVFree055', cmdlist=cmdlist, finishedCallback=None)
                        elif returnValue =="com_466":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia601406.us.archive.org/29/items/iptvworldit/IPTVWORLDES007.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='Free IPTVFree056', cmdlist=cmdlist, finishedCallback=None)
                        elif returnValue =="com_467":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia601406.us.archive.org/29/items/iptvworldit/IPTVWORLDES008.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='Free IPTVFree057', cmdlist=cmdlist, finishedCallback=None)
                        elif returnValue =="com_468":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia601406.us.archive.org/29/items/iptvworldit/IPTVWORLDES009.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='Free IPTVFree058', cmdlist=cmdlist, finishedCallback=None)
                        elif returnValue =="com_469":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia601406.us.archive.org/29/items/iptvworldit/IPTVWORLDES010.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='Free IPTVFree069', cmdlist=cmdlist, finishedCallback=None)
                        elif returnValue =="com_470":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia601406.us.archive.org/29/items/iptvworldit/IPTVWORLDES011.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='Free IPTVFree070', cmdlist=cmdlist, finishedCallback=None)
                        elif returnValue =="com_471":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia601406.us.archive.org/29/items/iptvworldit/IPTVWORLDES012.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='Free IPTVFree071', cmdlist=cmdlist, finishedCallback=None)
                        elif returnValue =="com_472":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia601406.us.archive.org/29/items/iptvworldit/IPTVWORLDES013.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='Free IPTVFree072', cmdlist=cmdlist, finishedCallback=None)
                        elif returnValue =="com_473":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia601406.us.archive.org/29/items/iptvworldit/IPTVWORLDES014.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='Free IPTVFree073', cmdlist=cmdlist, finishedCallback=None)
                        elif returnValue =="com_474":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia601406.us.archive.org/29/items/iptvworldit/IPTVWORLDES015.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='Free IPTVFree074', cmdlist=cmdlist, finishedCallback=None)
                        elif returnValue =="com_475":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia601406.us.archive.org/29/items/iptvworldit/IPTVWORLDES016.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='Free IPTVFree075', cmdlist=cmdlist, finishedCallback=None)
                        elif returnValue =="com_476":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia601406.us.archive.org/29/items/iptvworldit/IPTVWORLDES017.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='Free IPTVFree076', cmdlist=cmdlist, finishedCallback=None)
                        elif returnValue =="com_477":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia601406.us.archive.org/29/items/iptvworldit/IPTVWORLDES018.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='Free IPTVFree077', cmdlist=cmdlist, finishedCallback=None)
                        elif returnValue =="com_478":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia601406.us.archive.org/29/items/iptvworldit/IPTVWORLDES019.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='Free IPTVFree078', cmdlist=cmdlist, finishedCallback=None)
                        elif returnValue =="com_479":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia601406.us.archive.org/29/items/iptvworldit/IPTVWORLDES020.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='Free IPTVFree079', cmdlist=cmdlist, finishedCallback=None)
                        elif returnValue =="com_480":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia601406.us.archive.org/29/items/iptvworldit/IPTVWORLDES021.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='Free IPTVFree080', cmdlist=cmdlist, finishedCallback=None)
                        elif returnValue =="com_481":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia601406.us.archive.org/29/items/iptvworldit/IPTVWORLDES022.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='Free IPTVFree081', cmdlist=cmdlist, finishedCallback=None)
                        elif returnValue =="com_482":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia601406.us.archive.org/29/items/iptvworldit/IPTVWORLDES023.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='Free IPTVFree082', cmdlist=cmdlist, finishedCallback=None)
                        elif returnValue =="com_483":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia601406.us.archive.org/29/items/iptvworldit/IPTVWORLDPO001.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='Free IPTVFree083', cmdlist=cmdlist, finishedCallback=None)
                        elif returnValue =="com_484":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia601406.us.archive.org/29/items/iptvworldit/IPTVWORLDPO002.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='Free IPTVFree084', cmdlist=cmdlist, finishedCallback=None)
                        elif returnValue =="com_485":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia601406.us.archive.org/29/items/iptvworldit/IPTVWORLDPO003.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='Free IPTVFree085', cmdlist=cmdlist, finishedCallback=None)
                        elif returnValue =="com_486":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia601406.us.archive.org/29/items/iptvworldit/IPTVWORLDPO004.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='Free IPTVFree086', cmdlist=cmdlist, finishedCallback=None)
                        elif returnValue =="com_487":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia601406.us.archive.org/29/items/iptvworldit/IPTVWORLDPO005.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='Free IPTVFree087', cmdlist=cmdlist, finishedCallback=None)
                        elif returnValue =="com_488":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia601406.us.archive.org/29/items/iptvworldit/IPTVWORLDPO006.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='Free IPTVFree088', cmdlist=cmdlist, finishedCallback=None)
                        elif returnValue =="com_489":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia601406.us.archive.org/29/items/iptvworldit/IPTVWORLDPO007.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='Free IPTVFree089', cmdlist=cmdlist, finishedCallback=None)
                        elif returnValue =="com_490":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia601406.us.archive.org/29/items/iptvworldit/IPTVWORLDPO008.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='Free IPTVFree090', cmdlist=cmdlist, finishedCallback=None)
                        elif returnValue =="com_491":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia601406.us.archive.org/29/items/iptvworldit/IPTVWORLDPO009.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='Free IPTVFree091', cmdlist=cmdlist, finishedCallback=None)
                        elif returnValue =="com_492":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia601406.us.archive.org/29/items/iptvworldit/IPTVWORLDPO010.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='Free IPTVFree092', cmdlist=cmdlist, finishedCallback=None)
                        elif returnValue =="com_493":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia601406.us.archive.org/29/items/iptvworldit/IPTVWORLDPO011.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='Free IPTVFree093', cmdlist=cmdlist, finishedCallback=None)
                        elif returnValue =="com_494":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia601406.us.archive.org/29/items/iptvworldit/IPTVWORLDPO012.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='Free IPTVFree094', cmdlist=cmdlist, finishedCallback=None)
                        elif returnValue =="com_495":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia601406.us.archive.org/29/items/iptvworldit/IPTVWORLDPO013.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='Free IPTVFree095', cmdlist=cmdlist, finishedCallback=None)
                        elif returnValue =="com_496":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia601406.us.archive.org/29/items/iptvworldit/IPTVWORLDPO014.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='Free IPTVFree096', cmdlist=cmdlist, finishedCallback=None)
                        elif returnValue =="com_497":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia601406.us.archive.org/29/items/iptvworldit/IPTVWORLDPO015.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='Free IPTVFree097', cmdlist=cmdlist, finishedCallback=None)
                        elif returnValue =="com_498":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia601406.us.archive.org/29/items/iptvworldit/IPTVWORLDPO016.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='Free IPTVFree098', cmdlist=cmdlist, finishedCallback=None)
                        elif returnValue =="com_499":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia601406.us.archive.org/29/items/iptvworldit/IPTVWORLDPO017.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='Free IPTVFree099', cmdlist=cmdlist, finishedCallback=None)
                        elif returnValue =="com_500":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia601406.us.archive.org/29/items/iptvworldit/IPTVWORLDPO018.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='Free IPTVFree100', cmdlist=cmdlist, finishedCallback=None)
                        elif returnValue =="com_501":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia801404.us.archive.org/31/items/iptvworld_20191116/IPTVWORLDRO001.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='Free IPTVFree001', cmdlist=cmdlist, finishedCallback=None)
                        elif returnValue =="com_502":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia801404.us.archive.org/31/items/iptvworld_20191116/IPTVWORLDRO002.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='Free IPTVFree002', cmdlist=cmdlist, finishedCallback=None)
                        elif returnValue =="com_503":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia801404.us.archive.org/31/items/iptvworld_20191116/IPTVWORLDRO003.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='Free IPTVFree003', cmdlist=cmdlist, finishedCallback=None)
                        elif returnValue =="com_504":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'") 
                                cmdlist.append("%s https://ia801404.us.archive.org/31/items/iptvworld_20191116/IPTVWORLDRO004.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='Free IPTVFree004', cmdlist=cmdlist, finishedCallback=None)
                        elif returnValue =="com_505":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia801404.us.archive.org/31/items/iptvworld_20191116/IPTVWORLDRO005.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='Free IPTVFree005', cmdlist=cmdlist, finishedCallback=None)
                        elif returnValue =="com_506":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia801404.us.archive.org/31/items/iptvworld_20191116/IPTVWORLDRO006.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='Free IPTVFree006', cmdlist=cmdlist, finishedCallback=None)
                        elif returnValue =="com_507":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia801404.us.archive.org/31/items/iptvworld_20191116/IPTVWORLDRO007.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='Free IPTVFree007', cmdlist=cmdlist, finishedCallback=None)
                        elif returnValue =="com_508":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")    
                                cmdlist.append("%s https://ia801404.us.archive.org/31/items/iptvworld_20191116/IPTVWORLDRO008.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='Free IPTVFree008', cmdlist=cmdlist, finishedCallback=None)
                        elif returnValue =="com_509":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia801404.us.archive.org/31/items/iptvworld_20191116/IPTVWORLDRO009.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='Free IPTVFree009', cmdlist=cmdlist, finishedCallback=None)
                        elif returnValue =="com_510":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia801404.us.archive.org/31/items/iptvworld_20191116/IPTVWORLDRO010.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='Free IPTVFree010', cmdlist=cmdlist, finishedCallback=None)
                        elif returnValue =="com_511":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia801404.us.archive.org/31/items/iptvworld_20191116/IPTVWORLDRO011.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='Free IPTVFree011', cmdlist=cmdlist, finishedCallback=None)
                        elif returnValue =="com_512":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia801404.us.archive.org/31/items/iptvworld_20191116/IPTVWORLDRO012.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='Free IPTVFree012', cmdlist=cmdlist, finishedCallback=None)
                        elif returnValue =="com_513":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia801404.us.archive.org/31/items/iptvworld_20191116/IPTVWORLDRO013.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='Free IPTVFree013', cmdlist=cmdlist, finishedCallback=None)
                        elif returnValue =="com_514":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia801404.us.archive.org/31/items/iptvworld_20191116/IPTVWORLDRO014.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='Free IPTVFree014', cmdlist=cmdlist, finishedCallback=None)
                        elif returnValue =="com_515":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia801404.us.archive.org/31/items/iptvworld_20191116/IPTVWORLDBU001.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='Free IPTVFree015', cmdlist=cmdlist, finishedCallback=None)
                        elif returnValue =="com_516":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia801404.us.archive.org/31/items/iptvworld_20191116/IPTVWORLDBU002.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='Free IPTVFree016', cmdlist=cmdlist, finishedCallback=None)
                        elif returnValue =="com_517":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia801404.us.archive.org/31/items/iptvworld_20191116/IPTVWORLDBU003.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='Free IPTVFree017', cmdlist=cmdlist, finishedCallback=None)
                        elif returnValue =="com_518":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia801404.us.archive.org/31/items/iptvworld_20191116/IPTVWORLDBU004.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='Free IPTVFree018', cmdlist=cmdlist, finishedCallback=None)
                        elif returnValue =="com_519":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia801404.us.archive.org/31/items/iptvworld_20191116/IPTVWORLDBU005.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='Free IPTVFree019', cmdlist=cmdlist, finishedCallback=None)
                        elif returnValue =="com_520":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia801404.us.archive.org/31/items/iptvworld_20191116/IPTVWORLDBU006.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='Free IPTVFree020', cmdlist=cmdlist, finishedCallback=None)
                        elif returnValue =="com_521":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia801404.us.archive.org/31/items/iptvworld_20191116/IPTVWORLDBU007.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='Free IPTVFree021', cmdlist=cmdlist, finishedCallback=None)
                        elif returnValue =="com_522":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia801404.us.archive.org/31/items/iptvworld_20191116/IPTVWORLDBU008.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='Free IPTVFree022', cmdlist=cmdlist, finishedCallback=None)
                        elif returnValue =="com_523":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia801404.us.archive.org/31/items/iptvworld_20191116/IPTVWORLDBU009.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='Free IPTVFree023', cmdlist=cmdlist, finishedCallback=None)
                        elif returnValue =="com_524":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia801404.us.archive.org/31/items/iptvworld_20191116/IPTVWORLDBU010.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='Free IPTVFree024', cmdlist=cmdlist, finishedCallback=None)
                        elif returnValue =="com_525":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia801404.us.archive.org/31/items/iptvworld_20191116/IPTVWORLDBU011.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='Free IPTVFree025', cmdlist=cmdlist, finishedCallback=None)
                        elif returnValue =="com_526":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia801404.us.archive.org/31/items/iptvworld_20191116/IPTVWORLDBU012.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='Free IPTVFree026', cmdlist=cmdlist, finishedCallback=None)
                        elif returnValue =="com_527":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia801404.us.archive.org/31/items/iptvworld_20191116/IPTVWORLDBU013.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='Free IPTVFree027', cmdlist=cmdlist, finishedCallback=None)
                        elif returnValue =="com_528":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia801404.us.archive.org/31/items/iptvworld_20191116/IPTVWORLDBU014.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='Free IPTVFree028', cmdlist=cmdlist, finishedCallback=None)
                        elif returnValue =="com_529":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia801404.us.archive.org/31/items/iptvworld_20191116/IPTVWORLDBU015.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='Free IPTVFree029', cmdlist=cmdlist, finishedCallback=None)
                        elif returnValue =="com_530":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia801404.us.archive.org/31/items/iptvworld_20191116/IPTVWORLDBU016.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='Free IPTVFree030', cmdlist=cmdlist, finishedCallback=None)
                        elif returnValue =="com_531":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia801404.us.archive.org/31/items/iptvworld_20191116/IPTVWORLDBU017.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='Free IPTVFree031', cmdlist=cmdlist, finishedCallback=None)
                        elif returnValue =="com_532":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia801404.us.archive.org/31/items/iptvworld_20191116/IPTVWORLDBU018.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='Free IPTVFree032', cmdlist=cmdlist, finishedCallback=None)
                        elif returnValue =="com_533":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia801404.us.archive.org/31/items/iptvworld_20191116/IPTVWORLDBU019.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='Free IPTVFree033', cmdlist=cmdlist, finishedCallback=None)
                        elif returnValue =="com_534":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia801404.us.archive.org/31/items/iptvworld_20191116/IPTVWORLDBU020.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='Free IPTVFree034', cmdlist=cmdlist, finishedCallback=None)
                        elif returnValue =="com_535":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia801404.us.archive.org/31/items/iptvworld_20191116/IPTVWORLDBU021.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='Free IPTVFree035', cmdlist=cmdlist, finishedCallback=None)
                        elif returnValue =="com_536":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia801404.us.archive.org/31/items/iptvworld_20191116/IPTVWORLDBU022.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='Free IPTVFree036', cmdlist=cmdlist, finishedCallback=None)
                        elif returnValue =="com_537":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia801404.us.archive.org/31/items/iptvworld_20191116/IPTVWORLDBU023.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='Free IPTVFree037', cmdlist=cmdlist, finishedCallback=None)
                        elif returnValue =="com_538":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia801404.us.archive.org/31/items/iptvworld_20191116/IPTVWORLDBU024.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='Free IPTVFree038', cmdlist=cmdlist, finishedCallback=None)
                        elif returnValue =="com_539":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia801404.us.archive.org/31/items/iptvworld_20191116/IPTVWORLDBU025.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='Free IPTVFree039', cmdlist=cmdlist, finishedCallback=None)
                        elif returnValue =="com_540":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia801404.us.archive.org/31/items/iptvworld_20191116/IPTVWORLDBU026.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='Free IPTVFree040', cmdlist=cmdlist, finishedCallback=None)
                        elif returnValue =="com_541":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia801404.us.archive.org/31/items/iptvworld_20191116/IPTVWORLDBU027.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='Free IPTVFree041', cmdlist=cmdlist, finishedCallback=None)
                        elif returnValue =="com_542":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia801404.us.archive.org/31/items/iptvworld_20191116/IPTVWORLDGR001.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='Free IPTVFree042', cmdlist=cmdlist, finishedCallback=None)
                        elif returnValue =="com_543":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia801404.us.archive.org/31/items/iptvworld_20191116/IPTVWORLDGR002.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='Free IPTVFree043', cmdlist=cmdlist, finishedCallback=None)
                        elif returnValue =="com_544":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia801404.us.archive.org/31/items/iptvworld_20191116/IPTVWORLDGR003.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='Free IPTVFree044', cmdlist=cmdlist, finishedCallback=None)
                        elif returnValue =="com_545":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia801404.us.archive.org/31/items/iptvworld_20191116/IPTVWORLDGR004.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='Free IPTVFree045', cmdlist=cmdlist, finishedCallback=None)
                        elif returnValue =="com_546":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia801404.us.archive.org/31/items/iptvworld_20191116/IPTVWORLDGR005.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='Free IPTVFree046', cmdlist=cmdlist, finishedCallback=None)
                        elif returnValue =="com_547":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia801404.us.archive.org/31/items/iptvworld_20191116/IPTVWORLDGR006.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='Free IPTVFree047', cmdlist=cmdlist, finishedCallback=None)
                        elif returnValue =="com_548":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia801404.us.archive.org/31/items/iptvworld_20191116/IPTVWORLDGR007.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='Free IPTVFree048', cmdlist=cmdlist, finishedCallback=None)
                        elif returnValue =="com_549":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia801404.us.archive.org/31/items/iptvworld_20191116/IPTVWORLDGR008.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='Free IPTVFree049', cmdlist=cmdlist, finishedCallback=None)
                        elif returnValue =="com_550":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia801404.us.archive.org/31/items/iptvworld_20191116/IPTVWORLDGR009.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='Free IPTVFree050', cmdlist=cmdlist, finishedCallback=None)
                        elif returnValue =="com_551":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia801404.us.archive.org/31/items/iptvworld_20191116/IPTVWORLDGR010.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='Free IPTVFree051', cmdlist=cmdlist, finishedCallback=None)
                        elif returnValue =="com_552":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia801404.us.archive.org/31/items/iptvworld_20191116/IPTVWORLDSW001.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='Free IPTVFree052', cmdlist=cmdlist, finishedCallback=None)
                        elif returnValue =="com_553":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia801404.us.archive.org/31/items/iptvworld_20191116/IPTVWORLDSW002.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='Free IPTVFree053', cmdlist=cmdlist, finishedCallback=None)
                        elif returnValue =="com_554":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia801404.us.archive.org/31/items/iptvworld_20191116/IPTVWORLDSW003.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='Free IPTVFree054', cmdlist=cmdlist, finishedCallback=None)
                        elif returnValue =="com_555":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia801404.us.archive.org/31/items/iptvworld_20191116/IPTVWORLDSW004.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='Free IPTVFree055', cmdlist=cmdlist, finishedCallback=None)
                        elif returnValue =="com_556":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia801404.us.archive.org/31/items/iptvworld_20191116/IPTVWORLDSW005.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='Free IPTVFree056', cmdlist=cmdlist, finishedCallback=None)
                        elif returnValue =="com_557":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia801404.us.archive.org/31/items/iptvworld_20191116/IPTVWORLDSW006.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='Free IPTVFree057', cmdlist=cmdlist, finishedCallback=None)
                        elif returnValue =="com_558":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia801404.us.archive.org/31/items/iptvworld_20191116/IPTVWORLDSW007.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='Free IPTVFree058', cmdlist=cmdlist, finishedCallback=None)
                        elif returnValue =="com_559":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia801404.us.archive.org/31/items/iptvworld_20191116/IPTVWORLDSW008.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='Free IPTVFree059', cmdlist=cmdlist, finishedCallback=None)
                        elif returnValue =="com_560":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia801404.us.archive.org/31/items/iptvworld_20191116/IPTVWORLDYU001.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='Free IPTVFree060', cmdlist=cmdlist, finishedCallback=None)
                        elif returnValue =="com_561":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia801404.us.archive.org/31/items/iptvworld_20191116/IPTVWORLDYU002.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='Free IPTVFree051', cmdlist=cmdlist, finishedCallback=None)
                        elif returnValue =="com_562":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia801404.us.archive.org/31/items/iptvworld_20191116/IPTVWORLDYU003.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='Free IPTVFree052', cmdlist=cmdlist, finishedCallback=None)
                        elif returnValue =="com_563":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia801404.us.archive.org/31/items/iptvworld_20191116/IPTVWORLDYU004.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='Free IPTVFree053', cmdlist=cmdlist, finishedCallback=None)
                        elif returnValue =="com_564":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia801404.us.archive.org/31/items/iptvworld_20191116/IPTVWORLDYU005.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='Free IPTVFree054', cmdlist=cmdlist, finishedCallback=None)
                        elif returnValue =="com_565":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia801404.us.archive.org/31/items/iptvworld_20191116/IPTVWORLDYU006.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='Free IPTVFree055', cmdlist=cmdlist, finishedCallback=None)
                        elif returnValue =="com_566":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia801404.us.archive.org/31/items/iptvworld_20191116/IPTVWORLDYU007.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='Free IPTVFree056', cmdlist=cmdlist, finishedCallback=None)
                        elif returnValue =="com_567":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia801404.us.archive.org/31/items/iptvworld_20191116/IPTVWORLDYU008.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='Free IPTVFree057', cmdlist=cmdlist, finishedCallback=None)
                        elif returnValue =="com_568":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia801404.us.archive.org/31/items/iptvworld_20191116/IPTVWORLDYU009.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='Free IPTVFree058', cmdlist=cmdlist, finishedCallback=None)
                        elif returnValue =="com_569":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia801404.us.archive.org/31/items/iptvworld_20191116/IPTVWORLDYU010.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='Free IPTVFree069', cmdlist=cmdlist, finishedCallback=None)
                        elif returnValue =="com_570":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia801404.us.archive.org/31/items/iptvworld_20191116/IPTVWORLDYU011.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='Free IPTVFree070', cmdlist=cmdlist, finishedCallback=None)
                        elif returnValue =="com_571":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia801404.us.archive.org/31/items/iptvworld_20191116/IPTVWORLDYU012.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='Free IPTVFree071', cmdlist=cmdlist, finishedCallback=None)
                        elif returnValue =="com_572":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia801404.us.archive.org/31/items/iptvworld_20191116/IPTVWORLDYU013.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='Free IPTVFree072', cmdlist=cmdlist, finishedCallback=None)
                        elif returnValue =="com_573":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia801404.us.archive.org/31/items/iptvworld_20191116/IPTVWORLDYU014.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='Free IPTVFree073', cmdlist=cmdlist, finishedCallback=None)
                        elif returnValue =="com_574":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia801404.us.archive.org/31/items/iptvworld_20191116/IPTVWORLDYU015.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='Free IPTVFree074', cmdlist=cmdlist, finishedCallback=None)
                        elif returnValue =="com_575":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia801404.us.archive.org/31/items/iptvworld_20191116/IPTVWORLDYU019.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='Free IPTVFree075', cmdlist=cmdlist, finishedCallback=None)
                        elif returnValue =="com_576":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia801404.us.archive.org/31/items/iptvworld_20191116/IPTVWORLDYU020.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='Free IPTVFree076', cmdlist=cmdlist, finishedCallback=None)
                        elif returnValue =="com_577":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia801404.us.archive.org/31/items/iptvworld_20191116/IPTVWORLDYU021.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='Free IPTVFree077', cmdlist=cmdlist, finishedCallback=None)
                        elif returnValue =="com_578":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia801404.us.archive.org/31/items/iptvworld_20191116/IPTVWORLDYU022.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='Free IPTVFree078', cmdlist=cmdlist, finishedCallback=None)
                        elif returnValue =="com_579":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia801404.us.archive.org/31/items/iptvworld_20191116/IPTVWORLDYU023.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='Free IPTVFree079', cmdlist=cmdlist, finishedCallback=None)
                        elif returnValue =="com_580":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia801404.us.archive.org/31/items/iptvworld_20191116/IPTVWORLDYU024.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='Free IPTVFree080', cmdlist=cmdlist, finishedCallback=None)
                        elif returnValue =="com_581":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia801404.us.archive.org/31/items/iptvworld_20191116/IPTVWORLDYU025.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='Free IPTVFree081', cmdlist=cmdlist, finishedCallback=None)
                        elif returnValue =="com_582":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia801404.us.archive.org/31/items/iptvworld_20191116/IPTVWORLDYU026.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='Free IPTVFree082', cmdlist=cmdlist, finishedCallback=None)
                        elif returnValue =="com_583":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia801404.us.archive.org/31/items/iptvworld_20191116/IPTVWORLDYU027.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='Free IPTVFree083', cmdlist=cmdlist, finishedCallback=None)
                        elif returnValue =="com_584":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia801404.us.archive.org/31/items/iptvworld_20191116/IPTVWORLDYU028.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='Free IPTVFree084', cmdlist=cmdlist, finishedCallback=None)
                        elif returnValue =="com_585":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia801404.us.archive.org/31/items/iptvworld_20191116/IPTVWORLDYU029.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='Free IPTVFree085', cmdlist=cmdlist, finishedCallback=None)
                        elif returnValue =="com_586":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia801404.us.archive.org/31/items/iptvworld_20191116/IPTVWORLDYU030.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='Free IPTVFree086', cmdlist=cmdlist, finishedCallback=None)
                        elif returnValue =="com_587":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia801404.us.archive.org/31/items/iptvworld_20191116/IPTVWORLDYU031.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='Free IPTVFree087', cmdlist=cmdlist, finishedCallback=None)
                        elif returnValue =="com_588":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia801404.us.archive.org/31/items/iptvworld_20191116/IPTVWORLDYU032.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='Free IPTVFree088', cmdlist=cmdlist, finishedCallback=None)
                        elif returnValue =="com_589":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia801404.us.archive.org/31/items/iptvworld_20191116/IPTVWORLDYU033.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='Free IPTVFree089', cmdlist=cmdlist, finishedCallback=None)
                        elif returnValue =="com_590":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia801404.us.archive.org/31/items/iptvworld_20191116/IPTVWORLDYU034.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='Free IPTVFree090', cmdlist=cmdlist, finishedCallback=None)
                        elif returnValue =="com_591":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia801404.us.archive.org/31/items/iptvworld_20191116/IPTVWORLDYU035.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='Free IPTVFree091', cmdlist=cmdlist, finishedCallback=None)
                        elif returnValue =="com_592":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia801404.us.archive.org/31/items/iptvworld_20191116/IPTVWORLDYU036.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='Free IPTVFree092', cmdlist=cmdlist, finishedCallback=None)
                        elif returnValue =="com_593":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia801404.us.archive.org/31/items/iptvworld_20191116/IPTVWORLDCZ001.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='Free IPTVFree093', cmdlist=cmdlist, finishedCallback=None)
                        elif returnValue =="com_594":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia801404.us.archive.org/31/items/iptvworld_20191116/IPTVWORLDCZ002.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='Free IPTVFree094', cmdlist=cmdlist, finishedCallback=None)
                        elif returnValue =="com_595":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia801404.us.archive.org/31/items/iptvworld_20191116/IPTVWORLDCZ003.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='Free IPTVFree095', cmdlist=cmdlist, finishedCallback=None)
                        elif returnValue =="com_596":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia801404.us.archive.org/31/items/iptvworld_20191116/IPTVWORLDCZ004.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='Free IPTVFree096', cmdlist=cmdlist, finishedCallback=None)
                        elif returnValue =="com_597":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia801404.us.archive.org/31/items/iptvworld_20191116/IPTVWORLDCZ005.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='Free IPTVFree097', cmdlist=cmdlist, finishedCallback=None)
                        elif returnValue =="com_598":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia801404.us.archive.org/31/items/iptvworld_20191116/IPTVWORLDCA001.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='Free IPTVFree098', cmdlist=cmdlist, finishedCallback=None)
                        elif returnValue =="com_599":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia801404.us.archive.org/31/items/iptvworld_20191116/IPTVWORLDCA002.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='Free IPTVFree099', cmdlist=cmdlist, finishedCallback=None)
                        elif returnValue =="com_600":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia801404.us.archive.org/31/items/iptvworld_20191116/IPTVWORLDCA003.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='Free IPTVFree100', cmdlist=cmdlist, finishedCallback=None)
                        elif returnValue =="com_601":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia801404.us.archive.org/31/items/iptvworld_20191116/IPTVWORLDCA004.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='Free IPTVFree091', cmdlist=cmdlist, finishedCallback=None)
                        elif returnValue =="com_602":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia801404.us.archive.org/31/items/iptvworld_20191116/IPTVWORLDCA005.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='Free IPTVFree092', cmdlist=cmdlist, finishedCallback=None)
                        elif returnValue =="com_603":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia801404.us.archive.org/31/items/iptvworld_20191116/IPTVWORLDBR001.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='Free IPTVFree093', cmdlist=cmdlist, finishedCallback=None)
                        elif returnValue =="com_604":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia801404.us.archive.org/31/items/iptvworld_20191116/IPTVWORLDBR002.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='Free IPTVFree094', cmdlist=cmdlist, finishedCallback=None)
                        elif returnValue =="com_605":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia801404.us.archive.org/31/items/iptvworld_20191116/IPTVWORLDBR003.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='Free IPTVFree095', cmdlist=cmdlist, finishedCallback=None)
                        elif returnValue =="com_606":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia801404.us.archive.org/31/items/iptvworld_20191116/IPTVWORLDBR004.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='Free IPTVFree096', cmdlist=cmdlist, finishedCallback=None)
                        elif returnValue =="com_607":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia801404.us.archive.org/31/items/iptvworld_20191116/IPTVWORLDBR005.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='Free IPTVFree097', cmdlist=cmdlist, finishedCallback=None)
                        elif returnValue =="com_608":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia801404.us.archive.org/31/items/iptvworld_20191116/IPTVWORLDBR006.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='Free IPTVFree098', cmdlist=cmdlist, finishedCallback=None)
                        elif returnValue =="com_609":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia801404.us.archive.org/31/items/iptvworld_20191116/IPTVWORLDBR007.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='Free IPTVFree099', cmdlist=cmdlist, finishedCallback=None)
                        elif returnValue =="com_610":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia801404.us.archive.org/31/items/iptvworld_20191116/IPTVWORLDBR008.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='Free IPTVFree100', cmdlist=cmdlist, finishedCallback=None)

                        elif returnValue =="com_611":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia801404.us.archive.org/31/items/iptvworld_20191116/IPTVWORLDBR009.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='Free IPTVFree097', cmdlist=cmdlist, finishedCallback=None)
                        elif returnValue =="com_612":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia801404.us.archive.org/31/items/iptvworld_20191116/IPTVWORLDBR010.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='Free IPTVFree098', cmdlist=cmdlist, finishedCallback=None)
                        elif returnValue =="com_613":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia801404.us.archive.org/31/items/iptvworld_20191116/IPTVWORLDBR011.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='Free IPTVFree099', cmdlist=cmdlist, finishedCallback=None)
                        elif returnValue =="com_614":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia801404.us.archive.org/31/items/iptvworld_20191116/IPTVWORLDBR012.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='Free IPTVFree100', cmdlist=cmdlist, finishedCallback=None)

                        elif returnValue =="com_615":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia801404.us.archive.org/31/items/iptvworld_20191116/IPTVWORLDBR013.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='Free IPTVFree091', cmdlist=cmdlist, finishedCallback=None)
                        elif returnValue =="com_616":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia801404.us.archive.org/31/items/iptvworld_20191116/IPTVWORLDBR014.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='Free IPTVFree092', cmdlist=cmdlist, finishedCallback=None)
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
            #self.session.open(Console, title='Update links Bein Sport', cmdlist=cmdlist, finishedCallback=None)
        def IPTV(self):
            cmdlist = []
            cmdlist.append("%s -qO - '" % self.wget + "'")
            cmdlist.append("%s https://ia903000.us.archive.org/30/items/FreeServerinfo/Freeiptv.sh -qO - | /bin/sh" % self.wget)
            self.session.open(Console, title='Update links Bein Sport RMC', cmdlist=cmdlist, finishedCallback=None)
        def AUTOUPD(self):
            cmdlist = []
            cmdlist.append("%s -qO - '" % self.wget + "'")
            cmdlist.append("%s https://ia903000.us.archive.org/30/items/FreeServerinfo/Auto_update_Freeiptv.sh -qO - | /bin/sh" % self.wget)
            self.session.open(Console, title='AUTO Update links Bein Sport RMC', cmdlist=cmdlist, finishedCallback=None)
        def prombt(self, com):
            scripts = "/usr/lib/enigma2/python/Plugins/Extensions/FreeServer/scripts/"
            os.chmod(scripts, 755)
            self.session.open(Console,_("Executing: %s") % (com), ["%s" % com])
        def cancel(self):
            self.close(None)
            
