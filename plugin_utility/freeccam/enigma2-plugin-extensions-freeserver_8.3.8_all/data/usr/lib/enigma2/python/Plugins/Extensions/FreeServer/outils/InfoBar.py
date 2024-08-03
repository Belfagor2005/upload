# -*- coding: UTF-8 -*-
from __future__ import print_function

from Components.MenuList import MenuList
import io
from Components.Label import Label
from Plugins.Plugin import PluginDescriptor
from Tools.BoundFunction import boundFunction
from Screens.MessageBox import MessageBox
from Screens.Screen import Screen
from Screens.ChoiceBox import ChoiceBox
from Components.ActionMap import ActionMap, NumberActionMap
from Components.Sources.StaticText import StaticText
from Components.Sources.List import List
from Components.AVSwitch import AVSwitch
from Components.config import config, Config, ConfigSelection, ConfigSubsection, ConfigText, getConfigListEntry, ConfigYesNo, ConfigIP, ConfigNumber, ConfigLocations
from Components.config import KEY_DELETE, KEY_BACKSPACE, KEY_LEFT, KEY_RIGHT, KEY_HOME, KEY_END, KEY_TOGGLEOW, KEY_ASCII, KEY_TIMEOUT
from Components.ConfigList import ConfigListScreen
from Components.ServiceEventTracker import ServiceEventTracker, InfoBarBase
from Tools.Directories import pathExists, fileExists, resolveFilename, SCOPE_PLUGINS, SCOPE_SKIN_IMAGE, SCOPE_HDD, SCOPE_CURRENT_PLUGIN, SCOPE_CURRENT_SKIN
from Tools.LoadPixmap import LoadPixmap
from enigma import eTimer, quitMainloop, eListbox, ePoint, RT_HALIGN_LEFT, RT_HALIGN_RIGHT, RT_VALIGN_CENTER, eListboxPythonMultiContent, eListbox, gFont, getDesktop, ePicLoad, eServiceCenter, iServiceInformation, eServiceReference, iSeekableService, iServiceInformation, iPlayableService, iPlayableServicePtr
from os import path as os_path, system as os_system, unlink, stat, mkdir, popen, makedirs, listdir, access, rename, remove, W_OK, R_OK, F_OK
from twisted.web import client
from twisted.internet import reactor
from time import time
from Plugins.Extensions.FreeServer.outils.MyDynaTextScreen import *
from Screens.InfoBarGenerics import InfoBarShowHide, InfoBarSeek, InfoBarNotifications, InfoBarServiceNotifications
from Screens.InfoBarGenerics import InfoBarShowHide, NumberZap, InfoBarSeek, InfoBarAudioSelection, InfoBarSubtitleSupport  #1680,1152
dwidth = getDesktop(0).size().width()

######################################################################################################
from Components.Pixmap import Pixmap
from Components.ActionMap import ActionMap
from Components.Input import Input
from Screens.InputBox import InputBox
from Tools.Directories import fileExists
from Screens.Screen import Screen
import re
from Plugins.Plugin import PluginDescriptor
from Tools.Directories import fileExists
from Screens.Screen import Screen
from Screens.Standby import *
from Tools.Directories import *
from Components.Sources.List import List
from Components.MenuList import MenuList
from Components.Pixmap import Pixmap
from Components.ActionMap import ActionMap, NumberActionMap
from Components.Label import Label
from Components.Button import Button
from Components.Sources.StaticText import StaticText
from Components.ScrollLabel import ScrollLabel
from Components.MultiContent import MultiContentEntryText, MultiContentEntryPixmapAlphaTest
from Components.config import config, ConfigSelection, getConfigListEntry, ConfigSubsection, configfile
from enigma import eListbox, eTimer, eListboxPythonMultiContent, gFont, getDesktop, loadPNG, eConsoleAppContainer
from enigma import *

plugin_path = '/usr/lib/enigma2/python/Plugins/Extensions/FreeServer/fonts'
skin_path = '/usr/lib/enigma2/python/Plugins/Extensions/FreeServer/Skin/'
p_path = '/usr/lib/enigma2/python/Plugins/Extensions/FreeServer'   
from enigma import addFont
try:
    #addFont('%s/Raleway-Black.ttf' % plugin_path, 'Rale', 100, 1)
    #addFont('%s/PlayfairDisplay-Black.otf' % plugin_path, 'Play', 100, 1)
    addFont('%s/bpmono.ttf' % plugin_path, 'bpmo', 100, 1)
except Exception as ex:
    print(ex)
#########################################################################################################

