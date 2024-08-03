# -*- coding: utf-8 -*-
from .compat import PY3
from enigma import eConsoleAppContainer
from Screens.Screen import Screen
from Components.ActionMap import ActionMap
from Components.ScrollLabel import ScrollLabel
from Components.Sources.StaticText import StaticText
from Screens.MessageBox import MessageBox
from enigma import getDesktop
from Plugins.Extensions.FreeServer.outils.Input import *


def DreamOS():
    if os.path.exists('/var/lib/dpkg/status'):
        return DreamOS
        
def getDesktopSize():
    s = getDesktop(0).size()
    return (s.width(), s.height())

def isHD():
    desktopSize = getDesktopSize()
    return desktopSize[0] == 1280
    
class Console33(Screen):
    global HD_Res
    try:
        sz_w = getDesktop(0).size().width()
        if sz_w == 1280:
            fullHD_Res = False
        elif sz_w == 1920:
            fullHD_Res = True
        else:
            fullHD_Res = False
    except:
        HD_Res = False


    if fullHD_Res == False:
        skin = '''\n        \t\n                <screen name="Console33"  backgroundColor="#800009" position="center,center" size="920,600" title=""   >\n                \n\t\t<widget name="text" backgroundColor="#380038" position="30,30" size="865,570" font="Regular;20"   zPosition="2"  />
                                          <widget name="text" position="22,104" font="bpmo;22" size="756,256" foregroundColor="#f5f5dc" transparent="1" zPosition="10"/>
                                          <widget source="global.CurrentTime" render="Label" position="756,25" size="156,44" foregroundColor="#00ffffff" transparent="1" zPosition="1" font="bpmo;20">
                                            <convert type="ClockToText">Format:%A. %d.%m.%Y</convert>
                                          </widget>
                                          <widget source="global.CurrentTime" render="Label" position="410,25" size="250,45" foregroundColor="#00ffffff" transparent="1" zPosition="1" font="bpmo;33" halign="right">
                                            <convert type="ClockToText">Format:%-H:%M:%S</convert>
                                          </widget> 
                                          <!--widget name="key_green" position="165,532" size="200,30" foregroundColor="#008000" transparent="1" font="bpmo;28"/-->
                                                </screen>'''

    else:
        skin = '''\n        \t\n                <screen name="Console33" position="center,center" size="1380,675" title=""   >\n                \n\t\t<widget name="text" position="28,33" size="831,640" font="Regular;33"  transparent="1" zPosition="2"  />
                                          <widget name="text" position="22,104" font="bpmo;22" size="756,256" foregroundColor="#f5f5dc" transparent="1" zPosition="2"/>
                                          <widget source="global.CurrentTime" render="Label" position="756,25" size="156,44" foregroundColor="#00ffffff" transparent="1" zPosition="2" font="bpmo;20">
                                                        <convert type="ClockToText">Format:%A. %d.%m.%Y</convert>
                                          </widget>
                                          <widget source="global.CurrentTime" render="Label" position="287,17" size="150,35" foregroundColor="#00ffffff" transparent="1" zPosition="2" font="bpmo;24" halign="right">
                                                        <convert type="ClockToText">Format:%-H:%M:%S</convert>
                                          </widget>
                                          <!--widget name="key_green" position="320,532" size="200,28" foregroundColor="#008000" transparent="1" font="bpmo;24"/-->
                                                </screen>'''


    def __init__(self, session, title = 'Console', cmdlist = None, finishedCallback = None, closeOnSuccess = False, showStartStopText = True, skin = None, instr = None, endstr = None):
        Screen.__init__(self, session)
        self.color = '#800009' #001780
        self.finishedCallback = finishedCallback
        self.closeOnSuccess = closeOnSuccess
        self.showStartStopText = showStartStopText
        self.endstr = 'Press OK to exit'
        instr = 'Installing please wait\nEnigma will be restarted after finishing' + '\n*************************************\n'
        self['text'] = ScrollLabel(instr)
        self['key_red'] = StaticText(_('Cancel'))
        self['actions'] = ActionMap(['WizardActions', 'DirectionActions', 'ColorActions'], {'blue': self.restartenigma,
         'ok': self.cancel,
         'back': self.cancel,
         'up': self['text'].pageUp,
         'down': self['text'].pageDown}, -1)
        self.cmdlist = cmdlist
        self.newtitle = title
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
                
    def restartenigmold(self):
        os.system('killall -9 enigma2')

    def updateTitle(self):
        self.setTitle(self.newtitle)

    def startRun(self):
        self.run
        self.cmdlist[self.run]
        if self.container.execute(self.cmdlist[self.run]):
            self.runFinished(-1)
            
    def runFinished(self, retval):
        self.run += 1
        self.setTitle('Execution Finished')
        if self.run != len(self.cmdlist):
            if self.container.execute(self.cmdlist[self.run]):
                self.runFinished(-1)
        else:
            str = self['text'].getText()
            str += '\n' + _('Execution finished!!')
            self['text'].setText(str)
            self['text'].lastPage()
            if self.finishedCallback is not None and not retval:
                self.finishedCallback(True)
            if not retval and self.closeOnSuccess == False:
                self.restartenigma()
                self.cancel()
            else:
                str += '\n' + _(self.endstr)
                self['text'].setText(str)
                self['text'].lastPage()
        return
        

    def cancel(self):
        if self.finishedCallback is not None:
            self.finishedCallback(True)
        try:
            if DreamOS():
                self.container.appClosed.remove(self.runFinished)
                self.container.dataAvail.remove(self.dataAvail)
                self.close()
            else:
                self.contianer_closed = None
                self.contianer_dataAvail = None
                self.close()
            if self.run == len(self.cmdlist):
                self.close()
        except:
            pass

        return

    def dataAvail(self, str):
        if PY3:
            import six
            str = six.ensure_str(str)
            self["text"].appendText(str)
        else:
            self['text'].appendText(str)
                
    def restartenigma(self):
        if self.finishedCallback is not None:
            self.finishedCallback(True)
        self.session.open(TryQuitMainloop, 3)
        return

