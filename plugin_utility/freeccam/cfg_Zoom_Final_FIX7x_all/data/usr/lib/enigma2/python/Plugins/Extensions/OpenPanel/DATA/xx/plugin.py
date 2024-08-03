# -*- coding: utf-8 -*-

# This plugin based on StreamTV by kos
# This plugin is free software, you are allowed to
# modify it (if you keep the license),
# but you are not allowed to distribute/publish
# it without source code (this version and your modifications).
# This means you also have to distribute
# source code of your modifications.
# NaseDC

from Plugins.Plugin import PluginDescriptor
import os
import skin
from xml.etree.cElementTree import ElementTree
from enigma import gFont, eTimer, ePicLoad
from enigma import loadPNG, eServiceReference
from enigma import iPlayableService, eListboxPythonMultiContent
from enigma import RT_HALIGN_LEFT, RT_VALIGN_CENTER
from Screens.Screen import Screen
from Screens.ChoiceBox import ChoiceBox
# from Screens.MessageBox import MessageBox
from Screens.InfoBarGenerics import InfoBarNotifications
# from Components.Button import Button
from Components.Label import Label
# from Components.ConfigList import ConfigListScreen
# from Components.Sources.StaticText import StaticText
from Components.ActionMap import ActionMap
from Components.MenuList import MenuList
from Components.Pixmap import Pixmap
from Components.AVSwitch import AVSwitch
from Components.ServiceEventTracker import ServiceEventTracker
from Tools.Directories import resolveFilename, SCOPE_PLUGINS

pversion = "2.0"
pchange = "Plugin:\n\n - Genre Tierkamera entfernt\n\n\n stream.xml\n\n - URL´s angepasst / bereinigt"

PLUGIN_PATH = resolveFilename(SCOPE_PLUGINS, "Extensions/StreamTvPlayerFHD")