class ALAJREStream(Screen, InfoBarNotifications):
    STATE_IDLE = 0
    STATE_PLAYING = 1
    STATE_PAUSED = 2
    ENABLE_RESUME_SUPPORT = True
    ALLOW_SUSPEND = True
    PLAYER_STOPS = 3
    skinfhd = '''<screen name="ALAJREStream" flags="wfNoBorder" position="0,0" size="1920,1080" title="ALAJREStream" backgroundColor="transparent">
<widget source="session.CurrentService" render="Label" position="0,0" size="1920,1080" font="Regular; 22" backgroundColor="#263c59" shadowColor="#1d354c" shadowOffset="-100,-100" transparent="1" zPosition="1" halign="center">
<convert type="ServiceName">Name</convert>
</widget>
<widget source="global.CurrentTime" render="Label" position="266,222" size="250,100" font="bpmo; 32" halign="left" backgroundColor="black" transparent="1">
<convert type="ClockToText">Format:%H:%M:%S</convert>
</widget>
<ePixmap position="0,0" size="1920,1080" pixmap="/usr/lib/enigma2/python/Plugins/Extensions/FreeServer/Cimages/Freeservers_5.png" zPosition="-1" transparent="1" alphatest="blend" />
<ePixmap position="0,0" size="1920,1080" pixmap="/usr/lib/enigma2/python/Plugins/Extensions/FreeServer/Deco/button_red.png" zPosition="-1" transparent="1" alphatest="blend" />
<eLabel text="Exit" zPosition="1" position="40,0" size="160,35" font="Regular; 20" transparent="1" backgroundColor="black" halign="left" valign="left" />
</screen>'''
    skinhd = '''<screen name="LiveSoccerStream" flags="wfNoBorder" position="0,0" size="1280,720" title="LiveSoccerStream" backgroundColor="transparent">
<widget source="session.CurrentService" render="Label" position="0,0" size="1280,720" font="Regular; 22" backgroundColor="#263c59" shadowColor="#1d354c" shadowOffset="-100,-100" transparent="1" zPosition="1" halign="center">
<convert type="ServiceName">Name</convert>
</widget>
<widget source="global.CurrentTime" render="Label" position="266,22" size="150,100" font="bpmo; 32" halign="left" backgroundColor="black" transparent="1">
<convert type="ClockToText">Format:%H:%M:%S</convert>
</widget>
<ePixmap position="0,0" size="1280,720" pixmap="/usr/lib/enigma2/python/Plugins/Extensions/FreeServer/Cimages/Freeservers_5.png" zPosition="-1" transparent="1" alphatest="blend" />
<ePixmap position="0,0" size="1920,1080" pixmap="/usr/lib/enigma2/python/Plugins/Extensions/FreeServer/Deco/button_red.png" zPosition="-1" transparent="1" alphatest="blend" />
<eLabel text="Exit" zPosition="1" position="40,0" size="100,25" font="Regular; 20" transparent="1" backgroundColor="black" halign="left" valign="left" />
</screen>'''

    def __init__(self, session, service):
        Screen.__init__(self, session)
        if dwidth == 1280:
            self.skin = ALAJREStream.skinhd
        else:
            self.skin = ALAJREStream.skinfhd
        InfoBarNotifications.__init__(self)
        self.session = session
        self.service = service
        self.screen_timeout = 1000
        self.__event_tracker = ServiceEventTracker(screen=self, eventmap={iPlayableService.evSeekableStatusChanged: self.__seekableStatusChanged,
         iPlayableService.evStart: self.__serviceStarted,
         iPlayableService.evEOF: self.__evEOF})
        self['ButtonRedtext'] = Label(_('Exit'))                
        self['text'] = Label()
        self['actions'] = ActionMap(['SetupActions', 'DirectionActions', 'ColorActions', 
        #self['actions'] = ActionMap(['OkCancelActions',
         'InfobarSeekActions',
         'ColorActions',
         'MediaPlayerActions',
         'MovieSelectionActions'], {'ok': self.leavePlayer,
         'cancel': self.leavePlayer,
         'exit': self.exit,         
         'stop': self.leavePlayer}, -2)
        self['pauseplay'] = Label(_('Play'))
        self.hidetimer = eTimer()
        self.repeter = True
        self.state = self.STATE_PLAYING
        self.onPlayStateChanged = []
        self.play()
        self.onClose.append(self.__onClose)

    def __onClose(self):
        self.session.nav.stopService()

    def __evEOF(self):
        self.STATE_PLAYING = True
        self.state = self.STATE_PLAYING
        self.session.nav.playService(self.service)
        if self.session.nav.stopService():
            self.state = self.STATE_PLAYING
            self.session.nav.playService(self.service)
        else:
            self.leavePlayer()

    def __setHideTimer(self):
        self.hidetimer.start(self.screen_timeout)

    def ok(self):
        self.leavePlayer()
        
    def exit(self):
        self.close()
        
    def playNextFile(self):
        self.session.open(MessageBox, 'only to watch not play Next and Prev File', MessageBox.TYPE_INFO)

    def playPrevFile(self):
        self.session.open(MessageBox, 'only to watch not play Next and Prev File', MessageBox.TYPE_INFO)

    def playService(self, newservice):
        if self.state == self.STATE_IDLE:
            self.play()
        self.service = newservice

    def play(self):
        self.state = self.STATE_PLAYING
        self['pauseplay'].setText('PLAY')
        self.session.nav.playService(self.service)
        self.__evEOF

    def __seekableStatusChanged(self):
        service = self.session.nav.getCurrentService()
        if service is not None:
            seek = service.seek()
            if seek is None or not seek.isCurrentlySeekable():
                self.setSeekState(self.STATE_PLAYING)
                self.__evEOF
        return

    def __serviceStarted(self):
        self.state = self.STATE_PLAYING
        self.__evEOF

    def setSeekState(self, wantstate):
        print('setSeekState')
        if wantstate == self.STATE_PAUSED:
            print('trying to switch to Pause- state:', self.STATE_PAUSED)
        elif wantstate == self.STATE_PLAYING:
            print('trying to switch to playing- state:', self.STATE_PLAYING)
        service = self.session.nav.getCurrentService()
        if service is None:
            print('No Service found')
            return False
        else:
            pauseable = service.pause()
            if pauseable is None:
                print('not pauseable.')
                self.state = self.STATE_PLAYING
            if pauseable is not None:
                print('service is pausable')
                if wantstate == self.STATE_PAUSED:
                    print('WANT TO PAUSE')
                    pauseable.pause()
                    self.state = self.STATE_PAUSED
                    if not self.shown:
                        self.hidetimer.stop()
                        self.show()
                elif wantstate == self.STATE_PLAYING:
                    print('WANT TO PLAY')
                    pauseable.unpause()
                    self.state = self.STATE_PLAYING
                    if self.shown:
                        self.__setHideTimer()
            for c in self.onPlayStateChanged:
                c(self.state)

            return True
            return

    def handleLeave(self):
        self.close()

    def leavePlayer(self):
        self.close()                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 
