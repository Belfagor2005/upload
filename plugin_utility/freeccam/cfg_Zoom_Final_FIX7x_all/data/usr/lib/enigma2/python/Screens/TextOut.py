from Screens.Screen import Screen
from enigma import getDesktop
from Components.ActionMap import ActionMap
from Components.Sources.StaticText import StaticText
from Components.ScrollLabel import ScrollLabel


class TextOut(Screen):

    global HD_Res
    try:
        sz_w = getDesktop(0).size().width()
    except:
        sz_w = 720
    if sz_w == 1280:
        HD_Res = True
    else:
        HD_Res = False

    if HD_Res:

        skin = """
    <screen name="TextOut" position="100,70" size="1080,600" title="TextOut...">
        <widget name="text" position="10,10" size="780,580" font="Regular;20" />
        <!--widget source="text" render="Label" position="0,0" size="540,390" font="Regular;20" /-->
    </screen>"""

    else:
        skin = """
    <screen name="TextOut" position="50,60" size="620,480" title="TextOut...">
        <widget name="text" position="5,5" size="610,450" font="Regular;18" />
        <!--widget source="text" render="Label" position="0,0" size="540,390" font="Regular;18" /-->
    </screen>"""

    def __init__(self, session, text="", title=""):
        Screen.__init__(self, session)
        self.text = text
        self.newtitle = title
        self["text"] = ScrollLabel(self.text)
        self["actions"] = ActionMap(["OkCancelActions", "DirectionActions"],
                {
                    "cancel": self.cancel,
                    "ok": self.ok,
                    "up": self["text"].pageUp,
                    "down": self["text"].pageDown,
                }, -1)

        self["title"] = StaticText()
        self.onShown.append(self.updateTitle)

    def updateTitle(self):
        self.setTitle(self.newtitle)
        self["title"].setText(self.newtitle)

    def ok(self):
        self.close()

    def cancel(self):
        self.close()
