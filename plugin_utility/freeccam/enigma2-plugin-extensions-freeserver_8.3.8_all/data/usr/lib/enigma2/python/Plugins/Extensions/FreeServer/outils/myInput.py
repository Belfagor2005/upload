# -*- coding: UTF-8 -*-

from enigma import eTimer, ePicLoad, gPixmapPtr, getPrevAsciiCode
from Tools.Directories import fileExists
from Tools.Directories import fileExists, pathExists
from Components.Pixmap import Pixmap
from Components.Input import Input
from Screens.InputBox import InputBox
from Screens.MessageBox import MessageBox
from Screens.Screen import Screen
from Components.AVSwitch import AVSwitch
from Components.Label import Label
from Components.ConfigList import ConfigList
from Components.Sources.StaticText import StaticText
from Components.ActionMap import NumberActionMap, ActionMap, HelpableActionMap
from Components.config import ConfigText, KEY_0, KEY_DELETE, KEY_BACKSPACE, config
from enigma import getDesktop, eListboxPythonMultiContent, eListbox, eTimer, gFont, RT_HALIGN_LEFT, RT_HALIGN_RIGHT, RT_HALIGN_CENTER, RT_WRAP, loadPNG
#from Plugins.Extensions.FreeServer.outils.InputBox import InputBox
from Plugins.Extensions.FreeServer.outils.Console3 import Console3
from Plugins.Extensions.FreeServer.outils.compat import compat_urlopen
from shutil import copyfile
import sys, time, os, shutil, re, requests, json, os, shutil, fileinput, warnings
from os import system as os_system
from PIL import Image
import re
import sys,os

dwidth = getDesktop(0).size().width()

###########################################################################
import requests , json, re,random,string,time,warnings
from requests.packages.urllib3.exceptions import InsecureRequestWarning
warnings.simplefilter('ignore',InsecureRequestWarning)
N=9
rnd=''.join(random.choice(string.digits) for _ in range(N))
N=4
rnd2=''.join(random.choice(string.digits) for _ in range(N))
import os, os.path
import glob
import requests, re
import requests , json, re,random,string,time,warnings
from random import choice
RND_NAME=['Hisham','Pakita','Kristina','Lyna','Roberto','Lynch','Julia','Adams','Zakaria','Zinou','Cristina','Garza','Bethany','Cook','Clifton','Hunt','Austin','Estrada','Preston','Ruiz','Alfonso','Hodges',
          'Bombastic','Sackbut','Decaudate','RajaatHod','Luminous','Chronography','Abattoir','Cascer1Verily','Angelus','Lautitious','XxmiranSitar','Luminous','Aphicide','RichmitcSeton','RappelZizz','Luminous',
          'Rose','Franks','Mcknight','Murillo','Seymour','Sterling','Branch','Shepherd','Casey','Foreman','Stevens','Mock','Clinton','Franco','Means','Painter','Otero','Thacker','Glenn','Trent','Johns','Dupree',
          'Gagne','Fuentes','Fleming','Warren','Carpenter','Parham','Mclean','Snell','Nicholas','Jacobsen','Buck','Lambert','Fuller','Lanier','Wagner','Stevens','Everett','Gagnon','Piper','Faulkner','Vera','Shea',
          'Askew','Polk','Woodward','Wang','Carmichael','Cobb','Cannon','Marino','Granger','Hartley','Seymour','Warren','Stinson','Boyer','Cano','Lusk','King','Bruno','Fletcher','Tabor','Mcleod','Cornell','Phipps', 
          'Elliot','Lockhart','Britt','Downing','Cates','Rivera','Valentin','Jernigan','Henderson','Oneil','Riddle','Joiner','Riley','Rock','Ledbetter','Mercado','Felix','Ricks','Henley','Blanchard','Pierre','Meade',
          'Barron','Dawsonn','Lawson','Spencer','Andersen','Copeland','Shaw','Costa','Manley','Cooley','Cameron','Bridges','Crockett','Fitzpatrick','Jewell','Bruner','Whitman','Schroeder','Fountain','Brewster','Rhodes',
          'Mclean','Porter','Jimenez','Underwood','Sanchez','Galvan','Murillo','Childress','Covingto','Mcclure','Espinosa','Mathews','Thompson','Boudreaux','Samuel','Teague','Wesley','Grover','Gibson','Horton','Herring']