class ALAJREStream2(Screen, InfoBarNotifications):
    STATE_IDLE = 0
    STATE_PLAYING = 1
    STATE_PAUSED = 2
    ENABLE_RESUME_SUPPORT = True
    ALLOW_SUSPEND = True
    PLAYER_STOPS = 3
    skinfhd = '''<screen name="ALAJREStream2" flags="wfNoBorder" position="0,0" size="1920,1080" title="ALAJREStream" backgroundColor="transparent">
<widget source="session.CurrentService" render="Label" position="0,0" size="1920,1080" font="Regular; 22" backgroundColor="#263c59" shadowColor="#1d354c" shadowOffset="-100,-100" transparent="1" zPosition="1" halign="center">
<convert type="ServiceName">Name</convert>
</widget>
<widget source="global.CurrentTime" render="Label" position="266,222" size="250,100" font="bpmo; 32" halign="left" backgroundColor="black" transparent="1">
<convert type="ClockToText">Format:%H:%M:%S</convert>
</widget>
<ePixmap position="0,0" size="1920,1080" pixmap="/usr/lib/enigma2/python/Plugins/Extensions/FreeServer/Cimages/Freeservers_3.png" zPosition="-1" transparent="1" alphatest="blend" />
<ePixmap position="0,0" size="1920,1080" pixmap="/usr/lib/enigma2/python/Plugins/Extensions/FreeServer/Deco/button_red.png" zPosition="-1" transparent="1" alphatest="blend" />
<eLabel text="Exit" zPosition="1" position="40,0" size="160,35" font="Regular; 20" transparent="1" backgroundColor="black" halign="left" valign="left" />
</screen>'''
    skinhd = '''<screen name="LiveSoccerStream" flags="wfNoBorder" position="0,0" size="1280,720" title="LiveSoccerStream" backgroundColor="transparent">
<widget source="session.CurrentService" render="Label" position="0,0" size="1280,720" font="Regular; 22" backgroundColor="#263c59" shadowColor="#1d354c" shadowOffset="-100,-100" transparent="1" zPosition="1" halign="center">
<convert type="ServiceName">Name</convert>
</widget>
<widget source="global.CurrentTime" render="Label" position="266,22" size="150,100" font="bpmo; 32" halign="left" backgroundColor="black" transparent="1">
<convert type="ClockToText">Format:%H:%M:%S</convert>
</widget>
<ePixmap position="0,0" size="1280,720" pixmap="/usr/lib/enigma2/python/Plugins/Extensions/FreeServer/Cimages/Freeservers_3.png" zPosition="-1" transparent="1" alphatest="blend" />
<ePixmap position="0,0" size="1920,1080" pixmap="/usr/lib/enigma2/python/Plugins/Extensions/FreeServer/Deco/button_red.png" zPosition="-1" transparent="1" alphatest="blend" />
<eLabel text="Exit" zPosition="1" position="40,0" size="100,25" font="Regular; 20" transparent="1" backgroundColor="black" halign="left" valign="left" />
</screen>'''


    def __init__(self, session, service):
        Screen.__init__(self, session)
        if dwidth == 1280:
            self.skin = ALAJREStream2.skinhd
        else:
            self.skin = ALAJREStream2.skinfhd
        InfoBarNotifications.__init__(self)
        self.session = session
        self.service = service
        self.screen_timeout = 1000
        self.__event_tracker = ServiceEventTracker(screen=self, eventmap={iPlayableService.evSeekableStatusChanged: self.__seekableStatusChanged,
         iPlayableService.evStart: self.__serviceStarted,
         iPlayableService.evEOF: self.__evEOF})
        self['ButtonRedtext'] = Label(_('Exit'))                
        self['text'] = Label()
        self['actions'] = ActionMap(['SetupActions', 'DirectionActions', 'ColorActions', 
        #self['actions'] = ActionMap(['OkCancelActions',
         'InfobarSeekActions',
         'ColorActions',
         'MediaPlayerActions',
         'MovieSelectionActions'], {'ok': self.leavePlayer,
         'cancel': self.leavePlayer,
         'exit': self.exit,         
         'stop': self.leavePlayer}, -2)
        self['pauseplay'] = Label(_('Play'))
        self.hidetimer = eTimer()
        self.repeter = True
        self.state = self.STATE_PLAYING
        self.onPlayStateChanged = []
        self.play()
        self.onClose.append(self.__onClose)
        
    def __onClose(self):
        self.session.nav.stopService()

    def __evEOF(self):
        self.STATE_PLAYING = True
        self.state = self.STATE_PLAYING
        self.session.nav.playService(self.service)
        if self.session.nav.stopService():
            self.state = self.STATE_PLAYING
            self.session.nav.playService(self.service)
        else:
            self.leavePlayer()

    def __setHideTimer(self):
        self.hidetimer.start(self.screen_timeout)

    def ok(self):
        self.leavePlayer()
        
    def exit(self):
        self.close()

    def playNextFile(self):
        self.session.open(MessageBox, 'only to watch not play Next and Prev File', MessageBox.TYPE_INFO)

    def playPrevFile(self):
        self.session.open(MessageBox, 'only to watch not play Next and Prev File', MessageBox.TYPE_INFO)

    def playService(self, newservice):
        if self.state == self.STATE_IDLE:
            self.play()
        self.service = newservice

    def play(self):
        self.state = self.STATE_PLAYING
        self['pauseplay'].setText('PLAY')
        self.session.nav.playService(self.service)
        self.__evEOF

    def __seekableStatusChanged(self):
        service = self.session.nav.getCurrentService()
        if service is not None:
            seek = service.seek()
            if seek is None or not seek.isCurrentlySeekable():
                self.setSeekState(self.STATE_PLAYING)
                self.__evEOF
        return

    def __serviceStarted(self):
        self.state = self.STATE_PLAYING
        self.__evEOF

    def setSeekState(self, wantstate):
        print('setSeekState')
        if wantstate == self.STATE_PAUSED:
            print('trying to switch to Pause- state:', self.STATE_PAUSED)
        elif wantstate == self.STATE_PLAYING:
            print('trying to switch to playing- state:', self.STATE_PLAYING)
        service = self.session.nav.getCurrentService()
        if service is None:
            print('No Service found')
            return False
        else:
            pauseable = service.pause()
            if pauseable is None:
                print('not pauseable.')
                self.state = self.STATE_PLAYING
            if pauseable is not None:
                print('service is pausable')
                if wantstate == self.STATE_PAUSED:
                    print('WANT TO PAUSE')
                    pauseable.pause()
                    self.state = self.STATE_PAUSED
                    if not self.shown:
                        self.hidetimer.stop()
                        self.show()
                elif wantstate == self.STATE_PLAYING:
                    print('WANT TO PLAY')
                    pauseable.unpause()
                    self.state = self.STATE_PLAYING
                    if self.shown:
                        self.__setHideTimer()
            for c in self.onPlayStateChanged:
                c(self.state)

            return True
            return

    def handleLeave(self):
        self.close()

    def leavePlayer(self):
        self.close()  

