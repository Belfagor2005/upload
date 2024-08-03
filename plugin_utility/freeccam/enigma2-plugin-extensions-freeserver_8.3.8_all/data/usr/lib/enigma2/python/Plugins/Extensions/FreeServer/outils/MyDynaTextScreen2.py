#!/usr/bin/python
# -*- coding: UTF-8 -*-

from Plugins.Plugin import PluginDescriptor
from os import path as chmod
from shutil import move
from Screens.Screen import Screen
from datetime import date, datetime
from Components.Label import Label
from Screens.MessageBox import MessageBox
from Screens.Standby import *
from Components.Console import Console
from Components.MenuList import MenuList
from Components.ActionMap import ActionMap
from Components.MediaPlayer import *
from enigma import *
from Components.Pixmap import Pixmap  
from Tools.Directories import *
from Components.GUIComponent import *
from Components.config import *
from time import *
import requests , re, time, os, sys, time, datetime
from Components.Sources.List import List
from Screens.MessageBox import MessageBox
from Components.Pixmap import Pixmap  
from Components.GUIComponent import *
from Screens.ServiceInfo import *
from Components.config import *
from enigma import eServiceReference

from Plugins.Extensions.FreeServer.outils.compat import PY3
from Plugins.Extensions.FreeServer.outils.CronTimers import *
from Plugins.Extensions.FreeServer.outils.LiseScreencccam import *
from Plugins.Extensions.FreeServer.outils.LiseScreencccam2 import * 
from Plugins.Extensions.FreeServer.outils.Console2 import *
from Plugins.Extensions.FreeServer.outils.Console33 import *
from Plugins.Extensions.FreeServer.outils.Input import *
from Plugins.Extensions.FreeServer.outils.MyShPrombt import *
from Plugins.Extensions.FreeServer.outils.Showinfo import *

session = None

###################################################################################################### 
s = requests.Session()
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
    
def connected_to_internet():   
    try:
        _ = requests.get('https://github.com', timeout=3)
        return True
    except :
        return False
        