class StreamTvPlayerFHD(Screen, InfoBarNotifications):
    skin = """
        <screen name="StreamTvPlayerFHD" flags="wfNoBorder" position="0,0" size="1920,1080" title="XXX Films" backgroundColor="#95000000">
            <ePixmap position="340,941" size="120,100" pixmap="%s/pic/channel_background.png" backgroundColor="#000000" zPosition="1" alphatest="blend" transparent="1"/>
            <ePixmap position="1425,941" size="120,100" pixmap="/usr/lib/enigma2/python/Plugins/Extensions/StreamTvPlayerFHD/pic/channel_background.png" zPosition="1" alphatest="blend" transparent="1"/>
            <widget name="channel_icon" position="355,963" size="100,60" backgroundColor="#000000" zPosition="2" alphatest="blend" transparent="1"/>
            <widget name="channel_name" position="480,945" size="920,45" font="Regular;40" zPosition="1" halign="left" valign="center" noWrap="1" foregroundColor="#ffffff" backgroundColor="#40000000"/>
            <widget name="channel_genre" position="480,995" size="465,45" font="Regular;36" zPosition="1" halign="left" valign="center" foregroundColor="#848a84" backgroundColor="#40000000"/>
            <widget name="channel_uri" position="935,995" size="465,45" font="Regular;22" zPosition="1" halign="left" valign="center" noWrap="1" foregroundColor="#848a84" backgroundColor="#40000000"/>
            <widget source="session.CurrentService" render="Label" position="1430,975" size="110,40" font="Regular;30" halign="center" valign="center" zPosition="2" foregroundColor="#ffffff" backgroundColor="#40000000" transparent="1">
                <convert type="ServicePosition">Position</convert>
            </widget>
            <eLabel name="" position="465,944" size="960,98" backgroundColor="#40000000"/>
            <eLabel name="" position="340,945" size="120,100" backgroundColor="#40000000"/>
            <eLabel name="" position="1425,945" size="120,100" backgroundColor="#40000000"/>
            <eLabel name="" position="335,935" size="1215,5" backgroundColor="#535959" zPosition="1"/>
            <eLabel name="" position="335,1045" size="1215,5" backgroundColor="#535959" zPosition="1"/>
            <eLabel name="" position="335,940" size="5,105" backgroundColor="#535959" zPosition="1"/>
            <eLabel name="" position="1545,940" size="5,105" backgroundColor="#535959" zPosition="1"/>
            <eLabel name="" position="460,940" size="5,105" backgroundColor="#6a7070" zPosition="1"/>
            <eLabel name="" position="1420,940" size="5,105" backgroundColor="#6a7070" zPosition="1"/>
        </screen>
        """ % (PLUGIN_PATH)

    PLAYER_IDLE = 0
    PLAYER_PLAYING = 1
    PLAYER_PAUSED = 2

    def __init__(self, session, service, cbServiceCommand, chGenre, chDiscr, chName, chURL, chIcon):
        Screen.__init__(self, session)
        InfoBarNotifications.__init__(self)
        isEmpty = lambda x: x is None or len(x) == 0 or x == 'None'
        if isEmpty(chGenre): chGenre = 'Unknown'
        if isEmpty(chDiscr): chDiscr = 'Unknown'
        if isEmpty(chName): chName = 'Unknown'
        if isEmpty(chURL):  chURL = 'Unknown'
        if isEmpty(chIcon): chIcon = 'default.png'
        chIcon = '%s/icons/%s' % (PLUGIN_PATH, chIcon)
        self.session = session
        self.service = service
        self.cbServiceCommand = cbServiceCommand
        self["actions"] = ActionMap(["OkCancelActions", "InfobarSeekActions", "MediaPlayerActions", "MovieSelectionActions"], {
            "ok": self.doInfoAction,
            "cancel": self.doExit,
            "stop": self.doExit,
            "playpauseService": self.playpauseService,
        }, -2)

        font, size = skin.parameters.get("streamListFont", ('Regular', 22))

        self.__event_tracker = ServiceEventTracker(screen = self, eventmap = {
            iPlayableService.evSeekableStatusChanged: self.__seekableStatusChanged,
            iPlayableService.evStart: self.__serviceStarted,
            iPlayableService.evEOF: self.__evEOF,
        })

        self.hidetimer = eTimer()
        self.hidetimer.timeout.get().append(self.doInfoAction)

        self.state = self.PLAYER_PLAYING
        self.lastseekstate = self.PLAYER_PLAYING
        self.__seekableStatusChanged()
        self.onClose.append(self.__onClose)
        self.doPlay()
        self['channel_icon'] = Pixmap()
        self['channel_genre'] = Label(chGenre)
        self['channel_discr'] = Label(chDiscr)
        self['channel_name'] = Label(chName)
        self['channel_uri'] = Label(chURL)
        self.picload = ePicLoad()
        self.scale = AVSwitch().getFramebufferScale()
        self.picload.PictureData.get().append(self.cbDrawChannelIcon)
        print self.scale[0]
        print self.scale[1]
        self.picload.setPara((90, 54, self.scale[0], self.scale[1], False, 0, "#40000000"))
        self.picload.startDecode(chIcon)
        self.bypassExit = False
        self.cbServiceCommand(('docommand', self.doCommand))

    def doCommand(self, cmd):
        if cmd == 'bypass_exit':
            self.bypassExit = True

    def cbDrawChannelIcon(self, picInfo=None):
        ptr = self.picload.getData()
        if ptr is not None:
            self["channel_icon"].instance.setPixmap(ptr.__deref__())
            self["channel_icon"].show()

    def __onClose(self):
        self.session.nav.stopService()

    def __seekableStatusChanged(self):
        service = self.session.nav.getCurrentService()
        if service is not None:
            seek = service.seek()
            if seek is None or not seek.isCurrentlySeekable():
                self.setSeekState(self.PLAYER_PLAYING)

    def __serviceStarted(self):
        self.state = self.PLAYER_PLAYING
        self.__seekableStatusChanged()

    def __evEOF(self):
        if self.bypassExit:
            return
        self.doExit()

    def __setHideTimer(self):
        self.hidetimer.start(3500)

    def doExit(self):
        list = ((_("Yes"), "y"), (_("No"), "n"),)
        self.session.openWithCallback(self.cbDoExit, ChoiceBox, title=_("Stop playing this stream?"), list=list)

    def cbDoExit(self, answer):
        answer = answer and answer[1]
        if answer == "y":
            self.cbServiceCommand()
            self.close()

    def setSeekState(self, wantstate):
        service = self.session.nav.getCurrentService()
        if service is None:
            print "No Service found"
            return

        pauseable = service.pause()
        if pauseable is not None:
            if wantstate == self.PLAYER_PAUSED:
                pauseable.pause()
                self.state = self.PLAYER_PAUSED
                if not self.shown:
                    self.hidetimer.stop()
                    self.show()
            elif wantstate == self.PLAYER_PLAYING:
                pauseable.unpause()
                self.state = self.PLAYER_PLAYING
                if self.shown:
                    self.__setHideTimer()
        else:
            self.state = self.PLAYER_PLAYING

    def doInfoAction(self):
        if self.shown:
            self.hidetimer.stop()
            self.hide()
        else:
            self.show()
            if self.state == self.PLAYER_PLAYING:
                self.__setHideTimer()

    def doPlay(self):
        if self.state == self.PLAYER_PAUSED:
            if self.shown:
                self.__setHideTimer()
        self.state = self.PLAYER_PLAYING
        self.session.nav.playService(self.service)
        if self.shown:
            self.__setHideTimer()

    def playpauseService(self):
        if self.state == self.PLAYER_PLAYING:
            self.setSeekState(self.PLAYER_PAUSED)
        elif self.state == self.PLAYER_PAUSED:
            self.setSeekState(self.PLAYER_PLAYING)