################################################################################
PAD='3'
IPTVTMPPATH='/tmp/IPTV'
LINKFILE= '/tmp/link'
LINKFILE2= '/tmp/code'
LINKFILE2_1= '/tmp/post_token'
LINKFILE3_1= '/tmp/myPic1.png'
LINKFILE3= '/tmp/myPic.png'
TMPOUTPUTDATA= '/tmp/dateoutTMP'
BFNAME= 'userbouquet.IPTVWORLD45.tv'
LastScanned= 'userbouquet.LastScanned.tv'
M3UPATH= '/tmp/IPTVWORLD45.m3u'
m3ufile= 'IPTVWORLD45'
WGET='wget --no-check-certificate'
BOUQUETSPATH='/etc/enigma2/bouquets.tv'
E2SETTINGSPATH='/etc/enigma2'
url="http://4ksharing.com/panel/userpanel/testlines.php?action=new_test_line"
url22='http://cp.extracccam.com/includes/captcha.php'
services_url='https://ssdvpshosting.xyz/store/clientarea.php?action=services'
################################################################################

s = requests.Session()

HDR= {'User-Agent':'Mozilla/5.0 (Windows NT 6.1; rv:85.0) Gecko/20100101 Firefox/85.0',
      'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
      'Accept-Language': 'fr,fr-FR;q=0.8,en-US;q=0.5,en;q=0.3',
      'Upgrade-Insecure-Requests':'1',
      'Connection': 'keep-alive',
      'Accept-Encoding':'gzip, deflate'}
Post_Hdr={'User-Agent':'Mozilla/5.0 (Windows NT 6.1; rv:109.0) Gecko/20100101 Firefox/111.0',
          'Accept':'*/*',
          'Accept-Language':'fr,fr-FR;q=0.8,en-US;q=0.5,en;q=0.3',
          'Connection':'keep-alive',
          'Content-Type':'application/x-www-form-urlencoded',
          'Host':'cp.extracccam.com',
          'Referer':'http://cp.extracccam.com/index.php',
          'Upgrade-Insecure-Requests':'1',
          'Accept-Encoding':'gzip, deflate, br'}
          
chars = string.digits
RND_ID  =  ''.join(choice(chars) for _ in range(5))
RND_PASS=  ''.join(choice(chars) for _ in range(9))
NAME_TARGET=random.choice(RND_NAME)
EMAIL_TARGET=random.choice(RND_NAME)+str(RND_ID)+'@gmail.com' 

print("Password:",RND_PASS)  
print("EMail Target:",EMAIL_TARGET)

def cleanTMP():
    print("Clean tmp folder")
    print(LINE)
    os.system('rm -r %s > /dev/null 2>&1 && rm -f %s > /dev/null 2>&1' % (M3UPATH, LINKFILE))

