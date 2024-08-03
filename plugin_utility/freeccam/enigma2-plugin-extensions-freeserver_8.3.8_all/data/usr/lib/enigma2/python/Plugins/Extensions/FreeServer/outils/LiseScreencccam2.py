# -*- coding: UTF-8 -*-
from __future__ import print_function
from .compat import compat_Request, compat_urlopen, compat_HTTPError, PY3

from Components.Sources.List import List
from Plugins.Plugin import PluginDescriptor
import os, re, time, socket
from enigma import eTimer
from Screens.Screen import Screen
from Screens.MessageBox import MessageBox
from twisted.web import client
from Components.ActionMap import NumberActionMap, ActionMap
from Components.MenuList import MenuList
from Components.ActionMap import *
from Components.Label import Label
from Components.MultiContent import MultiContentEntryText, MultiContentEntryPixmap, MultiContentEntryPixmapAlphaTest
from Components.config import *
from Components.ConfigList import ConfigList, ConfigListScreen
from Components.config import config, ConfigSubsection, ConfigText, getConfigListEntry, ConfigSelection, ConfigPIN, ConfigDirectory, ConfigYesNo
from enigma import eListboxPythonMultiContent, eListbox, gFont, RT_HALIGN_LEFT, RT_HALIGN_RIGHT, RT_HALIGN_CENTER, RT_WRAP, RT_VALIGN_CENTER
from enigma import getDesktop, eServiceReference, iServiceInformation
from Tools.Directories import fileExists, resolveFilename, SCOPE_PLUGINS, pathExists
dwidth = getDesktop(0).size().width()
wsize = getDesktop(0).size().width()
hsize = getDesktop(0).size().height()

# Add By RAED to Fix (urlopen error [SSL: CERTIFICATE_VERIFY_FAILED])
import ssl
try:
    _create_unverified_https_context = ssl._create_unverified_context
except AttributeError:
    # Legacy Python that doesn't verify HTTPS certificates by default
    pass
else:
    # Handle target environment that doesn't support HTTPS verification
    ssl._create_default_https_context = _create_unverified_https_context

UserAgent = {'Mozilla/5.0 (X11; U; Linux x86_64; de; rv:1.9.0.15) Gecko/2009102815 Ubuntu/9.04 (jaunty) Firefox/3.'}
Agent = {'User-agent': 'Mozilla/5.0 (X11; U; Linux x86_64; de; rv:1.9.0.15) Gecko/2009102815 Ubuntu/9.04 (jaunty) Firefox/3.',
 'Connection': 'Close'}
Agent0 = {'User-Agent': 'Mozilla/5.0',
 'Accept': 'text/html'}
Lien11 = 'https://www.testious.com/'

def getUrl(url):
    try:
        print("Here in getUrl url =", url)
        req = compat_Request(url)
        req.add_header('User-Agent', 'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-GB; rv:1.9.0.3) Gecko/2008092417 Firefox/3.0.3')
        response = compat_urlopen(req)
        link=response.read()
        response.close()
        return link
    except compat_HTTPError:
        print('Not Found')
        return
class m2list(MenuList):
    def __init__(self, list):
        MenuList.__init__(self, list, False, eListboxPythonMultiContent)
        self.l.setFont(0, gFont('Regular', 14))
        self.l.setFont(1, gFont('Regular', 16))
        self.l.setFont(2, gFont('Regular', 18))
        self.l.setFont(3, gFont('Regular', 20))
        self.l.setFont(4, gFont('Regular', 22))
        self.l.setFont(5, gFont('Regular', 24))
        self.l.setFont(6, gFont('Regular', 26))
        self.l.setFont(7, gFont('Regular', 28))
        self.l.setFont(8, gFont('Regular', 30))
def show_listiptv(h, p, u, pw):
    #print(h, p, u, pw)
    if dwidth == 1280:
        res = [(h,
          p,
          u,
          pw)]
        if 'Free Server Cccam' in h:
            res.append(MultiContentEntryText(pos=(2, 2), size=(425, 31), font=5, text=h, backcolor_sel=26214, backcolor=22503, flags=RT_HALIGN_CENTER))
            return res
        else:
            res.append(MultiContentEntryText(pos=(2, 2), size=(425, 31), font=5, text=h, backcolor_sel=26214, backcolor=1090519040, flags=RT_HALIGN_CENTER))
            return res
    else:
        res = [(h,
          p,
          u,
          pw)]
        if 'Free Server Cccam' in h:
            res.append(MultiContentEntryText(pos=(2, 2), size=(600, 31), font=7, text=h, backcolor_sel=26214, backcolor=22503, flags=RT_HALIGN_CENTER))
            return res
        res.append(MultiContentEntryText(pos=(2, 2), size=(600, 31), font=7, text=h, backcolor_sel=26214, backcolor=1090519040, flags=RT_HALIGN_CENTER))
        return res
