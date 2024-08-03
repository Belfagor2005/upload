# -*- coding: utf-8 -*-
import os, re
from Components.config import *
from enigma import eConsoleAppContainer
from Screens.Screen import Screen
from Components.ActionMap import ActionMap
from Components.ScrollLabel import ScrollLabel
from Components.Sources.StaticText import StaticText
from Screens.MessageBox import MessageBox
from enigma import getDesktop
from Screens.Standby import TryQuitMainloop
from .compat import PY3
from .Update import News2
from .MyStatus import MyStatus
from Tools.Directories import fileExists
def DreamOS():
    if os.path.exists('/var/lib/dpkg/status'):
        return DreamOS
def getDesktopSize():
    s = getDesktop(0).size()
    return (s.width(), s.height())

def isHD():
    desktopSize = getDesktopSize()
    return desktopSize[0] == 1280

class Console3(Screen):
    if isHD():
    	skin = '''
    	<screen position="17,center" size="1245,681" title="Command execution..." backgroundColor="#16000000" flags="wfNoBorder">
		<widget name="text" position="9,48" size="1237,587" backgroundColor="#16000000" foregroundColor="#00ffffff" font="Console;24"/>
		<eLabel text="Command execution..." font="Regular;30" size="767,40" position="8,3" foregroundColor="#00ffffff" backgroundColor="#16000000" zPosition="4"/>
		<widget source="global.CurrentTime" render="Label" position="781,10" size="303,28" foregroundColor="#00ffffff" transparent="1" zPosition="1" font="bpmo;24" halign="center" valign="center">
			<convert type="ClockToText">Format:%A. %d.%m.%Y</convert>
		</widget>
		<widget source="global.CurrentTime" render="Label" position="1081,10" size="156,28" foregroundColor="#00ffffff" transparent="1" zPosition="1" font="bpmo;24" halign="right" valign="center">
			<convert type="ClockToText">Format:%-H:%M:%S</convert>
		</widget>
		<eLabel position="10,674" size="165,5" backgroundColor="#00ff2525" zPosition="1"/>
		<eLabel position="238,674" size="165,5" backgroundColor="#00389416" zPosition="1"/>
		<eLabel position="458,674" size="165,5" backgroundColor="#00e5b243" zPosition="1"/>
		<eLabel position="668,674" size="165,5" backgroundColor="#000080ff" zPosition="1"/>
		<widget source="key_red" render="Label" position="10,646" zPosition="2" size="165,30" font="Regular;24" halign="center" valign="center" backgroundColor="#16000000" foregroundColor="#00ffffff" transparent="1"/>
		<widget source="key_green" render="Label" position="238,646" zPosition="2" size="165,30" font="Regular;24" halign="center" valign="center" backgroundColor="#16000000" foregroundColor="#00ffffff" transparent="1"/>
		<widget source="key_yellow" render="Label" position="458,646" zPosition="2" size="165,30" font="Regular;24" halign="center" valign="center" backgroundColor="#16000000" foregroundColor="#00ffffff" transparent="1"/>
		<widget source="key_blue" render="Label" position="668,646" zPosition="2" size="165,30" font="Regular;24" halign="center" valign="center" backgroundColor="#16000000" foregroundColor="#00ffffff" transparent="1"/>
		<ePixmap position="1100,646" zPosition="1" size="60,25" pixmap="/usr/lib/enigma2/python/Plugins/Extensions/FreeServer/Deco/key_menu.png" alphatest="blend"/>
    	</screen>'''
    else:
    	skin = '''
    	<screen position="center,center" size="1886,1051" title="Command execution..." backgroundColor="#16000000" flags="wfNoBorder">
		<widget name="text" position="9,93" size="1868,897" backgroundColor="#16000000" foregroundColor="#00ffffff" font="Console;33"/>
		<eLabel text="Command execution..." font="Regular;45" size="1163,80" position="8,3" foregroundColor="#00ffffff" backgroundColor="#16000000" zPosition="4"/>
		<widget source="global.CurrentTime" render="Label" position="1202,17" size="380,55" foregroundColor="#00ffffff" transparent="1" zPosition="1" font="bpmo;30" halign="center" valign="center">
			<convert type="ClockToText">Format:%A. %d.%m.%Y</convert>
		</widget>
		<widget source="global.CurrentTime" render="Label" position="1576,17" size="302,55" foregroundColor="#00ffffff" transparent="1" zPosition="1" font="bpmo;35" halign="right" valign="center">
			<convert type="ClockToText">Format:%-H:%M:%S</convert>
 		 </widget>
		<eLabel position="10,1043" size="250,5" backgroundColor="#00ff2525" zPosition="1"/>
		<eLabel position="353,1043" size="250,5" backgroundColor="#00389416" zPosition="1"/>
		<eLabel position="688,1043" size="250,5" backgroundColor="#00e5b243" zPosition="1"/>
		<eLabel position="1031,1043" size="250,5" backgroundColor="#000080ff" zPosition="1"/>
		<widget source="key_red" render="Label" position="10,1004" zPosition="2" size="250,40" font="Regular;28" halign="center" valign="center" backgroundColor="#16000000" foregroundColor="#00ffffff" transparent="1"/>
		<widget source="key_green" render="Label" position="353,1004" zPosition="2" size="250,40" font="Regular;28" halign="center" valign="center" backgroundColor="#16000000" foregroundColor="#00ffffff" transparent="1"/>
		<widget source="key_yellow" render="Label" position="688,1004" zPosition="2" size="250,40" font="Regular;28" halign="center" valign="center" backgroundColor="#16000000" foregroundColor="#00ffffff" transparent="1"/>
		<widget source="key_blue" render="Label" position="1031,1004" zPosition="2" size="250,40" font="Regular;28" halign="center" valign="center" backgroundColor="#16000000" foregroundColor="#00ffffff" transparent="1"/>
		<ePixmap position="1764,1003" zPosition="1" size="100,40" pixmap="/usr/lib/enigma2/python/Plugins/Extensions/FreeServer/Deco/key_menuFHD.png" alphatest="blend"/>
    	</screen>'''

    def __init__(self, session, title = 'Console', cmdlist = None, finishedCallback = None, closeOnSuccess = False, showStartStopText = True, skin = None, instr = None, endstr = None):
        Screen.__init__(self, session)
        self.finishedCallback = finishedCallback
        self.closeOnSuccess = closeOnSuccess
        self.showStartStopText = showStartStopText
        if skin:
            self.skinName = [skin, 'Console3']
        self.errorOcurred = False
        self.endstr = 'Press OK to exit'
        instr = 'Installing please wait\nEnigma will be restarted after finishing' + '\n*************************************\n'
        self['text'] = ScrollLabel(instr)
        self['key_red'] = StaticText(_('Cancel'))
        self['key_green'] = StaticText(_('Hide/Show'))
        self['key_yellow'] = StaticText(_('ABOUT'))
        self['key_blue'] = StaticText(_('INFO'))
        self['actions'] = ActionMap(['WizardActions', 'DirectionActions', 'ColorActions', 'MenuActions'],
        {
         	'red': self.cancel,
         	'green': self.toggleHideShow,
         	'yellow': self.about,
         	'blue': self.KeyInfo,
         	'ok': self.cancel,
         	'back': self.cancel,
         	'menu': self.menu,
         	'up': self['text'].pageUp,
         	'down': self['text'].pageDown
        }, -1)
        self.cmdlist = isinstance(cmdlist, list) and cmdlist or [cmdlist]
        self.newtitle = title == 'Console' and _('Console') or title
        self.cancel_msg = None 
        self.hideflag = True
        self.hideflag = False
        self.onShown.append(self.updateTitle)
        self.container = eConsoleAppContainer()
        self.run = 0
        self.finished = False
        try: ## DreamOS By RAED
        	self.container.appClosed.append(self.runFinished)
        	self.container.dataAvail.append(self.dataAvail)
        except:
            	self.container.appClosed_conn = self.container.appClosed.connect(self.runFinished)
            	self.container.dataAvail_conn = self.container.dataAvail.connect(self.dataAvail)
        self.onLayoutFinish.append(self.startRun)

    def updateTitle(self):
        self.setTitle(self.newtitle)

    def startRun(self):
        if self.showStartStopText:
            self['text'].setText(_('Execution progress:') + '\n\n')
        print('[Console] executing in run', self.run, ' the command:', self.cmdlist[self.run])
        if self.container.execute(self.cmdlist[self.run]):
            self.runFinished(-1)

    def runFinished(self, retval):
        if retval:
            self.errorOcurred = True
            self.show()
        self.run += 1
        if self.run != len(self.cmdlist):
            if self.container.execute(self.cmdlist[self.run]):
                self.runFinished(-1)
        else:
            self.show()
            self.finished = True
            try:
                  lastpage = self['text'].isAtLastPage()
            except:
                  lastpage = self['text']
            if self.cancel_msg:
                self.cancel_msg.close()
            if self.showStartStopText:
                self['text'].appendText(_('Execution finished!!'))
            if self.finishedCallback is not None and not retval:
#                self.finishedCallback(True)
                self.finishedCallback()
            if not retval and self.closeOnSuccess == False:
                return
                self.session.openWithCallback(self.restartenigma, MessageBox, _('Job Finish.\n\nDo want ot restart enigma2 now.'), MessageBox.TYPE_YESNO)
            else:
                str += '\n' + _(self.endstr)
                self['text'].setText(str)
                self['text'].lastPage()

    def KeyInfo(self):
        self.session.open(News2)
            
    def about(self):
        self.session.open(MyStatus)   

    def menu(self):
        from .Input import Input
        self.session.open(Input) 
            

    #def toggleHideShow(self):
        #if self.finished:
            #return
        #if self.shown:
            #self.hide()
        #else:
            #self.show()

    def toggleHideShow(self):
        if self.finished:
            return
        if self.hideflag == True:
            self.hideflag = False
            count = 40
            while count > 0:
                count -= 1
                f = open('/proc/stb/video/alpha', 'w')
                f.write('%i' % (config.av.osd_alpha.value * count / 40))
                f.close()
        else:
            self.hideflag = True
            count = 0
            while count < 40:
                count += 1
                f = open('/proc/stb/video/alpha', 'w')
                f.write('%i' % (config.av.osd_alpha.value * count / 40))
                f.close()
                    
    #def toggleHideShow(self):
        #if self.finished:
            #return
        #if self.shown:
            #self.hide()
        #else:
            #self.show()

    def cancel(self):
        if self.finished:
            self.closeConsole()
        else:
            self.cancel_msg = self.session.openWithCallback(self.cancelCallback, MessageBox, _('Cancel execution?'), type=MessageBox.TYPE_YESNO, default=False)

    def cancelCallback(self, ret = None):
        self.cancel_msg = None
        if ret:
            try: ## DreamOS By RAED
                self.container.appClosed.remove(self.runFinished)
                self.container.dataAvail.remove(self.dataAvail)
            except:
                self.container.appClosed_conn = None
                self.container.dataAvail_conn = None
            self.container.kill()
            self.close()

    def closeConsole(self):
        if self.finished:
            try: ## DreamOS By RAED
                self.container.appClosed.remove(self.runFinished)
                self.container.dataAvail.remove(self.dataAvail)
            except:
                self.container.appClosed_conn = None
                self.container.dataAvail_conn = None
            self.close()
        else:
            self.show()
            
    def dataAvail(self, str):
        if PY3:
            str = (str).decode()
        self['text'].setText(self['text'].getText() + str)
        
    def restartenigma(self, answer=False):
        if answer:
        	from Screens.Standby import TryQuitMainloop
        	self.session.open(TryQuitMainloop, 3)
        else:
        	return