class ALAJREStream3(Screen, InfoBarNotifications):
    STATE_IDLE = 0
    STATE_PLAYING = 1
    STATE_PAUSED = 2
    ENABLE_RESUME_SUPPORT = True
    ALLOW_SUSPEND = True
    PLAYER_STOPS = 3
    skinfhd = '''<screen name="ALAJREStream3" flags="wfNoBorder" position="0,0" size="1920,1080" title="ALAJREStream" backgroundColor="transparent">
<widget source="session.CurrentService" render="Label" position="0,0" size="1920,1080" font="Regular; 22" backgroundColor="#263c59" shadowColor="#1d354c" shadowOffset="-100,-100" transparent="1" zPosition="1" halign="center">
<convert type="ServiceName">Name</convert>
</widget>
<widget source="global.CurrentTime" render="Label" position="266,222" size="250,100" font="bpmo; 32" halign="left" backgroundColor="black" transparent="1">
<convert type="ClockToText">Format:%H:%M:%S</convert>
</widget>
<ePixmap position="0,0" size="1920,1080" pixmap="/usr/lib/enigma2/python/Plugins/Extensions/FreeServer/Cimages/Freeservers_2.png" zPosition="-1" transparent="1" alphatest="blend" />
<ePixmap position="0,0" size="1920,1080" pixmap="/usr/lib/enigma2/python/Plugins/Extensions/FreeServer/Deco/button_red.png" zPosition="-1" transparent="1" alphatest="blend" />
<eLabel text="Exit" zPosition="1" position="40,0" size="160,35" font="Regular; 20" transparent="1" backgroundColor="black" halign="left" valign="left" />
</screen>'''
    skinhd = '''<screen name="LiveSoccerStream" flags="wfNoBorder" position="0,0" size="1280,720" title="LiveSoccerStream" backgroundColor="transparent">
<widget source="session.CurrentService" render="Label" position="0,0" size="1280,720" font="Regular; 22" backgroundColor="#263c59" shadowColor="#1d354c" shadowOffset="-100,-100" transparent="1" zPosition="1" halign="center">
<convert type="ServiceName">Name</convert>
</widget>
<widget source="global.CurrentTime" render="Label" position="266,22" size="150,100" font="bpmo; 32" halign="left" backgroundColor="black" transparent="1">
<convert type="ClockToText">Format:%H:%M:%S</convert>
</widget>
<ePixmap position="0,0" size="1280,720" pixmap="/usr/lib/enigma2/python/Plugins/Extensions/FreeServer/Cimages/Freeservers_2.jpg" zPosition="-1" transparent="1" alphatest="blend" />
<ePixmap position="0,0" size="1920,1080" pixmap="/usr/lib/enigma2/python/Plugins/Extensions/FreeServer/Deco/button_red.png" zPosition="-1" transparent="1" alphatest="blend" />
<eLabel text="Exit" zPosition="1" position="40,0" size="100,25" font="Regular; 20" transparent="1" backgroundColor="black" halign="left" valign="left" />
</screen>'''

    def __init__(self, session, service):
        Screen.__init__(self, session)
        if dwidth == 1280:
            self.skin = ALAJREStream3.skinhd
        else:
            self.skin = ALAJREStream3.skinfhd
        InfoBarNotifications.__init__(self)
        self.session = session
        self.service = service
        self.screen_timeout = 1000
        self.__event_tracker = ServiceEventTracker(screen=self, eventmap={iPlayableService.evSeekableStatusChanged: self.__seekableStatusChanged,
         iPlayableService.evStart: self.__serviceStarted,
         iPlayableService.evEOF: self.__evEOF})
        self['ButtonRedtext'] = Label(_('Exit'))                
        self['text'] = Label()
        self['actions'] = ActionMap(['SetupActions', 'DirectionActions', 'ColorActions', 
        #self['actions'] = ActionMap(['OkCancelActions',
         'InfobarSeekActions',
         'ColorActions',
         'MediaPlayerActions',
         'MovieSelectionActions'], {'ok': self.leavePlayer,
         'cancel': self.leavePlayer,
         'exit': self.exit,         
         'stop': self.leavePlayer}, -2)
        self['pauseplay'] = Label(_('Play'))
        self.hidetimer = eTimer()
        self.repeter = True
        self.state = self.STATE_PLAYING
        self.onPlayStateChanged = []
        self.play()
        self.onClose.append(self.__onClose)

    def __onClose(self):
        self.session.nav.stopService()

    def __evEOF(self):
        self.STATE_PLAYING = True
        self.state = self.STATE_PLAYING
        self.session.nav.playService(self.service)
        if self.session.nav.stopService():
            self.state = self.STATE_PLAYING
            self.session.nav.playService(self.service)
        else:
            self.leavePlayer()

    def __setHideTimer(self):
        self.hidetimer.start(self.screen_timeout)

    def ok(self):
        self.leavePlayer()
        
    def exit(self):
        self.close()
        
    def playNextFile(self):
        self.session.open(MessageBox, 'only to watch not play Next and Prev File', MessageBox.TYPE_INFO)

    def playPrevFile(self):
        self.session.open(MessageBox, 'only to watch not play Next and Prev File', MessageBox.TYPE_INFO)

    def playService(self, newservice):
        if self.state == self.STATE_IDLE:
            self.play()
        self.service = newservice

    def play(self):
        self.state = self.STATE_PLAYING
        self['pauseplay'].setText('PLAY')
        self.session.nav.playService(self.service)
        self.__evEOF

    def __seekableStatusChanged(self):
        service = self.session.nav.getCurrentService()
        if service is not None:
            seek = service.seek()
            if seek is None or not seek.isCurrentlySeekable():
                self.setSeekState(self.STATE_PLAYING)
                self.__evEOF
        return

    def __serviceStarted(self):
        self.state = self.STATE_PLAYING
        self.__evEOF

    def setSeekState(self, wantstate):
        print('setSeekState')
        if wantstate == self.STATE_PAUSED:
            print('trying to switch to Pause- state:', self.STATE_PAUSED)
        elif wantstate == self.STATE_PLAYING:
            print('trying to switch to playing- state:', self.STATE_PLAYING)
        service = self.session.nav.getCurrentService()
        if service is None:
            print('No Service found')
            return False
        else:
            pauseable = service.pause()
            if pauseable is None:
                print('not pauseable.')
                self.state = self.STATE_PLAYING
            if pauseable is not None:
                print('service is pausable')
                if wantstate == self.STATE_PAUSED:
                    print('WANT TO PAUSE')
                    pauseable.pause()
                    self.state = self.STATE_PAUSED
                    if not self.shown:
                        self.hidetimer.stop()
                        self.show()
                elif wantstate == self.STATE_PLAYING:
                    print('WANT TO PLAY')
                    pauseable.unpause()
                    self.state = self.STATE_PLAYING
                    if self.shown:
                        self.__setHideTimer()
            for c in self.onPlayStateChanged:
                c(self.state)

            return True
            return

    def handleLeave(self):
        self.close()

    def leavePlayer(self):
        self.close()