class LiseScreencccam2(Screen):
    skinfhd = '<screen name="LiseScreencccam2" position="0,0" size="1920,1064" title="" flags="wfNoBorder" backgroundColor="transparent">  <widget name="ProgramTv" zPosition="1" foregroundColorSelected="white" position="13,142" size="600,801" enableWrapAround="1" scrollbarMode="showNever" transparent="0" /><eLabel position="167,974" size="148,35" backgroundColor="#398564" /><eLabel position="322,974" size="148,35" backgroundColor="#ffcf40" /><eLabel position="468,975" size="148,35" backgroundColor="#222f5b" /><eLabel text="Wicardd" zPosition="4" position="170,977" size="140,30" font="Regular; 25" transparent="0" backgroundColor="black" halign="center" /><eLabel text="Ncam" zPosition="4" position="325,976" size="140,30" font="Regular; 25" transparent="0" backgroundColor="black" halign="center" /><eLabel text="Oscam" zPosition="4" position="474,976" size="140,30" font="Regular; 25" transparent="0" backgroundColor="black" halign="center" /><eLabel position="17,975" size="148,35" backgroundColor="#a32020" /><eLabel text="1 CCcam" zPosition="4" position="29,977" size="132,30" font="Regular; 25" transparent="0" backgroundColor="black" halign="center" /><eLabel text="All files in   /etc/tuxbox/config" zPosition="4" position="15,1046" size="600,20" transparent="0" backgroundColor="black" halign="center" /><widget name="List" zPosition="1" foregroundColorSelected="white" position="1286,176" size="600,801" enableWrapAround="1" scrollbarMode="showNever" transparent="0" /><eLabel text="OK to choose server" zPosition="4" position="12,945" size="600,25" font="Regular; 22" transparent="0" backgroundColor="black" halign="center" /><eLabel text="OK To Remove Server" zPosition="4" position="1286,1040" size="600,23" font="Regular; 22" transparent="0" backgroundColor="black" halign="center" /><eLabel text="List Of Choices" zPosition="4" position="1286,976" size="600,30" font="Regular; 22" transparent="0" backgroundColor="black" halign="center" /><widget name="info" position="1286,1008" zPosition="1" size="600,30" font="Regular;24" foregroundColor="#ffffff" transparent="0" halign="center" valign="center" backgroundColor="#000000" /><eLabel text="MENU Reset Server" zPosition="4" position="321,1013" size="294,31" font="Regular; 22" transparent="0" backgroundColor="black" halign="center" /><widget name="infoserver2" position="72,84" zPosition="2" size="450,28" font="Regular;25" foregroundColor="white" transparent="0" halign="center" valign="center" backgroundColor="black" /><widget name="infoserver" position="72,114" zPosition="2" size="450,28" font="Regular;25" foregroundColor="white" transparent="0" halign="center" valign="center" backgroundColor="black" /><eLabel text="2 Doscam" zPosition="4" position="30,1014" size="130,30" font="Regular; 20" transparent="0" backgroundColor="black" halign="center" /><eLabel position="17,1008" size="153,35" backgroundColor="#33ffff" /><eLabel text="3 Gcam" zPosition="4" position="177,1014" size="130,30" font="Regular; 20" transparent="0" backgroundColor="black" halign="center" /><eLabel position="169,1010" size="148,35" backgroundColor="#00cc33" /></screen>'
    skinhd = '<screen name="LiseScreencccam2" position="0,0" size="1284,720" title="" flags="wfNoBorder" backgroundColor="transparent">  <widget name="ProgramTv" zPosition="1" foregroundColorSelected="white" position="6,46" size="425,525" enableWrapAround="1" scrollbarMode="showNever" transparent="0" /><eLabel position="130,600" size="97,39" backgroundColor="#398564" /><eLabel position="229,600" size="99,39" backgroundColor="#ffcf40" /><eLabel position="328,600" size="102,39" backgroundColor="#222f5b" /><eLabel text="Wicardd" zPosition="4" position="133,604" size="90,28" font="Regular; 20" transparent="0" backgroundColor="black" halign="center" /><eLabel text="Ncam" zPosition="4" position="235,604" size="90,28" font="Regular; 20" transparent="0" backgroundColor="black" halign="center" /><eLabel text="Oscam" zPosition="4" position="335,604" size="90,28" font="Regular; 20" transparent="0" backgroundColor="black" halign="center" /><eLabel position="5,600" size="124,39" backgroundColor="#a32020" zPosition="3" /><eLabel text="1 CCcam" zPosition="4" position="29,604" size="90,28" font="Regular; 20" transparent="0" backgroundColor="black" halign="center" /><eLabel text="All files in   /etc/tuxbox/config" zPosition="4" position="6,679" size="425,26" transparent="0" backgroundColor="black" halign="center" /><widget name="List" zPosition="1" foregroundColorSelected="white" position="841,46" size="425,525" enableWrapAround="1" scrollbarMode="showNever" transparent="0" /><eLabel text="List Of Choices" zPosition="4" position="842,576" size="425,30" font="Regular; 22" transparent="0" backgroundColor="black" halign="center" /><widget name="info" position="842,609" zPosition="1" size="425,30" font="Regular;24" foregroundColor="#ffffff" transparent="0" halign="center" valign="center" backgroundColor="#000000" /><eLabel text="OK To Remove Server" zPosition="4" position="842,638" size="425,25" font="Regular; 22" transparent="0" backgroundColor="black" halign="center" /><eLabel text="OK to choose server" zPosition="4" position="6,574" size="424,26" font="Regular; 19" transparent="0" backgroundColor="black" halign="center" valign="center" /><eLabel text="MENU Reset Server" zPosition="4" position="228,640" size="201,38" font="Regular; 19" transparent="0" backgroundColor="black" halign="center" valign="center" /><widget name="infoserver" position="7,23" zPosition="2" size="425,28" font="Regular;25" foregroundColor="#03396c" transparent="1" halign="center" valign="center" backgroundColor="black" /><widget name="infoserver2" position="7,0" zPosition="2" size="425,28" font="Regular;25" foregroundColor="#03396c" transparent="1" halign="center" valign="center" backgroundColor="black" /><eLabel text="2 Doscam" zPosition="4" position="30,644" size="90,28" font="Regular; 18" transparent="0" backgroundColor="black" halign="center" /><eLabel position="6,639" size="122,39" backgroundColor="#33ffff" /><eLabel text="3 Gcam" zPosition="4" position="132,644" size="90,28" font="Regular; 18" transparent="0" backgroundColor="black" halign="center" /><eLabel position="129,638" size="97,39" backgroundColor="#00cc33" /></screen>'
    def __init__(self, session, args = 0):
        Screen.__init__(self, session)
        if dwidth == 1280:
            self.skin = LiseScreencccam2.skinhd
        else:
            self.skin = LiseScreencccam2.skinfhd
        self['actions'] = ActionMap(['OkCancelActions',
         'MenuActions',
         'ColorActions',
         'DirectionActions',
         'SetupActions',
         'MovieSelectionActions'], {'cancel': self.End,
         'ok': self.Choice_Cccam,
         'up': self.up,
         'down': self.down,
         'left': self.left,
         'green': self.Wicardd,
         '1': self.Cccam,
         'menu': self.initial,
         '2': self.Doscam,
         '3': self.Gcam,
         'yellow': self.Ncam,
         'blue': self.Oscam,
         'right': self.right}, -1)
        self['EPGSelectActions'] = HelpableActionMap(self, 'EPGSelectActions', {'nextBouquet': self.switchList,
         'prevBouquet': self.switchList}, -1)
        self.List = []
        self.letter_list = []
        self['List'] = m2list([])
        self.ProgramTv = []
        self.letter_list2 = []
        self['ProgramTv'] = m2list([])
        self.currentList = 'ProgramTv'
        self['List'].selectionEnabled(0)
        self['ProgramTv'].selectionEnabled(1)
        self['info'] = Label()
        self['info'].setText('....')
        self['infoserver'] = Label()
        self['infoserver'].setText('....')
        self['infoserver2'] = Label()
        self['infoserver2'].setText('Free Servers')
        self.updateTimer = eTimer()
        self.initsearch()

    def initsearch(self):