class myInput(Screen):
    skinfhd = '''
<screen position="center,center" size="856,556" title="" flags="wfNoBorder">
<widget source="Title" position="5,5" size="845,100" render="Label" font="Regular;28" foregroundColor="#00ffffff" transparent="1" halign="center"/>
<widget name="icon" render="Pixmap" pixmap="/tmp/myPic.png" zPosition="5" position="250,170" size="350,100" alphatest="blend" borderWidth="2" borderColor="#00ffffff" backgroundColor="#00000000" />
<widget name="input" position="276,290" size="470,50" font="Regular;40" transparent="0" itemHeight="40" foregroundColor="#00ffffff" backgroundColor="#b30000" zPosition="7"/>
<eLabel text="Code =" position="100,290" size="180,50" font="Regular; 40" transparent="0" foregroundColor="#00ffffff" backgroundColor="#b30000" halign="center" zPosition="5" />
<widget source="key_green" render="Label" position="65,480" size="200,40" zPosition="2"  valign="center" halign="center" font="Regular;28" transparent="0" foregroundColor="#00ffffff" backgroundColor="#00389416"/>
<widget name="HelpWindow" position="200,370" size="1,1" alphatest="on" foregroundColor="#00ffffff" transparent="1" zPosition="6" />
</screen>'''
    skinhd = '''
<screen position="center,center" size="856,556" title="" flags="wfNoBorder">
<widget source="Title" position="5,5" size="845,100" render="Label" font="Regular;28" foregroundColor="#00ffffff" transparent="1" halign="center"/>
<widget name="icon" render="Pixmap" pixmap="/tmp/myPic.png" zPosition="5" position="250,170" size="350,100" alphatest="blend" borderWidth="2" borderColor="#00ffffff" backgroundColor="#00000000" />
<widget name="input" position="276,290" size="470,50" font="Regular;40" transparent="0" itemHeight="40" foregroundColor="#00ffffff" backgroundColor="#b30000" zPosition="7"/>
<eLabel text="Code =" position="100,290" size="180,50" font="Regular; 40" transparent="0" foregroundColor="#00ffffff" backgroundColor="#b30000" halign="center" zPosition="5" />
<widget source="key_green" render="Label" position="65,480" size="200,40" zPosition="2"  valign="center" halign="center" font="Regular;28" transparent="0" foregroundColor="#00ffffff" backgroundColor="#00389416"/>
<widget name="HelpWindow" position="200,370" size="1,1" alphatest="on" foregroundColor="#00ffffff" transparent="1" zPosition="6" />
</screen>'''  

  
    def __init__(self, session, useableChars=None, **kwargs):
        self.session = session
        Screen.__init__(self, session)
        if dwidth == 1280:
            self.skin = myInput.skinhd
        else:
            self.skin = myInput.skinfhd
        #self["myActionMap"] = ActionMap(["SetupActions"],{"ok": self.myInput,"cancel": self.cancel}, -1)
        self["myActionMap"] = NumberActionMap(["WizardActions", "InputBoxActions", "InputAsciiActions", "KeyboardInputActions", "ColorActions"],
        	{           		
           		"gotAsciiCode": self.gotAsciiCode,
			"back": self.cancel,
			"green": self.save,
			"left": self.keyLeft,
			"right": self.keyRight,
			"deleteForward": self.keyDelete,
			"deleteBackward": self.keyBackspace,
			"tab": self.keyTab,
			"toggleOverwrite": self.keyInsert,
			"1": self.keyNumberGlobal,
			"2": self.keyNumberGlobal,
			"3": self.keyNumberGlobal,
			"4": self.keyNumberGlobal,
			"5": self.keyNumberGlobal,
			"6": self.keyNumberGlobal,
			"7": self.keyNumberGlobal,
			"8": self.keyNumberGlobal,
			"9": self.keyNumberGlobal,
			"0": self.keyNumberGlobal
           	}, -1)

### EDit By RAED To DreamOS OE2.5/2.6
        #if fileExists('/var/lib/dpkg/status'):
        #     self.wget = "/usr/bin/wget2 --no-check-certificate"
        #else:
        #     self.wget = "/usr/bin/wget"
        self.wget = "wget --no-check-certificate"
### End
        #import sys,os  
        #os.system("sh '/usr/lib/enigma2/python/Plugins/Extensions/FreeServer/scripts/pictureimage.sh'")
        self['key_green'] = StaticText(_('Save'))
        self['Password'] = Label()
        self['icon'] = Pixmap()
        self["HelpWindow"] = Pixmap()
        self["HelpWindow"].show()
        self["input"] = Input(**kwargs)
        if useableChars is not None:
            self["input"].setUseableChars(useableChars)
        self.timer = eTimer()
        try:
            self.timer.callback.append(self.Confirm)
        except:
            self.timer_conn = self.timer.timeout.connect(self.Confirm)
        #self.onLayoutFinish.append(self.setWindowTitle)
        self.onExecBegin.append(self.setKeyboardModeAscii)
        self.setTitle("Please enter the characters you see in the image below into the text box provided. This is required to prevent automated submissions.")
        #os.system('wget --no-check-certificate -q -O- --trust-server-names %s > %s' % (url22, LINKFILE3))
        #data=s.post('https://ssdvpshosting.xyz/store/includes/verifyimage.php',headers=Post_Hdr,verify=False,allow_redirects=True).text
        #with open(LINKFILE3, "a") as f: 
        #f.write(data)
        r = s.get(url22, stream = True)
        with open(LINKFILE3_1,'wb') as f:
                shutil.copyfileobj(r.raw, f)
        image = Image.open(LINKFILE3_1)
        new_image = image.resize((350, 100))
        new_image.save(LINKFILE3)

### EDit By RAED To DreamOS OE2.5/2.6
        #if fileExists('/var/lib/dpkg/status'):
        #     self.wget = "/usr/bin/wget2 --no-check-certificate"
        #else:
        #     self.wget = "/usr/bin/wget"
        self.wget = "wget --no-check-certificate"