class ALAJREStream4(Screen, InfoBarNotifications):
    STATE_IDLE = 0
    STATE_PLAYING = 1
    STATE_PAUSED = 2
    ENABLE_RESUME_SUPPORT = True
    ALLOW_SUSPEND = True
    PLAYER_STOPS =3
    skinfhd = '''<screen name="ALAJREStream4" flags="wfNoBorder" position="0,0" size="1920,1080" title="ALAJREStream" backgroundColor="transparent">
<widget source="session.CurrentService" render="Label" position="0,0" size="1920,1080" font="Regular; 22" backgroundColor="#263c59" shadowColor="#1d354c" shadowOffset="-100,-100" transparent="1" zPosition="1" halign="center">
<convert type="ServiceName">Name</convert>
</widget>
<widget source="global.CurrentTime" render="Label" position="266,222" size="250,100" font="bpmo; 32" halign="left" backgroundColor="black" transparent="1">
<convert type="ClockToText">Format:%H:%M:%S</convert>
</widget>
<ePixmap position="0,0" size="1920,1080" pixmap="/usr/lib/enigma2/python/Plugins/Extensions/FreeServer/Cimages/Freeservers_4.png" zPosition="-1" transparent="1" alphatest="blend" />
<ePixmap position="0,0" size="1920,1080" pixmap="/usr/lib/enigma2/python/Plugins/Extensions/FreeServer/Deco/button_red.png" zPosition="-1" transparent="1" alphatest="blend" />
<eLabel text="Exit" zPosition="1" position="40,0" size="160,35" font="Regular; 20" transparent="1" backgroundColor="black" halign="left" valign="left" />
</screen>'''
    skinhd = '''<screen name="LiveSoccerStream" flags="wfNoBorder" position="0,0" size="1280,720" title="LiveSoccerStream" backgroundColor="transparent">
<widget source="session.CurrentService" render="Label" position="0,0" size="1280,720" font="Regular; 22" backgroundColor="#263c59" shadowColor="#1d354c" shadowOffset="-100,-100" transparent="1" zPosition="1" halign="center">
<convert type="ServiceName">Name</convert>
</widget>
<widget source="global.CurrentTime" render="Label" position="266,22" size="150,100" font="bpmo; 32" halign="left" backgroundColor="black" transparent="1">
<convert type="ClockToText">Format:%H:%M:%S</convert>
</widget>
<ePixmap position="0,0" size="1280,720" pixmap="/usr/lib/enigma2/python/Plugins/Extensions/FreeServer/Cimages/Freeservers_4.png" zPosition="-1" transparent="1" alphatest="blend" />
<ePixmap position="0,0" size="1920,1080" pixmap="/usr/lib/enigma2/python/Plugins/Extensions/FreeServer/Deco/button_red.png" zPosition="-1" transparent="1" alphatest="blend" />
<eLabel text="Exit" zPosition="1" position="40,0" size="100,25" font="Regular; 20" transparent="1" backgroundColor="black" halign="left" valign="left" />
</screen>'''

    def __init__(self, session, service):
        Screen.__init__(self, session)
        if dwidth == 1280:
            self.skin = ALAJREStream4.skinhd
        else:
            self.skin = ALAJREStream4.skinfhd
        InfoBarNotifications.__init__(self)
        self.session = session
        self.service = service
        self.screen_timeout = 1000
        self.__event_tracker = ServiceEventTracker(screen=self, eventmap={iPlayableService.evSeekableStatusChanged: self.__seekableStatusChanged,
         iPlayableService.evStart: self.__serviceStarted,
         iPlayableService.evEOF: self.__evEOF})
        self['ButtonRedtext'] = Label(_('Exit'))                
        self['text'] = Label()
        self['actions'] = ActionMap(['SetupActions', 'DirectionActions', 'ColorActions', 
        #self['actions'] = ActionMap(['OkCancelActions',
         'InfobarSeekActions',
         'ColorActions',
         'MediaPlayerActions',
         'MovieSelectionActions'], {'ok': self.leavePlayer,
         'cancel': self.leavePlayer,
         'exit': self.exit,         
         'stop': self.leavePlayer}, -2)
        self['pauseplay'] = Label(_('Play'))
        self.hidetimer = eTimer()
        self.repeter = True
        self.state = self.STATE_PLAYING
        self.onPlayStateChanged = []
        self.play()
        self.onClose.append(self.__onClose)

    def __onClose(self):
        self.session.nav.stopService()

    def __evEOF(self):
        self.STATE_PLAYING = True
        self.state = self.STATE_PLAYING
        self.session.nav.playService(self.service)
        if self.session.nav.stopService():
            self.state = self.STATE_PLAYING
            self.session.nav.playService(self.service)
        else:
            self.leavePlayer()

    def __setHideTimer(self):
        self.hidetimer.start(self.screen_timeout)

    def ok(self):
        self.leavePlayer()
        
    def exit(self):
        self.close()
        
    def playNextFile(self):
        self.session.open(MessageBox, 'only to watch not play Next and Prev File', MessageBox.TYPE_INFO)

    def playPrevFile(self):
        self.session.open(MessageBox, 'only to watch not play Next and Prev File', MessageBox.TYPE_INFO)

    def playService(self, newservice):
        if self.state == self.STATE_IDLE:
            self.play()
        self.service = newservice

    def play(self):
        self.state = self.STATE_PLAYING
        self['pauseplay'].setText('PLAY')
        self.session.nav.playService(self.service)
        self.__evEOF

    def __seekableStatusChanged(self):
        service = self.session.nav.getCurrentService()
        if service is not None:
            seek = service.seek()
            if seek is None or not seek.isCurrentlySeekable():
                self.setSeekState(self.STATE_PLAYING)
                self.__evEOF
        return

    def __serviceStarted(self):
        self.state = self.STATE_PLAYING
        self.__evEOF

    def setSeekState(self, wantstate):
        print('setSeekState')
        if wantstate == self.STATE_PAUSED:
            print('trying to switch to Pause- state:', self.STATE_PAUSED)
        elif wantstate == self.STATE_PLAYING:
            print('trying to switch to playing- state:', self.STATE_PLAYING)
        service = self.session.nav.getCurrentService()
        if service is None:
            print('No Service found')
            return False
        else:
            pauseable = service.pause()
            if pauseable is None:
                print('not pauseable.')
                self.state = self.STATE_PLAYING
            if pauseable is not None:
                print('service is pausable')
                if wantstate == self.STATE_PAUSED:
                    print('WANT TO PAUSE')
                    pauseable.pause()
                    self.state = self.STATE_PAUSED
                    if not self.shown:
                        self.hidetimer.stop()
                        self.show()
                elif wantstate == self.STATE_PLAYING:
                    print('WANT TO PLAY')
                    pauseable.unpause()
                    self.state = self.STATE_PLAYING
                    if self.shown:
                        self.__setHideTimer()
            for c in self.onPlayStateChanged:
                c(self.state)

            return True
            return

    def handleLeave(self):
        self.close()

    def leavePlayer(self):
        self.close()
                          