### Edit By RAED
        try:
               from datetime import datetime
               dttm = datetime.now().strftime('%Y-%m-%d')
               print('Date', dttm)
               URL = 'http://testious.com/free-cccam-servers/' + dttm + '/'
               #print('url:', URL, self.list_iptv2(URL))
               self.list_iptv2(URL)
        except:
               #self.close()
               print('[No Connection or Bad url address]')
### End
    def list_iptv2(self, main_url):
        print("list_iptv2 main_url = ", main_url)
        data = getUrl(main_url)
        if PY3:
            data = data.decode('utf8')
        else:
            data = data
        print("data 1= ", data)
        if 'Not Found' in data:
            import datetime
            today = datetime.date.today()
            print('Oggi     :', today)
            one_day = datetime.timedelta(days=0)
            print('Un giorno:', one_day)
            yesterday = today - one_day
            print('Ieri     :', yesterday) 
            dttm = str(yesterday)
            URL = 'https://testious.com/old-free-cccam-servers/' + dttm + '/'
            #print('url:', main_url=URL)
            #print('main_url:', getUrl(main_url))
            self.load_iptv2(data)
        else:
            return

    def load_iptv2(self, data):
            print("load_iptv2 data = ", data)
            url = re.findall('<br>C: (.*?) (.*?) (.*?) (.*?) #', data)
            print("load_iptv2 url =", url)
            for url1 in url:
                print("load_iptv2 url1 =", url1)
                h = url1[0]
                p = url1[1]
                u = url1[2]
                pw = url1[3]
                if 'cccamspot' in h:
                    self.letter_list2.append(show_listiptv(h, p, u, 'cccamspot.com'))
                if 'free2.cccam-free2.com' in h:
                    self.letter_list2.append(show_listiptv(h, p, u, 'cccam-free2.com'))
                elif 'fr.free-cccam.com' in h:
                    self.letter_list2.append(show_listiptv(h, p, u, 'free-cccam.com'))
                elif 's2.cccam-free.com' in h or 's3.cccam-free.com' in h:
                    self.letter_list2.append(show_listiptv(h, p, u, 'cccam-free.com'))
                elif 's4.powerfullcccam.com' in h:
                    self.letter_list2.append(show_listiptv(h, p, u, 'powerfullcccam.com'))
                else:
                    self.letter_list2.append(show_listiptv(h, p, u, 'free'))
            H = len(self.letter_list2)
            self.load_cccam2(data,H)

    def load_cccam2(self, data,Llist):
        url1 = re.findall('<br>C: (.*?) (.*?) (.*?) (.*?) #', data)
        Nmb = len(url1)+Llist
        self['infoserver'].setText(str(Nmb) + '__Free Server Cccam')
        for h, p, u, pw in url1:
            self.letter_list2.append(show_listiptv(h, p, u, pw))
        self['ProgramTv'].l.setList(self.letter_list2)
        self['ProgramTv'].l.setItemHeight(31)

    def Choice_Cccam(self):
        if self.currentList == 'ProgramTv':
            if 'Free Server Cccam' in self['ProgramTv'].getCurrent()[0][0]:
                pass
            else:
                host = self['ProgramTv'].getCurrent()[0][0]
                port = self['ProgramTv'].getCurrent()[0][1]
                user = self['ProgramTv'].getCurrent()[0][2]
                pasw = self['ProgramTv'].getCurrent()[0][3]
                self.letter_list.append(show_listiptv(host, port, user, pasw))
                self['List'].l.setList(self.letter_list)
                self['List'].l.setItemHeight(31)
                condt0 = len(self.letter_list)
                self['info'].setText(str(condt0) + '_Server')
                InDex = self['ProgramTv'].getSelectionIndex()
                if InDex+1 == len(self.letter_list2):
                    self['ProgramTv'].moveToIndex(0)
                    self['List'].moveToIndex(condt0-1)
                else:
                    self['ProgramTv'].moveToIndex(InDex+1)
                    self['List'].moveToIndex(condt0-1)
                self['info'].setText(str(condt0)+'_Server')
                self['List'].selectionEnabled(1)
                self['ProgramTv'].selectionEnabled(1)
        else:
            Refc = self['List'].getSelectionIndex()
            condt = len(self.letter_list)
            if Refc == 0 and condt == 1:
                del self.letter_list[Refc]
                self['info'].setText('.....')
                self['List'].selectionEnabled(0)
                self['ProgramTv'].selectionEnabled(1)
                self.currentList = 'ProgramTv'
            if Refc == 0 and condt > 1:
                del self.letter_list[0]
                self['List'].l.setList(self.letter_list)
                self['List'].l.setItemHeight(31)
                self['List'].moveToIndex(0)
                self['info'].setText(str(condt - 1) + '_Server')
            if Refc != 0 and condt > 1:
                del self.letter_list[Refc]
                self['List'].l.setList(self.letter_list)
                self['List'].l.setItemHeight(31)
                self['List'].moveToIndex(Refc - 1)
                self['info'].setText(str(condt - 1) + '_Server')

    def switchList(self):
        if self.currentList == 'List':
            self['List'].selectionEnabled(1)
            self['ProgramTv'].selectionEnabled(1)
            self.currentList = 'ProgramTv'
        else:
            self['ProgramTv'].selectionEnabled(1)
            self['List'].selectionEnabled(1)
            self.currentList = 'List'

    def up(self):
        self[self.currentList].up()
        self.updateTimer.stop()

    def down(self):
        self[self.currentList].down()
        self.updateTimer.stop()

    def left(self):
        self[self.currentList].pageUp()
        self.updateTimer.stop()

    def right(self):
        self[self.currentList].pageDown()
        self.updateTimer.stop()

    def initial(self):
        self.List = []
        self.letter_list = []
        import shutil
        shutil.copy2('/usr/lib/enigma2/python/Plugins/Extensions/FreeServer/config/wicardd.conf', '/usr/lib/enigma2/python/Plugins/Extensions/FreeServer/data/wicardd.conf')
        shutil.copy2('/usr/lib/enigma2/python/Plugins/Extensions/FreeServer/config/ncam.server', '/usr/lib/enigma2/python/Plugins/Extensions/FreeServer/data/ncam.server')
        shutil.copy2('/usr/lib/enigma2/python/Plugins/Extensions/FreeServer/config/CCcam.cfg', '/usr/lib/enigma2/python/Plugins/Extensions/FreeServer/data/CCcam.cfg')
        shutil.copy2('/usr/lib/enigma2/python/Plugins/Extensions/FreeServer/config/oscam.server', '/usr/lib/enigma2/python/Plugins/Extensions/FreeServer/data/oscam.server')
        shutil.copy2('/usr/lib/enigma2/python/Plugins/Extensions/FreeServer/config/doscam.cfg', '/usr/lib/enigma2/python/Plugins/Extensions/FreeServer/data/doscam.cfg')
        shutil.copy2('/usr/lib/enigma2/python/Plugins/Extensions/FreeServer/config/gcam.server', '/usr/lib/enigma2/python/Plugins/Extensions/FreeServer/data/gcam.server')
        self['info'].setText('.....')
        self['List'].l.setList(self.letter_list)
        self['List'].l.setItemHeight(31)
        self.initsearch()
        self.session.open(MessageBox, 'Erase servers', type=MessageBox.TYPE_INFO, timeout=8)

    def End(self):
        self.close()

    def Wicardd(self):
        import shutil
        Imp = len(self.letter_list)
        if Imp == 0:
            self.session.open(MessageBox, 'Empty list', type=MessageBox.TYPE_INFO, timeout=8)
        else:
            self['ProgramTv'].selectionEnabled(0)
            self['List'].selectionEnabled(1)
            self.currentList = 'List'
            for x in range(Imp):
                try:
                    self['List'].moveToIndex(x)
                    host = self['List'].getCurrent()[0][0]
                    port = self['List'].getCurrent()[0][1]
                    user = self['List'].getCurrent()[0][2]
                    pasw = self['List'].getCurrent()[0][3]
                    Dist = '/etc/tuxbox/config/wicardd.conf'
                    if fileExists('/usr/cfmngr/wicardd/wicardd.conf'):
                        Dist = '/usr/cfmngr/wicardd/wicardd.conf'
                    elif fileExists('/etc/tuxbox/config/wicardd.conf'):
                        Dist = '/etc/tuxbox/config/wicardd.conf'
                    elif fileExists('/usr/keys/wicardd.conf'):
                        Dist = '/usr/keys/wicardd.conf'
                    elif fileExists('/var/tuxbox/config/wicardd.conf'):
                        Dist = '/var/tuxbox/config/wicardd.conf'                      
                    else:
                        if not os.path.exists('/etc/tuxbox/config'):
                            os.system('mkdir /etc/tuxbox/config')
                        shutil.copy2('/usr/lib/enigma2/python/Plugins/Extensions/FreeServer/data/wicardd.conf', '/etc/tuxbox/config/wicardd.conf')
                        Dist = '/etc/tuxbox/config/wicardd.conf'
                    fichier = open('/usr/lib/enigma2/python/Plugins/Extensions/FreeServer/data/wicardd.conf', 'a')
                    fichier.write('\n[reader]\nname= server_' + str(x) + '\nactive= 1\ntype= cccam\naccount=' + user + ':' + pasw + '@' + host + ':' + port + '\ndebug = 1\nreconnect_delay = 1\nemm_cache = 1\necm_ttl = 15000\nreconnect_to_account_ip =1\n\n')
                    fichier.close()
                    shutil.copy2('/usr/lib/enigma2/python/Plugins/Extensions/FreeServer/data/wicardd.conf', Dist)                
                except IndexError:
                    pass
            self.session.open(MessageBox, str(Imp) + '_Server Copy/in ' + Dist, type=MessageBox.TYPE_INFO, timeout=8)
            self['ProgramTv'].selectionEnabled(1)
            self['List'].selectionEnabled(0)
            self.currentList = 'ProgramTv'

    def Oscam(self):
        import shutil
        shutil.copy2('/etc/tuxbox/config/oscam.server', '/usr/lib/enigma2/python/Plugins/Extensions/FreeServer/data/oscam.server')    
        Imp = len(self.letter_list)
        if Imp == 0:
            self.session.open(MessageBox, 'Empty list', type=MessageBox.TYPE_INFO, timeout=8)
        else:
            self['ProgramTv'].selectionEnabled(0)
            self['List'].selectionEnabled(1)
            self.currentList = 'List'
            for x in range(Imp):
                try:
                    self['List'].moveToIndex(x)
                    host = self['List'].getCurrent()[0][0]
                    port = self['List'].getCurrent()[0][1]
                    user = self['List'].getCurrent()[0][2]
                    pasw = self['List'].getCurrent()[0][3]
                    Dist = '/etc/tuxbox/config/oscam.server'                  
                    if fileExists('/etc/tuxbox/config/oscam.server'):
                        Dist = '/etc/tuxbox/config/oscam.server'
                    elif fileExists('/usr/keys/oscam_atv_ymod/oscam.server'):
                        Dist = '/usr/keys/oscam_atv_ymod/oscam.server'
                    elif fileExists('/usr/keys/oscam.server'):
                        Dist = '/usr/keys/oscam.server'
                    elif fileExists('/var/keys/oscam.server'):
                        Dist = '/var/keys/oscam.server'                    
                    else:
                        if not os.path.exists('/etc/tuxbox/config'):
                            os.system('mkdir /etc/tuxbox/config')
                        Dist = '/etc/tuxbox/config/oscam.server'                
                    fichier = open('/usr/lib/enigma2/python/Plugins/Extensions/FreeServer/data/oscam.server', 'a')
                    fichier.write('\n[reader]\nlabel = Server_' + str(x) + '\nenable= 1\nprotocol = cccam\ndevice = ' + host + ',' + port + '\nuser = ' + user + '\npassword = ' + pasw + '\ninactivitytimeout = 30\ngroup = 3\ncccversion = 2.2.1\ncccmaxhops = 0\nccckeepalive = 1\naudisabled = 1\n\n')
                    fichier.close()
                    shutil.copy2('/usr/lib/enigma2/python/Plugins/Extensions/FreeServer/data/oscam.server', Dist)
                except IndexError:
                    pass
            self.session.open(MessageBox, str(Imp) + '_Server Copy/in ' + Dist, type=MessageBox.TYPE_INFO, timeout=8)
            self['ProgramTv'].selectionEnabled(1)
            self['List'].selectionEnabled(0)
            self.currentList = 'ProgramTv'

    def Doscam(self):
        import shutil
        Imp = len(self.letter_list)
        if Imp == 0:
            self.session.open(MessageBox, 'Empty list', type=MessageBox.TYPE_INFO, timeout=8)
        else:
            self['ProgramTv'].selectionEnabled(0)
            self['List'].selectionEnabled(1)
            self.currentList = 'List'
            for x in range(Imp):
                try:
                    self['List'].moveToIndex(x)
                    host = self['List'].getCurrent()[0][0]
                    port = self['List'].getCurrent()[0][1]
                    user = self['List'].getCurrent()[0][2]
                    pasw = self['List'].getCurrent()[0][3]
                    Dist = '/etc/tuxbox/doscam/doscam.cfg'                  
                    if fileExists('/etc/tuxbox/config/doscam.cfg'):
                        Dist = '/etc/tuxbox/config/doscam.cfg'
                    elif fileExists('/usr/keys/doscam.cfg'):
                        Dist = '/usr/keys/doscam.cfg'
                    elif fileExists('/etc/tuxbox/doscam.config/doscam.cfg'):
                        Dist = '/etc/tuxbox/doscam.config/doscam.cfg'
                    elif fileExists('/etc/tuxbox/doscam.cfg'):
                        Dist = '/etc/tuxbox/doscam.cfg'
                    elif fileExists('/usr/keys/doscam/doscam.cfg'):
                        Dist = '/usr/keys/doscam/doscam.cfg'
                    else:
                        if not os.path.exists('/etc/tuxbox/doscam'):
                            os.system('mkdir /etc/tuxbox/doscam')
                        shutil.copy2('/usr/lib/enigma2/python/Plugins/Extensions/FreeServer/data/doscam.cfg', '/etc/tuxbox/doscam/doscam.cfg' )
                        Dist = '/etc/tuxbox/doscam/doscam.cfg'                
                    fichier = open('/usr/lib/enigma2/python/Plugins/Extensions/FreeServer/data/doscam.cfg', 'a')
                    fichier.write('\n[reader]\nlabel = Server_' + str(x) + '\nenable= 1\nprotocol = cccam\ndevice = ' + host + ',' + port + '\nuser = ' + user + '\npassword = ' + pasw + '\ninactivitytimeout = 30\ngroup = 3\ncccversion = 2.2.1\ncccmaxhops = 0\nccckeepalive = 1\naudisabled = 1\n\n')
                    fichier.close()
                    shutil.copy2('/usr/lib/enigma2/python/Plugins/Extensions/FreeServer/data/doscam.cfg', Dist )                
                except IndexError:
                    pass
            self.session.open(MessageBox, str(Imp) + '_Server Copy/in ' + Dist, type=MessageBox.TYPE_INFO, timeout=8)
            self['ProgramTv'].selectionEnabled(1)
            self['List'].selectionEnabled(0)
            self.currentList = 'ProgramTv'

    def Gcam(self):
        import shutil
        Imp = len(self.letter_list)
        if Imp == 0:
            self.session.open(MessageBox, 'Empty list', type=MessageBox.TYPE_INFO, timeout=8)
        else:
            self['ProgramTv'].selectionEnabled(0)
            self['List'].selectionEnabled(1)
            self.currentList = 'List'
            for x in range(Imp):
                try:
                    self['List'].moveToIndex(x)
                    host = self['List'].getCurrent()[0][0]
                    port = self['List'].getCurrent()[0][1]
                    user = self['List'].getCurrent()[0][2]
                    pasw = self['List'].getCurrent()[0][3]
                    Dist = '/etc/tuxbox/config/gcam.server'                  
                    if fileExists('/etc/tuxbox/config/gcam.server'):
                        Dist = '/etc/tuxbox/config/gcam.server'
                    elif fileExists('/usr/keys/gcam.server'):
                        Dist = '/usr/keys/gcam.server'
                    elif fileExists('/var/keys/gcam.server'):
                        Dist = '/var/keys/gcam.server'                    
                    else:
                        if not os.path.exists('/etc/tuxbox/config'):
                            os.system('mkdir /etc/tuxbox/config')
                        shutil.copy2('/usr/lib/enigma2/python/Plugins/Extensions/FreeServer/data/gcam.server', '/etc/tuxbox/config/gcam.server' )
                        Dist = '/etc/tuxbox/config/gcam.server'                
                    fichier = open('/usr/lib/enigma2/python/Plugins/Extensions/FreeServer/data/gcam.server', 'a')
                    fichier.write('\n[reader]\nlabel = Server_' + str(x) + '\nenable= 1\nprotocol = cccam\ndevice = ' + host + ',' + port + '\nuser = ' + user + '\npassword = ' + pasw + '\ninactivitytimeout = 30\ngroup = 3\ncccversion = 2.2.1\ncccmaxhops = 0\nccckeepalive = 1\naudisabled = 1\n\n')
                    fichier.close()
                    shutil.copy2('/usr/lib/enigma2/python/Plugins/Extensions/FreeServer/data/gcam.server', Dist )                
                except IndexError:
                    pass
            self.session.open(MessageBox, str(Imp) + '_Server Copy/in ' + Dist, type=MessageBox.TYPE_INFO, timeout=8)
            self['ProgramTv'].selectionEnabled(1)
            self['List'].selectionEnabled(0)
            self.currentList = 'ProgramTv'

    def Cccam(self):
        import shutil                                              
        shutil.copy2('/etc/CCcam.cfg', '/usr/lib/enigma2/python/Plugins/Extensions/FreeServer/data/CCcam.cfg')
        Imp = len(self.letter_list)                      
        if Imp == 0:
            self.session.open(MessageBox, 'Empty list', type=MessageBox.TYPE_INFO, timeout=8)
        else:
            self['ProgramTv'].selectionEnabled(0)
            self['List'].selectionEnabled(1)
            self.currentList = 'List'
            for x in range(Imp):
                try:
                    self['List'].moveToIndex(x)
                    host = self['List'].getCurrent()[0][0]
                    port = self['List'].getCurrent()[0][1]
                    user = self['List'].getCurrent()[0][2]
                    pasw = self['List'].getCurrent()[0][3]
                    Dist = '/etc/CCcam.cfg'                
                    if fileExists('/etc/CCcam.cfg'):
                        Dist = '/etc/CCcam.cfg'
                    elif fileExists('/etc/tuxbox/config/CCcam.cfg'):
                        Dist = '/etc/tuxbox/config/CCcam.cfg'
                    elif fileExists('/usr/keys/CCcam.cfg'):
                        Dist = '/usr/keys/CCcam.cfg'
                    elif fileExists('/etc/keys/CCcam.cfg'):
                        Dist = '/etc/keys/CCcam.cfg'
                    else:
                        Dist = '/etc/CCcam.cfg'                
                    fichier = open('/usr/lib/enigma2/python/Plugins/Extensions/FreeServer/data/CCcam.cfg', 'a')
                    fichier.write('\n\nC: ' + host + ' ' + port + ' ' + user + ' ' + pasw)
                    fichier.close()
                    shutil.copy2('/usr/lib/enigma2/python/Plugins/Extensions/FreeServer/data/CCcam.cfg', Dist)                
                except IndexError:
                    pass
            self.session.open(MessageBox, str(Imp) + '_Server Copy in ' + Dist, type=MessageBox.TYPE_INFO, timeout=8)
            self['ProgramTv'].selectionEnabled(1)
            self['List'].selectionEnabled(0)
            self.currentList = 'ProgramTv'

    def Ncam(self):
        import shutil
        shutil.copy2('/etc/tuxbox/config/ncam.server', '/usr/lib/enigma2/python/Plugins/Extensions/FreeServer/data/ncam.server')    
        Imp = len(self.letter_list)
        if Imp == 0:
            self.session.open(MessageBox, 'Empty list', type=MessageBox.TYPE_INFO, timeout=8)
        else:
            self['ProgramTv'].selectionEnabled(0)
            self['List'].selectionEnabled(1)
            self.currentList = 'List'
            for x in range(Imp):
                try:
                    self['List'].moveToIndex(x)
                    host = self['List'].getCurrent()[0][0]
                    port = self['List'].getCurrent()[0][1]
                    user = self['List'].getCurrent()[0][2]
                    pasw = self['List'].getCurrent()[0][3]
                    Dist = '/etc/tuxbox/config/ncam.server'
                    if fileExists('/etc/tuxbox/config/ncam.server'):
                        Dist = '/etc/tuxbox/config/ncam.server'
                    elif fileExists('/var/keys/ncam.server'):
                        Dist = '/var/keys/ncam.server'
                    elif fileExists('/usr/keys/ncam.server'):
                        Dist = '/usr/keys/ncam.server'
                    else:
                        if not os.path.exists('/etc/tuxbox/config'):
                            os.system('mkdir /etc/tuxbox/config')
                        Dist = '/etc/tuxbox/config/ncam.server'                
                    fichier = open('/usr/lib/enigma2/python/Plugins/Extensions/FreeServer/data/ncam.server', 'a')
                    fichier.write('\n[reader]\nlabel= server_' + str(x) + '\nenable= 1\nprotocol= cccam\ndevice=' + host + ',' + port + '\nuser=' + user + '\npassword=' + pasw + '\ngroup= 1\ncccversion= 2.0.11\ndisablecrccws_only_for= 0500:032830\ncccmaxhops= 1\nccckeepalive= 1\naudisabled= 1\n\n')
                    fichier.close()
                    shutil.copy2('/usr/lib/enigma2/python/Plugins/Extensions/FreeServer/data/ncam.server', Dist)                
                except IndexError:
                    pass
            self.session.open(MessageBox, str(Imp) + '_Server Copy ' + Dist, type=MessageBox.TYPE_INFO, timeout=8)
            self['ProgramTv'].selectionEnabled(1)
            self['List'].selectionEnabled(0)
            self.currentList = 'ProgramTv'