def parseStreamDB(filename):
    tvlist = []
    genre_list = []
    tree = ElementTree()
    tree.parse(filename)

    for iptv in tree.findall('iptv'):
        g = str(iptv.findtext('genre'))
        d = str(iptv.findtext('discr'))
        n = str(iptv.findtext('name'))
        i = str(iptv.findtext('icon'))
        u = str(iptv.findtext('uri'))
        t = str(iptv.findtext('type'))
        if g and (g, "genre") not in genre_list:
            genre_list.append((g, "genre"))
        tvlist.append({'genre': g, 'discr': d, 'name': n, 'icon': i, 'type': t, 'uri': u})
    return (tvlist, genre_list)


def streamListEntry(entry):
    x, y, w, h = skin.parameters.get("streamListEntry", (160, 1, 940, 34))
    x1, y1, w1, h1 = skin.parameters.get("streamListEntry1", (160, 42, 940, 26))
    return [entry,
        (eListboxPythonMultiContent.TYPE_PIXMAP_ALPHATEST, 20, 5, 100, 60, loadPNG('%s/icons/%s' % (PLUGIN_PATH, str(entry[1].get('icon'))))),
        (eListboxPythonMultiContent.TYPE_TEXT, x, y, w, h, 1, RT_HALIGN_LEFT | RT_VALIGN_CENTER, str(entry[0])),  # Streamname
        (eListboxPythonMultiContent.TYPE_TEXT, x1, y1, w1, h1, 2, RT_HALIGN_LEFT | RT_VALIGN_CENTER, str(entry[1].get('discr')))  # Beschreibungstext
    ]


def genreListEntry(entry):
    x, y, w, h = skin.parameters.get("genreListEntry", (30, 7, 1095, 54))
    return [entry, (eListboxPythonMultiContent.TYPE_TEXT, x, y, w, h, 0, RT_HALIGN_LEFT | RT_VALIGN_CENTER, entry[0])]