#########################################################################################################
class MyDynaTextScreen2(Screen):
#### Edit By RAED
        if not isHD():
            if DreamOS():
            	skin = """
                      <screen position="0,0" size="1920,1080" title="Schedule to football matchs this week" backgroundColor="#16000000" flags="wfNoBorder">             
                      <widget source="Title" render="Label" position="12,7" size="600,32" font="Play;28" backgroundColor="#16000000" foregroundColor="#FFE375" valign="center" halign="center" zPosition="2"/>
                      <eLabel text="Move Up/Down or Left/Right to move list/page" position="600,7" size="680,32" font="Play;28" foregroundColor="#FC0000" backgroundColor="#16000000" zPosition="2"/>           
                      <widget name="myMenu" position="17,52" size="1865,1014" foregroundColor="#FEFEFE" transparent="1" zPosition="2"/>
                      <!--ePixmap position="0,0" size="1920,1080" pixmap="/usr/lib/enigma2/python/Plugins/Extensions/FreeServer/Deco/SLIDE_03.jpg" alphatest="blend" transparent="1" /-->
                      </screen>"""
            else:
             	skin = """
                      <screen position="0,0" size="1916,1080" title="Schedule to football matchs this week" backgroundColor="#16000000" flags="wfNoBorder">             
                      <widget source="Title" render="Label" position="12,7" size="600,32" font="Play;28" backgroundColor="#16000000" foregroundColor="#FFE375" valign="center" halign="center" zPosition="2"/>
                      <eLabel text="Move Up/Down or Left/Right to move list/page" position="600,7" size="680,32" font="Play;28" foregroundColor="#FC0000" backgroundColor="#16000000" zPosition="2"/>           
                      <widget name="myMenu" position="25,52" size="1865,1014" font="Play;35" itemHeight="40" foregroundColor="#FEFEFE" transparent="1" zPosition="2"/>
                      <!--ePixmap position="0,0" size="1916,1080" pixmap="/usr/lib/enigma2/python/Plugins/Extensions/FreeServer/Deco/SLIDE_03.jpg" alphatest="blend" transparent="1" /-->
                      </screen>"""
        else:
                skin = """
                      <screen position="0,0" size="1280,720" title="Schedule to football matchs this week" backgroundColor="#16000000" flags="wfNoBorder">              
                      <widget source="Title" render="Label" position="12,7" size="600,32" font="Play;28" backgroundColor="#16000000" foregroundColor="#FFE375" valign="center" halign="center" zPosition="2"/>
                      <eLabel text="Move Up/Down or Left/Right to move list/page" position="600,7" size="680,32" font="Play;28" foregroundColor="#FC0000" backgroundColor="#16000000" zPosition="2"/>           
                      <widget name="myMenu" position="12,51" size="735,662" foregroundColor="#FEFEFE" transparent="1" zPosition="2"/>
                      <ePixmap position="0,0" size="1280,720" pixmap="/usr/lib/enigma2/python/Plugins/Extensions/FreeServer/Deco/SLIDE_03.jpg" alphatest="blend" transparent="1" />
                      </screen>"""
        
        def __init__(self, session, finishedCallback = None, picPath = None, args = 0):
                self.session = session
                Screen.__init__(self, session)
                self.finishedCallback = finishedCallback
                self.setTitle("List of VPN server avilable")
                self.wget = "wget --no-check-certificate"   
                list = []
                if config.plugins.FreeServerminoo.lang.value == "EN":
                        list.append(("    Saud_Alshuraim", "com_01"))                         
                        list.append(("    LIVE 13", "com_02"))
                        list.append(("    LIVE 14", "com_03"))  
                        list.append(("    LIVE 16", "com_04"))
                        list.append(("    The Voice of Ummah", "com_05")) 
                        list.append(("    Al-Kahf", "com_06"))
                        list.append(("    Qahira", "com_1"))                         
                        list.append(("    KSA", "com_2"))
                        list.append(("    Algeria", "com_3"))  
                        list.append(("    Morocco", "com_4"))
                        list.append(("    EAU", "com_5")) 
                        list.append(("    San Francisco", "com_6"))
                        list.append(("    Nour Ala Nour", "com_7"))             
                        list.append(("    Washington", "com_8"))
                        list.append(("    Live 1", "com_9"))          
                        list.append(("    Live 2", "com_10"))                        
                        list.append(("    Live 3", "com_11"))
                        list.append(("    Live 4", "com_12"))
                        list.append(("    Live 5", "com_13"))                
                        list.append(("    Ashams", "com_14"))
                        list.append(("    Chaarawi", "com_15"))
                        list.append(("    Maka", "com_16"))
                        list.append(("    Ahl Al Quran", "com_17"))
                        list.append(("    UK", "com_18"))
                        list.append(("    Naplouse", "com_19"))
                        list.append(("    Spain", "com_20"))
                        list.append(("    Buzzislam", "com_21"))
                        list.append(("    Australia", "com_22"))
                        list.append(("    Dawn", "com_23"))                
                        list.append(("    Crescent", "com_24"))
                        list.append(("    Al Manshuroh", "com_25"))
                        list.append(("    Rodja", "com_26"))
                        list.append(("    Lebanon", "com_27"))
                        list.append(("    Live 6", "com_28"))
                        list.append(("    New York", "com_29"))
                        list.append(("    San Francisco 2", "com_30"))
                        list.append(("    San Francisco 3", "com_31"))
                        list.append(("    Live 7", "com_32"))
                        list.append(("    Verse 24", "com_33"))
                        list.append(("    Nouvelle-Galles du Sud , Sydney", "com_34"))
                        list.append(("    Kandahar", "com_35"))
                        list.append(("    Beyrouth", "com_36"))
                        list.append(("    Abou Dabi", "com_37"))
                        list.append(("    Hanoi", "com_38")) 
                        list.append(("    Sharjah", "com_39"))    
                        list.append(("    Khartoum", "com_40"))
                        list.append(("    Dusseldorf", "com_41"))
                        list.append(("    San Francisco 4", "com_42"))
                        list.append(("    Berlin", "com_43"))
                        list.append(("    New Jersey", "com_44"))
                        list.append(("    District de Columbia", "com_45"))
                        list.append(("    Saint Gall", "com_46"))
                        list.append(("    Bandung", "com_47"))
                        list.append(("    Istanbul", "com_48"))
                        list.append(("    Victoria", "com_49"))
                        list.append(("    Ankara", "com_50"))
                        list.append(("    Maka", "com_51"))
                        list.append(("    Abidjan", "com_52"))
                        list.append(("    Miraath's", "com_53"))
                        list.append(("    Birmingham", "com_54"))
                        list.append(("    Tirana", "com_55"))
                        list.append(("    National Capital Region, Capitol", "com_56"))
                        list.append(("    Adwaa", "com_57"))
                        list.append(("    Adwaa 2", "com_58")) 
                        list.append(("    San Francisco", "com_59"))
                        list.append(("    Java occidental", "com_60"))             
                        list.append(("    Tunis", "com_61"))
                        list.append(("    Ankara", "com_62"))          
                        list.append(("    Hayat", "com_63"))                        
                        list.append(("    Paris", "com_64"))
                        list.append(("    Kayseri", "com_65"))
                        list.append(("    Manama", "com_66"))                
                        list.append(("    Antalya", "com_67"))
                        list.append(("    Dakar", "com_68"))
                        list.append(("    Tripoli", "com_69"))
                        list.append(("    Gaza", "com_70"))
                        list.append(("    District de Columbia, Washington", "com_71"))
                        list.append(("    Tripoli 2", "com_72"))
                        list.append(("    Sirius", "com_73"))
                        list.append(("    Alsiyada", "com_74"))
                        list.append(("    Berlin", "com_75"))
                        list.append(("    New Jersey, Union City", "com_76"))                
                        list.append(("    Omdourman", "com_77"))
                        list.append(("    Copenhague", "com_78"))
                        list.append(("    Koweit", "com_79"))
                        list.append(("    Kampala", "com_80"))
                        list.append(("    Region metropolitaine de Santiago", "com_81"))
                        list.append(("    Rio de Janeiro", "com_82"))
                        list.append(("    Khartoum", "com_83"))
                        list.append(("    Baburrohmah", "com_84"))
                        list.append(("    Rabat", "com_85"))
                        list.append(("    Beyrouth", "com_86"))
                        list.append(("    Londres", "com_87"))
                        list.append(("    Birmingham", "com_88"))
                        list.append(("    Sydney", "com_89"))
                        list.append(("    Sunnah", "com_90"))
                        list.append(("    Amman", "com_91")) 
                        list.append(("    Birlik", "com_92"))    
                        list.append(("    District de Columbia, Washington", "com_93"))
                        list.append(("    Cisjordanie", "com_94"))
                        list.append(("    Manchester", "com_95"))
                        list.append(("    Berlin", "com_96"))
                        list.append(("    New Jersey", "com_97"))
                        list.append(("    Jakarta", "com_98"))
                        list.append(("    Sabeel Al Anbiyya", "com_99"))
                        list.append(("    Eman City", "com_100"))
                        list.append(("    Caroline du Nord , Durham", "com_101"))    
                        list.append(("    Australie-Occidentale , Perth", "com_102"))
                        list.append(("    Angleterre , Leicester", "com_103"))
                        list.append(("    Hesse , Cassel", "com_104"))
                        list.append(("    Centre , Singapour", "com_105"))
                        list.append(("    Al-Manshuroh", "com_106"))
                        list.append(("    Nouvelle-Galles du Sud , Sydney", "com_107"))
                        list.append(("    Bradford", "com_108"))
                        list.append(("    Nouvelle-Galles du Sud , Sydney", "com_109"))
                        list.append(("    Ile-de-France , Paris", "com_110"))
                        list.append(("    Miraath's", "com_111"))
                        list.append(("    Hayat", "com_112"))
                        list.append(("    Saint-Gall", "com_113"))
                        list.append(("    Ustikolina", "com_114"))
                        list.append(("    Berlin", "com_115"))
                        list.append(("    Vietnamese", "com_116"))
                        list.append(("    Albashaer", "com_117"))
                        list.append(("    RIM-Mayotte, M'Tsangamouji", "com_118")) 
                        list.append(("    Bass", "com_119"))
                        list.append(("    Hovedstaden", "com_120"))             
                        list.append(("    Mercan", "com_121"))
                        list.append(("    Chile", "com_122"))          
                        list.append(("    Bakel", "com_123"))                        
                        list.append(("    Nour", "com_124"))
                        list.append(("    Koweit", "com_125"))
                        list.append(("    Live 8", "com_126"))                
                        list.append(("    Live 9", "com_127"))
                        list.append(("    Live 10", "com_128"))
                        list.append(("    Live 11", "com_129"))
                        list.append(("    Live 12", "com_130"))
                        list.append(("    Nottingham", "com_131"))
                        list.append(("    Paris", "com_132"))
                        list.append(("    Australie-Occidentale , Perth", "com_133"))
                        list.append(("    Caroline du Nord , Durham", "com_134"))
                        list.append(("    Kalimantan oriental , Balikpapan", "com_135"))
                        list.append(("    Western , Colombo", "com_136"))                
                        list.append(("    Angleterre , Bolton", "com_137"))
                        list.append(("    Ramallah", "com_138"))
                        list.append(("    Java oriental , Kediri", "com_139"))
                        list.append(("    Mogadiscio", "com_140"))
                        list.append(("    Johannesbourg", "com_141"))
                        list.append(("    RIM-Mayotte", "com_142"))
                        list.append(("    Singapour", "com_143"))
                        list.append(("    Izmir", "com_144"))
                        list.append(("    Victoria, Melbourne", "com_145"))
                        list.append(("    Tirana", "com_146"))
                        list.append(("    Amman", "com_147"))
                        list.append(("    New York", "com_148"))
                        list.append(("    Muhammad Ayyoob - Surat Al-Baqara", "com_149"))
                        list.append(("    Fares Abbad - Surat Al-Baqara", "com_150"))
                        list.append(("    Java occidental, Tasikmalaya", "com_151"))
                        list.append(("    Mahmoud Khalil Al-Husary", "com_152")) 
                        list.append(("    Santiago, Nunoa", "com_153"))    
                        list.append(("    Nasser Alqatami Musshaf - Al-Furqan", "com_154"))
                        list.append(("    Abu Baker Al-Shatiri Musshaf - Ghafir", "com_155"))
                        list.append(("    Abdullah Ali Jabir - Surat An-Naml", "com_156"))
                        list.append(("    Yasser Al Dosari - 049-Al-Hujurat", "com_157"))
                        list.append(("    Hani ar-Rifai - Surat Al-Ankaboot", "com_158"))
                        list.append(("    Muhammad Jibreel - Surat Yunus", "com_159"))
                        list.append(("    Muhammad al-Luhaidan - Surat At-Tawba", "com_160"))
                        list.append(("    Mohammad Al-Tablaaway - Ash-Shura", "com_161"))
                        list.append(("    Khaalid Abdullaah al-Qahtaanee - 024", "com_162"))    
                        list.append(("    Mishaari Raashid al-Aafaasee - Surat Al-Araf", "com_163"))
                        list.append(("    Bakel", "com_164"))
                        list.append(("    Ahle el-Safa", "com_165"))
                        list.append(("    Abdulrahman Alsudaes - Al-Imran", "com_166"))
                        list.append(("    Fairfield", "com_167"))
                        list.append(("    Abdulbari Mohammad", "com_168"))
                        list.append(("    Abdul-Samad", "com_169"))
                        list.append(("    Al-Husary", "com_170"))
                        list.append(("    Paris", "com_171"))
                        list.append(("    Rayhan", "com_172"))
                        list.append(("    Masjid Live - Bolton", "com_173"))
                        list.append(("    Shurooq Ramadan", "com_174"))
                        list.append(("    Radio Moga", "com_175"))
                        list.append(("    Nour", "com_176"))
                        list.append(("    Cairo", "com_177"))
                        list.append(("    Mohammed_Siddiq_Alminshawi", "com_178")) 
                        list.append(("    Fi_Dilal_Alsiyra", "com_179"))
                        list.append(("    Alaikhtiarat_Alfiqhayha_Ben_Baz", "com_180"))             
                        list.append(("    France", "com_181"))
                        list.append(("    Live from Makkah", "com_182"))          
                        list.append(("    Heart", "com_183"))                        
                        list.append(("    Djedah", "com_184"))
                        list.append(("    Sydney", "com_185"))
                        list.append(("    Live 15", "com_186"))                
                        list.append(("    Java central, Cilacap", "com_187"))
                        list.append(("    Java oriental, Surabaya", "com_188"))
                        list.append(("    Kalmunai", "com_189"))
                        list.append(("    Abou Dabi", "com_190"))
                        list.append(("    Fares Abbad - Surat Maryam", "com_191"))
                        list.append(("    Muhammad Ayyoob - Quran - Surat Yusuf", "com_192"))
                        list.append(("    Mahmoud Khalil Al-Husary", "com_193"))                        
                        list.append(("    Gorontalo", "com_194"))
                        list.append(("    Nasser Alqatami- Al-Baqarah", "com_195"))
                        list.append(("    Abdullah Ali Jabir - Surat An-Nisa", "com_196"))                
                        list.append(("    Koweit", "com_197"))
                        list.append(("    Cisjordanie, Ramallah", "com_198"))
                        list.append(("    Barakath", "com_199"))
                        list.append(("    Makkah", "com_200"))
                        list.append(("    Al-Fatihah , Makkah  **7 (1)**", "com_201"))    
                        list.append(("    Al-Baqarah , Madinah  **286 (40)**", "com_202"))
                        list.append(("    Aali 'Imran , Madinah  **200 (20)**", "com_203"))
                        list.append(("    An-Nisa , Madinah  **176 (24)**", "com_204"))
                        list.append(("    Al-Ma'idah , Madinah  **120 (16)**", "com_205"))
                        list.append(("    Al-An'am , Makkah  **165 (20)**", "com_206"))
                        list.append(("    Al-A'raf , Makkah  **206 (24)**", "com_207"))
                        list.append(("    Al-Anfal , Madinah  **75 (10)**", "com_208"))
                        list.append(("    At-Tawbah , Madinah  **129 (16)**", "com_209"))
                        list.append(("    Yunus , Makkah  **109 (11)**", "com_210"))
                        list.append(("    Hud , Makkah  **123 (10)**", "com_211"))
                        list.append(("    Yusuf , Makkah  **111 (12)**", "com_212"))
                        list.append(("    Ar-Ra'd , Madinah  **743 (6)**", "com_213"))
                        list.append(("    Ibrahim , Makkah  **52 (7)**", "com_214"))
                        list.append(("    Al-Hijr , Makkah  **99 (6)**", "com_215"))
                        list.append(("    An-Nahl , Makkah  **128 (16)**", "com_216"))
                        list.append(("    Al-Isra , Makkah  **111 (12)**", "com_217"))
                        list.append(("    Al-Kahf , Makkah  **110 (12)**", "com_218")) 
                        list.append(("    Maryam , Makkah  **98 (6)**", "com_219"))
                        list.append(("    Ta-Ha , Makkah  **135 (8)**", "com_220"))             
                        list.append(("    Al-Anbiya , Makkah  **112 (7)**", "com_221"))
                        list.append(("    Al-Hajj , Madinah  **78 (10)**", "com_222"))          
                        list.append(("    Al-Mu'minun , Makkah  **118 (6)**", "com_223"))                        
                        list.append(("    An-Nur , Madinah  **64 (9)**", "com_224"))
                        list.append(("    Al-Furqan , Makkah  **77 (6)**", "com_225"))
                        list.append(("    Ash-Shu'ara , Makkah  **227 (11)**", "com_226"))                
                        list.append(("    An-Naml , Makkah  **93 (7)**", "com_227"))
                        list.append(("    Al-Qasas , Makkah  **88 (9)**", "com_228"))
                        list.append(("    Al-Ankabut , Makkah  **69 (7)**", "com_229"))
                        list.append(("    Ar-Rum , Makkah  **60 (6)**", "com_230"))
                        list.append(("    Luqmaan , Makkah  **34 (4)**", "com_231"))
                        list.append(("    As-Sajdah , Makkah  **30 (3)**", "com_232"))
                        list.append(("    Al-Ahzaab , Madinah  **73 (9)**", "com_233"))
                        list.append(("    Saba , Makkah  **54 (6)**", "com_234"))
                        list.append(("    Faatir , Makkah  **45 (5)**", "com_235"))
                        list.append(("    Ya-Sin , Makkah  **83 (5)**", "com_236"))                
                        list.append(("    As-Saaffaat , Makkah  **182 (5)**", "com_237"))
                        list.append(("    Saad , Makkah  **88 (5)**", "com_238"))
                        list.append(("    Az-Zumar , Makkah  **75 (8)**", "com_239"))
                        list.append(("    Ghafir , Makkah  **85 (9)**", "com_240"))
                        list.append(("    Fussilat , Makkah  **54 (6)**", "com_241"))
                        list.append(("    Ash-Shura , Makkah  **53 (5)**", "com_242"))
                        list.append(("    Az-Zukhruf , Makkah  **89 (7)**", "com_243"))
                        list.append(("    Ad-Dukhaan , Makkah  **59 (3)**", "com_244"))
                        list.append(("    Al-Jaathiyah , Makkah  **37 (4)**", "com_245"))
                        list.append(("    Al-Ahqaaf , Makkah  **35 (4 1/2)**", "com_246"))
                        list.append(("    Muhammad , Madinah  **38 (4)**", "com_247"))
                        list.append(("    Al-Fath , Madinah  **29 (4 1/2)**", "com_148"))
                        list.append(("    Al-Hujuraat , Madinah  **18 (2 1/2)**", "com_249"))
                        list.append(("    Qaaf , Makkah  **45 (3)**", "com_250"))
                        list.append(("    Adh-Dhaariyaat , Makkah  **60 (2 1/2)**", "com_251"))
                        list.append(("    At-Toor , Makkah  **49 (2 1/2)**", "com_252")) 
                        list.append(("    An-Najm , Makkah  **62 (2 1/2)**", "com_253"))    
                        list.append(("    Al-Qamar , Makkah  **55 (2 1/2)**", "com_254"))
                        list.append(("    Ar-Rahman , Makkah  **78 (3)**", "com_255"))
                        list.append(("    Al-Waqi'ah , Makkah  **96 (3 1/2)**", "com_256"))
                        list.append(("    Al-Hadeed , Madinah  **29 (4)**", "com_257"))
                        list.append(("    Al-Mujadila , Madinah  **22 (3 1/2)**", "com_258"))
                        list.append(("    Al-Hashr , Madinah  **24 (3 1/2)**", "com_259"))
                        list.append(("    Al-Mumtahanah , Madinah  **13 (2 1/2)**", "com_260"))
                        list.append(("    As-Saff , Madinah  **14 (1 1/2)**", "com_261"))
                        list.append(("    Al-Jumu'ah , Madinah  **11 (1 1/2)**", "com_262"))    
                        list.append(("    Al-Munafiqoon , Madinah  **11 (1 1/2)**", "com_263"))
                        list.append(("    At-Taghabun , Madinah  **18 (2)**", "com_264"))
                        list.append(("    At-Talaq , Madinah  **12 (2)**", "com_265"))
                        list.append(("    At-Tahreem , Madinah  **12 (2)**", "com_266"))
                        list.append(("    Al-Mulk , Makkah  **30 (1 1/2)**", "com_267"))
                        list.append(("    Al-Qalam , Makkah  **52 (2)**", "com_268"))
                        list.append(("    Al-Haaqqa , Makkah  **52 (2)**", "com_269"))
                        list.append(("    Al-Ma'aarij , Makkah  **44 (1 1/2)**", "com_270"))
                        list.append(("    Nuh , Makkah  **28 (1 1/2)**", "com_271"))
                        list.append(("    Al-Jinn , Makkah  **28 (2)**", "com_272"))
                        list.append(("    Al-Muzzammil , Makkah  **20 (1 1/2)**", "com_273"))
                        list.append(("    Al-Muddaththir , Makkah  **56 (2)**", "com_274"))
                        list.append(("    Al-Qiyamah , Makkah  **40 (1)**", "com_275"))
                        list.append(("    Al-Insaan , Madinah  **31 (2)**", "com_276"))
                        list.append(("    Al-Mursalaat , Makkah  **50 (1 1/2)**", "com_277"))
                        list.append(("    An-Naba' , Makkah  **40 (1 1/2)**", "com_278")) 
                        list.append(("    An-Naazi'aat , Makkah  **46 (1 1/2)**", "com_279"))
                        list.append(("    Abasa , Makkah  **42 (1)**", "com_280"))             
                        list.append(("    At-Takweer , Makkah  **29 (1)**", "com_181"))
                        list.append(("    Al-Infitar , Makkah  **19 (1/2)**", "com_282"))          
                        list.append(("    Al-Mutaffifeen , Makkah  **36 (1)**", "com_283"))                        
                        list.append(("    Al-Inshiqaaq , Makkah  **25 (1)**", "com_284"))
                        list.append(("    Al-Burooj , Makkah  **22 (1)**", "com_285"))
                        list.append(("    At-Taariq , Makkah  **17 (1/2)**", "com_286"))                
                        list.append(("    Al-A'la , Makkah  **19 (1/2)**", "com_287"))
                        list.append(("    Al-Ghaashiyah , Makkah  **26 (1)**", "com_288"))
                        list.append(("    Al-Fajr , Makkah  **30 (1)**", "com_289"))
                        list.append(("    Al-Balad , Makkah  **20 (1/2)**", "com_190"))
                        list.append(("    Ash-Shams , Makkah  **15 (1/2)**", "com_291"))
                        list.append(("    Al-Layl , Makkah  **21 (1/2)**", "com_292"))
                        list.append(("    Ad-Dhuha , Makkah  **11 (1/2)**", "com_293"))                        
                        list.append(("    Ash-Sharh , Makkah  **8 (1/3)**", "com_294"))
                        list.append(("    At-Tin , Makkah  **8 (1/3)**", "com_295"))
                        list.append(("    Al-Alaq , Makkah  **19 (1/2)**", "com_296"))                
                        list.append(("    Al-Qadr , Makkah  **5 (1/3)**", "com_297"))
                        list.append(("    Al-Bayyinah , Madinah  **8 (1)**", "com_298"))
                        list.append(("    Az-Zalzalah , Madinah  **8 (1/3)**", "com_299"))
                        list.append(("    Al-'Aadiyat , Makkah  **11 (1/3)**", "com_300"))
                        list.append(("    Al-Qaari'ah , Makkah  **11 (1/3)**", "com_301"))
                        list.append(("    At-Takaathur , Makkah  **8 (1/3)**", "com_302"))
                        list.append(("    Al-'Asr , Makkah  **3 (1/3)**", "com_303"))
                        list.append(("    Al-Humazah , Makkah  **9 (1/3)**", "com_304"))
                        list.append(("    Al-Feel , Makkah  **5 (1/3)**", "com_305"))
                        list.append(("    Quraish , Makkah  **4 (1/3)**", "com_306"))
                        list.append(("    Al-Maa'oon , Makkah  **7 (1/3)**", "com_307"))
                        list.append(("    Al-Kawthar , Makkah  **3 (1/3)**", "com_308"))
                        list.append(("    Al-Kaafiroon , Makkah  **6 (1/3)**", "com_309"))
                        list.append(("    An-Nasr , Madinah  **3 (1/3)**", "com_310"))
                        list.append(("    Al-Masad , Makkah  **5 (1/3)**", "com_311"))
                        list.append(("    Al-Ikhlas , Makkah  **4 (1/3)**", "com_312"))
                        list.append(("    Al-Falaq , Makkah  **5 (1/3)**", "com_313"))
                        list.append(("    An-Naas , Makkah  **6 (1/3)**", "com_314"))
                        list.append(("    Full Tilawa", "com_315"))                        
                        list.append(("    Doa Khatam Quran", "com_316"))
                        list.append(("    Doa Khatam Quran", "com_317"))
                        list.append(("    Doa Khatam Quran", "com_318"))                
                        list.append(("    Doa Khatam Quran", "com_319"))
                        list.append(("    Doa Khatam Quran", "com_320"))
                        list.append(("    Doa Khatam Quran", "com_321"))                
                        list.append(("    Doa Khatam Quran 1409", "com_322"))
                        list.append(("    Part of ama Doa Khatam Quran 1414", "com_323"))
                        list.append(("    Doa Khatam Quran for the night of 27 Ramadan 1423", "com_324"))
                        list.append(("    Doa Khatam Quran", "com_325"))                        
                elif config.plugins.FreeServerminoo.lang.value == "AR":
                        list.append(("    Saud_Alshuraim", "com_01"))                         
                        list.append(("    LIVE 13", "com_02"))
                        list.append(("    LIVE 14", "com_03"))  
                        list.append(("    LIVE 16", "com_04"))
                        list.append(("    The Voice of Ummah", "com_05")) 
                        list.append(("    Al-Kahf", "com_06"))
                        list.append(("    القاهرة", "com_1"))                         
                        list.append(("    السعودية", "com_2"))
                        list.append(("    الجزائر", "com_3"))  
                        list.append(("    المغرب", "com_4"))
                        list.append(("    EAU", "com_5")) 
                        list.append(("    النشرة الإسلامية", "com_6"))
                        list.append(("    نور على نور", "com_7"))             
                        list.append(("    واشنطن", "com_8"))
                        list.append(("    مباشر", "com_9"))          
                        list.append(("    مباشر", "com_10"))                        
                        list.append(("    مباشر", "com_11"))
                        list.append(("    مباشر", "com_12"))
                        list.append(("    مباشر", "com_13"))                
                        list.append(("    أشمس", "com_14"))
                        list.append(("    Chaarawi", "com_15"))
                        list.append(("    Maka", "com_16"))
                        list.append(("    Ahl Al Quran", "com_17"))
                        list.append(("    UK", "com_18"))
                        list.append(("    Naplouse", "com_19"))
                        list.append(("    Spain", "com_20"))
                        list.append(("    Buzzislam", "com_21"))
                        list.append(("    Australia", "com_22"))
                        list.append(("    Dawn", "com_23"))                
                        list.append(("    Crescent", "com_24"))
                        list.append(("    Al Manshuroh", "com_25"))
                        list.append(("    Rodja", "com_26"))
                        list.append(("    Lebanon", "com_27"))
                        list.append(("    Live 6", "com_28"))
                        list.append(("    New York", "com_29"))
                        list.append(("    San Francisco 2", "com_30"))
                        list.append(("    San Francisco 3", "com_31"))
                        list.append(("    Live 7", "com_32"))
                        list.append(("    Verse 24", "com_33"))
                        list.append(("    Nouvelle-Galles du Sud , Sydney", "com_34"))
                        list.append(("    Kandahar", "com_35"))
                        list.append(("    Beyrouth", "com_36"))
                        list.append(("    Abou Dabi", "com_37"))
                        list.append(("    Hanoi", "com_38")) 
                        list.append(("    Sharjah", "com_39"))    
                        list.append(("    Khartoum", "com_40"))
                        list.append(("    Dsseldorf", "com_41"))
                        list.append(("    San Francisco 4", "com_42"))
                        list.append(("    Berlin", "com_43"))
                        list.append(("    New Jersey", "com_44"))
                        list.append(("    District de Columbia", "com_45"))
                        list.append(("    Saint Gall", "com_46"))
                        list.append(("    Bandung", "com_47"))
                        list.append(("    Istanbul", "com_48"))
                        list.append(("    Victoria", "com_49"))
                        list.append(("    Ankara", "com_50"))
                        list.append(("    Maka", "com_51"))
                        list.append(("    Abidjan", "com_52"))
                        list.append(("    Miraath's", "com_53"))
                        list.append(("    Birmingham", "com_54"))
                        list.append(("    Tirana", "com_55"))
                        list.append(("    National Capital Region, Capitol", "com_56"))
                        list.append(("    Adwaa", "com_57"))
                        list.append(("    Adwaa 2", "com_58")) 
                        list.append(("    San Francisco", "com_59"))
                        list.append(("    Java occidental", "com_60"))             
                        list.append(("    Tunis", "com_61"))
                        list.append(("    Ankara", "com_62"))          
                        list.append(("    Hayat", "com_63"))                        
                        list.append(("    Paris", "com_64"))
                        list.append(("    Kayseri", "com_65"))
                        list.append(("    Manama", "com_66"))                
                        list.append(("    Antalya", "com_67"))
                        list.append(("    Dakar", "com_68"))
                        list.append(("    Tripoli", "com_69"))
                        list.append(("    Gaza", "com_70"))
                        list.append(("    District de Columbia, Washington", "com_71"))
                        list.append(("    Tripoli 2", "com_72"))
                        list.append(("    Sirius", "com_73"))
                        list.append(("    Alsiyada", "com_74"))
                        list.append(("    Berlin", "com_75"))
                        list.append(("    New Jersey, Union City", "com_76"))                
                        list.append(("    Omdourman", "com_77"))
                        list.append(("    Copenhague", "com_78"))
                        list.append(("    Koweit", "com_79"))
                        list.append(("    Kampala", "com_80"))
                        list.append(("    Region metropolitaine de Santiago", "com_81"))
                        list.append(("    Rio de Janeiro", "com_82"))
                        list.append(("    Khartoum", "com_83"))
                        list.append(("    Baburrohmah", "com_84"))
                        list.append(("    Rabat", "com_85"))
                        list.append(("    Beyrouth", "com_86"))
                        list.append(("    Londres", "com_87"))
                        list.append(("    Birmingham", "com_88"))
                        list.append(("    Sydney", "com_89"))
                        list.append(("    Sunnah", "com_90"))
                        list.append(("    Amman", "com_91")) 
                        list.append(("    Birlik", "com_92"))    
                        list.append(("    District de Columbia, Washington", "com_93"))
                        list.append(("    Cisjordanie", "com_94"))
                        list.append(("    Manchester", "com_95"))
                        list.append(("    Berlin", "com_96"))
                        list.append(("    New Jersey", "com_97"))
                        list.append(("    Jakarta", "com_98"))
                        list.append(("    Sabeel Al Anbiyya", "com_99"))
                        list.append(("    Eman City", "com_100"))
                        list.append(("    Caroline du Nord , Durham", "com_101"))    
                        list.append(("    Australie-Occidentale , Perth", "com_102"))
                        list.append(("    Angleterre , Leicester", "com_103"))
                        list.append(("    Hesse , Cassel", "com_104"))
                        list.append(("    Centre , Singapour", "com_105"))
                        list.append(("    Al-Manshuroh", "com_106"))
                        list.append(("    Nouvelle-Galles du Sud , Sydney", "com_107"))
                        list.append(("    Bradford", "com_108"))
                        list.append(("    Nouvelle-Galles du Sud , Sydney", "com_109"))
                        list.append(("    Ile-de-France , Paris", "com_110"))
                        list.append(("    Miraath's", "com_111"))
                        list.append(("    Hayat", "com_112"))
                        list.append(("    Saint-Gall", "com_113"))
                        list.append(("    Ustikolina", "com_114"))
                        list.append(("    Berlin", "com_115"))
                        list.append(("    Vietnamese", "com_116"))
                        list.append(("    Albashaer", "com_117"))
                        list.append(("    RIM-Mayotte, M'Tsangamouji", "com_118")) 
                        list.append(("    Bass", "com_119"))
                        list.append(("    Hovedstaden", "com_120"))             
                        list.append(("    Mercan", "com_121"))
                        list.append(("    Chile", "com_122"))          
                        list.append(("    Bakel", "com_123"))                        
                        list.append(("    Nour", "com_124"))
                        list.append(("    Koweit", "com_125"))
                        list.append(("    Live 8", "com_126"))                
                        list.append(("    Live 9", "com_127"))
                        list.append(("    Live 10", "com_128"))
                        list.append(("    Live 11", "com_129"))
                        list.append(("    Live 12", "com_130"))
                        list.append(("    Nottingham", "com_131"))
                        list.append(("    Paris", "com_132"))
                        list.append(("    Australie-Occidentale , Perth", "com_133"))
                        list.append(("    Caroline du Nord , Durham", "com_134"))
                        list.append(("    Kalimantan oriental , Balikpapan", "com_135"))
                        list.append(("    Western , Colombo", "com_136"))                
                        list.append(("    Angleterre , Bolton", "com_137"))
                        list.append(("    Ramallah", "com_138"))
                        list.append(("    Java oriental , Kediri", "com_139"))
                        list.append(("    Mogadiscio", "com_140"))
                        list.append(("    Johannesbourg", "com_141"))
                        list.append(("    RIM-Mayotte", "com_142"))
                        list.append(("    Singapour", "com_143"))
                        list.append(("    Izmir", "com_144"))
                        list.append(("    Victoria, Melbourne", "com_145"))
                        list.append(("    Tirana", "com_146"))
                        list.append(("    Amman", "com_147"))
                        list.append(("    New York", "com_148"))
                        list.append(("    Muhammad Ayyoob - Surat Al-Baqara", "com_149"))
                        list.append(("    Fares Abbad - Surat Al-Baqara", "com_150"))
                        list.append(("    Java occidental, Tasikmalaya", "com_151"))
                        list.append(("    Mahmoud Khalil Al-Husary", "com_152")) 
                        list.append(("    Santiago, Nunoa", "com_153"))    
                        list.append(("    Nasser Alqatami Musshaf - Al-Furqan", "com_154"))
                        list.append(("    Abu Baker Al-Shatiri Musshaf - Ghafir", "com_155"))
                        list.append(("    Abdullah Ali Jabir - Surat An-Naml", "com_156"))
                        list.append(("    Yasser Al Dosari - 049-Al-Hujurat", "com_157"))
                        list.append(("    Hani ar-Rifai - Surat Al-Ankaboot", "com_158"))
                        list.append(("    Muhammad Jibreel - Surat Yunus", "com_159"))
                        list.append(("    Muhammad al-Luhaidan - Surat At-Tawba", "com_160"))
                        list.append(("    Mohammad Al-Tablaaway - Ash-Shura", "com_161"))
                        list.append(("    Khaalid Abdullaah al-Qahtaanee - 024", "com_162"))    
                        list.append(("    Mishaari Raashid al-Aafaasee - Surat Al-Araf", "com_163"))
                        list.append(("    Bakel", "com_164"))
                        list.append(("    Ahle el-Safa", "com_165"))
                        list.append(("    Abdulrahman Alsudaes - Al-Imran", "com_166"))
                        list.append(("    Fairfield", "com_167"))
                        list.append(("    Abdulbari Mohammad", "com_168"))
                        list.append(("    Abdul-Samad", "com_169"))
                        list.append(("    Al-Husary", "com_170"))
                        list.append(("    Paris", "com_171"))
                        list.append(("    Rayhan", "com_172"))
                        list.append(("    Masjid Live - Bolton", "com_173"))
                        list.append(("    Shurooq Ramadan", "com_174"))
                        list.append(("    Radio Moga", "com_175"))
                        list.append(("    Nour", "com_176"))
                        list.append(("    Cairo", "com_177"))
                        list.append(("    Mohammed_Siddiq_Alminshawi", "com_178")) 
                        list.append(("    Fi_Dilal_Alsiyra", "com_179"))
                        list.append(("    Alaikhtiarat_Alfiqhayha_Ben_Baz", "com_180"))             
                        list.append(("    France", "com_181"))
                        list.append(("    Live from Makkah", "com_182"))          
                        list.append(("    Heart", "com_183"))                        
                        list.append(("    Djedah", "com_184"))
                        list.append(("    Sydney", "com_185"))
                        list.append(("    Live 15", "com_186"))                
                        list.append(("    Java central, Cilacap", "com_187"))
                        list.append(("    Java oriental, Surabaya", "com_188"))
                        list.append(("    Kalmunai", "com_189"))
                        list.append(("    Abou Dabi", "com_190"))
                        list.append(("    Fares Abbad - Surat Maryam", "com_191"))
                        list.append(("    Muhammad Ayyoob - Quran - Surat Yusuf", "com_192"))
                        list.append(("    Mahmoud Khalil Al-Husary", "com_193"))                        
                        list.append(("    Gorontalo", "com_194"))
                        list.append(("    Nasser Alqatami- Al-Baqarah", "com_195"))
                        list.append(("    Abdullah Ali Jabir - Surat An-Nisa", "com_196"))                
                        list.append(("    Koweit", "com_197"))
                        list.append(("    Cisjordanie, Ramallah", "com_198"))
                        list.append(("    Barakath", "com_199"))
                        list.append(("    Makkah", "com_200"))
                        list.append(("    Al-Fatihah , Makkah  **7 (1)**", "com_201"))    
                        list.append(("    Al-Baqarah , Madinah  **286 (40)**", "com_202"))
                        list.append(("    Aali 'Imran , Madinah  **200 (20)**", "com_203"))
                        list.append(("    An-Nisa , Madinah  **176 (24)**", "com_204"))
                        list.append(("    Al-Ma'idah , Madinah  **120 (16)**", "com_205"))
                        list.append(("    Al-An'am , Makkah  **165 (20)**", "com_206"))
                        list.append(("    Al-A'raf , Makkah  **206 (24)**", "com_207"))
                        list.append(("    Al-Anfal , Madinah  **75 (10)**", "com_208"))
                        list.append(("    At-Tawbah , Madinah  **129 (16)**", "com_209"))
                        list.append(("    Yunus , Makkah  **109 (11)**", "com_210"))
                        list.append(("    Hud , Makkah  **123 (10)**", "com_211"))
                        list.append(("    Yusuf , Makkah  **111 (12)**", "com_212"))
                        list.append(("    Ar-Ra'd , Madinah  **743 (6)**", "com_213"))
                        list.append(("    Ibrahim , Makkah  **52 (7)**", "com_214"))
                        list.append(("    Al-Hijr , Makkah  **99 (6)**", "com_215"))
                        list.append(("    An-Nahl , Makkah  **128 (16)**", "com_216"))
                        list.append(("    Al-Isra , Makkah  **111 (12)**", "com_217"))
                        list.append(("    Al-Kahf , Makkah  **110 (12)**", "com_218")) 
                        list.append(("    Maryam , Makkah  **98 (6)**", "com_219"))
                        list.append(("    Ta-Ha , Makkah  **135 (8)**", "com_220"))             
                        list.append(("    Al-Anbiya , Makkah  **112 (7)**", "com_221"))
                        list.append(("    Al-Hajj , Madinah  **78 (10)**", "com_222"))          
                        list.append(("    Al-Mu'minun , Makkah  **118 (6)**", "com_223"))                        
                        list.append(("    An-Nur , Madinah  **64 (9)**", "com_224"))
                        list.append(("    Al-Furqan , Makkah  **77 (6)**", "com_225"))
                        list.append(("    Ash-Shu'ara , Makkah  **227 (11)**", "com_226"))                
                        list.append(("    An-Naml , Makkah  **93 (7)**", "com_227"))
                        list.append(("    Al-Qasas , Makkah  **88 (9)**", "com_228"))
                        list.append(("    Al-Ankabut , Makkah  **69 (7)**", "com_229"))
                        list.append(("    Ar-Rum , Makkah  **60 (6)**", "com_230"))
                        list.append(("    Luqmaan , Makkah  **34 (4)**", "com_231"))
                        list.append(("    As-Sajdah , Makkah  **30 (3)**", "com_232"))
                        list.append(("    Al-Ahzaab , Madinah  **73 (9)**", "com_233"))
                        list.append(("    Saba , Makkah  **54 (6)**", "com_234"))
                        list.append(("    Faatir , Makkah  **45 (5)**", "com_235"))
                        list.append(("    Ya-Sin , Makkah  **83 (5)**", "com_236"))                
                        list.append(("    As-Saaffaat , Makkah  **182 (5)**", "com_237"))
                        list.append(("    Saad , Makkah  **88 (5)**", "com_238"))
                        list.append(("    Az-Zumar , Makkah  **75 (8)**", "com_239"))
                        list.append(("    Ghafir , Makkah  **85 (9)**", "com_240"))
                        list.append(("    Fussilat , Makkah  **54 (6)**", "com_241"))
                        list.append(("    Ash-Shura , Makkah  **53 (5)**", "com_242"))
                        list.append(("    Az-Zukhruf , Makkah  **89 (7)**", "com_243"))
                        list.append(("    Ad-Dukhaan , Makkah  **59 (3)**", "com_244"))
                        list.append(("    Al-Jaathiyah , Makkah  **37 (4)**", "com_245"))
                        list.append(("    Al-Ahqaaf , Makkah  **35 (4 1/2)**", "com_246"))
                        list.append(("    Muhammad , Madinah  **38 (4)**", "com_247"))
                        list.append(("    Al-Fath , Madinah  **29 (4 1/2)**", "com_148"))
                        list.append(("    Al-Hujuraat , Madinah  **18 (2 1/2)**", "com_249"))
                        list.append(("    Qaaf , Makkah  **45 (3)**", "com_250"))
                        list.append(("    Adh-Dhaariyaat , Makkah  **60 (2 1/2)**", "com_251"))
                        list.append(("    At-Toor , Makkah  **49 (2 1/2)**", "com_252")) 
                        list.append(("    An-Najm , Makkah  **62 (2 1/2)**", "com_253"))    
                        list.append(("    Al-Qamar , Makkah  **55 (2 1/2)**", "com_254"))
                        list.append(("    Ar-Rahman , Makkah  **78 (3)**", "com_255"))
                        list.append(("    Al-Waqi'ah , Makkah  **96 (3 1/2)**", "com_256"))
                        list.append(("    Al-Hadeed , Madinah  **29 (4)**", "com_257"))
                        list.append(("    Al-Mujadila , Madinah  **22 (3 1/2)**", "com_258"))
                        list.append(("    Al-Hashr , Madinah  **24 (3 1/2)**", "com_259"))
                        list.append(("    Al-Mumtahanah , Madinah  **13 (2 1/2)**", "com_260"))
                        list.append(("    As-Saff , Madinah  **14 (1 1/2)**", "com_261"))
                        list.append(("    Al-Jumu'ah , Madinah  **11 (1 1/2)**", "com_262"))    
                        list.append(("    Al-Munafiqoon , Madinah  **11 (1 1/2)**", "com_263"))
                        list.append(("    At-Taghabun , Madinah  **18 (2)**", "com_264"))
                        list.append(("    At-Talaq , Madinah  **12 (2)**", "com_265"))
                        list.append(("    At-Tahreem , Madinah  **12 (2)**", "com_266"))
                        list.append(("    Al-Mulk , Makkah  **30 (1 1/2)**", "com_267"))
                        list.append(("    Al-Qalam , Makkah  **52 (2)**", "com_268"))
                        list.append(("    Al-Haaqqa , Makkah  **52 (2)**", "com_269"))
                        list.append(("    Al-Ma'aarij , Makkah  **44 (1 1/2)**", "com_270"))
                        list.append(("    Nuh , Makkah  **28 (1 1/2)**", "com_271"))
                        list.append(("    Al-Jinn , Makkah  **28 (2)**", "com_272"))
                        list.append(("    Al-Muzzammil , Makkah  **20 (1 1/2)**", "com_273"))
                        list.append(("    Al-Muddaththir , Makkah  **56 (2)**", "com_274"))
                        list.append(("    Al-Qiyamah , Makkah  **40 (1)**", "com_275"))
                        list.append(("    Al-Insaan , Madinah  **31 (2)**", "com_276"))
                        list.append(("    Al-Mursalaat , Makkah  **50 (1 1/2)**", "com_277"))
                        list.append(("    An-Naba' , Makkah  **40 (1 1/2)**", "com_278")) 
                        list.append(("    An-Naazi'aat , Makkah  **46 (1 1/2)**", "com_279"))
                        list.append(("    Abasa , Makkah  **42 (1)**", "com_280"))             
                        list.append(("    At-Takweer , Makkah  **29 (1)**", "com_181"))
                        list.append(("    Al-Infitar , Makkah  **19 (1/2)**", "com_282"))          
                        list.append(("    Al-Mutaffifeen , Makkah  **36 (1)**", "com_283"))                        
                        list.append(("    Al-Inshiqaaq , Makkah  **25 (1)**", "com_284"))
                        list.append(("    Al-Burooj , Makkah  **22 (1)**", "com_285"))
                        list.append(("    At-Taariq , Makkah  **17 (1/2)**", "com_286"))                
                        list.append(("    Al-A'la , Makkah  **19 (1/2)**", "com_287"))
                        list.append(("    Al-Ghaashiyah , Makkah  **26 (1)**", "com_288"))
                        list.append(("    Al-Fajr , Makkah  **30 (1)**", "com_289"))
                        list.append(("    Al-Balad , Makkah  **20 (1/2)**", "com_190"))
                        list.append(("    Ash-Shams , Makkah  **15 (1/2)**", "com_291"))
                        list.append(("    Al-Layl , Makkah  **21 (1/2)**", "com_292"))
                        list.append(("    Ad-Dhuha , Makkah  **11 (1/2)**", "com_293"))                        
                        list.append(("    Ash-Sharh , Makkah  **8 (1/3)**", "com_294"))
                        list.append(("    At-Tin , Makkah  **8 (1/3)**", "com_295"))
                        list.append(("    Al-Alaq , Makkah  **19 (1/2)**", "com_296"))                
                        list.append(("    Al-Qadr , Makkah  **5 (1/3)**", "com_297"))
                        list.append(("    Al-Bayyinah , Madinah  **8 (1)**", "com_298"))
                        list.append(("    Az-Zalzalah , Madinah  **8 (1/3)**", "com_299"))
                        list.append(("    Al-'Aadiyat , Makkah  **11 (1/3)**", "com_300"))
                        list.append(("    Al-Qaari'ah , Makkah  **11 (1/3)**", "com_301"))
                        list.append(("    At-Takaathur , Makkah  **8 (1/3)**", "com_302"))
                        list.append(("    Al-'Asr , Makkah  **3 (1/3)**", "com_303"))
                        list.append(("    Al-Humazah , Makkah  **9 (1/3)**", "com_304"))
                        list.append(("    Al-Feel , Makkah  **5 (1/3)**", "com_305"))
                        list.append(("    Quraish , Makkah  **4 (1/3)**", "com_306"))
                        list.append(("    Al-Maa'oon , Makkah  **7 (1/3)**", "com_307"))
                        list.append(("    Al-Kawthar , Makkah  **3 (1/3)**", "com_308"))
                        list.append(("    Al-Kaafiroon , Makkah  **6 (1/3)**", "com_309"))
                        list.append(("    An-Nasr , Madinah  **3 (1/3)**", "com_310"))
                        list.append(("    Al-Masad , Makkah  **5 (1/3)**", "com_311"))
                        list.append(("    Al-Ikhlas , Makkah  **4 (1/3)**", "com_312"))
                        list.append(("    Al-Falaq , Makkah  **5 (1/3)**", "com_313"))
                        list.append(("    An-Naas , Makkah  **6 (1/3)**", "com_314"))
                        list.append(("    Full Tilawa", "com_315"))                        
                        list.append(("    Doa Khatam Quran", "com_316"))
                        list.append(("    Doa Khatam Quran", "com_317"))
                        list.append(("    Doa Khatam Quran", "com_318"))                
                        list.append(("    Doa Khatam Quran", "com_319"))
                        list.append(("    Doa Khatam Quran", "com_320"))
                        list.append(("    Doa Khatam Quran", "com_321"))                
                        list.append(("    Doa Khatam Quran 1409", "com_322"))
                        list.append(("    Part of ama Doa Khatam Quran 1414", "com_323"))
                        list.append(("    Doa Khatam Quran for the night of 27 Ramadan 1423", "com_324"))
                        list.append(("    Doa Khatam Quran", "com_325"))  
                elif config.plugins.FreeServerminoo.lang.value == "FR":
                        list.append(("    Saud_Alshuraim", "com_01"))                         
                        list.append(("    LIVE 13", "com_02"))
                        list.append(("    LIVE 14", "com_03"))  
                        list.append(("    LIVE 16", "com_04"))
                        list.append(("    The Voice of Ummah", "com_05")) 
                        list.append(("    Al-Kahf", "com_06"))
                        list.append(("    Caire", "com_1"))                         
                        list.append(("    Arabie Saoudite", "com_2"))
                        list.append(("    Algérie", "com_3"))  
                        list.append(("    Maroc", "com_4"))
                        list.append(("    EAU", "com_5")) 
                        list.append(("    San Francisco", "com_6"))
                        list.append(("    Nour Ala Nour", "com_7"))             
                        list.append(("    Washington", "com_8"))
                        list.append(("    Live 1", "com_9"))          
                        list.append(("    Live 2", "com_10"))                        
                        list.append(("    Live 3", "com_11"))
                        list.append(("    Live 4", "com_12"))
                        list.append(("    Live 5", "com_13"))                
                        list.append(("    Ashams", "com_14"))
                        list.append(("    Chaarawi", "com_15"))
                        list.append(("    Maka", "com_16"))
                        list.append(("    Ahl Al Quran", "com_17"))
                        list.append(("    UK", "com_18"))
                        list.append(("    Naplouse", "com_19"))
                        list.append(("    Spain", "com_20"))
                        list.append(("    Buzzislam", "com_21"))
                        list.append(("    Australia", "com_22"))
                        list.append(("    Dawn", "com_23"))                
                        list.append(("    Crescent", "com_24"))
                        list.append(("    Al Manshuroh", "com_25"))
                        list.append(("    Rodja", "com_26"))
                        list.append(("    Lebanon", "com_27"))
                        list.append(("    Live 6", "com_28"))
                        list.append(("    New York", "com_29"))
                        list.append(("    San Francisco 2", "com_30"))
                        list.append(("    San Francisco 3", "com_31"))
                        list.append(("    Live 7", "com_32"))
                        list.append(("    Verse 24", "com_33"))
                        list.append(("    Nouvelle-Galles du Sud , Sydney", "com_34"))
                        list.append(("    Kandahar", "com_35"))
                        list.append(("    Beyrouth", "com_36"))
                        list.append(("    Abou Dabi", "com_37"))
                        list.append(("    Hanoi", "com_38")) 
                        list.append(("    Sharjah", "com_39"))    
                        list.append(("    Khartoum", "com_40"))
                        list.append(("    Dusseldorf", "com_41"))
                        list.append(("    San Francisco 4", "com_42"))
                        list.append(("    Berlin", "com_43"))
                        list.append(("    New Jersey", "com_44"))
                        list.append(("    District de Columbia", "com_45"))
                        list.append(("    Saint Gall", "com_46"))
                        list.append(("    Bandung", "com_47"))
                        list.append(("    Istanbul", "com_48"))
                        list.append(("    Victoria", "com_49"))
                        list.append(("    Ankara", "com_50"))
                        list.append(("    Maka", "com_51"))
                        list.append(("    Abidjan", "com_52"))
                        list.append(("    Miraath's", "com_53"))
                        list.append(("    Birmingham", "com_54"))
                        list.append(("    Tirana", "com_55"))
                        list.append(("    National Capital Region, Capitol", "com_56"))
                        list.append(("    Adwaa", "com_57"))
                        list.append(("    Adwaa 2", "com_58")) 
                        list.append(("    San Francisco", "com_59"))
                        list.append(("    Java occidental", "com_60"))             
                        list.append(("    Tunis", "com_61"))
                        list.append(("    Ankara", "com_62"))          
                        list.append(("    Hayat", "com_63"))                        
                        list.append(("    Paris", "com_64"))
                        list.append(("    Kayseri", "com_65"))
                        list.append(("    Manama", "com_66"))                
                        list.append(("    Antalya", "com_67"))
                        list.append(("    Dakar", "com_68"))
                        list.append(("    Tripoli", "com_69"))
                        list.append(("    Gaza", "com_70"))
                        list.append(("    District de Columbia, Washington", "com_71"))
                        list.append(("    Tripoli 2", "com_72"))
                        list.append(("    Sirius", "com_73"))
                        list.append(("    Alsiyada", "com_74"))
                        list.append(("    Berlin", "com_75"))
                        list.append(("    New Jersey, Union City", "com_76"))                
                        list.append(("    Omdourman", "com_77"))
                        list.append(("    Copenhague", "com_78"))
                        list.append(("    Koweit", "com_79"))
                        list.append(("    Kampala", "com_80"))
                        list.append(("    Region metropolitaine de Santiago", "com_81"))
                        list.append(("    Rio de Janeiro", "com_82"))
                        list.append(("    Khartoum", "com_83"))
                        list.append(("    Baburrohmah", "com_84"))
                        list.append(("    Rabat", "com_85"))
                        list.append(("    Beyrouth", "com_86"))
                        list.append(("    Londres", "com_87"))
                        list.append(("    Birmingham", "com_88"))
                        list.append(("    Sydney", "com_89"))
                        list.append(("    Sunnah", "com_90"))
                        list.append(("    Amman", "com_91")) 
                        list.append(("    Birlik", "com_92"))    
                        list.append(("    District de Columbia, Washington", "com_93"))
                        list.append(("    Cisjordanie", "com_94"))
                        list.append(("    Manchester", "com_95"))
                        list.append(("    Berlin", "com_96"))
                        list.append(("    New Jersey", "com_97"))
                        list.append(("    Jakarta", "com_98"))
                        list.append(("    Sabeel Al Anbiyya", "com_99"))
                        list.append(("    Eman City", "com_100"))
                        list.append(("    Caroline du Nord , Durham", "com_101"))    
                        list.append(("    Australie-Occidentale , Perth", "com_102"))
                        list.append(("    Angleterre , Leicester", "com_103"))
                        list.append(("    Hesse , Cassel", "com_104"))
                        list.append(("    Centre , Singapour", "com_105"))
                        list.append(("    Al-Manshuroh", "com_106"))
                        list.append(("    Nouvelle-Galles du Sud , Sydney", "com_107"))
                        list.append(("    Bradford", "com_108"))
                        list.append(("    Nouvelle-Galles du Sud , Sydney", "com_109"))
                        list.append(("    Ile-de-France , Paris", "com_110"))
                        list.append(("    Miraath's", "com_111"))
                        list.append(("    Hayat", "com_112"))
                        list.append(("    Saint-Gall", "com_113"))
                        list.append(("    Ustikolina", "com_114"))
                        list.append(("    Berlin", "com_115"))
                        list.append(("    Vietnamese", "com_116"))
                        list.append(("    Albashaer", "com_117"))
                        list.append(("    RIM-Mayotte, M'Tsangamouji", "com_118")) 
                        list.append(("    Bass", "com_119"))
                        list.append(("    Hovedstaden", "com_120"))             
                        list.append(("    Mercan", "com_121"))
                        list.append(("    Chile", "com_122"))          
                        list.append(("    Bakel", "com_123"))                        
                        list.append(("    Nour", "com_124"))
                        list.append(("    Koweit", "com_125"))
                        list.append(("    Live 8", "com_126"))                
                        list.append(("    Live 9", "com_127"))
                        list.append(("    Live 10", "com_128"))
                        list.append(("    Live 11", "com_129"))
                        list.append(("    Live 12", "com_130"))
                        list.append(("    Nottingham", "com_131"))
                        list.append(("    Paris", "com_132"))
                        list.append(("    Australie-Occidentale , Perth", "com_133"))
                        list.append(("    Caroline du Nord , Durham", "com_134"))
                        list.append(("    Kalimantan oriental , Balikpapan", "com_135"))
                        list.append(("    Western , Colombo", "com_136"))                
                        list.append(("    Angleterre , Bolton", "com_137"))
                        list.append(("    Ramallah", "com_138"))
                        list.append(("    Java oriental , Kediri", "com_139"))
                        list.append(("    Mogadiscio", "com_140"))
                        list.append(("    Johannesbourg", "com_141"))
                        list.append(("    RIM-Mayotte", "com_142"))
                        list.append(("    Singapour", "com_143"))
                        list.append(("    Izmir", "com_144"))
                        list.append(("    Victoria, Melbourne", "com_145"))
                        list.append(("    Tirana", "com_146"))
                        list.append(("    Amman", "com_147"))
                        list.append(("    New York", "com_148"))
                        list.append(("    Muhammad Ayyoob - Surat Al-Baqara", "com_149"))
                        list.append(("    Fares Abbad - Surat Al-Baqara", "com_150"))
                        list.append(("    Java occidental, Tasikmalaya", "com_151"))
                        list.append(("    Mahmoud Khalil Al-Husary", "com_152")) 
                        list.append(("    Santiago, Nunoa", "com_153"))    
                        list.append(("    Nasser Alqatami Musshaf - Al-Furqan", "com_154"))
                        list.append(("    Abu Baker Al-Shatiri Musshaf - Ghafir", "com_155"))
                        list.append(("    Abdullah Ali Jabir - Surat An-Naml", "com_156"))
                        list.append(("    Yasser Al Dosari - 049-Al-Hujurat", "com_157"))
                        list.append(("    Hani ar-Rifai - Surat Al-Ankaboot", "com_158"))
                        list.append(("    Muhammad Jibreel - Surat Yunus", "com_159"))
                        list.append(("    Muhammad al-Luhaidan - Surat At-Tawba", "com_160"))
                        list.append(("    Mohammad Al-Tablaaway - Ash-Shura", "com_161"))
                        list.append(("    Khaalid Abdullaah al-Qahtaanee - 024", "com_162"))    
                        list.append(("    Mishaari Raashid al-Aafaasee - Surat Al-Araf", "com_163"))
                        list.append(("    Bakel", "com_164"))
                        list.append(("    Ahle el-Safa", "com_165"))
                        list.append(("    Abdulrahman Alsudaes - Al-Imran", "com_166"))
                        list.append(("    Fairfield", "com_167"))
                        list.append(("    Abdulbari Mohammad", "com_168"))
                        list.append(("    Abdul-Samad", "com_169"))
                        list.append(("    Al-Husary", "com_170"))
                        list.append(("    Paris", "com_171"))
                        list.append(("    Rayhan", "com_172"))
                        list.append(("    Masjid Live - Bolton", "com_173"))
                        list.append(("    Shurooq Ramadan", "com_174"))
                        list.append(("    Radio Moga", "com_175"))
                        list.append(("    Nour", "com_176"))
                        list.append(("    Cairo", "com_177"))
                        list.append(("    Mohammed_Siddiq_Alminshawi", "com_178")) 
                        list.append(("    Fi_Dilal_Alsiyra", "com_179"))
                        list.append(("    Alaikhtiarat_Alfiqhayha_Ben_Baz", "com_180"))             
                        list.append(("    France", "com_181"))
                        list.append(("    Live from Makkah", "com_182"))          
                        list.append(("    Heart", "com_183"))                        
                        list.append(("    Djedah", "com_184"))
                        list.append(("    Sydney", "com_185"))
                        list.append(("    Live 15", "com_186"))                
                        list.append(("    Java central, Cilacap", "com_187"))
                        list.append(("    Java oriental, Surabaya", "com_188"))
                        list.append(("    Kalmunai", "com_189"))
                        list.append(("    Abou Dabi", "com_190"))
                        list.append(("    Fares Abbad - Surat Maryam", "com_191"))
                        list.append(("    Muhammad Ayyoob - Quran - Surat Yusuf", "com_192"))
                        list.append(("    Mahmoud Khalil Al-Husary", "com_193"))                        
                        list.append(("    Gorontalo", "com_194"))
                        list.append(("    Nasser Alqatami- Al-Baqarah", "com_195"))
                        list.append(("    Abdullah Ali Jabir - Surat An-Nisa", "com_196"))                
                        list.append(("    Koweit", "com_197"))
                        list.append(("    Cisjordanie, Ramallah", "com_198"))
                        list.append(("    Barakath", "com_199"))
                        list.append(("    Makkah", "com_200"))
                        list.append(("    Al-Fatihah , Makkah  **7 (1)**", "com_201"))    
                        list.append(("    Al-Baqarah , Madinah  **286 (40)**", "com_202"))
                        list.append(("    Aali 'Imran , Madinah  **200 (20)**", "com_203"))
                        list.append(("    An-Nisa , Madinah  **176 (24)**", "com_204"))
                        list.append(("    Al-Ma'idah , Madinah  **120 (16)**", "com_205"))
                        list.append(("    Al-An'am , Makkah  **165 (20)**", "com_206"))
                        list.append(("    Al-A'raf , Makkah  **206 (24)**", "com_207"))
                        list.append(("    Al-Anfal , Madinah  **75 (10)**", "com_208"))
                        list.append(("    At-Tawbah , Madinah  **129 (16)**", "com_209"))
                        list.append(("    Yunus , Makkah  **109 (11)**", "com_210"))
                        list.append(("    Hud , Makkah  **123 (10)**", "com_211"))
                        list.append(("    Yusuf , Makkah  **111 (12)**", "com_212"))
                        list.append(("    Ar-Ra'd , Madinah  **743 (6)**", "com_213"))
                        list.append(("    Ibrahim , Makkah  **52 (7)**", "com_214"))
                        list.append(("    Al-Hijr , Makkah  **99 (6)**", "com_215"))
                        list.append(("    An-Nahl , Makkah  **128 (16)**", "com_216"))
                        list.append(("    Al-Isra , Makkah  **111 (12)**", "com_217"))
                        list.append(("    Al-Kahf , Makkah  **110 (12)**", "com_218")) 
                        list.append(("    Maryam , Makkah  **98 (6)**", "com_219"))
                        list.append(("    Ta-Ha , Makkah  **135 (8)**", "com_220"))             
                        list.append(("    Al-Anbiya , Makkah  **112 (7)**", "com_221"))
                        list.append(("    Al-Hajj , Madinah  **78 (10)**", "com_222"))          
                        list.append(("    Al-Mu'minun , Makkah  **118 (6)**", "com_223"))                        
                        list.append(("    An-Nur , Madinah  **64 (9)**", "com_224"))
                        list.append(("    Al-Furqan , Makkah  **77 (6)**", "com_225"))
                        list.append(("    Ash-Shu'ara , Makkah  **227 (11)**", "com_226"))                
                        list.append(("    An-Naml , Makkah  **93 (7)**", "com_227"))
                        list.append(("    Al-Qasas , Makkah  **88 (9)**", "com_228"))
                        list.append(("    Al-Ankabut , Makkah  **69 (7)**", "com_229"))
                        list.append(("    Ar-Rum , Makkah  **60 (6)**", "com_230"))
                        list.append(("    Luqmaan , Makkah  **34 (4)**", "com_231"))
                        list.append(("    As-Sajdah , Makkah  **30 (3)**", "com_232"))
                        list.append(("    Al-Ahzaab , Madinah  **73 (9)**", "com_233"))
                        list.append(("    Saba , Makkah  **54 (6)**", "com_234"))
                        list.append(("    Faatir , Makkah  **45 (5)**", "com_235"))
                        list.append(("    Ya-Sin , Makkah  **83 (5)**", "com_236"))                
                        list.append(("    As-Saaffaat , Makkah  **182 (5)**", "com_237"))
                        list.append(("    Saad , Makkah  **88 (5)**", "com_238"))
                        list.append(("    Az-Zumar , Makkah  **75 (8)**", "com_239"))
                        list.append(("    Ghafir , Makkah  **85 (9)**", "com_240"))
                        list.append(("    Fussilat , Makkah  **54 (6)**", "com_241"))
                        list.append(("    Ash-Shura , Makkah  **53 (5)**", "com_242"))
                        list.append(("    Az-Zukhruf , Makkah  **89 (7)**", "com_243"))
                        list.append(("    Ad-Dukhaan , Makkah  **59 (3)**", "com_244"))
                        list.append(("    Al-Jaathiyah , Makkah  **37 (4)**", "com_245"))
                        list.append(("    Al-Ahqaaf , Makkah  **35 (4 1/2)**", "com_246"))
                        list.append(("    Muhammad , Madinah  **38 (4)**", "com_247"))
                        list.append(("    Al-Fath , Madinah  **29 (4 1/2)**", "com_148"))
                        list.append(("    Al-Hujuraat , Madinah  **18 (2 1/2)**", "com_249"))
                        list.append(("    Qaaf , Makkah  **45 (3)**", "com_250"))
                        list.append(("    Adh-Dhaariyaat , Makkah  **60 (2 1/2)**", "com_251"))
                        list.append(("    At-Toor , Makkah  **49 (2 1/2)**", "com_252")) 
                        list.append(("    An-Najm , Makkah  **62 (2 1/2)**", "com_253"))    
                        list.append(("    Al-Qamar , Makkah  **55 (2 1/2)**", "com_254"))
                        list.append(("    Ar-Rahman , Makkah  **78 (3)**", "com_255"))
                        list.append(("    Al-Waqi'ah , Makkah  **96 (3 1/2)**", "com_256"))
                        list.append(("    Al-Hadeed , Madinah  **29 (4)**", "com_257"))
                        list.append(("    Al-Mujadila , Madinah  **22 (3 1/2)**", "com_258"))
                        list.append(("    Al-Hashr , Madinah  **24 (3 1/2)**", "com_259"))
                        list.append(("    Al-Mumtahanah , Madinah  **13 (2 1/2)**", "com_260"))
                        list.append(("    As-Saff , Madinah  **14 (1 1/2)**", "com_261"))
                        list.append(("    Al-Jumu'ah , Madinah  **11 (1 1/2)**", "com_262"))    
                        list.append(("    Al-Munafiqoon , Madinah  **11 (1 1/2)**", "com_263"))
                        list.append(("    At-Taghabun , Madinah  **18 (2)**", "com_264"))
                        list.append(("    At-Talaq , Madinah  **12 (2)**", "com_265"))
                        list.append(("    At-Tahreem , Madinah  **12 (2)**", "com_266"))
                        list.append(("    Al-Mulk , Makkah  **30 (1 1/2)**", "com_267"))
                        list.append(("    Al-Qalam , Makkah  **52 (2)**", "com_268"))
                        list.append(("    Al-Haaqqa , Makkah  **52 (2)**", "com_269"))
                        list.append(("    Al-Ma'aarij , Makkah  **44 (1 1/2)**", "com_270"))
                        list.append(("    Nuh , Makkah  **28 (1 1/2)**", "com_271"))
                        list.append(("    Al-Jinn , Makkah  **28 (2)**", "com_272"))
                        list.append(("    Al-Muzzammil , Makkah  **20 (1 1/2)**", "com_273"))
                        list.append(("    Al-Muddaththir , Makkah  **56 (2)**", "com_274"))
                        list.append(("    Al-Qiyamah , Makkah  **40 (1)**", "com_275"))
                        list.append(("    Al-Insaan , Madinah  **31 (2)**", "com_276"))
                        list.append(("    Al-Mursalaat , Makkah  **50 (1 1/2)**", "com_277"))
                        list.append(("    An-Naba' , Makkah  **40 (1 1/2)**", "com_278")) 
                        list.append(("    An-Naazi'aat , Makkah  **46 (1 1/2)**", "com_279"))
                        list.append(("    Abasa , Makkah  **42 (1)**", "com_280"))             
                        list.append(("    At-Takweer , Makkah  **29 (1)**", "com_181"))
                        list.append(("    Al-Infitar , Makkah  **19 (1/2)**", "com_282"))          
                        list.append(("    Al-Mutaffifeen , Makkah  **36 (1)**", "com_283"))                        
                        list.append(("    Al-Inshiqaaq , Makkah  **25 (1)**", "com_284"))
                        list.append(("    Al-Burooj , Makkah  **22 (1)**", "com_285"))
                        list.append(("    At-Taariq , Makkah  **17 (1/2)**", "com_286"))                
                        list.append(("    Al-A'la , Makkah  **19 (1/2)**", "com_287"))
                        list.append(("    Al-Ghaashiyah , Makkah  **26 (1)**", "com_288"))
                        list.append(("    Al-Fajr , Makkah  **30 (1)**", "com_289"))
                        list.append(("    Al-Balad , Makkah  **20 (1/2)**", "com_190"))
                        list.append(("    Ash-Shams , Makkah  **15 (1/2)**", "com_291"))
                        list.append(("    Al-Layl , Makkah  **21 (1/2)**", "com_292"))
                        list.append(("    Ad-Dhuha , Makkah  **11 (1/2)**", "com_293"))                        
                        list.append(("    Ash-Sharh , Makkah  **8 (1/3)**", "com_294"))
                        list.append(("    At-Tin , Makkah  **8 (1/3)**", "com_295"))
                        list.append(("    Al-Alaq , Makkah  **19 (1/2)**", "com_296"))                
                        list.append(("    Al-Qadr , Makkah  **5 (1/3)**", "com_297"))
                        list.append(("    Al-Bayyinah , Madinah  **8 (1)**", "com_298"))
                        list.append(("    Az-Zalzalah , Madinah  **8 (1/3)**", "com_299"))
                        list.append(("    Al-'Aadiyat , Makkah  **11 (1/3)**", "com_300"))
                        list.append(("    Al-Qaari'ah , Makkah  **11 (1/3)**", "com_301"))
                        list.append(("    At-Takaathur , Makkah  **8 (1/3)**", "com_302"))
                        list.append(("    Al-'Asr , Makkah  **3 (1/3)**", "com_303"))
                        list.append(("    Al-Humazah , Makkah  **9 (1/3)**", "com_304"))
                        list.append(("    Al-Feel , Makkah  **5 (1/3)**", "com_305"))
                        list.append(("    Quraish , Makkah  **4 (1/3)**", "com_306"))
                        list.append(("    Al-Maa'oon , Makkah  **7 (1/3)**", "com_307"))
                        list.append(("    Al-Kawthar , Makkah  **3 (1/3)**", "com_308"))
                        list.append(("    Al-Kaafiroon , Makkah  **6 (1/3)**", "com_309"))
                        list.append(("    An-Nasr , Madinah  **3 (1/3)**", "com_310"))
                        list.append(("    Al-Masad , Makkah  **5 (1/3)**", "com_311"))
                        list.append(("    Al-Ikhlas , Makkah  **4 (1/3)**", "com_312"))
                        list.append(("    Al-Falaq , Makkah  **5 (1/3)**", "com_313"))
                        list.append(("    An-Naas , Makkah  **6 (1/3)**", "com_314")) 
                        list.append(("    Full Tilawa", "com_315"))                        
                        list.append(("    Doa Khatam Quran", "com_316"))
                        list.append(("    Doa Khatam Quran", "com_317"))
                        list.append(("    Doa Khatam Quran", "com_318"))                
                        list.append(("    Doa Khatam Quran", "com_319"))
                        list.append(("    Doa Khatam Quran", "com_320"))
                        list.append(("    Doa Khatam Quran", "com_321"))                
                        list.append(("    Doa Khatam Quran 1409", "com_322"))
                        list.append(("    Part of ama Doa Khatam Quran 1414", "com_323"))
                        list.append(("    Doa Khatam Quran for the night of 27 Ramadan 1423", "com_324"))
                        list.append(("    Doa Khatam Quran", "com_325"))                        
                else:
                        list.append(("    Saud_Alshuraim", "com_01"))                         
                        list.append(("    LIVE 13", "com_02"))
                        list.append(("    LIVE 14", "com_03"))  
                        list.append(("    LIVE 16", "com_04"))
                        list.append(("    The Voice of Ummah", "com_05")) 
                        list.append(("    Al-Kahf", "com_06"))
                        list.append(("    Qahira", "com_1"))                         
                        list.append(("    KSA", "com_2"))
                        list.append(("    Algeria", "com_3"))  
                        list.append(("    Morocco", "com_4"))
                        list.append(("    EAU", "com_5")) 
                        list.append(("    San Francisco", "com_6"))
                        list.append(("    Nour Ala Nour", "com_7"))             
                        list.append(("    Washington", "com_8"))
                        list.append(("    Live 1", "com_9"))          
                        list.append(("    Live 2", "com_10"))                        
                        list.append(("    Live 3", "com_11"))
                        list.append(("    Live 4", "com_12"))
                        list.append(("    Live 5", "com_13"))                
                        list.append(("    Ashams", "com_14"))
                        list.append(("    Chaarawi", "com_15"))
                        list.append(("    Maka", "com_16"))
                        list.append(("    Ahl Al Quran", "com_17"))
                        list.append(("    UK", "com_18"))
                        list.append(("    Naplouse", "com_19"))
                        list.append(("    Spain", "com_20"))
                        list.append(("    Buzzislam", "com_21"))
                        list.append(("    Australia", "com_22"))
                        list.append(("    Dawn", "com_23"))                
                        list.append(("    Crescent", "com_24"))
                        list.append(("    Al Manshuroh", "com_25"))
                        list.append(("    Rodja", "com_26"))
                        list.append(("    Lebanon", "com_27"))
                        list.append(("    Live 6", "com_28"))
                        list.append(("    New York", "com_29"))
                        list.append(("    San Francisco 2", "com_30"))
                        list.append(("    San Francisco 3", "com_31"))
                        list.append(("    Live 7", "com_32"))
                        list.append(("    Verse 24", "com_33"))
                        list.append(("    Nouvelle-Galles du Sud , Sydney", "com_34"))
                        list.append(("    Kandahar", "com_35"))
                        list.append(("    Beyrouth", "com_36"))
                        list.append(("    Abou Dabi", "com_37"))
                        list.append(("    Hanoi", "com_38")) 
                        list.append(("    Sharjah", "com_39"))    
                        list.append(("    Khartoum", "com_40"))
                        list.append(("    Dusseldorf", "com_41"))
                        list.append(("    San Francisco 4", "com_42"))
                        list.append(("    Berlin", "com_43"))
                        list.append(("    New Jersey", "com_44"))
                        list.append(("    District de Columbia", "com_45"))
                        list.append(("    Saint Gall", "com_46"))
                        list.append(("    Bandung", "com_47"))
                        list.append(("    Istanbul", "com_48"))
                        list.append(("    Victoria", "com_49"))
                        list.append(("    Ankara", "com_50"))
                        list.append(("    Maka", "com_51"))
                        list.append(("    Abidjan", "com_52"))
                        list.append(("    Miraath's", "com_53"))
                        list.append(("    Birmingham", "com_54"))
                        list.append(("    Tirana", "com_55"))
                        list.append(("    National Capital Region, Capitol", "com_56"))
                        list.append(("    Adwaa", "com_57"))
                        list.append(("    Adwaa 2", "com_58")) 
                        list.append(("    San Francisco", "com_59"))
                        list.append(("    Java occidental", "com_60"))             
                        list.append(("    Tunis", "com_61"))
                        list.append(("    Ankara", "com_62"))          
                        list.append(("    Hayat", "com_63"))                        
                        list.append(("    Paris", "com_64"))
                        list.append(("    Kayseri", "com_65"))
                        list.append(("    Manama", "com_66"))                
                        list.append(("    Antalya", "com_67"))
                        list.append(("    Dakar", "com_68"))
                        list.append(("    Tripoli", "com_69"))
                        list.append(("    Gaza", "com_70"))
                        list.append(("    District de Columbia, Washington", "com_71"))
                        list.append(("    Tripoli 2", "com_72"))
                        list.append(("    Sirius", "com_73"))
                        list.append(("    Alsiyada", "com_74"))
                        list.append(("    Berlin", "com_75"))
                        list.append(("    New Jersey, Union City", "com_76"))                
                        list.append(("    Omdourman", "com_77"))
                        list.append(("    Copenhague", "com_78"))
                        list.append(("    Koweit", "com_79"))
                        list.append(("    Kampala", "com_80"))
                        list.append(("    Region metropolitaine de Santiago", "com_81"))
                        list.append(("    Rio de Janeiro", "com_82"))
                        list.append(("    Khartoum", "com_83"))
                        list.append(("    Baburrohmah", "com_84"))
                        list.append(("    Rabat", "com_85"))
                        list.append(("    Beyrouth", "com_86"))
                        list.append(("    Londres", "com_87"))
                        list.append(("    Birmingham", "com_88"))
                        list.append(("    Sydney", "com_89"))
                        list.append(("    Sunnah", "com_90"))
                        list.append(("    Amman", "com_91")) 
                        list.append(("    Birlik", "com_92"))    
                        list.append(("    District de Columbia, Washington", "com_93"))
                        list.append(("    Cisjordanie", "com_94"))
                        list.append(("    Manchester", "com_95"))
                        list.append(("    Berlin", "com_96"))
                        list.append(("    New Jersey", "com_97"))
                        list.append(("    Jakarta", "com_98"))
                        list.append(("    Sabeel Al Anbiyya", "com_99"))
                        list.append(("    Eman City", "com_100"))
                        list.append(("    Caroline du Nord , Durham", "com_101"))    
                        list.append(("    Australie-Occidentale , Perth", "com_102"))
                        list.append(("    Angleterre , Leicester", "com_103"))
                        list.append(("    Hesse , Cassel", "com_104"))
                        list.append(("    Centre , Singapour", "com_105"))
                        list.append(("    Al-Manshuroh", "com_106"))
                        list.append(("    Nouvelle-Galles du Sud , Sydney", "com_107"))
                        list.append(("    Bradford", "com_108"))
                        list.append(("    Nouvelle-Galles du Sud , Sydney", "com_109"))
                        list.append(("    Ile-de-France , Paris", "com_110"))
                        list.append(("    Miraath's", "com_111"))
                        list.append(("    Hayat", "com_112"))
                        list.append(("    Saint-Gall", "com_113"))
                        list.append(("    Ustikolina", "com_114"))
                        list.append(("    Berlin", "com_115"))
                        list.append(("    Vietnamese", "com_116"))
                        list.append(("    Albashaer", "com_117"))
                        list.append(("    RIM-Mayotte, M'Tsangamouji", "com_118")) 
                        list.append(("    Bass", "com_119"))
                        list.append(("    Hovedstaden", "com_120"))             
                        list.append(("    Mercan", "com_121"))
                        list.append(("    Chile", "com_122"))          
                        list.append(("    Bakel", "com_123"))                        
                        list.append(("    Nour", "com_124"))
                        list.append(("    Koweit", "com_125"))
                        list.append(("    Live 8", "com_126"))                
                        list.append(("    Live 9", "com_127"))
                        list.append(("    Live 10", "com_128"))
                        list.append(("    Live 11", "com_129"))
                        list.append(("    Live 12", "com_130"))
                        list.append(("    Nottingham", "com_131"))
                        list.append(("    Paris", "com_132"))
                        list.append(("    Australie-Occidentale , Perth", "com_133"))
                        list.append(("    Caroline du Nord , Durham", "com_134"))
                        list.append(("    Kalimantan oriental , Balikpapan", "com_135"))
                        list.append(("    Western , Colombo", "com_136"))                
                        list.append(("    Angleterre , Bolton", "com_137"))
                        list.append(("    Ramallah", "com_138"))
                        list.append(("    Java oriental , Kediri", "com_139"))
                        list.append(("    Mogadiscio", "com_140"))
                        list.append(("    Johannesbourg", "com_141"))
                        list.append(("    RIM-Mayotte", "com_142"))
                        list.append(("    Singapour", "com_143"))
                        list.append(("    Izmir", "com_144"))
                        list.append(("    Victoria, Melbourne", "com_145"))
                        list.append(("    Tirana", "com_146"))
                        list.append(("    Amman", "com_147"))
                        list.append(("    New York", "com_148"))
                        list.append(("    Muhammad Ayyoob - Surat Al-Baqara", "com_149"))
                        list.append(("    Fares Abbad - Surat Al-Baqara", "com_150"))
                        list.append(("    Java occidental, Tasikmalaya", "com_151"))
                        list.append(("    Mahmoud Khalil Al-Husary", "com_152")) 
                        list.append(("    Santiago, Nunoa", "com_153"))    
                        list.append(("    Nasser Alqatami Musshaf - Al-Furqan", "com_154"))
                        list.append(("    Abu Baker Al-Shatiri Musshaf - Ghafir", "com_155"))
                        list.append(("    Abdullah Ali Jabir - Surat An-Naml", "com_156"))
                        list.append(("    Yasser Al Dosari - 049-Al-Hujurat", "com_157"))
                        list.append(("    Hani ar-Rifai - Surat Al-Ankaboot", "com_158"))
                        list.append(("    Muhammad Jibreel - Surat Yunus", "com_159"))
                        list.append(("    Muhammad al-Luhaidan - Surat At-Tawba", "com_160"))
                        list.append(("    Mohammad Al-Tablaaway - Ash-Shura", "com_161"))
                        list.append(("    Khaalid Abdullaah al-Qahtaanee - 024", "com_162"))    
                        list.append(("    Mishaari Raashid al-Aafaasee - Surat Al-Araf", "com_163"))
                        list.append(("    Bakel", "com_164"))
                        list.append(("    Ahle el-Safa", "com_165"))
                        list.append(("    Abdulrahman Alsudaes - Al-Imran", "com_166"))
                        list.append(("    Fairfield", "com_167"))
                        list.append(("    Abdulbari Mohammad", "com_168"))
                        list.append(("    Abdul-Samad", "com_169"))
                        list.append(("    Al-Husary", "com_170"))
                        list.append(("    Paris", "com_171"))
                        list.append(("    Rayhan", "com_172"))
                        list.append(("    Masjid Live - Bolton", "com_173"))
                        list.append(("    Shurooq Ramadan", "com_174"))
                        list.append(("    Radio Moga", "com_175"))
                        list.append(("    Nour", "com_176"))
                        list.append(("    Cairo", "com_177"))
                        list.append(("    Mohammed_Siddiq_Alminshawi", "com_178")) 
                        list.append(("    Fi_Dilal_Alsiyra", "com_179"))
                        list.append(("    Alaikhtiarat_Alfiqhayha_Ben_Baz", "com_180"))             
                        list.append(("    France", "com_181"))
                        list.append(("    Live from Makkah", "com_182"))          
                        list.append(("    Heart", "com_183"))                        
                        list.append(("    Djedah", "com_184"))
                        list.append(("    Sydney", "com_185"))
                        list.append(("    Live 15", "com_186"))                
                        list.append(("    Java central, Cilacap", "com_187"))
                        list.append(("    Java oriental, Surabaya", "com_188"))
                        list.append(("    Kalmunai", "com_189"))
                        list.append(("    Abou Dabi", "com_190"))
                        list.append(("    Fares Abbad - Surat Maryam", "com_191"))
                        list.append(("    Muhammad Ayyoob - Quran - Surat Yusuf", "com_192"))
                        list.append(("    Mahmoud Khalil Al-Husary", "com_193"))                        
                        list.append(("    Gorontalo", "com_194"))
                        list.append(("    Nasser Alqatami- Al-Baqarah", "com_195"))
                        list.append(("    Abdullah Ali Jabir - Surat An-Nisa", "com_196"))                
                        list.append(("    Koweit", "com_197"))
                        list.append(("    Cisjordanie, Ramallah", "com_198"))
                        list.append(("    Barakath", "com_199"))
                        list.append(("    Makkah", "com_200"))
                        list.append(("    Al-Fatihah , Makkah  **7 (1)**", "com_201"))    
                        list.append(("    Al-Baqarah , Madinah  **286 (40)**", "com_202"))
                        list.append(("    Aali 'Imran , Madinah  **200 (20)**", "com_203"))
                        list.append(("    An-Nisa , Madinah  **176 (24)**", "com_204"))
                        list.append(("    Al-Ma'idah , Madinah  **120 (16)**", "com_205"))
                        list.append(("    Al-An'am , Makkah  **165 (20)**", "com_206"))
                        list.append(("    Al-A'raf , Makkah  **206 (24)**", "com_207"))
                        list.append(("    Al-Anfal , Madinah  **75 (10)**", "com_208"))
                        list.append(("    At-Tawbah , Madinah  **129 (16)**", "com_209"))
                        list.append(("    Yunus , Makkah  **109 (11)**", "com_210"))
                        list.append(("    Hud , Makkah  **123 (10)**", "com_211"))
                        list.append(("    Yusuf , Makkah  **111 (12)**", "com_212"))
                        list.append(("    Ar-Ra'd , Madinah  **743 (6)**", "com_213"))
                        list.append(("    Ibrahim , Makkah  **52 (7)**", "com_214"))
                        list.append(("    Al-Hijr , Makkah  **99 (6)**", "com_215"))
                        list.append(("    An-Nahl , Makkah  **128 (16)**", "com_216"))
                        list.append(("    Al-Isra , Makkah  **111 (12)**", "com_217"))
                        list.append(("    Al-Kahf , Makkah  **110 (12)**", "com_218")) 
                        list.append(("    Maryam , Makkah  **98 (6)**", "com_219"))
                        list.append(("    Ta-Ha , Makkah  **135 (8)**", "com_220"))             
                        list.append(("    Al-Anbiya , Makkah  **112 (7)**", "com_221"))
                        list.append(("    Al-Hajj , Madinah  **78 (10)**", "com_222"))          
                        list.append(("    Al-Mu'minun , Makkah  **118 (6)**", "com_223"))                        
                        list.append(("    An-Nur , Madinah  **64 (9)**", "com_224"))
                        list.append(("    Al-Furqan , Makkah  **77 (6)**", "com_225"))
                        list.append(("    Ash-Shu'ara , Makkah  **227 (11)**", "com_226"))                
                        list.append(("    An-Naml , Makkah  **93 (7)**", "com_227"))
                        list.append(("    Al-Qasas , Makkah  **88 (9)**", "com_228"))
                        list.append(("    Al-Ankabut , Makkah  **69 (7)**", "com_229"))
                        list.append(("    Ar-Rum , Makkah  **60 (6)**", "com_230"))
                        list.append(("    Luqmaan , Makkah  **34 (4)**", "com_231"))
                        list.append(("    As-Sajdah , Makkah  **30 (3)**", "com_232"))
                        list.append(("    Al-Ahzaab , Madinah  **73 (9)**", "com_233"))
                        list.append(("    Saba , Makkah  **54 (6)**", "com_234"))
                        list.append(("    Faatir , Makkah  **45 (5)**", "com_235"))
                        list.append(("    Ya-Sin , Makkah  **83 (5)**", "com_236"))                
                        list.append(("    As-Saaffaat , Makkah  **182 (5)**", "com_237"))
                        list.append(("    Saad , Makkah  **88 (5)**", "com_238"))
                        list.append(("    Az-Zumar , Makkah  **75 (8)**", "com_239"))
                        list.append(("    Ghafir , Makkah  **85 (9)**", "com_240"))
                        list.append(("    Fussilat , Makkah  **54 (6)**", "com_241"))
                        list.append(("    Ash-Shura , Makkah  **53 (5)**", "com_242"))
                        list.append(("    Az-Zukhruf , Makkah  **89 (7)**", "com_243"))
                        list.append(("    Ad-Dukhaan , Makkah  **59 (3)**", "com_244"))
                        list.append(("    Al-Jaathiyah , Makkah  **37 (4)**", "com_245"))
                        list.append(("    Al-Ahqaaf , Makkah  **35 (4 1/2)**", "com_246"))
                        list.append(("    Muhammad , Madinah  **38 (4)**", "com_247"))
                        list.append(("    Al-Fath , Madinah  **29 (4 1/2)**", "com_148"))
                        list.append(("    Al-Hujuraat , Madinah  **18 (2 1/2)**", "com_249"))
                        list.append(("    Qaaf , Makkah  **45 (3)**", "com_250"))
                        list.append(("    Adh-Dhaariyaat , Makkah  **60 (2 1/2)**", "com_251"))
                        list.append(("    At-Toor , Makkah  **49 (2 1/2)**", "com_252")) 
                        list.append(("    An-Najm , Makkah  **62 (2 1/2)**", "com_253"))    
                        list.append(("    Al-Qamar , Makkah  **55 (2 1/2)**", "com_254"))
                        list.append(("    Ar-Rahman , Makkah  **78 (3)**", "com_255"))
                        list.append(("    Al-Waqi'ah , Makkah  **96 (3 1/2)**", "com_256"))
                        list.append(("    Al-Hadeed , Madinah  **29 (4)**", "com_257"))
                        list.append(("    Al-Mujadila , Madinah  **22 (3 1/2)**", "com_258"))
                        list.append(("    Al-Hashr , Madinah  **24 (3 1/2)**", "com_259"))
                        list.append(("    Al-Mumtahanah , Madinah  **13 (2 1/2)**", "com_260"))
                        list.append(("    As-Saff , Madinah  **14 (1 1/2)**", "com_261"))
                        list.append(("    Al-Jumu'ah , Madinah  **11 (1 1/2)**", "com_262"))    
                        list.append(("    Al-Munafiqoon , Madinah  **11 (1 1/2)**", "com_263"))
                        list.append(("    At-Taghabun , Madinah  **18 (2)**", "com_264"))
                        list.append(("    At-Talaq , Madinah  **12 (2)**", "com_265"))
                        list.append(("    At-Tahreem , Madinah  **12 (2)**", "com_266"))
                        list.append(("    Al-Mulk , Makkah  **30 (1 1/2)**", "com_267"))
                        list.append(("    Al-Qalam , Makkah  **52 (2)**", "com_268"))
                        list.append(("    Al-Haaqqa , Makkah  **52 (2)**", "com_269"))
                        list.append(("    Al-Ma'aarij , Makkah  **44 (1 1/2)**", "com_270"))
                        list.append(("    Nuh , Makkah  **28 (1 1/2)**", "com_271"))
                        list.append(("    Al-Jinn , Makkah  **28 (2)**", "com_272"))
                        list.append(("    Al-Muzzammil , Makkah  **20 (1 1/2)**", "com_273"))
                        list.append(("    Al-Muddaththir , Makkah  **56 (2)**", "com_274"))
                        list.append(("    Al-Qiyamah , Makkah  **40 (1)**", "com_275"))
                        list.append(("    Al-Insaan , Madinah  **31 (2)**", "com_276"))
                        list.append(("    Al-Mursalaat , Makkah  **50 (1 1/2)**", "com_277"))
                        list.append(("    An-Naba' , Makkah  **40 (1 1/2)**", "com_278")) 
                        list.append(("    An-Naazi'aat , Makkah  **46 (1 1/2)**", "com_279"))
                        list.append(("    Abasa , Makkah  **42 (1)**", "com_280"))             
                        list.append(("    At-Takweer , Makkah  **29 (1)**", "com_181"))
                        list.append(("    Al-Infitar , Makkah  **19 (1/2)**", "com_282"))          
                        list.append(("    Al-Mutaffifeen , Makkah  **36 (1)**", "com_283"))                        
                        list.append(("    Al-Inshiqaaq , Makkah  **25 (1)**", "com_284"))
                        list.append(("    Al-Burooj , Makkah  **22 (1)**", "com_285"))
                        list.append(("    At-Taariq , Makkah  **17 (1/2)**", "com_286"))                
                        list.append(("    Al-A'la , Makkah  **19 (1/2)**", "com_287"))
                        list.append(("    Al-Ghaashiyah , Makkah  **26 (1)**", "com_288"))
                        list.append(("    Al-Fajr , Makkah  **30 (1)**", "com_289"))
                        list.append(("    Al-Balad , Makkah  **20 (1/2)**", "com_190"))
                        list.append(("    Ash-Shams , Makkah  **15 (1/2)**", "com_291"))
                        list.append(("    Al-Layl , Makkah  **21 (1/2)**", "com_292"))
                        list.append(("    Ad-Dhuha , Makkah  **11 (1/2)**", "com_293"))                        
                        list.append(("    Ash-Sharh , Makkah  **8 (1/3)**", "com_294"))
                        list.append(("    At-Tin , Makkah  **8 (1/3)**", "com_295"))
                        list.append(("    Al-Alaq , Makkah  **19 (1/2)**", "com_296"))                
                        list.append(("    Al-Qadr , Makkah  **5 (1/3)**", "com_297"))
                        list.append(("    Al-Bayyinah , Madinah  **8 (1)**", "com_298"))
                        list.append(("    Az-Zalzalah , Madinah  **8 (1/3)**", "com_299"))
                        list.append(("    Al-'Aadiyat , Makkah  **11 (1/3)**", "com_300"))
                        list.append(("    Al-Qaari'ah , Makkah  **11 (1/3)**", "com_301"))
                        list.append(("    At-Takaathur , Makkah  **8 (1/3)**", "com_302"))
                        list.append(("    Al-'Asr , Makkah  **3 (1/3)**", "com_303"))
                        list.append(("    Al-Humazah , Makkah  **9 (1/3)**", "com_304"))
                        list.append(("    Al-Feel , Makkah  **5 (1/3)**", "com_305"))
                        list.append(("    Quraish , Makkah  **4 (1/3)**", "com_306"))
                        list.append(("    Al-Maa'oon , Makkah  **7 (1/3)**", "com_307"))
                        list.append(("    Al-Kawthar , Makkah  **3 (1/3)**", "com_308"))
                        list.append(("    Al-Kaafiroon , Makkah  **6 (1/3)**", "com_309"))
                        list.append(("    An-Nasr , Madinah  **3 (1/3)**", "com_310"))
                        list.append(("    Al-Masad , Makkah  **5 (1/3)**", "com_311"))
                        list.append(("    Al-Ikhlas , Makkah  **4 (1/3)**", "com_312"))
                        list.append(("    Al-Falaq , Makkah  **5 (1/3)**", "com_313"))
                        list.append(("    An-Naas , Makkah  **6 (1/3)**", "com_314"))
                        list.append(("    Full Tilawa", "com_315"))                        
                        list.append(("    Doa Khatam Quran", "com_316"))
                        list.append(("    Doa Khatam Quran", "com_317"))
                        list.append(("    Doa Khatam Quran", "com_318"))                
                        list.append(("    Doa Khatam Quran", "com_319"))
                        list.append(("    Doa Khatam Quran", "com_320"))
                        list.append(("    Doa Khatam Quran", "com_321"))                
                        list.append(("    Doa Khatam Quran 1409", "com_322"))
                        list.append(("    Part of ama Doa Khatam Quran 1414", "com_323"))
                        list.append(("    Doa Khatam Quran for the night of 27 Ramadan 1423", "com_324"))
                        list.append(("    Doa Khatam Quran", "com_325")) 
                        list.append((_("    Exit"), "exit"))
                list.append((_("Exit"), "exit"))
                Screen.__init__(self, session)
                #self["myYellowBtn"] = Label(_("restart"))
                #self["myBlueBtn"] = Label(_("Preview"))
                self.cmdlist = []
                self.onChangedEntry = []
                self.initialservice = session.nav.getCurrentlyPlayingServiceReference()         
                self["myMenu"] = MenuList(list)
                self['setupActions'] = ActionMap(['SetupActions'], 
                {
                        #'yellow': self.goto,
                        #'blue': self.gotoa,
                        'red': self.close,
                        'ok': self.go,
                        'cancel': self.close
                }, -1)
                if connected_to_internet():
                    self.wget = "wget --no-check-certificate"
                    import sys,os  
                    os.system("sh '/usr/lib/enigma2/python/Plugins/Extensions/FreeServer/scripts/picturecimages.sh'") 
                self.go               
                self.onChangedEntry = []
                self.timer_list = []
                self.processed_timers = [] 
                self.timer = eTimer()
                self.initialservice = session.nav.getCurrentlyPlayingServiceReference()
                self.updateTimer = eTimer()
                self.timer.start(2000, True)
                self.timer = eTimer()
                self.timer.start(2, 1)
                self.onLayoutFinish.append(self.layoutFinished)
                self.Tilawa