### End
        #import sys,os  
        #os.system("sh '/usr/lib/enigma2/python/Plugins/Extensions/FreeServer/scripts/pictureimage.sh'") 

    def askForWord(self, code):
        if code is None:
            pass
        elif code == '':
            pass
        else:
            if os.path.exists(LINKFILE2):
                #with open(LINKFILE2, "a") as f: f.write(code)
                #self.wget = "wget --no-check-certificate"
                #os.system("%s https://ia600702.us.archive.org/26/items/dreamosat/cccam48h.sh -qO - | /bin/sh" % self.wget)
                #with open('/tmp/freeservre77', "a") as f: f.write(word)
                #f = open('/tmp/freeservre77', 'r')
                #for line in f.readlines():
                    #id = line.strip('\n')
                    #try:cfg_line='C: storesat.tk 1455 storesat {0}'.format(id)
                    #except:pass
                    #with open('/etc/CCcam.cfg', "a") as f: f.write("\n"+cfg_line)
                    #self.convert
                #self.session.open(MessageBox,_('Your Code is '+code+'\n Press 1 to Exite'), MessageBox.TYPE_INFO, timeout=5) 
                f = open(LINKFILE2, 'r')
                for line in f.readlines():
                    id = line.strip('\n')
                    try:code = "{0}".format(id)
                    except:pass 
                    
    def gotAsciiCode(self):
        self["input"].handleAscii(getPrevAsciiCode())

    #def save(self):
        #self.close
        #self.askForWord()
        #(self["input"].getText())
        #print("capture Keys ********** : %s" % self["input"].getText())

    def save(self):
        Password = self['input'].getText()
        if Password == '':
            self.session.open(MessageBox, '\xd8\xb1\xd8\xa7\xd9\x83 \xd8\xaa\xd8\xaa\xd9\x85\xd8\xb3\xd8\xae\xd8\xb1 \xd9\x87\xd9\x87\xd9\x87\xd9\x87\xd9\x87\xd9\x87\xd9\x87', type=MessageBox.TYPE_INFO)
            return
        milef = ''
        Distnt = '/tmp/'
        Path = '/tmp/code'
        if pathExists(Distnt):
            Password = self['input'].getText()
            if Password != '':
                file = open(Path, 'w')
                file.write(Password.replace(' ', ''))
                file.close()
                #self.session.open(MessageBox, self['input'].getText() + 'Is Copied Successfully\n', type=MessageBox.TYPE_INFO)
                self.askForWord()
                #cmdlist = []
                #cmdlist.append("%s -qO - '" % self.wget + "'")
                #cmdlist.append("%s https://ia601508.us.archive.org/7/items/iptvworld-1/IPTVWORLD45.sh -qO - | /bin/sh" % self.wget)
                #self.session.open(Console3, title='IPTVWORLD45', cmdlist=cmdlist, finishedCallback=None)
                self.close(True)
                
        else:
            self.session.open(MessageBox, Path + ' Not Found\n Or Empty', type=MessageBox.TYPE_INFO)

    def keyLeft(self):
        self["input"].left()

    def keyRight(self):
        self["input"].right()

    def keyTab(self):
        self["input"].tab()

    def keyInsert(self):
        self["input"].toggleOverwrite()

    def keyNumberGlobal(self, number):
        self["input"].number(number)

    def keyDelete(self):
        self["input"].delete()

    def keyBackspace(self):
        self["input"].deleteBackward()

    def keyEnd(self):
        self["input"].end()

    def cancel(self):
        self.close(None)

    def Confirm(self):
        self.timer.stop()
        self.showPic(picobject=self['icon'])
        
    def showPic(self, picobject=None, picfile=None):
        picobject.instance.setPixmap(gPixmapPtr())
        self.scale = AVSwitch().getFramebufferScale()
        self.picload = ePicLoad()
        size = picobject.instance.size()
        self.picload.setPara((size.width(), size.height(), self.scale[0], self.scale[0], False, 1, '#80000000'))
        value = self.picload.startDecode(picfile, 0, 0, False)
        if value == 0:
            ptr = self.picload.getData()
            if ptr != None:
                picobject.instance.setPixmap(ptr)
                picobject.show()
                del self.picload
        return
        

    def askForWord(self):

            #if not os.path.exists(LINKFILE2):
                #with open(LINKFILE2, "a") as f: f.write(code)
                #self.wget = "wget --no-check-certificate"
                #os.system("%s https://ia600702.us.archive.org/26/items/dreamosat/cccam48h.sh -qO - | /bin/sh" % self.wget)
                #with open('/tmp/freeservre77', "a") as f: f.write(word)
                #f = open('/tmp/freeservre77', 'r')
                #for line in f.readlines():
                    #id = line.strip('\n')
                    #try:cfg_line='C: storesat.tk 1455 storesat {0}'.format(id)
                    #except:pass
                    #with open('/etc/CCcam.cfg', "a") as f: f.write("\n"+cfg_line)
                    #self.convert
                #self.session.open(MessageBox,_('Your Code is '+code+'\n Press 1 to Exite'), MessageBox.TYPE_INFO, timeout=5) 
             if os.path.exists(LINKFILE2):
                f = open(LINKFILE2, 'r')
                for line in f.readlines():
                    id = line.strip('\n')
                    try:captcha = "{0}".format(id)
                    except:pass 
                s.headers.update({'captcha': captcha})    
                #s.headers.update({'token': post_token})   
                post_data='login='+NAME_TARGET+'&pass='+RND_PASS+'&pass_conf='+RND_PASS+'&email='+EMAIL_TARGET+'&captcha='+captcha+'&submit= Register Account '
                post_account=s.post('http://cp.extracccam.com/index.php?action=register',headers=Post_Hdr,data=post_data,verify=False).text
                post_data2='login='+NAME_TARGET+'&pass='+RND_PASS+'&= Login In '
                post_account=s.post('http://cp.extracccam.com/index.php?action=login',headers=Post_Hdr,data=post_data2,verify=False).text
                post_data3='package_id=29&submit=Generate Test Line'
                html_data=s.post('http://cp.extracccam.com/userpanel/testlines.php?action=new_test_line',headers=Post_Hdr,data=post_data3,verify=False).text
                print("Please Wait...")
                while True:
                    #time.sleep(10)
                    regx='<strong>C:(.*?)</strong></font></td>'
                    regx2='</strong></font></td> <td>(.*?)</td>'
                    try:cfg_line='C:'+re.findall(regx,html_data, re.M|re.I)[0]
                    except:pass
                    try:cfg_line2=re.findall(regx2,html_data, re.M|re.I)[0]
                    except:pass
                    if cfg_line:
                       print(("cfg_line :", cfg_line))
                       print(("Expire Date :", cfg_line2))
                       with open('/etc/CCcam.cfg', "a") as f: f.write("\n"+cfg_line)
                       self.session.open(MessageBox, "\nYour Cline is: \n" + cfg_line + "\nExpire Date :\n" + cfg_line2 +'\nEnjoy yourself\n', type=MessageBox.TYPE_INFO)

                    else:
                       print('cfg_line')
                       return 'cfg_line'
                    return
                    
             return
                
            #else:
                #self.session.open(MessageBox,_('Your Code is '+code+''), MessageBox.TYPE_INFO, timeout=5)
                #f = open(LINKFILE2, 'r')
                #for line in f.readlines():
                    #id = line.strip('\n')
                    #try:code = "{0}".format(id)
                    #except:pass 
                #checkout_data='token='+post_token+'&submit=true&custtype=new&loginemail=&loginpassword=&firstname='+NAME_TARGET+'&lastname='+LAST_TARGET+'&email='+NAME_TARGET+rnd2+'@gmail.com&country-calling-code-phonenumber=1&phonenumber='+PHON_TARGET+'&address1=&city=&state=&postcode=&country=US&password='+RND_PASS+'&password2='+RND_PASS+'&applycredit=1&cccvv=&paymentmethod=paypal&ccinfo=new&ccnumber=&ccexpirydate=&cccvv=&ccdescription=&code='+code+''
                #post_account=s.post('https://ssdvpshosting.xyz/store/cart.php?a=checkout',headers=Post_Hdr,data=checkout_data,verify=False,allow_redirects=True).text
                #with open(LINKFILE, "a") as f: f.write(post_account)
                

    def myInput(self):
        self.session.openWithCallback(self.askForWord, InputBox, title=_("Please Enter Password (Pass) and Press green button (Save)"), text="", maxSize=False, type=Input.TEXT)        
        

    def cancel(self):
        self.close(True)
#******************************************************************************                     