class ALAJREStream5(Screen, InfoBarNotifications):
    STATE_IDLE = 0
    STATE_PLAYING = 1
    STATE_PAUSED = 2
    ENABLE_RESUME_SUPPORT = True
    ALLOW_SUSPEND = True
    PLAYER_STOPS = 3                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              
    skinfhd = '<screen name="ALAJREStream5" flags="wfNoBorder" position="0,0" size="1920,1080" title="ALAJREStream" backgroundColor="transparent"><widget source="session.CurrentService" render="Label" position="396,1286" size="1920,1080" font="Regular; 66" backgroundColor="#263c59" shadowColor="#1d354c" shadowOffset="-100,-100" transparent="1" zPosition="1" halign="center"><convert type="ServiceName">Name</convert></widget><widget source="global.CurrentTime" render="Label" position="66,22" size="250,100" font="Regular; 22" halign="left" backgroundColor="black" transparent="1"><convert type="ClockToText">Format:%H:%M:%S</convert></widget><ePixmap position="0,0" size="1920,1080" font="Regular; 78" pixmap="/usr/lib/enigma2/python/Plugins/Extensions/FreeServer/Cimages/Freeservers_FHD.jpg" zPosition="-1" transparent="1" alphatest="blend" /></screen>'
    skinhd = '<screen name="LiveSoccerStream" flags="wfNoBorder" position="0,0" size="1280,720" title="LiveSoccerStream" backgroundColor="transparent"><widget source="session.CurrentService" render="Label" position="-20,1286" size="1280,720" font="Regular; 80" backgroundColor="#263c59" shadowColor="#1d354c" shadowOffset="-100,-100" transparent="1" zPosition="1" halign="center"><convert type="ServiceName">Name</convert></widget><widget source="global.CurrentTime" render="Label" position="66,22" size="150,100" font="Regular; 22" halign="left" backgroundColor="black" transparent="1"><convert type="ClockToText">Format:%H:%M:%S</convert></widget><ePixmap position="66,22" size="1366,1024" font="Regular; 78 " pixmap="/usr/lib/enigma2/python/Plugins/Extensions/FreeServer/Cimages/Freeservers_6.jpg" zPosition="-1" transparent="1" alphatest="blend" /></screen>'
    #skinfhd = '<screen name="ALAJREStream" flags="wfNoBorder" position="0,0" size="1920,1080" title="ALAJREStream" backgroundColor="transparent"><widget source="session.CurrentService" render="Label" position="396,1286" size="1920,1080" font="Regular; 66" backgroundColor="#263c59" shadowColor="#1d354c" shadowOffset="-1,-1" transparent="1" zPosition="1" halign="center"><convert type="ServiceName">Name</convert></widget><widget source="global.CurrentTime" render="Label" position="20,32" size="250,100" font="Regular; 32" halign="left" backgroundColor="black" transparent="1"><convert type="ClockToText">Format:%H:%M:%S</convert></widget><ePixmap position="0,300" size="640,960" font="Regular; 78" pixmap="/usr/lib/enigma2/python/Plugins/Extensions/FreeServer/Cimages/Freeservers_2.jpg" zPosition="-1" transparent="1" alphatest="blend" /></screen>'
    #skinhd = '<screen name="LiveSoccerStream" flags="wfNoBorder" position="0,0" size="1280,720" title="LiveSoccerStream" backgroundColor="transparent"><widget source="session.CurrentService" render="Label" position="-20,1286" size="1980,1920" font="Regular; 80" backgroundColor="#263c59" shadowColor="#1d354c" shadowOffset="-1,-1" transparent="1" zPosition="1" halign="center"><convert type="ServiceName">Name</convert></widget><widget source="global.CurrentTime" render="Label" position="20,32" size="250,100" font="Regular; 32" halign="left" backgroundColor="black" transparent="1"><convert type="ClockToText">Format:%H:%M:%S</convert></widget><ePixmap position="300,0" size="640,960" font="Regular; 78" pixmap="/usr/lib/enigma2/python/Plugins/Extensions/FreeServer/Cimages/Freeservers_2.jpg" zPosition="-1" transparent="1" alphatest="blend" /></screen>'


    def __init__(self, session, service):
        Screen.__init__(self, session)
        if dwidth == 1280:
            self.skin = ALAJREStream5.skinhd
        else:
            self.skin = ALAJREStream5.skinfhd
        InfoBarNotifications.__init__(self)
        self.session = session
        self.service = service
        self.screen_timeout = 1000
        self.__event_tracker = ServiceEventTracker(screen=self, eventmap={iPlayableService.evSeekableStatusChanged: self.__seekableStatusChanged,
         iPlayableService.evStart: self.__serviceStarted,
         iPlayableService.evEOF: self.__evEOF})
        self['actions'] = ActionMap(['OkCancelActions',
         'InfobarSeekActions',
         'ColorActions',
         'MediaPlayerActions',
         'MovieSelectionActions'], {'ok': self.leavePlayer,
         'cancel': self.leavePlayer,
         'stop': self.leavePlayer}, -2)
        self['pauseplay'] = Label(_('Play'))
        self.hidetimer = eTimer()
        self.repeter = True
        self.state = self.STATE_PLAYING
        self.onPlayStateChanged = []
        self.play()
        self.onClose.append(self.__onClose)

    def __onClose(self):
        self.session.nav.stopService()

    def __evEOF(self):
        self.STATE_PLAYING = True
        self.state = self.STATE_PLAYING
        self.session.nav.playService(self.service)
        if self.session.nav.stopService():
            self.state = self.STATE_PLAYING
            self.session.nav.playService(self.service)
        else:
            self.leavePlayer()

    def __setHideTimer(self):
        self.hidetimer.start(self.screen_timeout)

    def ok(self):
        self.leavePlayer()

    def playNextFile(self):
        self.session.open(MessageBox, 'only to watch not play Next and Prev File', MessageBox.TYPE_INFO)

    def playPrevFile(self):
        self.session.open(MessageBox, 'only to watch not play Next and Prev File', MessageBox.TYPE_INFO)

    def playService(self, newservice):
        if self.state == self.STATE_IDLE:
            self.play()
        self.service = newservice

    def play(self):
        self.state = self.STATE_PLAYING
        self['pauseplay'].setText('PLAY')
        self.session.nav.playService(self.service)
        self.__evEOF

    def __seekableStatusChanged(self):
        service = self.session.nav.getCurrentService()
        if service is not None:
            seek = service.seek()
            if seek is None or not seek.isCurrentlySeekable():
                self.setSeekState(self.STATE_PLAYING)
                self.__evEOF
        return

    def __serviceStarted(self):
        self.state = self.STATE_PLAYING
        self.__evEOF

    def setSeekState(self, wantstate):
        print('setSeekState')
        if wantstate == self.STATE_PAUSED:
            print('trying to switch to Pause- state:', self.STATE_PAUSED)
        elif wantstate == self.STATE_PLAYING:
            print('trying to switch to playing- state:', self.STATE_PLAYING)
        service = self.session.nav.getCurrentService()
        if service is None:
            print('No Service found')
            return False
        else:
            pauseable = service.pause()
            if pauseable is None:
                print('not pauseable.')
                self.state = self.STATE_PLAYING
            if pauseable is not None:
                print('service is pausable')
                if wantstate == self.STATE_PAUSED:
                    print('WANT TO PAUSE')
                    pauseable.pause()
                    self.state = self.STATE_PAUSED
                    if not self.shown:
                        self.hidetimer.stop()
                        self.show()
                elif wantstate == self.STATE_PLAYING:
                    print('WANT TO PLAY')
                    pauseable.unpause()
                    self.state = self.STATE_PLAYING
                    if self.shown:
                        self.__setHideTimer()
            for c in self.onPlayStateChanged:
                c(self.state)

            return True
            return

    def handleLeave(self):
        self.close()

    def leavePlayer(self):
        self.close()
        
