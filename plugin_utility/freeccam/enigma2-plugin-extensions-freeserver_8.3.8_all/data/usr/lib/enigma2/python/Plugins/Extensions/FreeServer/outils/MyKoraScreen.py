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
from Tools.Directories import fileExists
from time import *
import time
from enigma import eTimer, getDesktop
from enigma import *
import os, sys, re
#import urllib
import base64
from Plugins.Extensions.FreeServer.outils.MyShPrombt import *
#session = None
#data_xml = 'aHR0cHM6Ly9pYTYwMDcwMi51cy5hcmNoaXZlLm9yZy8yNi9pdGVtcy9kcmVhbW9zYXQvY2Ftc3RhcnQwLnR4dA=='
#xml_path = base64.b64decode(data_xml)
#version = '7710'    
#currversion = '7710'   
###################################################################################################### 
Name_001= "RMC 1 FHD"
Name_002= "RMC 2 FHD"
Name_003= "RMC 3 FHD"
Name_004= "RMC 4 FHD"
Name_1= "BEINFR 1 FHD"
Name_2= "BEINFR 2 FHD"
Name_3= "BEINFR 3 FHD"
Name_01= "BEIN 1 FHD"
Name_02= "BEIN 2 FHD"
Name_03= "BEIN 3 FHD"
Name_04= "BEIN 4 FHD"
Name_05= "BEIN 5 FHD"
Name_06= "BEIN 6 FHD"
Name_07= "BEIN 7 FHD"
Name_08= "BEIN 8 FHD"
Name_09= "BEIN 9 FHD"
Name_10= "BEIN 10 FHD"
Name_11= "BEIN 11 FHD"
Name_12= "DAZN 1 BAR HD"
Name_13= "DAZN 2 BAR HD"

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
class MyKoraScreen(Screen):
#### Edit By RAED
        if isHD():
            skin = """
                 <screen position="40,50" size="1200,636" title="IPTV WORLD SPORT MOVIES        CHANNELS" flags="wfNoBorder" backgroundColor="#20000000">
                      <widget source="Title" render="Label" position="0,3" size="1200,28" zPosition="3" halign="center" valign="center" font="Regular;26" backgroundColor="#20000000" transparent="1" foregroundColor="#bab329"/>       
                      <widget name="key_red" position="10,556" size="100,40" backgroundColor="red" valign="center" halign="center" zPosition="2"  foregroundColor="white" font="Regular;20"/>
                      <widget name="key_green" position="120,556" size="100,40" backgroundColor="green" valign="center" halign="center" zPosition="2"  foregroundColor="white" font="Regular;20"/>
                      <widget name="myMenu" position="0,40" size="620,500" foregroundColor="#FEFEFE" transparent="1" zPosition="2" />
                 </screen>"""
        else:
            skin = """
                 <screen position="0,0" size="1920,1080" title="IPTV WORLD SPORT MOVIES        CHANNELS" flags="wfNoBorder" backgroundColor="#20000000">
                      <widget source="Title" render="Label" position="0,3" size="1920,32" zPosition="3" halign="center" valign="center" font="Regular;30" backgroundColor="#20000000" transparent="1" foregroundColor="#bab329" />      
                      <widget name="key_red" position="30,1030" size="130,40" backgroundColor="red" valign="center" halign="center" zPosition="2"  foregroundColor="white" font="Regular;33"/>
                      <widget name="key_green" position="170,1030" size="130,40" backgroundColor="green" valign="center" halign="center" zPosition="2"  foregroundColor="white" font="Regular;33"/>
                      <widget name="myMenu" position="5,40" size="1690,1000" foregroundColor="#FEFEFE" transparent="1" zPosition="2" />
                 </screen>"""

        def __init__(self, session, finishedCallback = None, picPath = None, args = 0):
                self.session = session
                Screen.__init__(self, session)
                self.finishedCallback = finishedCallback
                self.wget = "wget --no-check-certificate"
                list = []
                list.append(("  SPORT IPTV CHANNELS", "com_***"))
                list.append(("  RMC1 FHD", "com_001"))
                list.append(("  RMC2 FHD", "com_002"))
                list.append(("  RMC3 FHD", "com_003"))
                list.append(("  RMC4 FHD", "com_004"))          
                list.append(("  BEINSPORTS FR 1FHD", "com_005"))                
                list.append(("  BEINSPORTS FR 2FHD", "com_006"))
                list.append(("  BEINSPORTS FR 3FHD", "com_007"))                
                list.append(("  BEINSPORTS 1FHD", "com_01"))            
                list.append(("  BEINSPORTS 2FHD", "com_02"))
                list.append(("  BEINSPORTS 3FHD", "com_03"))
                list.append(("  BEINSPORTS 4FHD", "com_04"))            
                list.append(("  BEINSPORTS 5FHD", "com_05"))    
                list.append(("  BEINSPORTS 6FHD", "com_06"))
                list.append(("  BEINSPORTS 7FHD", "com_07"))            
                list.append(("  BEINSPORTS 8FHD", "com_08"))    
                list.append(("  BEINSPORTS 9FHD", "com_09"))
                list.append(("  BEINSPORTS 10FHD", "com_010"))  
                list.append(("  BEINSPORTS 11FHD", "com_011"))
                list.append(("  DAZN 1 BAR HD", "com_012"))     
                list.append(("  DAZN 2 BAR HD", "com_013"))
                list.append(("  LISTS IPTV SPORTS", "com_***")) 
                list.append(("  Bouquet counter 0", "com_0001"))
                list.append(("  Bouquet counter 20", "com_0002"))       
                list.append(("  Bouquet counter 50", "com_0003"))
                list.append(("  Bouquet counter 100", "com_0004")) 
                list.append(("  Bouquet counter ALL", "com_0005"))      
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
                list.append(("  IPTVFree097", "com_77"))
                list.append(("  IPTVFree098", "com_98"))
                list.append(("  IPTVFree099", "com_99"))
                list.append(("  IPTVFree100", "com_100"))
                list.append(("  IPTVFree101", "com_101"))
                list.append(("  IPTVFree102", "com_102"))
                list.append(("  IPTVFree103", "com_103"))
                list.append(("  IPTVFree104", "com_104"))  
                list.append(("  IPTVFree105", "com_105"))  
                list.append(("  IPTVFree106", "com_106"))
                list.append(("  IPTVFree107", "com_107"))  
                list.append(("  IPTVFree108", "com_108"))
                list.append(("  IPTVFree109", "com_109"))                 
                list.append(("  IPTVFree110", "com_110"))
                list.append(("  IPTVFree111", "com_111"))
                list.append(("  IPTVFree112", "com_112"))
                list.append(("  IPTVFree113", "com_113"))
                list.append(("  IPTVFree114", "com_114"))
                list.append(("  IPTVFree115", "com_115"))  
                list.append(("  IPTVFree116", "com_116"))  
                list.append(("  IPTVFree117", "com_117"))
                list.append(("  IPTVFree118", "com_118"))  
                list.append(("  IPTVFree119", "com_119"))
                list.append(("  IPTVFree120", "com_120")) 
                list.append(("  IPTVFree121", "com_121"))
                list.append(("  IPTVFree122", "com_122"))
                list.append(("  IPTVFree123", "com_123"))
                list.append(("  IPTVFree124", "com_124"))
                list.append(("  IPTVFree125", "com_125"))  
                list.append(("  IPTVFree126", "com_126"))  
                list.append(("  IPTVFree127", "com_127"))
                list.append(("  IPTVFree128", "com_128"))  
                list.append(("  IPTVFree129", "com_129"))
                list.append(("  IPTVFree130", "com_130")) 
                list.append(("  IPTVFree131", "com_131"))
                list.append(("  IPTVFree132", "com_132"))
                list.append(("  IPTVFree133", "com_133"))
                list.append(("  IPTVFree134", "com_134"))
                list.append(("  IPTVFree135", "com_135"))  
                list.append(("  IPTVFree136", "com_136"))  
                list.append(("  IPTVFree137", "com_137"))
                list.append(("  IPTVFree138", "com_138"))  
                list.append(("  IPTVFree139", "com_139"))
                list.append(("  IPTVFree140", "com_140")) 
                list.append(("  IPTVFree141", "com_141"))
                list.append(("  IPTVFree142", "com_142"))
                list.append(("  IPTVFree143", "com_143"))
                list.append(("  IPTVFree144", "com_144"))
                list.append(("  IPTVFree145", "com_145"))  
                list.append(("  IPTVFree146", "com_146"))  
                list.append(("  IPTVFree147", "com_147"))
                list.append(("  IPTVFree148", "com_148"))  
                list.append(("  IPTVFree149", "com_149"))
                list.append(("  IPTVFree150", "com_150"))                               
                list.append(("  ***** ARABE *****", "com_***"))
                list.append(("  Bouquet counter 0", "com_0151"))
                list.append(("  Bouquet counter 20", "com_0152"))       
                list.append(("  Bouquet counter 50", "com_0153"))
                list.append(("  Bouquet counter 100", "com_0154")) 
                list.append(("  Bouquet counter ALL", "com_0155"))                              
                list.append(("  IPTVWORLDAR001", "com_151"))
                list.append(("  IPTVWORLDAR002", "com_152"))    
                list.append(("  IPTVWORLDAR003", "com_153"))
                list.append(("  IPTVWORLDAR004", "com_154")) 
                list.append(("  IPTVWORLDAR005", "com_155"))
                list.append(("  IPTVWORLDAR006", "com_156"))
                list.append(("  IPTVWORLDAR007", "com_157"))
                list.append(("  IPTVWORLDAR008", "com_158"))
                list.append(("  IPTVWORLDAR009", "com_159"))
                list.append(("  IPTVWORLDAR010", "com_160"))
                list.append(("  IPTVWORLDAR011", "com_161"))
                list.append(("  IPTVWORLDAR012", "com_162"))  
                list.append(("  IPTVWORLDAR013", "com_163"))
                list.append(("  IPTVWORLDAR014", "com_164"))
                list.append(("  IPTVWORLDAR015", "com_165"))
                list.append(("  IPTVWORLDAR016", "com_166"))            
                list.append(("  IPTVWORLDAR017", "com_167"))
                list.append(("  IPTVWORLDAR018", "com_168"))
                list.append(("  IPTVWORLDAR019", "com_169"))
                list.append(("  IPTVWORLDAR020", "com_170"))
                list.append(("  IPTVWORLDAR021", "com_171"))
                list.append(("  IPTVWORLDAR022", "com_172"))
                list.append(("  IPTVWORLDAR023", "com_173"))
                list.append(("  IPTVWORLDAR024", "com_174"))
                list.append(("  IPTVWORLDAR025", "com_175"))
                list.append(("  IPTVWORLDAR026", "com_176"))
                list.append(("  IPTVWORLDAR027", "com_177"))
                list.append(("  IPTVWORLDAR028", "com_178"))
                list.append(("  IPTVWORLDAR029", "com_179"))
                list.append(("  IPTVWORLDAR030", "com_180"))
                list.append(("  IPTVWORLDAR031", "com_181"))
                list.append(("  IPTVWORLDAR032", "com_182"))
                list.append(("  IPTVWORLDAR033", "com_183"))
                list.append(("  IPTVWORLDAR034", "com_184"))
                list.append(("  IPTVWORLDAR035", "com_185"))
                list.append(("  IPTVWORLDAR036", "com_186"))
                list.append(("  IPTVWORLDAR037", "com_187"))
                list.append(("  IPTVWORLDAR038", "com_188"))
                list.append(("  IPTVWORLDAR039", "com_189"))
                list.append(("  IPTVWORLDAR040", "com_190"))
                list.append(("  IPTVWORLDAR041", "com_191"))
                list.append(("  IPTVWORLDAR042", "com_192"))
                list.append(("  IPTVWORLDAR043", "com_193"))
                list.append(("  IPTVWORLDAR044", "com_194"))  
                list.append(("  IPTVWORLDAR045", "com_195"))  
                list.append(("  IPTVWORLDAR046", "com_196"))
                list.append(("  IPTVWORLDAR047", "com_197"))  
                list.append(("  IPTVWORLDAR048", "com_198"))
                list.append(("  IPTVWORLDAR049", "com_199"))  
                list.append(("  IPTVWORLDAR050", "com_200"))
                list.append(("  IPTVWORLDAR051", "com_201"))
                list.append(("  IPTVWORLDAR052", "com_202"))    
                list.append(("  IPTVWORLDAR053", "com_203"))
                list.append(("  IPTVWORLDAR054", "com_204")) 
                list.append(("  IPTVWORLDAR055", "com_205"))
                list.append(("  IPTVWORLDAR056", "com_206"))
                list.append(("  IPTVWORLDAR057", "com_207"))
                list.append(("  IPTVWORLDAR058", "com_208"))
                list.append(("  IPTVWORLDAR059", "com_209"))
                list.append(("  IPTVWORLDAR060", "com_210"))
                list.append(("  IPTVWORLDAR061", "com_211"))
                list.append(("  IPTVWORLDAR062", "com_212"))  
                list.append(("  IPTVWORLDAR063", "com_213"))
                list.append(("  IPTVWORLDAR064", "com_214"))
                list.append(("  IPTVWORLDAR065", "com_215"))
                list.append(("  IPTVWORLDAR066", "com_216"))            
                list.append(("  IPTVWORLDAR067", "com_217"))
                list.append(("  IPTVWORLDAR068", "com_218"))
                list.append(("  IPTVWORLDAR069", "com_219"))
                list.append(("  IPTVWORLDAR070", "com_220"))
                list.append(("  IPTVWORLDAR071", "com_221"))
                list.append(("  IPTVWORLDAR072", "com_222"))
                list.append(("  IPTVWORLDAR073", "com_223"))
                list.append(("  IPTVWORLDAR074", "com_234"))
                list.append(("  IPTVWORLDAR075", "com_235"))
                list.append(("  IPTVWORLDAR076", "com_236"))
                list.append(("  IPTVWORLDAR077", "com_237"))
                list.append(("  IPTVWORLDAR078", "com_238"))
                list.append(("  IPTVWORLDAR079", "com_239"))
                list.append(("  IPTVWORLDAR080", "com_240"))
                list.append(("  IPTVWORLDAR081", "com_241"))
                list.append(("  IPTVWORLDAR082", "com_242"))
                list.append(("  IPTVWORLDAR083", "com_243"))
                list.append(("  IPTVWORLDAR084", "com_244"))
                list.append(("  IPTVWORLDAR085", "com_245"))
                list.append(("  IPTVWORLDAR086", "com_246"))
                list.append(("  IPTVWORLDAR087", "com_247"))
                list.append(("  IPTVWORLDAR088", "com_248"))
                list.append(("  IPTVWORLDAR089", "com_249"))
                list.append(("  IPTVWORLDAR090", "com_240"))
                list.append(("  IPTVWORLDAR091", "com_241"))
                list.append(("  IPTVWORLDAR092", "com_242"))
                list.append(("  IPTVWORLDAR093", "com_243"))
                list.append(("  IPTVWORLDAR094", "com_244"))  
                list.append(("  IPTVWORLDAR095", "com_245"))  
                list.append(("  IPTVWORLDAR096", "com_246"))
                list.append(("  IPTVWORLDAR097", "com_247"))  
                list.append(("  IPTVWORLDAR098", "com_248"))
                list.append(("  IPTVWORLDAR099", "com_249"))  
                list.append(("  IPTVWORLDAR100", "com_250"))
                list.append(("  ***** FRANCE INDEX1 *****", "com_***"))         
                list.append(("  IPTVWORLDFR001", "com_251"))
                list.append(("  IPTVWORLDFR002", "com_252"))    
                list.append(("  IPTVWORLDFR003", "com_253"))
                list.append(("  IPTVWORLDFR004", "com_254")) 
                list.append(("  IPTVWORLDFR005", "com_255"))
                list.append(("  IPTVWORLDFR006", "com_256"))
                list.append(("  ***** FRANCE INDEX2 *****", "com_***"))
                list.append(("  Bouquet counter 0", "com_0257"))
                list.append(("  Bouquet counter 20", "com_0258"))       
                list.append(("  Bouquet counter 50", "com_0259"))
                list.append(("  Bouquet counter 100", "com_0260")) 
                list.append(("  Bouquet counter ALL", "com_0261"))              
                list.append(("  IPTVWORLDFR001", "com_257"))
                list.append(("  IPTVWORLDFR002", "com_258"))
                list.append(("  IPTVWORLDFR003", "com_259"))
                list.append(("  IPTVWORLDFR004", "com_260"))
                list.append(("  IPTVWORLDFR005", "com_261"))
                list.append(("  IPTVWORLDFR006", "com_262"))  
                list.append(("  IPTVWORLDFR007", "com_263"))
                list.append(("  IPTVWORLDFR008", "com_264"))
                list.append(("  IPTVWORLDFR009", "com_265"))
                list.append(("  IPTVWORLDFR010", "com_266"))            
                list.append(("  IPTVWORLDFR011", "com_267"))
                list.append(("  IPTVWORLDFR012", "com_268"))
                list.append(("  IPTVWORLDFR013", "com_269"))
                list.append(("  IPTVWORLDFR014", "com_270"))
                list.append(("  IPTVWORLDFR015", "com_271"))
                list.append(("  IPTVWORLDFR016", "com_272"))            
                list.append(("  IPTVWORLDFR017", "com_273"))
                list.append(("  IPTVWORLDFR018", "com_274"))
                list.append(("  IPTVWORLDFR019", "com_275"))
                list.append(("  IPTVWORLDFR020", "com_276"))
                list.append(("  IPTVWORLDFR021", "com_277"))
                list.append(("  IPTVWORLDFR022", "com_278"))
                list.append(("  IPTVWORLDFR023", "com_279"))
                list.append(("  IPTVWORLDFR024", "com_280"))
                list.append(("  IPTVWORLDFR025", "com_281"))
                list.append(("  IPTVWORLDFR026", "com_282"))
                list.append(("  IPTVWORLDFR027", "com_283"))
                list.append(("  IPTVWORLDFR028", "com_284"))
                list.append(("  IPTVWORLDFR029", "com_285"))
                list.append(("  IPTVWORLDFR030", "com_286"))    
                list.append(("  IPTVWORLDFR031", "com_287"))
                list.append(("  IPTVWORLDFR032", "com_288"))
                list.append(("  IPTVWORLDFR033", "com_289"))
                list.append(("  IPTVWORLDFR034", "com_290"))
                list.append(("  IPTVWORLDFR035", "com_291"))
                list.append(("  IPTVWORLDFR036", "com_292"))
                list.append(("  IPTVWORLDFR037", "com_293"))
                list.append(("  IPTVWORLDFR038", "com_294"))
                list.append(("  IPTVWORLDFR039", "com_295"))
                list.append(("  IPTVWORLDFR040", "com_296"))    
                list.append(("  IPTVWORLDFR041", "com_297"))
                list.append(("  IPTVWORLDFR042", "com_298"))
                list.append(("  IPTVWORLDFR043", "com_299"))
                list.append(("  IPTVWORLDFR044", "com_300"))  
                list.append(("  IPTVWORLDFR045", "com_301"))  
                list.append(("  IPTVWORLDFR046", "com_302"))
                list.append(("  IPTVWORLDFR047", "com_303"))  
                list.append(("  IPTVWORLDFR048", "com_304"))
                list.append(("  IPTVWORLDFR049", "com_305"))  
                list.append(("  IPTVWORLDFR050", "com_306"))
                list.append(("  IPTVWORLDFR051", "com_307"))
                list.append(("  IPTVWORLDFR052", "com_308"))
                list.append(("  IPTVWORLDFR053", "com_309"))
                list.append(("  IPTVWORLDFR054", "com_310"))
                list.append(("  IPTVWORLDFR055", "com_311"))
                list.append(("  IPTVWORLDFR056", "com_312"))  
                list.append(("  IPTVWORLDFR057", "com_313"))
                list.append(("  IPTVWORLDFR058", "com_314"))
                list.append(("  IPTVWORLDFR059", "com_315"))
                list.append(("  IPTVWORLDFR060", "com_316"))            
                list.append(("  IPTVWORLDFR061", "com_317"))
                list.append(("  IPTVWORLDFR062", "com_318"))
                list.append(("  IPTVWORLDFR063", "com_319"))
                list.append(("  IPTVWORLDFR064", "com_320"))
                list.append(("  IPTVWORLDFR065", "com_321"))
                list.append(("  IPTVWORLDFR066", "com_322"))            
                list.append(("  IPTVWORLDFR067", "com_323"))
                list.append(("  IPTVWORLDFR068", "com_324"))
                list.append(("  IPTVWORLDFR069", "com_325"))
                list.append(("  IPTVWORLDFR070", "com_326"))
                list.append(("  IPTVWORLDFR071", "com_327"))
                list.append(("  IPTVWORLDFR072", "com_328"))
                list.append(("  IPTVWORLDFR073", "com_329"))
                list.append(("  IPTVWORLDFR074", "com_330"))
                list.append(("  IPTVWORLDFR075", "com_331"))
                list.append(("  IPTVWORLDFR076", "com_332"))
                list.append(("  IPTVWORLDFR077", "com_333"))
                list.append(("  IPTVWORLDFR078", "com_334"))
                list.append(("  IPTVWORLDFR079", "com_335"))
                list.append(("  IPTVWORLDFR080", "com_336"))    
                list.append(("  IPTVWORLDFR081", "com_337"))
                list.append(("  IPTVWORLDFR082", "com_338"))
                list.append(("  IPTVWORLDFR083", "com_339"))
                list.append(("  IPTVWORLDFR084", "com_340"))
                list.append(("  IPTVWORLDFR085", "com_341"))
                list.append(("  IPTVWORLDFR086", "com_342"))
                list.append(("  IPTVWORLDFR087", "com_343"))
                list.append(("  IPTVWORLDFR088", "com_344"))
                list.append(("  IPTVWORLDFR089", "com_345"))
                list.append(("  IPTVWORLDFR090", "com_346"))    
                list.append(("  IPTVWORLDFR091", "com_347"))
                list.append(("  IPTVWORLDFR092", "com_348"))
                list.append(("  IPTVWORLDFR093", "com_349"))
                list.append(("  IPTVWORLDFR094", "com_350"))  
                list.append(("  IPTVWORLDFR095", "com_351"))  
                list.append(("  IPTVWORLDFR096", "com_352"))
                list.append(("  IPTVWORLDFR097", "com_353"))  
                list.append(("  IPTVWORLDFR098", "com_354"))
                list.append(("  IPTVWORLDFR099", "com_355"))  
                list.append(("  IPTVWORLDFR100", "com_356"))            
                list.append(("  IPTVWORLDFR101", "com_357"))
                list.append(("  IPTVWORLDFR102", "com_358"))
                list.append(("  IPTVWORLDFR103", "com_359"))
                list.append(("  IPTVWORLDFR104", "com_360"))
                list.append(("  IPTVWORLDFR105", "com_361"))
                list.append(("  IPTVWORLDFR106", "com_362"))
                list.append(("  IPTVWORLDFR107", "com_363"))
                list.append(("  IPTVWORLDFR108", "com_364"))
                list.append(("  IPTVWORLDFR109", "com_365"))
                list.append(("  IPTVWORLDFR110", "com_366"))    
                list.append(("  IPTVWORLDFR111", "com_367"))
                list.append(("  IPTVWORLDFR112", "com_368"))
                list.append(("  IPTVWORLDFR113", "com_369"))
                list.append(("  IPTVWORLDFR114", "com_370"))  
                list.append(("  IPTVWORLDFR115", "com_371"))  
                list.append(("  IPTVWORLDFR116", "com_372"))
                list.append(("  IPTVWORLDFR117", "com_373"))  
                list.append(("  IPTVWORLDFR118", "com_374"))
                list.append(("  IPTVWORLDFR119", "com_375"))  
                list.append(("  IPTVWORLDFR120", "com_376"))
                list.append(("  ***** GREEK INDEX1 *****", "com_***"))               
                list.append(("  IPTVWORLDGR001", "com_377"))
                list.append(("  IPTVWORLDGR002", "com_378"))
                list.append(("  IPTVWORLDGR003", "com_379"))
                list.append(("  IPTVWORLDGR004", "com_380"))  
                list.append(("  IPTVWORLDGR005", "com_381"))
                list.append(("  ***** GREEK INDEX2 *****", "com_***"))
                list.append(("  Bouquet counter 0", "com_0382"))
                list.append(("  Bouquet counter 20", "com_0384"))       
                list.append(("  Bouquet counter 50", "com_0385")) 
                list.append(("  Bouquet counter ALL", "com_0386"))
                list.append(("  IPTVWORLDGR001", "com_382"))            
                list.append(("  IPTVWORLDGR002", "com_383"))  
                list.append(("  IPTVWORLDGR003", "com_384"))
                list.append(("  IPTVWORLDGR004", "com_385"))  
                list.append(("  IPTVWORLDGR005", "com_386"))
                list.append(("  IPTVWORLDGR006", "com_387"))
                list.append(("  IPTVWORLDGR007", "com_388"))  
                list.append(("  IPTVWORLDGR008", "com_389"))
                list.append(("  IPTVWORLDGR009", "com_390"))  
                list.append(("  IPTVWORLDGR010", "com_391"))
                list.append(("  IPTVWORLDGR011", "com_392"))            
                list.append(("  IPTVWORLDGR012", "com_393"))  
                list.append(("  IPTVWORLDGR013", "com_394"))
                list.append(("  IPTVWORLDGR014", "com_395"))  
                list.append(("  IPTVWORLDGR015", "com_396"))
                list.append(("  IPTVWORLDGR016", "com_397"))
                list.append(("  IPTVWORLDGR017", "com_398"))  
                list.append(("  IPTVWORLDGR018", "com_399"))
                list.append(("  IPTVWORLDGR019", "com_400"))  
                list.append(("  IPTVWORLDGR020", "com_401"))    
                list.append(("  IPTVWORLDGR021", "com_402"))  
                list.append(("  IPTVWORLDGR022", "com_403"))
                list.append(("  IPTVWORLDGR023", "com_404"))  
                list.append(("  IPTVWORLDGR024", "com_405"))
                list.append(("  IPTVWORLDGR025", "com_406"))
                list.append(("  IPTVWORLDGR026", "com_407"))  
                list.append(("  IPTVWORLDGR027", "com_408"))
                list.append(("  IPTVWORLDGR028", "com_409"))  
                list.append(("  IPTVWORLDGR029", "com_410"))    
                list.append(("  IPTVWORLDGR030", "com_411"))  
                list.append(("  IPTVWORLDGR031", "com_412"))
                list.append(("  IPTVWORLDGR032", "com_413"))  
                list.append(("  IPTVWORLDGR033", "com_414"))
                list.append(("  IPTVWORLDGR034", "com_415"))
                list.append(("  IPTVWORLDGR035", "com_416"))  
                list.append(("  IPTVWORLDGR036", "com_417"))
                list.append(("  IPTVWORLDGR037", "com_418"))  
                list.append(("  IPTVWORLDGR038", "com_419"))    
                list.append(("  IPTVWORLDGR039", "com_420"))  
                list.append(("  IPTVWORLDGR040", "com_421"))
                list.append(("  IPTVWORLDGR041", "com_422"))  
                list.append(("  IPTVWORLDGR042", "com_423"))
                list.append(("  IPTVWORLDGR043", "com_424"))
                list.append(("  IPTVWORLDGR044", "com_425"))  
                list.append(("  IPTVWORLDGR045", "com_426"))
                list.append(("  IPTVWORLDGR046", "com_427"))  
                list.append(("  IPTVWORLDGR047", "com_428")) 
                list.append(("  IPTVWORLDGR048", "com_429"))  
                list.append(("  IPTVWORLDGR049", "com_430"))
                list.append(("  IPTVWORLDGR050", "com_431"))
                list.append(("  ***** USA INDEX1 *****", "com_***")) 
                list.append(("  IPTVWORLDUS001", "com_432"))
                list.append(("  IPTVWORLDUS002", "com_433"))
                list.append(("  IPTVWORLDUS003", "com_434"))
                list.append(("  IPTVWORLDUS004", "com_435"))  
                list.append(("  IPTVWORLDUS005", "com_436"))
                list.append(("  IPTVWORLDUS005", "com_436"))  
                list.append(("  IPTVWORLDUS006", ""))                               
                list.append(("  ***** USA INDEX2 *****", "com_***"))
                list.append(("  Bouquet counter 10", "com_0438")) 
                list.append(("  Bouquet counter 20", "com_0439"))    
                list.append(("  Bouquet counter 50", "com_0440")) 
                list.append(("  Bouquet counter 50", "com_0441")) 
                list.append(("  IPTVWORLDUS001", "com_438"))
                list.append(("  IPTVWORLDUS002", "com_439"))
                list.append(("  IPTVWORLDUS003", "com_440"))
                list.append(("  IPTVWORLDUS004", "com_441"))  
                list.append(("  IPTVWORLDUS005", "com_442"))  
                list.append(("  IPTVWORLDUS006", "com_443"))
                list.append(("  IPTVWORLDUS007", "com_444"))  
                list.append(("  IPTVWORLDUS008", "com_445"))
                list.append(("  IPTVWORLDUS009", "com_446"))  
                list.append(("  IPTVWORLDUS010", "com_447"))
                list.append(("  IPTVWORLDUS011", "com_448"))
                list.append(("  IPTVWORLDUS012", "com_449"))    
                list.append(("  IPTVWORLDUS013", "com_450"))
                list.append(("  IPTVWORLDUS014", "com_451")) 
                list.append(("  IPTVWORLDUS015", "com_452"))
                list.append(("  IPTVWORLDUS016", "com_453"))
                list.append(("  IPTVWORLDUS017", "com_454"))
                list.append(("  IPTVWORLDUS018", "com_455"))
                list.append(("  IPTVWORLDUS019", "com_456"))
                list.append(("  IPTVWORLDUS020", "com_457"))
                list.append(("  IPTVWORLDUS021", "com_458"))
                list.append(("  IPTVWORLDUS022", "com_459"))
                list.append(("  IPTVWORLDUS023", "com_460"))
                list.append(("  IPTVWORLDUS024", "com_461"))  
                list.append(("  IPTVWORLDUS025", "com_462"))  
                list.append(("  IPTVWORLDUS026", "com_463"))
                list.append(("  IPTVWORLDUS027", "com_464"))  
                list.append(("  IPTVWORLDUS028", "com_465"))
                list.append(("  IPTVWORLDUS029", "com_466"))  
                list.append(("  IPTVWORLDUS030", "com_467"))
                list.append(("  IPTVWORLDUS031", "com_468"))
                list.append(("  IPTVWORLDUS032", "com_469"))    
                list.append(("  IPTVWORLDUS033", "com_470"))
                list.append(("  IPTVWORLDUS034", "com_471")) 
                list.append(("  IPTVWORLDUS035", "com_472"))
                list.append(("  IPTVWORLDUS036", "com_473"))
                list.append(("  IPTVWORLDUS037", "com_474"))
                list.append(("  IPTVWORLDUS038", "com_475"))
                list.append(("  IPTVWORLDUS039", "com_476"))
                list.append(("  IPTVWORLDUS040", "com_477"))
                list.append(("  IPTVWORLDUS041", "com_478"))
                list.append(("  IPTVWORLDUS042", "com_479"))
                list.append(("  IPTVWORLDUS043", "com_480"))
                list.append(("  IPTVWORLDUS044", "com_481"))  
                list.append(("  IPTVWORLDUS045", "com_482"))  
                list.append(("  IPTVWORLDUS046", "com_483"))
                list.append(("  IPTVWORLDUS047", "com_484"))  
                list.append(("  IPTVWORLDUS048", "com_485"))
                list.append(("  IPTVWORLDUS049", "com_486"))  
                list.append(("  IPTVWORLDUS050", "com_487"))
                list.append(("  IPTVWORLDUS051", "com_488"))
                list.append(("  IPTVWORLDUS052", "com_489"))    
                list.append(("  IPTVWORLDUS053", "com_490"))
                list.append(("  IPTVWORLDUS054", "com_491")) 
                list.append(("  IPTVWORLDUS055", "com_492"))
                list.append(("  IPTVWORLDUS056", "com_493"))
                list.append(("  IPTVWORLDUS057", "com_494"))
                list.append(("  IPTVWORLDUS058", "com_495"))
                list.append(("  IPTVWORLDUS059", "com_496"))
                list.append(("  IPTVWORLDUS060", "com_497"))
                list.append(("  IPTVWORLDUS061", "com_499"))
                list.append(("  IPTVWORLDUS062", "com_500"))
                list.append(("  IPTVWORLDUS063", "com_501"))
                list.append(("  IPTVWORLDUS064", "com_502"))  
                list.append(("  IPTVWORLDUS065", "com_503"))  
                list.append(("  IPTVWORLDUS066", "com_504"))
                list.append(("  IPTVWORLDUS067", "com_505"))  
                list.append(("  IPTVWORLDUS068", "com_506"))
                list.append(("  IPTVWORLDUS069", "com_507"))  
                list.append(("  IPTVWORLDUS070", "com_508"))
                list.append(("  IPTVWORLDUS071", "com_509"))
                list.append(("  IPTVWORLDUS072", "com_510"))    
                list.append(("  IPTVWORLDUS073", "com_511"))
                list.append(("  IPTVWORLDUS074", "com_512")) 
                list.append(("  IPTVWORLDUS075", "com_513"))
                list.append(("  IPTVWORLDUS076", "com_514"))
                list.append(("  IPTVWORLDUS077", "com_515"))
                list.append(("  IPTVWORLDUS078", "com_516"))
                list.append(("  IPTVWORLDUS079", "com_517"))
                list.append(("  IPTVWORLDUS080", "com_518"))            
                list.append(("  IPTVWORLDUS081", "com_519"))
                list.append(("  IPTVWORLDUS082", "com_520"))
                list.append(("  IPTVWORLDUS083", "com_521"))
                list.append(("  IPTVWORLDUS084", "com_522"))  
                list.append(("  IPTVWORLDUS085", "com_523"))  
                list.append(("  IPTVWORLDUS086", "com_524"))
                list.append(("  IPTVWORLDUS087", "com_525"))  
                list.append(("  IPTVWORLDUS088", "com_526"))
                list.append(("  IPTVWORLDUS089", "com_527"))  
                list.append(("  IPTVWORLDUS090", "com_528"))
                list.append(("  IPTVWORLDUS091", "com_529"))
                list.append(("  IPTVWORLDUS092", "com_530"))    
                list.append(("  IPTVWORLDUS093", "com_531"))
                list.append(("  IPTVWORLDUS094", "com_532")) 
                list.append(("  IPTVWORLDUS095", "com_533"))
                list.append(("  IPTVWORLDUS096", "com_534"))
                list.append(("  IPTVWORLDUS097", "com_535"))
                list.append(("  IPTVWORLDUS098", "com_536"))
                list.append(("  IPTVWORLDUS099", "com_537"))
                list.append(("  IPTVWORLDUS100", "com_538"))
                list.append(("  IPTVWORLDUS101", "com_539"))
                list.append(("  IPTVWORLDUS102", "com_540"))
                list.append(("  IPTVWORLDUS103", "com_541"))
                list.append(("  IPTVWORLDUS104", "com_542"))  
                list.append(("  IPTVWORLDUS105", "com_543"))  
                list.append(("  IPTVWORLDUS106", "com_544"))
                list.append(("  IPTVWORLDUS107", "com_545"))  
                list.append(("  IPTVWORLDUS108", "com_546"))
                list.append(("  IPTVWORLDUS109", "com_547"))  
                list.append(("  IPTVWORLDUS110", "com_548"))
                list.append(("  IPTVWORLDUS111", "com_549"))
                list.append(("  IPTVWORLDUS112", "com_550"))    
                list.append(("  IPTVWORLDUS113", "com_551"))
                list.append(("  IPTVWORLDUS114", "com_552")) 
                list.append(("  IPTVWORLDUS115", "com_553"))
                list.append(("  IPTVWORLDUS116", "com_554"))
                list.append(("  IPTVWORLDUS117", "com_555"))
                list.append(("  IPTVWORLDUS118", "com_556"))
                list.append(("  IPTVWORLDUS119", "com_557"))
                list.append(("  IPTVWORLDUS120", "com_558"))            
                list.append(("  IPTVWORLDUS121", "com_559"))
                list.append(("  IPTVWORLDUS122", "com_560"))
                list.append(("  IPTVWORLDUS123", "com_561"))
                list.append(("  IPTVWORLDUS124", "com_562"))  
                list.append(("  IPTVWORLDUS125", "com_563"))  
                list.append(("  IPTVWORLDUS126", "com_564"))
                list.append(("  IPTVWORLDUS127", "com_565"))  
                list.append(("  IPTVWORLDUS128", "com_566"))
                list.append(("  IPTVWORLDUS129", "com_567"))  
                list.append(("  IPTVWORLDUS130", "com_568"))
                list.append(("  IPTVWORLDUS131", "com_569"))
                list.append(("  IPTVWORLDUS132", "com_570"))    
                list.append(("  IPTVWORLDUS133", "com_571"))
                list.append(("  IPTVWORLDUS134", "com_572")) 
                list.append(("  IPTVWORLDUS135", "com_573"))
                list.append(("  IPTVWORLDUS136", "com_574"))
                list.append(("  IPTVWORLDUS137", "com_575"))
                list.append(("  IPTVWORLDUS138", "com_576"))
                list.append(("  IPTVWORLDUS139", "com_577"))
                list.append(("  IPTVWORLDUS140", "com_578"))
                list.append(("  IPTVWORLDUS141", "com_579"))
                list.append(("  IPTVWORLDUS142", "com_580"))
                list.append(("  IPTVWORLDUS143", "com_581"))
                list.append(("  IPTVWORLDUS144", "com_582"))  
                list.append(("  IPTVWORLDUS145", "com_583"))  
                list.append(("  IPTVWORLDUS146", "com_584"))
                list.append(("  IPTVWORLDUS147", "com_585"))  
                list.append(("  IPTVWORLDUS148", "com_586"))
                list.append(("  IPTVWORLDUS149", "com_587"))  
                list.append(("  IPTVWORLDUS150", "com_588"))
                list.append(("  ***** WORLD BOUQUET INDEX1 *****", "com_***")) 
                list.append(("  Bouquet counter 100", "com_589"))
                list.append(("  Bouquet counter 50", "com_590"))
                list.append(("  Bouquet counter 20", "com_591"))
                list.append(("  Bouquet counter 10", "com_592"))                               
                list.append(("  ***** NETHERLANDS INDEX2 *****", "com_***"))
                list.append(("  Bouquet counter 50", "com_593"))
                list.append(("  IPTVWORLDNL002", "com_594"))
                list.append(("  IPTVWORLDNL003", "com_595"))
                list.append(("  IPTVWORLDNL004", "com_596"))  
                list.append(("  IPTVWORLDNL005", "com_597"))  
                list.append(("  IPTVWORLDNL006", "com_598"))
                list.append(("  IPTVWORLDNL007", "com_599"))  
                list.append(("  IPTVWORLDNL008", "com_600"))
                list.append(("  IPTVWORLDNL009", "com_601"))  
                list.append(("  IPTVWORLDNL010", "com_602"))
                list.append(("  IPTVWORLDNL011", "com_603"))
                list.append(("  IPTVWORLDNL012", "com_604"))    
                list.append(("  IPTVWORLDNL013", "com_605"))
                list.append(("  IPTVWORLDNL014", "com_606")) 
                list.append(("  IPTVWORLDNL015", "com_607"))
                list.append(("  IPTVWORLDNL016", "com_608"))
                list.append(("  IPTVWORLDNL017", "com_609"))
                list.append(("  IPTVWORLDNL018", "com_610"))
                list.append(("  IPTVWORLDNL019", "com_611"))
                list.append(("  IPTVWORLDNL020", "com_612"))
                list.append(("  IPTVWORLDNL021", "com_613"))
                list.append(("  IPTVWORLDNL022", "com_615"))
                list.append(("  IPTVWORLDNL023", "com_616"))
                list.append(("  IPTVWORLDNL024", "com_617"))  
                list.append(("  IPTVWORLDNL025", "com_618"))  
                list.append(("  IPTVWORLDNL026", "com_619"))
                list.append(("  IPTVWORLDNL027", "com_620"))  
                list.append(("  IPTVWORLDNL028", "com_621"))
                list.append(("  IPTVWORLDNL029", "com_622"))  
                list.append(("  IPTVWORLDNL030", "com_623"))
                list.append(("  IPTVWORLDNL031", "com_624"))
                list.append(("  IPTVWORLDNL032", "com_625"))    
                list.append(("  IPTVWORLDNL033", "com_626"))
                list.append(("  IPTVWORLDNL034", "com_627")) 
                list.append(("  IPTVWORLDNL035", "com_628"))
                list.append(("  IPTVWORLDNL036", "com_629"))
                list.append(("  IPTVWORLDNL037", "com_630"))
                list.append(("  IPTVWORLDNL038", "com_631"))
                list.append(("  IPTVWORLDNL039", "com_632"))
                list.append(("  IPTVWORLDNL040", "com_633"))
                list.append(("  IPTVWORLDNL041", "com_634"))
                list.append(("  IPTVWORLDNL042", "com_635"))
                list.append(("  IPTVWORLDNL043", "com_636"))
                list.append(("  IPTVWORLDNL044", "com_637"))  
                list.append(("  IPTVWORLDNL045", "com_638"))  
                list.append(("  IPTVWORLDNL046", "com_639"))
                list.append(("  IPTVWORLDNL047", "com_640"))  
                list.append(("  IPTVWORLDNL048", "com_641"))
                list.append(("  IPTVWORLDNL049", "com_642"))  
                list.append(("  IPTVWORLDNL050", "com_643"))
                list.append(("  ***** ITALIAN  INDEX2 *****", "com_***"))
                list.append(("  Bouquet counter 10", "com_644"))
                list.append(("  Bouquet counter 20", "com_0645"))
                list.append(("  Bouquet counter 50", "com_0646"))       
                list.append(("  Bouquet counter 100", "com_0647"))      
                list.append(("  IPTVWORLDIT001", "com_645"))
                list.append(("  IPTVWORLDIT002", "com_646"))    
                list.append(("  IPTVWORLDIT003", "com_647"))
                list.append(("  IPTVWORLDIT004", "com_648")) 
                list.append(("  IPTVWORLDIT005", "com_649"))
                list.append(("  IPTVWORLDIT006", "com_650"))
                list.append(("  IPTVWORLDIT007", "com_651"))
                list.append(("  IPTVWORLDIT008", "com_652"))
                list.append(("  IPTVWORLDIT009", "com_653"))
                list.append(("  IPTVWORLDIT010", "com_654"))
                list.append(("  IPTVWORLDIT011", "com_655"))
                list.append(("  IPTVWORLDIT012", "com_656"))
                list.append(("  IPTVWORLDIT013", "com_657"))
                list.append(("  IPTVWORLDIT014", "com_658"))  
                list.append(("  IPTVWORLDIT015", "com_659"))  
                list.append(("  IPTVWORLDIT016", "com_660"))
                list.append(("  IPTVWORLDIT017", "com_661"))  
                list.append(("  IPTVWORLDIT018", "com_662"))
                list.append(("  IPTVWORLDIT019", "com_663"))  
                list.append(("  IPTVWORLDIT020", "com_664"))
                list.append(("  IPTVWORLDIT021", "com_665"))
                list.append(("  IPTVWORLDIT022", "com_666"))    
                list.append(("  IPTVWORLDIT023", "com_667"))
                list.append(("  IPTVWORLDIT024", "com_668")) 
                list.append(("  IPTVWORLDIT025", "com_669"))
                list.append(("  IPTVWORLDIT026", "com_670"))
                list.append(("  IPTVWORLDIT027", "com_671"))
                list.append(("  IPTVWORLDIT028", "com_672"))
                list.append(("  IPTVWORLDIT029", "com_673"))
                list.append(("  IPTVWORLDIT030", "com_674"))            
                list.append(("  IPTVWORLDIT031", "com_675"))
                list.append(("  IPTVWORLDIT032", "com_676"))
                list.append(("  IPTVWORLDIT033", "com_677"))
                list.append(("  IPTVWORLDIT034", "com_678"))  
                list.append(("  IPTVWORLDIT035", "com_679"))  
                list.append(("  IPTVWORLDIT036", "com_680"))
                list.append(("  IPTVWORLDIT037", "com_681"))  
                list.append(("  IPTVWORLDIT038", "com_682"))
                list.append(("  IPTVWORLDIT039", "com_683"))  
                list.append(("  IPTVWORLDIT040", "com_684"))
                list.append(("  IPTVWORLDIT041", "com_685"))
                list.append(("  IPTVWORLDIT042", "com_686"))    
                list.append(("  IPTVWORLDIT043", "com_687"))
                list.append(("  IPTVWORLDIT044", "com_688")) 
                list.append(("  IPTVWORLDIT045", "com_689"))
                list.append(("  IPTVWORLDIT046", "com_690"))
                list.append(("  IPTVWORLDIT047", "com_691"))
                list.append(("  IPTVWORLDIT048", "com_692"))
                list.append(("  IPTVWORLDIT049", "com_693"))
                list.append(("  IPTVWORLDIT050", "com_694"))            
                list.append(("  IPTVWORLDIT051", "com_695"))
                list.append(("  IPTVWORLDIT052", "com_696"))    
                list.append(("  IPTVWORLDIT053", "com_697"))
                list.append(("  IPTVWORLDIT054", "com_698")) 
                list.append(("  IPTVWORLDIT055", "com_699"))
                list.append(("  IPTVWORLDIT056", "com_700"))
                list.append(("  IPTVWORLDIT057", "com_701"))
                list.append(("  IPTVWORLDIT058", "com_702"))
                list.append(("  IPTVWORLDIT059", "com_703"))
                list.append(("  IPTVWORLDIT060", "com_704"))
                list.append(("  IPTVWORLDIT061", "com_705"))
                list.append(("  IPTVWORLDIT062", "com_706"))
                list.append(("  IPTVWORLDIT063", "com_707"))
                list.append(("  IPTVWORLDIT064", "com_708"))  
                list.append(("  IPTVWORLDIT065", "com_709"))  
                list.append(("  IPTVWORLDIT066", "com_710"))
                list.append(("  IPTVWORLDIT067", "com_711"))  
                list.append(("  IPTVWORLDIT068", "com_712"))
                list.append(("  IPTVWORLDIT069", "com_713"))  
                list.append(("  IPTVWORLDIT070", "com_714"))
                list.append(("  IPTVWORLDIT071", "com_715"))
                list.append(("  IPTVWORLDIT072", "com_716"))    
                list.append(("  IPTVWORLDIT073", "com_717"))
                list.append(("  IPTVWORLDIT074", "com_718")) 
                list.append(("  IPTVWORLDIT075", "com_719"))
                list.append(("  IPTVWORLDIT076", "com_720"))
                list.append(("  IPTVWORLDIT077", "com_721"))
                list.append(("  IPTVWORLDIT078", "com_722"))
                list.append(("  IPTVWORLDIT079", "com_723"))
                list.append(("  IPTVWORLDIT080", "com_724"))            
                list.append(("  IPTVWORLDIT081", "com_725"))
                list.append(("  IPTVWORLDIT082", "com_726"))
                list.append(("  IPTVWORLDIT083", "com_727"))
                list.append(("  IPTVWORLDIT084", "com_728"))  
                list.append(("  IPTVWORLDIT085", "com_729"))  
                list.append(("  IPTVWORLDIT086", "com_730"))
                list.append(("  IPTVWORLDIT087", "com_731"))  
                list.append(("  IPTVWORLDIT088", "com_732"))
                list.append(("  IPTVWORLDIT089", "com_733"))  
                list.append(("  IPTVWORLDIT090", "com_734"))
                list.append(("  IPTVWORLDIT091", "com_735"))
                list.append(("  IPTVWORLDIT092", "com_736"))    
                list.append(("  IPTVWORLDIT093", "com_737"))
                list.append(("  IPTVWORLDIT094", "com_738")) 
                list.append(("  IPTVWORLDIT095", "com_739"))
                list.append(("  IPTVWORLDIT096", "com_740"))
                list.append(("  IPTVWORLDIT097", "com_741"))
                list.append(("  IPTVWORLDIT098", "com_742"))
                list.append(("  IPTVWORLDIT099", "com_743"))
                list.append(("  IPTVWORLDIT100", "com_744"))
                list.append(("  ***** RUSSE *****", "com_***")) 
                list.append(("  Bouquet counter 20", "com_0745"))
                list.append(("  IPTVWORLDRU001", "com_745"))
                list.append(("  IPTVWORLDRU002", "com_746"))
                list.append(("  IPTVWORLDRU003", "com_747"))
                list.append(("  IPTVWORLDRU004", "com_748"))  
                list.append(("  IPTVWORLDRU005", "com_749"))  
                list.append(("  IPTVWORLDRU006", "com_750"))
                list.append(("  IPTVWORLDRU007", "com_751"))  
                list.append(("  IPTVWORLDRU008", "com_752"))
                list.append(("  IPTVWORLDRU009", "com_753"))  
                list.append(("  IPTVWORLDRU010", "com_754"))
                list.append(("  IPTVWORLDRU011", "com_755"))
                list.append(("  IPTVWORLDRU012", "com_756"))    
                list.append(("  IPTVWORLDRU013", "com_757"))
                list.append(("  IPTVWORLDRU014", "com_758")) 
                list.append(("  IPTVWORLDRU015", "com_759"))
                list.append(("  IPTVWORLDRU016", "com_760"))
                list.append(("  IPTVWORLDRU017", "com_761"))
                list.append(("  IPTVWORLDRU018", "com_762"))
                list.append(("  IPTVWORLDRU019", "com_763"))
                list.append(("  IPTVWORLDRU020", "com_764"))                            
                list.append(("  ***** TURKE *****", "com_***"))
                list.append(("  Bouquet counter 20", "com_0765"))
                list.append(("  IPTVWORLDTR001", "com_765"))
                list.append(("  IPTVWORLDTR002", "com_766"))
                list.append(("  IPTVWORLDTR003", "com_767"))
                list.append(("  IPTVWORLDTR004", "com_768"))  
                list.append(("  IPTVWORLDTR005", "com_769"))  
                list.append(("  IPTVWORLDTR006", "com_770"))
                list.append(("  IPTVWORLDTR007", "com_771"))  
                list.append(("  IPTVWORLDTR008", "com_772"))
                list.append(("  IPTVWORLDTR009", "com_773"))  
                list.append(("  IPTVWORLDTR010", "com_774"))
                list.append(("  IPTVWORLDTR011", "com_775"))
                list.append(("  IPTVWORLDTR012", "com_776"))    
                list.append(("  IPTVWORLDTR013", "com_777"))
                list.append(("  IPTVWORLDTR014", "com_778")) 
                list.append(("  IPTVWORLDTR015", "com_779"))
                list.append(("  IPTVWORLDTR016", "com_780"))
                list.append(("  IPTVWORLDTR017", "com_781"))
                list.append(("  IPTVWORLDTR018", "com_782"))
                list.append(("  IPTVWORLDTR019", "com_783"))
                list.append(("  IPTVWORLDTR020", "com_784"))
                list.append(("  ***** POLAND *****", "com_***"))
                list.append(("  Bouquet counter 10", "com_0785")) 
                list.append(("  Bouquet counter 20", "com_0786"))    
                list.append(("  Bouquet counter 50", "com_0787")) 
                list.append(("  IPTVWORDLPL001", "com_785"))
                list.append(("  IPTVWORLDPL002", "com_786"))    
                list.append(("  IPTVWORLDPL003", "com_787"))
                list.append(("  IPTVWORLDPL004", "com_788")) 
                list.append(("  IPTVWORLDPL005", "com_789"))
                list.append(("  IPTVWORLDPL006", "com_790"))
                list.append(("  IPTVWORLDPL007", "com_791"))
                list.append(("  IPTVWORLDPL008", "com_792"))
                list.append(("  IPTVWORLDPL009", "com_793"))
                list.append(("  IPTVWORLDPL010", "com_794"))
                list.append(("  IPTVWORLDPL011", "com_795"))
                list.append(("  IPTVWORLDPL012", "com_796"))
                list.append(("  IPTVWORLDPL013", "com_797"))
                list.append(("  IPTVWORLDPL014", "com_798"))  
                list.append(("  IPTVWORLDPL015", "com_799"))  
                list.append(("  IPTVWORLDPL016", "com_800"))
                list.append(("  IPTVWORLDPL017", "com_801"))  
                list.append(("  IPTVWORLDPL018", "com_802"))
                list.append(("  IPTVWORLDPL019", "com_803"))  
                list.append(("  IPTVWORLDPL020", "com_804"))
                list.append(("  IPTVWORLDPL021", "com_805"))
                list.append(("  IPTVWORLDPL022", "com_806"))    
                list.append(("  IPTVWORLDPL023", "com_807"))
                list.append(("  IPTVWORLDPL024", "com_808")) 
                list.append(("  IPTVWORLDPL025", "com_809"))
                list.append(("  IPTVWORLDPL026", "com_810"))
                list.append(("  IPTVWORLDPL027", "com_811"))
                list.append(("  IPTVWORLDPL028", "com_812"))
                list.append(("  IPTVWORLDPL029", "com_813"))
                list.append(("  IPTVWORLDPL030", "com_814"))                                     
                list.append(("  IPTVWORLDPL031", "com_815"))
                list.append(("  IPTVWORLDPL032", "com_816"))    
                list.append(("  IPTVWORLDPL033", "com_817"))
                list.append(("  IPTVWORLDPL034", "com_818")) 
                list.append(("  IPTVWORLDPL035", "com_819"))
                list.append(("  IPTVWORLDPL036", "com_820"))
                list.append(("  IPTVWORLDPL037", "com_821"))
                list.append(("  IPTVWORLDPL038", "com_822"))
                list.append(("  IPTVWORLDPL039", "com_823"))
                list.append(("  IPTVWORLDPL040", "com_824"))
                list.append(("  IPTVWORLDPL041", "com_825"))
                list.append(("  IPTVWORLDPL042", "com_826"))  
                list.append(("  IPTVWORLDPL043", "com_827"))
                list.append(("  IPTVWORLDPL044", "com_828"))
                list.append(("  IPTVWORLDPL045", "com_829"))
                list.append(("  IPTVWORLDPL046", "com_830"))            
                list.append(("  IPTVWORLDPL047", "com_831"))
                list.append(("  IPTVWORLDPL048", "com_832"))
                list.append(("  IPTVWORLDPL049", "com_833"))
                list.append(("  IPTVWORLDPL050", "com_834"))
                list.append(("  ***** PORTUGUAL *****", "com_***"))
                list.append(("  Bouquet counter 10", "com_0835")) 
                list.append(("  Bouquet counter 20", "com_0836"))    
                list.append(("  Bouquet counter 50", "com_0867"))       
                list.append(("  IPTVWORLDPO001", "com_835"))
                list.append(("  IPTVWORLDPO002", "com_836"))
                list.append(("  IPTVWORLDPO003", "com_837"))
                list.append(("  IPTVWORLDPO004", "com_838"))
                list.append(("  IPTVWORLDPO005", "com_839"))
                list.append(("  IPTVWORLDPO006", "com_840"))
                list.append(("  IPTVWORLDPO007", "com_841"))
                list.append(("  IPTVWORLDPO008", "com_842"))
                list.append(("  IPTVWORLDPO009", "com_843"))
                list.append(("  IPTVWORLDPO010", "com_844"))
                list.append(("  IPTVWORLDPO011", "com_845"))
                list.append(("  IPTVWORLDPO012", "com_846"))
                list.append(("  IPTVWORLDPO013", "com_847"))
                list.append(("  IPTVWORLDPO014", "com_848"))
                list.append(("  IPTVWORLDPO015", "com_849"))
                list.append(("  IPTVWORLDPO016", "com_850"))
                list.append(("  IPTVWORLDPO017", "com_851"))
                list.append(("  IPTVWORLDPO018", "com_852"))
                list.append(("  IPTVWORLDPO019", "com_853"))
                list.append(("  IPTVWORLDPO020", "com_854"))
                list.append(("  IPTVWORLDPO021", "com_855"))
                list.append(("  IPTVWORLDPO022", "com_856"))
                list.append(("  IPTVWORLDPO023", "com_857"))
                list.append(("  IPTVWORLDPO024", "com_858"))  
                list.append(("  IPTVWORLDPO025", "com_859"))  
                list.append(("  IPTVWORLDPO026", "com_860"))
                list.append(("  IPTVWORLDPO027", "com_861"))  
                list.append(("  IPTVWORLDPO028", "com_862"))
                list.append(("  IPTVWORLDPO029", "com_863"))  
                list.append(("  IPTVWORLDPO030", "com_864")) 
                list.append(("  IPTVWORLDPO031", "com_866"))
                list.append(("  IPTVWORLDPO032", "com_867"))  
                list.append(("  IPTVWORLDPO033", "com_868"))
                list.append(("  IPTVWORLDPO034", "com_869"))
                list.append(("  IPTVWORLDPO035", "com_870"))
                list.append(("  IPTVWORLDPO036", "com_871"))            
                list.append(("  IPTVWORLDPO037", "com_872"))
                list.append(("  IPTVWORLDPO038", "com_873"))
                list.append(("  IPTVWORLDPO039", "com_874"))
                list.append(("  IPTVWORLDPO040", "com_875"))                            
                list.append(("  IPTVWORLDPO041", "com_876"))
                list.append(("  IPTVWORLDPO042", "com_877"))  
                list.append(("  IPTVWORLDPO043", "com_878"))
                list.append(("  IPTVWORLDPO044", "com_879"))
                list.append(("  IPTVWORLDPO045", "com_880"))
                list.append(("  IPTVWORLDPO046", "com_881"))            
                list.append(("  IPTVWORLDPO047", "com_882"))
                list.append(("  IPTVWORLDPO048", "com_883"))
                list.append(("  IPTVWORLDPO049", "com_884"))
                list.append(("  IPTVWORLDPO050", "com_885"))
                list.append(("  ***** ENGLAND *****", "com_***"))
                list.append(("  Bouquet counter 10", "com_0886")) 
                list.append(("  Bouquet counter 20", "com_0887"))    
                list.append(("  Bouquet counter 50", "com_0888"))                       
                list.append(("  IPTVWORLDUK001", "com_886"))
                list.append(("  IPTVWORLDUK002", "com_887"))
                list.append(("  IPTVWORLDUK003", "com_888"))
                list.append(("  IPTVWORLDUK004", "com_889"))
                list.append(("  IPTVWORLDUK005", "com_890"))
                list.append(("  IPTVWORLDUK006", "com_891"))
                list.append(("  IPTVWORLDUK007", "com_892"))
                list.append(("  IPTVWORLDUK008", "com_893"))
                list.append(("  IPTVWORLDUK009", "com_894"))
                list.append(("  IPTVWORLDUK010", "com_895"))
                list.append(("  IPTVWORLDUK011", "com_896")) 
                list.append(("  IPTVWORLDUK012", "com_897"))
                list.append(("  IPTVWORLDUK013", "com_898"))
                list.append(("  IPTVWORLDUK014", "com_899"))
                list.append(("  IPTVWORLDUK015", "com_900"))
                list.append(("  IPTVWORLDUK016", "com_901"))  
                list.append(("  IPTVWORLDUK017", "com_902"))  
                list.append(("  IPTVWORLDUK018", "com_903"))
                list.append(("  IPTVWORLDUK019", "com_904"))  
                list.append(("  IPTVWORLDUK020", "com_905"))
                list.append(("  IPTVWORLDUK021", "com_906"))                             
                list.append(("  IPTVWORLDUK022", "com_907"))
                list.append(("  IPTVWORLDUK023", "com_908"))
                list.append(("  IPTVWORLDUK024", "com_909"))  
                list.append(("  IPTVWORLDUK025", "com_910"))
                list.append(("  IPTVWORLDUK026", "com_911"))  
                list.append(("  IPTVWORLDUK027", "com_912"))
                list.append(("  IPTVWORLDUK028", "com_913"))                             
                list.append(("  IPTVWORLDUK029", "com_914"))
                list.append(("  IPTVWORLDUK030", "com_915"))
                list.append(("  IPTVWORLDUK031", "com_916"))
                list.append(("  IPTVWORLDUK032", "com_917"))  
                list.append(("  IPTVWORLDUK033", "com_918"))
                list.append(("  IPTVWORLDUK034", "com_919"))
                list.append(("  IPTVWORLDUK035", "com_920"))
                list.append(("  IPTVWORLDUK036", "com_921"))            
                list.append(("  IPTVWORLDUK037", "com_922"))
                list.append(("  IPTVWORLDUK038", "com_923"))
                list.append(("  IPTVWORLDUK039", "com_924"))
                list.append(("  IPTVWORLDUK040", "com_925"))                            
                list.append(("  IPTVWORLDUK041", "com_926"))
                list.append(("  IPTVWORLDUK042", "com_927"))  
                list.append(("  IPTVWORLDUK043", "com_928"))
                list.append(("  IPTVWORLDUK044", "com_929"))
                list.append(("  IPTVWORLDUK045", "com_930"))
                list.append(("  IPTVWORLDUK046", "com_931"))            
                list.append(("  IPTVWORLDUK047", "com_932"))
                list.append(("  IPTVWORLDUK048", "com_933"))
                list.append(("  IPTVWORLDUK049", "com_934"))
                list.append(("  IPTVWORLDUK050", "com_935"))
                list.append(("  ***** SPAN *****", "com_***"))
                list.append(("  Bouquet counter 10", "com_0936")) 
                list.append(("  Bouquet counter 20", "com_0937"))    
                list.append(("  Bouquet counter 50", "com_0938"))               
                list.append(("  IPTVWORLDES001", "com_936")) 
                list.append(("  IPTVWORLDES002", "com_937"))
                list.append(("  IPTVWORLDES003", "com_938"))
                list.append(("  IPTVWORLDES004", "com_939"))
                list.append(("  IPTVWORLDES005", "com_940"))
                list.append(("  IPTVWORLDES006", "com_941"))  
                list.append(("  IPTVWORLDES007", "com_942"))  
                list.append(("  IPTVWORLDES008", "com_943"))
                list.append(("  IPTVWORLDES009", "com_944"))  
                list.append(("  IPTVWORLDES010", "com_945"))
                list.append(("  IPTVWORLDES011", "com_946")) 
                list.append(("  IPTVWORLDES012", "com_947"))
                list.append(("  IPTVWORLDES013", "com_948"))
                list.append(("  IPTVWORLDES014", "com_949"))
                list.append(("  IPTVWORLDES015", "com_950"))
                list.append(("  IPTVWORLDES016", "com_951"))  
                list.append(("  IPTVWORLDES017", "com_952"))  
                list.append(("  IPTVWORLDES018", "com_953"))
                list.append(("  IPTVWORLDES019", "com_954"))  
                list.append(("  IPTVWORLDES020", "com_955"))
                list.append(("  IPTVWORLDES021", "com_956"))                             
                list.append(("  IPTVWORLDES022", "com_957"))
                list.append(("  IPTVWORLDES023", "com_958"))
                list.append(("  IPTVWORLDES024", "com_959"))  
                list.append(("  IPTVWORLDES025", "com_960"))
                list.append(("  IPTVWORLDES026", "com_961"))  
                list.append(("  IPTVWORLDES027", "com_962"))
                list.append(("  IPTVWORLDES028", "com_963"))                             
                list.append(("  IPTVWORLDES029", "com_964"))
                list.append(("  IPTVWORLDES030", "com_965"))
                list.append(("  IPTVWORLDES031", "com_966"))
                list.append(("  IPTVWORLDES032", "com_967"))  
                list.append(("  IPTVWORLDES033", "com_968"))
                list.append(("  IPTVWORLDES034", "com_969"))
                list.append(("  IPTVWORLDES035", "com_970"))
                list.append(("  IPTVWORLDES036", "com_971"))            
                list.append(("  IPTVWORLDES037", "com_972"))
                list.append(("  IPTVWORLDES038", "com_973"))
                list.append(("  IPTVWORLDES039", "com_974"))
                list.append(("  IPTVWORLDES040", "com_925"))                            
                list.append(("  IPTVWORLDES041", "com_976"))
                list.append(("  IPTVWORLDES042", "com_977"))  
                list.append(("  IPTVWORLDES043", "com_978"))
                list.append(("  IPTVWORLDES044", "com_979"))
                list.append(("  IPTVWORLDES045", "com_980"))
                list.append(("  IPTVWORLDES046", "com_981"))            
                list.append(("  IPTVWORLDES047", "com_982"))
                list.append(("  IPTVWORLDES048", "com_983"))
                list.append(("  IPTVWORLDES049", "com_984"))
                list.append(("  IPTVWORLDES050", "com_985"))            
                list.append(("  ***** ALBANIA *****", "com_***"))
                list.append(("  Bouquet counter 20", "com_0986"))    
                list.append(("  Bouquet counter 50", "com_0987")) 
                list.append(("  Bouquet counter 100", "com_0988"))                  
                list.append(("  Bouquet counter 100", "com_0989"))              
                list.append(("  IPTVWORLDAL001", "com_986"))
                list.append(("  IPTVWORLDAL002", "com_987"))
                list.append(("  IPTVWORLDAL003", "com_988"))
                list.append(("  IPTVWORLDAL004", "com_989"))  
                list.append(("  IPTVWORLDAL005", "com_990"))  
                list.append(("  IPTVWORLDAL006", "com_991"))
                list.append(("  IPTVWORLDAL007", "com_992"))  
                list.append(("  IPTVWORLDAL008", "com_993"))
                list.append(("  IPTVWORLDAL009", "com_994"))  
                list.append(("  IPTVWORLDAL010", "com_995"))            
                list.append(("  IPTVWORLDAL011", "com_996"))
                list.append(("  IPTVWORLDAL012", "com_997"))
                list.append(("  IPTVWORLDAL013", "com_998"))
################################################################################
                list.append(("  ***** SPORT INDEX2 *****", "com_***")) 
                list.append(("  Bouquet counter 10", "com_999"))
                list.append(("  IPTVWORLDSP001", "com_1000"))
                list.append(("  IPTVWORLDSP002", "com_1001"))
                list.append(("  IPTVWORLDSP003", "com_1002"))
                list.append(("  IPTVWORLDSP004", "com_1003"))  
                list.append(("  IPTVWORLDSP005", "com_1004"))  
                list.append(("  IPTVWORLDSP006", "com_1005"))
                list.append(("  IPTVWORLDSP007", "com_1006"))
                list.append(("  ***** ARABE INDEX2 *****", "com_***")) 
                list.append(("  Bouquet counter 10", "com_1007"))
                list.append(("  IPTVWORLDAR001", "com_1008"))
                list.append(("  IPTVWORLDAR002", "com_1009"))
                list.append(("  IPTVWORLDAR003", "com_1010"))
                list.append(("  IPTVWORLDAR004", "com_1011"))  
                list.append(("  IPTVWORLDAR005", "com_1012"))  
                list.append(("  IPTVWORLDAR006", "com_1013"))
                list.append(("  IPTVWORLDAR007", "com_1014"))  
                list.append(("  IPTVWORLDAR008", "com_1015"))
                list.append(("  IPTVWORLDAR009", "com_1016"))  
                list.append(("  IPTVWORLDAR010", "com_1017"))
                list.append(("  ***** FRANCE INDEX2 *****", "com_***"))
                list.append(("  Bouquet counter 10", "com_1018"))
                list.append(("  IPTVWORLDFR001", "com_1019"))   
                list.append(("  IPTVWORLDFR002", "com_1020"))
                list.append(("  IPTVWORLDFR003", "com_1021")) 
                list.append(("  IPTVWORLDFR004", "com_1022"))
                list.append(("  IPTVWORLDFR005", "com_1023"))
                list.append(("  IPTVWORLDFR006", "com_1024"))
                list.append(("  IPTVWORLDFR007", "com_1025"))
                list.append(("  IPTVWORLDFR008", "com_1026"))
                list.append(("  IPTVWORLDFR009", "com_1027"))
                list.append(("  IPTVWORLDFR010", "com_1028"))
                list.append(("  ***** WORLD BOUQUET INDEX2 *****", "com_***")) 
                list.append(("  Bouquet counter 100", "com_1029"))
                list.append(("  Bouquet counter 50", "com_1030"))
                list.append(("  Bouquet counter 20", "com_1031"))
                list.append(("  Bouquet counter 10", "com_1032"))                               
                list.append(("  ***** SPORT INDEX3 *****", "com_***"))
                list.append(("  IPTVWORLDSP001", "com_1033"))
                list.append(("  ***** ARABE INDEX3 *****", "com_***"))
                list.append(("  IPTVWORLDAR001", "com_1034"))
                list.append(("  ***** FRANCE INDEX3 *****", "com_***"))
                list.append(("  IPTVWORLDFR001", "com_1035"))
                list.append(("  ***** USA INDEX3 *****", "com_***"))
                list.append(("  IPTVWORLDUS001", "com_1036"))
                list.append(("  ***** GERMANY INDEX3 *****", "com_***"))
                list.append(("  IPTVWORLDGR001", "com_1037"))
                list.append(("  ***** TURK INDEX3 *****", "com_***"))
                list.append(("  IPTVWORLDTU001", "com_1038"))
                list.append(("  ***** ITALIE INDEX3 *****", "com_***"))
                list.append(("  IPTVWORLDIT001", "com_1039"))
                list.append(("  ***** SPAN INDEX3 *****", "com_***"))
                list.append(("  IPTVWORLDES001", "com_1040"))
                list.append(("  ***** ALL IPTV INDEX3 *****", "com_***"))
                list.append(("  IPTVWORLDUALL001", "com_1041"))
                list.append(("  ***** GERMANY *****", "com_***"))
                list.append(("  Bouquet counter 10", "com_01042")) 
                list.append(("  Bouquet counter 20", "com_01043"))    
                list.append(("  Bouquet counter 50", "com_01044")) 
                list.append(("  Bouquet counter 100", "com_01045")) 
                list.append(("  IPTVWORLDDE001", "com_1042"))
                list.append(("  IPTVWORLDDE002", "com_1043"))   
                list.append(("  IPTVWORLDDE003", "com_1044"))
                list.append(("  IPTVWORLDDE004", "com_1045")) 
                list.append(("  IPTVWORLDDE005", "com_1046"))
                list.append(("  IPTVWORLDDE006", "com_1047"))
                list.append(("  IPTVWORLDDE007", "com_1048"))
                list.append(("  IPTVWORLDDE008", "com_1049"))
                list.append(("  IPTVWORLDDE009", "com_1050"))
                list.append(("  IPTVWORLDDE010", "com_1051"))
                list.append(("  IPTVWORLDDE011", "com_1052"))
                list.append(("  IPTVWORLDDE012", "com_1053"))
                list.append(("  IPTVWORLDDE013", "com_1054"))
                list.append(("  IPTVWORLDDE014", "com_1055"))  
                list.append(("  IPTVWORLDDE015", "com_1056"))  
                list.append(("  IPTVWORLDDE016", "com_1057"))
                list.append(("  IPTVWORLDDE017", "com_1058"))  
                list.append(("  IPTVWORLDDE018", "com_1059"))
                list.append(("  IPTVWORLDDE019", "com_1060"))  
                list.append(("  IPTVWORLDDE020", "com_1061"))
                list.append(("  IPTVWORLDDE021", "com_1062"))
                list.append(("  IPTVWORLDDE022", "com_1063"))   
                list.append(("  IPTVWORLDDE023", "com_1064"))
                list.append(("  IPTVWORLDDE024", "com_1065")) 
                list.append(("  IPTVWORLDDE025", "com_1066"))
                list.append(("  IPTVWORLDDE026", "com_1067"))
                list.append(("  IPTVWORLDDE027", "com_1068"))
                list.append(("  IPTVWORLDDE028", "com_1069"))
                list.append(("  IPTVWORLDDE029", "com_1070"))
                list.append(("  IPTVWORLDDE030", "com_1071"))
                list.append(("  IPTVWORLDDE031", "com_1072"))
                list.append(("  IPTVWORLDDE032", "com_1073"))
                list.append(("  IPTVWORLDDE033", "com_1074"))
                list.append(("  IPTVWORLDDE034", "com_1075"))  
                list.append(("  IPTVWORLDDE035", "com_1076"))  
                list.append(("  IPTVWORLDDE036", "com_1077"))
                list.append(("  IPTVWORLDDE037", "com_1078"))  
                list.append(("  IPTVWORLDDE038", "com_1079"))
                list.append(("  IPTVWORLDDE039", "com_1080"))  
                list.append(("  IPTVWORLDDE040", "com_1081"))
                list.append(("  IPTVWORLDDE041", "com_1082"))
                list.append(("  IPTVWORLDDE042", "com_1083"))   
                list.append(("  IPTVWORLDDE043", "com_1084"))
                list.append(("  IPTVWORLDDE044", "com_1085")) 
                list.append(("  IPTVWORLDDE045", "com_1086"))
                list.append(("  IPTVWORLDDE046", "com_1087"))
                list.append(("  IPTVWORLDDE047", "com_1088"))
                list.append(("  IPTVWORLDDE048", "com_1089"))
                list.append(("  IPTVWORLDDE049", "com_1090"))
                list.append(("  IPTVWORLDDE050", "com_1091"))
                list.append(("  ***** BRAZIL *****", "com_***"))
                list.append(("  Bouquet counter 10", "com_01092")) 
                list.append(("  Bouquet counter 20", "com_01093"))    
                list.append(("  Bouquet counter 50", "com_01094")) 
                list.append(("  Bouquet counter 100", "com_01095"))             
                list.append(("  IPTVWORLDBR001", "com_1092"))
                list.append(("  IPTVWORLDBR002", "com_1093"))
                list.append(("  IPTVWORLDBR003", "com_1094"))
                list.append(("  IPTVWORLDBR004", "com_1095"))  
                list.append(("  IPTVWORLDBR005", "com_1096"))  
                list.append(("  IPTVWORLDBR006", "com_1097"))
                list.append(("  IPTVWORLDBR007", "com_1098"))  
                list.append(("  IPTVWORLDBR008", "com_1099"))
                list.append(("  IPTVWORLDBR009", "com_1100"))
                list.append(("  IPTVWORLDBR010", "com_1101"))
                list.append(("  IPTVWORLDBR011", "com_1102"))
                list.append(("  IPTVWORLDBR012", "com_1103"))   
                list.append(("  IPTVWORLDBR013", "com_1104"))
                list.append(("  IPTVWORLDBR014", "com_1105")) 
                list.append(("  IPTVWORLDBR015", "com_1106"))
                list.append(("  IPTVWORLDBR016", "com_1107"))
                list.append(("  IPTVWORLDBR017", "com_1108"))
                list.append(("  IPTVWORLDBR018", "com_1109"))
                list.append(("  IPTVWORLDBR019", "com_1110"))
                list.append(("  IPTVWORLDBR020", "com_1111"))
                list.append(("  IPTVWORLDBR021", "com_1112"))
                list.append(("  IPTVWORLDBR022", "com_1113"))
                list.append(("  IPTVWORLDBR023", "com_1114"))
                list.append(("  IPTVWORLDBR024", "com_1115"))  
                list.append(("  IPTVWORLDBR025", "com_1116"))  
                list.append(("  IPTVWORLDBR026", "com_1117"))
                list.append(("  IPTVWORLDBR027", "com_1118"))  
                list.append(("  IPTVWORLDBR028", "com_1119"))
                list.append(("  IPTVWORLDBR029", "com_1120"))  
                list.append(("  IPTVWORLDBR030", "com_1121"))
                list.append(("  IPTVWORLDBR031", "com_1122"))
                list.append(("  IPTVWORLDBR032", "com_1123"))   
                list.append(("  IPTVWORLDBR033", "com_1124"))
                list.append(("  IPTVWORLDBR034", "com_1125")) 
                list.append(("  IPTVWORLDBR035", "com_1126"))
                list.append(("  IPTVWORLDBR036", "com_1127"))
                list.append(("  IPTVWORLDBR037", "com_1128"))
                list.append(("  IPTVWORLDBR038", "com_1129"))
                list.append(("  IPTVWORLDBR039", "com_1130"))
                list.append(("  IPTVWORLDBR040", "com_1131"))           
                list.append(("  IPTVWORLDBR041", "com_1132"))
                list.append(("  IPTVWORLDBR042", "com_1133"))
                list.append(("  IPTVWORLDBR043", "com_1134"))
                list.append(("  IPTVWORLDBR044", "com_1135"))  
                list.append(("  IPTVWORLDBR045", "com_1136"))  
                list.append(("  IPTVWORLDBR046", "com_1137"))
                list.append(("  IPTVWORLDBR047", "com_1138"))  
                list.append(("  IPTVWORLDBR048", "com_1139"))
                list.append(("  IPTVWORLDBR049", "com_1140"))  
                list.append(("  IPTVWORLDBR050", "com_1141"))   
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
                    return '[New Update Avilable]'

        def install(self, *retval):
            os.system("%s https://ia600702.us.archive.org/26/items/dreamosat/freecc4.sh -qO - | /bin/sh" % self.wget)
            self.session.openWithCallback(self.restartenigma, MessageBox, _('** Nedd Restart Enigma2 To Load New Update ?!! **'), MessageBox.TYPE_YESNO, timeout=10)
### End EDit
        def go(self):
                from Plugins.Extensions.FreeServer.outils.Console3 import Console3
                returnValue = self["myMenu"].l.getCurrentSelection()[1]
                if returnValue != None:         
                        if returnValue =="com_001":
                            self.RMCHD1()
                        elif returnValue =="com_002":
                            self.RMCHD2()
                        elif returnValue =="com_003":
                            self.RMCHD3()
                        elif returnValue =="com_004":
                            self.RMCHD4()
                        elif returnValue =="com_005":
                            self.BeinFRHD1()
                        elif returnValue =="com_006":
                            self.BeinFRHD2()                        
                        elif returnValue =="com_007":
                            self.BeinFRHD3()                        
                        elif returnValue =="com_01":
                            self.BeinHD1()
                        elif returnValue =="com_02":
                            self.BeinHD2()
                        elif returnValue =="com_03":
                            self.BeinHD3()
                        elif returnValue =="com_04":
                            self.BeinHD4()
                        elif returnValue =="com_05":
                            self.BeinHD5()
                        elif returnValue =="com_06":
                            self.BeinHD6()
                        elif returnValue =="com_07":
                            self.BeinHD7()
                        elif returnValue =="com_08":
                            self.BeinHD8()
                        elif returnValue =="com_09":
                            self.BeinHD9()
                        elif returnValue =="com_010":
                            self.BeinHD10()
                        elif returnValue =="com_011":
                            self.BeinHD11()
                        elif returnValue =="com_012":
                            self.DAZN1HD()
                        elif returnValue =="com_013": 
                            self.DAZN2HD()
                        elif returnValue =="com_0001":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia601405.us.archive.org/33/items/freeiptv_201911/FreeIPTVN0.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='Free IPTVFree001', cmdlist=cmdlist, finishedCallback=None)
                        elif returnValue =="com_0002":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia601405.us.archive.org/33/items/freeiptv_201911/FreeIPTVN20.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='Free IPTVFree002', cmdlist=cmdlist, finishedCallback=None)
                        elif returnValue =="com_0003":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia601405.us.archive.org/33/items/freeiptv_201911/FreeIPTVN50.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='Free IPTVFree003', cmdlist=cmdlist, finishedCallback=None)
                        elif returnValue =="com_0004":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'") 
                                cmdlist.append("%s https://ia601405.us.archive.org/33/items/freeiptv_201911/FreeIPTVN100.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='Free IPTVFree004', cmdlist=cmdlist, finishedCallback=None)
                        elif returnValue =="com_0005":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia601405.us.archive.org/33/items/freeiptv_201911/FreeIPTVNALL.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='Free IPTVFree005', cmdlist=cmdlist, finishedCallback=None)
                        elif returnValue =="com_1":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia601405.us.archive.org/33/items/freeiptv_201911/FreeIPTV001.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='Free IPTVFree001', cmdlist=cmdlist, finishedCallback=None)
                        elif returnValue =="com_2":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia601405.us.archive.org/33/items/freeiptv_201911/FreeIPTV002.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='Free IPTVFree002', cmdlist=cmdlist, finishedCallback=None)
                        elif returnValue =="com_3":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia601405.us.archive.org/33/items/freeiptv_201911/FreeIPTV003.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='Free IPTVFree003', cmdlist=cmdlist, finishedCallback=None)
                        elif returnValue =="com_4":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'") 
                                cmdlist.append("%s https://ia601405.us.archive.org/33/items/freeiptv_201911/FreeIPTV004.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='Free IPTVFree004', cmdlist=cmdlist, finishedCallback=None)
                        elif returnValue =="com_5":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia601405.us.archive.org/33/items/freeiptv_201911/FreeIPTV005.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='Free IPTVFree005', cmdlist=cmdlist, finishedCallback=None)
                        elif returnValue =="com_6":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia601405.us.archive.org/33/items/freeiptv_201911/FreeIPTV006.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='Free IPTVFree006', cmdlist=cmdlist, finishedCallback=None)
                        elif returnValue =="com_7":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia601405.us.archive.org/33/items/freeiptv_201911/FreeIPTV007.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='Free IPTVFree007', cmdlist=cmdlist, finishedCallback=None)
                        elif returnValue =="com_8":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")    
                                cmdlist.append("%s https://ia601405.us.archive.org/33/items/freeiptv_201911/FreeIPTV008.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='Free IPTVFree008', cmdlist=cmdlist, finishedCallback=None)
                        elif returnValue =="com_9":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia601405.us.archive.org/33/items/freeiptv_201911/FreeIPTV009.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='Free IPTVFree009', cmdlist=cmdlist, finishedCallback=None)
                        elif returnValue =="com_10":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia601405.us.archive.org/33/items/freeiptv_201911/FreeIPTV010.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='Free IPTVFree010', cmdlist=cmdlist, finishedCallback=None)
                        elif returnValue =="com_11":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia601405.us.archive.org/33/items/freeiptv_201911/FreeIPTV011.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='Free IPTVFree011', cmdlist=cmdlist, finishedCallback=None)
                        elif returnValue =="com_12":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia601405.us.archive.org/33/items/freeiptv_201911/FreeIPTV012.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='Free IPTVFree012', cmdlist=cmdlist, finishedCallback=None)
                        elif returnValue =="com_13":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia601405.us.archive.org/33/items/freeiptv_201911/FreeIPTV013.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='Free IPTVFree013', cmdlist=cmdlist, finishedCallback=None)
                        elif returnValue =="com_14":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia601405.us.archive.org/33/items/freeiptv_201911/FreeIPTV014.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='Free IPTVFree014', cmdlist=cmdlist, finishedCallback=None)
                        elif returnValue =="com_15":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia601405.us.archive.org/33/items/freeiptv_201911/FreeIPTV015.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='Free IPTVFree015', cmdlist=cmdlist, finishedCallback=None)
                        elif returnValue =="com_16":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia601405.us.archive.org/33/items/freeiptv_201911/FreeIPTV016.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='Free IPTVFree016', cmdlist=cmdlist, finishedCallback=None)
                        elif returnValue =="com_17":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia601405.us.archive.org/33/items/freeiptv_201911/FreeIPTV017.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='Free IPTVFree017', cmdlist=cmdlist, finishedCallback=None)
                        elif returnValue =="com_18":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia601405.us.archive.org/33/items/freeiptv_201911/FreeIPTV018.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='Free IPTVFree018', cmdlist=cmdlist, finishedCallback=None)
                        elif returnValue =="com_19":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia601405.us.archive.org/33/items/freeiptv_201911/FreeIPTV019.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='Free IPTVFree019', cmdlist=cmdlist, finishedCallback=None)
                        elif returnValue =="com_20":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia601405.us.archive.org/33/items/freeiptv_201911/FreeIPTV020.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='Free IPTVFree020', cmdlist=cmdlist, finishedCallback=None)
                        elif returnValue =="com_21":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia601405.us.archive.org/33/items/freeiptv_201911/FreeIPTV021.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='Free IPTVFree021', cmdlist=cmdlist, finishedCallback=None)
                        elif returnValue =="com_22":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia601405.us.archive.org/33/items/freeiptv_201911/FreeIPTV022.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='Free IPTVFree022', cmdlist=cmdlist, finishedCallback=None)
                        elif returnValue =="com_23":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia601405.us.archive.org/33/items/freeiptv_201911/FreeIPTV023.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='Free IPTVFree023', cmdlist=cmdlist, finishedCallback=None)
                        elif returnValue =="com_24":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia601405.us.archive.org/33/items/freeiptv_201911/FreeIPTV024.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='Free IPTVFree024', cmdlist=cmdlist, finishedCallback=None)
                        elif returnValue =="com_25":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia601405.us.archive.org/33/items/freeiptv_201911/FreeIPTV025.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='Free IPTVFree025', cmdlist=cmdlist, finishedCallback=None)
                        elif returnValue =="com_26":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia601405.us.archive.org/33/items/freeiptv_201911/FreeIPTV026.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='Free IPTVFree026', cmdlist=cmdlist, finishedCallback=None)
                        elif returnValue =="com_27":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia601405.us.archive.org/33/items/freeiptv_201911/FreeIPTV027.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='Free IPTVFree027', cmdlist=cmdlist, finishedCallback=None)
                        elif returnValue =="com_28":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia601405.us.archive.org/33/items/freeiptv_201911/FreeIPTV028.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='Free IPTVFree028', cmdlist=cmdlist, finishedCallback=None)
                        elif returnValue =="com_29":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia601405.us.archive.org/33/items/freeiptv_201911/FreeIPTV029.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='Free IPTVFree029', cmdlist=cmdlist, finishedCallback=None)
                        elif returnValue =="com_30":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia601405.us.archive.org/33/items/freeiptv_201911/FreeIPTV030.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='Free IPTVFree030', cmdlist=cmdlist, finishedCallback=None)
                        elif returnValue =="com_31":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia601405.us.archive.org/33/items/freeiptv_201911/FreeIPTV031.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='Free IPTVFree031', cmdlist=cmdlist, finishedCallback=None)
                        elif returnValue =="com_32":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia601405.us.archive.org/33/items/freeiptv_201911/FreeIPTV032.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='Free IPTVFree032', cmdlist=cmdlist, finishedCallback=None)
                        elif returnValue =="com_33":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia601405.us.archive.org/33/items/freeiptv_201911/FreeIPTV033.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='Free IPTVFree033', cmdlist=cmdlist, finishedCallback=None)
                        elif returnValue =="com_34":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia601405.us.archive.org/33/items/freeiptv_201911/FreeIPTV034.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='Free IPTVFree034', cmdlist=cmdlist, finishedCallback=None)
                        elif returnValue =="com_35":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia601405.us.archive.org/33/items/freeiptv_201911/FreeIPTV035.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='Free IPTVFree035', cmdlist=cmdlist, finishedCallback=None)
                        elif returnValue =="com_36":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia601405.us.archive.org/33/items/freeiptv_201911/FreeIPTV036.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='Free IPTVFree036', cmdlist=cmdlist, finishedCallback=None)
                        elif returnValue =="com_37":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia601405.us.archive.org/33/items/freeiptv_201911/FreeIPTV037.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='Free IPTVFree037', cmdlist=cmdlist, finishedCallback=None)
                        elif returnValue =="com_38":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia601405.us.archive.org/33/items/freeiptv_201911/FreeIPTV038.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='Free IPTVFree038', cmdlist=cmdlist, finishedCallback=None)
                        elif returnValue =="com_39":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia601405.us.archive.org/33/items/freeiptv_201911/FreeIPTV039.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='Free IPTVFree039', cmdlist=cmdlist, finishedCallback=None)
                        elif returnValue =="com_40":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia601405.us.archive.org/33/items/freeiptv_201911/FreeIPTV040.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='Free IPTVFree040', cmdlist=cmdlist, finishedCallback=None)
                        elif returnValue =="com_41":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia601405.us.archive.org/33/items/freeiptv_201911/FreeIPTV041.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='Free IPTVFree041', cmdlist=cmdlist, finishedCallback=None)
                        elif returnValue =="com_42":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia601501.us.archive.org/12/items/freeiptv001/FreeIPTV042.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='Free IPTVFree042', cmdlist=cmdlist, finishedCallback=None)
                        elif returnValue =="com_43":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia601501.us.archive.org/12/items/freeiptv001/FreeIPTV043.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='Free IPTVFree043', cmdlist=cmdlist, finishedCallback=None)
                        elif returnValue =="com_44":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia601501.us.archive.org/12/items/freeiptv001/FreeIPTV044.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='Free IPTVFree044', cmdlist=cmdlist, finishedCallback=None)
                        elif returnValue =="com_45":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia601405.us.archive.org/33/items/freeiptv_201911/FreeIPTV045.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='Free IPTVFree045', cmdlist=cmdlist, finishedCallback=None)
                        elif returnValue =="com_46":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia601405.us.archive.org/33/items/freeiptv_201911/FreeIPTV046.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='Free IPTVFree046', cmdlist=cmdlist, finishedCallback=None)
                        elif returnValue =="com_47":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia601501.us.archive.org/12/items/freeiptv001/FreeIPTV047.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='Free IPTVFree047', cmdlist=cmdlist, finishedCallback=None)
                        elif returnValue =="com_48":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia601405.us.archive.org/33/items/freeiptv_201911/FreeIPTV048.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='Free IPTVFree048', cmdlist=cmdlist, finishedCallback=None)
                        elif returnValue =="com_49":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia601405.us.archive.org/33/items/freeiptv_201911/FreeIPTV049.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='Free IPTVFree049', cmdlist=cmdlist, finishedCallback=None)
                        elif returnValue =="com_50":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia601405.us.archive.org/33/items/freeiptv_201911/FreeIPTV050.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='Free IPTVFree050', cmdlist=cmdlist, finishedCallback=None)
                        elif returnValue =="com_51":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia601405.us.archive.org/33/items/freeiptv_201911/FreeIPTV051.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='Free IPTVFree051', cmdlist=cmdlist, finishedCallback=None)
                        elif returnValue =="com_052":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia601405.us.archive.org/33/items/freeiptv_201911/FreeIPTV052.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='Free IPTVFree052', cmdlist=cmdlist, finishedCallback=None)
                        elif returnValue =="com_53":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia601405.us.archive.org/33/items/freeiptv_201911/FreeIPTV053.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='Free IPTVFree053', cmdlist=cmdlist, finishedCallback=None)
                        elif returnValue =="com_54":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia601405.us.archive.org/33/items/freeiptv_201911/FreeIPTV054.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='Free IPTVFree054', cmdlist=cmdlist, finishedCallback=None)
                        elif returnValue =="com_55":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia601405.us.archive.org/33/items/freeiptv_201911/FreeIPTV055.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='Free IPTVFree055', cmdlist=cmdlist, finishedCallback=None)
                        elif returnValue =="com_56":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia601405.us.archive.org/33/items/freeiptv_201911/FreeIPTV056.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='Free IPTVFree056', cmdlist=cmdlist, finishedCallback=None)
                        elif returnValue =="com_57":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia601405.us.archive.org/33/items/freeiptv_201911/FreeIPTV057.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='Free IPTVFree057', cmdlist=cmdlist, finishedCallback=None)
                        elif returnValue =="com_58":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia601405.us.archive.org/33/items/freeiptv_201911/FreeIPTV058.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='Free IPTVFree058', cmdlist=cmdlist, finishedCallback=None)
                        elif returnValue =="com_59":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia601405.us.archive.org/33/items/freeiptv_201911/FreeIPTV059.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='Free IPTVFree059', cmdlist=cmdlist, finishedCallback=None)
                        elif returnValue =="com_60":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia601405.us.archive.org/33/items/freeiptv_201911/FreeIPTV060.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='Free IPTVFree060', cmdlist=cmdlist, finishedCallback=None)
                        elif returnValue =="com_61":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia601405.us.archive.org/33/items/freeiptv_201911/FreeIPTV061.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='Free IPTVFree061', cmdlist=cmdlist, finishedCallback=None)
                        elif returnValue =="com_62":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia601405.us.archive.org/33/items/freeiptv_201911/FreeIPTV062.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='Free IPTVFree062', cmdlist=cmdlist, finishedCallback=None)
                        elif returnValue =="com_63":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia601405.us.archive.org/33/items/freeiptv_201911/FreeIPTV063.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='Free IPTVFree063', cmdlist=cmdlist, finishedCallback=None)
                        elif returnValue =="com_64":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'") 
                                cmdlist.append("%s https://ia601405.us.archive.org/33/items/freeiptv_201911/FreeIPTV064.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='Free IPTVFree064', cmdlist=cmdlist, finishedCallback=None)
                        elif returnValue =="com_65":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia601405.us.archive.org/33/items/freeiptv_201911/FreeIPTV065.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='Free IPTVFree065', cmdlist=cmdlist, finishedCallback=None)
                        elif returnValue =="com_66":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia601405.us.archive.org/33/items/freeiptv_201911/FreeIPTV066.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='Free IPTVFree066', cmdlist=cmdlist, finishedCallback=None)
                        elif returnValue =="com_67":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia601405.us.archive.org/33/items/freeiptv_201911/FreeIPTV067.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='Free IPTVFree067', cmdlist=cmdlist, finishedCallback=None)
                        elif returnValue =="com_68":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")    
                                cmdlist.append("%s https://ia601405.us.archive.org/33/items/freeiptv_201911/FreeIPTV068.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='Free IPTVFree068', cmdlist=cmdlist, finishedCallback=None)
                        elif returnValue =="com_69":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia601405.us.archive.org/33/items/freeiptv_201911/FreeIPTV069.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='Free IPTVFree069', cmdlist=cmdlist, finishedCallback=None)
                        elif returnValue =="com_70":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia601405.us.archive.org/33/items/freeiptv_201911/FreeIPTV070.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='Free IPTVFree070', cmdlist=cmdlist, finishedCallback=None)

                        elif returnValue =="com_71":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia601405.us.archive.org/33/items/freeiptv_201911/FreeIPTV071.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='Free IPTVFree071', cmdlist=cmdlist, finishedCallback=None)
                        elif returnValue =="com_72":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia601405.us.archive.org/33/items/freeiptv_201911/FreeIPTV072.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='Free IPTVFree072', cmdlist=cmdlist, finishedCallback=None)
                        elif returnValue =="com_73":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia601405.us.archive.org/33/items/freeiptv_201911/FreeIPTV073.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='Free IPTVFree073', cmdlist=cmdlist, finishedCallback=None)
                        elif returnValue =="com_74":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'") 
                                cmdlist.append("%s https://ia601405.us.archive.org/33/items/freeiptv_201911/FreeIPTV074.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='Free IPTVFree074', cmdlist=cmdlist, finishedCallback=None)
                        elif returnValue =="com_75":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia601405.us.archive.org/33/items/freeiptv_201911/FreeIPTV075.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='Free IPTVFree075', cmdlist=cmdlist, finishedCallback=None)
                        elif returnValue =="com_76":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia601405.us.archive.org/33/items/freeiptv_201911/FreeIPTV076.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='Free IPTVFree076', cmdlist=cmdlist, finishedCallback=None)
                        elif returnValue =="com_77":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia601405.us.archive.org/33/items/freeiptv_201911/FreeIPTV077.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='Free IPTVFree077', cmdlist=cmdlist, finishedCallback=None)
                        elif returnValue =="com_78":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")    
                                cmdlist.append("%s https://ia601405.us.archive.org/33/items/freeiptv_201911/FreeIPTV078.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='Free IPTVFree078', cmdlist=cmdlist, finishedCallback=None)
                        elif returnValue =="com_79":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia601405.us.archive.org/33/items/freeiptv_201911/FreeIPTV079.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='Free IPTVFree079', cmdlist=cmdlist, finishedCallback=None)
                        elif returnValue =="com_80":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia601405.us.archive.org/33/items/freeiptv_201911/FreeIPTV080.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='Free IPTVFree080', cmdlist=cmdlist, finishedCallback=None)
                        elif returnValue =="com_81":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia601405.us.archive.org/33/items/freeiptv_201911/FreeIPTV081.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='Free IPTVFree081', cmdlist=cmdlist, finishedCallback=None)
                        elif returnValue =="com_82":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia601405.us.archive.org/33/items/freeiptv_201911/FreeIPTV082.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='Free IPTVFree082', cmdlist=cmdlist, finishedCallback=None)
                        elif returnValue =="com_83":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia601405.us.archive.org/33/items/freeiptv_201911/FreeIPTV083.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='Free IPTVFree083', cmdlist=cmdlist, finishedCallback=None)
                        elif returnValue =="com_84":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia601405.us.archive.org/33/items/freeiptv_201911/FreeIPTV084.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='Free IPTVFree084', cmdlist=cmdlist, finishedCallback=None)
                        elif returnValue =="com_85":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia601405.us.archive.org/33/items/freeiptv_201911/FreeIPTV085.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='Free IPTVFree085', cmdlist=cmdlist, finishedCallback=None)
                        elif returnValue =="com_86":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia601405.us.archive.org/33/items/freeiptv_201911/FreeIPTV086.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='Free IPTVFree086', cmdlist=cmdlist, finishedCallback=None)
                        elif returnValue =="com_87":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia601405.us.archive.org/33/items/freeiptv_201911/FreeIPTV087.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='Free IPTVFree087', cmdlist=cmdlist, finishedCallback=None)
                        elif returnValue =="com_88":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia601405.us.archive.org/33/items/freeiptv_201911/FreeIPTV088.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='Free IPTVFree088', cmdlist=cmdlist, finishedCallback=None)
                        elif returnValue =="com_89":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia601405.us.archive.org/33/items/freeiptv_201911/FreeIPTV089.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='Free IPTVFree089', cmdlist=cmdlist, finishedCallback=None)
                        elif returnValue =="com_90":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia601405.us.archive.org/33/items/freeiptv_201911/FreeIPTV090.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='Free IPTVFree090', cmdlist=cmdlist, finishedCallback=None)
                        elif returnValue =="com_91":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia601405.us.archive.org/33/items/freeiptv_201911/FreeIPTV091.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='Free IPTVFree091', cmdlist=cmdlist, finishedCallback=None)
                        elif returnValue =="com_92":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia601405.us.archive.org/33/items/freeiptv_201911/FreeIPTV092.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='Free IPTVFree092', cmdlist=cmdlist, finishedCallback=None)
                        elif returnValue =="com_93":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia601405.us.archive.org/33/items/freeiptv_201911/FreeIPTV093.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='Free IPTVFree093', cmdlist=cmdlist, finishedCallback=None)
                        elif returnValue =="com_94":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia601405.us.archive.org/33/items/freeiptv_201911/FreeIPTV094.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='Free IPTVFree094', cmdlist=cmdlist, finishedCallback=None)
                        elif returnValue =="com_95":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia601405.us.archive.org/33/items/freeiptv_201911/FreeIPTV095.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='Free IPTVFree095', cmdlist=cmdlist, finishedCallback=None)
                        elif returnValue =="com_96":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia601405.us.archive.org/33/items/freeiptv_201911/FreeIPTV096.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='Free IPTVFree096', cmdlist=cmdlist, finishedCallback=None)
                        elif returnValue =="com_97":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia601405.us.archive.org/33/items/freeiptv_201911/FreeIPTV097.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='Free IPTVFree097', cmdlist=cmdlist, finishedCallback=None)
                        elif returnValue =="com_98":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia601405.us.archive.org/33/items/freeiptv_201911/FreeIPTV098.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='Free IPTVFree098', cmdlist=cmdlist, finishedCallback=None)
                        elif returnValue =="com_99":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia601405.us.archive.org/33/items/freeiptv_201911/FreeIPTV099.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='Free IPTVFree099', cmdlist=cmdlist, finishedCallback=None)
                        elif returnValue =="com_100":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia601405.us.archive.org/33/items/freeiptv_201911/FreeIPTV100.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='Free IPTVFree100', cmdlist=cmdlist, finishedCallback=None)
                        elif returnValue =="com_101":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia601405.us.archive.org/33/items/freeiptv_201911/FreeIPTV101.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='Free IPTVFree101', cmdlist=cmdlist, finishedCallback=None)
                        elif returnValue =="com_102":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia601405.us.archive.org/33/items/freeiptv_201911/FreeIPTV102.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='Free IPTVFree102', cmdlist=cmdlist, finishedCallback=None)
                        elif returnValue =="com_103":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia601405.us.archive.org/33/items/freeiptv_201911/FreeIPTV103.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='Free IPTVFree103', cmdlist=cmdlist, finishedCallback=None)
                        elif returnValue =="com_104":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia601405.us.archive.org/33/items/freeiptv_201911/FreeIPTV104.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='Free IPTVFree104', cmdlist=cmdlist, finishedCallback=None)
                        elif returnValue =="com_105":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia601405.us.archive.org/33/items/freeiptv_201911/FreeIPTV105.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='Free IPTVFree105', cmdlist=cmdlist, finishedCallback=None)
                        elif returnValue =="com_106":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia601405.us.archive.org/33/items/freeiptv_201911/FreeIPTV106.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='Free IPTVFree106', cmdlist=cmdlist, finishedCallback=None)
                        elif returnValue =="com_107":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia601405.us.archive.org/33/items/freeiptv_201911/FreeIPTV107.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='Free IPTVFree107', cmdlist=cmdlist, finishedCallback=None)
                        elif returnValue =="com_108":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia601405.us.archive.org/33/items/freeiptv_201911/FreeIPTV108.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='Free IPTVFree108', cmdlist=cmdlist, finishedCallback=None)
                        elif returnValue =="com_109":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia601405.us.archive.org/33/items/freeiptv_201911/FreeIPTV109.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='Free IPTVFree109', cmdlist=cmdlist, finishedCallback=None)
                        elif returnValue =="com_110":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia601405.us.archive.org/33/items/freeiptv_201911/FreeIPTV110.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='Free IPTVFree110', cmdlist=cmdlist, finishedCallback=None)
                        elif returnValue =="com_111":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia601405.us.archive.org/33/items/freeiptv_201911/FreeIPTV111.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='Free IPTVFree111', cmdlist=cmdlist, finishedCallback=None)
                        elif returnValue =="com_112":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia601405.us.archive.org/33/items/freeiptv_201911/FreeIPTV112.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='Free IPTVFree112', cmdlist=cmdlist, finishedCallback=None)
                        elif returnValue =="com_113":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia601405.us.archive.org/33/items/freeiptv_201911/FreeIPTV113.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='Free IPTVFree113', cmdlist=cmdlist, finishedCallback=None)
                        elif returnValue =="com_114":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia601405.us.archive.org/33/items/freeiptv_201911/FreeIPTV114.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='Free IPTVFree114', cmdlist=cmdlist, finishedCallback=None)
                        elif returnValue =="com_115":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia601405.us.archive.org/33/items/freeiptv_201911/FreeIPTV115.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='Free IPTVFree115', cmdlist=cmdlist, finishedCallback=None)
                        elif returnValue =="com_116":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia601405.us.archive.org/33/items/freeiptv_201911/FreeIPTV116.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='Free IPTVFree116', cmdlist=cmdlist, finishedCallback=None)
                        elif returnValue =="com_117":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia601405.us.archive.org/33/items/freeiptv_201911/FreeIPTV117.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='Free IPTVFree117', cmdlist=cmdlist, finishedCallback=None)
                        elif returnValue =="com_118":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia601405.us.archive.org/33/items/freeiptv_201911/FreeIPTV118.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='Free IPTVFree118', cmdlist=cmdlist, finishedCallback=None)
                        elif returnValue =="com_119":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia601405.us.archive.org/33/items/freeiptv_201911/FreeIPTV119.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='Free IPTVFree119', cmdlist=cmdlist, finishedCallback=None)
                        elif returnValue =="com_120":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia601405.us.archive.org/33/items/freeiptv_201911/FreeIPTV120.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='Free IPTVFree120', cmdlist=cmdlist, finishedCallback=None)
                        elif returnValue =="com_121":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia601405.us.archive.org/33/items/freeiptv_201911/FreeIPTV121.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='Free IPTVFree121', cmdlist=cmdlist, finishedCallback=None)
                        elif returnValue =="com_0122":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia601405.us.archive.org/33/items/freeiptv_201911/FreeIPTV122.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='Free IPTVFree122', cmdlist=cmdlist, finishedCallback=None)
                        elif returnValue =="com_123":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia601405.us.archive.org/33/items/freeiptv_201911/FreeIPTV123.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='Free IPTVFree123', cmdlist=cmdlist, finishedCallback=None)
                        elif returnValue =="com_124":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia601405.us.archive.org/33/items/freeiptv_201911/FreeIPTV124.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='Free IPTVFree124', cmdlist=cmdlist, finishedCallback=None)
                        elif returnValue =="com_125":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia601405.us.archive.org/33/items/freeiptv_201911/FreeIPTV125.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='Free IPTVFree125', cmdlist=cmdlist, finishedCallback=None)
                        elif returnValue =="com_126":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia601405.us.archive.org/33/items/freeiptv_201911/FreeIPTV126.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='Free IPTVFree126', cmdlist=cmdlist, finishedCallback=None)
                        elif returnValue =="com_127":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia601405.us.archive.org/33/items/freeiptv_201911/FreeIPTV127.sh  -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='Free IPTVFree127', cmdlist=cmdlist, finishedCallback=None)
                        elif returnValue =="com_128":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia601405.us.archive.org/33/items/freeiptv_201911/FreeIPTV128.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='Free IPTVFree128', cmdlist=cmdlist, finishedCallback=None)
                        elif returnValue =="com_129":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia601405.us.archive.org/33/items/freeiptv_201911/FreeIPTV129.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='Free IPTVFree129', cmdlist=cmdlist, finishedCallback=None)
                        elif returnValue =="com_130":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia601405.us.archive.org/33/items/freeiptv_201911/FreeIPTV130.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='Free IPTVFree130', cmdlist=cmdlist, finishedCallback=None)
                        elif returnValue =="com_131":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia601405.us.archive.org/33/items/freeiptv_201911/FreeIPTV131.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='Free IPTVFree131', cmdlist=cmdlist, finishedCallback=None)
                        elif returnValue =="com_132":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia601405.us.archive.org/33/items/freeiptv_201911/FreeIPTV132.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='Free IPTVFree132', cmdlist=cmdlist, finishedCallback=None)
                        elif returnValue =="com_133":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia601405.us.archive.org/33/items/freeiptv_201911/FreeIPTV133.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='Free IPTVFree133', cmdlist=cmdlist, finishedCallback=None)
                        elif returnValue =="com_134":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'") 
                                cmdlist.append("%s https://ia601405.us.archive.org/33/items/freeiptv_201911/FreeIPTV134.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='Free IPTVFree134', cmdlist=cmdlist, finishedCallback=None)
                        elif returnValue =="com_135":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia601405.us.archive.org/33/items/freeiptv_201911/FreeIPTV135.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='Free IPTVFree135', cmdlist=cmdlist, finishedCallback=None)
                        elif returnValue =="com_136":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia601405.us.archive.org/33/items/freeiptv_201911/FreeIPTV136.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='Free IPTVFree136', cmdlist=cmdlist, finishedCallback=None)
                        elif returnValue =="com_137":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia601405.us.archive.org/33/items/freeiptv_201911/FreeIPTV137.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='Free IPTVFree137', cmdlist=cmdlist, finishedCallback=None)
                        elif returnValue =="com_138":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")    
                                cmdlist.append("%s https://ia601405.us.archive.org/33/items/freeiptv_201911/FreeIPTV138.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='Free IPTVFree138', cmdlist=cmdlist, finishedCallback=None)
                        elif returnValue =="com_139":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia601405.us.archive.org/33/items/freeiptv_201911/FreeIPTV139.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='Free IPTVFree139', cmdlist=cmdlist, finishedCallback=None)
                        elif returnValue =="com_140":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia601405.us.archive.org/33/items/freeiptv_201911/FreeIPTV140.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='Free IPTVFree140', cmdlist=cmdlist, finishedCallback=None)
                        elif returnValue =="com_141":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia601405.us.archive.org/33/items/freeiptv_201911/FreeIPTV141.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='Free IPTVFree141', cmdlist=cmdlist, finishedCallback=None)
                        elif returnValue =="com_142":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia601405.us.archive.org/33/items/freeiptv_201911/FreeIPTV142.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='Free IPTVFree142', cmdlist=cmdlist, finishedCallback=None)
                        elif returnValue =="com_143":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia601405.us.archive.org/33/items/freeiptv_201911/FreeIPTV143.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='Free IPTVFree143', cmdlist=cmdlist, finishedCallback=None)
                        elif returnValue =="com_144":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia601405.us.archive.org/33/items/freeiptv_201911/FreeIPTV144.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='Free IPTVFree144', cmdlist=cmdlist, finishedCallback=None)
                        elif returnValue =="com_145":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia601405.us.archive.org/33/items/freeiptv_201911/FreeIPTV145.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='Free IPTVFree145', cmdlist=cmdlist, finishedCallback=None)
                        elif returnValue =="com_146":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia601405.us.archive.org/33/items/freeiptv_201911/FreeIPTV146.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='Free IPTVFree146', cmdlist=cmdlist, finishedCallback=None)
                        elif returnValue =="com_147":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia601405.us.archive.org/33/items/freeiptv_201911/FreeIPTV147.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='Free IPTVFree147', cmdlist=cmdlist, finishedCallback=None)
                        elif returnValue =="com_148":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia601405.us.archive.org/33/items/freeiptv_201911/FreeIPTV148.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='Free IPTVFree148', cmdlist=cmdlist, finishedCallback=None)
                        elif returnValue =="com_149":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia601405.us.archive.org/33/items/freeiptv_201911/FreeIPTV149.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='Free IPTVFree149', cmdlist=cmdlist, finishedCallback=None)
                        elif returnValue =="com_150":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia601405.us.archive.org/33/items/freeiptv_201911/FreeIPTV150.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='Free IPTVFree150', cmdlist=cmdlist, finishedCallback=None)


                        elif returnValue =="com_0151":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia601403.us.archive.org/4/items/iptvworldarb/IPTVWORLDARN0.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='IPTV WORLD ARABE', cmdlist=cmdlist, finishedCallback=None)
                        elif returnValue =="com_0152":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia601403.us.archive.org/4/items/iptvworldarb/IPTVWORLDARN0.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='IPTV WORLD ARABE', cmdlist=cmdlist, finishedCallback=None)
                        elif returnValue =="com_0153":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia601403.us.archive.org/4/items/iptvworldarb/IPTVWORLDARN20.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='IPTV WORLD ARABE', cmdlist=cmdlist, finishedCallback=None)
                        elif returnValue =="com_0154":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'") 
                                cmdlist.append("%s https://ia601403.us.archive.org/4/items/iptvworldarb/IPTVWORLDARN50.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='IPTV WORLD ARABE', cmdlist=cmdlist, finishedCallback=None)
                        elif returnValue =="com_0155":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia601403.us.archive.org/4/items/iptvworldarb/IPTVWORLDARN100.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='IPTV WORLD ARABE', cmdlist=cmdlist, finishedCallback=None)
                        elif returnValue =="com_151":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia601403.us.archive.org/4/items/iptvworldarb/IPTVWORLDAR001.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='IPTV WORLD ARABE', cmdlist=cmdlist, finishedCallback=None)
                        elif returnValue =="com_152":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia601403.us.archive.org/4/items/iptvworldarb/IPTVWORLDAR002.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='IPTV WORLD ARABE', cmdlist=cmdlist, finishedCallback=None)
                        elif returnValue =="com_153":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia601403.us.archive.org/4/items/iptvworldarb/IPTVWORLDAR003.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='IPTV WORLD ARABE', cmdlist=cmdlist, finishedCallback=None)
                        elif returnValue =="com_154":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'") 
                                cmdlist.append("%s https://ia601403.us.archive.org/4/items/iptvworldarb/IPTVWORLDAR004.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='IPTV WORLD ARABE', cmdlist=cmdlist, finishedCallback=None)
                        elif returnValue =="com_155":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia601403.us.archive.org/4/items/iptvworldarb/IPTVWORLDAR005.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='IPTV WORLD ARABE', cmdlist=cmdlist, finishedCallback=None)
                        elif returnValue =="com_156":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia601403.us.archive.org/4/items/iptvworldarb/IPTVWORLDAR006.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='IPTV WORLD ARABE', cmdlist=cmdlist, finishedCallback=None)
                        elif returnValue =="com_157":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia601403.us.archive.org/4/items/iptvworldarb/IPTVWORLDAR007.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='IPTV WORLD ARABE', cmdlist=cmdlist, finishedCallback=None)
                        elif returnValue =="com_158":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")    
                                cmdlist.append("%s https://ia601403.us.archive.org/4/items/iptvworldarb/IPTVWORLDAR008.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='IPTV WORLD ARABE', cmdlist=cmdlist, finishedCallback=None)
                        elif returnValue =="com_159":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia601403.us.archive.org/4/items/iptvworldarb/IPTVWORLDAR009.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='IPTV WORLD ARABE', cmdlist=cmdlist, finishedCallback=None)
                        elif returnValue =="com_160":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia601403.us.archive.org/4/items/iptvworldarb/IPTVWORLDAR010.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='IPTV WORLD ARABE', cmdlist=cmdlist, finishedCallback=None)
                        elif returnValue =="com_161":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia601403.us.archive.org/4/items/iptvworldarb/IPTVWORLDAR011.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='IPTV WORLD ARABE', cmdlist=cmdlist, finishedCallback=None)
                        elif returnValue =="com_162":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia601403.us.archive.org/4/items/iptvworldarb/IPTVWORLDAR012.sh  -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='IPTV WORLD SMART TV', cmdlist=cmdlist, finishedCallback=None)
                        elif returnValue =="com_163":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia601403.us.archive.org/4/items/iptvworldarb/IPTVWORLDAR013.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='IPTV WORLD ARABE', cmdlist=cmdlist, finishedCallback=None)
                        elif returnValue =="com_164":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia601403.us.archive.org/4/items/iptvworldarb/IPTVWORLDAR014.sh  -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='IPTV WORLD ARABE', cmdlist=cmdlist, finishedCallback=None)
                        elif returnValue =="com_165":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia601403.us.archive.org/4/items/iptvworldarb/IPTVWORLDAR015.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='IPTV WORLD ARABE', cmdlist=cmdlist, finishedCallback=None)
                        elif returnValue =="com_166":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia601403.us.archive.org/4/items/iptvworldarb/IPTVWORLDAR016.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='IPTV WORLD ARABE', cmdlist=cmdlist, finishedCallback=None)
                        elif returnValue =="com_167":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia601403.us.archive.org/4/items/iptvworldarb/IPTVWORLDAR017.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='IPTV WORLD ARABE', cmdlist=cmdlist, finishedCallback=None)
                        elif returnValue =="com_168":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia601403.us.archive.org/4/items/iptvworldarb/IPTVWORLDAR018.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='IPTV WORLD ARABE', cmdlist=cmdlist, finishedCallback=None)
                        elif returnValue =="com_69":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia601403.us.archive.org/4/items/iptvworldarb/IPTVWORLDAR019.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='IPTV WORLD ARABE', cmdlist=cmdlist, finishedCallback=None)
                        elif returnValue =="com_170":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia601403.us.archive.org/4/items/iptvworldarb/IPTVWORLDAR020.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='IPTV WORLD ARABE', cmdlist=cmdlist, finishedCallback=None)
                        elif returnValue =="com_171":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia601403.us.archive.org/4/items/iptvworldarb/IPTVWORLDAR021.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='IPTV WORLD ARABE', cmdlist=cmdlist, finishedCallback=None)
                        elif returnValue =="com_172":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia601403.us.archive.org/4/items/iptvworldarb/IPTVWORLDAR022.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='IPTV WORD ARABE', cmdlist=cmdlist, finishedCallback=None)
                        elif returnValue =="com_173":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia601403.us.archive.org/4/items/iptvworldarb/IPTVWORLDAR023.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='IPTV WORD ARABE', cmdlist=cmdlist, finishedCallback=None)
                        elif returnValue =="com_174":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia601403.us.archive.org/4/items/iptvworldarb/IPTVWORLDAR024.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='IPTV WORD ARABE', cmdlist=cmdlist, finishedCallback=None)
                        elif returnValue =="com_175":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia601403.us.archive.org/4/items/iptvworldarb/IPTVWORLDAR025.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='IPTV WORD ARABE', cmdlist=cmdlist, finishedCallback=None)
                        elif returnValue =="com_176":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia601403.us.archive.org/4/items/iptvworldarb/IPTVWORLDAR026.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='IPTV WORD ARABE', cmdlist=cmdlist, finishedCallback=None)
                        elif returnValue =="com_177":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia601403.us.archive.org/4/items/iptvworldarb/IPTVWORLDAR027.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='IPTV WORD ARABE', cmdlist=cmdlist, finishedCallback=None)
                        elif returnValue =="com_178":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia601403.us.archive.org/4/items/iptvworldarb/IPTVWORLDAR028.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='IPTV WORD ARABE', cmdlist=cmdlist, finishedCallback=None)
                        elif returnValue =="com_179":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia601403.us.archive.org/4/items/iptvworldarb/IPTVWORLDAR029.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='IPTV WORD ARABE', cmdlist=cmdlist, finishedCallback=None)
                        elif returnValue =="com_180":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia601403.us.archive.org/4/items/iptvworldarb/IPTVWORLDAR030.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='IPTV WORD ARABE', cmdlist=cmdlist, finishedCallback=None)
                        elif returnValue =="com_181":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia601403.us.archive.org/4/items/iptvworldarb/IPTVWORLDAR031.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='IPTV WORD ARABE', cmdlist=cmdlist, finishedCallback=None)
                        elif returnValue =="com_182":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia601403.us.archive.org/4/items/iptvworldarb/IPTVWORLDAR032.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='IPTV WORD ARABE', cmdlist=cmdlist, finishedCallback=None)
                        elif returnValue =="com_183":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia601403.us.archive.org/4/items/iptvworldarb/IPTVWORLDAR033.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='IPTV WORD ARABE', cmdlist=cmdlist, finishedCallback=None)
                        elif returnValue =="com_184":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia601403.us.archive.org/4/items/iptvworldarb/IPTVWORLDAR034.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='IPTV WORD ARABE', cmdlist=cmdlist, finishedCallback=None)
                        elif returnValue =="com_185":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia601403.us.archive.org/4/items/iptvworldarb/IPTVWORLDAR035.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='IPTV WORD ARABE', cmdlist=cmdlist, finishedCallback=None)
                        elif returnValue =="com_186":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia601403.us.archive.org/4/items/iptvworldarb/IPTVWORLDAR036.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='IPTV WORD ARABE', cmdlist=cmdlist, finishedCallback=None)
                        elif returnValue =="com_187":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia601403.us.archive.org/4/items/iptvworldarb/IPTVWORLDAR037.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='IPTV WORD ARABE', cmdlist=cmdlist, finishedCallback=None)
                        elif returnValue =="com_188":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia601403.us.archive.org/4/items/iptvworldarb/IPTVWORLDAR038.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='IPTV WORD ARABE', cmdlist=cmdlist, finishedCallback=None)
                        elif returnValue =="com_189":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia601403.us.archive.org/4/items/iptvworldarb/IPTVWORLDAR039.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='IPTV WORD ARABE', cmdlist=cmdlist, finishedCallback=None)
                        elif returnValue =="com_190":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia601403.us.archive.org/4/items/iptvworldarb/IPTVWORLDAR040.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='IPTV WORD ARABE', cmdlist=cmdlist, finishedCallback=None)
                        elif returnValue =="com_191":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia601403.us.archive.org/4/items/iptvworldarb/IPTVWORLDAR041.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='IPTV WORD ARABE', cmdlist=cmdlist, finishedCallback=None)
                        elif returnValue =="com_192":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia601403.us.archive.org/4/items/iptvworldarb/IPTVWORLDAR042.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='IPTV WORD ARABE', cmdlist=cmdlist, finishedCallback=None)
                        elif returnValue =="com_193":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia601403.us.archive.org/4/items/iptvworldarb/IPTVWORLDAR043.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='IPTV WORD ARABE', cmdlist=cmdlist, finishedCallback=None)
                        elif returnValue =="com_194":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia601403.us.archive.org/4/items/iptvworldarb/IPTVWORLDAR044.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='IPTV WORD ARABE', cmdlist=cmdlist, finishedCallback=None)
                        elif returnValue =="com_195":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia601403.us.archive.org/4/items/iptvworldarb/IPTVWORLDAR045.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='IPTV WORD ARABE', cmdlist=cmdlist, finishedCallback=None)
                        elif returnValue =="com_196":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia601403.us.archive.org/4/items/iptvworldarb/IPTVWORLDAR046.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='IPTV WORD ARABE', cmdlist=cmdlist, finishedCallback=None)
                        elif returnValue =="com_197":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia601403.us.archive.org/4/items/iptvworldarb/IPTVWORLDAR047.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='IPTV WORLD ARABE', cmdlist=cmdlist, finishedCallback=None)
                        elif returnValue =="com_198":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia601403.us.archive.org/4/items/iptvworldarb/IPTVWORLDAR048.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='IPTV WORLD ARABE', cmdlist=cmdlist, finishedCallback=None)
                        elif returnValue =="com_199":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia601403.us.archive.org/4/items/iptvworldarb/IPTVWORLDAR049.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='IPTV WORLD ARABE', cmdlist=cmdlist, finishedCallback=None)
                        elif returnValue =="com_200":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia601403.us.archive.org/4/items/iptvworldarb/IPTVWORLDAR050.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='IPTV WORLD ARABE', cmdlist=cmdlist, finishedCallback=None)
                        elif returnValue =="com_201":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia601403.us.archive.org/4/items/iptvworldarb/IPTVWORLDAR051.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='IPTV WORLD ARABE', cmdlist=cmdlist, finishedCallback=None)
                        elif returnValue =="com_202":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia601403.us.archive.org/4/items/iptvworldarb/IPTVWORLDAR052.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='IPTV WORLD ARABE', cmdlist=cmdlist, finishedCallback=None)
                        elif returnValue =="com_203":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia601403.us.archive.org/4/items/iptvworldarb/IPTVWORLDAR053.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='IPTV WORLD ARABE', cmdlist=cmdlist, finishedCallback=None)
                        elif returnValue =="com_204":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia601403.us.archive.org/4/items/iptvworldarb/IPTVWORLDAR054.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='IPTV WORLD ARABE', cmdlist=cmdlist, finishedCallback=None)
                        elif returnValue =="com_205":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia601403.us.archive.org/4/items/iptvworldarb/IPTVWORLDAR055.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='IPTV WORLD ARABE', cmdlist=cmdlist, finishedCallback=None)
                        elif returnValue =="com_206":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia601403.us.archive.org/4/items/iptvworldarb/IPTVWORLDAR056.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='IPTV WORLD ARABE', cmdlist=cmdlist, finishedCallback=None)
                        elif returnValue =="com_207":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia601403.us.archive.org/4/items/iptvworldarb/IPTVWORLDAR057.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='IPTV WORLD ARABE', cmdlist=cmdlist, finishedCallback=None)
                        elif returnValue =="com_208":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia601403.us.archive.org/4/items/iptvworldarb/IPTVWORLDAR058.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='IPTV WORLD ARABE', cmdlist=cmdlist, finishedCallback=None)
                        elif returnValue =="com_209":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia601403.us.archive.org/4/items/iptvworldarb/IPTVWORLDAR059.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='IPTV WORLD ARABE', cmdlist=cmdlist, finishedCallback=None)
                        elif returnValue =="com_210":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia601403.us.archive.org/4/items/iptvworldarb/IPTVWORLDAR060.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='IPTV WORLD ARABE', cmdlist=cmdlist, finishedCallback=None)
                        elif returnValue =="com_211":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia601403.us.archive.org/4/items/iptvworldarb/IPTVWORLDAR061.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='IPTV WORLD ARABE', cmdlist=cmdlist, finishedCallback=None)
                        elif returnValue =="com_212":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia601403.us.archive.org/4/items/iptvworldarb/IPTVWORLDAR062.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='IPTV WORLD ARABE', cmdlist=cmdlist, finishedCallback=None)
                        elif returnValue =="com_213":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia601403.us.archive.org/4/items/iptvworldarb/IPTVWORLDAR063.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='IPTV WORLD ARABE', cmdlist=cmdlist, finishedCallback=None)
                        elif returnValue =="com_214":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia601403.us.archive.org/4/items/iptvworldarb/IPTVWORLDAR064.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='IPTV WORLD ARABE', cmdlist=cmdlist, finishedCallback=None)
                        elif returnValue =="com_215":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia601403.us.archive.org/4/items/iptvworldarb/IPTVWORLDAR065.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='IPTV WORLD ARABE', cmdlist=cmdlist, finishedCallback=None)
                        elif returnValue =="com_216":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia601403.us.archive.org/4/items/iptvworldarb/IPTVWORLDAR066.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='IPTV WORLD ARABE', cmdlist=cmdlist, finishedCallback=None)
                        elif returnValue =="com_217":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia601403.us.archive.org/4/items/iptvworldarb/IPTVWORLDAR067.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='IPTV WORLD ARABE', cmdlist=cmdlist, finishedCallback=None)
                        elif returnValue =="com_218":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia601403.us.archive.org/4/items/iptvworldarb/IPTVWORLDAR068.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='IPTV WORLD ARABE', cmdlist=cmdlist, finishedCallback=None)
                        elif returnValue =="com_219":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia601403.us.archive.org/4/items/iptvworldarb/IPTVWORLDAR069.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='IPTV WORLD ARABE', cmdlist=cmdlist, finishedCallback=None)
                        elif returnValue =="com_220":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia601403.us.archive.org/4/items/iptvworldarb/IPTVWORLDAR070.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='IPTV WORLD ARABE', cmdlist=cmdlist, finishedCallback=None)
                        elif returnValue =="com_221":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia601403.us.archive.org/4/items/iptvworldarb/IPTVWORLDAR071.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='IPTV WORLD ARABE', cmdlist=cmdlist, finishedCallback=None)
                        elif returnValue =="com_222":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia601403.us.archive.org/4/items/iptvworldarb/IPTVWORLDAR072.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='IPTV WORLD ARABE', cmdlist=cmdlist, finishedCallback=None)
                        elif returnValue =="com_223":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia601403.us.archive.org/4/items/iptvworldarb/IPTVWORLDAR073.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='IPTV WORLD ARABE', cmdlist=cmdlist, finishedCallback=None)
                        elif returnValue =="com_224":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia601403.us.archive.org/4/items/iptvworldarb/IPTVWORLDAR074.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='IPTV WORLD ARABE', cmdlist=cmdlist, finishedCallback=None)
                        elif returnValue =="com_225":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia601403.us.archive.org/4/items/iptvworldarb/IPTVWORLDAR075.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='IPTV WORLD ARABE', cmdlist=cmdlist, finishedCallback=None)
                        elif returnValue =="com_226":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia601403.us.archive.org/4/items/iptvworldarb/IPTVWORLDAR076.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='IPTV WORLD ARABE', cmdlist=cmdlist, finishedCallback=None)
                        elif returnValue =="com_227":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia601403.us.archive.org/4/items/iptvworldarb/IPTVWORLDAR077.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='IPTV WORLD ARABE', cmdlist=cmdlist, finishedCallback=None)
                        elif returnValue =="com_228":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia601403.us.archive.org/4/items/iptvworldarb/IPTVWORLDAR078.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='IPTV WORLD ARABE', cmdlist=cmdlist, finishedCallback=None)
                        elif returnValue =="com_229":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia601403.us.archive.org/4/items/iptvworldarb/IPTVWORLDAR079.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='IPTV WORLD ARABE', cmdlist=cmdlist, finishedCallback=None)
                        elif returnValue =="com_230":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia601403.us.archive.org/4/items/iptvworldarb/IPTVWORLDAR080.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='IPTV WORLD ARABE', cmdlist=cmdlist, finishedCallback=None)
                        elif returnValue =="com_231":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia601403.us.archive.org/4/items/iptvworldarb/IPTVWORLDAR081.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='IPTV WORLD ARABE', cmdlist=cmdlist, finishedCallback=None)
                        elif returnValue =="com_232":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia601403.us.archive.org/4/items/iptvworldarb/IPTVWORLDAR082.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='IPTV WORLD ARABE', cmdlist=cmdlist, finishedCallback=None)
                        elif returnValue =="com_233":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia601403.us.archive.org/4/items/iptvworldarb/IPTVWORLDAR083.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='IPTV WORLD ARABE', cmdlist=cmdlist, finishedCallback=None)
                        elif returnValue =="com_234":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'") 
                                cmdlist.append("%s https://ia601403.us.archive.org/4/items/iptvworldarb/IPTVWORLDAR084.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='IPTV WORLD ARABE', cmdlist=cmdlist, finishedCallback=None)
                        elif returnValue =="com_235":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia601403.us.archive.org/4/items/iptvworldarb/IPTVWORLDAR085.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='IPTV WORLD ARABE', cmdlist=cmdlist, finishedCallback=None)
                        elif returnValue =="com_236":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia601403.us.archive.org/4/items/iptvworldarb/IPTVWORLDAR086.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='IPTV WORLD ARABE', cmdlist=cmdlist, finishedCallback=None)
                        elif returnValue =="com_237":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia601403.us.archive.org/4/items/iptvworldarb/IPTVWORLDAR087.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='IPTV WORLD ARABE', cmdlist=cmdlist, finishedCallback=None)
                        elif returnValue =="com_238":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")    
                                cmdlist.append("%s https://ia601403.us.archive.org/4/items/iptvworldarb/IPTVWORLDAR088.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='IPTV WORLD ARABE', cmdlist=cmdlist, finishedCallback=None)
                        elif returnValue =="com_239":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia601403.us.archive.org/4/items/iptvworldarb/IPTVWORLDAR089.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='IPTV WORLD ARABE', cmdlist=cmdlist, finishedCallback=None)
                        elif returnValue =="com_240":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia601403.us.archive.org/4/items/iptvworldarb/IPTVWORLDAR090.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='Free IPTVFree050', cmdlist=cmdlist, finishedCallback=None)
                        elif returnValue =="com_241":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia601403.us.archive.org/4/items/iptvworldarb/IPTVWORLDAR091.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='IPTV WORLD ARABE', cmdlist=cmdlist, finishedCallback=None)
                        elif returnValue =="com_242":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia601403.us.archive.org/4/items/iptvworldarb/IPTVWORLDAR092.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='IPTV WORLD ARABE', cmdlist=cmdlist, finishedCallback=None)
                        elif returnValue =="com_243":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia601403.us.archive.org/4/items/iptvworldarb/IPTVWORLDAR093.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='IPTV WORLD ARABE', cmdlist=cmdlist, finishedCallback=None)
                        elif returnValue =="com_244":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia601403.us.archive.org/4/items/iptvworldarb/IPTVWORLDAR094.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='IPTV WORLD ARABE', cmdlist=cmdlist, finishedCallback=None)
                        elif returnValue =="com_245":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia601403.us.archive.org/4/items/iptvworldarb/IPTVWORLDAR095.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='IPTV WORLD ARABE', cmdlist=cmdlist, finishedCallback=None)
                        elif returnValue =="com_246":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia601403.us.archive.org/4/items/iptvworldarb/IPTVWORLDAR096.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='IPTV WORLD ARABE', cmdlist=cmdlist, finishedCallback=None)
                        elif returnValue =="com_247":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia601403.us.archive.org/4/items/iptvworldarb/IPTVWORLDAR097.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='IPTV WORLD ARABE', cmdlist=cmdlist, finishedCallback=None)
                        elif returnValue =="com_248":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia601403.us.archive.org/4/items/iptvworldarb/IPTVWORLDAR098.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='IPTV WORLD ARABE', cmdlist=cmdlist, finishedCallback=None)
                        elif returnValue =="com_249":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia601403.us.archive.org/4/items/iptvworldarb/IPTVWORLDAR099.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='IPTV WORLD ARABE', cmdlist=cmdlist, finishedCallback=None)
                        elif returnValue =="com_250":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia601403.us.archive.org/4/items/iptvworldarb/IPTVWORLDAR100.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='IPTV WORLD ARABE', cmdlist=cmdlist, finishedCallback=None)
                        elif returnValue =="com_251":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia601408.us.archive.org/29/items/iptvworldfr_202101/IPTVWORLDFR001.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='IPTV WORLD FRANCE', cmdlist=cmdlist, finishedCallback=None)
                        elif returnValue =="com_252":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia601408.us.archive.org/29/items/iptvworldfr_202101/IPTVWORLDFR002.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='IPTV WORLD FRANCE', cmdlist=cmdlist, finishedCallback=None)
                        elif returnValue =="com_253":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia601408.us.archive.org/29/items/iptvworldfr_202101/IPTVWORLDFR003.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='IPTV WORLD FRANCE', cmdlist=cmdlist, finishedCallback=None)
                        elif returnValue =="com_254":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'") 
                                cmdlist.append("%s https://ia601408.us.archive.org/29/items/iptvworldfr_202101/IPTVWORLDFR004.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='IPTV WORLD FRANCE', cmdlist=cmdlist, finishedCallback=None)
                        elif returnValue =="com_255":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia601408.us.archive.org/29/items/iptvworldfr_202101/IPTVWORLDFR005.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='IPTV WORLD FRANCE', cmdlist=cmdlist, finishedCallback=None)
                        elif returnValue =="com_256":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia601408.us.archive.org/29/items/iptvworldfr_202101/IPTVWORLDFR006.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='IPTV WORLD FRANCE', cmdlist=cmdlist, finishedCallback=None)
                        elif returnValue =="com_0257":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia601409.us.archive.org/7/items/iptvworldfr/IPTVWORLDFRN0.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='IPTV WORLD FRANCE', cmdlist=cmdlist, finishedCallback=None)
                        elif returnValue =="com_0258":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")    
                                cmdlist.append("%s https://ia601409.us.archive.org/7/items/iptvworldfr/IPTVWORLDFRN20.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='IPTV WORLD FRANCE', cmdlist=cmdlist, finishedCallback=None)
                        elif returnValue =="com_0259":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia601409.us.archive.org/7/items/iptvworldfr/IPTVWORLDFRN50.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='IPTV WORLD FRANCE', cmdlist=cmdlist, finishedCallback=None)
                        elif returnValue =="com_0260":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia601409.us.archive.org/7/items/iptvworldfr/IPTVWORLDFRN100.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='IPTV WORLD FRANCE', cmdlist=cmdlist, finishedCallback=None)
                        elif returnValue =="com_0261":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia601409.us.archive.org/7/items/iptvworldfr/IPTVWORLDFRNALL.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='IPTV WORLD FRANCE', cmdlist=cmdlist, finishedCallback=None)
                        elif returnValue =="com_257":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia601409.us.archive.org/7/items/iptvworldfr/IPTVWORLDFR001.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='IPTV WORLD FRANCE', cmdlist=cmdlist, finishedCallback=None)
                        elif returnValue =="com_258":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")    
                                cmdlist.append("%s https://ia601409.us.archive.org/7/items/iptvworldfr/IPTVWORLDFR002.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='IPTV WORLD FRANCE', cmdlist=cmdlist, finishedCallback=None)
                        elif returnValue =="com_259":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia601409.us.archive.org/7/items/iptvworldfr/IPTVWORLDFR003.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='IPTV WORLD FRANCE', cmdlist=cmdlist, finishedCallback=None)
                        elif returnValue =="com_260":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia601409.us.archive.org/7/items/iptvworldfr/IPTVWORLDFR004.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='IPTV WORLD FRANCE', cmdlist=cmdlist, finishedCallback=None)
                        elif returnValue =="com_261":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia601409.us.archive.org/7/items/iptvworldfr/IPTVWORLDFR005.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='IPTV WORLD FRANCE', cmdlist=cmdlist, finishedCallback=None)
                        elif returnValue =="com_262":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia601409.us.archive.org/7/items/iptvworldfr/IPTVWORLDFR006.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='IPTV WORLD FRANCE', cmdlist=cmdlist, finishedCallback=None)
                        elif returnValue =="com_263":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia601409.us.archive.org/7/items/iptvworldfr/IPTVWORLDFR007.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='IPTV WORLD FRANCE', cmdlist=cmdlist, finishedCallback=None)
                        elif returnValue =="com_264":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia601409.us.archive.org/7/items/iptvworldfr/IPTVWORLDFR008.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='IPTV WORLD FRANCE', cmdlist=cmdlist, finishedCallback=None)
                        elif returnValue =="com_265":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia601409.us.archive.org/7/items/iptvworldfr/IPTVWORLDFR009.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='IPTV WORLD FRANCE', cmdlist=cmdlist, finishedCallback=None)
                        elif returnValue =="com_266":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia601409.us.archive.org/7/items/iptvworldfr/IPTVWORLDFR010.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='IPTV WORLD FRANCE', cmdlist=cmdlist, finishedCallback=None)
                        elif returnValue =="com_267":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia601409.us.archive.org/7/items/iptvworldfr/IPTVWORLDFR011.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='IPTV WORLD FRANCE', cmdlist=cmdlist, finishedCallback=None)
                        elif returnValue =="com_268":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia601409.us.archive.org/7/items/iptvworldfr/IPTVWORLDFR012.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='IPTV WORLD FRANCE', cmdlist=cmdlist, finishedCallback=None)
                        elif returnValue =="com_269":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia601409.us.archive.org/7/items/iptvworldfr/IPTVWORLDFR013.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='IPTV WORLD FRANCE', cmdlist=cmdlist, finishedCallback=None)
                        elif returnValue =="com_270":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia601409.us.archive.org/7/items/iptvworldfr/IPTVWORLDFR014.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='IPTV WORLD FRANCE', cmdlist=cmdlist, finishedCallback=None)
                        elif returnValue =="com_271":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia601409.us.archive.org/7/items/iptvworldfr/IPTVWORLDFR015.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='IPTV WORLD FRANCE', cmdlist=cmdlist, finishedCallback=None)
                        elif returnValue =="com_272":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia601409.us.archive.org/7/items/iptvworldfr/IPTVWORLDFR016.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='IPTV WORLD FRANCE', cmdlist=cmdlist, finishedCallback=None)
                        elif returnValue =="com_273":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia601409.us.archive.org/7/items/iptvworldfr/IPTVWORLDFR017.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='IPTV WORLD FRANCE', cmdlist=cmdlist, finishedCallback=None)
                        elif returnValue =="com_274":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia601409.us.archive.org/7/items/iptvworldfr/IPTVWORLDFR018.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='IPTV WORLD FRANCE', cmdlist=cmdlist, finishedCallback=None)
                        elif returnValue =="com_275":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia601409.us.archive.org/7/items/iptvworldfr/IPTVWORLDFR019.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='IPTV WORLD FRANCE', cmdlist=cmdlist, finishedCallback=None)
                        elif returnValue =="com_276":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia601409.us.archive.org/7/items/iptvworldfr/IPTVWORLDFR020.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='IPTV WORD FRANCE', cmdlist=cmdlist, finishedCallback=None)
                        elif returnValue =="com_277":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia601409.us.archive.org/7/items/iptvworldfr/IPTVWORLDFR021.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='IPTV WORD FRANCE', cmdlist=cmdlist, finishedCallback=None)
                        elif returnValue =="com_278":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia601409.us.archive.org/7/items/iptvworldfr/IPTVWORLDFR022.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='IPTV WORD FRANCE', cmdlist=cmdlist, finishedCallback=None)
                        elif returnValue =="com_279":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia601409.us.archive.org/7/items/iptvworldfr/IPTVWORLDFR023.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='IPTV WORD FRANCE', cmdlist=cmdlist, finishedCallback=None)
                        elif returnValue =="com_280":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia601409.us.archive.org/7/items/iptvworldfr/IPTVWORLDFR024.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='IPTV WORLD FRANCE', cmdlist=cmdlist, finishedCallback=None)
                        elif returnValue =="com_281":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia601409.us.archive.org/7/items/iptvworldfr/IPTVWORLDFR025.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='IPTV WORLD FRANCE', cmdlist=cmdlist, finishedCallback=None)
                        elif returnValue =="com_282":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia601409.us.archive.org/7/items/iptvworldfr/IPTVWORLDFR026.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='IPTV WORLD FRANCE', cmdlist=cmdlist, finishedCallback=None)
                        elif returnValue =="com_283":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia601409.us.archive.org/7/items/iptvworldfr/IPTVWORLDFR027.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='IPTV WORLD FRANCE', cmdlist=cmdlist, finishedCallback=None)
                        elif returnValue =="com_284":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia601409.us.archive.org/7/items/iptvworldfr/IPTVWORLDFR028.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='IPTV WORLD FRANCE', cmdlist=cmdlist, finishedCallback=None)
                        elif returnValue =="com_285":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia601409.us.archive.org/7/items/iptvworldfr/IPTVWORLDFR029.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='IPTV WORLD FRANCE', cmdlist=cmdlist, finishedCallback=None)
                        elif returnValue =="com_286":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia601409.us.archive.org/7/items/iptvworldfr/IPTVWORLDFR030.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='IPTV WORLD FRANCE', cmdlist=cmdlist, finishedCallback=None)
                        elif returnValue =="com_287":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia601409.us.archive.org/7/items/iptvworldfr/IPTVWORLDFR031.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='IPTV WORLD FRANCE', cmdlist=cmdlist, finishedCallback=None)
                        elif returnValue =="com_288":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia601409.us.archive.org/7/items/iptvworldfr/IPTVWORLDFR032.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='IPTV WORLD FRANCE', cmdlist=cmdlist, finishedCallback=None)
                        elif returnValue =="com_289":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia601409.us.archive.org/7/items/iptvworldfr/IPTVWORLDFR033.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='IPTV WORLD FRANCE', cmdlist=cmdlist, finishedCallback=None)
                        elif returnValue =="com_290":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia601409.us.archive.org/7/items/iptvworldfr/IPTVWORLDFR034.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='IPTV WORLD FRANCE', cmdlist=cmdlist, finishedCallback=None)
                        elif returnValue =="com_291":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia601409.us.archive.org/7/items/iptvworldfr/IPTVWORLDFR035.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='IPTV WORD FRANCE', cmdlist=cmdlist, finishedCallback=None)
                        elif returnValue =="com_292":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia601409.us.archive.org/7/items/iptvworldfr/IPTVWORLDFR036.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='IPTV WORD FRANCE', cmdlist=cmdlist, finishedCallback=None)
                        elif returnValue =="com_293":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia601409.us.archive.org/7/items/iptvworldfr/IPTVWORLDFR037.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='IPTV WORLD FRANCE', cmdlist=cmdlist, finishedCallback=None)
                        elif returnValue =="com_294":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia601409.us.archive.org/7/items/iptvworldfr/IPTVWORLDFR038.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='IPTV WORLD FRANCE', cmdlist=cmdlist, finishedCallback=None)
                        elif returnValue =="com_295":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia601409.us.archive.org/7/items/iptvworldfr/IPTVWORLDFR039.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='IPTV WORLD FRANCE', cmdlist=cmdlist, finishedCallback=None)
                        elif returnValue =="com_296":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia601409.us.archive.org/7/items/iptvworldfr/IPTVWORLDFR040.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='IPTV WORLD FRANCE', cmdlist=cmdlist, finishedCallback=None)
                        elif returnValue =="com_297":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia601409.us.archive.org/7/items/iptvworldfr/IPTVWORLDFR041.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='IPTV WORLD FRANCE', cmdlist=cmdlist, finishedCallback=None)
                        elif returnValue =="com_298":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia601409.us.archive.org/7/items/iptvworldfr/IPTVWORLDFR042.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='IPTV WORLD FRANCE', cmdlist=cmdlist, finishedCallback=None)
                        elif returnValue =="com_299":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia601409.us.archive.org/7/items/iptvworldfr/IPTVWORLDFR043.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='IPTV WORLD FRANCE', cmdlist=cmdlist, finishedCallback=None)
                        elif returnValue =="com_300":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia601409.us.archive.org/7/items/iptvworldfr/IPTVWORLDFR044.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='IPTV WORLD FRANCE', cmdlist=cmdlist, finishedCallback=None)
                        elif returnValue =="com_301":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia601409.us.archive.org/7/items/iptvworldfr/IPTVWORLDFR045.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='IPTV WORLD FRANCE', cmdlist=cmdlist, finishedCallback=None)
                        elif returnValue =="com_302":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")    
                                cmdlist.append("%s https://ia601409.us.archive.org/7/items/iptvworldfr/IPTVWORLDFR046.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='IPTV WORLD FRANCE', cmdlist=cmdlist, finishedCallback=None)
                        elif returnValue =="com_303":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia601409.us.archive.org/7/items/iptvworldfr/IPTVWORLDFR047.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='IPTV WORLD FRANCE', cmdlist=cmdlist, finishedCallback=None)
                        elif returnValue =="com_304":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia601409.us.archive.org/7/items/iptvworldfr/IPTVWORLDFR048.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='IPTV WORLD FRANCE', cmdlist=cmdlist, finishedCallback=None)
                        elif returnValue =="com_305":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia601409.us.archive.org/7/items/iptvworldfr/IPTVWORLDFR049.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='IPTV WORLD FRANCE', cmdlist=cmdlist, finishedCallback=None)
                        elif returnValue =="com_306":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia601409.us.archive.org/7/items/iptvworldfr/IPTVWORLDFR050.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='IPTV WORLD FRANCE', cmdlist=cmdlist, finishedCallback=None)
                        elif returnValue =="com_307":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia601409.us.archive.org/7/items/iptvworldfr/IPTVWORLDFR051.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='IPTV WORLD FRANCE', cmdlist=cmdlist, finishedCallback=None)
                        elif returnValue =="com_308":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia601409.us.archive.org/7/items/iptvworldfr/IPTVWORLDFR052.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='IPTV WORLD FRANCE', cmdlist=cmdlist, finishedCallback=None)
                        elif returnValue =="com_309":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia601409.us.archive.org/7/items/iptvworldfr/IPTVWORLDFR053.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='IPTV WORLD FRANCE', cmdlist=cmdlist, finishedCallback=None)
                        elif returnValue =="com_310":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia601409.us.archive.org/7/items/iptvworldfr/IPTVWORLDFR054.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='IPTV WORLD FRANCE', cmdlist=cmdlist, finishedCallback=None)
                        elif returnValue =="com_311":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia601409.us.archive.org/7/items/iptvworldfr/IPTVWORLDFR055.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='IPTV WORLD FRANCE', cmdlist=cmdlist, finishedCallback=None)
                        elif returnValue =="com_312":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia601409.us.archive.org/7/items/iptvworldfr/IPTVWORLDFR056.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='IPTV WORLD FRANCE', cmdlist=cmdlist, finishedCallback=None)
                        elif returnValue =="com_313":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia601409.us.archive.org/7/items/iptvworldfr/IPTVWORLDFR057.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='IPTV WORLD FRANCE', cmdlist=cmdlist, finishedCallback=None)
                        elif returnValue =="com_314":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia601409.us.archive.org/7/items/iptvworldfr/IPTVWORLDFR058.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='IPTV WORLD FRANCE', cmdlist=cmdlist, finishedCallback=None)
                        elif returnValue =="com_315":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia601409.us.archive.org/7/items/iptvworldfr/IPTVWORLDFR059.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='IPTV WORLD FRANCE', cmdlist=cmdlist, finishedCallback=None)
                        elif returnValue =="com_316":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia601409.us.archive.org/7/items/iptvworldfr/IPTVWORLDFR060.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='IPTV WORLD FRANCE', cmdlist=cmdlist, finishedCallback=None)
                        elif returnValue =="com_317":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia601409.us.archive.org/7/items/iptvworldfr/IPTVWORLDFR061.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='IPTV WORLD FRANCE', cmdlist=cmdlist, finishedCallback=None)
                        elif returnValue =="com_318":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia601409.us.archive.org/7/items/iptvworldfr/IPTVWORLDFR062.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='IPTV WORLD FRANCE', cmdlist=cmdlist, finishedCallback=None)
                        elif returnValue =="com_319":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia601409.us.archive.org/7/items/iptvworldfr/IPTVWORLDFR063.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='IPTV WORLD FRANCE', cmdlist=cmdlist, finishedCallback=None)
                        elif returnValue =="com_320":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia601409.us.archive.org/7/items/iptvworldfr/IPTVWORLDFR064.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='IPTV WORD FRANCE', cmdlist=cmdlist, finishedCallback=None)
                        elif returnValue =="com_321":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia601409.us.archive.org/7/items/iptvworldfr/IPTVWORLDFR065.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='IPTV WORD FRANCE', cmdlist=cmdlist, finishedCallback=None)
                        elif returnValue =="com_322":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia601409.us.archive.org/7/items/iptvworldfr/IPTVWORLDFR066.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='IPTV WORD FRANCE', cmdlist=cmdlist, finishedCallback=None)
                        elif returnValue =="com_323":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia601409.us.archive.org/7/items/iptvworldfr/IPTVWORLDFR067.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='IPTV WORD FRANCE', cmdlist=cmdlist, finishedCallback=None)
                        elif returnValue =="com_324":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia601409.us.archive.org/7/items/iptvworldfr/IPTVWORLDFR068.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='IPTV WORLD FRANCE', cmdlist=cmdlist, finishedCallback=None)
                        elif returnValue =="com_325":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia601409.us.archive.org/7/items/iptvworldfr/IPTVWORLDFR069.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='IPTV WORLD FRANCE', cmdlist=cmdlist, finishedCallback=None)
                        elif returnValue =="com_326":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia601409.us.archive.org/7/items/iptvworldfr/IPTVWORLDFR070.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='IPTV WORLD FRANCE', cmdlist=cmdlist, finishedCallback=None)
                        elif returnValue =="com_327":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia601409.us.archive.org/7/items/iptvworldfr/IPTVWORLDFR071.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='IPTV WORLD FRANCE', cmdlist=cmdlist, finishedCallback=None)
                        elif returnValue =="com_328":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia601409.us.archive.org/7/items/iptvworldfr/IPTVWORLDFR072.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='IPTV WORLD FRANCE', cmdlist=cmdlist, finishedCallback=None)
                        elif returnValue =="com_329":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia601409.us.archive.org/7/items/iptvworldfr/IPTVWORLDFR073.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='IPTV WORLD FRANCE', cmdlist=cmdlist, finishedCallback=None)
                        elif returnValue =="com_330":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia601409.us.archive.org/7/items/iptvworldfr/IPTVWORLDFR074.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='IPTV WORLD FRANCE', cmdlist=cmdlist, finishedCallback=None)
                        elif returnValue =="com_331":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia601409.us.archive.org/7/items/iptvworldfr/IPTVWORLDFR075.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='IPTV WORLD FRANCE', cmdlist=cmdlist, finishedCallback=None)
                        elif returnValue =="com_332":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia601409.us.archive.org/7/items/iptvworldfr/IPTVWORLDFR076.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='IPTV WORLD FRANCE', cmdlist=cmdlist, finishedCallback=None)
                        elif returnValue =="com_333":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia601409.us.archive.org/7/items/iptvworldfr/IPTVWORLDFR077.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='IPTV WORLD FRANCE', cmdlist=cmdlist, finishedCallback=None)
                        elif returnValue =="com_334":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia601409.us.archive.org/7/items/iptvworldfr/IPTVWORLDFR078.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='IPTV WORLD FRANCE', cmdlist=cmdlist, finishedCallback=None)
                        elif returnValue =="com_335":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia601409.us.archive.org/7/items/iptvworldfr/IPTVWORLDFR079.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='IPTV WORD FRANCE', cmdlist=cmdlist, finishedCallback=None)
                        elif returnValue =="com_336":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia601409.us.archive.org/7/items/iptvworldfr/IPTVWORLDFR080.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='IPTV WORD FRANCE', cmdlist=cmdlist, finishedCallback=None)
                        elif returnValue =="com_337":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia601409.us.archive.org/7/items/iptvworldfr/IPTVWORLDFR081.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='IPTV WORLD FRANCE', cmdlist=cmdlist, finishedCallback=None)
                        elif returnValue =="com_338":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia601409.us.archive.org/7/items/iptvworldfr/IPTVWORLDFR082.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='IPTV WORLD FRANCE', cmdlist=cmdlist, finishedCallback=None)
                        elif returnValue =="com_339":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia601409.us.archive.org/7/items/iptvworldfr/IPTVWORLDFR083.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='IPTV WORLD FRANCE', cmdlist=cmdlist, finishedCallback=None)
                        elif returnValue =="com_340":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia601409.us.archive.org/7/items/iptvworldfr/IPTVWORLDFR084.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='IPTV WORLD FRANCE', cmdlist=cmdlist, finishedCallback=None)
                        elif returnValue =="com_341":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia601409.us.archive.org/7/items/iptvworldfr/IPTVWORLDFR085.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='IPTV WORLD FRANCE', cmdlist=cmdlist, finishedCallback=None)
                        elif returnValue =="com_342":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia601409.us.archive.org/7/items/iptvworldfr/IPTVWORLDFR086.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='IPTV WORLD FRANCE', cmdlist=cmdlist, finishedCallback=None)
                        elif returnValue =="com_343":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia601409.us.archive.org/7/items/iptvworldfr/IPTVWORLDFR087.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='IPTV WORLD FRANCE', cmdlist=cmdlist, finishedCallback=None)
                        elif returnValue =="com_344":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia601409.us.archive.org/7/items/iptvworldfr/IPTVWORLDFR088.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='IPTV WORLD FRANCE', cmdlist=cmdlist, finishedCallback=None)
                        elif returnValue =="com_345":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia601409.us.archive.org/7/items/iptvworldfr/IPTVWORLDFR089.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='IPTV WORD FRANCE', cmdlist=cmdlist, finishedCallback=None)
                        elif returnValue =="com_346":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia601409.us.archive.org/7/items/iptvworldfr/IPTVWORLDFR090.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='IPTV WORLD FRANCE', cmdlist=cmdlist, finishedCallback=None)
                        elif returnValue =="com_347":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia601409.us.archive.org/7/items/iptvworldfr/IPTVWORLDFR091.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='IPTV WORLD FRANCE', cmdlist=cmdlist, finishedCallback=None)
                        elif returnValue =="com_348":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia601409.us.archive.org/7/items/iptvworldfr/IPTVWORLDFR092.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='IPTV WORLD FRANCE', cmdlist=cmdlist, finishedCallback=None)
                        elif returnValue =="com_349":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia601409.us.archive.org/7/items/iptvworldfr/IPTVWORLDFR093.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='IPTV WORLD FRANCE', cmdlist=cmdlist, finishedCallback=None)
                        elif returnValue =="com_350":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia601409.us.archive.org/7/items/iptvworldfr/IPTVWORLDFR094.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='IPTV WORLD FRANCE', cmdlist=cmdlist, finishedCallback=None)
                        elif returnValue =="com_351":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia601409.us.archive.org/7/items/iptvworldfr/IPTVWORLDFR095.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='IPTV WORLD FRANCE', cmdlist=cmdlist, finishedCallback=None)
                        elif returnValue =="com_352":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia601409.us.archive.org/7/items/iptvworldfr/IPTVWORLDFR096.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='IPTV WORLD FRANCE', cmdlist=cmdlist, finishedCallback=None)
                        elif returnValue =="com_353":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia601409.us.archive.org/7/items/iptvworldfr/IPTVWORLDFR097.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='IPTV WORLD FRANCE', cmdlist=cmdlist, finishedCallback=None)
                        elif returnValue =="com_354":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia601409.us.archive.org/7/items/iptvworldfr/IPTVWORLDFR098.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='IPTV WORLD FRANCE', cmdlist=cmdlist, finishedCallback=None)
                        elif returnValue =="com_355":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia601409.us.archive.org/7/items/iptvworldfr/IPTVWORLDFR099.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='IPTV WORLD FRANCE', cmdlist=cmdlist, finishedCallback=None)
                        elif returnValue =="com_356":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia601409.us.archive.org/7/items/iptvworldfr/IPTVWORLDFR100.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='IPTV WORLD FRANCE', cmdlist=cmdlist, finishedCallback=None)
                        elif returnValue =="com_357":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia601409.us.archive.org/7/items/iptvworldfr/IPTVWORLDFR101.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='IPTV WORD FRANCE', cmdlist=cmdlist, finishedCallback=None)
                        elif returnValue =="com_358":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia601409.us.archive.org/7/items/iptvworldfr/IPTVWORLDFR102.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='IPTV WORD FRANCE', cmdlist=cmdlist, finishedCallback=None)
                        elif returnValue =="com_359":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia601409.us.archive.org/7/items/iptvworldfr/IPTVWORLDFR103.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='IPTV WORLD FRANCE', cmdlist=cmdlist, finishedCallback=None)
                        elif returnValue =="com_360":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia601409.us.archive.org/7/items/iptvworldfr/IPTVWORLDFR104.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='IPTV WORLD FRANCE', cmdlist=cmdlist, finishedCallback=None)
                        elif returnValue =="com_361":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia601409.us.archive.org/7/items/iptvworldfr/IPTVWORLDFR105.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='IPTV WORLD FRANCE', cmdlist=cmdlist, finishedCallback=None)
                        elif returnValue =="com_362":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia601409.us.archive.org/7/items/iptvworldfr/IPTVWORLDFR106.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='IPTV WORLD FRANCE', cmdlist=cmdlist, finishedCallback=None)
                        elif returnValue =="com_363":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia601409.us.archive.org/7/items/iptvworldfr/IPTVWORLDFR107.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='IPTV WORLD FRANCE', cmdlist=cmdlist, finishedCallback=None)
                        elif returnValue =="com_364":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia601409.us.archive.org/7/items/iptvworldfr/IPTVWORLDFR108.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='IPTV WORLD FRANCE', cmdlist=cmdlist, finishedCallback=None)
                        elif returnValue =="com_365":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia601409.us.archive.org/7/items/iptvworldfr/IPTVWORLDFR109.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='IPTV WORLD FRANCE', cmdlist=cmdlist, finishedCallback=None)
                        elif returnValue =="com_366":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia601409.us.archive.org/7/items/iptvworldfr/IPTVWORLDFR110.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='IPTV WORLD FRANCE', cmdlist=cmdlist, finishedCallback=None)
                        elif returnValue =="com_367":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia601409.us.archive.org/7/items/iptvworldfr/IPTVWORLDFR111.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='IPTV WORD FRANCE', cmdlist=cmdlist, finishedCallback=None)
                        elif returnValue =="com_368":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia601409.us.archive.org/7/items/iptvworldfr/IPTVWORLDFR112.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='IPTV WORD FRANCE', cmdlist=cmdlist, finishedCallback=None)
                        elif returnValue =="com_369":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia601409.us.archive.org/7/items/iptvworldfr/IPTVWORLDFR113.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='IPTV WORLD FRANCE', cmdlist=cmdlist, finishedCallback=None)
                        elif returnValue =="com_370":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia601409.us.archive.org/7/items/iptvworldfr/IPTVWORLDFR114.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='IPTV WORLD FRANCE', cmdlist=cmdlist, finishedCallback=None)
                        elif returnValue =="com_371":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia601409.us.archive.org/7/items/iptvworldfr/IPTVWORLDFR115.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='IPTV WORLD FRANCE', cmdlist=cmdlist, finishedCallback=None)
                        elif returnValue =="com_372":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia601409.us.archive.org/7/items/iptvworldfr/IPTVWORLDFR116.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='IPTV WORLD FRANCE', cmdlist=cmdlist, finishedCallback=None)
                        elif returnValue =="com_373":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia601409.us.archive.org/7/items/iptvworldfr/IPTVWORLDFR117.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='IPTV WORLD FRANCE', cmdlist=cmdlist, finishedCallback=None)
                        elif returnValue =="com_374":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia601409.us.archive.org/7/items/iptvworldfr/IPTVWORLDFR118.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='IPTV WORLD FRANCE', cmdlist=cmdlist, finishedCallback=None)
                        elif returnValue =="com_375":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia601409.us.archive.org/7/items/iptvworldfr/IPTVWORLDFR119.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='IPTV WORLD FRANCE', cmdlist=cmdlist, finishedCallback=None)
                        elif returnValue =="com_376":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia601409.us.archive.org/7/items/iptvworldfr/IPTVWORLDFR120.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='IPTV WORLD FRANCE', cmdlist=cmdlist, finishedCallback=None)
                        elif returnValue =="com_377":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia801409.us.archive.org/29/items/iptvworld_201911/IPTVWORLDGR001.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='IPTV WORLD GRESS', cmdlist=cmdlist, finishedCallback=None)
                        elif returnValue =="com_378":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia801409.us.archive.org/29/items/iptvworld_201911/IPTVWORLDGR002.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='IPTV WORLD GRESS', cmdlist=cmdlist, finishedCallback=None)
                        elif returnValue =="com_379":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia801409.us.archive.org/29/items/iptvworld_201911/IPTVWORLDGR003.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='IPTV WORLD GRESS', cmdlist=cmdlist, finishedCallback=None)
                        elif returnValue =="com_380":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia801409.us.archive.org/29/items/iptvworld_201911/IPTVWORLDGR004.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='IPTV WORLD GRESS', cmdlist=cmdlist, finishedCallback=None)
                        elif returnValue =="com_381":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia801409.us.archive.org/29/items/iptvworld_201911/IPTVWORLDGR005.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='IPTV WORLD GRESS', cmdlist=cmdlist, finishedCallback=None)
                        elif returnValue =="com_0382":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia601403.us.archive.org/21/items/iptvworldgr-001/IPTVWORLDGRN0.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='IPTV GRESS', cmdlist=cmdlist, finishedCallback=None)
                        elif returnValue =="com_0383":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia601403.us.archive.org/21/items/iptvworldgr-001/IPTVWORLDGRN20.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='IPTV GRESS', cmdlist=cmdlist, finishedCallback=None)
                        elif returnValue =="com_0384":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia601403.us.archive.org/21/items/iptvworldgr-001/IPTVWORLDGRN50.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='IPTV GRESS', cmdlist=cmdlist, finishedCallback=None)
                        elif returnValue =="com_0385":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia601403.us.archive.org/21/items/iptvworldgr-001/IPTVWORLDGRNALL.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='IPTV GRESS', cmdlist=cmdlist, finishedCallback=None)
                        elif returnValue =="com_382":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia601403.us.archive.org/21/items/iptvworldgr-001/IPTVWORLDGR001.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='IPTV GRESS', cmdlist=cmdlist, finishedCallback=None)
                        elif returnValue =="com_383":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia601403.us.archive.org/21/items/iptvworldgr-001/IPTVWORLDGR002.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='IPTV GRESS', cmdlist=cmdlist, finishedCallback=None)
                        elif returnValue =="com_384":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia601403.us.archive.org/21/items/iptvworldgr-001/IPTVWORLDGR003.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='IPTV GRESS', cmdlist=cmdlist, finishedCallback=None)
                        elif returnValue =="com_385":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia601403.us.archive.org/21/items/iptvworldgr-001/IPTVWORLDGR004.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='IPTV GRESS', cmdlist=cmdlist, finishedCallback=None)
                        elif returnValue =="com_386":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia601403.us.archive.org/21/items/iptvworldgr-001/IPTVWORLDGR005.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='IPTV GRESS', cmdlist=cmdlist, finishedCallback=None)
                        elif returnValue =="com_387":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia601403.us.archive.org/21/items/iptvworldgr-001/IPTVWORLDGR006.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='IPTV GRESS', cmdlist=cmdlist, finishedCallback=None)
                        elif returnValue =="com_388":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia601403.us.archive.org/21/items/iptvworldgr-001/IPTVWORLDGR007.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='IPTV GRESS', cmdlist=cmdlist, finishedCallback=None)
                        elif returnValue =="com_389":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia601403.us.archive.org/21/items/iptvworldgr-001/IPTVWORLDGR008.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='IPTV GRESS', cmdlist=cmdlist, finishedCallback=None)
                        elif returnValue =="com_390":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia601403.us.archive.org/21/items/iptvworldgr-001/IPTVWORLDGR009.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='IPTV GRESS', cmdlist=cmdlist, finishedCallback=None)
                        elif returnValue =="com_391":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia601403.us.archive.org/21/items/iptvworldgr-001/IPTVWORLDGR010.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='IPTV GRESS', cmdlist=cmdlist, finishedCallback=None)
                        elif returnValue =="com_392":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia601403.us.archive.org/21/items/iptvworldgr-001/IPTVWORLDGR011.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='IPTV GRESS', cmdlist=cmdlist, finishedCallback=None)
                        elif returnValue =="com_393":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia601403.us.archive.org/21/items/iptvworldgr-001/IPTVWORLDGR012.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='IPTV GRESS', cmdlist=cmdlist, finishedCallback=None)
                        elif returnValue =="com_394":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia601403.us.archive.org/21/items/iptvworldgr-001/IPTVWORLDGR013.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='IPTV GRESS', cmdlist=cmdlist, finishedCallback=None)
                        elif returnValue =="com_395":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia601403.us.archive.org/21/items/iptvworldgr-001/IPTVWORLDGR014.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='IPTV GRESS', cmdlist=cmdlist, finishedCallback=None)
                        elif returnValue =="com_396":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia601403.us.archive.org/21/items/iptvworldgr-001/IPTVWORLDGR015.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='IPTV GRESS', cmdlist=cmdlist, finishedCallback=None)
                        elif returnValue =="com_397":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia601403.us.archive.org/21/items/iptvworldgr-001/IPTVWORLDGR016.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='IPTV GRESS', cmdlist=cmdlist, finishedCallback=None)
                        elif returnValue =="com_398":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia601403.us.archive.org/21/items/iptvworldgr-001/IPTVWORLDGR017.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='IPTV GRESS', cmdlist=cmdlist, finishedCallback=None)
                        elif returnValue =="com_399":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia601403.us.archive.org/21/items/iptvworldgr-001/IPTVWORLDGR018.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='IPTV GRESS', cmdlist=cmdlist, finishedCallback=None)
                        elif returnValue =="com_400":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia601403.us.archive.org/21/items/iptvworldgr-001/IPTVWORLDGR019.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='IPTV GRESS', cmdlist=cmdlist, finishedCallback=None)
                        elif returnValue =="com_401":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia601403.us.archive.org/21/items/iptvworldgr-001/IPTVWORLDGR020.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='IPTV GRESS', cmdlist=cmdlist, finishedCallback=None)
                        elif returnValue =="com_402":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia601403.us.archive.org/21/items/iptvworldgr-001/IPTVWORLDGR021.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='IPTV GRESS', cmdlist=cmdlist, finishedCallback=None)
                        elif returnValue =="com_403":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia601403.us.archive.org/21/items/iptvworldgr-001/IPTVWORLDGR022.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='IPTV GRESS', cmdlist=cmdlist, finishedCallback=None)
                        elif returnValue =="com_404":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia601403.us.archive.org/21/items/iptvworldgr-001/IPTVWORLDGR023.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='IPTV GRESS', cmdlist=cmdlist, finishedCallback=None)
                        elif returnValue =="com_405":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia601403.us.archive.org/21/items/iptvworldgr-001/IPTVWORLDGR024.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='IPTV GRESS', cmdlist=cmdlist, finishedCallback=None)
                        elif returnValue =="com_406":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia601403.us.archive.org/21/items/iptvworldgr-001/IPTVWORLDGR025.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='IPTV GRESS', cmdlist=cmdlist, finishedCallback=None)
                        elif returnValue =="com_407":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia601403.us.archive.org/21/items/iptvworldgr-001/IPTVWORLDGR026.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='IPTV GRESS', cmdlist=cmdlist, finishedCallback=None)
                        elif returnValue =="com_408":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia601403.us.archive.org/21/items/iptvworldgr-001/IPTVWORLDGR027.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='IPTV GRESS', cmdlist=cmdlist, finishedCallback=None)
                        elif returnValue =="com_409":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia601403.us.archive.org/21/items/iptvworldgr-001/IPTVWORLDGR028.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='IPTV GRESS', cmdlist=cmdlist, finishedCallback=None)
                        elif returnValue =="com_410":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'") 
                                cmdlist.append("%s https://ia601403.us.archive.org/21/items/iptvworldgr-001/IPTVWORLDGR029.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='IPTV GRESS', cmdlist=cmdlist, finishedCallback=None)
                        elif returnValue =="com_411":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia601403.us.archive.org/21/items/iptvworldgr-001/IPTVWORLDGR030.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='IPTV GRESS', cmdlist=cmdlist, finishedCallback=None)
                        elif returnValue =="com_412":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia601403.us.archive.org/21/items/iptvworldgr-001/IPTVWORLDGR031.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='IPTV GRESS', cmdlist=cmdlist, finishedCallback=None)
                        elif returnValue =="com_413":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia601403.us.archive.org/21/items/iptvworldgr-001/IPTVWORLDGR032.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='IPTV GRESS', cmdlist=cmdlist, finishedCallback=None)
                        elif returnValue =="com_414":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")    
                                cmdlist.append("%s https://ia601403.us.archive.org/21/items/iptvworldgr-001/IPTVWORLDGR033.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='IPTV WORLD GRESS', cmdlist=cmdlist, finishedCallback=None)
                        elif returnValue =="com_415":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia601403.us.archive.org/21/items/iptvworldgr-001/IPTVWORLDGR034.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='IPTV GRESS', cmdlist=cmdlist, finishedCallback=None)
                        elif returnValue =="com_416":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia601403.us.archive.org/21/items/iptvworldgr-001/IPTVWORLDGR035.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='IPTV GRESS', cmdlist=cmdlist, finishedCallback=None)
                        elif returnValue =="com_417":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia601403.us.archive.org/21/items/iptvworldgr-001/IPTVWORLDGR036.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='IPTV GRESS', cmdlist=cmdlist, finishedCallback=None)
                        elif returnValue =="com_418":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia601403.us.archive.org/21/items/iptvworldgr-001/IPTVWORLDGR037.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='IPTV GRESS', cmdlist=cmdlist, finishedCallback=None)
                        elif returnValue =="com_419":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia601403.us.archive.org/21/items/iptvworldgr-001/IPTVWORLDGR038.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='IPTV GRESS', cmdlist=cmdlist, finishedCallback=None)
                        elif returnValue =="com_420":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia601403.us.archive.org/21/items/iptvworldgr-001/IPTVWORLDGR039.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='IPTV GRESS', cmdlist=cmdlist, finishedCallback=None)
                        elif returnValue =="com_421":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia601403.us.archive.org/21/items/iptvworldgr-001/IPTVWORLDGR040.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='IPTV GRESS', cmdlist=cmdlist, finishedCallback=None)
                        elif returnValue =="com_422":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia601403.us.archive.org/21/items/iptvworldgr-001/IPTVWORLDGR041.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='IPTV GRESS', cmdlist=cmdlist, finishedCallback=None)
                        elif returnValue =="com_423":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia601403.us.archive.org/21/items/iptvworldgr-001/IPTVWORLDGR042.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='IPTV GRESS', cmdlist=cmdlist, finishedCallback=None)
                        elif returnValue =="com_424":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia601403.us.archive.org/21/items/iptvworldgr-001/IPTVWORLDGR043.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='IPTV GRESS', cmdlist=cmdlist, finishedCallback=None)
                        elif returnValue =="com_425":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia601403.us.archive.org/21/items/iptvworldgr-001/IPTVWORLDGR044.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='IPTV GRESS', cmdlist=cmdlist, finishedCallback=None)
                        elif returnValue =="com_426":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia601403.us.archive.org/21/items/iptvworldgr-001/IPTVWORLDGR045.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='IPTV GRESS', cmdlist=cmdlist, finishedCallback=None)
                        elif returnValue =="com_427":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia601403.us.archive.org/21/items/iptvworldgr-001/IPTVWORLDGR046.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='IPTV GRESS', cmdlist=cmdlist, finishedCallback=None)
                        elif returnValue =="com_428":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia601403.us.archive.org/21/items/iptvworldgr-001/IPTVWORLDGR047.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='IPTV GRESS', cmdlist=cmdlist, finishedCallback=None)
                        elif returnValue =="com_429":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia601403.us.archive.org/21/items/iptvworldgr-001/IPTVWORLDGR048.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='IPTV GRESS', cmdlist=cmdlist, finishedCallback=None)
                        elif returnValue =="com_430":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'") 
                                cmdlist.append("%s https://ia601403.us.archive.org/21/items/iptvworldgr-001/IPTVWORLDGR049.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='IPTV GRESS', cmdlist=cmdlist, finishedCallback=None)
                        elif returnValue =="com_431":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia601403.us.archive.org/21/items/iptvworldgr-001/IPTVWORLDGR050.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='IPTV GRESS', cmdlist=cmdlist, finishedCallback=None)
                        elif returnValue =="com_432":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia601403.us.archive.org/21/items/iptvworldgr-001/IPTVWORLDUS001.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='IPTV USA', cmdlist=cmdlist, finishedCallback=None)
                        elif returnValue =="com_433":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia801409.us.archive.org/29/items/iptvworld_201911/IPTVWORLDUS002.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='IPTV USA', cmdlist=cmdlist, finishedCallback=None)
                        elif returnValue =="com_434":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")    
                                cmdlist.append("%s https://ia801409.us.archive.org/29/items/iptvworld_201911/IPTVWORLDUS003.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='IPTV USA', cmdlist=cmdlist, finishedCallback=None)
                        elif returnValue =="com_435":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia801409.us.archive.org/29/items/iptvworld_201911/IPTVWORLDUS004.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='IPTV USA', cmdlist=cmdlist, finishedCallback=None)
                        elif returnValue =="com_436":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia801409.us.archive.org/29/items/iptvworld_201911/IPTVWORLDUS005.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='IPTV USA', cmdlist=cmdlist, finishedCallback=None)
                        elif returnValue =="com_437":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia801409.us.archive.org/29/items/iptvworld_201911/IPTVWORLDUS006.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='IPTV WORLD', cmdlist=cmdlist, finishedCallback=None)
                        elif returnValue =="com_0438":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")    
                                cmdlist.append("%s https://ia801409.us.archive.org/29/items/iptvworld_201911/IPTVWORLDUSN10.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='IPTV WORLD', cmdlist=cmdlist, finishedCallback=None)
                        elif returnValue =="com_0439":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia801409.us.archive.org/29/items/iptvworld_201911/IPTVWORLDUSN20.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='IPTV WORLD', cmdlist=cmdlist, finishedCallback=None)
                        elif returnValue =="com_0440":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia801409.us.archive.org/29/items/iptvworld_201911/IPTVWORLDUSN50.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='IPTV WORLD', cmdlist=cmdlist, finishedCallback=None)
                        elif returnValue =="com_0441":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia801409.us.archive.org/29/items/iptvworld_201911/IPTVWORLDUSN100.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='IPTV WORLD', cmdlist=cmdlist, finishedCallback=None)
                        elif returnValue =="com_438":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")    
                                cmdlist.append("%s https://ia801409.us.archive.org/29/items/iptvworld_201911/IPTVWORLDUS001.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='IPTV WORLD', cmdlist=cmdlist, finishedCallback=None)
                        elif returnValue =="com_439":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia801409.us.archive.org/29/items/iptvworld_201911/IPTVWORLDUS002.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='IPTV WORLD', cmdlist=cmdlist, finishedCallback=None)
                        elif returnValue =="com_440":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia801409.us.archive.org/29/items/iptvworld_201911/IPTVWORLDUS003.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='IPTV WORLD', cmdlist=cmdlist, finishedCallback=None)
                        elif returnValue =="com_441":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia801409.us.archive.org/29/items/iptvworld_201911/IPTVWORLDUS004.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='IPTV WORLD', cmdlist=cmdlist, finishedCallback=None)
                        elif returnValue =="com_442":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia801409.us.archive.org/29/items/iptvworld_201911/IPTVWORLDUS005.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='IPTV WORLD', cmdlist=cmdlist, finishedCallback=None)
                        elif returnValue =="com_443":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia801409.us.archive.org/29/items/iptvworld_201911/IPTVWORLDUS006.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='IPTV WORLD', cmdlist=cmdlist, finishedCallback=None)
                        elif returnValue =="com_444":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia801409.us.archive.org/29/items/iptvworld_201911/IPTVWORLDUS007.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='IPTV WORLD', cmdlist=cmdlist, finishedCallback=None)
                        elif returnValue =="com_445":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia801409.us.archive.org/29/items/iptvworld_201911/IPTVWORLDUS008.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='IPTV WORLD', cmdlist=cmdlist, finishedCallback=None)
                        elif returnValue =="com_446":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia801409.us.archive.org/29/items/iptvworld_201911/IPTVWORLDUS009.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='IPTV WORLD', cmdlist=cmdlist, finishedCallback=None)
                        elif returnValue =="com_447":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia801409.us.archive.org/29/items/iptvworld_201911/IPTVWORLDUS010.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='IPTV WORLD', cmdlist=cmdlist, finishedCallback=None)
                        elif returnValue =="com_448":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia801409.us.archive.org/29/items/iptvworld_201911/IPTVWORLDUS011.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='IPTV WORLD', cmdlist=cmdlist, finishedCallback=None)
                        elif returnValue =="com_449":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia801409.us.archive.org/29/items/iptvworld_201911/IPTVWORLDUS012.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='IPTV WORLD', cmdlist=cmdlist, finishedCallback=None)
                        elif returnValue =="com_450":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia801409.us.archive.org/29/items/iptvworld_201911/IPTVWORLDUS013.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='IPTV WORLD', cmdlist=cmdlist, finishedCallback=None)
                        elif returnValue =="com_451":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia801409.us.archive.org/29/items/iptvworld_201911/IPTVWORLDUS014.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='IPTV USA', cmdlist=cmdlist, finishedCallback=None)
                        elif returnValue =="com_452":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia801409.us.archive.org/29/items/iptvworld_201911/IPTVWORLDUS015.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='IPTV USA', cmdlist=cmdlist, finishedCallback=None)
                        elif returnValue =="com_453":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia801409.us.archive.org/29/items/iptvworld_201911/IPTVWORLDUS016.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='IPTV USA', cmdlist=cmdlist, finishedCallback=None)
                        elif returnValue =="com_454":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'") 
                                cmdlist.append("%s https://ia801409.us.archive.org/29/items/iptvworld_201911/IPTVWORLDUS017.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='IPTV USA', cmdlist=cmdlist, finishedCallback=None)
                        elif returnValue =="com_455":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia801409.us.archive.org/29/items/iptvworld_201911/IPTVWORLDUS018.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='IPTV USA', cmdlist=cmdlist, finishedCallback=None)
                        elif returnValue =="com_456":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia801409.us.archive.org/29/items/iptvworld_201911/IPTVWORLDUS019.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='IPTV USA', cmdlist=cmdlist, finishedCallback=None)
                        elif returnValue =="com_457":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia801409.us.archive.org/29/items/iptvworld_201911/IPTVWORLDUS020.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='IPTV USA', cmdlist=cmdlist, finishedCallback=None)
                        elif returnValue =="com_458":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")    
                                cmdlist.append("%s https://ia801409.us.archive.org/29/items/iptvworld_201911/IPTVWORLDUS021.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='IPTV USA', cmdlist=cmdlist, finishedCallback=None)
                        elif returnValue =="com_459":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia801409.us.archive.org/29/items/iptvworld_201911/IPTVWORLDUS022.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='IPTV USA', cmdlist=cmdlist, finishedCallback=None)
                        elif returnValue =="com_460":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia801409.us.archive.org/29/items/iptvworld_201911/IPTVWORLDUS023.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='IPTV USA', cmdlist=cmdlist, finishedCallback=None)
                        elif returnValue =="com_461":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia801409.us.archive.org/29/items/iptvworld_201911/IPTVWORLDUS024.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='IPTV WORLD', cmdlist=cmdlist, finishedCallback=None)
                        elif returnValue =="com_462":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia801409.us.archive.org/29/items/iptvworld_201911/IPTVWORLDUS024.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='IPTV WORLD', cmdlist=cmdlist, finishedCallback=None)
                        elif returnValue =="com_463":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia801409.us.archive.org/29/items/iptvworld_201911/IPTVWORLDUS025.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='IPTV WORLD', cmdlist=cmdlist, finishedCallback=None)
                        elif returnValue =="com_464":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia801409.us.archive.org/29/items/iptvworld_201911/IPTVWORLDUS026.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='IPTV WORLD', cmdlist=cmdlist, finishedCallback=None)
                        elif returnValue =="com_465":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia801409.us.archive.org/29/items/iptvworld_201911/IPTVWORLDUS027.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='IPTV WORLD', cmdlist=cmdlist, finishedCallback=None)
                        elif returnValue =="com_466":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia801409.us.archive.org/29/items/iptvworld_201911/IPTVWORLDUS028.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='IPTV WORLD', cmdlist=cmdlist, finishedCallback=None)
                        elif returnValue =="com_467":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia801409.us.archive.org/29/items/iptvworld_201911/IPTVWORLDUS029.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='IPTV WORLD', cmdlist=cmdlist, finishedCallback=None)
                        elif returnValue =="com_468":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia801409.us.archive.org/29/items/iptvworld_201911/IPTVWORLDUS030.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='IPTV WORLD', cmdlist=cmdlist, finishedCallback=None)
                        elif returnValue =="com_469":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia801409.us.archive.org/29/items/iptvworld_201911/IPTVWORLDUS031.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='IPTV WORLD', cmdlist=cmdlist, finishedCallback=None)
                        elif returnValue =="com_470":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia801409.us.archive.org/29/items/iptvworld_201911/IPTVWORLDUS032.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='IPTV WORLD', cmdlist=cmdlist, finishedCallback=None)
                        elif returnValue =="com_471":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia801409.us.archive.org/29/items/iptvworld_201911/IPTVWORLDUS033.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='IPTV WORLD', cmdlist=cmdlist, finishedCallback=None)
                        elif returnValue =="com_472":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia801409.us.archive.org/29/items/iptvworld_201911/IPTVWORLDUS034.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='IPTV WORLD', cmdlist=cmdlist, finishedCallback=None)
                        elif returnValue =="com_473":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia801409.us.archive.org/29/items/iptvworld_201911/IPTVWORLDUS035.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='IPTV WORLD', cmdlist=cmdlist, finishedCallback=None)
                        elif returnValue =="com_474":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia801409.us.archive.org/29/items/iptvworld_201911/IPTVWORLDUS036.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='IPTV WORLD', cmdlist=cmdlist, finishedCallback=None)
                        elif returnValue =="com_475":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia801409.us.archive.org/29/items/iptvworld_201911/IPTVWORLDUS037.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='IPTV WORLD', cmdlist=cmdlist, finishedCallback=None)
                        elif returnValue =="com_476":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia801409.us.archive.org/29/items/iptvworld_201911/IPTVWORLDUS038.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='IPTV WORLD', cmdlist=cmdlist, finishedCallback=None)
                        elif returnValue =="com_477":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia801409.us.archive.org/29/items/iptvworld_201911/IPTVWORLDUS039.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='IPTV WORLD', cmdlist=cmdlist, finishedCallback=None)
                        elif returnValue =="com_478":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia801409.us.archive.org/29/items/iptvworld_201911/IPTVWORLDUS040.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='IPTV WORLD', cmdlist=cmdlist, finishedCallback=None)
                        elif returnValue =="com_479":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia801409.us.archive.org/29/items/iptvworld_201911/IPTVWORLDUS041.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='IPTV WORLD', cmdlist=cmdlist, finishedCallback=None)
                        elif returnValue =="com_480":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia801409.us.archive.org/29/items/iptvworld_201911/IPTVWORLDUS042.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='IPTV WORLD', cmdlist=cmdlist, finishedCallback=None)
                        elif returnValue =="com_481":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia801409.us.archive.org/29/items/iptvworld_201911/IPTVWORLDUS043.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='IPTV WORLD', cmdlist=cmdlist, finishedCallback=None)
                        elif returnValue =="com_482":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia801409.us.archive.org/29/items/iptvworld_201911/IPTVWORLDUS044.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='IPTV WORLD', cmdlist=cmdlist, finishedCallback=None)
                        elif returnValue =="com_483":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia801409.us.archive.org/29/items/iptvworld_201911/IPTVWORLDUS045.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='IPTV WORLD', cmdlist=cmdlist, finishedCallback=None)
                        elif returnValue =="com_484":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia801409.us.archive.org/29/items/iptvworld_201911/IPTVWORLDUS046.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='IPTV WORLD', cmdlist=cmdlist, finishedCallback=None)
                        elif returnValue =="com_485":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia801409.us.archive.org/29/items/iptvworld_201911/IPTVWORLDUS047.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='IPTV WORLD', cmdlist=cmdlist, finishedCallback=None)
                        elif returnValue =="com_486":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia801409.us.archive.org/29/items/iptvworld_201911/IPTVWORLDUS048.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='IPTV WORLD', cmdlist=cmdlist, finishedCallback=None)
                        elif returnValue =="com_487":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia801409.us.archive.org/29/items/iptvworld_201911/IPTVWORLDUS049.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='IPTV WORLD', cmdlist=cmdlist, finishedCallback=None)
                        elif returnValue =="com_488":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia801409.us.archive.org/29/items/iptvworld_201911/IPTVWORLDUS050.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='IPTV WORLD', cmdlist=cmdlist, finishedCallback=None)
                        elif returnValue =="com_489":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia801409.us.archive.org/29/items/iptvworld_201911/IPTVWORLDUS051.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='IPTV WORLD', cmdlist=cmdlist, finishedCallback=None)
                        elif returnValue =="com_490":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia801409.us.archive.org/29/items/iptvworld_201911/IPTVWORLDUS052.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='IPTV WORLD', cmdlist=cmdlist, finishedCallback=None)
                        elif returnValue =="com_491":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia801409.us.archive.org/29/items/iptvworld_201911/IPTVWORLDUS053.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='IPTV WORD', cmdlist=cmdlist, finishedCallback=None)
                        elif returnValue =="com_492":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia801409.us.archive.org/29/items/iptvworld_201911/IPTVWORLDUS054.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='IPTV WORD', cmdlist=cmdlist, finishedCallback=None)
                        elif returnValue =="com_493":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia801409.us.archive.org/29/items/iptvworld_201911/IPTVWORLDUS055.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='IPTV WORLD', cmdlist=cmdlist, finishedCallback=None)
                        elif returnValue =="com_494":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia801409.us.archive.org/29/items/iptvworld_201911/IPTVWORLDUS056.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='IPTV WORLD', cmdlist=cmdlist, finishedCallback=None)
                        elif returnValue =="com_495":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia801409.us.archive.org/29/items/iptvworld_201911/IPTVWORLDUS057.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='IPTV WORLD', cmdlist=cmdlist, finishedCallback=None)
                        elif returnValue =="com_496":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia801409.us.archive.org/29/items/iptvworld_201911/IPTVWORLDUS058.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='IPTV WORLD', cmdlist=cmdlist, finishedCallback=None)
                        elif returnValue =="com_497":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia801409.us.archive.org/29/items/iptvworld_201911/IPTVWORLDUS059.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='IPTV WORLD', cmdlist=cmdlist, finishedCallback=None)
                        elif returnValue =="com_498":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia801409.us.archive.org/29/items/iptvworld_201911/IPTVWORLDUS060.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='IPTV WORLD', cmdlist=cmdlist, finishedCallback=None)
                        elif returnValue =="com_499":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia801409.us.archive.org/29/items/iptvworld_201911/IPTVWORLDUS061.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='IPTV WORLD', cmdlist=cmdlist, finishedCallback=None)
                        elif returnValue =="com_500":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia801409.us.archive.org/29/items/iptvworld_201911/IPTVWORLDUS062.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='IPTV WORLD', cmdlist=cmdlist, finishedCallback=None)
                        elif returnValue =="com_501":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia801409.us.archive.org/29/items/iptvworld_201911/IPTVWORLDUS063.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='IPTV WORLD', cmdlist=cmdlist, finishedCallback=None)
                        elif returnValue =="com_502":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia801409.us.archive.org/29/items/iptvworld_201911/IPTVWORLDUS064.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='IPTV WORLD', cmdlist=cmdlist, finishedCallback=None)
                        elif returnValue =="com_503":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia801409.us.archive.org/29/items/iptvworld_201911/IPTVWORLDUS065.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='IPTV WORLD', cmdlist=cmdlist, finishedCallback=None)
                        elif returnValue =="com_504":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia801409.us.archive.org/29/items/iptvworld_201911/IPTVWORLDUS066.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='IPTV WORLD', cmdlist=cmdlist, finishedCallback=None)
                        elif returnValue =="com_505":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia801409.us.archive.org/29/items/iptvworld_201911/IPTVWORLDUS067.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='IPTV WORLD', cmdlist=cmdlist, finishedCallback=None)
                        elif returnValue =="com_506":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia801409.us.archive.org/29/items/iptvworld_201911/IPTVWORLDUS068.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='IPTV WORLD', cmdlist=cmdlist, finishedCallback=None)
                        elif returnValue =="com_507":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia801409.us.archive.org/29/items/iptvworld_201911/IPTVWORLDUS069.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='IPTV WORLD', cmdlist=cmdlist, finishedCallback=None)
                        elif returnValue =="com_508":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia801409.us.archive.org/29/items/iptvworld_201911/IPTVWORLDUS070.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='IPTV WORLD', cmdlist=cmdlist, finishedCallback=None)
                        elif returnValue =="com_509":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia801409.us.archive.org/29/items/iptvworld_201911/IPTVWORLDUS071.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='IPTV WORLD', cmdlist=cmdlist, finishedCallback=None)
                        elif returnValue =="com_510":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia801409.us.archive.org/29/items/iptvworld_201911/IPTVWORLDUS072.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='IPTV WORLD', cmdlist=cmdlist, finishedCallback=None)
                        elif returnValue =="com_511":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia801409.us.archive.org/29/items/iptvworld_201911/IPTVWORLDUS073.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='IPTV WORLD', cmdlist=cmdlist, finishedCallback=None)
                        elif returnValue =="com_512":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia801409.us.archive.org/29/items/iptvworld_201911/IPTVWORLDUS074.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='IPTV WORLD', cmdlist=cmdlist, finishedCallback=None)
                        elif returnValue =="com_513":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia801409.us.archive.org/29/items/iptvworld_201911/IPTVWORLDUS075.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='IPTV WORLD', cmdlist=cmdlist, finishedCallback=None)
                        elif returnValue =="com_514":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia801409.us.archive.org/29/items/iptvworld_201911/IPTVWORLDUS076.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='IPTV WORLD', cmdlist=cmdlist, finishedCallback=None)
                        elif returnValue =="com_515":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia801409.us.archive.org/29/items/iptvworld_201911/IPTVWORLDUS077.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='IPTV WORLD', cmdlist=cmdlist, finishedCallback=None)
                        elif returnValue =="com_516":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia801409.us.archive.org/29/items/iptvworld_201911/IPTVWORLDUS078.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='IPTV WORLD', cmdlist=cmdlist, finishedCallback=None)
                        elif returnValue =="com_517":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia801409.us.archive.org/29/items/iptvworld_201911/IPTVWORLDUS079.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='IPTV WORLD', cmdlist=cmdlist, finishedCallback=None)
                        elif returnValue =="com_518":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia801409.us.archive.org/29/items/iptvworld_201911/IPTVWORLDUS080.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='IPTV WORLD', cmdlist=cmdlist, finishedCallback=None)
                        elif returnValue =="com_519":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia801409.us.archive.org/29/items/iptvworld_201911/IPTVWORLDUS081.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='IPTV WORLD', cmdlist=cmdlist, finishedCallback=None)
                        elif returnValue =="com_520":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia801409.us.archive.org/29/items/iptvworld_201911/IPTVWORLDUS082.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='IPTV WORLD', cmdlist=cmdlist, finishedCallback=None)
                        elif returnValue =="com_521":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia801409.us.archive.org/29/items/iptvworld_201911/IPTVWORLDUS083.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='IPTV WORLD', cmdlist=cmdlist, finishedCallback=None)
                        elif returnValue =="com_522":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia801409.us.archive.org/29/items/iptvworld_201911/IPTVWORLDUS084.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='IPTV WORLD', cmdlist=cmdlist, finishedCallback=None)
                        elif returnValue =="com_523":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia801409.us.archive.org/29/items/iptvworld_201911/IPTVWORLDUS085.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='IPTV WORLD', cmdlist=cmdlist, finishedCallback=None)
                        elif returnValue =="com_524":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia801409.us.archive.org/29/items/iptvworld_201911/IPTVWORLDUS086.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='IPTV WORLD', cmdlist=cmdlist, finishedCallback=None)
                        elif returnValue =="com_525":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia801409.us.archive.org/29/items/iptvworld_201911/IPTVWORLDUS087.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='IPTV WORLD', cmdlist=cmdlist, finishedCallback=None)
                        elif returnValue =="com_526":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia801409.us.archive.org/29/items/iptvworld_201911/IPTVWORLDUS088.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='IPTV WORLD', cmdlist=cmdlist, finishedCallback=None)
                        elif returnValue =="com_527":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia801409.us.archive.org/29/items/iptvworld_201911/IPTVWORLDUS089.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='IPTV WORLD', cmdlist=cmdlist, finishedCallback=None)
                        elif returnValue =="com_528":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia801409.us.archive.org/29/items/iptvworld_201911/IPTVWORLDUS090.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='IPTV WORLD', cmdlist=cmdlist, finishedCallback=None)
                        elif returnValue =="com_529":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia801409.us.archive.org/29/items/iptvworld_201911/IPTVWORLDUS091.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='IPTV WORLD', cmdlist=cmdlist, finishedCallback=None)
                        elif returnValue =="com_530":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia801409.us.archive.org/29/items/iptvworld_201911/IPTVWORLDUS092.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='IPTV WORLD', cmdlist=cmdlist, finishedCallback=None)
                        elif returnValue =="com_531":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia801409.us.archive.org/29/items/iptvworld_201911/IPTVWORLDUS093.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='IPTV WORLD', cmdlist=cmdlist, finishedCallback=None)
                        elif returnValue =="com_532":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia801409.us.archive.org/29/items/iptvworld_201911/IPTVWORLDUS094.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='IPTV WORLD', cmdlist=cmdlist, finishedCallback=None)
                        elif returnValue =="com_533":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia801409.us.archive.org/29/items/iptvworld_201911/IPTVWORLDUS095.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='IPTV WORLD', cmdlist=cmdlist, finishedCallback=None)
                        elif returnValue =="com_534":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'") 
                                cmdlist.append("%s https://ia801409.us.archive.org/29/items/iptvworld_201911/IPTVWORLDUS096.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='IPTV WORLD', cmdlist=cmdlist, finishedCallback=None)
                        elif returnValue =="com_535":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia801409.us.archive.org/29/items/iptvworld_201911/IPTVWORLDUS097.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='IPTV WORLD', cmdlist=cmdlist, finishedCallback=None)
                        elif returnValue =="com_536":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia801409.us.archive.org/29/items/iptvworld_201911/IPTVWORLDUS098.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='IPTV WORLD', cmdlist=cmdlist, finishedCallback=None)
                        elif returnValue =="com_537":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia801409.us.archive.org/29/items/iptvworld_201911/IPTVWORLDUS099.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='IPTV WORLD', cmdlist=cmdlist, finishedCallback=None)
                        elif returnValue =="com_538":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")    
                                cmdlist.append("%s https://ia801409.us.archive.org/29/items/iptvworld_201911/IPTVWORLDUS100.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='IPTV WORLD', cmdlist=cmdlist, finishedCallback=None)
                        elif returnValue =="com_539":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia801409.us.archive.org/29/items/iptvworld_201911/IPTVWORLDUS101.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='IPTV WORLD', cmdlist=cmdlist, finishedCallback=None)
                        elif returnValue =="com_540":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia801409.us.archive.org/29/items/iptvworld_201911/IPTVWORLDUS102.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='IPTV WORLD', cmdlist=cmdlist, finishedCallback=None)
                        elif returnValue =="com_541":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia801409.us.archive.org/29/items/iptvworld_201911/IPTVWORLDUS103.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='IPTV WORLD', cmdlist=cmdlist, finishedCallback=None)
                        elif returnValue =="com_542":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia801409.us.archive.org/29/items/iptvworld_201911/IPTVWORLDUS104.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='IPTV WORLD', cmdlist=cmdlist, finishedCallback=None)
                        elif returnValue =="com_543":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia801409.us.archive.org/29/items/iptvworld_201911/IPTVWORLDUS105.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='IPTV WORLD', cmdlist=cmdlist, finishedCallback=None)
                        elif returnValue =="com_544":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia801409.us.archive.org/29/items/iptvworld_201911/IPTVWORLDUS106.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='IPTV WORLD', cmdlist=cmdlist, finishedCallback=None)
                        elif returnValue =="com_545":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia801409.us.archive.org/29/items/iptvworld_201911/IPTVWORLDUS107.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='IPTV WORLD', cmdlist=cmdlist, finishedCallback=None)
                        elif returnValue =="com_546":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia801409.us.archive.org/29/items/iptvworld_201911/IPTVWORLDUS108.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='IPTV WORLD', cmdlist=cmdlist, finishedCallback=None)
                        elif returnValue =="com_547":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia801409.us.archive.org/29/items/iptvworld_201911/IPTVWORLDUS109.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='IPTV WORLD', cmdlist=cmdlist, finishedCallback=None)
                        elif returnValue =="com_548":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia801409.us.archive.org/29/items/iptvworld_201911/IPTVWORLDUS110.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='IPTV WORLD', cmdlist=cmdlist, finishedCallback=None)
                        elif returnValue =="com_549":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia801409.us.archive.org/29/items/iptvworld_201911/IPTVWORLDUS111.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='IPTV WORLD', cmdlist=cmdlist, finishedCallback=None)
                        elif returnValue =="com_550":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia801409.us.archive.org/29/items/iptvworld_201911/IPTVWORLDUS112.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='IPTV WORLD', cmdlist=cmdlist, finishedCallback=None)
                        elif returnValue =="com_551":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia801409.us.archive.org/29/items/iptvworld_201911/IPTVWORLDUS113.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='IPTV USA', cmdlist=cmdlist, finishedCallback=None)
                        elif returnValue =="com_552":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia801409.us.archive.org/29/items/iptvworld_201911/IPTVWORLDUS114.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='IPTV USA', cmdlist=cmdlist, finishedCallback=None)
                        elif returnValue =="com_553":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia801409.us.archive.org/29/items/iptvworld_201911/IPTVWORLDUS115.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='IPTV USA', cmdlist=cmdlist, finishedCallback=None)
                        elif returnValue =="com_554":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'") 
                                cmdlist.append("%s https://ia801409.us.archive.org/29/items/iptvworld_201911/IPTVWORLDUS116.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='IPTV USA', cmdlist=cmdlist, finishedCallback=None)
                        elif returnValue =="com_555":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia801409.us.archive.org/29/items/iptvworld_201911/IPTVWORLDUS117.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='IPTV USA', cmdlist=cmdlist, finishedCallback=None)
                        elif returnValue =="com_556":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia801409.us.archive.org/29/items/iptvworld_201911/IPTVWORLDUS118.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='IPTV USA', cmdlist=cmdlist, finishedCallback=None)
                        elif returnValue =="com_557":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia801409.us.archive.org/29/items/iptvworld_201911/IPTVWORLDUS119.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='IPTV USA', cmdlist=cmdlist, finishedCallback=None)
                        elif returnValue =="com_558":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")    
                                cmdlist.append("%s https://ia801409.us.archive.org/29/items/iptvworld_201911/IPTVWORLDUS120.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='IPTV USA', cmdlist=cmdlist, finishedCallback=None)
                        elif returnValue =="com_559":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia801409.us.archive.org/29/items/iptvworld_201911/IPTVWORLDUS121.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='IPTV USA', cmdlist=cmdlist, finishedCallback=None)
                        elif returnValue =="com_560":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia801409.us.archive.org/29/items/iptvworld_201911/IPTVWORLDUS122.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='IPTV USA', cmdlist=cmdlist, finishedCallback=None)
                        elif returnValue =="com_561":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia801409.us.archive.org/29/items/iptvworld_201911/IPTVWORLDUS123.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='IPTV WORLD', cmdlist=cmdlist, finishedCallback=None)
                        elif returnValue =="com_562":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia801409.us.archive.org/29/items/iptvworld_201911/IPTVWORLDUS124.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='IPTV WORLD', cmdlist=cmdlist, finishedCallback=None)
                        elif returnValue =="com_563":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia801409.us.archive.org/29/items/iptvworld_201911/IPTVWORLDUS125.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='IPTV WORLD', cmdlist=cmdlist, finishedCallback=None)
                        elif returnValue =="com_564":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia801409.us.archive.org/29/items/iptvworld_201911/IPTVWORLDUS126.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='IPTV WORLD', cmdlist=cmdlist, finishedCallback=None)
                        elif returnValue =="com_565":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia801409.us.archive.org/29/items/iptvworld_201911/IPTVWORLDUS127.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='IPTV WORLD', cmdlist=cmdlist, finishedCallback=None)
                        elif returnValue =="com_566":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia801409.us.archive.org/29/items/iptvworld_201911/IPTVWORLDUS128.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='IPTV WORLD', cmdlist=cmdlist, finishedCallback=None)
                        elif returnValue =="com_567":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia801409.us.archive.org/29/items/iptvworld_201911/IPTVWORLDUS129.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='IPTV WORLD', cmdlist=cmdlist, finishedCallback=None)
                        elif returnValue =="com_568":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia801409.us.archive.org/29/items/iptvworld_201911/IPTVWORLDUS130.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='IPTV WORLD', cmdlist=cmdlist, finishedCallback=None)
                        elif returnValue =="com_569":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia801409.us.archive.org/29/items/iptvworld_201911/IPTVWORLDUS131.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='IPTV WORLD', cmdlist=cmdlist, finishedCallback=None)
                        elif returnValue =="com_570":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia801409.us.archive.org/29/items/iptvworld_201911/IPTVWORLDUS132.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='IPTV WORLD', cmdlist=cmdlist, finishedCallback=None)
                        elif returnValue =="com_571":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia801409.us.archive.org/29/items/iptvworld_201911/IPTVWORLDUS133.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='IPTV WORLD', cmdlist=cmdlist, finishedCallback=None)
                        elif returnValue =="com_572":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia801409.us.archive.org/29/items/iptvworld_201911/IPTVWORLDUS134.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='IPTV WORLD', cmdlist=cmdlist, finishedCallback=None)
                        elif returnValue =="com_573":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia801409.us.archive.org/29/items/iptvworld_201911/IPTVWORLDUS135.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='IPTV WORLD', cmdlist=cmdlist, finishedCallback=None)
                        elif returnValue =="com_574":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia801409.us.archive.org/29/items/iptvworld_201911/IPTVWORLDUS136.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='IPTV WORLD', cmdlist=cmdlist, finishedCallback=None)
                        elif returnValue =="com_575":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia801409.us.archive.org/29/items/iptvworld_201911/IPTVWORLDUS137.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='IPTV WORLD', cmdlist=cmdlist, finishedCallback=None)
                        elif returnValue =="com_576":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia801409.us.archive.org/29/items/iptvworld_201911/IPTVWORLDUS138.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='IPTV WORLD', cmdlist=cmdlist, finishedCallback=None)
                        elif returnValue =="com_577":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia801409.us.archive.org/29/items/iptvworld_201911/IPTVWORLDUS139.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='IPTV WORLD', cmdlist=cmdlist, finishedCallback=None)
                        elif returnValue =="com_578":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia801409.us.archive.org/29/items/iptvworld_201911/IPTVWORLDUS140.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='IPTV WORLD', cmdlist=cmdlist, finishedCallback=None)
                        elif returnValue =="com_579":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia801409.us.archive.org/29/items/iptvworld_201911/IPTVWORLDUS141.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='IPTV WORLD', cmdlist=cmdlist, finishedCallback=None)
                        elif returnValue =="com_580":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia801409.us.archive.org/29/items/iptvworld_201911/IPTVWORLDUS142.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='IPTV WORLD', cmdlist=cmdlist, finishedCallback=None)
                        elif returnValue =="com_581":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia801409.us.archive.org/29/items/iptvworld_201911/IPTVWORLDUS143.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='IPTV WORLD', cmdlist=cmdlist, finishedCallback=None)
                        elif returnValue =="com_582":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia801409.us.archive.org/29/items/iptvworld_201911/IPTVWORLDUS144.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='IPTV WORLD', cmdlist=cmdlist, finishedCallback=None)
                        elif returnValue =="com_583":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia801409.us.archive.org/29/items/iptvworld_201911/IPTVWORLDUS145.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='IPTV WORLD', cmdlist=cmdlist, finishedCallback=None)
                        elif returnValue =="com_584":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia801409.us.archive.org/29/items/iptvworld_201911/IPTVWORLDUS146.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='IPTV WORLD', cmdlist=cmdlist, finishedCallback=None)
                        elif returnValue =="com_585":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia801409.us.archive.org/29/items/iptvworld_201911/IPTVWORLDUS147.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='IPTV WORLD', cmdlist=cmdlist, finishedCallback=None)
                        elif returnValue =="com_586":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia801409.us.archive.org/29/items/iptvworld_201911/IPTVWORLDUS148.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='IPTV WORLD', cmdlist=cmdlist, finishedCallback=None)
                        elif returnValue =="com_587":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia801409.us.archive.org/29/items/iptvworld_201911/IPTVWORLDUS149.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='IPTV WORLD', cmdlist=cmdlist, finishedCallback=None)
                        elif returnValue =="com_588":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia801409.us.archive.org/29/items/iptvworld_201911/IPTVWORLDUS150.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='IPTV WORLD', cmdlist=cmdlist, finishedCallback=None)
                        elif returnValue =="com_589":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia903108.us.archive.org/1/items/iptvworld_20191116/IPTVWORLDN100.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='IPTV WORLD', cmdlist=cmdlist, finishedCallback=None)
                        elif returnValue =="com_590":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia801409.us.archive.org/29/items/iptvworld_201911/IIPTVWORLDN50.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='IPTV WORLD', cmdlist=cmdlist, finishedCallback=None)
                        elif returnValue =="com_591":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia801409.us.archive.org/29/items/iptvworld_201911/IPTVWORLDN20.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='IPTV WORD', cmdlist=cmdlist, finishedCallback=None)
                        elif returnValue =="com_592":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia801409.us.archive.org/29/items/iptvworld_201911/IPTVWORLDN10.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='IPTV WORD', cmdlist=cmdlist, finishedCallback=None)
                        elif returnValue =="com_593":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia601505.us.archive.org/2/items/europe_202101/IPTVWORLDNLN50.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='IPTV WORLD', cmdlist=cmdlist, finishedCallback=None)
                        elif returnValue =="com_594":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia601505.us.archive.org/2/items/europe_202101/IPTVWORLDNL001.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='IPTV WORLD', cmdlist=cmdlist, finishedCallback=None)
                        elif returnValue =="com_595":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia601505.us.archive.org/2/items/europe_202101/IPTVWORLDNL002.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='IPTV WORLD', cmdlist=cmdlist, finishedCallback=None)
                        elif returnValue =="com_596":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia601505.us.archive.org/2/items/europe_202101/IPTVWORLDNL003.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='IPTV WORLD', cmdlist=cmdlist, finishedCallback=None)
                        elif returnValue =="com_597":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia601505.us.archive.org/2/items/europe_202101/IPTVWORLDNL004.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='IPTV WORLD', cmdlist=cmdlist, finishedCallback=None)
                        elif returnValue =="com_598":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia601505.us.archive.org/2/items/europe_202101/IPTVWORLDNL005.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='IPTV WORLD', cmdlist=cmdlist, finishedCallback=None)
                        elif returnValue =="com_599":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia601505.us.archive.org/2/items/europe_202101/IPTVWORLDNL006.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='IPTV WORLD', cmdlist=cmdlist, finishedCallback=None)
                        elif returnValue =="com_600":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia601505.us.archive.org/2/items/europe_202101/IPTVWORLDNL007.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='IPTV WORLD', cmdlist=cmdlist, finishedCallback=None)
                        elif returnValue =="com_601":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia601505.us.archive.org/2/items/europe_202101/IPTVWORLDNL008.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='IPTV WORLD', cmdlist=cmdlist, finishedCallback=None)
                        elif returnValue =="com_602":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia601505.us.archive.org/2/items/europe_202101/IPTVWORLDNL009.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='IPTV WORLD', cmdlist=cmdlist, finishedCallback=None)
                        elif returnValue =="com_603":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia601505.us.archive.org/2/items/europe_202101/IPTVWORLDNL010.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='IPTV WORLD', cmdlist=cmdlist, finishedCallback=None)
                        elif returnValue =="com_604":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia601505.us.archive.org/2/items/europe_202101/IPTVWORLDNL011.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='IPTV WORLD', cmdlist=cmdlist, finishedCallback=None)
                        elif returnValue =="com_605":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia601505.us.archive.org/2/items/europe_202101/IPTVWORLDNL012.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='IPTV WORLD', cmdlist=cmdlist, finishedCallback=None)
                        elif returnValue =="com_606":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia601505.us.archive.org/2/items/europe_202101/IPTVWORLDNL013.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='IPTV WORLD', cmdlist=cmdlist, finishedCallback=None)
                        elif returnValue =="com_607":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia601505.us.archive.org/2/items/europe_202101/IPTVWORLDNL014.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='IPTV WORLD', cmdlist=cmdlist, finishedCallback=None)
                        elif returnValue =="com_608":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia601505.us.archive.org/2/items/europe_202101/IPTVWORLDNL015.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='IPTV WORLD', cmdlist=cmdlist, finishedCallback=None)
                        elif returnValue =="com_609":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia601505.us.archive.org/2/items/europe_202101/IPTVWORLDNL016.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='IPTV WORLD', cmdlist=cmdlist, finishedCallback=None)
                        elif returnValue =="com_610":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia601505.us.archive.org/2/items/europe_202101/IPTVWORLDNL017.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='IPTV WORLD', cmdlist=cmdlist, finishedCallback=None)
                        elif returnValue =="com_611":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia601505.us.archive.org/2/items/europe_202101/IPTVWORLDNL018.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='IPTV WORLD', cmdlist=cmdlist, finishedCallback=None)
                        elif returnValue =="com_612":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia601505.us.archive.org/2/items/europe_202101/IPTVWORLDNL019.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='IPTV WORLD', cmdlist=cmdlist, finishedCallback=None)
                        elif returnValue =="com_613":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia601505.us.archive.org/2/items/europe_202101/IPTVWORLDNL020.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='IPTV WORLD', cmdlist=cmdlist, finishedCallback=None)
                        elif returnValue =="com_614":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia601505.us.archive.org/2/items/europe_202101/IPTVWORLDNL021.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='IPTV WORLD', cmdlist=cmdlist, finishedCallback=None)
                        elif returnValue =="com_615":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia601505.us.archive.org/2/items/europe_202101/IPTVWORLDNL022.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='IPTV WORLD', cmdlist=cmdlist, finishedCallback=None)
                        elif returnValue =="com_616":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia601505.us.archive.org/2/items/europe_202101/IPTVWORLDNL023.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='IPTV WORLD', cmdlist=cmdlist, finishedCallback=None)
                        elif returnValue =="com_617":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia601505.us.archive.org/2/items/europe_202101/IPTVWORLDNL024.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='IPTV WORLD', cmdlist=cmdlist, finishedCallback=None)
                        elif returnValue =="com_618":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia601505.us.archive.org/2/items/europe_202101/IPTVWORLDNL025.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='IPTV WORLD', cmdlist=cmdlist, finishedCallback=None)
                        elif returnValue =="com_619":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia601505.us.archive.org/2/items/europe_202101/IPTVWORLDNL026.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='IPTV WORLD', cmdlist=cmdlist, finishedCallback=None)
                        elif returnValue =="com_620":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia601505.us.archive.org/2/items/europe_202101/IPTVWORLDNL027.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='IPTV WORLD', cmdlist=cmdlist, finishedCallback=None)
                        elif returnValue =="com_621":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia601505.us.archive.org/2/items/europe_202101/IPTVWORLDNL028.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='IPTV WORLD', cmdlist=cmdlist, finishedCallback=None)
                        elif returnValue =="com_622":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia601505.us.archive.org/2/items/europe_202101/IPTVWORLDNL029.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='IPTV WORLD', cmdlist=cmdlist, finishedCallback=None)
                        elif returnValue =="com_623":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia601505.us.archive.org/2/items/europe_202101/IPTVWORLDNL030.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='IPTV WORLD', cmdlist=cmdlist, finishedCallback=None)
                        elif returnValue =="com_624":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia601505.us.archive.org/2/items/europe_202101/IPTVWORLDNL031.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='IPTV WORLD', cmdlist=cmdlist, finishedCallback=None)
                        elif returnValue =="com_625":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia601505.us.archive.org/2/items/europe_202101/IPTVWORLDNL032.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='IPTV WORLD', cmdlist=cmdlist, finishedCallback=None)
                        elif returnValue =="com_626":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia601505.us.archive.org/2/items/europe_202101/IPTVWORLDNL033.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='IPTV WORLD', cmdlist=cmdlist, finishedCallback=None)
                        elif returnValue =="com_627":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia601505.us.archive.org/2/items/europe_202101/IPTVWORLDNL034.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='IPTV WORLD', cmdlist=cmdlist, finishedCallback=None)
                        elif returnValue =="com_628":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia601505.us.archive.org/2/items/europe_202101/IPTVWORLDNL035.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='IPTV WORLD', cmdlist=cmdlist, finishedCallback=None)
                        elif returnValue =="com_629":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia601505.us.archive.org/2/items/europe_202101/IPTVWORLDNL036.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='IPTV WORLD', cmdlist=cmdlist, finishedCallback=None)
                        elif returnValue =="com_630":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia601505.us.archive.org/2/items/europe_202101/IPTVWORLDNL037.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='IPTV WORLD', cmdlist=cmdlist, finishedCallback=None)
                        elif returnValue =="com_631":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia601505.us.archive.org/2/items/europe_202101/IPTVWORLDNL038.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='IPTV WORLD', cmdlist=cmdlist, finishedCallback=None)
                        elif returnValue =="com_632":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia601505.us.archive.org/2/items/europe_202101/IPTVWORLDNL039.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='IPTV WORLD', cmdlist=cmdlist, finishedCallback=None)
                        elif returnValue =="com_633":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia601505.us.archive.org/2/items/europe_202101/IPTVWORLDNL040.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='IPTV WORLD', cmdlist=cmdlist, finishedCallback=None)
                        elif returnValue =="com_634":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'") 
                                cmdlist.append("%s https://ia601505.us.archive.org/2/items/europe_202101/IPTVWORLDNL041.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='IPTV WORLD', cmdlist=cmdlist, finishedCallback=None)
                        elif returnValue =="com_635":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia601505.us.archive.org/2/items/europe_202101/IPTVWORLDNL042.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='IPTV WORLD', cmdlist=cmdlist, finishedCallback=None)
                        elif returnValue =="com_636":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia601505.us.archive.org/2/items/europe_202101/IPTVWORLDNL043.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='IPTV WORLD', cmdlist=cmdlist, finishedCallback=None)
                        elif returnValue =="com_637":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia601505.us.archive.org/2/items/europe_202101/IPTVWORLDNL044.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='IPTV WORLD', cmdlist=cmdlist, finishedCallback=None)
                        elif returnValue =="com_638":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")    
                                cmdlist.append("%s https://ia601505.us.archive.org/2/items/europe_202101/IPTVWORLDNL045.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='IPTV WORLD', cmdlist=cmdlist, finishedCallback=None)
                        elif returnValue =="com_639":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia601505.us.archive.org/2/items/europe_202101/IPTVWORLDNL046.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='IPTV WORLD', cmdlist=cmdlist, finishedCallback=None)
                        elif returnValue =="com_640":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia601505.us.archive.org/2/items/europe_202101/IPTVWORLDNL047.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='IPTV WORLD', cmdlist=cmdlist, finishedCallback=None)
                        elif returnValue =="com_641":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia601505.us.archive.org/2/items/europe_202101/IPTVWORLDNL048.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='IPTV WORLD', cmdlist=cmdlist, finishedCallback=None)
                        elif returnValue =="com_642":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia601505.us.archive.org/2/items/europe_202101/IPTVWORLDNL049.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='IPTV WORLD', cmdlist=cmdlist, finishedCallback=None)
                        elif returnValue =="com_643":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia601505.us.archive.org/2/items/europe_202101/IPTVWORLDNL050.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='IPTV WORLD', cmdlist=cmdlist, finishedCallback=None)
                        elif returnValue =="com_644":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia601505.us.archive.org/2/items/europe_202101/IPTVWORLDITN10.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='IPTV WORLD', cmdlist=cmdlist, finishedCallback=None)
                        elif returnValue =="com_0645":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia601505.us.archive.org/2/items/europe_202101/IPTVWORLDITN20.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='IPTV WORLD', cmdlist=cmdlist, finishedCallback=None)
                        elif returnValue =="com_0646":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia601505.us.archive.org/2/items/europe_202101/IPTVWORLDITN50.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='IPTV WORLD', cmdlist=cmdlist, finishedCallback=None)
                        elif returnValue =="com_0647":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia601505.us.archive.org/2/items/europe_202101/IPTVWORLDITN100.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='IPTV WORLD', cmdlist=cmdlist, finishedCallback=None)
                        elif returnValue =="com_645":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia601505.us.archive.org/2/items/europe_202101/IPTVWORLDIT001.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='IPTV WORLD', cmdlist=cmdlist, finishedCallback=None)
                        elif returnValue =="com_646":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia601505.us.archive.org/2/items/europe_202101/IPTVWORLDIT002.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='IPTV WORLD', cmdlist=cmdlist, finishedCallback=None)
                        elif returnValue =="com_647":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia601505.us.archive.org/2/items/europe_202101/IPTVWORLDIT003.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='IPTV WORLD', cmdlist=cmdlist, finishedCallback=None)
                        elif returnValue =="com_648":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia601505.us.archive.org/2/items/europe_202101/IPTVWORLDIT004.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='IPTV WORLD', cmdlist=cmdlist, finishedCallback=None)
                        elif returnValue =="com_649":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia601505.us.archive.org/2/items/europe_202101/IPTVWORLDIT005.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='IPTV WORLD', cmdlist=cmdlist, finishedCallback=None)
                        elif returnValue =="com_650":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia601505.us.archive.org/2/items/europe_202101/IPTVWORLDIT006.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='IPTV WORLD', cmdlist=cmdlist, finishedCallback=None)
                        elif returnValue =="com_651":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia601505.us.archive.org/2/items/europe_202101/IPTVWORLDIT007.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='IPTV USA', cmdlist=cmdlist, finishedCallback=None)
                        elif returnValue =="com_652":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia601505.us.archive.org/2/items/europe_202101/IPTVWORLDIT008.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='IPTV USA', cmdlist=cmdlist, finishedCallback=None)
                        elif returnValue =="com_653":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia601505.us.archive.org/2/items/europe_202101/IPTVWORLDIT009.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='IPTV USA', cmdlist=cmdlist, finishedCallback=None)
                        elif returnValue =="com_654":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'") 
                                cmdlist.append("%s https://ia601505.us.archive.org/2/items/europe_202101/IPTVWORLDIT010.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='IPTV USA', cmdlist=cmdlist, finishedCallback=None)
                        elif returnValue =="com_655":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia601505.us.archive.org/2/items/europe_202101/IPTVWORLDIT011.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='IPTV USA', cmdlist=cmdlist, finishedCallback=None)
                        elif returnValue =="com_656":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia601505.us.archive.org/2/items/europe_202101/IPTVWORLDIT012.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='IPTV USA', cmdlist=cmdlist, finishedCallback=None)
                        elif returnValue =="com_657":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia601505.us.archive.org/2/items/europe_202101/IPTVWORLDIT013.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='IPTV USA', cmdlist=cmdlist, finishedCallback=None)
                        elif returnValue =="com_658":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")    
                                cmdlist.append("%s https://ia601505.us.archive.org/2/items/europe_202101/IPTVWORLDIT014.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='IPTV USA', cmdlist=cmdlist, finishedCallback=None)
                        elif returnValue =="com_659":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia601505.us.archive.org/2/items/europe_202101/IPTVWORLDIT015.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='IPTV USA', cmdlist=cmdlist, finishedCallback=None)
                        elif returnValue =="com_660":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia601505.us.archive.org/2/items/europe_202101/IPTVWORLDIT016.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='IPTV USA', cmdlist=cmdlist, finishedCallback=None)
                        elif returnValue =="com_661":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia601505.us.archive.org/2/items/europe_202101/IPTVWORLDIT017.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='IPTV WORLD', cmdlist=cmdlist, finishedCallback=None)
                        elif returnValue =="com_662":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia601505.us.archive.org/2/items/europe_202101/IPTVWORLDIT018.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='IPTV WORLD', cmdlist=cmdlist, finishedCallback=None)
                        elif returnValue =="com_663":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia601505.us.archive.org/2/items/europe_202101/IPTVWORLDIT019.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='IPTV WORLD', cmdlist=cmdlist, finishedCallback=None)
                        elif returnValue =="com_664":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia601505.us.archive.org/2/items/europe_202101/IPTVWORLDIT020.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='IPTV WORLD', cmdlist=cmdlist, finishedCallback=None)
                        elif returnValue =="com_665":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia601505.us.archive.org/2/items/europe_202101/IPTVWORLDIT021.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='IPTV WORLD', cmdlist=cmdlist, finishedCallback=None)
                        elif returnValue =="com_666":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia601505.us.archive.org/2/items/europe_202101/IPTVWORLDIT022.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='IPTV WORLD', cmdlist=cmdlist, finishedCallback=None)
                        elif returnValue =="com_667":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia601505.us.archive.org/2/items/europe_202101/IPTVWORLDIT023.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='IPTV WORLD', cmdlist=cmdlist, finishedCallback=None)
                        elif returnValue =="com_668":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia601505.us.archive.org/2/items/europe_202101/IPTVWORLDIT024.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='IPTV WORLD', cmdlist=cmdlist, finishedCallback=None)
                        elif returnValue =="com_669":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia601505.us.archive.org/2/items/europe_202101/IPTVWORLDIT025.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='IPTV WORLD', cmdlist=cmdlist, finishedCallback=None)
                        elif returnValue =="com_670":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia601505.us.archive.org/2/items/europe_202101/IPTVWORLDIT026.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='IPTV WORLD', cmdlist=cmdlist, finishedCallback=None)
                        elif returnValue =="com_671":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia601505.us.archive.org/2/items/europe_202101/IPTVWORLDIT027.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='IPTV WORLD', cmdlist=cmdlist, finishedCallback=None)
                        elif returnValue =="com_672":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia601505.us.archive.org/2/items/europe_202101/IPTVWORLDIT028.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='IPTV USA', cmdlist=cmdlist, finishedCallback=None)
                        elif returnValue =="com_673":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia601505.us.archive.org/2/items/europe_202101/IPTVWORLDIT029.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='IPTV USA', cmdlist=cmdlist, finishedCallback=None)
                        elif returnValue =="com_674":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia601505.us.archive.org/2/items/europe_202101/IPTVWORLDIT030.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='IPTV USA', cmdlist=cmdlist, finishedCallback=None)
                        elif returnValue =="com_675":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'") 
                                cmdlist.append("%s https://ia601505.us.archive.org/2/items/europe_202101/IPTVWORLDIT031.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='IPTV USA', cmdlist=cmdlist, finishedCallback=None)
                        elif returnValue =="com_676":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia601505.us.archive.org/2/items/europe_202101/IPTVWORLDIT032.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='IPTV USA', cmdlist=cmdlist, finishedCallback=None)
                        elif returnValue =="com_677":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia601505.us.archive.org/2/items/europe_202101/IPTVWORLDIT033.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='IPTV USA', cmdlist=cmdlist, finishedCallback=None)
                        elif returnValue =="com_678":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia601505.us.archive.org/2/items/europe_202101/IPTVWORLDIT034.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='IPTV USA', cmdlist=cmdlist, finishedCallback=None)
                        elif returnValue =="com_679":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")    
                                cmdlist.append("%s https://ia601505.us.archive.org/2/items/europe_202101/IPTVWORLDIT035.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='IPTV USA', cmdlist=cmdlist, finishedCallback=None)
                        elif returnValue =="com_680":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia601505.us.archive.org/2/items/europe_202101/IPTVWORLDIT036.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='IPTV USA', cmdlist=cmdlist, finishedCallback=None)
                        elif returnValue =="com_681":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia601505.us.archive.org/2/items/europe_202101/IPTVWORLDIT037.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='IPTV USA', cmdlist=cmdlist, finishedCallback=None)
                        elif returnValue =="com_682":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia601505.us.archive.org/2/items/europe_202101/IPTVWORLDIT038.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='IPTV WORLD', cmdlist=cmdlist, finishedCallback=None)
                        elif returnValue =="com_683":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia601505.us.archive.org/2/items/europe_202101/IPTVWORLDIT039.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='IPTV WORLD', cmdlist=cmdlist, finishedCallback=None)
                        elif returnValue =="com_684":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia601505.us.archive.org/2/items/europe_202101/IPTVWORLDIT040.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='IPTV WORLD', cmdlist=cmdlist, finishedCallback=None)
                        elif returnValue =="com_685":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia601505.us.archive.org/2/items/europe_202101/IPTVWORLDIT041.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='IPTV WORLD', cmdlist=cmdlist, finishedCallback=None)
                        elif returnValue =="com_686":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia601505.us.archive.org/2/items/europe_202101/IPTVWORLDIT042.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='IPTV WORLD', cmdlist=cmdlist, finishedCallback=None)
                        elif returnValue =="com_687":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia601505.us.archive.org/2/items/europe_202101/IPTVWORLDIT043.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='IPTV WORLD', cmdlist=cmdlist, finishedCallback=None)
                        elif returnValue =="com_688":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia601505.us.archive.org/2/items/europe_202101/IPTVWORLDIT044.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='IPTV WORLD', cmdlist=cmdlist, finishedCallback=None)
                        elif returnValue =="com_689":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia601505.us.archive.org/2/items/europe_202101/IPTVWORLDIT045.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='IPTV WORLD', cmdlist=cmdlist, finishedCallback=None)
                        elif returnValue =="com_690":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia601505.us.archive.org/2/items/europe_202101/IPTVWORLDIT046.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='IPTV WORLD', cmdlist=cmdlist, finishedCallback=None)
                        elif returnValue =="com_691":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia601505.us.archive.org/2/items/europe_202101/IPTVWORLDIT047.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='IPTV WORLD', cmdlist=cmdlist, finishedCallback=None)
                        elif returnValue =="com_692":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia601505.us.archive.org/2/items/europe_202101/IPTVWORLDIT048.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='IPTV WORLD', cmdlist=cmdlist, finishedCallback=None)
                        elif returnValue =="com_693":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia601505.us.archive.org/2/items/europe_202101/IPTVWORLDIT049.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='IPTV WORLD', cmdlist=cmdlist, finishedCallback=None)
                        elif returnValue =="com_694":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia601505.us.archive.org/2/items/europe_202101/IPTVWORLDIT050.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='IPTV WORLD', cmdlist=cmdlist, finishedCallback=None)
                        elif returnValue =="com_695":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia601505.us.archive.org/2/items/europe_202101/IPTVWORLDIT051.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='IPTV WORLD', cmdlist=cmdlist, finishedCallback=None)
                        elif returnValue =="com_696":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia601505.us.archive.org/2/items/europe_202101/IPTVWORLDIT052.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='IPTV WORLD', cmdlist=cmdlist, finishedCallback=None)
                        elif returnValue =="com_697":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia601505.us.archive.org/2/items/europe_202101/IPTVWORLDIT053.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='IPTV WORLD', cmdlist=cmdlist, finishedCallback=None)
                        elif returnValue =="com_698":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia601505.us.archive.org/2/items/europe_202101/IPTVWORLDIT054.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='IPTV WORLD', cmdlist=cmdlist, finishedCallback=None)
                        elif returnValue =="com_699":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia601505.us.archive.org/2/items/europe_202101/IPTVWORLDIT055.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='IPTV WORLD', cmdlist=cmdlist, finishedCallback=None)
                        elif returnValue =="com_700":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia601505.us.archive.org/2/items/europe_202101/IPTVWORLDIT056.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='IPTV WORLD', cmdlist=cmdlist, finishedCallback=None)
                        elif returnValue =="com_701":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia601505.us.archive.org/2/items/europe_202101/IPTVWORLDIT057.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='IPTV WORLD', cmdlist=cmdlist, finishedCallback=None)
                        elif returnValue =="com_702":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia601505.us.archive.org/2/items/europe_202101/IPTVWORLDIT058.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='IPTV WORLD', cmdlist=cmdlist, finishedCallback=None)
                        elif returnValue =="com_703":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia601505.us.archive.org/2/items/europe_202101/IPTVWORLDIT059.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='IPTV WORLD', cmdlist=cmdlist, finishedCallback=None)
                        elif returnValue =="com_704":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia601505.us.archive.org/2/items/europe_202101/IPTVWORLDIT060.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='IPTV WORLD', cmdlist=cmdlist, finishedCallback=None)
                        elif returnValue =="com_705":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia601505.us.archive.org/2/items/europe_202101/IPTVWORLDIT061.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='IPTV WORLD', cmdlist=cmdlist, finishedCallback=None)
                        elif returnValue =="com_706":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia601505.us.archive.org/2/items/europe_202101/IPTVWORLDIT062.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='IPTV WORLD', cmdlist=cmdlist, finishedCallback=None)
                        elif returnValue =="com_707":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia601505.us.archive.org/2/items/europe_202101/IPTVWORLDIT063.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='IPTV WORLD', cmdlist=cmdlist, finishedCallback=None)
                        elif returnValue =="com_708":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia601505.us.archive.org/2/items/europe_202101/IPTVWORLDIT064.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='IPTV WORLD', cmdlist=cmdlist, finishedCallback=None)
                        elif returnValue =="com_709":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia601505.us.archive.org/2/items/europe_202101/IPTVWORLDIT065.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='IPTV WORLD', cmdlist=cmdlist, finishedCallback=None)
                        elif returnValue =="com_710":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia601505.us.archive.org/2/items/europe_202101/IPTVWORLDIT066.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='IPTV WORLD', cmdlist=cmdlist, finishedCallback=None)
                        elif returnValue =="com_711":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia601505.us.archive.org/2/items/europe_202101/IPTVWORLDIT067.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='IPTV WORLD', cmdlist=cmdlist, finishedCallback=None)
                        elif returnValue =="com_712":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia601505.us.archive.org/2/items/europe_202101/IPTVWORLDIT068.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='IPTV WORD', cmdlist=cmdlist, finishedCallback=None)
                        elif returnValue =="com_713":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia601505.us.archive.org/2/items/europe_202101/IPTVWORLDIT069.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='IPTV WORD', cmdlist=cmdlist, finishedCallback=None)
                        elif returnValue =="com_714":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia601505.us.archive.org/2/items/europe_202101/IPTVWORLDIT070.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='IPTV WORLD', cmdlist=cmdlist, finishedCallback=None)
                        elif returnValue =="com_715":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia601505.us.archive.org/2/items/europe_202101/IPTVWORLDIT071.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='IPTV WORLD', cmdlist=cmdlist, finishedCallback=None)
                        elif returnValue =="com_716":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia601505.us.archive.org/2/items/europe_202101/IPTVWORLDIT072.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='IPTV WORLD', cmdlist=cmdlist, finishedCallback=None)
                        elif returnValue =="com_717":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia601505.us.archive.org/2/items/europe_202101/IPTVWORLDIT073.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='IPTV WORLD', cmdlist=cmdlist, finishedCallback=None)
                        elif returnValue =="com_718":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia601505.us.archive.org/2/items/europe_202101/IPTVWORLDIT074.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='IPTV WORLD', cmdlist=cmdlist, finishedCallback=None)
                        elif returnValue =="com_719":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia601505.us.archive.org/2/items/europe_202101/IPTVWORLDIT075.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='IPTV WORLD', cmdlist=cmdlist, finishedCallback=None)
                        elif returnValue =="com_720":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia601505.us.archive.org/2/items/europe_202101/IPTVWORLDIT076.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='IPTV WORLD', cmdlist=cmdlist, finishedCallback=None)
                        elif returnValue =="com_721":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia601505.us.archive.org/2/items/europe_202101/IPTVWORLDIT077.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='IPTV WORLD', cmdlist=cmdlist, finishedCallback=None)
                        elif returnValue =="com_722":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia601505.us.archive.org/2/items/europe_202101/IPTVWORLDIT078.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='IPTV WORLD', cmdlist=cmdlist, finishedCallback=None)
                        elif returnValue =="com_723":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia601505.us.archive.org/2/items/europe_202101/IPTVWORLDIT079.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='IPTV WORLD', cmdlist=cmdlist, finishedCallback=None)
                        elif returnValue =="com_724":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia601505.us.archive.org/2/items/europe_202101/IPTVWORLDIT080.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='IPTV WORLD', cmdlist=cmdlist, finishedCallback=None)
                        elif returnValue =="com_725":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia601505.us.archive.org/2/items/europe_202101/IPTVWORLDIT081.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='IPTV WORLD', cmdlist=cmdlist, finishedCallback=None)
                        elif returnValue =="com_726":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia601505.us.archive.org/2/items/europe_202101/IPTVWORLDIT082.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='IPTV WORLD', cmdlist=cmdlist, finishedCallback=None)
                        elif returnValue =="com_727":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia601505.us.archive.org/2/items/europe_202101/IPTVWORLDIT083.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='IPTV WORLD', cmdlist=cmdlist, finishedCallback=None)
                        elif returnValue =="com_728":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia601505.us.archive.org/2/items/europe_202101/IPTVWORLDIT084.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='IPTV WORLD', cmdlist=cmdlist, finishedCallback=None)
                        elif returnValue =="com_729":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia601505.us.archive.org/2/items/europe_202101/IPTVWORLDIT085.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='IPTV WORLD', cmdlist=cmdlist, finishedCallback=None)
                        elif returnValue =="com_730":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia601505.us.archive.org/2/items/europe_202101/IPTVWORLDIT086.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='IPTV WORLD', cmdlist=cmdlist, finishedCallback=None)
                        elif returnValue =="com_731":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia601505.us.archive.org/2/items/europe_202101/IPTVWORLDIT087.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='IPTV WORLD', cmdlist=cmdlist, finishedCallback=None)
                        elif returnValue =="com_732":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia601505.us.archive.org/2/items/europe_202101/IPTVWORLDIT088.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='IPTV WORLD', cmdlist=cmdlist, finishedCallback=None)
                        elif returnValue =="com_733":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia601505.us.archive.org/2/items/europe_202101/IPTVWORLDIT089.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='IPTV WORLD', cmdlist=cmdlist, finishedCallback=None)
                        elif returnValue =="com_734":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia601505.us.archive.org/2/items/europe_202101/IPTVWORLDIT090.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='IPTV WORLD', cmdlist=cmdlist, finishedCallback=None)
                        elif returnValue =="com_735":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia601505.us.archive.org/2/items/europe_202101/IPTVWORLDIT091.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='IPTV WORLD', cmdlist=cmdlist, finishedCallback=None)
                        elif returnValue =="com_736":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia601505.us.archive.org/2/items/europe_202101/IPTVWORLDIT092.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='IPTV WORLD', cmdlist=cmdlist, finishedCallback=None)
                        elif returnValue =="com_737":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia601505.us.archive.org/2/items/europe_202101/IPTVWORLDIT093.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='IPTV WORLD', cmdlist=cmdlist, finishedCallback=None)
                        elif returnValue =="com_738":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia601505.us.archive.org/2/items/europe_202101/IPTVWORLDIT094.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='IPTV WORLD', cmdlist=cmdlist, finishedCallback=None)
                        elif returnValue =="com_739":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia601505.us.archive.org/2/items/europe_202101/IPTVWORLDIT095.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='IPTV WORLD', cmdlist=cmdlist, finishedCallback=None)
                        elif returnValue =="com_740":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia601505.us.archive.org/2/items/europe_202101/IPTVWORLDIT096.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='IPTV WORLD', cmdlist=cmdlist, finishedCallback=None)
                        elif returnValue =="com_741":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia601505.us.archive.org/2/items/europe_202101/IPTVWORLDIT097.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='IPTV WORLD', cmdlist=cmdlist, finishedCallback=None)
                        elif returnValue =="com_742":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia601505.us.archive.org/2/items/europe_202101/IPTVWORLDIT098.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='IPTV WORLD', cmdlist=cmdlist, finishedCallback=None)
                        elif returnValue =="com_743":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia601505.us.archive.org/2/items/europe_202101/IPTVWORLDIT099.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='IPTV WORLD', cmdlist=cmdlist, finishedCallback=None)
                        elif returnValue =="com_744":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia601505.us.archive.org/2/items/europe_202101/IPTVWORLDIT100.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='IPTV WORLD', cmdlist=cmdlist, finishedCallback=None)
                        elif returnValue =="com_0745":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia601505.us.archive.org/2/items/europe_202101/IPTVWORLDRUN20.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='IPTV WORLD', cmdlist=cmdlist, finishedCallback=None)
                        elif returnValue =="com_745":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia601505.us.archive.org/2/items/europe_202101/IPTVWORLDRU001.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='IPTV WORLD', cmdlist=cmdlist, finishedCallback=None)
                        elif returnValue =="com_746":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia601505.us.archive.org/2/items/europe_202101/IPTVWORLDRU002.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='IPTV WORLD', cmdlist=cmdlist, finishedCallback=None)
                        elif returnValue =="com_747":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia601505.us.archive.org/2/items/europe_202101/IPTVWORLDRU003.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='IPTV WORLD', cmdlist=cmdlist, finishedCallback=None)
                        elif returnValue =="com_748":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia601505.us.archive.org/2/items/europe_202101/IPTVWORLDRU004.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='IPTV WORLD', cmdlist=cmdlist, finishedCallback=None)
                        elif returnValue =="com_749":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia601505.us.archive.org/2/items/europe_202101/IPTVWORLDRU005.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='IPTV WORLD', cmdlist=cmdlist, finishedCallback=None)
                        elif returnValue =="com_750":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia601505.us.archive.org/2/items/europe_202101/IPTVWORLDRU006.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='IPTV WORLD', cmdlist=cmdlist, finishedCallback=None)
                        elif returnValue =="com_751":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia601505.us.archive.org/2/items/europe_202101/IPTVWORLDRU007.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='IPTV WORLD', cmdlist=cmdlist, finishedCallback=None)
                        elif returnValue =="com_752":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia601505.us.archive.org/2/items/europe_202101/IPTVWORLDRU008.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='IPTV WORLD', cmdlist=cmdlist, finishedCallback=None)
                        elif returnValue =="com_753":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia601505.us.archive.org/2/items/europe_202101/IPTVWORLDRU009.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='IPTV WORLD', cmdlist=cmdlist, finishedCallback=None)
                        elif returnValue =="com_754":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'") 
                                cmdlist.append("%s https://ia601505.us.archive.org/2/items/europe_202101/IPTVWORLDRU010.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='IPTV WORLD', cmdlist=cmdlist, finishedCallback=None)
                        elif returnValue =="com_755":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia601505.us.archive.org/2/items/europe_202101/IPTVWORLDRU011.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='IPTV WORLD', cmdlist=cmdlist, finishedCallback=None)
                        elif returnValue =="com_756":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia601505.us.archive.org/2/items/europe_202101/IPTVWORLDRU012.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='IPTV WORLD', cmdlist=cmdlist, finishedCallback=None)
                        elif returnValue =="com_757":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia601505.us.archive.org/2/items/europe_202101/IPTVWORLDRU013.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='IPTV WORLD', cmdlist=cmdlist, finishedCallback=None)
                        elif returnValue =="com_758":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")    
                                cmdlist.append("%s https://ia601505.us.archive.org/2/items/europe_202101/IPTVWORLDRU014.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='IPTV WORLD', cmdlist=cmdlist, finishedCallback=None)
                        elif returnValue =="com_759":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia601505.us.archive.org/2/items/europe_202101/IPTVWORLDRU015.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='IPTV WORLD', cmdlist=cmdlist, finishedCallback=None)
                        elif returnValue =="com_760":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia601505.us.archive.org/2/items/europe_202101/IPTVWORLDRU016.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='IPTV WORLD', cmdlist=cmdlist, finishedCallback=None)
                        elif returnValue =="com_761":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia601505.us.archive.org/2/items/europe_202101/IPTVWORLDRU017.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='IPTV WORLD', cmdlist=cmdlist, finishedCallback=None)
                        elif returnValue =="com_762":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia601505.us.archive.org/2/items/europe_202101/IPTVWORLDRU018.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='IPTV WORLD', cmdlist=cmdlist, finishedCallback=None)
                        elif returnValue =="com_763":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia601505.us.archive.org/2/items/europe_202101/IPTVWORLDRU019.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='IPTV WORLD', cmdlist=cmdlist, finishedCallback=None)
                        elif returnValue =="com_764":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia601505.us.archive.org/2/items/europe_202101/IPTVWORLDRU020.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='IPTV WORLD', cmdlist=cmdlist, finishedCallback=None)
                        elif returnValue =="com_0765":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia601505.us.archive.org/2/items/europe_202101/IPTVWORLDTRN10.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='IPTV WORLD', cmdlist=cmdlist, finishedCallback=None)
                        elif returnValue =="com_0766":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia601505.us.archive.org/2/items/europe_202101/IPTVWORLDTRN20.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='IPTV WORLD', cmdlist=cmdlist, finishedCallback=None)
                        elif returnValue =="com_0767":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia601505.us.archive.org/2/items/europe_202101/IPTVWORLDTRN50.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='IPTV WORLD', cmdlist=cmdlist, finishedCallback=None)
                        elif returnValue =="com_0768":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia601505.us.archive.org/2/items/europe_202101/IPTVWORLDTRN100.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='IPTV WORLD', cmdlist=cmdlist, finishedCallback=None)
                        elif returnValue =="com_765":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia601505.us.archive.org/2/items/europe_202101/IPTVWORLDTR001.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='IPTV WORLD', cmdlist=cmdlist, finishedCallback=None)
                        elif returnValue =="com_766":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia601505.us.archive.org/2/items/europe_202101/IPTVWORLDTR002.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='IPTV WORLD', cmdlist=cmdlist, finishedCallback=None)
                        elif returnValue =="com_767":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia601505.us.archive.org/2/items/europe_202101/IPTVWORLDTR003.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='IPTV WORLD', cmdlist=cmdlist, finishedCallback=None)
                        elif returnValue =="com_768":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia601505.us.archive.org/2/items/europe_202101/IPTVWORLDTR004.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='IPTV WORLD', cmdlist=cmdlist, finishedCallback=None)
                        elif returnValue =="com_769":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia601505.us.archive.org/2/items/europe_202101/IPTVWORLDTR005.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='IPTV WORLD', cmdlist=cmdlist, finishedCallback=None)
                        elif returnValue =="com_770":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia601505.us.archive.org/2/items/europe_202101/IPTVWORLDTR006.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='IPTV WORLD', cmdlist=cmdlist, finishedCallback=None)
                        elif returnValue =="com_771":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia601505.us.archive.org/2/items/europe_202101/IPTVWORLDTR007.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='IPTV USA', cmdlist=cmdlist, finishedCallback=None)
                        elif returnValue =="com_772":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia601505.us.archive.org/2/items/europe_202101/IPTVWORLDTR008.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='IPTV USA', cmdlist=cmdlist, finishedCallback=None)
                        elif returnValue =="com_773":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia601505.us.archive.org/2/items/europe_202101/IPTVWORLDTR009.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='IPTV USA', cmdlist=cmdlist, finishedCallback=None)
                        elif returnValue =="com_774":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'") 
                                cmdlist.append("%s https://ia601505.us.archive.org/2/items/europe_202101/IPTVWORLDTR010.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='IPTV USA', cmdlist=cmdlist, finishedCallback=None)
                        elif returnValue =="com_0775":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia601505.us.archive.org/2/items/europe_202101/IPTVWORLDTR011.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='IPTV USA', cmdlist=cmdlist, finishedCallback=None)
                        elif returnValue =="com_776":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia601505.us.archive.org/2/items/europe_202101/IPTVWORLDTR012.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='IPTV USA', cmdlist=cmdlist, finishedCallback=None)
                        elif returnValue =="com_777":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia601505.us.archive.org/2/items/europe_202101/IPTVWORLDTR013.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='IPTV USA', cmdlist=cmdlist, finishedCallback=None)
                        elif returnValue =="com_778":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")    
                                cmdlist.append("%s https://ia601505.us.archive.org/2/items/europe_202101/IPTVWORLDTR014.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='IPTV USA', cmdlist=cmdlist, finishedCallback=None)
                        elif returnValue =="com_779":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia601505.us.archive.org/2/items/europe_202101/IPTVWORLDTR015.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='IPTV USA', cmdlist=cmdlist, finishedCallback=None)
                        elif returnValue =="com_780":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia601505.us.archive.org/2/items/europe_202101/IPTVWORLDTR016.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='IPTV USA', cmdlist=cmdlist, finishedCallback=None)
                        elif returnValue =="com_781":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia601505.us.archive.org/2/items/europe_202101/IPTVWORLDTR017.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='IPTV WORLD', cmdlist=cmdlist, finishedCallback=None)
                        elif returnValue =="com_782":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia601505.us.archive.org/2/items/europe_202101/IPTVWORLDTR018.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='IPTV WORLD', cmdlist=cmdlist, finishedCallback=None)
                        elif returnValue =="com_783":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia601505.us.archive.org/2/items/europe_202101/IPTVWORLDTR019.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='IPTV WORLD', cmdlist=cmdlist, finishedCallback=None)
                        elif returnValue =="com_784":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia601505.us.archive.org/2/items/europe_202101/IPTVWORLDTR020.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='IPTV WORLD', cmdlist=cmdlist, finishedCallback=None)
                        elif returnValue =="com_0785":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia601505.us.archive.org/2/items/europe_202101/IPTVWORLDPLN10.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='IPTV WORLD', cmdlist=cmdlist, finishedCallback=None)
                        elif returnValue =="com_0786":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia601505.us.archive.org/2/items/europe_202101/IPTVWORLDPLN20.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='IPTV WORLD', cmdlist=cmdlist, finishedCallback=None)
                        elif returnValue =="com_0787":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia601505.us.archive.org/2/items/europe_202101/IPTVWORLDPLN50.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='IPTV WORLD', cmdlist=cmdlist, finishedCallback=None)
                        elif returnValue =="com_785":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia601505.us.archive.org/2/items/europe_202101/IPTVWORLDPL001.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='IPTV WORLD', cmdlist=cmdlist, finishedCallback=None)
                        elif returnValue =="com_786":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia601505.us.archive.org/2/items/europe_202101/IPTVWORLDPL002.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='IPTV WORLD', cmdlist=cmdlist, finishedCallback=None)
                        elif returnValue =="com_787":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia601505.us.archive.org/2/items/europe_202101/IPTVWORLDPL003.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='IPTV WORLD', cmdlist=cmdlist, finishedCallback=None)
                        elif returnValue =="com_788":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia601505.us.archive.org/2/items/europe_202101/IPTVWORLDPL004.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='IPTV WORLD', cmdlist=cmdlist, finishedCallback=None)
                        elif returnValue =="com_789":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia601505.us.archive.org/2/items/europe_202101/IPTVWORLDPL005.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='IPTV WORLD', cmdlist=cmdlist, finishedCallback=None)
                        elif returnValue =="com_790":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia601505.us.archive.org/2/items/europe_202101/IPTVWORLDPL006.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='IPTV WORLD', cmdlist=cmdlist, finishedCallback=None)
                        elif returnValue =="com_791":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia601505.us.archive.org/2/items/europe_202101/IPTVWORLDPL007.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='IPTV WORLD', cmdlist=cmdlist, finishedCallback=None)
                        elif returnValue =="com_792":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia601505.us.archive.org/2/items/europe_202101/IPTVWORLDPL008.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='IPTV WORLD', cmdlist=cmdlist, finishedCallback=None)
                        elif returnValue =="com_793":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia601505.us.archive.org/2/items/europe_202101/IPTVWORLDPL009.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='IPTV WORLD', cmdlist=cmdlist, finishedCallback=None)
                        elif returnValue =="com_794":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia601505.us.archive.org/2/items/europe_202101/IPTVWORLDPL010.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='IPTV WORLD', cmdlist=cmdlist, finishedCallback=None)
                        elif returnValue =="com_795":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia601505.us.archive.org/2/items/europe_202101/IPTVWORLDPL011.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='IPTV WORLD', cmdlist=cmdlist, finishedCallback=None)
                        elif returnValue =="com_796":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia601505.us.archive.org/2/items/europe_202101/IPTVWORLDPL012.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='IPTV WORLD', cmdlist=cmdlist, finishedCallback=None)
                        elif returnValue =="com_797":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia601505.us.archive.org/2/items/europe_202101/IPTVWORLDPL013.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='IPTV WORLD', cmdlist=cmdlist, finishedCallback=None)
                        elif returnValue =="com_798":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia601505.us.archive.org/2/items/europe_202101/IPTVWORLDPL014.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='IPTV WORLD', cmdlist=cmdlist, finishedCallback=None)
                        elif returnValue =="com_799":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia601505.us.archive.org/2/items/europe_202101/IPTVWORLDPL015.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='IPTV WORLD', cmdlist=cmdlist, finishedCallback=None)
                        elif returnValue =="com_800":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia601505.us.archive.org/2/items/europe_202101/IPTVWORLDPL016.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='IPTV WORLD', cmdlist=cmdlist, finishedCallback=None)
                        elif returnValue =="com_801":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia601505.us.archive.org/2/items/europe_202101/IPTVWORLDPL017.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='IPTV WORLD', cmdlist=cmdlist, finishedCallback=None)
                        elif returnValue =="com_802":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia601505.us.archive.org/2/items/europe_202101/IPTVWORLDPL018.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='IPTV WORLD', cmdlist=cmdlist, finishedCallback=None)
                        elif returnValue =="com_803":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia601505.us.archive.org/2/items/europe_202101/IPTVWORLDPL019.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='IPTV WORLD', cmdlist=cmdlist, finishedCallback=None)
                        elif returnValue =="com_804":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia601505.us.archive.org/2/items/europe_202101/IPTVWORLDPL020.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='IPTV WORLD', cmdlist=cmdlist, finishedCallback=None)
                        elif returnValue =="com_805":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia601505.us.archive.org/2/items/europe_202101/IPTVWORLDPL021.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='IPTV WORLD', cmdlist=cmdlist, finishedCallback=None)
                        elif returnValue =="com_806":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia601505.us.archive.org/2/items/europe_202101/IPTVWORLDPL022.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='IPTV WORLD', cmdlist=cmdlist, finishedCallback=None)
                        elif returnValue =="com_807":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia601505.us.archive.org/2/items/europe_202101/IPTVWORLDPL023.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='IPTV WORLD', cmdlist=cmdlist, finishedCallback=None)
                        elif returnValue =="com_808":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia601505.us.archive.org/2/items/europe_202101/IPTVWORLDPL024.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='IPTV WORLD', cmdlist=cmdlist, finishedCallback=None)
                        elif returnValue =="com_809":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia601505.us.archive.org/2/items/europe_202101/IPTVWORLDPL025.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='IPTV WORD', cmdlist=cmdlist, finishedCallback=None)
                        elif returnValue =="com_810":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia601505.us.archive.org/2/items/europe_202101/IPTVWORLDPL026.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='IPTV WORD', cmdlist=cmdlist, finishedCallback=None)
                        elif returnValue =="com_811":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia601505.us.archive.org/2/items/europe_202101/IPTVWORLDPL027.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='IPTV WORLD', cmdlist=cmdlist, finishedCallback=None)
                        elif returnValue =="com_812":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia601505.us.archive.org/2/items/europe_202101/IPTVWORLDPL028.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='IPTV WORLD', cmdlist=cmdlist, finishedCallback=None)
                        elif returnValue =="com_813":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia601505.us.archive.org/2/items/europe_202101/IPTVWORLDPL029.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='IPTV WORLD', cmdlist=cmdlist, finishedCallback=None)
                        elif returnValue =="com_814":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia601505.us.archive.org/2/items/europe_202101/IPTVWORLDPL030.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='IPTV WORLD', cmdlist=cmdlist, finishedCallback=None)
                        elif returnValue =="com_815":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia601505.us.archive.org/2/items/europe_202101/IPTVWORLDPL031.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='IPTV WORLD', cmdlist=cmdlist, finishedCallback=None)
                        elif returnValue =="com_816":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia601505.us.archive.org/2/items/europe_202101/IPTVWORLDPL032.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='IPTV WORLD', cmdlist=cmdlist, finishedCallback=None)
                        elif returnValue =="com_817":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia601505.us.archive.org/2/items/europe_202101/IPTVWORLDPL033.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='IPTV WORLD', cmdlist=cmdlist, finishedCallback=None)
                        elif returnValue =="com_818":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia601505.us.archive.org/2/items/europe_202101/IPTVWORLDPL034.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='IPTV WORLD', cmdlist=cmdlist, finishedCallback=None)
                        elif returnValue =="com_819":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia601505.us.archive.org/2/items/europe_202101/IPTVWORLDPL035.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='IPTV WORLD', cmdlist=cmdlist, finishedCallback=None)
                        elif returnValue =="com_820":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia601505.us.archive.org/2/items/europe_202101/IPTVWORLDPL036.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='IPTV WORLD', cmdlist=cmdlist, finishedCallback=None)
                        elif returnValue =="com_821":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia601505.us.archive.org/2/items/europe_202101/IPTVWORLDPL037.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='IPTV WORLD', cmdlist=cmdlist, finishedCallback=None)
                        elif returnValue =="com_822":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia601505.us.archive.org/2/items/europe_202101/IPTVWORLDPL038.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='IPTV WORLD', cmdlist=cmdlist, finishedCallback=None)
                        elif returnValue =="com_823":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia601505.us.archive.org/2/items/europe_202101/IPTVWORLDPL039.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='IPTV WORLD', cmdlist=cmdlist, finishedCallback=None)
                        elif returnValue =="com_824":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia601505.us.archive.org/2/items/europe_202101/IPTVWORLDPL040.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='IPTV WORLD', cmdlist=cmdlist, finishedCallback=None)
                        elif returnValue =="com_825":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia601505.us.archive.org/2/items/europe_202101/IPTVWORLDPL041.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='IPTV WORLD', cmdlist=cmdlist, finishedCallback=None)
                        elif returnValue =="com_826":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia601505.us.archive.org/2/items/europe_202101/IPTVWORLDPL042.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='IPTV WORLD', cmdlist=cmdlist, finishedCallback=None)
                        elif returnValue =="com_827":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia601505.us.archive.org/2/items/europe_202101/IPTVWORLDPL043.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='IPTV WORLD', cmdlist=cmdlist, finishedCallback=None)
                        elif returnValue =="com_828":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia601505.us.archive.org/2/items/europe_202101/IPTVWORLDPL044.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='IPTV WORLD', cmdlist=cmdlist, finishedCallback=None)
                        elif returnValue =="com_829":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia601505.us.archive.org/2/items/europe_202101/IPTVWORLDPL045.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='IPTV WORLD', cmdlist=cmdlist, finishedCallback=None)
                        elif returnValue =="com_830":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia601505.us.archive.org/2/items/europe_202101/IPTVWORLDPL046.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='IPTV WORLD', cmdlist=cmdlist, finishedCallback=None)
                        elif returnValue =="com_831":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia601505.us.archive.org/2/items/europe_202101/IPTVWORLDPL047.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='IPTV WORLD', cmdlist=cmdlist, finishedCallback=None)
                        elif returnValue =="com_832":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia601505.us.archive.org/2/items/europe_202101/IPTVWORLDPL048.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='IPTV WORLD', cmdlist=cmdlist, finishedCallback=None)
                        elif returnValue =="com_833":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia601505.us.archive.org/2/items/europe_202101/IPTVWORLDPL049.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='IPTV WORLD', cmdlist=cmdlist, finishedCallback=None)
                        elif returnValue =="com_834":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia601505.us.archive.org/2/items/europe_202101/IPTVWORLDPL050.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='IPTV WORLD', cmdlist=cmdlist, finishedCallback=None)
                        elif returnValue =="com_0835":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia601505.us.archive.org/2/items/europe_202101/IPTVWORLDPON10.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='IPTV WORLD', cmdlist=cmdlist, finishedCallback=None)
                        elif returnValue =="com_0836":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia601505.us.archive.org/2/items/europe_202101/IPTVWORLDPON20.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='IPTV WORLD', cmdlist=cmdlist, finishedCallback=None)
                        elif returnValue =="com_0837":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia601505.us.archive.org/2/items/europe_202101/IPTVWORLDPON50.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='IPTV WORLD', cmdlist=cmdlist, finishedCallback=None)
                        elif returnValue =="com_835":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia601505.us.archive.org/2/items/europe_202101/IPTVWORLDPO001.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='IPTV WORLD', cmdlist=cmdlist, finishedCallback=None)
                        elif returnValue =="com_836":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia601505.us.archive.org/2/items/europe_202101/IPTVWORLDPO002.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='IPTV WORLD', cmdlist=cmdlist, finishedCallback=None)
                        elif returnValue =="com_837":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia601505.us.archive.org/2/items/europe_202101/IPTVWORLDPO002.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='IPTV WORLD', cmdlist=cmdlist, finishedCallback=None)
                        elif returnValue =="com_838":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia601505.us.archive.org/2/items/europe_202101/IPTVWORLDPO003.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='IPTV WORLD', cmdlist=cmdlist, finishedCallback=None)
                        elif returnValue =="com_839":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia601505.us.archive.org/2/items/europe_202101/IPTVWORLDPO004.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='IPTV WORLD', cmdlist=cmdlist, finishedCallback=None)
                        elif returnValue =="com_840":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia601505.us.archive.org/2/items/europe_202101/IPTVWORLDPO005.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='IPTV WORLD', cmdlist=cmdlist, finishedCallback=None)
                        elif returnValue =="com_841":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia601505.us.archive.org/2/items/europe_202101/IPTVWORLDPO006.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='IPTV WORLD', cmdlist=cmdlist, finishedCallback=None)
                        elif returnValue =="com_842":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia601505.us.archive.org/2/items/europe_202101/IPTVWORLDPO007.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='IPTV WORLD', cmdlist=cmdlist, finishedCallback=None)
                        elif returnValue =="com_843":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia601505.us.archive.org/2/items/europe_202101/IPTVWORLDPO008.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='IPTV WORLD', cmdlist=cmdlist, finishedCallback=None)
                        elif returnValue =="com_844":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia601505.us.archive.org/2/items/europe_202101/IPTVWORLDPO009.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='IPTV WORLD', cmdlist=cmdlist, finishedCallback=None)
                        elif returnValue =="com_845":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia601505.us.archive.org/2/items/europe_202101/IPTVWORLDPO010.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='IPTV WORLD', cmdlist=cmdlist, finishedCallback=None)
                        elif returnValue =="com_846":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia601505.us.archive.org/2/items/europe_202101/IPTVWORLDPO011.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='IPTV WORLD', cmdlist=cmdlist, finishedCallback=None)
                        elif returnValue =="com_847":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia601505.us.archive.org/2/items/europe_202101/IPTVWORLDPO012.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='IPTV WORLD', cmdlist=cmdlist, finishedCallback=None)
                        elif returnValue =="com_848":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia601505.us.archive.org/2/items/europe_202101/IPTVWORLDPO013.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='IPTV WORLD', cmdlist=cmdlist, finishedCallback=None)
                        elif returnValue =="com_849":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia601505.us.archive.org/2/items/europe_202101/IPTVWORLDPO014.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='IPTV WORLD', cmdlist=cmdlist, finishedCallback=None)
                        elif returnValue =="com_850":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia601505.us.archive.org/2/items/europe_202101/IPTVWORLDPO015.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='IPTV WORLD', cmdlist=cmdlist, finishedCallback=None)
                        elif returnValue =="com_851":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia601505.us.archive.org/2/items/europe_202101/IPTVWORLDPO016.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='IPTV WORLD', cmdlist=cmdlist, finishedCallback=None)
                        elif returnValue =="com_852":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'") 
                                cmdlist.append("%s https://ia601505.us.archive.org/2/items/europe_202101/IPTVWORLDPO017.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='IPTV WORLD', cmdlist=cmdlist, finishedCallback=None)
                        elif returnValue =="com_853":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia601505.us.archive.org/2/items/europe_202101/IPTVWORLDPO018.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='IPTV WORLD', cmdlist=cmdlist, finishedCallback=None)
                        elif returnValue =="com_854":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia601505.us.archive.org/2/items/europe_202101/IPTVWORLDPO019.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='IPTV WORLD', cmdlist=cmdlist, finishedCallback=None)
                        elif returnValue =="com_855":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia601505.us.archive.org/2/items/europe_202101/IPTVWORLDPO020.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='IPTV WORLD', cmdlist=cmdlist, finishedCallback=None)
                        elif returnValue =="com_856":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia601505.us.archive.org/2/items/europe_202101/IPTVWORLDPO021.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='IPTV WORLD', cmdlist=cmdlist, finishedCallback=None)
                        elif returnValue =="com_857":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia601505.us.archive.org/2/items/europe_202101/IPTVWORLDPO022.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='IPTV WORLD', cmdlist=cmdlist, finishedCallback=None)
                        elif returnValue =="com_858":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")    
                                cmdlist.append("%s https://ia601505.us.archive.org/2/items/europe_202101/IPTVWORLDPO023.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='IPTV WORLD', cmdlist=cmdlist, finishedCallback=None)
                        elif returnValue =="com_859":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia601505.us.archive.org/2/items/europe_202101/IPTVWORLDPO024.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='IPTV WORLD', cmdlist=cmdlist, finishedCallback=None)
                        elif returnValue =="com_860":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia601505.us.archive.org/2/items/europe_202101/IPTVWORLDPO025.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='IPTV WORLD', cmdlist=cmdlist, finishedCallback=None)
                        elif returnValue =="com_861":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia601505.us.archive.org/2/items/europe_202101/IPTVWORLDPO026.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='IPTV WORLD', cmdlist=cmdlist, finishedCallback=None)
                        elif returnValue =="com_862":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia601505.us.archive.org/2/items/europe_202101/IPTVWORLDPO027.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='IPTV WORLD', cmdlist=cmdlist, finishedCallback=None)
                        elif returnValue =="com_863":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia601505.us.archive.org/2/items/europe_202101/IPTVWORLDPO028.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='IPTV WORLD', cmdlist=cmdlist, finishedCallback=None)
                        elif returnValue =="com_864":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia601505.us.archive.org/2/items/europe_202101/IPTVWORLDPO029.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='IPTV WORLD', cmdlist=cmdlist, finishedCallback=None)
                        elif returnValue =="com_865":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia601505.us.archive.org/2/items/europe_202101/IPTVWORLDPO030.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='IPTV WORLD', cmdlist=cmdlist, finishedCallback=None)
                        elif returnValue =="com_866":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia601505.us.archive.org/2/items/europe_202101/IPTVWORLDPO031.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='IPTV WORLD', cmdlist=cmdlist, finishedCallback=None)
                        elif returnValue =="com_867":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia601505.us.archive.org/2/items/europe_202101/IPTVWORLDPO032.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='IPTV WORLD', cmdlist=cmdlist, finishedCallback=None)
                        elif returnValue =="com_868":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia601505.us.archive.org/2/items/europe_202101/IPTVWORLDPO033.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='IPTV WORLD', cmdlist=cmdlist, finishedCallback=None)
                        elif returnValue =="com_869":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia601505.us.archive.org/2/items/europe_202101/IPTVWORLDPO034.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='IPTV WORLD', cmdlist=cmdlist, finishedCallback=None)
                        elif returnValue =="com_870":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia601505.us.archive.org/2/items/europe_202101/IPTVWORLDPO035.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='IPTV WORLD', cmdlist=cmdlist, finishedCallback=None)
                        elif returnValue =="com_871":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia601505.us.archive.org/2/items/europe_202101/IPTVWORLDPO036.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='IPTV USA', cmdlist=cmdlist, finishedCallback=None)
                        elif returnValue =="com_872":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia601505.us.archive.org/2/items/europe_202101/IPTVWORLDPO037.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='IPTV USA', cmdlist=cmdlist, finishedCallback=None)
                        elif returnValue =="com_873":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia601505.us.archive.org/2/items/europe_202101/IPTVWORLDPO038.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='IPTV USA', cmdlist=cmdlist, finishedCallback=None)
                        elif returnValue =="com_874":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'") 
                                cmdlist.append("%s https://ia601505.us.archive.org/2/items/europe_202101/IPTVWORLDPO039.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='IPTV USA', cmdlist=cmdlist, finishedCallback=None)
                        elif returnValue =="com_875":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia601505.us.archive.org/2/items/europe_202101/IPTVWORLDPO040.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='IPTV USA', cmdlist=cmdlist, finishedCallback=None)
                        elif returnValue =="com_876":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia601505.us.archive.org/2/items/europe_202101/IPTVWORLDPO041.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='IPTV USA', cmdlist=cmdlist, finishedCallback=None)
                        elif returnValue =="com_877":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia601505.us.archive.org/2/items/europe_202101/IPTVWORLDPO042.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='IPTV USA', cmdlist=cmdlist, finishedCallback=None)
                        elif returnValue =="com_878":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")    
                                cmdlist.append("%s https://ia601505.us.archive.org/2/items/europe_202101/IPTVWORLDPO043.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='IPTV USA', cmdlist=cmdlist, finishedCallback=None)
                        elif returnValue =="com_879":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia601505.us.archive.org/2/items/europe_202101/IPTVWORLDPO044.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='IPTV USA', cmdlist=cmdlist, finishedCallback=None)
                        elif returnValue =="com_880":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia601505.us.archive.org/2/items/europe_202101/IPTVWORLDPO045.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='IPTV USA', cmdlist=cmdlist, finishedCallback=None)
                        elif returnValue =="com_881":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia601505.us.archive.org/2/items/europe_202101/IPTVWORLDPO046.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='IPTV WORLD', cmdlist=cmdlist, finishedCallback=None)
                        elif returnValue =="com_882":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia601505.us.archive.org/2/items/europe_202101/IPTVWORLDPO047.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='IPTV WORLD', cmdlist=cmdlist, finishedCallback=None)
                        elif returnValue =="com_883":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia601505.us.archive.org/2/items/europe_202101/IPTVWORLDPO048.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='IPTV WORLD', cmdlist=cmdlist, finishedCallback=None)
                        elif returnValue =="com_884":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia601505.us.archive.org/2/items/europe_202101/IPTVWORLDPO049.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='IPTV WORLD', cmdlist=cmdlist, finishedCallback=None)
                        elif returnValue =="com_885":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia601505.us.archive.org/2/items/europe_202101/IPTVWORLDPO050.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='IPTV WORLD', cmdlist=cmdlist, finishedCallback=None)
                        elif returnValue =="com_0886":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia601505.us.archive.org/2/items/europe_202101/IPTVWORLDUKN10.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='IPTV WORLD', cmdlist=cmdlist, finishedCallback=None)
                        elif returnValue =="com_0887":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia601505.us.archive.org/2/items/europe_202101/IPTVWORLDUKN20.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='IPTV WORLD', cmdlist=cmdlist, finishedCallback=None)
                        elif returnValue =="com_0888":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia601505.us.archive.org/2/items/europe_202101/IPTVWORLDUKN50.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='IPTV WORLD', cmdlist=cmdlist, finishedCallback=None)
                        elif returnValue =="com_886":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia601505.us.archive.org/2/items/europe_202101/IPTVWORLDUK001.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='IPTV WORLD', cmdlist=cmdlist, finishedCallback=None)
                        elif returnValue =="com_887":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia601505.us.archive.org/2/items/europe_202101/IPTVWORLDUK002.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='IPTV WORLD', cmdlist=cmdlist, finishedCallback=None)
                        elif returnValue =="com_888":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia601505.us.archive.org/2/items/europe_202101/IPTVWORLDUK003.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='IPTV WORLD', cmdlist=cmdlist, finishedCallback=None)
                        elif returnValue =="com_889":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia601505.us.archive.org/2/items/europe_202101/IPTVWORLDUK004.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='IPTV WORLD', cmdlist=cmdlist, finishedCallback=None)
                        elif returnValue =="com_890":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia601505.us.archive.org/2/items/europe_202101/IPTVWORLDUK005.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='IPTV WORLD', cmdlist=cmdlist, finishedCallback=None)
                        elif returnValue =="com_891":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia601505.us.archive.org/2/items/europe_202101/IPTVWORLDUK006.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='IPTV WORLD', cmdlist=cmdlist, finishedCallback=None)
                        elif returnValue =="com_892":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia601505.us.archive.org/2/items/europe_202101/IPTVWORLDUK007.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='IPTV WORLD', cmdlist=cmdlist, finishedCallback=None)
                        elif returnValue =="com_893":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia601505.us.archive.org/2/items/europe_202101/IPTVWORLDUK008.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='IPTV WORLD', cmdlist=cmdlist, finishedCallback=None)
                        elif returnValue =="com_894":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia601505.us.archive.org/2/items/europe_202101/IPTVWORLDUK009.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='IPTV WORLD', cmdlist=cmdlist, finishedCallback=None)
                        elif returnValue =="com_895":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia601505.us.archive.org/2/items/europe_202101/IPTVWORLDUK010.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='IPTV WORLD', cmdlist=cmdlist, finishedCallback=None)
                        elif returnValue =="com_896":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia601505.us.archive.org/2/items/europe_202101/IPTVWORLDUK011.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='IPTV WORLD', cmdlist=cmdlist, finishedCallback=None)
                        elif returnValue =="com_897":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia601505.us.archive.org/2/items/europe_202101/IPTVWORLDUK012.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='IPTV WORLD', cmdlist=cmdlist, finishedCallback=None)
                        elif returnValue =="com_898":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia601505.us.archive.org/2/items/europe_202101/IPTVWORLDUK013.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='IPTV WORLD', cmdlist=cmdlist, finishedCallback=None)
                        elif returnValue =="com_899":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia601505.us.archive.org/2/items/europe_202101/IPTVWORLDUK014.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='IPTV WORLD', cmdlist=cmdlist, finishedCallback=None)
                        elif returnValue =="com_900":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia601505.us.archive.org/2/items/europe_202101/IPTVWORLDUK015.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='IPTV WORLD', cmdlist=cmdlist, finishedCallback=None)
                        elif returnValue =="com_901":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia601505.us.archive.org/2/items/europe_202101/IPTVWORLDUK016.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='IPTV WORLD', cmdlist=cmdlist, finishedCallback=None)
                        elif returnValue =="com_902":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia601505.us.archive.org/2/items/europe_202101/IPTVWORLDUK017.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='IPTV WORLD', cmdlist=cmdlist, finishedCallback=None)
                        elif returnValue =="com_903":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia601505.us.archive.org/2/items/europe_202101/IPTVWORLDUK018.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='IPTV WORLD', cmdlist=cmdlist, finishedCallback=None)
                        elif returnValue =="com_904":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia601505.us.archive.org/2/items/europe_202101/IPTVWORLDUK019.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='IPTV WORLD', cmdlist=cmdlist, finishedCallback=None)
                        elif returnValue =="com_905":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia601505.us.archive.org/2/items/europe_202101/IPTVWORLDUK020.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='IPTV WORLD', cmdlist=cmdlist, finishedCallback=None)
                        elif returnValue =="com_906":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia601505.us.archive.org/2/items/europe_202101/IPTVWORLDUK021.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='IPTV WORLD', cmdlist=cmdlist, finishedCallback=None)
                        elif returnValue =="com_907":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia601505.us.archive.org/2/items/europe_202101/IPTVWORLDUK022.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='IPTV WORLD', cmdlist=cmdlist, finishedCallback=None)
                        elif returnValue =="com_908":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia601505.us.archive.org/2/items/europe_202101/IPTVWORLDUK023.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='IPTV WORLD', cmdlist=cmdlist, finishedCallback=None)
                        elif returnValue =="com_909":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia601505.us.archive.org/2/items/europe_202101/IPTVWORLDUK024.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='IPTV WORD', cmdlist=cmdlist, finishedCallback=None)
                        elif returnValue =="com_910":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia601505.us.archive.org/2/items/europe_202101/IPTVWORLDUK025.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='IPTV WORD', cmdlist=cmdlist, finishedCallback=None)
                        elif returnValue =="com_911":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia601505.us.archive.org/2/items/europe_202101/IPTVWORLDUK026.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='IPTV WORLD', cmdlist=cmdlist, finishedCallback=None)
                        elif returnValue =="com_912":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia601505.us.archive.org/2/items/europe_202101/IPTVWORLDUK027.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='IPTV WORLD', cmdlist=cmdlist, finishedCallback=None)
                        elif returnValue =="com_913":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia601505.us.archive.org/2/items/europe_202101/IPTVWORLDUK028.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='IPTV WORLD', cmdlist=cmdlist, finishedCallback=None)
                        elif returnValue =="com_914":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia601505.us.archive.org/2/items/europe_202101/IPTVWORLDUK029.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='IPTV WORLD', cmdlist=cmdlist, finishedCallback=None)
                        elif returnValue =="com_915":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia601505.us.archive.org/2/items/europe_202101/IPTVWORLDUK030.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='IPTV WORLD', cmdlist=cmdlist, finishedCallback=None)
                        elif returnValue =="com_916":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia601505.us.archive.org/2/items/europe_202101/IPTVWORLDUK031.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='IPTV WORLD', cmdlist=cmdlist, finishedCallback=None)
                        elif returnValue =="com_917":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia601505.us.archive.org/2/items/europe_202101/IPTVWORLDUK032.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='IPTV WORLD', cmdlist=cmdlist, finishedCallback=None)
                        elif returnValue =="com_918":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia601505.us.archive.org/2/items/europe_202101/IPTVWORLDUK033.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='IPTV WORLD', cmdlist=cmdlist, finishedCallback=None)
                        elif returnValue =="com_919":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia601505.us.archive.org/2/items/europe_202101/IPTVWORLDUK034.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='IPTV WORLD', cmdlist=cmdlist, finishedCallback=None)
                        elif returnValue =="com_920":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia601505.us.archive.org/2/items/europe_202101/IPTVWORLDUK035.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='IPTV WORLD', cmdlist=cmdlist, finishedCallback=None)
                        elif returnValue =="com_921":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia601505.us.archive.org/2/items/europe_202101/IPTVWORLDUK036.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='IPTV WORLD', cmdlist=cmdlist, finishedCallback=None)
                        elif returnValue =="com_922":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia601505.us.archive.org/2/items/europe_202101/IPTVWORLDUK037.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='IPTV WORLD', cmdlist=cmdlist, finishedCallback=None)
                        elif returnValue =="com_923":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia601505.us.archive.org/2/items/europe_202101/IPTVWORLDUK038.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='IPTV WORLD', cmdlist=cmdlist, finishedCallback=None)
                        elif returnValue =="com_924":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia601505.us.archive.org/2/items/europe_202101/IPTVWORLDUK039.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='IPTV WORLD', cmdlist=cmdlist, finishedCallback=None)
                        elif returnValue =="com_925":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia601505.us.archive.org/2/items/europe_202101/IPTVWORLDUK040.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='IPTV WORLD', cmdlist=cmdlist, finishedCallback=None)
                        elif returnValue =="com_926":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia601505.us.archive.org/2/items/europe_202101/IPTVWORLDUK041.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='IPTV WORLD', cmdlist=cmdlist, finishedCallback=None)
                        elif returnValue =="com_927":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia601505.us.archive.org/2/items/europe_202101/IPTVWORLDUK042.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='IPTV WORLD', cmdlist=cmdlist, finishedCallback=None)
                        elif returnValue =="com_928":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia601505.us.archive.org/2/items/europe_202101/IPTVWORLDUK043.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='IPTV WORLD', cmdlist=cmdlist, finishedCallback=None)
                        elif returnValue =="com_929":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia601505.us.archive.org/2/items/europe_202101/IPTVWORLDUK044.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='IPTV WORLD', cmdlist=cmdlist, finishedCallback=None)
                        elif returnValue =="com_930":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia601505.us.archive.org/2/items/europe_202101/IPTVWORLDUK045.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='IPTV WORLD', cmdlist=cmdlist, finishedCallback=None)
                        elif returnValue =="com_931":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia601505.us.archive.org/2/items/europe_202101/IPTVWORLDUK046.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='IPTV WORLD', cmdlist=cmdlist, finishedCallback=None)
                        elif returnValue =="com_932":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia601505.us.archive.org/2/items/europe_202101/IPTVWORLDUK047.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='IPTV WORLD', cmdlist=cmdlist, finishedCallback=None)
                        elif returnValue =="com_933":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia601505.us.archive.org/2/items/europe_202101/IPTVWORLDUK048.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='IPTV WORLD', cmdlist=cmdlist, finishedCallback=None)
                        elif returnValue =="com_934":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia601505.us.archive.org/2/items/europe_202101/IPTVWORLDUK049.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='IPTV WORLD', cmdlist=cmdlist, finishedCallback=None)
                        elif returnValue =="com_935":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia601505.us.archive.org/2/items/europe_202101/IPTVWORLDUK050.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='IPTV WORLD', cmdlist=cmdlist, finishedCallback=None)
                        elif returnValue =="com_0936":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia601505.us.archive.org/2/items/europe_202101/IPTVWORLDESN10.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='IPTV WORLD', cmdlist=cmdlist, finishedCallback=None)
                        elif returnValue =="com_0937":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia601505.us.archive.org/2/items/europe_202101/IPTVWORLDESN20.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='IPTV WORLD', cmdlist=cmdlist, finishedCallback=None)
                        elif returnValue =="com_0938":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia601505.us.archive.org/2/items/europe_202101/IPTVWORLDESN50.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='IPTV WORLD', cmdlist=cmdlist, finishedCallback=None)
                        elif returnValue =="com_936":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia601505.us.archive.org/2/items/europe_202101/IPTVWORLDES001.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='IPTV WORLD', cmdlist=cmdlist, finishedCallback=None)
                        elif returnValue =="com_937":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia601505.us.archive.org/2/items/europe_202101/IPTVWORLDES002.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='IPTV WORLD', cmdlist=cmdlist, finishedCallback=None)
                        elif returnValue =="com_938":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia601505.us.archive.org/2/items/europe_202101/IPTVWORLDES003.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='IPTV WORLD', cmdlist=cmdlist, finishedCallback=None)
                        elif returnValue =="com_939":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia601505.us.archive.org/2/items/europe_202101/IPTVWORLDES004.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='IPTV WORLD', cmdlist=cmdlist, finishedCallback=None)
                        elif returnValue =="com_940":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia601505.us.archive.org/2/items/europe_202101/IPTVWORLDES005.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='IPTV WORLD', cmdlist=cmdlist, finishedCallback=None)
                        elif returnValue =="com_941":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia601505.us.archive.org/2/items/europe_202101/IPTVWORLDES006.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='IPTV WORLD', cmdlist=cmdlist, finishedCallback=None)
                        elif returnValue =="com_942":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia601505.us.archive.org/2/items/europe_202101/IPTVWORLDES007.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='IPTV WORLD', cmdlist=cmdlist, finishedCallback=None)
                        elif returnValue =="com_943":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia601505.us.archive.org/2/items/europe_202101/IPTVWORLDES008.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='IPTV WORLD', cmdlist=cmdlist, finishedCallback=None)
                        elif returnValue =="com_944":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia601505.us.archive.org/2/items/europe_202101/IPTVWORLDES009.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='IPTV WORLD', cmdlist=cmdlist, finishedCallback=None)
                        elif returnValue =="com_945":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia601505.us.archive.org/2/items/europe_202101/IPTVWORLDES010.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='IPTV WORLD', cmdlist=cmdlist, finishedCallback=None)
                        elif returnValue =="com_946":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia601505.us.archive.org/2/items/europe_202101/IPTVWORLDES011.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='IPTV WORLD', cmdlist=cmdlist, finishedCallback=None)
                        elif returnValue =="com_947":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia601505.us.archive.org/2/items/europe_202101/IPTVWORLDES012.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='IPTV WORLD', cmdlist=cmdlist, finishedCallback=None)
                        elif returnValue =="com_948":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia601505.us.archive.org/2/items/europe_202101/IPTVWORLDES013.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='IPTV WORLD', cmdlist=cmdlist, finishedCallback=None)
                        elif returnValue =="com_949":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia601505.us.archive.org/2/items/europe_202101/IPTVWORLDES014.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='IPTV WORLD', cmdlist=cmdlist, finishedCallback=None)
                        elif returnValue =="com_950":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia601505.us.archive.org/2/items/europe_202101/IPTVWORLDES015.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='IPTV WORLD', cmdlist=cmdlist, finishedCallback=None)
                        elif returnValue =="com_951":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia601505.us.archive.org/2/items/europe_202101/IPTVWORLDES016.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='IPTV WORLD', cmdlist=cmdlist, finishedCallback=None)
                        elif returnValue =="com_952":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'") 
                                cmdlist.append("%s https://ia601505.us.archive.org/2/items/europe_202101/IPTVWORLDES017.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='IPTV WORLD', cmdlist=cmdlist, finishedCallback=None)
                        elif returnValue =="com_953":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia601505.us.archive.org/2/items/europe_202101/IPTVWORLDES018.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='IPTV WORLD', cmdlist=cmdlist, finishedCallback=None)
                        elif returnValue =="com_954":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia601505.us.archive.org/2/items/europe_202101/IPTVWORLDES019.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='IPTV WORLD', cmdlist=cmdlist, finishedCallback=None)
                        elif returnValue =="com_955":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia601505.us.archive.org/2/items/europe_202101/IPTVWORLDES020.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='IPTV WORLD', cmdlist=cmdlist, finishedCallback=None)
                        elif returnValue =="com_956":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia601505.us.archive.org/2/items/europe_202101/IPTVWORLDES021.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='IPTV WORLD', cmdlist=cmdlist, finishedCallback=None)
                        elif returnValue =="com_957":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia601505.us.archive.org/2/items/europe_202101/IPTVWORLDES022.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='IPTV WORLD', cmdlist=cmdlist, finishedCallback=None)
                        elif returnValue =="com_958":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia601505.us.archive.org/2/items/europe_202101/IPTVWORLDES023.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='IPTV WORLD', cmdlist=cmdlist, finishedCallback=None)
                        elif returnValue =="com_959":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia601505.us.archive.org/2/items/europe_202101/IPTVWORLDES024.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='IPTV WORLD', cmdlist=cmdlist, finishedCallback=None)
                        elif returnValue =="com_960":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia601505.us.archive.org/2/items/europe_202101/IPTVWORLDES025.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='IPTV WORLD', cmdlist=cmdlist, finishedCallback=None)
                        elif returnValue =="com_961":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia601505.us.archive.org/2/items/europe_202101/IPTVWORLDES026.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='IPTV WORLD', cmdlist=cmdlist, finishedCallback=None)
                        elif returnValue =="com_962":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia601505.us.archive.org/2/items/europe_202101/IPTVWORLDES027.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='IPTV WORLD', cmdlist=cmdlist, finishedCallback=None)
                        elif returnValue =="com_963":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia601505.us.archive.org/2/items/europe_202101/IPTVWORLDES028.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='IPTV WORLD', cmdlist=cmdlist, finishedCallback=None)
                        elif returnValue =="com_964":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia601505.us.archive.org/2/items/europe_202101/IPTVWORLDES029.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='IPTV WORLD', cmdlist=cmdlist, finishedCallback=None)
                        elif returnValue =="com_965":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia601505.us.archive.org/2/items/europe_202101/IPTVWORLDES030.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='IPTV WORLD', cmdlist=cmdlist, finishedCallback=None)
                        elif returnValue =="com_966":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia601505.us.archive.org/2/items/europe_202101/IPTVWORLDES031.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='IPTV WORLD', cmdlist=cmdlist, finishedCallback=None)
                        elif returnValue =="com_967":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia601505.us.archive.org/2/items/europe_202101/IPTVWORLDES032.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='IPTV WORLD', cmdlist=cmdlist, finishedCallback=None)
                        elif returnValue =="com_968":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia601505.us.archive.org/2/items/europe_202101/IPTVWORLDES033.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='IPTV WORLD', cmdlist=cmdlist, finishedCallback=None)
                        elif returnValue =="com_969":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia601505.us.archive.org/2/items/europe_202101/IPTVWORLDES034.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='IPTV WORLD', cmdlist=cmdlist, finishedCallback=None)
                        elif returnValue =="com_970":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia601505.us.archive.org/2/items/europe_202101/IPTVWORLDES035.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='IPTV WORLD', cmdlist=cmdlist, finishedCallback=None)
                        elif returnValue =="com_971":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia601505.us.archive.org/2/items/europe_202101/IPTVWORLDES036.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='IPTV WORLD', cmdlist=cmdlist, finishedCallback=None)
                        elif returnValue =="com_972":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia601505.us.archive.org/2/items/europe_202101/IPTVWORLDES037.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='IPTV WORLD', cmdlist=cmdlist, finishedCallback=None)
                        elif returnValue =="com_973":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia601505.us.archive.org/2/items/europe_202101/IPTVWORLDES038.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='IPTV WORLD', cmdlist=cmdlist, finishedCallback=None)
                        elif returnValue =="com_974":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia601505.us.archive.org/2/items/europe_202101/IPTVWORLDES039.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='IPTV WORLD', cmdlist=cmdlist, finishedCallback=None)
                        elif returnValue =="com_975":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'") 
                                cmdlist.append("%s https://ia601505.us.archive.org/2/items/europe_202101/IPTVWORLDES040.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='IPTV WORLD', cmdlist=cmdlist, finishedCallback=None)
                        elif returnValue =="com_976":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia601505.us.archive.org/2/items/europe_202101/IPTVWORLDES041.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='IPTV WORLD', cmdlist=cmdlist, finishedCallback=None)
                        elif returnValue =="com_977":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia601505.us.archive.org/2/items/europe_202101/IPTVWORLDES042.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='IPTV WORLD', cmdlist=cmdlist, finishedCallback=None)
                        elif returnValue =="com_978":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia601505.us.archive.org/2/items/europe_202101/IPTVWORLDES043.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='IPTV WORLD', cmdlist=cmdlist, finishedCallback=None)
                        elif returnValue =="com_979":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia601505.us.archive.org/2/items/europe_202101/IPTVWORLDES044.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='IPTV WORLD', cmdlist=cmdlist, finishedCallback=None)
                        elif returnValue =="com_980":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia601505.us.archive.org/2/items/europe_202101/IPTVWORLDES045.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='IPTV WORLD', cmdlist=cmdlist, finishedCallback=None)
                        elif returnValue =="com_981":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia601505.us.archive.org/2/items/europe_202101/IPTVWORLDES046.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='IPTV WORLD', cmdlist=cmdlist, finishedCallback=None)
                        elif returnValue =="com_982":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia601505.us.archive.org/2/items/europe_202101/IPTVWORLDES047.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='IPTV WORLD', cmdlist=cmdlist, finishedCallback=None)
                        elif returnValue =="com_983":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia601505.us.archive.org/2/items/europe_202101/IPTVWORLDES048.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='IPTV WORLD', cmdlist=cmdlist, finishedCallback=None)
                        elif returnValue =="com_984":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia601505.us.archive.org/2/items/europe_202101/IPTVWORLDES049.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='IPTV WORLD', cmdlist=cmdlist, finishedCallback=None)
                        elif returnValue =="com_985":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia601505.us.archive.org/2/items/europe_202101/IPTVWORLDES050.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='IPTV WORLD', cmdlist=cmdlist, finishedCallback=None)
                        elif returnValue =="com_0986":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'") 
                                cmdlist.append("%s https://ia601505.us.archive.org/2/items/europe_202101/IPTVWORLDALN10.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='IPTV WORLD', cmdlist=cmdlist, finishedCallback=None)
                        elif returnValue =="com_0987":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia601505.us.archive.org/2/items/europe_202101/IPTVWORLDALN20.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='IPTV WORLD', cmdlist=cmdlist, finishedCallback=None)
                        elif returnValue =="com_0988":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia601505.us.archive.org/2/items/europe_202101/IPTVWORLDALN50.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='IPTV WORLD', cmdlist=cmdlist, finishedCallback=None)
                        elif returnValue =="com_0989":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia601505.us.archive.org/2/items/europe_202101/IPTVWORLDALN100.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='IPTV WORLD', cmdlist=cmdlist, finishedCallback=None)
                        elif returnValue =="com_986":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'") 
                                cmdlist.append("%s https://ia601505.us.archive.org/2/items/europe_202101/IPTVWORLDAL001.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='IPTV WORLD', cmdlist=cmdlist, finishedCallback=None)
                        elif returnValue =="com_987":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia601505.us.archive.org/2/items/europe_202101/IPTVWORLDAL002.sh-qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='IPTV WORLD', cmdlist=cmdlist, finishedCallback=None)
                        elif returnValue =="com_988":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia601505.us.archive.org/2/items/europe_202101/IPTVWORLDAL003.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='IPTV WORLD', cmdlist=cmdlist, finishedCallback=None)
                        elif returnValue =="com_989":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia601505.us.archive.org/2/items/europe_202101/IPTVWORLDAL004.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='IPTV WORLD', cmdlist=cmdlist, finishedCallback=None)
                        elif returnValue =="com_990":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia601505.us.archive.org/2/items/europe_202101/IPTVWORLDAL005.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='IPTV WORLD', cmdlist=cmdlist, finishedCallback=None)
                        elif returnValue =="com_991":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia601505.us.archive.org/2/items/europe_202101/IPTVWORLDAL006.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='IPTV WORLD', cmdlist=cmdlist, finishedCallback=None)
                        elif returnValue =="com_992":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia601505.us.archive.org/2/items/europe_202101/IPTVWORLDAL007.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='IPTV WORLD', cmdlist=cmdlist, finishedCallback=None)
                        elif returnValue =="com_993":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia601505.us.archive.org/2/items/europe_202101/IPTVWORLDAL008.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='IPTV WORLD', cmdlist=cmdlist, finishedCallback=None)
                        elif returnValue =="com_994":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia601505.us.archive.org/2/items/europe_202101/IPTVWORLDAL009.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='IPTV WORLD', cmdlist=cmdlist, finishedCallback=None)
                        elif returnValue =="com_995":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia601505.us.archive.org/2/items/europe_202101/IPTVWORLDAL010.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='IPTV WORLD', cmdlist=cmdlist, finishedCallback=None)
                        elif returnValue =="com_996":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia601505.us.archive.org/2/items/europe_202101/IPTVWORLDAL011.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='IPTV WORLD', cmdlist=cmdlist, finishedCallback=None)
                        elif returnValue =="com_997":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia601505.us.archive.org/2/items/europe_202101/IPTVWORLDAL012.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='IPTV WORLD', cmdlist=cmdlist, finishedCallback=None)
                        elif returnValue =="com_998":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia601505.us.archive.org/2/items/europe_202101/IPTVWORLDAL013.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='IPTV WORLD', cmdlist=cmdlist, finishedCallback=None)

################################################################################################
                        elif returnValue =="com_999":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia801403.us.archive.org/21/items/iptvworldgr-001/IPTVWORLDSPN10.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='IPTV WORLDSP', cmdlist=cmdlist, finishedCallback=None)
                        elif returnValue =="com_1000":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia801403.us.archive.org/21/items/iptvworldgr-001/IPTVWORLDSP001.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='IPTV WORLD', cmdlist=cmdlist, finishedCallback=None)
                        elif returnValue =="com_1001":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia801403.us.archive.org/21/items/iptvworldgr-001/IPTVWORLDSP002.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='IPTV WORLD', cmdlist=cmdlist, finishedCallback=None)
                        elif returnValue =="com_1002":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia801403.us.archive.org/21/items/iptvworldgr-001/IPTVWORLDSP003.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='IPTV WORLD', cmdlist=cmdlist, finishedCallback=None)
                        elif returnValue =="com_1003":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia801403.us.archive.org/21/items/iptvworldgr-001/IPTVWORLDSP004.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='IPTV WORLD', cmdlist=cmdlist, finishedCallback=None)
                        elif returnValue =="com_1004":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia801403.us.archive.org/21/items/iptvworldgr-001/IPTVWORLDSP005.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='IPTV WORLD', cmdlist=cmdlist, finishedCallback=None)
                        elif returnValue =="com_1005":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia801403.us.archive.org/21/items/iptvworldgr-001/IPTVWORLDSP006.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='IPTV WORD', cmdlist=cmdlist, finishedCallback=None)
                        elif returnValue =="com_592":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia801403.us.archive.org/21/items/iptvworldgr-001/IPTVWORLDSP007.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='IPTV WORD', cmdlist=cmdlist, finishedCallback=None)
                        elif returnValue =="com_1006":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia801403.us.archive.org/21/items/iptvworldgr-001/IPTVWORLDSPN10.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='IPTV WORLD', cmdlist=cmdlist, finishedCallback=None)
                        elif returnValue =="com_1007":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia801403.us.archive.org/21/items/iptvworldgr-001/IPTVWORLDARN10.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='IPTV WORLD', cmdlist=cmdlist, finishedCallback=None)
                        elif returnValue =="com_1008":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia801403.us.archive.org/21/items/iptvworldgr-001/IPTVWORLDAR001.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='IPTV WORLD', cmdlist=cmdlist, finishedCallback=None)
                        elif returnValue =="com_1009":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia801403.us.archive.org/21/items/iptvworldgr-001/IPTVWORLDAR002.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='IPTV WORLD', cmdlist=cmdlist, finishedCallback=None)
                        elif returnValue =="com_1010":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia801403.us.archive.org/21/items/iptvworldgr-001/IPTVWORLDAR003.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='IPTV WORLD', cmdlist=cmdlist, finishedCallback=None)
                        elif returnValue =="com_1011":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia801403.us.archive.org/21/items/iptvworldgr-001/IPTVWORLDAR004.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='IPTV WORLD', cmdlist=cmdlist, finishedCallback=None)
                        elif returnValue =="com_1012":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia801403.us.archive.org/21/items/iptvworldgr-001/IPTVWORLDAR005.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='IPTV WORLD', cmdlist=cmdlist, finishedCallback=None)
                        elif returnValue =="com_1013":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia801403.us.archive.org/21/items/iptvworldgr-001/IPTVWORLDAR006.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='IPTV WORLD', cmdlist=cmdlist, finishedCallback=None)
                        elif returnValue =="com_1014":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia801403.us.archive.org/21/items/iptvworldgr-001/IPTVWORLDAR009.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='IPTV WORLD', cmdlist=cmdlist, finishedCallback=None)
                        elif returnValue =="com_1015":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia801403.us.archive.org/21/items/iptvworldgr-001/IPTVWORLDAR008.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='IPTV WORLD', cmdlist=cmdlist, finishedCallback=None)
                        elif returnValue =="com_1016":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia801403.us.archive.org/21/items/iptvworldgr-001/IPTVWORLDAR009.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='IPTV WORLD', cmdlist=cmdlist, finishedCallback=None)
                        elif returnValue =="com_1017":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia801403.us.archive.org/21/items/iptvworldgr-001/IPTVWORLDAR010.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='IPTV WORLD', cmdlist=cmdlist, finishedCallback=None)
                        elif returnValue =="com_1018":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia801403.us.archive.org/21/items/iptvworldgr-001/IPTVWORLDFRN10.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='IPTV WORLD', cmdlist=cmdlist, finishedCallback=None)
                        elif returnValue =="com_1019":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia801403.us.archive.org/21/items/iptvworldgr-001/IPTVWORLDFR001.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='IPTV WORLD', cmdlist=cmdlist, finishedCallback=None)
                        elif returnValue =="com_1020":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia801403.us.archive.org/21/items/iptvworldgr-001/IPTVWORLDFR002.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='IPTV WORLD', cmdlist=cmdlist, finishedCallback=None)
                        elif returnValue =="com_1021":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia801403.us.archive.org/21/items/iptvworldgr-001/IPTVWORLDFR003.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='IPTV WORLD', cmdlist=cmdlist, finishedCallback=None)
                        elif returnValue =="com_1022":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia801403.us.archive.org/21/items/iptvworldgr-001/IPTVWORLDFR004.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='IPTV WORLD', cmdlist=cmdlist, finishedCallback=None)
                        elif returnValue =="com_1023":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia801403.us.archive.org/21/items/iptvworldgr-001/IPTVWORLDFR005.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='IPTV WORLD', cmdlist=cmdlist, finishedCallback=None)
                        elif returnValue =="com_1024":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia801403.us.archive.org/21/items/iptvworldgr-001/IPTVWORLDFR006.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='IPTV WORLD', cmdlist=cmdlist, finishedCallback=None)
                        elif returnValue =="com_1025":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia801403.us.archive.org/21/items/iptvworldgr-001/IPTVWORLDFR007.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='IPTV WORLD', cmdlist=cmdlist, finishedCallback=None)
                        elif returnValue =="com_1026":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia801403.us.archive.org/21/items/iptvworldgr-001/IPTVWORLDFR008.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='IPTV WORLD', cmdlist=cmdlist, finishedCallback=None)
                        elif returnValue =="com_1027":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia801403.us.archive.org/21/items/iptvworldgr-001/IPTVWORLDFR009.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='IPTV WORLD', cmdlist=cmdlist, finishedCallback=None)
                        elif returnValue =="com_1028":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia801403.us.archive.org/21/items/iptvworldgr-001/IPTVWORLDFR010.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='IPTV WORLD', cmdlist=cmdlist, finishedCallback=None)
                        elif returnValue =="com_1029":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia801403.us.archive.org/21/items/iptvworldgr-001/IPTVWORLDN100.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='IPTV WORLD', cmdlist=cmdlist, finishedCallback=None)
                        elif returnValue =="com_1030":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia801403.us.archive.org/21/items/iptvworldgr-001/IPTVWORLDN50.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='IPTV WORLD', cmdlist=cmdlist, finishedCallback=None)
                        elif returnValue =="com_1031":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia801403.us.archive.org/21/items/iptvworldgr-001/IPTVWORLDN20.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='IPTV WORLD', cmdlist=cmdlist, finishedCallback=None)
                        elif returnValue =="com_1032":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia801403.us.archive.org/21/items/iptvworldgr-001/IPTVWORLDN10.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='IPTV WORLD', cmdlist=cmdlist, finishedCallback=None)
                        elif returnValue =="com1033":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia601501.us.archive.org/15/items/iptvworldgr_001_202101/IPTVWORLDSP001.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='IPTV WORLD', cmdlist=cmdlist, finishedCallback=None)
                        elif returnValue =="com_1034":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia601501.us.archive.org/15/items/iptvworldgr_001_202101/IPTVWORLDAR001.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='IPTV WORLD', cmdlist=cmdlist, finishedCallback=None)
                        elif returnValue =="com_1035":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia601501.us.archive.org/15/items/iptvworldgr_001_202101/IPTVWORLDFR001.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='IPTV WORLD', cmdlist=cmdlist, finishedCallback=None)
                        elif returnValue =="com_1036":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia601501.us.archive.org/15/items/iptvworldgr_001_202101/IPTVWORLDUS001.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='IPTV WORLD', cmdlist=cmdlist, finishedCallback=None)
                        elif returnValue =="com_1037":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia601501.us.archive.org/15/items/iptvworldgr_001_202101/IPTVWORLDTR001.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='IPTV WORLD', cmdlist=cmdlist, finishedCallback=None)
                        elif returnValue =="com_1038":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia601501.us.archive.org/15/items/iptvworldgr_001_202101/IPTVWORLDGR001.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='IPTV WORLD', cmdlist=cmdlist, finishedCallback=None)
                        elif returnValue =="com_1039":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia601501.us.archive.org/15/items/iptvworldgr_001_202101/IPTVWORLDIT001.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='IPTV WORLD', cmdlist=cmdlist, finishedCallback=None)
                        elif returnValue =="com_1040":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia601501.us.archive.org/15/items/iptvworldgr_001_202101/IPTVWORLDES001.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='IPTV WORLD', cmdlist=cmdlist, finishedCallback=None)
                        elif returnValue =="com_1041":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia601501.us.archive.org/15/items/iptvworldgr_001_202101/IPTVWORLDALL001.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='IPTV WORLD', cmdlist=cmdlist, finishedCallback=None)
                        elif returnValue =="com_01042":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia601505.us.archive.org/2/items/europe_202101/IPTVWORLDDEN10.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='IPTV WORLD', cmdlist=cmdlist, finishedCallback=None)
                        elif returnValue =="com_01043":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia601505.us.archive.org/2/items/europe_202101/IPTVWORLDDEN20.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='IPTV WORLD', cmdlist=cmdlist, finishedCallback=None)
                        elif returnValue =="com_01044":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia601505.us.archive.org/2/items/europe_202101/IPTVWORLDDEN50.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='IPTV WORLD', cmdlist=cmdlist, finishedCallback=None)
                        elif returnValue =="com_01045":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia601505.us.archive.org/2/items/europe_202101/IPTVWORLDDEN100.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='IPTV WORLD', cmdlist=cmdlist, finishedCallback=None)
                        elif returnValue =="com_1042":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia601505.us.archive.org/2/items/europe_202101/IPTVWORLDDE001.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='IPTV WORLD', cmdlist=cmdlist, finishedCallback=None)
                        elif returnValue =="com_1043":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia601505.us.archive.org/2/items/europe_202101/IPTVWORLDDE002.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='IPTV WORLD', cmdlist=cmdlist, finishedCallback=None)
                        elif returnValue =="com_1044":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia601505.us.archive.org/2/items/europe_202101/IPTVWORLDDE003.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='IPTV WORLD', cmdlist=cmdlist, finishedCallback=None)
                        elif returnValue =="com_1045":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia601505.us.archive.org/2/items/europe_202101/IPTVWORLDDE004.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='IPTV WORLD', cmdlist=cmdlist, finishedCallback=None)
                        elif returnValue =="com_1046":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia601505.us.archive.org/2/items/europe_202101/IPTVWORLDDE005.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='IPTV WORLD', cmdlist=cmdlist, finishedCallback=None)
                        elif returnValue =="com_1047":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'") 
                                cmdlist.append("%s https://ia601505.us.archive.org/2/items/europe_202101/IPTVWORLDDE006.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='IPTV WORLD', cmdlist=cmdlist, finishedCallback=None)
                        elif returnValue =="com_1048":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia601505.us.archive.org/2/items/europe_202101/IPTVWORLDDE007.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='IPTV WORLD', cmdlist=cmdlist, finishedCallback=None)
                        elif returnValue =="com_1049":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia601505.us.archive.org/2/items/europe_202101/IPTVWORLDDE008.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='IPTV WORLD', cmdlist=cmdlist, finishedCallback=None)
                        elif returnValue =="com_1050":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia601505.us.archive.org/2/items/europe_202101/IPTVWORLDDE009.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='IPTV WORLD', cmdlist=cmdlist, finishedCallback=None)
                        elif returnValue =="com_1051":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")    
                                cmdlist.append("%s https://ia601505.us.archive.org/2/items/europe_202101/IPTVWORLDDE010.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='IPTV WORLD', cmdlist=cmdlist, finishedCallback=None)
                        elif returnValue =="com_1052":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia601505.us.archive.org/2/items/europe_202101/IPTVWORLDDE011.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='IPTV WORLD', cmdlist=cmdlist, finishedCallback=None)
                        elif returnValue =="com_1053":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia601505.us.archive.org/2/items/europe_202101/IPTVWORLDDE012.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='IPTV WORLD', cmdlist=cmdlist, finishedCallback=None)
                        elif returnValue =="com_1054":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia601505.us.archive.org/2/items/europe_202101/IPTVWORLDDE013.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='IPTV WORLD', cmdlist=cmdlist, finishedCallback=None)
                        elif returnValue =="com_1055":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia601505.us.archive.org/2/items/europe_202101/IPTVWORLDDE014.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='IPTV WORLD', cmdlist=cmdlist, finishedCallback=None)
                        elif returnValue =="com_1056":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia601505.us.archive.org/2/items/europe_202101/IPTVWORLDDE015.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='IPTV WORLD', cmdlist=cmdlist, finishedCallback=None)
                        elif returnValue =="com_1057":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia601505.us.archive.org/2/items/europe_202101/IPTVWORLDDE016.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='IPTV WORLD', cmdlist=cmdlist, finishedCallback=None)
                        elif returnValue =="com_1058":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia601505.us.archive.org/2/items/europe_202101/IPTVWORLDDE017.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='IPTV WORLD', cmdlist=cmdlist, finishedCallback=None)
                        elif returnValue =="com_1059":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia601505.us.archive.org/2/items/europe_202101/IPTVWORLDDE018.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='IPTV WORLD', cmdlist=cmdlist, finishedCallback=None)
                        elif returnValue =="com_1060":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia601505.us.archive.org/2/items/europe_202101/IPTVWORLDDE019.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='IPTV WORLD', cmdlist=cmdlist, finishedCallback=None)
                        elif returnValue =="com_1061":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia601505.us.archive.org/2/items/europe_202101/IPTVWORLDDE020.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='IPTV WORLD', cmdlist=cmdlist, finishedCallback=None)
                        elif returnValue =="com_1062":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia601505.us.archive.org/2/items/europe_202101/IPTVWORLDDE021.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='IPTV WORLD', cmdlist=cmdlist, finishedCallback=None)
                        elif returnValue =="com_1063":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia601505.us.archive.org/2/items/europe_202101/IPTVWORLDDE022.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='IPTV WORLD', cmdlist=cmdlist, finishedCallback=None)
                        elif returnValue =="com_1064":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia601505.us.archive.org/2/items/europe_202101/IPTVWORLDDE023.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='IPTV USA', cmdlist=cmdlist, finishedCallback=None)
                        elif returnValue =="com_1065":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia601505.us.archive.org/2/items/europe_202101/IPTVWORLDDE024.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='IPTV USA', cmdlist=cmdlist, finishedCallback=None)
                        elif returnValue =="com_1066":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia601505.us.archive.org/2/items/europe_202101/IPTVWORLDDE025.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='IPTV USA', cmdlist=cmdlist, finishedCallback=None)
                        elif returnValue =="com_1067":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'") 
                                cmdlist.append("%s https://ia601505.us.archive.org/2/items/europe_202101/IPTVWORLDDE026.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='IPTV USA', cmdlist=cmdlist, finishedCallback=None)
                        elif returnValue =="com_1068":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia601505.us.archive.org/2/items/europe_202101/IPTVWORLDDE027.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='IPTV USA', cmdlist=cmdlist, finishedCallback=None)
                        elif returnValue =="com_1069":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia601505.us.archive.org/2/items/europe_202101/IPTVWORLDDE028.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='IPTV USA', cmdlist=cmdlist, finishedCallback=None)
                        elif returnValue =="com_1070":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia601505.us.archive.org/2/items/europe_202101/IPTVWORLDDE029.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='IPTV USA', cmdlist=cmdlist, finishedCallback=None)
                        elif returnValue =="com_1071":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")    
                                cmdlist.append("%s https://ia601505.us.archive.org/2/items/europe_202101/IPTVWORLDDE030.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='IPTV USA', cmdlist=cmdlist, finishedCallback=None)
                        elif returnValue =="com_1072":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia601505.us.archive.org/2/items/europe_202101/IPTVWORLDDE031.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='IPTV USA', cmdlist=cmdlist, finishedCallback=None)
                        elif returnValue =="com_1073":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia601505.us.archive.org/2/items/europe_202101/IPTVWORLDDE032.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='IPTV USA', cmdlist=cmdlist, finishedCallback=None)
                        elif returnValue =="com_1074":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia601505.us.archive.org/2/items/europe_202101/IPTVWORLDDE033.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='IPTV WORLD', cmdlist=cmdlist, finishedCallback=None)
                        elif returnValue =="com_1075":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia601505.us.archive.org/2/items/europe_202101/IPTVWORLDDE034.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='IPTV WORLD', cmdlist=cmdlist, finishedCallback=None)
                        elif returnValue =="com_1076":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia601505.us.archive.org/2/items/europe_202101/IPTVWORLDDE035.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='IPTV WORLD', cmdlist=cmdlist, finishedCallback=None)
                        elif returnValue =="com_1077":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia601505.us.archive.org/2/items/europe_202101/IPTVWORLDDE036.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='IPTV WORLD', cmdlist=cmdlist, finishedCallback=None)
                        elif returnValue =="com_1078":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia601505.us.archive.org/2/items/europe_202101/IPTVWORLDDE037.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='IPTV WORLD', cmdlist=cmdlist, finishedCallback=None)
                        elif returnValue =="com_1079":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia601505.us.archive.org/2/items/europe_202101/IPTVWORLDDE038.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='IPTV WORLD', cmdlist=cmdlist, finishedCallback=None)
                        elif returnValue =="com_1080":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia601505.us.archive.org/2/items/europe_202101/IPTVWORLDDE039.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='IPTV WORLD', cmdlist=cmdlist, finishedCallback=None)
                        elif returnValue =="com_1081":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia601505.us.archive.org/2/items/europe_202101/IPTVWORLDDE040.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='IPTV WORLD', cmdlist=cmdlist, finishedCallback=None)
                        elif returnValue =="com_1082":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia601505.us.archive.org/2/items/europe_202101/IPTVWORLDDE041.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='IPTV WORLD', cmdlist=cmdlist, finishedCallback=None)
                        elif returnValue =="com_1083":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia601505.us.archive.org/2/items/europe_202101/IPTVWORLDDE042.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='IPTV WORLD', cmdlist=cmdlist, finishedCallback=None)
                        elif returnValue =="com_1084":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia601505.us.archive.org/2/items/europe_202101/IPTVWORLDDE043.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='IPTV WORLD', cmdlist=cmdlist, finishedCallback=None)
                        elif returnValue =="com_1085":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia601505.us.archive.org/2/items/europe_202101/IPTVWORLDDE044.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='IPTV WORLD', cmdlist=cmdlist, finishedCallback=None)
                        elif returnValue =="com_1086":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'") 
                                cmdlist.append("%s https://ia601505.us.archive.org/2/items/europe_202101/IPTVWORLDDE045.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='IPTV WORLD', cmdlist=cmdlist, finishedCallback=None)
                        elif returnValue =="com_1087":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia601505.us.archive.org/2/items/europe_202101/IPTVWORLDDE046.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='IPTV WORLD', cmdlist=cmdlist, finishedCallback=None)
                        elif returnValue =="com_1088":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia601505.us.archive.org/2/items/europe_202101/IPTVWORLDDE047.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='IPTV WORLD', cmdlist=cmdlist, finishedCallback=None)
                        elif returnValue =="com_1089":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia601505.us.archive.org/2/items/europe_202101/IPTVWORLDDE048.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='IPTV WORLD', cmdlist=cmdlist, finishedCallback=None)
                        elif returnValue =="com_1090":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")    
                                cmdlist.append("%s https://ia601505.us.archive.org/2/items/europe_202101/IPTVWORLDDE049.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='IPTV WORLD', cmdlist=cmdlist, finishedCallback=None)
                        elif returnValue =="com_1091":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia601505.us.archive.org/2/items/europe_202101/IPTVWORLDDE050.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='IPTV WORLD', cmdlist=cmdlist, finishedCallback=None)
                        elif returnValue =="com_01092":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia601505.us.archive.org/2/items/europe_202101/IPTVWORLDBRN10.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='IPTV WORLD', cmdlist=cmdlist, finishedCallback=None)
                        elif returnValue =="com_01093":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia601505.us.archive.org/2/items/europe_202101/IPTVWORLDBRN20.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='IPTV WORLD', cmdlist=cmdlist, finishedCallback=None)
                        elif returnValue =="com_01094":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia601505.us.archive.org/2/items/europe_202101/IPTVWORLDBRN50.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='IPTV WORLD', cmdlist=cmdlist, finishedCallback=None)
                        elif returnValue =="com_01095":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia601505.us.archive.org/2/items/europe_202101/IPTVWORLDBRN100.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='IPTV WORLD', cmdlist=cmdlist, finishedCallback=None)
                        elif returnValue =="com_1092":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia601505.us.archive.org/2/items/europe_202101/IPTVWORLDBR001.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='IPTV WORLD', cmdlist=cmdlist, finishedCallback=None)
                        elif returnValue =="com_1093":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia601505.us.archive.org/2/items/europe_202101/IPTVWORLDBR002.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='IPTV WORLD', cmdlist=cmdlist, finishedCallback=None)
                        elif returnValue =="com_1094":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia601505.us.archive.org/2/items/europe_202101/IPTVWORLDBR003.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='IPTV WORLD', cmdlist=cmdlist, finishedCallback=None)
                        elif returnValue =="com_1095":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia601505.us.archive.org/2/items/europe_202101/IPTVWORLDBR004.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='IPTV WORLD', cmdlist=cmdlist, finishedCallback=None)
                        elif returnValue =="com_1096":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia601505.us.archive.org/2/items/europe_202101/IPTVWORLDBR005.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='IPTV WORLD', cmdlist=cmdlist, finishedCallback=None)
                        elif returnValue =="com_1097":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia601505.us.archive.org/2/items/europe_202101/IPTVWORLDBR006.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='IPTV WORLD', cmdlist=cmdlist, finishedCallback=None)
                        elif returnValue =="com_1098":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia601505.us.archive.org/2/items/europe_202101/IPTVWORLDBR007.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='IPTV WORLD', cmdlist=cmdlist, finishedCallback=None)
                        elif returnValue =="com_1099":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia601505.us.archive.org/2/items/europe_202101/IPTVWORLDBR008.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='IPTV WORLD', cmdlist=cmdlist, finishedCallback=None)
                        elif returnValue =="com_1100":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia601505.us.archive.org/2/items/europe_202101/IPTVWORLDBR009.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='IPTV WORLD', cmdlist=cmdlist, finishedCallback=None)
                        elif returnValue =="com_1101":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia601505.us.archive.org/2/items/europe_202101/IPTVWORLDBR010.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='IPTV WORLD', cmdlist=cmdlist, finishedCallback=None)
                        elif returnValue =="com_1102":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia601505.us.archive.org/2/items/europe_202101/IPTVWORLDBR011.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='IPTV WORLD', cmdlist=cmdlist, finishedCallback=None)
                        elif returnValue =="com_1103":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia601505.us.archive.org/2/items/europe_202101/IPTVWORLDBR012.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='IPTV USA', cmdlist=cmdlist, finishedCallback=None)
                        elif returnValue =="com_1104":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia601505.us.archive.org/2/items/europe_202101/IPTVWORLDBR013.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='IPTV USA', cmdlist=cmdlist, finishedCallback=None)
                        elif returnValue =="com_1105":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia601505.us.archive.org/2/items/europe_202101/IPTVWORLDBR014.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='IPTV USA', cmdlist=cmdlist, finishedCallback=None)
                        elif returnValue =="com_1106":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'") 
                                cmdlist.append("%s https://ia601505.us.archive.org/2/items/europe_202101/IPTVWORLDBR015.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='IPTV USA', cmdlist=cmdlist, finishedCallback=None)
                        elif returnValue =="com_1107":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia601505.us.archive.org/2/items/europe_202101/IPTVWORLDBR016.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='IPTV USA', cmdlist=cmdlist, finishedCallback=None)
                        elif returnValue =="com_1108":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia601505.us.archive.org/2/items/europe_202101/IPTVWORLDBR017.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='IPTV USA', cmdlist=cmdlist, finishedCallback=None)
                        elif returnValue =="com_1109":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia601505.us.archive.org/2/items/europe_202101/IPTVWORLDBR018.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='IPTV USA', cmdlist=cmdlist, finishedCallback=None)
                        elif returnValue =="com_1110":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")    
                                cmdlist.append("%s https://ia601505.us.archive.org/2/items/europe_202101/IPTVWORLDBR019.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='IPTV USA', cmdlist=cmdlist, finishedCallback=None)
                        elif returnValue =="com_1111":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia601505.us.archive.org/2/items/europe_202101/IPTVWORLDBR020.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='IPTV USA', cmdlist=cmdlist, finishedCallback=None)
                        elif returnValue =="com_1112":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia601505.us.archive.org/2/items/europe_202101/IPTVWORLDBR021.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='IPTV USA', cmdlist=cmdlist, finishedCallback=None)
                        elif returnValue =="com_1113":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia601505.us.archive.org/2/items/europe_202101/IPTVWORLDBR022.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='IPTV WORLD', cmdlist=cmdlist, finishedCallback=None)
                        elif returnValue =="com_1114":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia601505.us.archive.org/2/items/europe_202101/IPTVWORLDBR023.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='IPTV WORLD', cmdlist=cmdlist, finishedCallback=None)
                        elif returnValue =="com_1115":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia601505.us.archive.org/2/items/europe_202101/IPTVWORLDBR024.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='IPTV WORLD', cmdlist=cmdlist, finishedCallback=None)
                        elif returnValue =="com_1116":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia601505.us.archive.org/2/items/europe_202101/IPTVWORLDBR025.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='IPTV WORLD', cmdlist=cmdlist, finishedCallback=None)
                        elif returnValue =="com_1117":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia601505.us.archive.org/2/items/europe_202101/IPTVWORLDBR026.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='IPTV WORLD', cmdlist=cmdlist, finishedCallback=None)
                        elif returnValue =="com_1118":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia601505.us.archive.org/2/items/europe_202101/IPTVWORLDBR027.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='IPTV WORLD', cmdlist=cmdlist, finishedCallback=None)
                        elif returnValue =="com_1119":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'") 
                                cmdlist.append("%s https://ia601505.us.archive.org/2/items/europe_202101/IPTVWORLDBR028.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='IPTV WORLD', cmdlist=cmdlist, finishedCallback=None)
                        elif returnValue =="com_1120":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia601505.us.archive.org/2/items/europe_202101/IPTVWORLDBR029.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='IPTV WORLD', cmdlist=cmdlist, finishedCallback=None)
                        elif returnValue =="com_1121":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia601505.us.archive.org/2/items/europe_202101/IPTVWORLDBR030.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='IPTV WORLD', cmdlist=cmdlist, finishedCallback=None)
                        elif returnValue =="com_1122":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia601505.us.archive.org/2/items/europe_202101/IPTVWORLDBR031.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='IPTV WORLD', cmdlist=cmdlist, finishedCallback=None)
                        elif returnValue =="com_1123":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")    
                                cmdlist.append("%s https://ia601505.us.archive.org/2/items/europe_202101/IPTVWORLDBR032.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='IPTV WORLD', cmdlist=cmdlist, finishedCallback=None)
                        elif returnValue =="com_1124":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia601505.us.archive.org/2/items/europe_202101/IPTVWORLDBR033.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='IPTV WORLD', cmdlist=cmdlist, finishedCallback=None)
                        elif returnValue =="com_1125":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia601505.us.archive.org/2/items/europe_202101/IPTVWORLDBR034.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='IPTV WORLD', cmdlist=cmdlist, finishedCallback=None)
                        elif returnValue =="com_1126":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia601505.us.archive.org/2/items/europe_202101/IPTVWORLDBR035.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='IPTV WORLD', cmdlist=cmdlist, finishedCallback=None)
                        elif returnValue =="com_1127":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia601505.us.archive.org/2/items/europe_202101/IPTVWORLDBR036.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='IPTV WORLD', cmdlist=cmdlist, finishedCallback=None)
                        elif returnValue =="com_1128":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia601505.us.archive.org/2/items/europe_202101/IPTVWORLDBR037.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='IPTV WORLD', cmdlist=cmdlist, finishedCallback=None)
                        elif returnValue =="com_1129":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia601505.us.archive.org/2/items/europe_202101/IPTVWORLDBR038.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='IPTV WORLD', cmdlist=cmdlist, finishedCallback=None)
                        elif returnValue =="com_1130":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia601505.us.archive.org/2/items/europe_202101/IPTVWORLDBR039.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='IPTV WORLD', cmdlist=cmdlist, finishedCallback=None)
                        elif returnValue =="com_1131":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia601505.us.archive.org/2/items/europe_202101/IPTVWORLDBR040.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='IPTV WORLD', cmdlist=cmdlist, finishedCallback=None)
                        elif returnValue =="com_1132":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia601505.us.archive.org/2/items/europe_202101/IPTVWORLDBR041.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='IPTV WORLD', cmdlist=cmdlist, finishedCallback=None)
                        elif returnValue =="com_1133":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia601505.us.archive.org/2/items/europe_202101/IPTVWORLDBR042.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='IPTV WORLD', cmdlist=cmdlist, finishedCallback=None)
                        elif returnValue =="com_1134":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia601505.us.archive.org/2/items/europe_202101/IPTVWORLDBR043.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='IPTV WORLD', cmdlist=cmdlist, finishedCallback=None)
                        elif returnValue =="com_1135":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia601505.us.archive.org/2/items/europe_202101/IPTVWORLDBR044.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='IPTV WORLD', cmdlist=cmdlist, finishedCallback=None)
                        elif returnValue =="com_1136":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia601505.us.archive.org/2/items/europe_202101/IPTVWORLDBR045.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='IPTV USA', cmdlist=cmdlist, finishedCallback=None)
                        elif returnValue =="com_1137":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia601505.us.archive.org/2/items/europe_202101/IPTVWORLDBR046.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='IPTV USA', cmdlist=cmdlist, finishedCallback=None)
                        elif returnValue =="com_1138":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia601505.us.archive.org/2/items/europe_202101/IPTVWORLDBR047.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='IPTV USA', cmdlist=cmdlist, finishedCallback=None)
                        elif returnValue =="com_1139":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'") 
                                cmdlist.append("%s https://ia601505.us.archive.org/2/items/europe_202101/IPTVWORLDBR048.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='IPTV USA', cmdlist=cmdlist, finishedCallback=None)
                        elif returnValue =="com_1140":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia601505.us.archive.org/2/items/europe_202101/IPTVWORLDBR049.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='IPTV USA', cmdlist=cmdlist, finishedCallback=None)
                        elif returnValue =="com_1141":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia601505.us.archive.org/2/items/europe_202101/IPTVWORLDBR050.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='IPTV USA', cmdlist=cmdlist, finishedCallback=None)
                        elif returnValue =="com_1142":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia601505.us.archive.org/2/items/europe_202101/IPTVWORLDBR050.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='IPTV USA', cmdlist=cmdlist, finishedCallback=None)
                        elif returnValue =="com_1143":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")    
                                cmdlist.append("%s https://ia801409.us.archive.org/29/items/iptvworld_201911/IPTVWORLDAS058.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='IPTV USA', cmdlist=cmdlist, finishedCallback=None)
                        elif returnValue =="com_1144":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia801409.us.archive.org/29/items/iptvworld_201911/IPTVWORLDAS059.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='IPTV USA', cmdlist=cmdlist, finishedCallback=None)
                        elif returnValue =="com_1145":
                                cmdlist = []
                                cmdlist.append("%s -qO - '" % self.wget + "'")
                                cmdlist.append("%s https://ia801409.us.archive.org/29/items/iptvworld_201911/IPTVWORLDAS060.sh -qO - | /bin/sh" % self.wget)
                                self.session.open(Console3, title='IPTV USA', cmdlist=cmdlist, finishedCallback=None)






                        else:
                                print("\n[MyShPrombt] cancel\n")
                                self.close(None)

        def Update(self):
            Update = "afile"
            afile = open('/tmp/monfichier.txt', 'w')
            self.session.openWithCallback(self.restartenigma, MessageBox, _('Free Server V_' + str(Update) + '\nRestart Enigma2 To Load New Settings?'), MessageBox.TYPE_YESNO)

        def RMCHD1(self):
            from Screens.InfoBar import MoviePlayer, InfoBar        
            #url01="http://iptvpro.premium-itv.com:8789/live/31031986/31031986/32718.m3u8"  
            #url01="http://skdn.redi-vo.com/iptv/ch255?code=103131497823984&key=43852"           
            #url01="http://live.redfhd.com:8000/live/cemal/sakarya54/1729.m3u8" 
            url01="http://vvn.neoredi.com/iptv/ch255?code=1501309316704233&key=23296"
            #url01="http://95.154.194.14:8000/live/3E3tfSepRV/CHoDruHskE/33365.m3u8" 
            #url01="http://www.sansat.net:25461/bRRMEeD4n5/7F09Vz4zRp/49213" 
            #url01="http://iptvoffshore.com:80/2806892/8940691/10527" 
            #url01="http://senadi.mine.nu:8000/live/O5ckVk7U1C/K91jSvYCeA/1216.ts"
            #url01="http://linux-app.tv:6204/live/mustafa96/mustafa96/14046.m3u8"            
            #url01="http://iptv9211.hopto.me:8000/live/DlrSUqOZ2k/lFcKAenHiB/33365.m3u8" 
            #url01="http://topiptv.net:5890/live/1234567/12345/601.m3u8"
            #url01="http://showflix.org:5890/live/1234567/12345/601.m3u8"
            #url01="http://topiptv.net:5890/live/1234567/12345/601.m3u8"  
            ref = eServiceReference(4097, 0, url01)
            ref.setName(Name_001)
            self.session.open(MoviePlayer, ref)
        def RMCHD2(self):
            from Screens.InfoBar import MoviePlayer, InfoBar
            #url02="http://senadi.mine.nu:8000/live/O5ckVk7U1C/K91jSvYCeA/1264.ts"  
            #url01="http://skdn.redi-vo.com/iptv/ch253?code=103131497823984&key=43971"
            #url02="http://iptvoffshore.com:80/2806892/8940691/341"
            #url02="http://live.redfhd.com:8000/live/cemal/sakarya54/1728.m3u8"
            url02="http://vvn.neoredi.com/iptv/ch253?code=1501309316704233&key=54264"
            #url02="http://iptv-luxe.com:8789/live/1212/1212/29823.m3u8"
            #url02="http://iptv-luxe.com:8789/live/1212/1212/29823.m3u8"
            #url02="http://95.154.194.14:8000/live/3E3tfSepRV/CHoDruHskE/33364.m3u8"
            #url02="http://iptvpro.premium-itv.com:8789/live/31031986/31031986/32714.m3u8"
            #url02="http://iptvpro.premium-tv.media:8789/live/francesdclark/MJ5jwjknJA/39502.m3u8"
            #url02="http://tv2iptv.com:8000/live/Faysal/faysal123/30614.m3u8"
            #url02="http://tv.sigma-net.co:6500/live/q7iDM0wsgh/42xjrPv0tB/26130.m3u8"      
            #url02="http://linux-app.tv:6204/live/mustafa96/mustafa96/14045.m3u8"
            #url02="http://topiptv.net:5890/live/1234567/12345/603.m3u8"
            ref = eServiceReference(4097, 0, url02)
            ref.setName(Name_002)
            self.session.open(MoviePlayer, ref)  
        def RMCHD3(self):
            from Screens.InfoBar import MoviePlayer, InfoBar 
            #url03="http://iptv9211.hopto.me:8000/live/DlrSUqOZ2k/lFcKAenHiB/33363.m3u8"
            #url03="http://skdn.redi-vo.com/iptv/ch254?code=103131497823984&key=13496"
            #url03="http://iptv7.premium-stv.com:25461/rmcsport3/1557539943/58"
            #url03="http://iptvpro.premium-tv.media:8789/live/francesdclark/MJ5jwjknJA/39501.m3u8"
            #url03="http://iptv-luxe.com:8789/live/1212/1212/29824.m3u8"
            #url03="http://95.154.194.14:8000/live/3E3tfSepRV/CHoDruHskE/33363.m3u8"
            #url03="http://iptv-luxe.com:8789/live/1212/1212/29824.m3u8"
            #url03="http://linux-app.tv:6204/live/mustafa96/mustafa96/14044.m3u8"
            #url03="http://showflix.org:5890/live/1234567/12345/605.m3u8"            
            #url03="http://live.redfhd.com:8000/live/cemal/sakarya54/1739.m3u8"     
            url03="http://vvn.neoredi.com/iptv/ch253?code=1501309316704233&key=31480"       
            ref = eServiceReference(4097, 0, url03)
            ref.setName(Name_003)
            self.session.open(MoviePlayer, ref)
        def RMCHD4(self):
            from Screens.InfoBar import MoviePlayer, InfoBar
            #url04="http://linux-app.tv:6204/live/mustafa96/mustafa96/14043.m3u8" 
            #url04="http://www.sansat.net:25461/zbuyen95/JZ1jh5CJV5/42338"
            #url04="http://iptv-luxe.com:8789/live/1212/1212/29825.m3u8"
            #url04="http://senadi.mine.nu:8000/live/O5ckVk7U1C/K91jSvYCeA/1270.ts"
            #url04="http://showflix.org:5890/live/1234567/12345/607.m3u8"
            #url04="http://iptv-luxe.com:8789/live/1212/1212/16099.m3u8"
            #url04="http://live.redfhd.com:8000/live/cemal/sakarya54/38798.m3u8"
            #url04="http://skdn.redi-vo.com/iptv/ch243?code=103131497823984&key=62334"
            #url04="http://iptv6.premium-stv.com:25461/sourcefrhevcpro1/0493432475/3312"
            #url04="http://mytvonline.nl:80/live/2YQyltguql/XwEAnAWfE0/27343.m3u8"
            #url04="http://topiptv.net:5890/live/1234567/12345/607.m3u8" 
            url04="http://vvn.neoredi.com/iptv/ch243?code=1501309316704233&key=15110"  
            ref = eServiceReference(4097, 0, url04)
            ref.setName(Name_004)
            self.session.open(MoviePlayer, ref)   
        def BeinFRHD1(self):
            from Screens.InfoBar import MoviePlayer, InfoBar
            #url05="http://senadi.mine.nu:8000/live/O5ckVk7U1C/K91jSvYCeA/1287.ts"          
            #url05="http://showflix.org:5890/live/1234567/12345/58334.m3u8"            
            #url05="http://iptv-luxe.com:8789/live/1212/1212/10531.m3u8"
            url05="http://skdn.redi-vo.com/iptv/ch119?code=138137164006399&key=56827"
            #url05="http://s1.niacam.net:24621/mtg_2406_1/IyBf86mT158!1/397"        
            #url05="http://live.redfhd.com:8000/live/cemal/sakarya54/115.m3u8" 
            #url05="http://skdn.redi-vo.com/iptv/ch119?code=103131497823984&key=62807"
            #url05="http://nvkdn.redi-vo.com/iptv/ch119?code=1701273726237058&key=50356"
            #url05="http://iptv6.premium-stv.com:25461/pro1turc/bhXdd32sd1g/1459"           
            #url05="http://iptvpro.premium-tv.media:8789/live/francesdclark/MJ5jwjknJA/39499.m3u8"          
            #url05="http://senadi.mine.nu:8000/live/O5ckVk7U1C/K91jSvYCeA/1287.ts"          
            #url05="http://linux-app.tv:6204/live/mustafa96/mustafa96/28371.m3u8"
            #url05="http://iptv-luxe.com:8789/live/1212/1212/29819.m3u8"
            #url05="http://iptv-luxe.com:8789/live/1212/1212/29819.m3u8"
            ref = eServiceReference(4097, 0, url05)
            ref.setName(Name_1)
            self.session.open(MoviePlayer, ref)
        def BeinFRHD2(self):
            from Screens.InfoBar import MoviePlayer, InfoBar
            #url06="http://senadi.mine.nu:8000/live/O5ckVk7U1C/K91jSvYCeA/1288.ts"       
            #url06="http://iptv-luxe.com:8789/live/1212/1212/29820.m3u8"
            #url06="http://iptv6.premium-stv.com:25461/pro1turc/bhXdd32sd1g/1458"
            #url06="http://iptv9211.hopto.me:8000/live/DlrSUqOZ2k/lFcKAenHiB/33380.m3u8"
            url06="http://vvn.neoredi.com/iptv/ch120?code=1501309316704233&key=51185"   
            #url06="http://live.redfhd.com:8000/live/cemal/sakarya54/114.m3u8"    
            #url06="http://skdn.redi-vo.com/iptv/ch120?code=103131497823984&key=38010"
            #url06="http://nvkdn.redi-vo.com/iptv/ch120?code=1701273726237058&key=51185"
            #url06="http://www.sansat.net:25461/bRRMEeD4n5/7F09Vz4zRp/49230"
            #url06="http://linux-app.tv:6204/live/mustafa96/mustafa96/28372.m3u8"
            #url06="http://iptv-luxe.com:8789/live/1212/1212/29820.m3u8"
            #url06="http://showflix.org:5890/live/1234567/12345/588.m3u8"   
            #url06="http://iptv-luxe.com:8789/live/1212/1212/10530.m3u8"            
            ref = eServiceReference(4097, 0, url06)
            ref.setName(Name_2)
            self.session.open(MoviePlayer, ref) 
        def BeinFRHD3(self):
            from Screens.InfoBar import MoviePlayer, InfoBar
            #url07="http://skdn.redi-vo.com/iptv/ch206?code=103131497823984&key=26341"   
            #url07="http://iptv6.premium-stv.com:25461/pro1turc/bhXdd32sd1g/1457"
            #url07="http://nvkdn.redi-vo.com/iptv/ch120?code=1701273726237058&key=11755"
            url07="http://vvn.neoredi.com/iptv/ch120?code=1501309316704233&key=11755"
            #url07="http://mytvonline.nl:80/live/2YQyltguql/XwEAnAWfE0/27340.m3u8"
            #url07="http://iptvpro.premium-tv.media:8789/live/francesdclark/MJ5jwjknJA/39497.m3u8"
            #url07="http://www.sansat.net:25461/bRRMEeD4n5/7F09Vz4zRp/49231"
            #url07="http://95.154.194.14:8000/live/3E3tfSepRV/CHoDruHskE/33379.m3u8"
            #url07="http://linux-app.tv:6204/live/mustafa96/mustafa96/28373.m3u8"
            #url07="http://iptv-luxe.com:8789/live/1212/1212/29821.m3u8"
            #url07="http://showflix.org:5890/live/1234567/12345/590.m3u8"   
            #url07="http://iptv-luxe.com:8789/live/1212/1212/10529.m3u8"            
            ref = eServiceReference(4097, 0, url07)
            ref.setName(Name_3)
            self.session.open(MoviePlayer, ref)
        def BeinHD1(self):
            from Screens.InfoBar import MoviePlayer, InfoBar
            url1="http://showflix.org:5890/Mohamed/1234567/16"      
            #url1="http://95.170.215.101:80/hls/m3u8/Bein-S1-a58.m3u8"
            #url1="http://dreamtv.v90.co:2095/KASS0102/n4FhD5Id8E/52"
            #url1="http://skdn.redi-vo.com/iptv/ch111?code=103131497823984&key=54576"
            #url1="http://iptvpro.vision-new.org:8789/1212/1212/10517"
            #url1="http://95.154.194.84:8000/live/DlrSUqOZ2k/lFcKAenHiB/32098.m3u8"
            #url1="http://mu02.v2iptv.com:8880/HJLM1399/gOQedvLAFg/2140"
            ref = eServiceReference(4097, 0, url1)
            ref.setName(Name_01)
            self.session.open(MoviePlayer, ref)
        def BeinHD2(self):
            from Screens.InfoBar import MoviePlayer, InfoBar
            #url2="http://iptvpro.vision-new.org:8789/1212/1212/10516"      
            url2="http://showflix.org:5890/Mohamed/1234567/17"
            #url2="http://iptv9211.hopto.me:8000/live/nfzNlANvf2/HHfWU3dzWt/32097.m3u8"
            #url2="http://skdn.redi-vo.com/iptv/ch112?code=103131497823984&key=46098"
            #url2="http://iptv9211.hopto.me:8000/nfzNlANvf2/HHfWU3dzWt/32097"
            #url2="http://95.154.194.84:8000/live/DlrSUqOZ2k/lFcKAenHiB/32097.m3u8"
            #url2="http://mu02.v2iptv.com:8880/HJLM1399/gOQedvLAFg/2139"            
            ref = eServiceReference(4097, 0, url2)
            ref.setName(Name_02)
            self.session.open(MoviePlayer, ref)
        def BeinHD3(self):
            from Screens.InfoBar import MoviePlayer, InfoBar
            url3="http://showflix.org:5890/Mohamed/1234567/18"
            #url3="http://skdn.redi-vo.com/iptv/ch113?code=103131497823984&key=39255"
            #url3="http://mu02.v2iptv.com:8880/HJLM1399/gOQedvLAFg/2138"
            #url3="http://iptv9211.hopto.me:8000/live/nfzNlANvf2/HHfWU3dzWt/32096.m3u8" 
            #url3="http://mu02.v2iptv.com:8880/HJLM1399/gOQedvLAFg/2137"   
            ref = eServiceReference(4097, 0, url3)
            ref.setName(Name_03)
            self.session.open(MoviePlayer, ref) 
        def BeinHD4(self):
            from Screens.InfoBar import MoviePlayer, InfoBar
            url4="http://showflix.org:5890/Mohamed/1234567/19"
            #url4="http://skdn.redi-vo.com/iptv/ch114?code=103131497823984&key=46165"
            #url4="http://premiumplustv.com:8000/live/user938303/G26ZM4L1gY/81759.m3u8"
            #url4="http://tv2iptv.com:8000/live/Faysal/faysal123/32.m3u8"
            #url4="http://iptv9211.hopto.me:8000/live/nfzNlANvf2/HHfWU3dzWt/32095.m3u8"
            #url4="http://iptv-luxe.com:8789/1212/1212/11176"
            #url4="http://iptvpro.vision-new.org:8789/1212/1212/11178"      
            ref = eServiceReference(4097, 0, url4)
            ref.setName(Name_04)
            self.session.open(MoviePlayer, ref)
        def BeinHD5(self):
            from Screens.InfoBar import MoviePlayer, InfoBar
            url5="http://showflix.org:5890/Mohamed/1234567/20"
            #url5="http://skdn.redi-vo.com/iptv/ch115?code=103131497823984&key=45992"
            #url5="http://xtiptv.xyz:25461/live/PYGj0mbvYI/4fceOZuE1c/55899.ts"
            #url5="http://95.154.194.84:8000/live/DlrSUqOZ2k/lFcKAenHiB/32094.m3u8"
            #url5="http://iptv9211.hopto.me:8000/live/nfzNlANvf2/HHfWU3dzWt/32094.m3u8"
            #url5="http://mu02.v2iptv.com:8880/HJLM1399/gOQedvLAFg/2136"         
            #url5="http://iptvpro.vision-new.org:8789/1212/1212/11176"  
            ref = eServiceReference(4097, 0, url5)
            ref.setName(Name_05)
            self.session.open(MoviePlayer, ref)
        def BeinHD6(self):
            from Screens.InfoBar import MoviePlayer, InfoBar
            url6="http://showflix.org:5890/Mohamed/1234567/21"
            #url6="http://skdn.redi-vo.com/iptv/ch116?code=103131497823984&key=57392"
            #url6="http://mu02.v2iptv.com:8880/HJLM1399/gOQedvLAFg/2135"
            #url6="http://iptv9211.hopto.me:8000/live/nfzNlANvf2/HHfWU3dzWt/32093.m3u8"
            #url6="http://iptv-luxe.com:8789/1212/1212/11172"
            #url6="http://iptvpro.vision-new.org:8789/1212/1212/11174"      
            ref = eServiceReference(4097, 0, url6)
            ref.setName(Name_06)
            self.session.open(MoviePlayer, ref)
        def BeinHD7(self):
            from Screens.InfoBar import MoviePlayer, InfoBar
            #url7="http://mu02.v2iptv.com:8880/HJLM1399/gOQedvLAFg/2134"
            url7="http://showflix.org:5890/Mohamed/1234567/22"
            #url7="http://skdn.redi-vo.com/iptv/ch117?code=103131497823984&key=58844"
            #url7="http://beryantv.com:25461/02410251710104/02410251710104/824"
            #url7="http://iptv-luxe.com:8789/1212/1212/11170"
            #url7="http://iptv9211.hopto.me:8000/live/nfzNlANvf2/HHfWU3dzWt/32092.m3u8"  
            #url7="http://iptvpro.vision-new.org:8789/1212/1212/11172" 
            ref = eServiceReference(4097, 0, url7)
            ref.setName(Name_07)
            self.session.open(MoviePlayer, ref)
        def BeinHD8(self):
            from Screens.InfoBar import MoviePlayer, InfoBar
            url8="http://showflix.org:5890/Mohamed/1234567/23"
            #url8="http://skdn.redi-vo.com/iptv/ch118?code=103131497823984&key=43336"
            #url8="http://mu02.v2iptv.com:8880/HJLM1399/gOQedvLAFg/2133"
            #url8="http://senadi.mine.nu:8000/live/O5ckVk7U1C/K91jSvYCeA/1264.ts"       
            #url8="http://iptv9211.hopto.me:8000/live/nfzNlANvf2/HHfWU3dzWt/32091.m3u8"   
            #url8="http://iptvpro.vision-new.org:8789/1212/1212/11170"
            ref = eServiceReference(4097, 0, url8)
            ref.setName(Name_08)
            self.session.open(MoviePlayer, ref)
        def BeinHD9(self):
            from Screens.InfoBar import MoviePlayer, InfoBar
            url9="http://iptvpro.premium-itv.com:8789/ahmed/1234/32718"
            #url9="http://skdn.redi-vo.com/iptv/ch510?code=103131497823984&key=27398"
            #url9="http://iptv-luxe.com:8789/live/1212/1212/29822.m3u8"
            #url9="http://mu02.v2iptv.com:8880/HJLM1399/gOQedvLAFg/2132"        
            #url9="http://senadi.mine.nu:8000/live/O5ckVk7U1C/K91jSvYCeA/1287.ts" 
            #url9="http://iptvpro.vision-new.org:8789/1212/1212/11168"  
            ref = eServiceReference(4097, 0, url9)
            ref.setName(Name_09)
            self.session.open(MoviePlayer, ref)
        def BeinHD10(self):
            from Screens.InfoBar import MoviePlayer, InfoBar
            url10="http://iptvpro.premium-itv.com:8789/ahmed/1234/92"
            #url10="http://skdn.redi-vo.com/iptv/ch511?code=103131497823984&key=51278"
            #url10="http://skdn.redi-vo.com/iptv/ch255?code=103131497823984&key=43852"
            #url10="http://iptv-luxe.com:8789/live/1212/1212/92.m3u8"
            #url10="http://iptvpro.vision-new.org:8789/1212/1212/10508"
            #url10="http://mu02.v2iptv.com:8880/HJLM1399/gOQedvLAFg/2131"
            #url10="http://best-servers.xyz:8000/3505832905415/3046728127636/14808"
            #url10="http://iptvpro.vision-new.org:8789/1212/1212/11166"             
            ref = eServiceReference(4097, 0, url10)
            ref.setName(Name_10)
            self.session.open(MoviePlayer, ref)
        def BeinHD11(self):
            from Screens.InfoBar import MoviePlayer, InfoBar
            #url11="http://skdn.redi-vo.com/iptv/ch202?code=103131497823984&key=22881"
            #url11="http://universeiptv.com:8000/live/alexaiptv/hvsfw2yfgwu/853.m3u8"
            #url11="http://universeiptv.com:8000/alexaiptv/hvsfw2yfgwu/853"
            #url11="http://nvkdn.redi-vo.com/iptv/ch202?code=1701273726237058&key=50378"            
            #url11="http://topiptv.net:5890/live/1234567/12345/553.m3u8"
            #url11="http://iptv-luxe.com:8789/live/1212/1212/17404.m3u8"
            #url11="http://iptv9211.hopto.me:8000/live/nfzNlANvf2/HHfWU3dzWt/32088.m3u8"  
            #url11="http://topiptv.net:5890/live/1234567/12345/58334.m3u8"       
            url11="http://vvn.neoredi.com/iptv/ch203?code=1501309316704233&key=15169"       
            ref = eServiceReference(4097, 0, url11)
            ref.setName(Name_11)
            self.session.open(MoviePlayer, ref)
        def DAZN1HD(self):
            from Screens.InfoBar import MoviePlayer, InfoBar        
            #url12="http://iptv.iptivihd.com:8000/live/cemal/sakarya54/22499.m3u8"
            url12="http://showflix.org:5890/Mohamed/1234567/1266"
            #url12="http://iptvsmarters.cc:25461/live/serkan/yilmaz/1951.ts"
            #url12="http://hemn2.xyz:8000/live/6PlHOlmM7a/gfKgQfpWED/10582.m3u8"
            #url12="http://45.77.65.162:80/live/SRTgsrtGsRth/7ue6hs45aerha34/257.m3u8"
            #url12="http://primeplus.tv:8080/YMq12IOMMi/XqJX8Mfx0i/16319" 
            #url12="http://s.igiptv.com:8000/live/abbas/112233/25652.m3u8"  
            #url12="http://linux-app.tv:6204/live/mustafa96/mustafa96/28357.m3u8" 
            #url12="http://62.210.92.2:25461/151515/151515/14378"                           
            #url12="http://g3m1n10.dyndns.org:2611/oB69PpuXuL/3x1zfkCdEo/299" 
            ref = eServiceReference(4097, 0, url12)
            ref.setName(Name_12)
            self.session.open(MoviePlayer, ref)
        def DAZN2HD(self):
            from Screens.InfoBar import MoviePlayer, InfoBar
            #url13="http://tv2iptv.com:8000/live/Faysal/faysal123/25653.m3u8"
            #url13="http://primeplus.tv:8080/YMq12IOMMi/XqJX8Mfx0i/16319" 
            #url13="http://linux-app.tv:6204/live/mustafa96/mustafa96/28358.m3u8"
            url13="http://showflix.org:5890/Mohamed/1234567/1267"
            #url13="http://iptv.iptivihd.com:8000/live/cemal/sakarya54/22500.m3u8"
            #url13="http://turkiptv.xyz:8080/live/elena/Elena123/126970.m3u8"
            #url13="http://tv2iptv.com:8000/live/Faysal/faysal123/25652.m3u8"  
            #url13="http://iptv6.premium-stv.com:25461/live/sourcegermanypro2/0626674936/2675.m3u8"
            #url13="http://topiptv.net:5890/tom01/01tom/1267"
            #url13="http://turkiptv.xyz:8080/live/elena/Elena123/126969.m3u8"       
            ref = eServiceReference(4097, 0, url13)
            ref.setName(Name_13)
            self.session.open(MoviePlayer, ref)  

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