### Edit By RAED To DreamOS & Fix update notification restart warrning
                try:
                       self.timer.callback.append(self.update)
                except:
                       self.timer_conn = self.timer.timeout.connect(self.update)

        def layoutFinished(self):
                self.setTitle(" ")


        def Tilawa(self):

            from enigma import eServiceReference
            from Plugins.Extensions.FreeServer.outils.InfoBar import ALAJREStream5
            url = "http://n06.radiojar.com/8s5u5tpdtwzuv"
            #url = 'http://ample-09.radiojar.com/8s5u5tpdtwzuv'
            #url = 'http://178.33.178.204:9322/index.html'
            #url = 'https://ia601507.us.archive.org/22/items/PremierLeague_201812/Premier_League.mp3'
            ref = eServiceReference(4097, 0, url)
            ref.setName(Version_1)
            self.session.openWithCallback(self.backToIntialService, ALAJREStream5, ref)

       
        def backToIntialService(self, ret = None):
            self.session.nav.stopService()
            self.session.nav.playService(self.initialservice)
            self.fast()

        def fast(self):   
            self.timer.stop()
            #self.session.openWithCallback(self.close, ALAJREStream6, ref)
            #self.session.close(ALAJREStream5)
             
        def disappear(self):
            self.Tilawa()
### End EDit
        def go(self):
                if config.plugins.FreeServerminoo.lang.value == "EN":
                	Version_1 = 'Plese Wait whIle is being updated... Plese be patient...'
                elif config.plugins.FreeServerminoo.lang.value == "AR":
                	Version_1 = u'... يرجى الانتظار بينما يتم تحديث وحدة التحكم الإلكترونية الخاصة بك ... يرجى التحلي بالصبر'
                elif config.plugins.FreeServerminoo.lang.value == "FR":
                	Version_1 = 'Veuillez patienter pendant la mise à jour... Veuillez patienter...'
                else:
                	Version_1 = 'Plese Wait whIle is being updated... Plese be patient...'   
                returnValue = self["myMenu"].l.getCurrentSelection()[1]
                if returnValue != None:
                        if returnValue =="com_01":
                            if connected_to_internet():
                               from enigma import eServiceReference
                               from Plugins.Extensions.FreeServer.outils.InfoBar import ALAJREStream5
                               url = "https://Qurango.net/radio/saud_alshuraim.mp3"                           
                               ref = eServiceReference(4097, 0, url)
                               ref.setName(Version_1)         
                               self.session.openWithCallback(self.backToIntialService, ALAJREStream5, ref)
                        elif returnValue =="com_02":
                            if connected_to_internet():
                               from enigma import eServiceReference
                               from Plugins.Extensions.FreeServer.outils.InfoBar import ALAJREStream5
                               url = "http://live.mp3quran.net:9960/;"                           
                               ref = eServiceReference(4097, 0, url)
                               ref.setName(Version_1)         
                               self.session.openWithCallback(self.backToIntialService, ALAJREStream5, ref)
                        elif returnValue =="com_03":
                            if connected_to_internet():
                               from enigma import eServiceReference
                               from Plugins.Extensions.FreeServer.outils.InfoBar import ALAJREStream5
                               url = "http://live.mp3quran.net:8014/;"                           
                               ref = eServiceReference(4097, 0, url)
                               ref.setName(Version_1)         
                               self.session.openWithCallback(self.backToIntialService, ALAJREStream5, ref)
                        elif returnValue =="com_04":
                            if connected_to_internet():
                               from enigma import eServiceReference
                               from Plugins.Extensions.FreeServer.outils.InfoBar import ALAJREStream5
                               url = "http://live.mp3quran.net:9976/;"                           
                               ref = eServiceReference(4097, 0, url)
                               ref.setName(Version_1)         
                               self.session.openWithCallback(self.backToIntialService, ALAJREStream5, ref)
                        elif returnValue =="com_05":
                            if connected_to_internet():
                               from enigma import eServiceReference
                               from Plugins.Extensions.FreeServer.outils.InfoBar import ALAJREStream5
                               url = "https://mediati.me/radio/8010/radio.mp3?1608014536"                           
                               ref = eServiceReference(4097, 0, url)
                               ref.setName(Version_1) 
                               self.session.openWithCallback(self.backToIntialService, ALAJREStream5, ref)
                        elif returnValue =="com_06":
                            if connected_to_internet():
                               from enigma import eServiceReference
                               from Plugins.Extensions.FreeServer.outils.InfoBar import ALAJREStream5
                               url = "http://listen.ourquraan.com/Saud_Al-Shuraim/018.mp3"                           
                               ref = eServiceReference(4097, 0, url)
                               ref.setName(Version_1) 
                               self.session.openWithCallback(self.backToIntialService, ALAJREStream5, ref)
                        elif returnValue =="com_1":
                            if connected_to_internet():
                               from enigma import eServiceReference
                               from Plugins.Extensions.FreeServer.outils.InfoBar import ALAJREStream5
                               url = "http://n06.radiojar.com/8s5u5tpdtwzuv"                           
                               ref = eServiceReference(4097, 0, url)
                               ref.setName(Version_1)         
                               self.session.openWithCallback(self.backToIntialService, ALAJREStream5, ref)
                        elif returnValue =="com_2":
                            if connected_to_internet():
                               from enigma import eServiceReference
                               from Plugins.Extensions.FreeServer.outils.InfoBar import ALAJREStream5
                               url = "https://stream.radiojar.com/4wqre23fytzuv"                           
                               ref = eServiceReference(4097, 0, url)
                               ref.setName(Version_1)         
                               self.session.openWithCallback(self.backToIntialService, ALAJREStream5, ref)
                        elif returnValue =="com_3":
                            if connected_to_internet():
                               from enigma import eServiceReference
                               from Plugins.Extensions.FreeServer.outils.InfoBar import ALAJREStream5
                               url = "https://webradio.tda.dz/Coran_64K.mp3"                           
                               ref = eServiceReference(4097, 0, url)
                               ref.setName(Version_1)         
                               self.session.openWithCallback(self.backToIntialService, ALAJREStream5, ref)
                        elif returnValue =="com_4":
                            if connected_to_internet():
                               from enigma import eServiceReference
                               from Plugins.Extensions.FreeServer.outils.InfoBar import ALAJREStream5
                               url = "http://92.222.103.13:8005/;stream.nsv"                           
                               ref = eServiceReference(4097, 0, url)
                               ref.setName(Version_1)         
                               self.session.openWithCallback(self.backToIntialService, ALAJREStream5, ref)
                        elif returnValue =="com_5":
                            if connected_to_internet():
                               from enigma import eServiceReference
                               from Plugins.Extensions.FreeServer.outils.InfoBar import ALAJREStream5
                               url = "https://zayedquran.gov.ae/stream.php"                           
                               ref = eServiceReference(4097, 0, url)
                               ref.setName(Version_1)         
                               self.session.openWithCallback(self.backToIntialService, ALAJREStream5, ref)                        
                        elif returnValue =="com_6":
                            if connected_to_internet():
                               from enigma import eServiceReference
                               from Plugins.Extensions.FreeServer.outils.InfoBar import ALAJREStream5
                               url = "https://edge.mixlr.com/channel/liqju"                           
                               ref = eServiceReference(4097, 0, url)
                               ref.setName(Version_1)         
                               self.session.openWithCallback(self.backToIntialService, ALAJREStream5, ref)                        
                        elif returnValue =="com_7":
                            if connected_to_internet():
                               from enigma import eServiceReference
                               from Plugins.Extensions.FreeServer.outils.InfoBar import ALAJREStream5
                               url = "https://edge.mixlr.com/channel/eterm"                           
                               ref = eServiceReference(4097, 0, url)
                               ref.setName(Version_1)         
                               self.session.openWithCallback(self.backToIntialService, ALAJREStream5, ref)   
                        elif returnValue =="com_8":
                            if connected_to_internet():
                               from enigma import eServiceReference
                               from Plugins.Extensions.FreeServer.outils.InfoBar import ALAJREStream5
                               url = "http://66.45.232.131:9994/;stream.nsv"                           
                               ref = eServiceReference(4097, 0, url)
                               ref.setName(Version_1)         
                               self.session.openWithCallback(self.backToIntialService, ALAJREStream5, ref)  
                        elif returnValue =="com_9":
                            if connected_to_internet():
                               from enigma import eServiceReference
                               from Plugins.Extensions.FreeServer.outils.InfoBar import ALAJREStream5
                               url = "http://66.45.232.131:9994/;stream.nsv"                           
                               ref = eServiceReference(4097, 0, url)
                               ref.setName(Version_1)         
                               self.session.openWithCallback(self.backToIntialService, ALAJREStream5, ref)  
                        elif returnValue =="com_10":
                            if connected_to_internet():
                               from enigma import eServiceReference
                               from Plugins.Extensions.FreeServer.outils.InfoBar import ALAJREStream5
                               url = "http://206.72.199.179:9992/;stream.nsv"                           
                               ref = eServiceReference(4097, 0, url)
                               ref.setName(Version_1)         
                               self.session.openWithCallback(self.backToIntialService, ALAJREStream5, ref)  
                        elif returnValue =="com_11":
                            if connected_to_internet():
                               from enigma import eServiceReference
                               from Plugins.Extensions.FreeServer.outils.InfoBar import ALAJREStream5
                               url = "http://www.quran-radio.org:8080/;stream.nsv"                           
                               ref = eServiceReference(4097, 0, url)
                               ref.setName(Version_1)         
                               self.session.openWithCallback(self.backToIntialService, ALAJREStream5, ref)  
                        elif returnValue =="com_12":
                            if connected_to_internet():
                               from enigma import eServiceReference
                               from Plugins.Extensions.FreeServer.outils.InfoBar import ALAJREStream5
                               url = "http://live.mp3quran.net:9960/"                           
                               ref = eServiceReference(4097, 0, url)
                               ref.setName(Version_1)         
                               self.session.openWithCallback(self.backToIntialService, ALAJREStream5, ref)
                        elif returnValue =="com_13":
                            if connected_to_internet():
                               from enigma import eServiceReference
                               from Plugins.Extensions.FreeServer.outils.InfoBar import ALAJREStream5
                               url = "http://listen.radioislam.co.za:8080/radioislam.mp3"                           
                               ref = eServiceReference(4097, 0, url)
                               ref.setName(Version_1)         
                               self.session.openWithCallback(self.backToIntialService, ALAJREStream5, ref)  
                        elif returnValue =="com_14":
                            if connected_to_internet():
                               from enigma import eServiceReference
                               from Plugins.Extensions.FreeServer.outils.InfoBar import ALAJREStream5
                               url = "https://tvs.jagobd.com/radio.php?u=al-quran-radio.stream&vw=780&vh=90"                           
                               ref = eServiceReference(4097, 0, url)
                               ref.setName(Version_1)         
                               self.session.openWithCallback(self.backToIntialService, ALAJREStream5, ref)
                        elif returnValue =="com_15":
                            if connected_to_internet():
                               from enigma import eServiceReference
                               from Plugins.Extensions.FreeServer.outils.InfoBar import ALAJREStream5
                               url = "https://onlineradiobox.com/json/us/allahuakbar/play?platform=web"                           
                               ref = eServiceReference(4097, 0, url)
                               ref.setName(Version_1)         
                               self.session.openWithCallback(self.backToIntialService, ALAJREStream5, ref)
                        elif returnValue =="com_16":
                            if connected_to_internet():
                               from enigma import eServiceReference
                               from Plugins.Extensions.FreeServer.outils.InfoBar import ALAJREStream5
                               url = "http://r7.tarat.com:8004/;"                           
                               ref = eServiceReference(4097, 0, url)
                               ref.setName(Version_1)         
                               self.session.openWithCallback(self.backToIntialService, ALAJREStream5, ref)
                        elif returnValue =="com_17":
                            if connected_to_internet():
                               from enigma import eServiceReference
                               from Plugins.Extensions.FreeServer.outils.InfoBar import ALAJREStream5
                               url = "http://r7.tarat.com:8002/;"                           
                               ref = eServiceReference(4097, 0, url)
                               ref.setName(Version_1)         
                               self.session.openWithCallback(self.backToIntialService, ALAJREStream5, ref)
                        elif returnValue =="com_18":
                            if connected_to_internet():
                               from enigma import eServiceReference
                               from Plugins.Extensions.FreeServer.outils.InfoBar import ALAJREStream5
                               url = "https://server03.quran.com.kw:7032/;"                           
                               ref = eServiceReference(4097, 0, url)
                               ref.setName(Version_1)         
                               self.session.openWithCallback(self.backToIntialService, ALAJREStream5, ref)
                        elif returnValue =="com_19":
                            if connected_to_internet():
                               from enigma import eServiceReference
                               from Plugins.Extensions.FreeServer.outils.InfoBar import ALAJREStream5
                               url = "http://www.quran-radio.org:8002/;stream.nsv"                           
                               ref = eServiceReference(4097, 0, url)
                               ref.setName(Version_1)         
                               self.session.openWithCallback(self.backToIntialService, ALAJREStream5, ref)
                        elif returnValue =="com_20":
                            if connected_to_internet():
                               from enigma import eServiceReference
                               from Plugins.Extensions.FreeServer.outils.InfoBar import ALAJREStream5
                               url = "http://66.45.232.134:9300/;"                           
                               ref = eServiceReference(4097, 0, url)
                               ref.setName(Version_1)         
                               self.session.openWithCallback(self.backToIntialService, ALAJREStream5, ref)
                        elif returnValue =="com_21":
                            if connected_to_internet():
                               from enigma import eServiceReference
                               from Plugins.Extensions.FreeServer.outils.InfoBar import ALAJREStream5
                               url = "https://tunein.buzzislam.com/radio/8000/radio.mp3"                           
                               ref = eServiceReference(4097, 0, url)
                               ref.setName(Version_1)         
                               self.session.openWithCallback(self.backToIntialService, ALAJREStream5, ref)
                        elif returnValue =="com_22":
                            if connected_to_internet():
                               from enigma import eServiceReference
                               from Plugins.Extensions.FreeServer.outils.InfoBar import ALAJREStream5
                               url = "http://www.2mfm.org.au:8000/live"                           
                               ref = eServiceReference(4097, 0, url)
                               ref.setName(Version_1)         
                               self.session.openWithCallback(self.backToIntialService, ALAJREStream5, ref)
                        elif returnValue =="com_23":
                            if connected_to_internet():
                               from enigma import eServiceReference
                               from Plugins.Extensions.FreeServer.outils.InfoBar import ALAJREStream5
                               url = "https://radiodawn.radioca.st/stream"                           
                               ref = eServiceReference(4097, 0, url)
                               ref.setName(Version_1)         
                               self.session.openWithCallback(self.backToIntialService, ALAJREStream5, ref)
                        elif returnValue =="com_24":
                            if connected_to_internet():
                               from enigma import eServiceReference
                               from Plugins.Extensions.FreeServer.outils.InfoBar import ALAJREStream5
                               url = "http://icecast.commedia.org.uk:8000/crescent.mp3"                           
                               ref = eServiceReference(4097, 0, url)
                               ref.setName(Version_1)         
                               self.session.openWithCallback(self.backToIntialService, ALAJREStream5, ref)
                        elif returnValue =="com_25":
                            if connected_to_internet():
                               from enigma import eServiceReference
                               from Plugins.Extensions.FreeServer.outils.InfoBar import ALAJREStream5
                               url = "http://66.45.232.133:9998/;"                           
                               ref = eServiceReference(4097, 0, url)
                               ref.setName(Version_1)         
                               self.session.openWithCallback(self.backToIntialService, ALAJREStream5, ref)
                        elif returnValue =="com_26":
                            if connected_to_internet():
                               from enigma import eServiceReference
                               from Plugins.Extensions.FreeServer.outils.InfoBar import ALAJREStream5
                               url = "https://radioislamindonesia.com/rodja.mp3"                           
                               ref = eServiceReference(4097, 0, url)
                               ref.setName(Version_1)         
                               self.session.openWithCallback(self.backToIntialService, ALAJREStream5, ref)
                        elif returnValue =="com_27":
                            if connected_to_internet():
                               from enigma import eServiceReference
                               from Plugins.Extensions.FreeServer.outils.InfoBar import ALAJREStream5
                               url = "http://162.244.81.30:8224/;stream.mp3?src=1"                           
                               ref = eServiceReference(4097, 0, url)
                               ref.setName(Version_1)         
                               self.session.openWithCallback(self.backToIntialService, ALAJREStream5, ref)
                        elif returnValue =="com_28":
                            if connected_to_internet():
                               from enigma import eServiceReference
                               from Plugins.Extensions.FreeServer.outils.InfoBar import ALAJREStream5
                               url = "http://104.167.2.55:8000/;"                           
                               ref = eServiceReference(4097, 0, url)
                               ref.setName(Version_1)         
                               self.session.openWithCallback(self.backToIntialService, ALAJREStream5, ref)
                        elif returnValue =="com_29":
                            if connected_to_internet():
                               from enigma import eServiceReference
                               from Plugins.Extensions.FreeServer.outils.InfoBar import ALAJREStream5
                               url = "http://206.72.199.179:9992/;"                           
                               ref = eServiceReference(4097, 0, url)
                               ref.setName(Version_1)         
                               self.session.openWithCallback(self.backToIntialService, ALAJREStream5, ref)
                        elif returnValue =="com_30":
                            if connected_to_internet():
                               from enigma import eServiceReference
                               from Plugins.Extensions.FreeServer.outils.InfoBar import ALAJREStream5
                               url = "http://edge.mixlr.com/channel/rwumx"                           
                               ref = eServiceReference(4097, 0, url)
                               ref.setName(Version_1)         
                               self.session.openWithCallback(self.backToIntialService, ALAJREStream5, ref)
                        elif returnValue =="com_31":
                            if connected_to_internet():
                               from enigma import eServiceReference
                               from Plugins.Extensions.FreeServer.outils.InfoBar import ALAJREStream5
                               url = "http://104.7.66.64:8095/stream/1/"                           
                               ref = eServiceReference(4097, 0, url)
                               ref.setName(Version_1)         
                               self.session.openWithCallback(self.backToIntialService, ALAJREStream5, ref)
                        elif returnValue =="com_32":
                            if connected_to_internet():
                               from enigma import eServiceReference
                               from Plugins.Extensions.FreeServer.outils.InfoBar import ALAJREStream5
                               url = "https://zinebladi.ma/radio"                           
                               ref = eServiceReference(4097, 0, url)
                               ref.setName(Version_1)         
                               self.session.openWithCallback(self.backToIntialService, ALAJREStream5, ref)
                        elif returnValue =="com_33":
                            if connected_to_internet():
                               from enigma import eServiceReference
                               from Plugins.Extensions.FreeServer.outils.InfoBar import ALAJREStream5
                               url = "http://149.28.52.216:3344/stream/1/"                           
                               ref = eServiceReference(4097, 0, url)
                               ref.setName(Version_1)
                               self.session.openWithCallback(self.backToIntialService, ALAJREStream5, ref)        
                        elif returnValue =="com_34":
                            if connected_to_internet():
                               from enigma import eServiceReference
                               from Plugins.Extensions.FreeServer.outils.InfoBar import ALAJREStream5
                               url = "http://104.167.2.55:8000/;"                           
                               ref = eServiceReference(4097, 0, url)
                               ref.setName(Version_1)
                               self.session.openWithCallback(self.backToIntialService, ALAJREStream5, ref)  
                        elif returnValue =="com_35":
                            if connected_to_internet():
                               from enigma import eServiceReference
                               from Plugins.Extensions.FreeServer.outils.InfoBar import ALAJREStream5
                               url = "http://aradio.aryanict.com:9332/;"                           
                               ref = eServiceReference(4097, 0, url)
                               ref.setName(Version_1)
                               self.session.openWithCallback(self.backToIntialService, ALAJREStream5, ref)       
                        elif returnValue =="com_36":
                            if connected_to_internet():
                               from enigma import eServiceReference
                               from Plugins.Extensions.FreeServer.outils.InfoBar import ALAJREStream5
                               url = "http://149.28.52.216:3344/stream/1/"                           
                               ref = eServiceReference(4097, 0, url)
                               ref.setName(Version_1)
                               self.session.openWithCallback(self.backToIntialService, ALAJREStream5, ref)   
                        elif returnValue =="com_37":
                            if connected_to_internet():
                               from enigma import eServiceReference
                               from Plugins.Extensions.FreeServer.outils.InfoBar import ALAJREStream5
                               url = "http://162.244.81.30:8224/;"                           
                               ref = eServiceReference(4097, 0, url)
                               ref.setName(Version_1)
                               self.session.openWithCallback(self.backToIntialService, ALAJREStream5, ref)   
                        elif returnValue =="com_38":
                            if connected_to_internet():
                               from enigma import eServiceReference
                               from Plugins.Extensions.FreeServer.outils.InfoBar import ALAJREStream5
                               url = "https://www.qurantranslations.net/sound/English/AbdulBaset_AbdulSamad/002.mp3?type=.mp3/;stream.mp3"                           
                               ref = eServiceReference(4097, 0, url)
                               ref.setName(Version_1)
                               self.session.openWithCallback(self.backToIntialService, ALAJREStream5, ref)  
                        elif returnValue =="com_39":
                            if connected_to_internet():
                               from enigma import eServiceReference
                               from Plugins.Extensions.FreeServer.outils.InfoBar import ALAJREStream5
                               url = "https://l3.itworkscdn.net/smcquranlive/quranradiolive/icecast.audio"                           
                               ref = eServiceReference(4097, 0, url)
                               ref.setName(Version_1)
                               self.session.openWithCallback(self.backToIntialService, ALAJREStream5, ref)   
                        elif returnValue =="com_40":
                            if connected_to_internet():
                               from enigma import eServiceReference
                               from Plugins.Extensions.FreeServer.outils.InfoBar import ALAJREStream5
                               url = "https://alzainquran.radioca.st/stream"                           
                               ref = eServiceReference(4097, 0, url)
                               ref.setName(Version_1)
                               self.session.openWithCallback(self.backToIntialService, ALAJREStream5, ref)   
                        elif returnValue =="com_41":
                            if connected_to_internet():
                               from enigma import eServiceReference
                               from Plugins.Extensions.FreeServer.outils.InfoBar import ALAJREStream5
                               url = "http://server4.streamserver24.com:21494/stream/1/"                           
                               ref = eServiceReference(4097, 0, url)
                               ref.setName(Version_1)
                               self.session.openWithCallback(self.backToIntialService, ALAJREStream5, ref)    
                        elif returnValue =="com_42":
                            if connected_to_internet():
                               from enigma import eServiceReference
                               from Plugins.Extensions.FreeServer.outils.InfoBar import ALAJREStream5
                               url = "http://104.7.66.64:8088/stream/1/"                           
                               ref = eServiceReference(4097, 0, url)
                               ref.setName(Version_1)
                               self.session.openWithCallback(self.backToIntialService, ALAJREStream5, ref) 
                        elif returnValue =="com_43":
                            if connected_to_internet():
                               from enigma import eServiceReference
                               from Plugins.Extensions.FreeServer.outils.InfoBar import ALAJREStream5
                               url = "http://66.45.232.133:9998/;stream.nsv"                           
                               ref = eServiceReference(4097, 0, url)
                               ref.setName(Version_1)
                               self.session.openWithCallback(self.backToIntialService, ALAJREStream5, ref)    
                        elif returnValue =="com_44":
                            if connected_to_internet():
                               from enigma import eServiceReference
                               from Plugins.Extensions.FreeServer.outils.InfoBar import ALAJREStream5
                               url = "https://onlineradiobox.com/json/us/emancity/play?platform=web"                           
                               ref = eServiceReference(4097, 0, url)
                               ref.setName(Version_1)
                               self.session.openWithCallback(self.backToIntialService, ALAJREStream5, ref)    
                        elif returnValue =="com_45":
                            if connected_to_internet():
                               from enigma import eServiceReference
                               from Plugins.Extensions.FreeServer.outils.InfoBar import ALAJREStream5
                               url = "http://66.45.232.132:9996/;"                           
                               ref = eServiceReference(4097, 0, url)
                               ref.setName(Version_1)
                               self.session.openWithCallback(self.backToIntialService, ALAJREStream5, ref)   
                        elif returnValue =="com_46":
                            if connected_to_internet():
                               from enigma import eServiceReference
                               from Plugins.Extensions.FreeServer.outils.InfoBar import ALAJREStream5
                               url = "http://149.28.52.216:3344/stream/1/"                           
                               ref = eServiceReference(4097, 0, url)
                               ref.setName(Version_1)
                               self.session.openWithCallback(self.backToIntialService, ALAJREStream5, ref)  
                        elif returnValue =="com_47":
                            if connected_to_internet():
                               from enigma import eServiceReference
                               from Plugins.Extensions.FreeServer.outils.InfoBar import ALAJREStream5
                               url = "http://s1.wohooo.net:9018/;"                           
                               ref = eServiceReference(4097, 0, url)
                               ref.setName(Version_1)
                               self.session.openWithCallback(self.backToIntialService, ALAJREStream5, ref) 
                        elif returnValue =="com_47":
                            if connected_to_internet():
                               from enigma import eServiceReference
                               from Plugins.Extensions.FreeServer.outils.InfoBar import ALAJREStream5
                               url = "http://svara-stream.radioddns.net:8000/bandung_mqfm_mp3"                           
                               ref = eServiceReference(4097, 0, url)
                               ref.setName(Version_1)
                               self.session.openWithCallback(self.backToIntialService, ALAJREStream5, ref)    
                        elif returnValue =="com_48":
                            if connected_to_internet():
                               from enigma import eServiceReference
                               from Plugins.Extensions.FreeServer.outils.InfoBar import ALAJREStream5
                               url = "http://streamer3.rightclickitservices.com:9755/;"                           
                               ref = eServiceReference(4097, 0, url)
                               ref.setName(Version_1)
                               self.session.openWithCallback(self.backToIntialService, ALAJREStream5, ref)   
                        elif returnValue =="com_49":
                            if connected_to_internet():                                            
                               from enigma import eServiceReference
                               from Plugins.Extensions.FreeServer.outils.InfoBar import ALAJREStream5
                               url = "http://149.28.52.216:3344/stream/1/"                           
                               ref = eServiceReference(4097, 0, url)
                               ref.setName(Version_1)
                               self.session.openWithCallback(self.backToIntialService, ALAJREStream5, ref)  
                        elif returnValue =="com_50":
                            if connected_to_internet():
                               from enigma import eServiceReference
                               from Plugins.Extensions.FreeServer.outils.InfoBar import ALAJREStream5
                               url = "http://yayin.dostfm.com:8920/;"                           
                               ref = eServiceReference(4097, 0, url)
                               ref.setName(Version_1)
                               self.session.openWithCallback(self.backToIntialService, ALAJREStream5, ref)                                     
                        elif returnValue =="com_51":
                            if connected_to_internet():
                               from enigma import eServiceReference
                               from Plugins.Extensions.FreeServer.outils.InfoBar import ALAJREStream5
                               url = "http://andromeda.shoutca.st:8189/stream"                           
                               ref = eServiceReference(4097, 0, url)  
                               ref.setName(Version_1)
                               self.session.openWithCallback(self.backToIntialService, ALAJREStream5, ref) 
                        elif returnValue =="com_52":
                            if connected_to_internet():
                               from enigma import eServiceReference
                               from Plugins.Extensions.FreeServer.outils.InfoBar import ALAJREStream5
                               url = "https://stream.zenolive.com/seb77kna90duv"                           
                               ref = eServiceReference(4097, 0, url)
                               ref.setName(Version_1)
                               self.session.openWithCallback(self.backToIntialService, ALAJREStream5, ref) 
                        elif returnValue =="com_53":
                            if connected_to_internet():
                               from enigma import eServiceReference
                               from Plugins.Extensions.FreeServer.outils.InfoBar import ALAJREStream5
                               url = "https://radio.al7eah.net/8010/stream"                           
                               ref = eServiceReference(4097, 0, url)
                               ref.setName(Version_1)
                               self.session.openWithCallback(self.backToIntialService, ALAJREStream5, ref) 
                        elif returnValue =="com_54":
                            if connected_to_internet():
                               from enigma import eServiceReference
                               from Plugins.Extensions.FreeServer.outils.InfoBar import ALAJREStream5
                               url = "http://live.canstream.co.uk:8000/unity.mp3"                           
                               ref = eServiceReference(4097, 0, url)
                               ref.setName(Version_1)
                               self.session.openWithCallback(self.backToIntialService, ALAJREStream5, ref) 
                        elif returnValue =="com_55":
                            if connected_to_internet():
                               from enigma import eServiceReference
                               from Plugins.Extensions.FreeServer.outils.InfoBar import ALAJREStream5
                               url = "http://rtvpendimi.com:8020/;stream.nsv"                           
                               ref = eServiceReference(4097, 0, url)
                               ref.setName(Version_1)
                               self.session.openWithCallback(self.backToIntialService, ALAJREStream5, ref) 
                        elif returnValue =="com_56":
                            if connected_to_internet():
                               from enigma import eServiceReference
                               from Plugins.Extensions.FreeServer.outils.InfoBar import ALAJREStream5
                               url = "https://tunzilla.com:443/http://109.169.23.124:9091/stream?type=.aac"                           
                               ref = eServiceReference(4097, 0, url)
                               ref.setName(Version_1)
                               self.session.openWithCallback(self.backToIntialService, ALAJREStream5, ref) 
                        elif returnValue =="com_57":
                            if connected_to_internet():
                               from enigma import eServiceReference
                               from Plugins.Extensions.FreeServer.outils.InfoBar import ALAJREStream5
                               url = "https://stream.zeno.fm/x4451xh0x1zuv"                           
                               ref = eServiceReference(4097, 0, url)
                               ref.setName(Version_1)         
                               self.session.openWithCallback(self.backToIntialService, ALAJREStream5, ref)
                        elif returnValue =="com_58":
                            if connected_to_internet():
                               from enigma import eServiceReference
                               from Plugins.Extensions.FreeServer.outils.InfoBar import ALAJREStream5
                               url = "https://stream.zeno.fm/vrrtqsh0x1zuv"                           
                               ref = eServiceReference(4097, 0, url)
                               ref.setName(Version_1)         
                               self.session.openWithCallback(self.backToIntialService, ALAJREStream5, ref)
                        elif returnValue =="com_59":
                            if connected_to_internet():
                               from enigma import eServiceReference
                               from Plugins.Extensions.FreeServer.outils.InfoBar import ALAJREStream5
                               url = "http://149.28.52.216:3344/stream/1/"                           
                               ref = eServiceReference(4097, 0, url)
                               ref.setName(Version_1)
                               self.session.openWithCallback(self.backToIntialService, ALAJREStream5, ref)          
                        elif returnValue =="com_60":
                            if connected_to_internet():
                               from enigma import eServiceReference
                               from Plugins.Extensions.FreeServer.outils.InfoBar import ALAJREStream5
                               url = "https://void.idserverhost.com:8010/;"                           
                               ref = eServiceReference(4097, 0, url)
                               ref.setName(Version_1)         
                               self.session.openWithCallback(self.backToIntialService, ALAJREStream5, ref)  
                        elif returnValue =="com_61":
                            if connected_to_internet():
                               from enigma import eServiceReference
                               from Plugins.Extensions.FreeServer.outils.InfoBar import ALAJREStream5
                               url = "https://zitounafm.toutech.net/zitounalive"                           
                               ref = eServiceReference(4097, 0, url)
                               ref.setName(Version_1)
                               self.session.openWithCallback(self.backToIntialService, ALAJREStream5, ref)        
                        elif returnValue =="com_62":
                            if connected_to_internet():
                               from enigma import eServiceReference
                               from Plugins.Extensions.FreeServer.outils.InfoBar import ALAJREStream5
                               url = "http://stream.radyogrup.com:4010/;"                           
                               ref = eServiceReference(4097, 0, url)
                               ref.setName(Version_1)
                               self.session.openWithCallback(self.backToIntialService, ALAJREStream5, ref)    
                        elif returnValue =="com_63":
                            if connected_to_internet():
                               from enigma import eServiceReference
                               from Plugins.Extensions.FreeServer.outils.InfoBar import ALAJREStream5
                               url = "http://104.194.9.142:8302/live"                           
                               ref = eServiceReference(4097, 0, url)
                               ref.setName(Version_1)
                               self.session.openWithCallback(self.backToIntialService, ALAJREStream5, ref)   
                        elif returnValue =="com_64":
                            if connected_to_internet():
                               from enigma import eServiceReference
                               from Plugins.Extensions.FreeServer.outils.InfoBar import ALAJREStream5
                               url = "https://francemaghreb2.ice.infomaniak.ch/francemaghreb2-high.mp3"                           
                               ref = eServiceReference(4097, 0, url)
                               ref.setName(Version_1)
                               self.session.openWithCallback(self.backToIntialService, ALAJREStream5, ref)  
                        elif returnValue =="com_65":
                            if connected_to_internet():
                               from enigma import eServiceReference
                               from Plugins.Extensions.FreeServer.outils.InfoBar import ALAJREStream5
                               url = "http://yayin2.canliyayin.org:7082/;stream.nsv"                           
                               ref = eServiceReference(4097, 0, url)
                               ref.setName(Version_1)
                               self.session.openWithCallback(self.backToIntialService, ALAJREStream5, ref)   
                        elif returnValue =="com_66":
                            if connected_to_internet():
                               from enigma import eServiceReference
                               from Plugins.Extensions.FreeServer.outils.InfoBar import ALAJREStream5
                               url = "https://mediati.me/radio/8010/radio.mp3"                           
                               ref = eServiceReference(4097, 0, url)
                               ref.setName(Version_1)
                               self.session.openWithCallback(self.backToIntialService, ALAJREStream5, ref)    
                        elif returnValue =="com_67":
                            if connected_to_internet():
                               from enigma import eServiceReference
                               from Plugins.Extensions.FreeServer.outils.InfoBar import ALAJREStream5
                               url = "http://yayin2.canliyayin.org:8400/;stream.nsv"                           
                               ref = eServiceReference(4097, 0, url)
                               ref.setName(Version_1)
                               self.session.openWithCallback(self.backToIntialService, ALAJREStream5, ref)   
                        elif returnValue =="com_68":
                            if connected_to_internet():
                               from enigma import eServiceReference
                               from Plugins.Extensions.FreeServer.outils.InfoBar import ALAJREStream5
                               url = "http://listen.senemultimedia.net:5526/;"                           
                               ref = eServiceReference(4097, 0, url)
                               ref.setName(Version_1)
                               self.session.openWithCallback(self.backToIntialService, ALAJREStream5, ref)  
                        elif returnValue =="com_69":
                            if connected_to_internet():
                               from enigma import eServiceReference
                               from Plugins.Extensions.FreeServer.outils.InfoBar import ALAJREStream5
                               url = "http://162.244.80.52:6656/stream"                           
                               ref = eServiceReference(4097, 0, url)
                               ref.setName(Version_1)
                               self.session.openWithCallback(self.backToIntialService, ALAJREStream5, ref)   
                        elif returnValue =="com_70":
                            if connected_to_internet():
                               from enigma import eServiceReference
                               from Plugins.Extensions.FreeServer.outils.InfoBar import ALAJREStream5
                               url = "http://live.alboraq.ps:8000/;stream.mp3"                           
                               ref = eServiceReference(4097, 0, url)
                               ref.setName(Version_1)
                               self.session.openWithCallback(self.backToIntialService, ALAJREStream5, ref)  
                        elif returnValue =="com_71":
                            if connected_to_internet():
                               from enigma import eServiceReference
                               from Plugins.Extensions.FreeServer.outils.InfoBar import ALAJREStream5
                               url = "http://66.45.232.134:9300/;"                           
                               ref = eServiceReference(4097, 0, url)
                               ref.setName(Version_1)
                               self.session.openWithCallback(self.backToIntialService, ALAJREStream5, ref) 
                        elif returnValue =="com_72":
                            if connected_to_internet():
                               from enigma import eServiceReference
                               from Plugins.Extensions.FreeServer.outils.InfoBar import ALAJREStream5
                               url = "http://162.244.80.118:5678/stream"                           
                               ref = eServiceReference(4097, 0, url)
                               ref.setName(Version_1)
                               self.session.openWithCallback(self.backToIntialService, ALAJREStream5, ref)   
                        elif returnValue =="com_73":
                            if connected_to_internet():
                               from enigma import eServiceReference
                               from Plugins.Extensions.FreeServer.outils.InfoBar import ALAJREStream5
                               url = "http://s8.voscast.com:7112/;"                           
                               ref = eServiceReference(4097, 0, url)
                               ref.setName(Version_1)
                               self.session.openWithCallback(self.backToIntialService, ALAJREStream5, ref)   
                        elif returnValue =="com_74":
                            if connected_to_internet():
                               from enigma import eServiceReference
                               from Plugins.Extensions.FreeServer.outils.InfoBar import ALAJREStream5
                               url = "http://tijaniyyah.asuscomm.com:8000/stream/9/"                           
                               ref = eServiceReference(4097, 0, url)
                               ref.setName(Version_1)
                               self.session.openWithCallback(self.backToIntialService, ALAJREStream5, ref)  
                        elif returnValue =="com_75":
                            if connected_to_internet():                                            
                               from enigma import eServiceReference
                               from Plugins.Extensions.FreeServer.outils.InfoBar import ALAJREStream5
                               url = "http://95.173.161.133:9394/;stream.nsv"                           
                               ref = eServiceReference(4097, 0, url)
                               ref.setName(Version_1)
                               self.session.openWithCallback(self.backToIntialService, ALAJREStream5, ref)  
                        elif returnValue =="com_76":
                            if connected_to_internet():
                               from enigma import eServiceReference
                               from Plugins.Extensions.FreeServer.outils.InfoBar import ALAJREStream5
                               url = "http://206.72.199.180:9990/;"                           
                               ref = eServiceReference(4097, 0, url)
                               ref.setName(Version_1)         
                               self.session.openWithCallback(self.backToIntialService, ALAJREStream5, ref)                                    
                        elif returnValue =="com_77":
                            if connected_to_internet():
                               from enigma import eServiceReference
                               from Plugins.Extensions.FreeServer.outils.InfoBar import ALAJREStream5
                               url = "http://tijaniyyah.asuscomm.com:8000/stream/2/"                           
                               ref = eServiceReference(4097, 0, url)  
                               ref.setName(Version_1)
                               self.session.openWithCallback(self.backToIntialService, ALAJREStream5, ref) 
                        elif returnValue =="com_78":
                            if connected_to_internet():
                               from enigma import eServiceReference
                               from Plugins.Extensions.FreeServer.outils.InfoBar import ALAJREStream5
                               url = "http://5.56.158.246:8000/stream"                           
                               ref = eServiceReference(4097, 0, url)
                               ref.setName(Version_1)
                               self.session.openWithCallback(self.backToIntialService, ALAJREStream5, ref) 
                        elif returnValue =="com_79":
                            if connected_to_internet():
                               from enigma import eServiceReference
                               from Plugins.Extensions.FreeServer.outils.InfoBar import ALAJREStream5
                               url = "http://server2.quraan.us:9814/;*.mp3"                           
                               ref = eServiceReference(4097, 0, url)
                               ref.setName(Version_1)
                               self.session.openWithCallback(self.backToIntialService, ALAJREStream5, ref) 
                        elif returnValue =="com_80":
                            if connected_to_internet():
                               from enigma import eServiceReference
                               from Plugins.Extensions.FreeServer.outils.InfoBar import ALAJREStream5
                               url = "http://s13.myradiostream.com:40212/;stream.nsv"                           
                               ref = eServiceReference(4097, 0, url)
                               ref.setName(Version_1)
                               self.session.openWithCallback(self.backToIntialService, ALAJREStream5, ref) 
                        elif returnValue =="com_81":
                            if connected_to_internet():
                               from enigma import eServiceReference
                               from Plugins.Extensions.FreeServer.outils.InfoBar import ALAJREStream5
                               url = "http://5.9.65.9:8031/live?1508938696879"                           
                               ref = eServiceReference(4097, 0, url)
                               ref.setName(Version_1)
                               self.session.openWithCallback(self.backToIntialService, ALAJREStream5, ref) 
                        elif returnValue =="com_82":
                            if connected_to_internet():
                               from enigma import eServiceReference
                               from Plugins.Extensions.FreeServer.outils.InfoBar import ALAJREStream5
                               url = "http://s3.voscast.com:8450/;"                            
                               ref = eServiceReference(4097, 0, url)
                               ref.setName(Version_1)
                               self.session.openWithCallback(self.backToIntialService, ALAJREStream5, ref)    
                        elif returnValue =="com_83":
                            if connected_to_internet():
                               from enigma import eServiceReference
                               from Plugins.Extensions.FreeServer.outils.InfoBar import ALAJREStream5
                               url = "http://tijaniyyah.asuscomm.com:8000/stream/4/"                           
                               ref = eServiceReference(4097, 0, url)
                               ref.setName(Version_1)
                               self.session.openWithCallback(self.backToIntialService, ALAJREStream5, ref)    
                        elif returnValue =="com_84":
                            if connected_to_internet():
                               from enigma import eServiceReference
                               from Plugins.Extensions.FreeServer.outils.InfoBar import ALAJREStream5
                               url = "http://sv3.alhasmedia.com/radio/8270/radio"                           
                               ref = eServiceReference(4097, 0, url)
                               ref.setName(Version_1)
                               self.session.openWithCallback(self.backToIntialService, ALAJREStream5, ref)  
                        elif returnValue =="com_85":
                            if connected_to_internet():
                               from enigma import eServiceReference
                               from Plugins.Extensions.FreeServer.outils.InfoBar import ALAJREStream5
                               url = "http://92.222.103.13:8005/;stream.nsv"                           
                               ref = eServiceReference(4097, 0, url)
                               ref.setName(Version_1)
                               self.session.openWithCallback(self.backToIntialService, ALAJREStream5, ref) 
                        elif returnValue =="com_86":
                            if connected_to_internet():
                               from enigma import eServiceReference
                               from Plugins.Extensions.FreeServer.outils.InfoBar import ALAJREStream5
                               url = "http://162.244.81.30:8224/;"                           
                               ref = eServiceReference(4097, 0, url)
                               ref.setName(Version_1)
                               self.session.openWithCallback(self.backToIntialService, ALAJREStream5, ref) 
                        elif returnValue =="com_87":
                            if connected_to_internet():
                               from enigma import eServiceReference
                               from Plugins.Extensions.FreeServer.outils.InfoBar import ALAJREStream5
                               url = "http://139.59.200.203:8000/radio.mp3"                           
                               ref = eServiceReference(4097, 0, url)
                               ref.setName(Version_1)
                               self.session.openWithCallback(self.backToIntialService, ALAJREStream5, ref)   
                        elif returnValue =="com_88":
                            if connected_to_internet():
                               from enigma import eServiceReference
                               from Plugins.Extensions.FreeServer.outils.InfoBar import ALAJREStream5
                               url = "http://live.canstream.co.uk:8000/unity.mp3"                           
                               ref = eServiceReference(4097, 0, url)
                               ref.setName(Version_1)
                               self.session.openWithCallback(self.backToIntialService, ALAJREStream5, ref)   
                        elif returnValue =="com_89":
                            if connected_to_internet():
                               from enigma import eServiceReference
                               from Plugins.Extensions.FreeServer.outils.InfoBar import ALAJREStream5
                               url = "http://islam2day.tv:9898/;"                           
                               ref = eServiceReference(4097, 0, url)
                               ref.setName(Version_1)
                               self.session.openWithCallback(self.backToIntialService, ALAJREStream5, ref)   
                        elif returnValue =="com_90":
                            if connected_to_internet():
                               from enigma import eServiceReference
                               from Plugins.Extensions.FreeServer.outils.InfoBar import ALAJREStream5
                               url = "http://andromeda.shoutca.st:8189/stream"                           
                               ref = eServiceReference(4097, 0, url)
                               ref.setName(Version_1)
                               self.session.openWithCallback(self.backToIntialService, ALAJREStream5, ref)   
                        elif returnValue =="com_91":
                            if connected_to_internet():
                               from enigma import eServiceReference
                               from Plugins.Extensions.FreeServer.outils.InfoBar import ALAJREStream5
                               url = "http://104.194.9.142:8302/live"                           
                               ref = eServiceReference(4097, 0, url)
                               ref.setName(Version_1)
                               self.session.openWithCallback(self.backToIntialService, ALAJREStream5, ref)   
                        elif returnValue =="com_92":
                            if connected_to_internet():                                            
                               from enigma import eServiceReference
                               from Plugins.Extensions.FreeServer.outils.InfoBar import ALAJREStream5
                               url = "http://yayin2.canliyayin.org:7082/;stream.nsv"                           
                               ref = eServiceReference(4097, 0, url)
                               ref.setName(Version_1)
                               self.session.openWithCallback(self.backToIntialService, ALAJREStream5, ref)   
                        elif returnValue =="com_93":
                            if connected_to_internet():
                               from enigma import eServiceReference
                               from Plugins.Extensions.FreeServer.outils.InfoBar import ALAJREStream5
                               url = "http://66.45.232.131:9994/;"                           
                               ref = eServiceReference(4097, 0, url)
                               ref.setName(Version_1)
                               self.session.openWithCallback(self.backToIntialService, ALAJREStream5, ref)                                   
                        elif returnValue =="com_94":
                            if connected_to_internet():
                               from enigma import eServiceReference
                               from Plugins.Extensions.FreeServer.outils.InfoBar import ALAJREStream5
                               url = "http://www.quran-radio.org:8080/;stream.mp3"                           
                               ref = eServiceReference(4097, 0, url)  
                        elif returnValue =="com_95":
                            if connected_to_internet():
                               from enigma import eServiceReference
                               from Plugins.Extensions.FreeServer.outils.InfoBar import ALAJREStream5
                               url = "http://icecast.commedia.org.uk:8000/crescent.mp3"                           
                               ref = eServiceReference(4097, 0, url)
                               ref.setName(Version_1)
                               self.session.openWithCallback(self.backToIntialService, ALAJREStream5, ref) 
                        elif returnValue =="com_96":
                            if connected_to_internet():
                               from enigma import eServiceReference
                               from Plugins.Extensions.FreeServer.outils.InfoBar import ALAJREStream5
                               url = "https://radio.al7eah.net/8010/stream"                           
                               ref = eServiceReference(4097, 0, url)
                               ref.setName(Version_1)
                               self.session.openWithCallback(self.backToIntialService, ALAJREStream5, ref) 
                        elif returnValue =="com_97":
                            if connected_to_internet():
                               from enigma import eServiceReference
                               from Plugins.Extensions.FreeServer.outils.InfoBar import ALAJREStream5
                               url = "http://live.canstream.co.uk:8000/unity.mp3"                           
                               ref = eServiceReference(4097, 0, url)
                               ref.setName(Version_1)
                               self.session.openWithCallback(self.backToIntialService, ALAJREStream5, ref) 
                        elif returnValue =="com_98":
                            if connected_to_internet():
                               from enigma import eServiceReference
                               from Plugins.Extensions.FreeServer.outils.InfoBar import ALAJREStream5
                               url = "https://stream.zeno.fm/64bx3eq5cnruv"                           
                               ref = eServiceReference(4097, 0, url)
                               ref.setName(Version_1)
                               self.session.openWithCallback(self.backToIntialService, ALAJREStream5, ref) 
                        elif returnValue =="com_99":
                            if connected_to_internet():
                               from enigma import eServiceReference
                               from Plugins.Extensions.FreeServer.outils.InfoBar import ALAJREStream5
                               url = "https://radio.al7eah.net/8042/stream"                           
                               ref = eServiceReference(4097, 0, url)
                               ref.setName(Version_1)
                               self.session.openWithCallback(self.backToIntialService, ALAJREStream5, ref) 
                        elif returnValue =="com_100":
                            if connected_to_internet():
                               from enigma import eServiceReference
                               from Plugins.Extensions.FreeServer.outils.InfoBar import ALAJREStream5
                               url = "http://206.72.199.180:9990/;"                           
                               ref = eServiceReference(4097, 0, url)
                               ref.setName(Version_1) 
                               self.session.openWithCallback(self.backToIntialService, ALAJREStream5, ref) 
                        elif returnValue =="com_101":
                            if connected_to_internet():
                               from enigma import eServiceReference
                               from Plugins.Extensions.FreeServer.outils.InfoBar import ALAJREStream5
                               url = "https://stream.zeno.fm/yeg36tua9a0uv"                           
                               ref = eServiceReference(4097, 0, url)
                               ref.setName(Version_1)
                               self.session.openWithCallback(self.backToIntialService, ALAJREStream5, ref) 
                        elif returnValue =="com_102":
                            if connected_to_internet():
                               from enigma import eServiceReference
                               from Plugins.Extensions.FreeServer.outils.InfoBar import ALAJREStream5
                               url = "http://streamer5.rightclickitservices.com:9755/stream"                           
                               ref = eServiceReference(4097, 0, url)
                               ref.setName(Version_1)
                               self.session.openWithCallback(self.backToIntialService, ALAJREStream5, ref) 
                        elif returnValue =="com_103":
                            if connected_to_internet():
                               from enigma import eServiceReference
                               from Plugins.Extensions.FreeServer.outils.InfoBar import ALAJREStream5
                               url = "https://islamicl.radioca.st/;"                           
                               ref = eServiceReference(4097, 0, url)
                               ref.setName(Version_1)
                               self.session.openWithCallback(self.backToIntialService, ALAJREStream5, ref) 
                        elif returnValue =="com_104":
                            if connected_to_internet():
                               from enigma import eServiceReference
                               from Plugins.Extensions.FreeServer.outils.InfoBar import ALAJREStream5
                               url = "https://stream.laut.fm/gh1"                           
                               ref = eServiceReference(4097, 0, url)
                               ref.setName(Version_1) 
                               self.session.openWithCallback(self.backToIntialService, ALAJREStream5, ref)  
                        elif returnValue =="com_105":
                            if connected_to_internet():
                               from enigma import eServiceReference
                               from Plugins.Extensions.FreeServer.outils.InfoBar import ALAJREStream5
                               url = "https://stream.rcs.revma.com/cy0s94xf268uv"                           
                               ref = eServiceReference(4097, 0, url)
                               ref.setName(Version_1)
                               self.session.openWithCallback(self.backToIntialService, ALAJREStream5, ref) 
                        elif returnValue =="com_106":
                            if connected_to_internet():
                               from enigma import eServiceReference
                               from Plugins.Extensions.FreeServer.outils.InfoBar import ALAJREStream5
                               url = "http://209.58.160.62:11162/stream"                           
                               ref = eServiceReference(4097, 0, url)
                               ref.setName(Version_1)
                               self.session.openWithCallback(self.backToIntialService, ALAJREStream5, ref) 
                        elif returnValue =="com_107":
                            if connected_to_internet():
                               from enigma import eServiceReference
                               from Plugins.Extensions.FreeServer.outils.InfoBar import ALAJREStream5
                               url = "http://104.167.2.55:8000/;"                           
                               ref = eServiceReference(4097, 0, url)
                               ref.setName(Version_1)
                               self.session.openWithCallback(self.backToIntialService, ALAJREStream5, ref) 
                        elif returnValue =="com_108":
                            if connected_to_internet():
                               from enigma import eServiceReference
                               from Plugins.Extensions.FreeServer.outils.InfoBar import ALAJREStream5
                               url = "https://shabir.radioca.st/;"                           
                               ref = eServiceReference(4097, 0, url)
                               ref.setName(Version_1)
                               self.session.openWithCallback(self.backToIntialService, ALAJREStream5, ref) 
                        elif returnValue =="com_109":
                            if connected_to_internet():
                               from enigma import eServiceReference
                               from Plugins.Extensions.FreeServer.outils.InfoBar import ALAJREStream5
                               url = "http://voiceofislam.appsunder.com:8000/voiceofislam.mp3"                           
                               ref = eServiceReference(4097, 0, url)
                               ref.setName(Version_1)
                               self.session.openWithCallback(self.backToIntialService, ALAJREStream5, ref) 
                        elif returnValue =="com_110":
                            if connected_to_internet():
                               from enigma import eServiceReference
                               from Plugins.Extensions.FreeServer.outils.InfoBar import ALAJREStream5
                               url = "https://stream.zeno.fm/vp59hnkmkzzuv"                           
                               ref = eServiceReference(4097, 0, url)
                               ref.setName(Version_1)
                               self.session.openWithCallback(self.backToIntialService, ALAJREStream5, ref) 
                        elif returnValue =="com_111":
                            if connected_to_internet():
                               from enigma import eServiceReference
                               from Plugins.Extensions.FreeServer.outils.InfoBar import ALAJREStream5
                               url = "https://stream.zeno.fm/yeg36tua9a0uv"                           
                               ref = eServiceReference(4097, 0, url)
                               ref.setName(Version_1)
                               self.session.openWithCallback(self.backToIntialService, ALAJREStream5, ref) 
                        elif returnValue =="com_112":
                            if connected_to_internet():
                               from enigma import eServiceReference
                               from Plugins.Extensions.FreeServer.outils.InfoBar import ALAJREStream5
                               url = "http://104.194.9.142:8302/live"                           
                               ref = eServiceReference(4097, 0, url)
                               ref.setName(Version_1)
                               self.session.openWithCallback(self.backToIntialService, ALAJREStream5, ref) 
                        elif returnValue =="com_113":
                            if connected_to_internet():
                               from enigma import eServiceReference
                               from Plugins.Extensions.FreeServer.outils.InfoBar import ALAJREStream5
                               url = "http://s1.wohooo.net:9018/;"                           
                               ref = eServiceReference(4097, 0, url)
                               ref.setName(Version_1)
                               self.session.openWithCallback(self.backToIntialService, ALAJREStream5, ref) 
                        elif returnValue =="com_114":
                            if connected_to_internet():
                               from enigma import eServiceReference
                               from Plugins.Extensions.FreeServer.outils.InfoBar import ALAJREStream5
                               url = "http://eu3.fastcast4u.com:5762/;stream.nsv"                           
                               ref = eServiceReference(4097, 0, url)
                               ref.setName(Version_1) 
                               self.session.openWithCallback(self.backToIntialService, ALAJREStream5, ref) 
                        elif returnValue =="com_115":
                            if connected_to_internet():
                               from enigma import eServiceReference
                               from Plugins.Extensions.FreeServer.outils.InfoBar import ALAJREStream5
                               url = "http://95.173.161.133:9394/;stream.nsv"                           
                               ref = eServiceReference(4097, 0, url)
                               ref.setName(Version_1)
                               self.session.openWithCallback(self.backToIntialService, ALAJREStream5, ref) 
                        elif returnValue =="com_116":
                            if connected_to_internet():
                               from enigma import eServiceReference
                               from Plugins.Extensions.FreeServer.outils.InfoBar import ALAJREStream5
                               url = "https://www.qurantranslations.net/sound/English/AbdulBaset_AbdulSamad/002.mp3?type=.mp3/;stream.mp3"                           
                               ref = eServiceReference(4097, 0, url)
                               ref.setName(Version_1)
                               self.session.openWithCallback(self.backToIntialService, ALAJREStream5, ref) 
                        elif returnValue =="com_117":
                            if connected_to_internet():
                               from enigma import eServiceReference
                               from Plugins.Extensions.FreeServer.outils.InfoBar import ALAJREStream5
                               url = "https://streamer.radio.co/sc0a077d6e/listen"                           
                               ref = eServiceReference(4097, 0, url)
                               ref.setName(Version_1)
                               self.session.openWithCallback(self.backToIntialService, ALAJREStream5, ref) 
                        elif returnValue =="com_118":
                            if connected_to_internet():
                               from enigma import eServiceReference
                               from Plugins.Extensions.FreeServer.outils.InfoBar import ALAJREStream5
                               url = "https://radio.mayotte-streaming.com/8006/stream"                           
                               ref = eServiceReference(4097, 0, url)
                               ref.setName(Version_1) 
                               self.session.openWithCallback(self.backToIntialService, ALAJREStream5, ref)  
                        elif returnValue =="com_119":
                            if connected_to_internet():
                               from enigma import eServiceReference
                               from Plugins.Extensions.FreeServer.outils.InfoBar import ALAJREStream5
                               url = "https://bassfm.radio.yufid.com/;"                           
                               ref = eServiceReference(4097, 0, url)
                               ref.setName(Version_1)
                               self.session.openWithCallback(self.backToIntialService, ALAJREStream5, ref) 
                        elif returnValue =="com_120":
                            if connected_to_internet():
                               from enigma import eServiceReference
                               from Plugins.Extensions.FreeServer.outils.InfoBar import ALAJREStream5
                               url = "http://5.56.158.246:8000/stream"                           
                               ref = eServiceReference(4097, 0, url)
                               ref.setName(Version_1)
                               self.session.openWithCallback(self.backToIntialService, ALAJREStream5, ref) 
                        elif returnValue =="com_121":
                            if connected_to_internet():
                               from enigma import eServiceReference
                               from Plugins.Extensions.FreeServer.outils.InfoBar import ALAJREStream5
                               url = "http://yayin2.canliyayin.org:8400/;stream.nsv"                           
                               ref = eServiceReference(4097, 0, url)
                               ref.setName(Version_1)
                               self.session.openWithCallback(self.backToIntialService, ALAJREStream5, ref) 
                        elif returnValue =="com_122":
                            if connected_to_internet():
                               from enigma import eServiceReference
                               from Plugins.Extensions.FreeServer.outils.InfoBar import ALAJREStream5
                               url = "http://5.9.65.9:8031/live?1508938696879"                           
                               ref = eServiceReference(4097, 0, url)
                               ref.setName(Version_1)
                               self.session.openWithCallback(self.backToIntialService, ALAJREStream5, ref) 
                        elif returnValue =="com_123":
                            if connected_to_internet():
                               from enigma import eServiceReference
                               from Plugins.Extensions.FreeServer.outils.InfoBar import ALAJREStream5
                               url = "https://stream.zeno.fm/hnp45knerm0uv"                           
                               ref = eServiceReference(4097, 0, url)
                               ref.setName(Version_1)
                               self.session.openWithCallback(self.backToIntialService, ALAJREStream5, ref) 
                        elif returnValue =="com_124":
                            if connected_to_internet():
                               from enigma import eServiceReference
                               from Plugins.Extensions.FreeServer.outils.InfoBar import ALAJREStream5
                               url = "https://nour-webradio.ice.infomaniak.ch/nour-webradio.mayotte-32.aac"                           
                               ref = eServiceReference(4097, 0, url)
                               ref.setName(Version_1) 
                               self.session.openWithCallback(self.backToIntialService, ALAJREStream5, ref) 
                        elif returnValue =="com_125":
                            if connected_to_internet():
                               from enigma import eServiceReference
                               from Plugins.Extensions.FreeServer.outils.InfoBar import ALAJREStream5
                               url = "https://server03.quran.com.kw:7033/;*.mp3"                           
                               ref = eServiceReference(4097, 0, url)
                               ref.setName(Version_1)
                               self.session.openWithCallback(self.backToIntialService, ALAJREStream5, ref) 
                        elif returnValue =="com_126":
                            if connected_to_internet():
                               from enigma import eServiceReference
                               from Plugins.Extensions.FreeServer.outils.InfoBar import ALAJREStream5
                               url = "http://quraan.us:9892/;*.mp3"                           
                               ref = eServiceReference(4097, 0, url)
                               ref.setName(Version_1)
                               self.session.openWithCallback(self.backToIntialService, ALAJREStream5, ref) 
                        elif returnValue =="com_127":
                            if connected_to_internet():
                               from enigma import eServiceReference
                               from Plugins.Extensions.FreeServer.outils.InfoBar import ALAJREStream5
                               url = "https://server03.quran.com.kw:7038/;*.mp3"                           
                               ref = eServiceReference(4097, 0, url)
                               ref.setName(Version_1)
                               self.session.openWithCallback(self.backToIntialService, ALAJREStream5, ref)  
                        elif returnValue =="com_128":
                            if connected_to_internet():
                               from enigma import eServiceReference
                               from Plugins.Extensions.FreeServer.outils.InfoBar import ALAJREStream5
                               url = "https://server03.quran.com.kw:7034/;*.mp3"                           
                               ref = eServiceReference(4097, 0, url)
                               ref.setName(Version_1) 
                               self.session.openWithCallback(self.backToIntialService, ALAJREStream5, ref) 
                        elif returnValue =="com_129":
                            if connected_to_internet():
                               from enigma import eServiceReference
                               from Plugins.Extensions.FreeServer.outils.InfoBar import ALAJREStream5
                               url = "https://server03.quran.com.kw:7036/;*.mp3"                           
                               ref = eServiceReference(4097, 0, url)
                               ref.setName(Version_1) 
                               self.session.openWithCallback(self.backToIntialService, ALAJREStream5, ref)  
                        elif returnValue =="com_130":
                            if connected_to_internet():
                               from enigma import eServiceReference
                               from Plugins.Extensions.FreeServer.outils.InfoBar import ALAJREStream5
                               url = "https://server03.quran.com.kw:7036/;*.mp3"                           
                               ref = eServiceReference(4097, 0, url)
                               ref.setName(Version_1) 
                               self.session.openWithCallback(self.backToIntialService, ALAJREStream5, ref)  
                        elif returnValue =="com_131":
                            if connected_to_internet():
                               from enigma import eServiceReference
                               from Plugins.Extensions.FreeServer.outils.InfoBar import ALAJREStream5
                               url = "https://radiodawn.radioca.st/stream"                           
                               ref = eServiceReference(4097, 0, url)
                               ref.setName(Version_1) 
                               self.session.openWithCallback(self.backToIntialService, ALAJREStream5, ref)
                        elif returnValue =="com_132":
                            if connected_to_internet():
                               from enigma import eServiceReference
                               from Plugins.Extensions.FreeServer.outils.InfoBar import ALAJREStream5
                               url = "https://stream.zeno.fm/vp59hnkmkzzuv"                          
                               ref = eServiceReference(4097, 0, url)
                               ref.setName(Version_1) 
                               self.session.openWithCallback(self.backToIntialService, ALAJREStream5, ref)   
                        elif returnValue =="com_133":
                            if connected_to_internet():
                               from enigma import eServiceReference
                               from Plugins.Extensions.FreeServer.outils.InfoBar import ALAJREStream5
                               url = "http://streamer5.rightclickitservices.com:9755/stream "                           
                               ref = eServiceReference(4097, 0, url)
                               ref.setName(Version_1)
                               self.session.openWithCallback(self.backToIntialService, ALAJREStream5, ref) 
                        elif returnValue =="com_134":
                            if connected_to_internet():
                               from enigma import eServiceReference
                               from Plugins.Extensions.FreeServer.outils.InfoBar import ALAJREStream5
                               url = "https://stream.zeno.fm/yeg36tua9a0uv"                           
                               ref = eServiceReference(4097, 0, url)
                               ref.setName(Version_1)
                               self.session.openWithCallback(self.backToIntialService, ALAJREStream5, ref) 
                        elif returnValue =="com_135":
                            if connected_to_internet():
                               from enigma import eServiceReference
                               from Plugins.Extensions.FreeServer.outils.InfoBar import ALAJREStream5
                               url = "http://pu.klikhost.com:8146/live"                           
                               ref = eServiceReference(4097, 0, url)
                               ref.setName(Version_1) 
                               self.session.openWithCallback(self.backToIntialService, ALAJREStream5, ref) 
                        elif returnValue =="com_136":
                            if connected_to_internet():
                               from enigma import eServiceReference
                               from Plugins.Extensions.FreeServer.outils.InfoBar import ALAJREStream5
                               url = "https://s2.voscast.com:9357/stream"                           
                               ref = eServiceReference(4097, 0, url)
                               ref.setName(Version_1)
                               self.session.openWithCallback(self.backToIntialService, ALAJREStream5, ref) 
                        elif returnValue =="com_137":
                            if connected_to_internet():
                               from enigma import eServiceReference
                               from Plugins.Extensions.FreeServer.outils.InfoBar import ALAJREStream5
                               url = "http://95.154.250.9:9300/;stream.nsv"                           
                               ref = eServiceReference(4097, 0, url)
                               ref.setName(Version_1)
                               self.session.openWithCallback(self.backToIntialService, ALAJREStream5, ref) 
                        elif returnValue =="com_138":
                            if connected_to_internet():
                               from enigma import eServiceReference
                               from Plugins.Extensions.FreeServer.outils.InfoBar import ALAJREStream5
                               url = "https://sawtelghad.org:7001/;"                           
                               ref = eServiceReference(4097, 0, url)
                               ref.setName(Version_1)
                               self.session.openWithCallback(self.backToIntialService, ALAJREStream5, ref) 
                        elif returnValue =="com_139":
                            if connected_to_internet():
                               from enigma import eServiceReference
                               from Plugins.Extensions.FreeServer.outils.InfoBar import ALAJREStream5
                               url = "https://stream.zeno.fm/z3f462xp1uhvv"                           
                               ref = eServiceReference(4097, 0, url)
                               ref.setName(Version_1) 
                               self.session.openWithCallback(self.backToIntialService, ALAJREStream5, ref)  
                        elif returnValue =="com_140":
                            if connected_to_internet():
                               from enigma import eServiceReference
                               from Plugins.Extensions.FreeServer.outils.InfoBar import ALAJREStream5
                               url = "https://stream.zeno.fm/n8bd6q1k1c9uv"                           
                               ref = eServiceReference(4097, 0, url)
                               ref.setName(Version_1)
                               self.session.openWithCallback(self.backToIntialService, ALAJREStream5, ref) 
                        elif returnValue =="com_141":
                            if connected_to_internet():
                               from enigma import eServiceReference
                               from Plugins.Extensions.FreeServer.outils.InfoBar import ALAJREStream5
                               url = "https://edge.iono.fm/xice/109_medium.aac"                           
                               ref = eServiceReference(4097, 0, url)
                               ref.setName(Version_1)
                               self.session.openWithCallback(self.backToIntialService, ALAJREStream5, ref) 
                        elif returnValue =="com_142":
                            if connected_to_internet():
                               from enigma import eServiceReference
                               from Plugins.Extensions.FreeServer.outils.InfoBar import ALAJREStream5
                               url = "https://radio.mayotte-streaming.com/8006/stream"                           
                               ref = eServiceReference(4097, 0, url)
                               ref.setName(Version_1)
                               self.session.openWithCallback(self.backToIntialService, ALAJREStream5, ref) 
                        elif returnValue =="com_143":
                            if connected_to_internet():
                               from enigma import eServiceReference
                               from Plugins.Extensions.FreeServer.outils.InfoBar import ALAJREStream5
                               url = "https://stream.rcs.revma.com/cy0s94xf268uv"                           
                               ref = eServiceReference(4097, 0, url)
                               ref.setName(Version_1)
                               self.session.openWithCallback(self.backToIntialService, ALAJREStream5, ref) 
                        elif returnValue =="com_144":
                            if connected_to_internet():
                               from enigma import eServiceReference
                               from Plugins.Extensions.FreeServer.outils.InfoBar import ALAJREStream5
                               url = "http://live.radyotvonline.com:8150/;"                           
                               ref = eServiceReference(4097, 0, url)
                               ref.setName(Version_1)
                               self.session.openWithCallback(self.backToIntialService, ALAJREStream5, ref) 
                        elif returnValue =="com_145":
                            if connected_to_internet():
                               from enigma import eServiceReference
                               from Plugins.Extensions.FreeServer.outils.InfoBar import ALAJREStream5
                               url = "http://streamer3.rightclickitservices.com:9755/;"                           
                               ref = eServiceReference(4097, 0, url)
                               ref.setName(Version_1)
                               self.session.openWithCallback(self.backToIntialService, ALAJREStream5, ref) 
                        elif returnValue =="com_146":
                            if connected_to_internet():
                               from enigma import eServiceReference
                               from Plugins.Extensions.FreeServer.outils.InfoBar import ALAJREStream5
                               url = "http://rtvpendimi.com:8020/;stream.nsv"                           
                               ref = eServiceReference(4097, 0, url)
                               ref.setName(Version_1)
                               self.session.openWithCallback(self.backToIntialService, ALAJREStream5, ref) 
                        elif returnValue =="com_147":
                            if connected_to_internet():
                               from enigma import eServiceReference
                               from Plugins.Extensions.FreeServer.outils.InfoBar import ALAJREStream5
                               url = "http://104.194.9.142:8302/live"                           
                               ref = eServiceReference(4097, 0, url)
                               ref.setName(Version_1)
                               self.session.openWithCallback(self.backToIntialService, ALAJREStream5, ref) 
                        elif returnValue =="com_148":
                            if connected_to_internet():
                               from enigma import eServiceReference
                               from Plugins.Extensions.FreeServer.outils.InfoBar import ALAJREStream5
                               url = "https://ramadhan786.radioca.st/stream"                           
                               ref = eServiceReference(4097, 0, url)
                               ref.setName(Version_1)
                               self.session.openWithCallback(self.backToIntialService, ALAJREStream5, ref) 
                        elif returnValue =="com_149":
                            if connected_to_internet():
                               from enigma import eServiceReference
                               from Plugins.Extensions.FreeServer.outils.InfoBar import ALAJREStream5
                               url = "http://server2.quraan.us:9896/;*.mp3"                           
                               ref = eServiceReference(4097, 0, url)
                               ref.setName(Version_1) 
                               self.session.openWithCallback(self.backToIntialService, ALAJREStream5, ref) 
                        elif returnValue =="com_150":
                            if connected_to_internet():
                               from enigma import eServiceReference
                               from Plugins.Extensions.FreeServer.outils.InfoBar import ALAJREStream5
                               url = "https://server03.quran.com.kw:7033/;*.mp3"                           
                               ref = eServiceReference(4097, 0, url)
                               ref.setName(Version_1)
                               self.session.openWithCallback(self.backToIntialService, ALAJREStream5, ref) 
                        elif returnValue =="com_151":
                            if connected_to_internet():
                               from enigma import eServiceReference
                               from Plugins.Extensions.FreeServer.outils.InfoBar import ALAJREStream5
                               url = "http://live.syaria.net:9306/;stream.nsv"                           
                               ref = eServiceReference(4097, 0, url)
                               ref.setName(Version_1)
                               self.session.openWithCallback(self.backToIntialService, ALAJREStream5, ref) 
                        elif returnValue =="com_152":
                            if connected_to_internet():
                               from enigma import eServiceReference
                               from Plugins.Extensions.FreeServer.outils.InfoBar import ALAJREStream5
                               url = "http://server2.quraan.us:9814/;*.mp3"                           
                               ref = eServiceReference(4097, 0, url)
                               ref.setName(Version_1)
                               self.session.openWithCallback(self.backToIntialService, ALAJREStream5, ref) 
                        elif returnValue =="com_153":
                            if connected_to_internet():
                               from enigma import eServiceReference
                               from Plugins.Extensions.FreeServer.outils.InfoBar import ALAJREStream5
                               url = "http://5.9.65.9:8031/live?1508938696879"                           
                               ref = eServiceReference(4097, 0, url)
                               ref.setName(Version_1) 
                               self.session.openWithCallback(self.backToIntialService, ALAJREStream5, ref)  
                        elif returnValue =="com_154":
                            if connected_to_internet():
                               from enigma import eServiceReference
                               from Plugins.Extensions.FreeServer.outils.InfoBar import ALAJREStream5     
                               url = "http://server2.quraan.us:9886/;*.mp3"                           
                               ref = eServiceReference(4097, 0, url)
                               ref.setName(Version_1)
                               self.session.openWithCallback(self.backToIntialService, ALAJREStream5, ref) 
                        elif returnValue =="com_155":
                            if connected_to_internet():
                               from enigma import eServiceReference
                               from Plugins.Extensions.FreeServer.outils.InfoBar import ALAJREStream5
                               url = "http://quraan.us:9892/;*.mp3"                           
                               ref = eServiceReference(4097, 0, url)
                               ref.setName(Version_1)
                               self.session.openWithCallback(self.backToIntialService, ALAJREStream5, ref) 
                        elif returnValue =="com_156":
                            if connected_to_internet():
                               from enigma import eServiceReference
                               from Plugins.Extensions.FreeServer.outils.InfoBar import ALAJREStream5
                               url = "http://quraan.us:9912/;*.mp3"                           
                               ref = eServiceReference(4097, 0, url)
                               ref.setName(Version_1)
                               self.session.openWithCallback(self.backToIntialService, ALAJREStream5, ref) 
                        elif returnValue =="com_157":
                            if connected_to_internet():
                               from enigma import eServiceReference
                               from Plugins.Extensions.FreeServer.outils.InfoBar import ALAJREStream5
                               url = "http://quraan.us:9884/;*.mp3"                           
                               ref = eServiceReference(4097, 0, url)
                               ref.setName(Version_1)
                               self.session.openWithCallback(self.backToIntialService, ALAJREStream5, ref) 
                        elif returnValue =="com_158":
                            if connected_to_internet():
                               from enigma import eServiceReference
                               from Plugins.Extensions.FreeServer.outils.InfoBar import ALAJREStream5
                               url = "http://quraan.us:9902/;*.mp3"                           
                               ref = eServiceReference(4097, 0, url)
                               ref.setName(Version_1)
                               self.session.openWithCallback(self.backToIntialService, ALAJREStream5, ref) 
                        elif returnValue =="com_159":
                            if connected_to_internet():
                               from enigma import eServiceReference
                               from Plugins.Extensions.FreeServer.outils.InfoBar import ALAJREStream5
                               url = "http://quraan.us:9894/;*.mp3"                           
                               ref = eServiceReference(4097, 0, url)
                               ref.setName(Version_1)
                               self.session.openWithCallback(self.backToIntialService, ALAJREStream5, ref) 
                        elif returnValue =="com_160":
                            if connected_to_internet():
                               from enigma import eServiceReference
                               from Plugins.Extensions.FreeServer.outils.InfoBar import ALAJREStream5
                               url = "http://server2.quraan.us:9898/;*.mp3"                           
                               ref = eServiceReference(4097, 0, url)
                               ref.setName(Version_1) 
                               self.session.openWithCallback(self.backToIntialService, ALAJREStream5, ref) 
                        elif returnValue =="com_161":
                            if connected_to_internet():
                               from enigma import eServiceReference
                               from Plugins.Extensions.FreeServer.outils.InfoBar import ALAJREStream5
                               url = "https://server03.quran.com.kw:7038/;*.mp3"                           
                               ref = eServiceReference(4097, 0, url)
                               ref.setName(Version_1)
                               self.session.openWithCallback(self.backToIntialService, ALAJREStream5, ref) 
                        elif returnValue =="com_162":
                            if connected_to_internet():
                               from enigma import eServiceReference
                               from Plugins.Extensions.FreeServer.outils.InfoBar import ALAJREStream5
                               url = "https://server03.quran.com.kw:7034/;*.mp3"                           
                               ref = eServiceReference(4097, 0, url)
                               ref.setName(Version_1)
                               self.session.openWithCallback(self.backToIntialService, ALAJREStream5, ref) 
                        elif returnValue =="com_163":
                            if connected_to_internet():
                               from enigma import eServiceReference
                               from Plugins.Extensions.FreeServer.outils.InfoBar import ALAJREStream5
                               url = "https://s2.voscast.com:9357/stream"                           
                               ref = eServiceReference(4097, 0, url)
                               ref.setName(Version_1)
                               self.session.openWithCallback(self.backToIntialService, ALAJREStream5, ref)  
                        elif returnValue =="com_164":
                            if connected_to_internet():
                               from enigma import eServiceReference
                               from Plugins.Extensions.FreeServer.outils.InfoBar import ALAJREStream5
                               url = "https://stream.zeno.fm/hnp45knerm0uv"                           
                               ref = eServiceReference(4097, 0, url)
                               ref.setName(Version_1) 
                               self.session.openWithCallback(self.backToIntialService, ALAJREStream5, ref) 
                        elif returnValue =="com_165":
                            if connected_to_internet():
                               from enigma import eServiceReference
                               from Plugins.Extensions.FreeServer.outils.InfoBar import ALAJREStream5
                               url = "http://tijaniyyah.asuscomm.com:8000/stream/4/"                           
                               ref = eServiceReference(4097, 0, url)
                               ref.setName(Version_1) 
                               self.session.openWithCallback(self.backToIntialService, ALAJREStream5, ref)  
                        elif returnValue =="com_166":
                            if connected_to_internet():
                               from enigma import eServiceReference
                               from Plugins.Extensions.FreeServer.outils.InfoBar import ALAJREStream5
                               url = "http://92.222.103.13:8005/;stream.nsv"                           
                               ref = eServiceReference(4097, 0, url)
                               ref.setName(Version_1) 
                               self.session.openWithCallback(self.backToIntialService, ALAJREStream5, ref)  
                        elif returnValue =="com_167":
                            if connected_to_internet():
                               from enigma import eServiceReference
                               from Plugins.Extensions.FreeServer.outils.InfoBar import ALAJREStream5
                               url = "http://listen.qkradio.com.au:8382/listen.mp3"                           
                               ref = eServiceReference(4097, 0, url)
                               ref.setName(Version_1) 
                               self.session.openWithCallback(self.backToIntialService, ALAJREStream5, ref)
                        elif returnValue =="com_168":
                            if connected_to_internet():
                               from enigma import eServiceReference
                               from Plugins.Extensions.FreeServer.outils.InfoBar import ALAJREStream5
                               url = "http://qurango.net/radio/abdulbari_mohammad"                           
                               ref = eServiceReference(4097, 0, url)
                               ref.setName(Version_1)
                               self.session.openWithCallback(self.backToIntialService, ALAJREStream5, ref) 
                        elif returnValue =="com_169":
                            if connected_to_internet():
                               from enigma import eServiceReference
                               from Plugins.Extensions.FreeServer.outils.InfoBar import ALAJREStream5
                               url = "http://server2.quraan.us:9810/stream/;"                           
                               ref = eServiceReference(4097, 0, url)
                               ref.setName(Version_1)
                               self.session.openWithCallback(self.backToIntialService, ALAJREStream5, ref) 
                        elif returnValue =="com_170":
                            if connected_to_internet():
                               from enigma import eServiceReference
                               from Plugins.Extensions.FreeServer.outils.InfoBar import ALAJREStream5
                               url = "http://server2.quraan.us:9814/stream/;"                           
                               ref = eServiceReference(4097, 0, url)
                               ref.setName(Version_1) 
                               self.session.openWithCallback(self.backToIntialService, ALAJREStream5, ref) 
                        elif returnValue =="com_171":
                            if connected_to_internet():
                               from enigma import eServiceReference
                               from Plugins.Extensions.FreeServer.outils.InfoBar import ALAJREStream5
                               url = "http://79.137.32.10:8000/;;"                           
                               ref = eServiceReference(4097, 0, url)
                               ref.setName(Version_1)
                               self.session.openWithCallback(self.backToIntialService, ALAJREStream5, ref) 
                        elif returnValue =="com_172":
                            if connected_to_internet():
                               from enigma import eServiceReference
                               from Plugins.Extensions.FreeServer.outils.InfoBar import ALAJREStream5
                               url = "http://radio.rayhan.eu:8000/radio.mp3"                           
                               ref = eServiceReference(4097, 0, url)
                               ref.setName(Version_1)
                               self.session.openWithCallback(self.backToIntialService, ALAJREStream5, ref) 
                        elif returnValue =="com_173":
                            if connected_to_internet():
                               from enigma import eServiceReference
                               from Plugins.Extensions.FreeServer.outils.InfoBar import ALAJREStream5
                               url = "http://95.154.250.9:9300/;"                           
                               ref = eServiceReference(4097, 0, url)
                               ref.setName(Version_1)
                               self.session.openWithCallback(self.backToIntialService, ALAJREStream5, ref)  
                        elif returnValue =="com_174":
                            if connected_to_internet():
                               from enigma import eServiceReference
                               from Plugins.Extensions.FreeServer.outils.InfoBar import ALAJREStream5
                               url = "https://stream.zeno.fm/wu9yvyuzpnhvv"                           
                               ref = eServiceReference(4097, 0, url)
                               ref.setName(Version_1) 
                               self.session.openWithCallback(self.backToIntialService, ALAJREStream5, ref) 
                        elif returnValue =="com_175":
                            if connected_to_internet():
                               from enigma import eServiceReference
                               from Plugins.Extensions.FreeServer.outils.InfoBar import ALAJREStream5
                               url = "http://eu4.fastcast4u.com:5458/;.mp3"                           
                               ref = eServiceReference(4097, 0, url)
                               ref.setName(Version_1) 
                               self.session.openWithCallback(self.backToIntialService, ALAJREStream5, ref)  
                        elif returnValue =="com_176":
                            if connected_to_internet():
                               from enigma import eServiceReference
                               from Plugins.Extensions.FreeServer.outils.InfoBar import ALAJREStream5
                               url = "https://Nour-webradio.ice.infomaniak.ch/nour-webradio.mayotte-32.aac"                           
                               ref = eServiceReference(4097, 0, url)
                               ref.setName(Version_1) 
                               self.session.openWithCallback(self.backToIntialService, ALAJREStream5, ref)  
                        elif returnValue =="com_177":
                            if connected_to_internet():
                               from enigma import eServiceReference
                               from Plugins.Extensions.FreeServer.outils.InfoBar import ALAJREStream5
                               url = "https://stream.radiojar.com/8s5u5tpdtwzuv"                           
                               ref = eServiceReference(4097, 0, url)
                               ref.setName(Version_1) 
                               self.session.openWithCallback(self.backToIntialService, ALAJREStream5, ref)
                        elif returnValue =="com_178":
                            if connected_to_internet():
                               from enigma import eServiceReference
                               from Plugins.Extensions.FreeServer.outils.InfoBar import ALAJREStream5
                               url = "https://qurango.net/radio/mohammed_siddiq_alminshawi"                           
                               ref = eServiceReference(4097, 0, url)
                               ref.setName(Version_1)
                               self.session.openWithCallback(self.backToIntialService, ALAJREStream5, ref) 
                        elif returnValue =="com_179":
                            if connected_to_internet():
                               from enigma import eServiceReference
                               from Plugins.Extensions.FreeServer.outils.InfoBar import ALAJREStream5
                               url = "https://Qurango.net/radio/fi_zilal_alsiyra"                           
                               ref = eServiceReference(4097, 0, url)
                               ref.setName(Version_1) 
                               self.session.openWithCallback(self.backToIntialService, ALAJREStream5, ref) 
                        elif returnValue =="com_180":
                            if connected_to_internet():
                               from enigma import eServiceReference
                               from Plugins.Extensions.FreeServer.outils.InfoBar import ALAJREStream5
                               url = "https://Qurango.net/radio/alaikhtiarat_alfiqhayh_bin_baz"                           
                               ref = eServiceReference(4097, 0, url)
                               ref.setName(Version_1)
                               self.session.openWithCallback(self.backToIntialService, ALAJREStream5, ref) 
                        elif returnValue =="com_181":
                            if connected_to_internet():
                               from enigma import eServiceReference
                               from Plugins.Extensions.FreeServer.outils.InfoBar import ALAJREStream5
                               url = "https://listen.radio-coran.net:8001/live.mp3"                           
                               ref = eServiceReference(4097, 0, url)
                               ref.setName(Version_1)
                               self.session.openWithCallback(self.backToIntialService, ALAJREStream5, ref) 
                        elif returnValue =="com_182":
                            if connected_to_internet():
                               from enigma import eServiceReference
                               from Plugins.Extensions.FreeServer.outils.InfoBar import ALAJREStream5
                               url = "http://stream.radiojar.com/4wqre23fytzuv"                           
                               ref = eServiceReference(4097, 0, url)
                               ref.setName(Version_1)
                               self.session.openWithCallback(self.backToIntialService, ALAJREStream5, ref)  
                        elif returnValue =="com_183":
                            if connected_to_internet():
                               from enigma import eServiceReference
                               from Plugins.Extensions.FreeServer.outils.InfoBar import ALAJREStream5
                               url = "https://edge.mixlr.com/channel/rwumx"                           
                               ref = eServiceReference(4097, 0, url)
                               ref.setName(Version_1) 
                               self.session.openWithCallback(self.backToIntialService, ALAJREStream5, ref) 
                        elif returnValue =="com_184":
                            if connected_to_internet():
                               from enigma import eServiceReference
                               from Plugins.Extensions.FreeServer.outils.InfoBar import ALAJREStream5
                               url = "https://radio.al7eah.net/8010/stream"                           
                               ref = eServiceReference(4097, 0, url)
                               ref.setName(Version_1) 
                               self.session.openWithCallback(self.backToIntialService, ALAJREStream5, ref)  
                        elif returnValue =="com_185":
                            if connected_to_internet():
                               from enigma import eServiceReference
                               from Plugins.Extensions.FreeServer.outils.InfoBar import ALAJREStream5
                               url = "http://islam2day.tv:9898/;"                           
                               ref = eServiceReference(4097, 0, url)
                               ref.setName(Version_1) 
                               self.session.openWithCallback(self.backToIntialService, ALAJREStream5, ref)  
                        elif returnValue =="com_186":
                            if connected_to_internet():
                               from enigma import eServiceReference
                               from Plugins.Extensions.FreeServer.outils.InfoBar import ALAJREStream5
                               url = "https://guinee.radio/listen/5865"                           
                               ref = eServiceReference(4097, 0, url)
                               ref.setName(Version_1) 
                               self.session.openWithCallback(self.backToIntialService, ALAJREStream5, ref)
                        elif returnValue =="com_187":
                            if connected_to_internet():
                               from enigma import eServiceReference
                               from Plugins.Extensions.FreeServer.outils.InfoBar import ALAJREStream5
                               url = "http://209.58.160.62:11162/stream"                           
                               ref = eServiceReference(4097, 0, url)
                               ref.setName(Version_1)
                               self.session.openWithCallback(self.backToIntialService, ALAJREStream5, ref) 
                        elif returnValue =="com_188":
                            if connected_to_internet():
                               from enigma import eServiceReference
                               from Plugins.Extensions.FreeServer.outils.InfoBar import ALAJREStream5
                               url = "http://u.klikhost.net:7102/stream"                           
                               ref = eServiceReference(4097, 0, url)
                               ref.setName(Version_1) 
                               self.session.openWithCallback(self.backToIntialService, ALAJREStream5, ref) 
                        elif returnValue =="com_189":
                            if connected_to_internet():
                               from enigma import eServiceReference
                               from Plugins.Extensions.FreeServer.outils.InfoBar import ALAJREStream5
                               url = "http://s1.voscast.com:8778/;stream.nsv"                           
                               ref = eServiceReference(4097, 0, url)
                               ref.setName(Version_1)
                               self.session.openWithCallback(self.backToIntialService, ALAJREStream5, ref) 
                        elif returnValue =="com_190":
                            if connected_to_internet():
                               from enigma import eServiceReference
                               from Plugins.Extensions.FreeServer.outils.InfoBar import ALAJREStream5
                               url = "https://stream.zeno.fm/t5gkwva794zuv"                           
                               ref = eServiceReference(4097, 0, url)
                               ref.setName(Version_1)
                               self.session.openWithCallback(self.backToIntialService, ALAJREStream5, ref) 
                        elif returnValue =="com_191":
                            if connected_to_internet():
                               from enigma import eServiceReference
                               from Plugins.Extensions.FreeServer.outils.InfoBar import ALAJREStream5
                               url = "https://server03.quran.com.kw:7033/;*.mp3"                           
                               ref = eServiceReference(4097, 0, url)
                               ref.setName(Version_1)
                               self.session.openWithCallback(self.backToIntialService, ALAJREStream5, ref)  
                        elif returnValue =="com_192":
                            if connected_to_internet():
                               from enigma import eServiceReference
                               from Plugins.Extensions.FreeServer.outils.InfoBar import ALAJREStream5
                               url = "http://server2.quraan.us:9896/;*.mp3"                           
                               ref = eServiceReference(4097, 0, url)
                               ref.setName(Version_1) 
                               self.session.openWithCallback(self.backToIntialService, ALAJREStream5, ref) 
                        elif returnValue =="com_193":
                            if connected_to_internet():
                               from enigma import eServiceReference
                               from Plugins.Extensions.FreeServer.outils.InfoBar import ALAJREStream5
                               url = "http://server2.quraan.us:9814/;*.mp3"                           
                               ref = eServiceReference(4097, 0, url)
                               ref.setName(Version_1) 
                               self.session.openWithCallback(self.backToIntialService, ALAJREStream5, ref)  
                        elif returnValue =="com_194":
                            if connected_to_internet():
                               from enigma import eServiceReference
                               from Plugins.Extensions.FreeServer.outils.InfoBar import ALAJREStream5
                               url = "https://ssg.streamingmurah.com:8022/ralfmgorontalo"                           
                               ref = eServiceReference(4097, 0, url)
                               ref.setName(Version_1) 
                               self.session.openWithCallback(self.backToIntialService, ALAJREStream5, ref)  
                        elif returnValue =="com_195":
                            if connected_to_internet():
                               from enigma import eServiceReference
                               from Plugins.Extensions.FreeServer.outils.InfoBar import ALAJREStream5
                               url = "http://server2.quraan.us:9886/;*.mp3"                           
                               ref = eServiceReference(4097, 0, url)
                               ref.setName(Version_1) 
                               self.session.openWithCallback(self.backToIntialService, ALAJREStream5, ref)
                        elif returnValue =="com_196":
                            if connected_to_internet():
                               from enigma import eServiceReference
                               from Plugins.Extensions.FreeServer.outils.InfoBar import ALAJREStream5
                               url = "http://quraan.us:9912/;*.mp3"                           
                               ref = eServiceReference(4097, 0, url)
                               ref.setName(Version_1)
                               self.session.openWithCallback(self.backToIntialService, ALAJREStream5, ref)  
                        elif returnValue =="com_197":
                            if connected_to_internet():
                               from enigma import eServiceReference
                               from Plugins.Extensions.FreeServer.outils.InfoBar import ALAJREStream5
                               url = "http://quraan.us:9894/;*.mp3"                           
                               ref = eServiceReference(4097, 0, url)
                               ref.setName(Version_1) 
                               self.session.openWithCallback(self.backToIntialService, ALAJREStream5, ref) 
                        elif returnValue =="com_198":
                            if connected_to_internet():
                               from enigma import eServiceReference
                               from Plugins.Extensions.FreeServer.outils.InfoBar import ALAJREStream5
                               url = "https://sawtelghad.org:7001/;"                           
                               ref = eServiceReference(4097, 0, url)
                               ref.setName(Version_1) 
                               self.session.openWithCallback(self.backToIntialService, ALAJREStream5, ref)  
                        elif returnValue =="com_199":
                            if connected_to_internet():
                               from enigma import eServiceReference
                               from Plugins.Extensions.FreeServer.outils.InfoBar import ALAJREStream5
                               url = "https://stream.rcs.revma.com/cy0s94xf268uv"                           
                               ref = eServiceReference(4097, 0, url)
                               ref.setName(Version_1) 
                               self.session.openWithCallback(self.backToIntialService, ALAJREStream5, ref)  
                        elif returnValue =="com_200":
                            if connected_to_internet():
                               from enigma import eServiceReference
                               from Plugins.Extensions.FreeServer.outils.InfoBar import ALAJREStream5
                               url = "https://strw1.openstream.co/2388"                           
                               ref = eServiceReference(4097, 0, url)
                               ref.setName(Version_1) 
                               self.session.openWithCallback(self.backToIntialService, ALAJREStream5, ref)   
                        elif returnValue =="com_201":
                            if connected_to_internet():
                               from enigma import eServiceReference
                               from Plugins.Extensions.FreeServer.outils.InfoBar import ALAJREStream5
                               url = "https://ia904707.us.archive.org/32/items/002_20221028/001.mp3"                           
                               ref = eServiceReference(4097, 0, url)
                               ref.setName(Version_1) 
                               self.session.openWithCallback(self.backToIntialService, ALAJREStream5, ref)
                        elif returnValue =="com_202":
                            if connected_to_internet():
                               from enigma import eServiceReference
                               from Plugins.Extensions.FreeServer.outils.InfoBar import ALAJREStream5
                               url = "https://ia904707.us.archive.org/32/items/002_20221028/002.mp3"                           
                               ref = eServiceReference(4097, 0, url)
                               ref.setName(Version_1) 
                               self.session.openWithCallback(self.backToIntialService, ALAJREStream5, ref)
                        elif returnValue =="com_203":
                            if connected_to_internet():
                               from enigma import eServiceReference
                               from Plugins.Extensions.FreeServer.outils.InfoBar import ALAJREStream5
                               url = "https://ia904707.us.archive.org/32/items/002_20221028/003.mp3"                           
                               ref = eServiceReference(4097, 0, url)
                               ref.setName(Version_1) 
                               self.session.openWithCallback(self.backToIntialService, ALAJREStream5, ref)
                        elif returnValue =="com_204":
                            if connected_to_internet():
                               from enigma import eServiceReference
                               from Plugins.Extensions.FreeServer.outils.InfoBar import ALAJREStream5
                               url = "https://ia904707.us.archive.org/32/items/002_20221028/004.mp3"                           
                               ref = eServiceReference(4097, 0, url)
                               ref.setName(Version_1) 
                               self.session.openWithCallback(self.backToIntialService, ALAJREStream5, ref)
                        elif returnValue =="com_205":
                            if connected_to_internet():
                               from enigma import eServiceReference
                               from Plugins.Extensions.FreeServer.outils.InfoBar import ALAJREStream5
                               url = "https://ia904707.us.archive.org/32/items/002_20221028/005.mp3"                           
                               ref = eServiceReference(4097, 0, url)
                               ref.setName(Version_1) 
                               self.session.openWithCallback(self.backToIntialService, ALAJREStream5, ref)
                        elif returnValue =="com_206":
                            if connected_to_internet():
                               from enigma import eServiceReference
                               from Plugins.Extensions.FreeServer.outils.InfoBar import ALAJREStream5
                               url = "https://ia904707.us.archive.org/32/items/002_20221028/006.mp3"                           
                               ref = eServiceReference(4097, 0, url)
                               ref.setName(Version_1) 
                               self.session.openWithCallback(self.backToIntialService, ALAJREStream5, ref)
                        elif returnValue =="com_207":
                            if connected_to_internet():
                               from enigma import eServiceReference
                               from Plugins.Extensions.FreeServer.outils.InfoBar import ALAJREStream5
                               url = "https://ia904707.us.archive.org/32/items/002_20221028/007.mp3"                           
                               ref = eServiceReference(4097, 0, url)
                               ref.setName(Version_1) 
                               self.session.openWithCallback(self.backToIntialService, ALAJREStream5, ref)
                        elif returnValue =="com_208":
                            if connected_to_internet():
                               from enigma import eServiceReference
                               from Plugins.Extensions.FreeServer.outils.InfoBar import ALAJREStream5
                               url = "https://ia904707.us.archive.org/32/items/002_20221028/008.mp3"                           
                               ref = eServiceReference(4097, 0, url)
                               ref.setName(Version_1) 
                               self.session.openWithCallback(self.backToIntialService, ALAJREStream5, ref)
                        elif returnValue =="com_209":
                            if connected_to_internet():
                               from enigma import eServiceReference
                               from Plugins.Extensions.FreeServer.outils.InfoBar import ALAJREStream5
                               url = "https://ia904707.us.archive.org/32/items/002_20221028/009.mp3"                           
                               ref = eServiceReference(4097, 0, url)
                               ref.setName(Version_1) 
                               self.session.openWithCallback(self.backToIntialService, ALAJREStream5, ref)
                        elif returnValue =="com_210":
                            if connected_to_internet():
                               from enigma import eServiceReference
                               from Plugins.Extensions.FreeServer.outils.InfoBar import ALAJREStream5
                               url = "https://ia904707.us.archive.org/32/items/002_20221028/010.mp3"                           
                               ref = eServiceReference(4097, 0, url)
                               ref.setName(Version_1) 
                               self.session.openWithCallback(self.backToIntialService, ALAJREStream5, ref)
                        elif returnValue =="com_211":
                            if connected_to_internet():
                               from enigma import eServiceReference
                               from Plugins.Extensions.FreeServer.outils.InfoBar import ALAJREStream5
                               url = "https://ia904707.us.archive.org/32/items/002_20221028/011.mp3"                           
                               ref = eServiceReference(4097, 0, url)
                               ref.setName(Version_1) 
                               self.session.openWithCallback(self.backToIntialService, ALAJREStream5, ref)
                        elif returnValue =="com_212":
                            if connected_to_internet():
                               from enigma import eServiceReference
                               from Plugins.Extensions.FreeServer.outils.InfoBar import ALAJREStream5
                               url = "https://ia904707.us.archive.org/32/items/002_20221028/012.mp3"                           
                               ref = eServiceReference(4097, 0, url)
                               ref.setName(Version_1) 
                               self.session.openWithCallback(self.backToIntialService, ALAJREStream5, ref)
                        elif returnValue =="com_213":
                            if connected_to_internet():
                               from enigma import eServiceReference
                               from Plugins.Extensions.FreeServer.outils.InfoBar import ALAJREStream5
                               url = "https://ia904707.us.archive.org/32/items/002_20221028/013.mp3"                           
                               ref = eServiceReference(4097, 0, url)
                               ref.setName(Version_1) 
                               self.session.openWithCallback(self.backToIntialService, ALAJREStream5, ref)
                        elif returnValue =="com_214":
                            if connected_to_internet():
                               from enigma import eServiceReference
                               from Plugins.Extensions.FreeServer.outils.InfoBar import ALAJREStream5
                               url = "https://ia904707.us.archive.org/32/items/002_20221028/014.mp3"                           
                               ref = eServiceReference(4097, 0, url)
                               ref.setName(Version_1) 
                               self.session.openWithCallback(self.backToIntialService, ALAJREStream5, ref)
                        elif returnValue =="com_215":
                            if connected_to_internet():
                               from enigma import eServiceReference
                               from Plugins.Extensions.FreeServer.outils.InfoBar import ALAJREStream5
                               url = "https://ia904707.us.archive.org/32/items/002_20221028/015.mp3"                           
                               ref = eServiceReference(4097, 0, url)
                               ref.setName(Version_1) 
                               self.session.openWithCallback(self.backToIntialService, ALAJREStream5, ref)
                        elif returnValue =="com_216":
                            if connected_to_internet():
                               from enigma import eServiceReference
                               from Plugins.Extensions.FreeServer.outils.InfoBar import ALAJREStream5
                               url = "https://ia904707.us.archive.org/32/items/002_20221028/016.mp3"                           
                               ref = eServiceReference(4097, 0, url)
                               ref.setName(Version_1) 
                               self.session.openWithCallback(self.backToIntialService, ALAJREStream5, ref)
                        elif returnValue =="com_217":
                            if connected_to_internet():
                               from enigma import eServiceReference
                               from Plugins.Extensions.FreeServer.outils.InfoBar import ALAJREStream5
                               url = "https://ia904707.us.archive.org/32/items/002_20221028/017.mp3"                           
                               ref = eServiceReference(4097, 0, url)
                               ref.setName(Version_1) 
                               self.session.openWithCallback(self.backToIntialService, ALAJREStream5, ref)
                        elif returnValue =="com_218":
                            if connected_to_internet():
                               from enigma import eServiceReference
                               from Plugins.Extensions.FreeServer.outils.InfoBar import ALAJREStream5
                               url = "https://ia904707.us.archive.org/32/items/002_20221028/018.mp3"                           
                               ref = eServiceReference(4097, 0, url)
                               ref.setName(Version_1) 
                               self.session.openWithCallback(self.backToIntialService, ALAJREStream5, ref)
                        elif returnValue =="com_219":
                            if connected_to_internet():
                               from enigma import eServiceReference
                               from Plugins.Extensions.FreeServer.outils.InfoBar import ALAJREStream5
                               url = "https://ia904707.us.archive.org/32/items/002_20221028/019.mp3"                           
                               ref = eServiceReference(4097, 0, url)
                               ref.setName(Version_1) 
                               self.session.openWithCallback(self.backToIntialService, ALAJREStream5, ref)                                          
                        elif returnValue =="com_220":
                            if connected_to_internet():
                               from enigma import eServiceReference
                               from Plugins.Extensions.FreeServer.outils.InfoBar import ALAJREStream5
                               url = "https://ia904707.us.archive.org/32/items/002_20221028/020.mp3"                           
                               ref = eServiceReference(4097, 0, url)
                               ref.setName(Version_1) 
                               self.session.openWithCallback(self.backToIntialService, ALAJREStream5, ref)
                        elif returnValue =="com_221":
                            if connected_to_internet():
                               from enigma import eServiceReference
                               from Plugins.Extensions.FreeServer.outils.InfoBar import ALAJREStream5
                               url = "https://ia904707.us.archive.org/32/items/002_20221028/021.mp3"                           
                               ref = eServiceReference(4097, 0, url)
                               ref.setName(Version_1) 
                               self.session.openWithCallback(self.backToIntialService, ALAJREStream5, ref)
                        elif returnValue =="com_222":
                            if connected_to_internet():
                               from enigma import eServiceReference
                               from Plugins.Extensions.FreeServer.outils.InfoBar import ALAJREStream5
                               url = "https://ia904707.us.archive.org/32/items/002_20221028/022.mp3"                           
                               ref = eServiceReference(4097, 0, url)
                               ref.setName(Version_1) 
                               self.session.openWithCallback(self.backToIntialService, ALAJREStream5, ref)
                        elif returnValue =="com_223":
                            if connected_to_internet():
                               from enigma import eServiceReference
                               from Plugins.Extensions.FreeServer.outils.InfoBar import ALAJREStream5
                               url = "https://ia904707.us.archive.org/32/items/002_20221028/023.mp3"                           
                               ref = eServiceReference(4097, 0, url)
                               ref.setName(Version_1) 
                               self.session.openWithCallback(self.backToIntialService, ALAJREStream5, ref)
                        elif returnValue =="com_224":
                            if connected_to_internet():
                               from enigma import eServiceReference
                               from Plugins.Extensions.FreeServer.outils.InfoBar import ALAJREStream5
                               url = "https://ia904707.us.archive.org/32/items/002_20221028/024.mp3"                           
                               ref = eServiceReference(4097, 0, url)
                               ref.setName(Version_1) 
                               self.session.openWithCallback(self.backToIntialService, ALAJREStream5, ref)
                        elif returnValue =="com_225":
                            if connected_to_internet():
                               from enigma import eServiceReference
                               from Plugins.Extensions.FreeServer.outils.InfoBar import ALAJREStream5
                               url = "https://ia904707.us.archive.org/32/items/002_20221028/025.mp3"                           
                               ref = eServiceReference(4097, 0, url)
                               ref.setName(Version_1) 
                               self.session.openWithCallback(self.backToIntialService, ALAJREStream5, ref)
                        elif returnValue =="com_226":
                            if connected_to_internet():
                               from enigma import eServiceReference
                               from Plugins.Extensions.FreeServer.outils.InfoBar import ALAJREStream5
                               url = "https://ia904707.us.archive.org/32/items/002_20221028/026.mp3"                           
                               ref = eServiceReference(4097, 0, url)
                               ref.setName(Version_1) 
                               self.session.openWithCallback(self.backToIntialService, ALAJREStream5, ref)
                        elif returnValue =="com_227":
                            if connected_to_internet():
                               from enigma import eServiceReference
                               from Plugins.Extensions.FreeServer.outils.InfoBar import ALAJREStream5
                               url = "https://ia904707.us.archive.org/32/items/002_20221028/027.mp3"                           
                               ref = eServiceReference(4097, 0, url)
                               ref.setName(Version_1) 
                               self.session.openWithCallback(self.backToIntialService, ALAJREStream5, ref)
                        elif returnValue =="com_228":
                            if connected_to_internet():
                               from enigma import eServiceReference
                               from Plugins.Extensions.FreeServer.outils.InfoBar import ALAJREStream5
                               url = "https://ia904707.us.archive.org/32/items/002_20221028/028.mp3"                           
                               ref = eServiceReference(4097, 0, url)
                               ref.setName(Version_1) 
                               self.session.openWithCallback(self.backToIntialService, ALAJREStream5, ref)
                        elif returnValue =="com_229":
                            if connected_to_internet():
                               from enigma import eServiceReference
                               from Plugins.Extensions.FreeServer.outils.InfoBar import ALAJREStream5
                               url = "https://ia904707.us.archive.org/32/items/002_20221028/029.mp3"                           
                               ref = eServiceReference(4097, 0, url)
                               ref.setName(Version_1) 
                               self.session.openWithCallback(self.backToIntialService, ALAJREStream5, ref)
                        elif returnValue =="com_230":
                            if connected_to_internet():
                               from enigma import eServiceReference
                               from Plugins.Extensions.FreeServer.outils.InfoBar import ALAJREStream5
                               url = "https://ia904707.us.archive.org/32/items/002_20221028/030.mp3"                           
                               ref = eServiceReference(4097, 0, url)
                               ref.setName(Version_1) 
                               self.session.openWithCallback(self.backToIntialService, ALAJREStream5, ref)
                        elif returnValue =="com_231":
                            if connected_to_internet():
                               from enigma import eServiceReference
                               from Plugins.Extensions.FreeServer.outils.InfoBar import ALAJREStream5
                               url = "https://ia904707.us.archive.org/32/items/002_20221028/031.mp3"                           
                               ref = eServiceReference(4097, 0, url)
                               ref.setName(Version_1) 
                               self.session.openWithCallback(self.backToIntialService, ALAJREStream5, ref)
                        elif returnValue =="com_232":
                            if connected_to_internet():
                               from enigma import eServiceReference
                               from Plugins.Extensions.FreeServer.outils.InfoBar import ALAJREStream5
                               url = "https://ia904707.us.archive.org/32/items/002_20221028/032.mp3"                           
                               ref = eServiceReference(4097, 0, url)
                               ref.setName(Version_1) 
                               self.session.openWithCallback(self.backToIntialService, ALAJREStream5, ref)
                        elif returnValue =="com_233":
                            if connected_to_internet():
                               from enigma import eServiceReference
                               from Plugins.Extensions.FreeServer.outils.InfoBar import ALAJREStream5
                               url = "https://ia904707.us.archive.org/32/items/002_20221028/033.mp3"                           
                               ref = eServiceReference(4097, 0, url)
                               ref.setName(Version_1) 
                               self.session.openWithCallback(self.backToIntialService, ALAJREStream5, ref)
                        elif returnValue =="com_234":
                            if connected_to_internet():
                               from enigma import eServiceReference
                               from Plugins.Extensions.FreeServer.outils.InfoBar import ALAJREStream5
                               url = "https://ia904707.us.archive.org/32/items/002_20221028/034.mp3"                           
                               ref = eServiceReference(4097, 0, url)
                               ref.setName(Version_1) 
                               self.session.openWithCallback(self.backToIntialService, ALAJREStream5, ref)
                        elif returnValue =="com_235":
                            if connected_to_internet():
                               from enigma import eServiceReference
                               from Plugins.Extensions.FreeServer.outils.InfoBar import ALAJREStream5
                               url = "https://ia904707.us.archive.org/32/items/002_20221028/035.mp3"                           
                               ref = eServiceReference(4097, 0, url)
                               ref.setName(Version_1) 
                               self.session.openWithCallback(self.backToIntialService, ALAJREStream5, ref)
                        elif returnValue =="com_236":
                            if connected_to_internet():
                               from enigma import eServiceReference
                               from Plugins.Extensions.FreeServer.outils.InfoBar import ALAJREStream5
                               url = "https://ia904707.us.archive.org/32/items/002_20221028/036.mp3"                           
                               ref = eServiceReference(4097, 0, url)
                               ref.setName(Version_1) 
                               self.session.openWithCallback(self.backToIntialService, ALAJREStream5, ref)
                        elif returnValue =="com_237":
                            if connected_to_internet():
                               from enigma import eServiceReference
                               from Plugins.Extensions.FreeServer.outils.InfoBar import ALAJREStream5
                               url = "https://ia904707.us.archive.org/32/items/002_20221028/037.mp3"                           
                               ref = eServiceReference(4097, 0, url)
                               ref.setName(Version_1) 
                               self.session.openWithCallback(self.backToIntialService, ALAJREStream5, ref)
                        elif returnValue =="com_238":
                            if connected_to_internet():
                               from enigma import eServiceReference
                               from Plugins.Extensions.FreeServer.outils.InfoBar import ALAJREStream5
                               url = "https://ia904707.us.archive.org/32/items/002_20221028/038.mp3"                           
                               ref = eServiceReference(4097, 0, url)
                               ref.setName(Version_1) 
                               self.session.openWithCallback(self.backToIntialService, ALAJREStream5, ref)
                        elif returnValue =="com_239":
                            if connected_to_internet():
                               from enigma import eServiceReference
                               from Plugins.Extensions.FreeServer.outils.InfoBar import ALAJREStream5
                               url = "https://ia904707.us.archive.org/32/items/002_20221028/039.mp3"                           
                               ref = eServiceReference(4097, 0, url)
                               ref.setName(Version_1) 
                               self.session.openWithCallback(self.backToIntialService, ALAJREStream5, ref)
                        elif returnValue =="com_240":
                            if connected_to_internet():
                               from enigma import eServiceReference
                               from Plugins.Extensions.FreeServer.outils.InfoBar import ALAJREStream5
                               url = "https://ia904707.us.archive.org/32/items/002_20221028/040.mp3"                           
                               ref = eServiceReference(4097, 0, url)
                               ref.setName(Version_1) 
                               self.session.openWithCallback(self.backToIntialService, ALAJREStream5, ref)
                        elif returnValue =="com_241":
                            if connected_to_internet():
                               from enigma import eServiceReference
                               from Plugins.Extensions.FreeServer.outils.InfoBar import ALAJREStream5
                               url = "https://ia904707.us.archive.org/32/items/002_20221028/041.mp3"                           
                               ref = eServiceReference(4097, 0, url)
                               ref.setName(Version_1) 
                               self.session.openWithCallback(self.backToIntialService, ALAJREStream5, ref)
                        elif returnValue =="com_242":
                            if connected_to_internet():
                               from enigma import eServiceReference
                               from Plugins.Extensions.FreeServer.outils.InfoBar import ALAJREStream5
                               url = "https://ia904707.us.archive.org/32/items/002_20221028/042.mp3"                           
                               ref = eServiceReference(4097, 0, url)
                               ref.setName(Version_1) 
                               self.session.openWithCallback(self.backToIntialService, ALAJREStream5, ref)
                        elif returnValue =="com_243":
                            if connected_to_internet():
                               from enigma import eServiceReference
                               from Plugins.Extensions.FreeServer.outils.InfoBar import ALAJREStream5
                               url = "https://ia904707.us.archive.org/32/items/002_20221028/043.mp3"                           
                               ref = eServiceReference(4097, 0, url)
                               ref.setName(Version_1) 
                               self.session.openWithCallback(self.backToIntialService, ALAJREStream5, ref)
                        elif returnValue =="com_244":
                            if connected_to_internet():
                               from enigma import eServiceReference
                               from Plugins.Extensions.FreeServer.outils.InfoBar import ALAJREStream5
                               url = "https://ia904707.us.archive.org/32/items/002_20221028/044.mp3"                           
                               ref = eServiceReference(4097, 0, url)
                               ref.setName(Version_1) 
                               self.session.openWithCallback(self.backToIntialService, ALAJREStream5, ref)
                        elif returnValue =="com_245":
                            if connected_to_internet():
                               from enigma import eServiceReference
                               from Plugins.Extensions.FreeServer.outils.InfoBar import ALAJREStream5
                               url = "https://ia904707.us.archive.org/32/items/002_20221028/045.mp3"                           
                               ref = eServiceReference(4097, 0, url)
                               ref.setName(Version_1) 
                               self.session.openWithCallback(self.backToIntialService, ALAJREStream5, ref)
                        elif returnValue =="com_246":
                            if connected_to_internet():
                               from enigma import eServiceReference
                               from Plugins.Extensions.FreeServer.outils.InfoBar import ALAJREStream5
                               url = "https://ia904707.us.archive.org/32/items/002_20221028/046.mp3"                           
                               ref = eServiceReference(4097, 0, url)
                               ref.setName(Version_1) 
                               self.session.openWithCallback(self.backToIntialService, ALAJREStream5, ref)
                        elif returnValue =="com_247":
                            if connected_to_internet():
                               from enigma import eServiceReference
                               from Plugins.Extensions.FreeServer.outils.InfoBar import ALAJREStream5
                               url = "https://ia904707.us.archive.org/32/items/002_20221028/047.mp3"                           
                               ref = eServiceReference(4097, 0, url)
                               ref.setName(Version_1) 
                               self.session.openWithCallback(self.backToIntialService, ALAJREStream5, ref)
                        elif returnValue =="com_248":
                            if connected_to_internet():
                               from enigma import eServiceReference
                               from Plugins.Extensions.FreeServer.outils.InfoBar import ALAJREStream5
                               url = "https://ia904707.us.archive.org/32/items/002_20221028/048.mp3"                           
                               ref = eServiceReference(4097, 0, url)
                               ref.setName(Version_1) 
                               self.session.openWithCallback(self.backToIntialService, ALAJREStream5, ref)
                        elif returnValue =="com_249":
                            if connected_to_internet():
                               from enigma import eServiceReference
                               from Plugins.Extensions.FreeServer.outils.InfoBar import ALAJREStream5
                               url = "https://ia904707.us.archive.org/32/items/002_20221028/049.mp3"                           
                               ref = eServiceReference(4097, 0, url)
                               ref.setName(Version_1) 
                               self.session.openWithCallback(self.backToIntialService, ALAJREStream5, ref)
                        elif returnValue =="com_250":
                            if connected_to_internet():
                               from enigma import eServiceReference
                               from Plugins.Extensions.FreeServer.outils.InfoBar import ALAJREStream5
                               url = "https://ia904707.us.archive.org/32/items/002_20221028/050.mp3"                           
                               ref = eServiceReference(4097, 0, url)
                               ref.setName(Version_1) 
                               self.session.openWithCallback(self.backToIntialService, ALAJREStream5, ref)
                        elif returnValue =="com_251":
                            if connected_to_internet():
                               from enigma import eServiceReference
                               from Plugins.Extensions.FreeServer.outils.InfoBar import ALAJREStream5
                               url = "https://ia904707.us.archive.org/32/items/002_20221028/051.mp3"                           
                               ref = eServiceReference(4097, 0, url)
                               ref.setName(Version_1) 
                               self.session.openWithCallback(self.backToIntialService, ALAJREStream5, ref)
                        elif returnValue =="com_252":
                            if connected_to_internet():
                               from enigma import eServiceReference
                               from Plugins.Extensions.FreeServer.outils.InfoBar import ALAJREStream5
                               url = "https://ia904707.us.archive.org/32/items/002_20221028/052.mp3"                           
                               ref = eServiceReference(4097, 0, url)
                               ref.setName(Version_1) 
                               self.session.openWithCallback(self.backToIntialService, ALAJREStream5, ref)
                        elif returnValue =="com_253":
                            if connected_to_internet():
                               from enigma import eServiceReference
                               from Plugins.Extensions.FreeServer.outils.InfoBar import ALAJREStream5
                               url = "https://ia904707.us.archive.org/32/items/002_20221028/053.mp3"                           
                               ref = eServiceReference(4097, 0, url)
                               ref.setName(Version_1) 
                               self.session.openWithCallback(self.backToIntialService, ALAJREStream5, ref)
                        elif returnValue =="com_254":
                            if connected_to_internet():
                               from enigma import eServiceReference
                               from Plugins.Extensions.FreeServer.outils.InfoBar import ALAJREStream5
                               url = "https://ia904707.us.archive.org/32/items/002_20221028/054.mp3"                           
                               ref = eServiceReference(4097, 0, url)
                               ref.setName(Version_1) 
                               self.session.openWithCallback(self.backToIntialService, ALAJREStream5, ref)
                        elif returnValue =="com_255":
                            if connected_to_internet():
                               from enigma import eServiceReference
                               from Plugins.Extensions.FreeServer.outils.InfoBar import ALAJREStream5
                               url = "https://ia904707.us.archive.org/32/items/002_20221028/055.mp3"                           
                               ref = eServiceReference(4097, 0, url)
                               ref.setName(Version_1) 
                               self.session.openWithCallback(self.backToIntialService, ALAJREStream5, ref)
                        elif returnValue =="com_256":
                            if connected_to_internet():
                               from enigma import eServiceReference
                               from Plugins.Extensions.FreeServer.outils.InfoBar import ALAJREStream5
                               url = "https://ia904707.us.archive.org/32/items/002_20221028/056.mp3"                           
                               ref = eServiceReference(4097, 0, url)
                               ref.setName(Version_1) 
                               self.session.openWithCallback(self.backToIntialService, ALAJREStream5, ref)
                        elif returnValue =="com_257":
                            if connected_to_internet():
                               from enigma import eServiceReference
                               from Plugins.Extensions.FreeServer.outils.InfoBar import ALAJREStream5
                               url = "https://ia904707.us.archive.org/32/items/002_20221028/057.mp3"                           
                               ref = eServiceReference(4097, 0, url)
                               ref.setName(Version_1) 
                               self.session.openWithCallback(self.backToIntialService, ALAJREStream5, ref)
                        elif returnValue =="com_258":
                            if connected_to_internet():
                               from enigma import eServiceReference
                               from Plugins.Extensions.FreeServer.outils.InfoBar import ALAJREStream5
                               url = "https://ia904707.us.archive.org/32/items/002_20221028/058.mp3"                           
                               ref = eServiceReference(4097, 0, url)
                               ref.setName(Version_1) 
                               self.session.openWithCallback(self.backToIntialService, ALAJREStream5, ref)
                        elif returnValue =="com_259":
                            if connected_to_internet():
                               from enigma import eServiceReference
                               from Plugins.Extensions.FreeServer.outils.InfoBar import ALAJREStream5
                               url = "https://ia904707.us.archive.org/32/items/002_20221028/059.mp3"                           
                               ref = eServiceReference(4097, 0, url)
                               ref.setName(Version_1) 
                               self.session.openWithCallback(self.backToIntialService, ALAJREStream5, ref)
                        elif returnValue =="com_260":
                            if connected_to_internet():
                               from enigma import eServiceReference
                               from Plugins.Extensions.FreeServer.outils.InfoBar import ALAJREStream5
                               url = "https://ia904707.us.archive.org/32/items/002_20221028/060.mp3"                           
                               ref = eServiceReference(4097, 0, url)
                               ref.setName(Version_1) 
                               self.session.openWithCallback(self.backToIntialService, ALAJREStream5, ref)
                        elif returnValue =="com_261":
                            if connected_to_internet():
                               from enigma import eServiceReference
                               from Plugins.Extensions.FreeServer.outils.InfoBar import ALAJREStream5
                               url = "https://ia904707.us.archive.org/32/items/002_20221028/061.mp3"                           
                               ref = eServiceReference(4097, 0, url)
                               ref.setName(Version_1) 
                               self.session.openWithCallback(self.backToIntialService, ALAJREStream5, ref)
                        elif returnValue =="com_262":
                            if connected_to_internet():
                               from enigma import eServiceReference
                               from Plugins.Extensions.FreeServer.outils.InfoBar import ALAJREStream5
                               url = "https://ia904707.us.archive.org/32/items/002_20221028/062.mp3"                           
                               ref = eServiceReference(4097, 0, url)
                               ref.setName(Version_1) 
                               self.session.openWithCallback(self.backToIntialService, ALAJREStream5, ref)
                        elif returnValue =="com_263":
                            if connected_to_internet():
                               from enigma import eServiceReference
                               from Plugins.Extensions.FreeServer.outils.InfoBar import ALAJREStream5
                               url = "https://ia904707.us.archive.org/32/items/002_20221028/063.mp3"                           
                               ref = eServiceReference(4097, 0, url)
                               ref.setName(Version_1) 
                               self.session.openWithCallback(self.backToIntialService, ALAJREStream5, ref)
                        elif returnValue =="com_264":
                            if connected_to_internet():
                               from enigma import eServiceReference
                               from Plugins.Extensions.FreeServer.outils.InfoBar import ALAJREStream5
                               url = "https://ia904707.us.archive.org/32/items/002_20221028/064.mp3"                           
                               ref = eServiceReference(4097, 0, url)
                               ref.setName(Version_1) 
                               self.session.openWithCallback(self.backToIntialService, ALAJREStream5, ref)
                        elif returnValue =="com_265":
                            if connected_to_internet():
                               from enigma import eServiceReference
                               from Plugins.Extensions.FreeServer.outils.InfoBar import ALAJREStream5
                               url = "https://ia904707.us.archive.org/32/items/002_20221028/065.mp3"                           
                               ref = eServiceReference(4097, 0, url)
                               ref.setName(Version_1) 
                               self.session.openWithCallback(self.backToIntialService, ALAJREStream5, ref)
                        elif returnValue =="com_266":
                            if connected_to_internet():
                               from enigma import eServiceReference
                               from Plugins.Extensions.FreeServer.outils.InfoBar import ALAJREStream5
                               url = "https://ia904707.us.archive.org/32/items/002_20221028/066.mp3"                           
                               ref = eServiceReference(4097, 0, url)
                               ref.setName(Version_1) 
                               self.session.openWithCallback(self.backToIntialService, ALAJREStream5, ref)
                        elif returnValue =="com_267":
                            if connected_to_internet():
                               from enigma import eServiceReference
                               from Plugins.Extensions.FreeServer.outils.InfoBar import ALAJREStream5
                               url = "https://ia904707.us.archive.org/32/items/002_20221028/067.mp3"                           
                               ref = eServiceReference(4097, 0, url)
                               ref.setName(Version_1) 
                               self.session.openWithCallback(self.backToIntialService, ALAJREStream5, ref)
                        elif returnValue =="com_268":
                            if connected_to_internet():
                               from enigma import eServiceReference
                               from Plugins.Extensions.FreeServer.outils.InfoBar import ALAJREStream5
                               url = "https://ia904707.us.archive.org/32/items/002_20221028/068.mp3"                           
                               ref = eServiceReference(4097, 0, url)
                               ref.setName(Version_1) 
                               self.session.openWithCallback(self.backToIntialService, ALAJREStream5, ref)
                        elif returnValue =="com_269":
                            if connected_to_internet():
                               from enigma import eServiceReference
                               from Plugins.Extensions.FreeServer.outils.InfoBar import ALAJREStream5
                               url = "https://ia904707.us.archive.org/32/items/002_20221028/069.mp3"                           
                               ref = eServiceReference(4097, 0, url)
                               ref.setName(Version_1) 
                               self.session.openWithCallback(self.backToIntialService, ALAJREStream5, ref)                                          
                        elif returnValue =="com_270":
                            if connected_to_internet():
                               from enigma import eServiceReference
                               from Plugins.Extensions.FreeServer.outils.InfoBar import ALAJREStream5
                               url = "https://ia904707.us.archive.org/32/items/002_20221028/070.mp3"                           
                               ref = eServiceReference(4097, 0, url)
                               ref.setName(Version_1) 
                               self.session.openWithCallback(self.backToIntialService, ALAJREStream5, ref)
                        elif returnValue =="com_271":
                            if connected_to_internet():
                               from enigma import eServiceReference
                               from Plugins.Extensions.FreeServer.outils.InfoBar import ALAJREStream5
                               url = "https://ia904707.us.archive.org/32/items/002_20221028/071.mp3"                           
                               ref = eServiceReference(4097, 0, url)
                               ref.setName(Version_1) 
                               self.session.openWithCallback(self.backToIntialService, ALAJREStream5, ref)
                        elif returnValue =="com_272":
                            if connected_to_internet():
                               from enigma import eServiceReference
                               from Plugins.Extensions.FreeServer.outils.InfoBar import ALAJREStream5
                               url = "https://ia904707.us.archive.org/32/items/002_20221028/072.mp3"                           
                               ref = eServiceReference(4097, 0, url)
                               ref.setName(Version_1) 
                               self.session.openWithCallback(self.backToIntialService, ALAJREStream5, ref)
                        elif returnValue =="com_273":
                            if connected_to_internet():
                               from enigma import eServiceReference
                               from Plugins.Extensions.FreeServer.outils.InfoBar import ALAJREStream5
                               url = "https://ia904707.us.archive.org/32/items/002_20221028/073.mp3"                           
                               ref = eServiceReference(4097, 0, url)
                               ref.setName(Version_1) 
                               self.session.openWithCallback(self.backToIntialService, ALAJREStream5, ref)
                        elif returnValue =="com_274":
                            if connected_to_internet():
                               from enigma import eServiceReference
                               from Plugins.Extensions.FreeServer.outils.InfoBar import ALAJREStream5
                               url = "https://ia904707.us.archive.org/32/items/002_20221028/074.mp3"                           
                               ref = eServiceReference(4097, 0, url)
                               ref.setName(Version_1) 
                               self.session.openWithCallback(self.backToIntialService, ALAJREStream5, ref)
                        elif returnValue =="com_275":
                            if connected_to_internet():
                               from enigma import eServiceReference
                               from Plugins.Extensions.FreeServer.outils.InfoBar import ALAJREStream5
                               url = "https://ia904707.us.archive.org/32/items/002_20221028/075.mp3"                           
                               ref = eServiceReference(4097, 0, url)
                               ref.setName(Version_1) 
                               self.session.openWithCallback(self.backToIntialService, ALAJREStream5, ref)
                        elif returnValue =="com_276":
                            if connected_to_internet():
                               from enigma import eServiceReference
                               from Plugins.Extensions.FreeServer.outils.InfoBar import ALAJREStream5
                               url = "https://ia904707.us.archive.org/32/items/002_20221028/076.mp3"                           
                               ref = eServiceReference(4097, 0, url)
                               ref.setName(Version_1) 
                               self.session.openWithCallback(self.backToIntialService, ALAJREStream5, ref)
                        elif returnValue =="com_277":
                            if connected_to_internet():
                               from enigma import eServiceReference
                               from Plugins.Extensions.FreeServer.outils.InfoBar import ALAJREStream5
                               url = "https://ia904707.us.archive.org/32/items/002_20221028/077.mp3"                           
                               ref = eServiceReference(4097, 0, url)
                               ref.setName(Version_1) 
                               self.session.openWithCallback(self.backToIntialService, ALAJREStream5, ref)
                        elif returnValue =="com_278":
                            if connected_to_internet():
                               from enigma import eServiceReference
                               from Plugins.Extensions.FreeServer.outils.InfoBar import ALAJREStream5
                               url = "https://ia904707.us.archive.org/32/items/002_20221028/078.mp3"                           
                               ref = eServiceReference(4097, 0, url)
                               ref.setName(Version_1) 
                               self.session.openWithCallback(self.backToIntialService, ALAJREStream5, ref)
                        elif returnValue =="com_279":
                            if connected_to_internet():
                               from enigma import eServiceReference
                               from Plugins.Extensions.FreeServer.outils.InfoBar import ALAJREStream5
                               url = "https://ia904707.us.archive.org/32/items/002_20221028/079.mp3"                           
                               ref = eServiceReference(4097, 0, url)
                               ref.setName(Version_1) 
                               self.session.openWithCallback(self.backToIntialService, ALAJREStream5, ref)
                        elif returnValue =="com_280":
                            if connected_to_internet():
                               from enigma import eServiceReference
                               from Plugins.Extensions.FreeServer.outils.InfoBar import ALAJREStream5
                               url = "https://ia904707.us.archive.org/32/items/002_20221028/080.mp3"                           
                               ref = eServiceReference(4097, 0, url)
                               ref.setName(Version_1) 
                               self.session.openWithCallback(self.backToIntialService, ALAJREStream5, ref)
                        elif returnValue =="com_281":
                            if connected_to_internet():
                               from enigma import eServiceReference
                               from Plugins.Extensions.FreeServer.outils.InfoBar import ALAJREStream5
                               url = "https://ia904707.us.archive.org/32/items/002_20221028/081.mp3"                           
                               ref = eServiceReference(4097, 0, url)
                               ref.setName(Version_1) 
                               self.session.openWithCallback(self.backToIntialService, ALAJREStream5, ref)
                        elif returnValue =="com_282":
                            if connected_to_internet():
                               from enigma import eServiceReference
                               from Plugins.Extensions.FreeServer.outils.InfoBar import ALAJREStream5
                               url = "https://ia904707.us.archive.org/32/items/002_20221028/082.mp3"                           
                               ref = eServiceReference(4097, 0, url)
                               ref.setName(Version_1) 
                               self.session.openWithCallback(self.backToIntialService, ALAJREStream5, ref)
                        elif returnValue =="com_283":
                            if connected_to_internet():
                               from enigma import eServiceReference
                               from Plugins.Extensions.FreeServer.outils.InfoBar import ALAJREStream5
                               url = "https://ia904707.us.archive.org/32/items/002_20221028/083.mp3"                           
                               ref = eServiceReference(4097, 0, url)
                               ref.setName(Version_1) 
                               self.session.openWithCallback(self.backToIntialService, ALAJREStream5, ref)
                        elif returnValue =="com_284":
                            if connected_to_internet():
                               from enigma import eServiceReference
                               from Plugins.Extensions.FreeServer.outils.InfoBar import ALAJREStream5
                               url = "https://ia904707.us.archive.org/32/items/002_20221028/084.mp3"                           
                               ref = eServiceReference(4097, 0, url)
                               ref.setName(Version_1) 
                               self.session.openWithCallback(self.backToIntialService, ALAJREStream5, ref)
                        elif returnValue =="com_285":
                            if connected_to_internet():
                               from enigma import eServiceReference
                               from Plugins.Extensions.FreeServer.outils.InfoBar import ALAJREStream5
                               url = "https://ia904707.us.archive.org/32/items/002_20221028/085.mp3"                           
                               ref = eServiceReference(4097, 0, url)
                               ref.setName(Version_1) 
                               self.session.openWithCallback(self.backToIntialService, ALAJREStream5, ref)
                        elif returnValue =="com_286":
                            if connected_to_internet():
                               from enigma import eServiceReference
                               from Plugins.Extensions.FreeServer.outils.InfoBar import ALAJREStream5
                               url = "https://ia904707.us.archive.org/32/items/002_20221028/086.mp3"                           
                               ref = eServiceReference(4097, 0, url)
                               ref.setName(Version_1) 
                               self.session.openWithCallback(self.backToIntialService, ALAJREStream5, ref)
                        elif returnValue =="com_287":
                            if connected_to_internet():
                               from enigma import eServiceReference
                               from Plugins.Extensions.FreeServer.outils.InfoBar import ALAJREStream5
                               url = "https://ia904707.us.archive.org/32/items/002_20221028/087.mp3"                           
                               ref = eServiceReference(4097, 0, url)
                               ref.setName(Version_1) 
                               self.session.openWithCallback(self.backToIntialService, ALAJREStream5, ref)
                        elif returnValue =="com_288":
                            if connected_to_internet():
                               from enigma import eServiceReference
                               from Plugins.Extensions.FreeServer.outils.InfoBar import ALAJREStream5
                               url = "https://ia904707.us.archive.org/32/items/002_20221028/088.mp3"                           
                               ref = eServiceReference(4097, 0, url)
                               ref.setName(Version_1) 
                               self.session.openWithCallback(self.backToIntialService, ALAJREStream5, ref)
                        elif returnValue =="com_289":
                            if connected_to_internet():
                               from enigma import eServiceReference
                               from Plugins.Extensions.FreeServer.outils.InfoBar import ALAJREStream5
                               url = "https://ia904707.us.archive.org/32/items/002_20221028/089.mp3"                           
                               ref = eServiceReference(4097, 0, url)
                               ref.setName(Version_1) 
                               self.session.openWithCallback(self.backToIntialService, ALAJREStream5, ref)
                        elif returnValue =="com_290":
                            if connected_to_internet():
                               from enigma import eServiceReference
                               from Plugins.Extensions.FreeServer.outils.InfoBar import ALAJREStream5
                               url = "https://ia904707.us.archive.org/32/items/002_20221028/090.mp3"                           
                               ref = eServiceReference(4097, 0, url)
                               ref.setName(Version_1) 
                               self.session.openWithCallback(self.backToIntialService, ALAJREStream5, ref)
                        elif returnValue =="com_291":
                            if connected_to_internet():
                               from enigma import eServiceReference
                               from Plugins.Extensions.FreeServer.outils.InfoBar import ALAJREStream5
                               url = "https://ia904707.us.archive.org/32/items/002_20221028/091.mp3"                           
                               ref = eServiceReference(4097, 0, url)
                               ref.setName(Version_1) 
                               self.session.openWithCallback(self.backToIntialService, ALAJREStream5, ref)
                        elif returnValue =="com_292":
                            if connected_to_internet():
                               from enigma import eServiceReference
                               from Plugins.Extensions.FreeServer.outils.InfoBar import ALAJREStream5
                               url = "https://ia904707.us.archive.org/32/items/002_20221028/092.mp3"                           
                               ref = eServiceReference(4097, 0, url)
                               ref.setName(Version_1) 
                               self.session.openWithCallback(self.backToIntialService, ALAJREStream5, ref)
                        elif returnValue =="com_293":
                            if connected_to_internet():
                               from enigma import eServiceReference
                               from Plugins.Extensions.FreeServer.outils.InfoBar import ALAJREStream5
                               url = "https://ia904707.us.archive.org/32/items/002_20221028/093.mp3"                           
                               ref = eServiceReference(4097, 0, url)
                               ref.setName(Version_1) 
                               self.session.openWithCallback(self.backToIntialService, ALAJREStream5, ref)
                        elif returnValue =="com_294":
                            if connected_to_internet():
                               from enigma import eServiceReference
                               from Plugins.Extensions.FreeServer.outils.InfoBar import ALAJREStream5
                               url = "https://ia904707.us.archive.org/32/items/002_20221028/094.mp3"                           
                               ref = eServiceReference(4097, 0, url)
                               ref.setName(Version_1) 
                               self.session.openWithCallback(self.backToIntialService, ALAJREStream5, ref)
                        elif returnValue =="com_295":
                            if connected_to_internet():
                               from enigma import eServiceReference
                               from Plugins.Extensions.FreeServer.outils.InfoBar import ALAJREStream5
                               url = "https://ia904707.us.archive.org/32/items/002_20221028/095.mp3"                           
                               ref = eServiceReference(4097, 0, url)
                               ref.setName(Version_1) 
                               self.session.openWithCallback(self.backToIntialService, ALAJREStream5, ref)
                        elif returnValue =="com_296":
                            if connected_to_internet():
                               from enigma import eServiceReference
                               from Plugins.Extensions.FreeServer.outils.InfoBar import ALAJREStream5
                               url = "https://ia904707.us.archive.org/32/items/002_20221028/096.mp3"                           
                               ref = eServiceReference(4097, 0, url)
                               ref.setName(Version_1) 
                               self.session.openWithCallback(self.backToIntialService, ALAJREStream5, ref)
                        elif returnValue =="com_297":
                            if connected_to_internet():
                               from enigma import eServiceReference
                               from Plugins.Extensions.FreeServer.outils.InfoBar import ALAJREStream5
                               url = "https://ia904707.us.archive.org/32/items/002_20221028/097.mp3"                           
                               ref = eServiceReference(4097, 0, url)
                               ref.setName(Version_1) 
                               self.session.openWithCallback(self.backToIntialService, ALAJREStream5, ref)
                        elif returnValue =="com_298":
                            if connected_to_internet():
                               from enigma import eServiceReference
                               from Plugins.Extensions.FreeServer.outils.InfoBar import ALAJREStream5
                               url = "https://ia904707.us.archive.org/32/items/002_20221028/098.mp3"                           
                               ref = eServiceReference(4097, 0, url)
                               ref.setName(Version_1) 
                               self.session.openWithCallback(self.backToIntialService, ALAJREStream5, ref)
                        elif returnValue =="com_299":
                            if connected_to_internet():
                               from enigma import eServiceReference
                               from Plugins.Extensions.FreeServer.outils.InfoBar import ALAJREStream5
                               url = "https://ia904707.us.archive.org/32/items/002_20221028/099.mp3"                           
                               ref = eServiceReference(4097, 0, url)
                               ref.setName(Version_1) 
                               self.session.openWithCallback(self.backToIntialService, ALAJREStream5, ref)
                        elif returnValue =="com_300":
                            if connected_to_internet():
                               from enigma import eServiceReference
                               from Plugins.Extensions.FreeServer.outils.InfoBar import ALAJREStream5
                               url = "https://ia904707.us.archive.org/32/items/002_20221028/100.mp3"                           
                               ref = eServiceReference(4097, 0, url)
                               ref.setName(Version_1) 
                               self.session.openWithCallback(self.backToIntialService, ALAJREStream5, ref)
                        elif returnValue =="com_301":
                            if connected_to_internet():
                               from enigma import eServiceReference
                               from Plugins.Extensions.FreeServer.outils.InfoBar import ALAJREStream5
                               url = "https://ia904707.us.archive.org/32/items/002_20221028/101.mp3"                           
                               ref = eServiceReference(4097, 0, url)
                               ref.setName(Version_1) 
                               self.session.openWithCallback(self.backToIntialService, ALAJREStream5, ref)
                        elif returnValue =="com_302":
                            if connected_to_internet():
                               from enigma import eServiceReference
                               from Plugins.Extensions.FreeServer.outils.InfoBar import ALAJREStream5
                               url = "https://ia904707.us.archive.org/32/items/002_20221028/102.mp3"                           
                               ref = eServiceReference(4097, 0, url)
                               ref.setName(Version_1) 
                               self.session.openWithCallback(self.backToIntialService, ALAJREStream5, ref)
                        elif returnValue =="com_303":
                            if connected_to_internet():
                               from enigma import eServiceReference
                               from Plugins.Extensions.FreeServer.outils.InfoBar import ALAJREStream5
                               url = "https://ia904707.us.archive.org/32/items/002_20221028/103.mp3"                           
                               ref = eServiceReference(4097, 0, url)
                               ref.setName(Version_1) 
                               self.session.openWithCallback(self.backToIntialService, ALAJREStream5, ref)
                        elif returnValue =="com_304":
                            if connected_to_internet():
                               from enigma import eServiceReference
                               from Plugins.Extensions.FreeServer.outils.InfoBar import ALAJREStream5
                               url = "https://ia904707.us.archive.org/32/items/002_20221028/104.mp3"                           
                               ref = eServiceReference(4097, 0, url)
                               ref.setName(Version_1) 
                               self.session.openWithCallback(self.backToIntialService, ALAJREStream5, ref)
                        elif returnValue =="com_305":
                            if connected_to_internet():
                               from enigma import eServiceReference
                               from Plugins.Extensions.FreeServer.outils.InfoBar import ALAJREStream5
                               url = "https://ia904707.us.archive.org/32/items/002_20221028/105.mp3"                           
                               ref = eServiceReference(4097, 0, url)
                               ref.setName(Version_1) 
                               self.session.openWithCallback(self.backToIntialService, ALAJREStream5, ref)
                        elif returnValue =="com_306":
                            if connected_to_internet():
                               from enigma import eServiceReference
                               from Plugins.Extensions.FreeServer.outils.InfoBar import ALAJREStream5
                               url = "https://ia904707.us.archive.org/32/items/002_20221028/106.mp3"                           
                               ref = eServiceReference(4097, 0, url)
                               ref.setName(Version_1) 
                               self.session.openWithCallback(self.backToIntialService, ALAJREStream5, ref)
                        elif returnValue =="com_307":
                            if connected_to_internet():
                               from enigma import eServiceReference
                               from Plugins.Extensions.FreeServer.outils.InfoBar import ALAJREStream5
                               url = "https://ia904707.us.archive.org/32/items/002_20221028/107.mp3"                           
                               ref = eServiceReference(4097, 0, url)
                               ref.setName(Version_1) 
                               self.session.openWithCallback(self.backToIntialService, ALAJREStream5, ref)
                        elif returnValue =="com_308":
                            if connected_to_internet():
                               from enigma import eServiceReference
                               from Plugins.Extensions.FreeServer.outils.InfoBar import ALAJREStream5
                               url = "https://ia904707.us.archive.org/32/items/002_20221028/108.mp3"                           
                               ref = eServiceReference(4097, 0, url)
                               ref.setName(Version_1) 
                               self.session.openWithCallback(self.backToIntialService, ALAJREStream5, ref)
                        elif returnValue =="com_309":
                            if connected_to_internet():
                               from enigma import eServiceReference
                               from Plugins.Extensions.FreeServer.outils.InfoBar import ALAJREStream5
                               url = "https://ia904707.us.archive.org/32/items/002_20221028/109.mp3"                           
                               ref = eServiceReference(4097, 0, url)
                               ref.setName(Version_1) 
                               self.session.openWithCallback(self.backToIntialService, ALAJREStream5, ref)
                        elif returnValue =="com_310":
                            if connected_to_internet():
                               from enigma import eServiceReference
                               from Plugins.Extensions.FreeServer.outils.InfoBar import ALAJREStream5
                               url = "https://ia904707.us.archive.org/32/items/002_20221028/110.mp3"                           
                               ref = eServiceReference(4097, 0, url)
                               ref.setName(Version_1) 
                               self.session.openWithCallback(self.backToIntialService, ALAJREStream5, ref)
                        elif returnValue =="com_311":
                            if connected_to_internet():
                               from enigma import eServiceReference
                               from Plugins.Extensions.FreeServer.outils.InfoBar import ALAJREStream5
                               url = "https://ia904707.us.archive.org/32/items/002_20221028/111.mp3"                           
                               ref = eServiceReference(4097, 0, url)
                               ref.setName(Version_1) 
                               self.session.openWithCallback(self.backToIntialService, ALAJREStream5, ref)
                        elif returnValue =="com_312":
                            if connected_to_internet():
                               from enigma import eServiceReference
                               from Plugins.Extensions.FreeServer.outils.InfoBar import ALAJREStream5
                               url = "https://ia904707.us.archive.org/32/items/002_20221028/112.mp3"                           
                               ref = eServiceReference(4097, 0, url)
                               ref.setName(Version_1) 
                               self.session.openWithCallback(self.backToIntialService, ALAJREStream5, ref)
                        elif returnValue =="com_313":
                            if connected_to_internet():
                               from enigma import eServiceReference
                               from Plugins.Extensions.FreeServer.outils.InfoBar import ALAJREStream5
                               url = "https://ia904707.us.archive.org/32/items/002_20221028/113.mp3"                           
                               ref = eServiceReference(4097, 0, url)
                               ref.setName(Version_1) 
                               self.session.openWithCallback(self.backToIntialService, ALAJREStream5, ref)
                        elif returnValue =="com_314":
                            if connected_to_internet():
                               from enigma import eServiceReference
                               from Plugins.Extensions.FreeServer.outils.InfoBar import ALAJREStream5
                               url = "https://ia904707.us.archive.org/32/items/002_20221028/114.mp3"                           
                               ref = eServiceReference(4097, 0, url)
                               ref.setName(Version_1) 
                               self.session.openWithCallback(self.backToIntialService, ALAJREStream5, ref)
                        elif returnValue =="com_315":
                            if connected_to_internet():
                               from enigma import eServiceReference
                               from Plugins.Extensions.FreeServer.outils.InfoBar import ALAJREStream5
                               url = "https://ia904707.us.archive.org/32/items/002_20221028/Full.mp3"                           
                               ref = eServiceReference(4097, 0, url)
                               ref.setName(Version_1) 
                               self.session.openWithCallback(self.backToIntialService, ALAJREStream5, ref)
                        elif returnValue =="com_316":
                            if connected_to_internet():
                               from enigma import eServiceReference
                               from Plugins.Extensions.FreeServer.outils.InfoBar import ALAJREStream5
                               url = "https://ia904707.us.archive.org/32/items/002_20221028/115.mp3"                           
                               ref = eServiceReference(4097, 0, url)
                               ref.setName(Version_1) 
                               self.session.openWithCallback(self.backToIntialService, ALAJREStream5, ref)
                        elif returnValue =="com_317":
                            if connected_to_internet():
                               from enigma import eServiceReference
                               from Plugins.Extensions.FreeServer.outils.InfoBar import ALAJREStream5
                               url = "https://ia904707.us.archive.org/32/items/002_20221028/116.mp3"                           
                               ref = eServiceReference(4097, 0, url)
                               ref.setName(Version_1) 
                               self.session.openWithCallback(self.backToIntialService, ALAJREStream5, ref)
                        elif returnValue =="com_318":
                            if connected_to_internet():
                               from enigma import eServiceReference
                               from Plugins.Extensions.FreeServer.outils.InfoBar import ALAJREStream5
                               url = "https://ia904707.us.archive.org/32/items/002_20221028/117.mp3"                           
                               ref = eServiceReference(4097, 0, url)
                               ref.setName(Version_1) 
                               self.session.openWithCallback(self.backToIntialService, ALAJREStream5, ref)
                        elif returnValue =="com_319":
                            if connected_to_internet():
                               from enigma import eServiceReference
                               from Plugins.Extensions.FreeServer.outils.InfoBar import ALAJREStream5
                               url = "https://ia904707.us.archive.org/32/items/002_20221028/118.mp3"                           
                               ref = eServiceReference(4097, 0, url)
                               ref.setName(Version_1) 
                               self.session.openWithCallback(self.backToIntialService, ALAJREStream5, ref)
                        elif returnValue =="com_320":
                            if connected_to_internet():
                               from enigma import eServiceReference
                               from Plugins.Extensions.FreeServer.outils.InfoBar import ALAJREStream5
                               url = "https://ia904707.us.archive.org/32/items/002_20221028/119.mp3"                           
                               ref = eServiceReference(4097, 0, url)
                               ref.setName(Version_1) 
                               self.session.openWithCallback(self.backToIntialService, ALAJREStream5, ref)
                        elif returnValue =="com_321":
                            if connected_to_internet():
                               from enigma import eServiceReference
                               from Plugins.Extensions.FreeServer.outils.InfoBar import ALAJREStream5
                               url = "https://ia904707.us.archive.org/32/items/002_20221028/120.mp3"                           
                               ref = eServiceReference(4097, 0, url)
                               ref.setName(Version_1) 
                               self.session.openWithCallback(self.backToIntialService, ALAJREStream5, ref)
                        elif returnValue =="com_322":
                            if connected_to_internet():
                               from enigma import eServiceReference
                               from Plugins.Extensions.FreeServer.outils.InfoBar import ALAJREStream5
                               url = "https://ia904707.us.archive.org/32/items/002_20221028/121.mp3"                           
                               ref = eServiceReference(4097, 0, url)
                               ref.setName(Version_1) 
                               self.session.openWithCallback(self.backToIntialService, ALAJREStream5, ref)
                        elif returnValue =="com_323":
                            if connected_to_internet():
                               from enigma import eServiceReference
                               from Plugins.Extensions.FreeServer.outils.InfoBar import ALAJREStream5
                               url = "https://ia904707.us.archive.org/32/items/002_20221028/122.mp3"                           
                               ref = eServiceReference(4097, 0, url)
                               ref.setName(Version_1) 
                               self.session.openWithCallback(self.backToIntialService, ALAJREStream5, ref)
                        elif returnValue =="com_324":
                            if connected_to_internet():
                               from enigma import eServiceReference
                               from Plugins.Extensions.FreeServer.outils.InfoBar import ALAJREStream5
                               url = "https://ia904707.us.archive.org/32/items/002_20221028/123.mp3"                           
                               ref = eServiceReference(4097, 0, url)
                               ref.setName(Version_1) 
                               self.session.openWithCallback(self.backToIntialService, ALAJREStream5, ref)
                        elif returnValue =="com_325":
                            if connected_to_internet():
                               from enigma import eServiceReference
                               from Plugins.Extensions.FreeServer.outils.InfoBar import ALAJREStream5
                               url = "https://ia904707.us.archive.org/32/items/002_20221028/124.mp3"                           
                               ref = eServiceReference(4097, 0, url)
                               ref.setName(Version_1) 
                               self.session.openWithCallback(self.backToIntialService, ALAJREStream5, ref)
                        else:
                                print("\n[MyShPrombt] cancel\n")
                                self.close(None)

        def prombt(self, com):                
            scripts = "/usr/lib/enigma2/python/Plugins/Extensions/FreeServer/scripts/"
            os.chmod(scripts, 755)
            self.session.open(Console3,_("Executing: %s") % (com), ["%s" % com])

        def cancel(self):
            self.close(None)