class StreamTvListFHD(Screen):
    skin = """
        <screen name="StreamTvListFHD" position="center,center" size="1920,1080" title="StreamTvPlayer FHD" backgroundColor="#30000000">
            <widget source="Title" render="Label" position="20,25" size="450,60" font="Regular;42" halign="left" valign="center" backgroundColor="black" zPosition="3" transparent="1" />
            <widget name="streamlist" position="20,100" size="1125,840" backgroundColor="black" zPosition="10" scrollbarMode="showOnDemand" scrollbarWidth="10" scrollbarSliderBorderColor="#535959" foregroundColorSelected="#ffffff" backgroundColorSelected="#0342424b" enableWrapAround="1" transparent="1" />
            <widget name="infolabel" position="20,948" size="100,60" font="Regular;28" halign="center" valign="center" backgroundColor="#30000000" />
            <widget name="infomation" position="119,950" size="1750,60" font="Regular;28" halign="left" valign="center" noWrap="1" backgroundColor="#30000000" />
            <widget name="version" position="470,21" size="655,60" font="Regular;42" zPosition="2" halign="right" valign="center" foregroundColor="foreground" backgroundColor="#30000000" />
            <eLabel text="Nevhodné pro mladší (18let)" position="1250,280" size="620,60" font="Regular;44" zPosition="2" halign="center" valign="center" backgroundColor="#30000000" />
            <widget name="change" position="1250,340" size="620,560" font="Regular;30" zPosition="2" halign="center" foregroundColor="foreground" backgroundColor="#30000000" />
            <ePixmap position="1355,70" size="400,160" pixmap="/usr/lib/enigma2/python/Plugins/Extensions/StreamTvPlayerFHD/pic/image.png" alphatest="blend" zPosition="1" transparent="1" />
            <widget name="key_red" position="85,1015" size="240,62" font="Regular;30" halign="left" valign="center" zPosition="2" transparent="1" />
            <widget name="key_green" position="385,1015" size="240,62" font="Regular;30" halign="left" valign="center" zPosition="2" transparent="1" />
            <widget name="key_yellow" position="685,1015" size="240,62" font="Regular;30" halign="left" valign="center" zPosition="2" transparent="1" />
            <widget name="select" position="1380,1015" size="200,62" font="Regular;30" halign="left" valign="center" zPosition="2" transparent="1" />
            <widget name="leave" position="1700,1010" size="200,70" font="Regular;30" halign="left" valign="center" zPosition="2" noWrap="0" transparent="1" />
            <ePixmap pixmap="/usr/lib/enigma2/python/Plugins/Extensions/StreamTvPlayerFHD/pic/red.png" position="40,1031" size="30,30" zPosition="2" alphatest="on" />
            <ePixmap pixmap="/usr/lib/enigma2/python/Plugins/Extensions/StreamTvPlayerFHD/pic/green.png" position="340,1031" size="30,30" zPosition="2" alphatest="on" />
            <ePixmap pixmap="/usr/lib/enigma2/python/Plugins/Extensions/StreamTvPlayerFHD/pic/yellow.png" position="640,1031" size="30,30" zPosition="2" alphatest="on" />
            <ePixmap pixmap="/usr/lib/enigma2/python/Plugins/Extensions/StreamTvPlayerFHD/pic/blue.png" position="940,1031" size="30,30" zPosition="2" alphatest="on" />
            <ePixmap pixmap="/usr/lib/enigma2/python/Plugins/Extensions/StreamTvPlayerFHD/pic/ok.png" position="1280,1025" size="80,40" zPosition="3" alphatest="on" />
            <ePixmap pixmap="/usr/lib/enigma2/python/Plugins/Extensions/StreamTvPlayerFHD/pic/exit.png" position="1600,1025" size="80,40" zPosition="3" alphatest="on" />
            <eLabel name="" position="10,1009" size="1900,2" zPosition="3" backgroundColor="#ffffff" />
            <eLabel name="" position="10,940" size="1900,2" zPosition="3" backgroundColor="#ffffff" />
            <eLabel name="" position="1155,10" size="2,925" zPosition="3" backgroundColor="#ffffff" />
        </screen>
        """

    def __init__(self, session):
        self.session = session
        Screen.__init__(self, session)
        self["actions"] = ActionMap(["OkCancelActions", "ShortcutActions", "WizardActions", "ColorActions", "SetupActions", "NumberActions", "MenuActions"], {
            "ok": self.keyOK,
            "cancel": self.keyCancel,
            "up": self.keyUp,
            "down": self.keyDown,
            "left": self.keyLeft,
            "right": self.keyRight,
            "green": self.Green,
            "yellow": self.Yellow,
        }, -1)

        self['key_red'] = Label(_("Odejít"))
        self['key_green'] = Label(_("Hlavní nabídka"))
        self['key_yellow'] = Label(_("seznam všech"))
        self['select'] = Label(_("Zvolit"))
        self['leave'] = Label(_("Stop / Návrat"))
        self.streamFile = resolveFilename(SCOPE_PLUGINS, "Extensions/StreamTvPlayerFHD/stream.xml")
        self['version'] = Label(("Version") + " %s" % pversion)
        self['change'] = Label(pchange)
        self.streamList = []
        self.genre_list = []
        self.makeStreamList()

    def makeStreamList(self):
        self.streamList = []
        xml_read = parseStreamDB(self.streamFile)
        self.all_streamList = xml_read[0]
        self.genre_list = xml_read[1]
        self.genre_list.sort(key=lambda x: x[0][0])
        self.streamMenuList = MenuList([], enableWrapAround=True, content=eListboxPythonMultiContent)
        self.streamMenuList.l.setFont(0, gFont('Regular', 38))
        self.streamMenuList.l.setFont(1, gFont('Regular', 32))
        self.streamMenuList.l.setFont(2, gFont('Regular', 24))
        self.streamMenuList.l.setItemHeight(70)
        self['streamlist'] = self.streamMenuList
        # self.streamMenuList.setList(map(streamListEntry, self.all_streamList))
        self.streamMenuList.setList(map(genreListEntry, self.genre_list))
        self["infolabel"] = Label("URL:")
        self["infomation"] = Label(" ")
        self["Genre"] = Label(" ")
        self["Discr"] = Label(" ")
        self["Name"] = Label(" ")
        self.updateInfomation()
        self.onLayoutFinish.append(self.layoutFinished)
        self.beforeService = None
        self.currentService = None
        self.playerStoped = False
        self.serviceDoCommand = None
        self.keyLocked = False

    def layoutFinished(self):
        rc = os.popen('ps -ef | grep rtmpdump | grep -v grep').read()
        print "a process already running :", rc
        if rc is not None:
            if rc.strip() != '':
                os.system('killall -INT rtmpdump')

    def updateInfomation(self):
        infomation = ''
        try:
            streamInfo = self["streamlist"].getCurrent()[0][1]
            infomation = streamInfo.get('uri').split()[0]
        except:
            infomation = ' '
        self["infomation"].setText(infomation)

    def keyLeft(self):
        if self.keyLocked:
            return
        self['streamlist'].pageUp()
        self.updateInfomation()

    def keyRight(self):
        if self.keyLocked:
            return
        self['streamlist'].pageDown()
        self.updateInfomation()

    def keyUp(self):
        if self.keyLocked:
            return
        self['streamlist'].up()
        self.updateInfomation()

    def keyDown(self):
        if self.keyLocked:
            return
        self['streamlist'].down()
        self.updateInfomation()

    def keyCancel(self):
        self.close()

    def keyOK(self):
        if self["streamlist"].getCurrent()[0][1] == "genre":
            self.streamList = []
            for x in self.all_streamList:
                if x.get('genre') == self["streamlist"].getCurrent()[0][0]:
                    self.streamList.append((x.get('name'), x))
                    if x.get('discr') == self["streamlist"].getCurrent()[0][1]:
                        self.streamList.append((x.get('name'), x))
            self.streamMenuList.setList(map(streamListEntry, self.streamList))
        else:
            if self.keyLocked:
                return
            self.keyLocked = True
            self.beforeService = None
            self.currentService = None
            self.playerStoped = False
            self.serviceDoCommand = None
            streamInfo = self["streamlist"].getCurrent()[0][1]
            uri = streamInfo.get('uri')
            typeInfo = streamInfo.get('type').split(':')
            genre = streamInfo.get('genre')
            discr = streamInfo.get('discr')
            serviceType = typeInfo[1]
            bufferSize = typeInfo[2]
            self.doStreamAction(uri, serviceType, bufferSize)

    def Green(self):
        self.streamMenuList.setList(map(genreListEntry, self.genre_list))

    def Yellow(self):
        self["streamlist"].getCurrent()[0][0]
        self.streamList = []
        for x in self.all_streamList:
                self.streamList.append((x.get('name'), x))
        self.streamMenuList.setList(map(streamListEntry, self.streamList))

    def doStreamAction(self, uri=None, serviceType='4097', bufferSize=None):
        try:
            serviceType = int(serviceType)
        except:
            serviceType = 4097
        try:
            bufferSize = int(bufferSize)
        except:
            bufferSize = None

        streamInfo = self["streamlist"].getCurrent()[0][1]
        serviceRef = "%(TYPE)d:0:1:0:0:0:0:0:0:0:%(URI)s:%(NAME)s" % {
                        'TYPE': serviceType,
                        'URI': uri.replace(':', '%3a').replace('@', '&'),
                        'NAME': streamInfo.get('name')
                        }
        service = eServiceReference(serviceRef)
        if bufferSize is not None:
            service.setData(2, bufferSize*1024)
        self.beforeService = self.session.nav.getCurrentlyPlayingServiceReference()
        self.currentService = self.session.openWithCallback(self.cbFinishedStream,
                                    StreamTvPlayerFHD,
                                    service,
                                    cbServiceCommand=self.cbServiceCommand,
                                    chGenre=str(streamInfo.get('genre')),
                                    chDiscr=str(streamInfo.get('discr')),
                                    chName=str(streamInfo.get('name')),
                                    chURL=str(streamInfo.get('uri')),
                                    chIcon=str(streamInfo.get('icon'))
        )

    def cbServiceCommand(self, params=None):
        if params is None:
            self.playerStoped = True
            return
        if params[0] == 'docommand':
            self.serviceDoCommand = params[1]

    def cbFinishedStream(self):
        self.keyLocked = False
        self.session.nav.playService(self.beforeService)
        print 'player done!!'


def main(session, **kwargs):
    session.open(StreamTvListFHD)


def menu(menuid, **kwargs):
    if menuid == "mainmenu":
        return [(_("StreamTvListFHD"), main, "StreamTvListFHD", 40)]
    return []


def Plugins(**kwargs):
    return PluginDescriptor(name=_("XXX Films"), description="Watching Porn movies RTSP/RTMP protocol.", where=PluginDescriptor.WHERE_PLUGINMENU, icon="plugin.png", fnc=main)