class ALAJREStream6(InfoBarNotifications):
    STATE_IDLE = 0
    STATE_PLAYING = 1
    STATE_PAUSED = 2
    ENABLE_RESUME_SUPPORT = True
    ALLOW_SUSPEND = True
    PLAYER_STOPS = 3                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              
    #skinfhd = '<screen name="ALAJREStream5" flags="wfNoBorder" position="0,0" size="1920,1080" title="ALAJREStream" backgroundColor="transparent"><widget source="session.CurrentService" render="Label" position="396,1286" size="1920,1080" font="Regular; 66" backgroundColor="#263c59" shadowColor="#1d354c" shadowOffset="-100,-100" transparent="1" zPosition="1" halign="center"><convert type="ServiceName">Name</convert></widget><widget source="global.CurrentTime" render="Label" position="66,22" size="250,100" font="Regular; 22" halign="left" backgroundColor="black" transparent="1"><convert type="ClockToText">Format:%H:%M:%S</convert></widget><ePixmap position="0,0" size="1920,1080" font="Regular; 78" pixmap="/usr/lib/enigma2/python/Plugins/Extensions/FreeServer/Cimages/Freeservers_FHD.jpg" zPosition="-1" transparent="1" alphatest="blend" /></screen>'
    #skinhd = '<screen name="LiveSoccerStream" flags="wfNoBorder" position="0,0" size="1280,720" title="LiveSoccerStream" backgroundColor="transparent"><widget source="session.CurrentService" render="Label" position="-20,1286" size="1280,720" font="Regular; 80" backgroundColor="#263c59" shadowColor="#1d354c" shadowOffset="-100,-100" transparent="1" zPosition="1" halign="center"><convert type="ServiceName">Name</convert></widget><widget source="global.CurrentTime" render="Label" position="66,22" size="150,100" font="Regular; 22" halign="left" backgroundColor="black" transparent="1"><convert type="ClockToText">Format:%H:%M:%S</convert></widget><ePixmap position="66,22" size="1366,1024" font="Regular; 78 " pixmap="/usr/lib/enigma2/python/Plugins/Extensions/FreeServer/Cimages/Freeservers_6.jpg" zPosition="-1" transparent="1" alphatest="blend" /></screen>'
    #skinfhd = '<screen name="ALAJREStream" flags="wfNoBorder" position="0,0" size="1920,1080" title="ALAJREStream" backgroundColor="transparent"><widget source="session.CurrentService" render="Label" position="396,1286" size="1920,1080" font="Regular; 66" backgroundColor="#263c59" shadowColor="#1d354c" shadowOffset="-1,-1" transparent="1" zPosition="1" halign="center"><convert type="ServiceName">Name</convert></widget><widget source="global.CurrentTime" render="Label" position="20,32" size="250,100" font="Regular; 32" halign="left" backgroundColor="black" transparent="1"><convert type="ClockToText">Format:%H:%M:%S</convert></widget><ePixmap position="0,300" size="640,960" font="Regular; 78" pixmap="/usr/lib/enigma2/python/Plugins/Extensions/FreeServer/Cimages/Freeservers_2.jpg" zPosition="-1" transparent="1" alphatest="blend" /></screen>'
    #skinhd = '<screen name="LiveSoccerStream" flags="wfNoBorder" position="0,0" size="1280,720" title="LiveSoccerStream" backgroundColor="transparent"><widget source="session.CurrentService" render="Label" position="-20,1286" size="1980,1920" font="Regular; 80" backgroundColor="#263c59" shadowColor="#1d354c" shadowOffset="-1,-1" transparent="1" zPosition="1" halign="center"><convert type="ServiceName">Name</convert></widget><widget source="global.CurrentTime" render="Label" position="20,32" size="250,100" font="Regular; 32" halign="left" backgroundColor="black" transparent="1"><convert type="ClockToText">Format:%H:%M:%S</convert></widget><ePixmap position="300,0" size="640,960" font="Regular; 78" pixmap="/usr/lib/enigma2/python/Plugins/Extensions/FreeServer/Cimages/Freeservers_2.jpg" zPosition="-1" transparent="1" alphatest="blend" /></screen>'
    def __init__(self, session, service, msg=None):
        InfoBarNotifications.__init__(self)
        self.session = session
        self.service = service
        self.screen_timeout = 1000
        self.__event_tracker = ServiceEventTracker(eventmap={iPlayableService.evSeekableStatusChanged: self.__seekableStatusChanged,
         iPlayableService.evStart: self.__serviceStarted,
         iPlayableService.evEOF: self.__evEOF})
        self['actions'] = ActionMap(['OkCancelActions',
         'InfobarSeekActions',
         'ColorActions',
         'MediaPlayerActions',
         'MovieSelectionActions'], {'ok': self.leavePlayer,
         'cancel': self.leavePlayer,
         'stop': self.leavePlayer}, -2)
        self['pauseplay'] = Label(_('Play'))
        self.hidetimer = eTimer()
        self.repeter = True
        self.state = self.STATE_PLAYING
        self.onPlayStateChanged = []
        self.play()
        self.onClose.append(self.__onClose)

    def __onClose(self):
        self.session.nav.stopService()

    def __evEOF(self):
        self.STATE_PLAYING = True
        self.state = self.STATE_PLAYING
        self.session.nav.playService(self.service)
        if self.session.nav.stopService():
            self.state = self.STATE_PLAYING
            self.session.nav.playService(self.service)
        else:
            self.leavePlayer()

    def __setHideTimer(self):
        self.hidetimer.start(self.screen_timeout)

    def ok(self):
        self.leavePlayer()

    def playNextFile(self):
        self.session.open(MessageBox, 'only to watch not play Next and Prev File', MessageBox.TYPE_INFO)

    def playPrevFile(self):
        self.session.open(MessageBox, 'only to watch not play Next and Prev File', MessageBox.TYPE_INFO)

    def playService(self, newservice):
        if self.state == self.STATE_IDLE:
            self.play()
        self.service = newservice

    def play(self):
        self.state = self.STATE_PLAYING
        self['pauseplay'].setText('PLAY')
        self.session.nav.playService(self.service)
        self.__evEOF

    def __seekableStatusChanged(self):
        service = self.session.nav.getCurrentService()
        if service is not None:
            seek = service.seek()
            if seek is None or not seek.isCurrentlySeekable():
                self.setSeekState(self.STATE_PLAYING)
                self.__evEOF
        return

    def __serviceStarted(self):
        self.state = self.STATE_PLAYING
        self.__evEOF
        
    def disappear(self):
        self.close()
        
    def setSeekState(self, wantstate):
        print('setSeekState')
        if wantstate == self.STATE_PAUSED:
            print('trying to switch to Pause- state:', self.STATE_PAUSED)
        elif wantstate == self.STATE_PLAYING:
            print('trying to switch to playing- state:', self.STATE_PLAYING)
        service = self.session.nav.getCurrentService()
        if service is None:
            print('No Service found')
            return False
        else:
            pauseable = service.pause()
            if pauseable is None:
                print('not pauseable.')
                self.state = self.STATE_PLAYING
            if pauseable is not None:
                print('service is pausable')
                if wantstate == self.STATE_PAUSED:
                    print('WANT TO PAUSE')
                    pauseable.pause()
                    self.state = self.STATE_PAUSED
                    if not self.shown:
                        self.hidetimer.stop()
                        self.show()
                elif wantstate == self.STATE_PLAYING:
                    print('WANT TO PLAY')
                    pauseable.unpause()
                    self.state = self.STATE_PLAYING
                    if self.shown:
                        self.__setHideTimer()
            for c in self.onPlayStateChanged:
                c(self.state)

            return True
            return

    def handleLeave(self):
        self.close()

    def leavePlayer(self):
        self.close()
        
