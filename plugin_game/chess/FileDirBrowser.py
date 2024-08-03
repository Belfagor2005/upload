# -*- coding: utf-8 -*-

from Screens.Screen import Screen
from Components.ActionMap import ActionMap
from Components.Label import Label
from Components.FileList import FileList
from Components.Sources.StaticText import StaticText

class FileDirBrowser(Screen):
	skin = """<screen name="FileDirBrowser" position="center,center" size="520,430" title="File Browser" >
			<ePixmap pixmap="skin_default/buttons/red.png" position="0,0" size="140,40" alphatest="on" />
			<ePixmap pixmap="skin_default/buttons/green.png" position="140,0" size="140,40" alphatest="on" />
			<widget source="key_red" render="Label" position="0,0" zPosition="1" size="140,40" font="Regular;20" halign="center" valign="center" backgroundColor="#9f1313" transparent="1" />
			<widget source="key_green" render="Label" position="140,0" zPosition="1" size="140,40" font="Regular;20" halign="center" valign="center" backgroundColor="#1f771f" transparent="1" />
			<widget name="current_selection" position="5,50" size="510,50" font="Regular;20" />
			<widget name="filelist" position="5,110" size="510,270" scrollbarMode="showOnDemand" />
		</screen>"""
	
	def __init__(self, session, title = "FileBrowser", initDir = '/', getDir = True, getFile = False, inhibitMounts = False, inhibitDirs = False, showMountpoints = False, showDirectories = True, showFiles = True):
		Screen.__init__(self, session)
		self["filelist"] = FileList(initDir, inhibitMounts = inhibitMounts, inhibitDirs = inhibitDirs, showMountpoints = showMountpoints, showDirectories = showDirectories, showFiles = showFiles)
		self["actions"] = ActionMap(["SetupActions", "DirectionActions", "ColorActions"],
		{
			"ok": self.ok,
			"cancel": self.cancel,
			"left": self.left,
			"right": self.right,
			"up": self.up,
			"down": self.down,
			"green": self.green,
			"red": self.cancel
		}, -1)
		self.title=_(title)
		try:
			self["title"]=StaticText(self.title)
		except:
			print('self["title"] was not found in skin')
		self["key_red"] = StaticText(_("Cancel"))
		self["key_green"] = StaticText(_("OK"))
		self["current_selection"] = Label()
		self.getDir = getDir
		self.getFile = getFile

	def cancel(self):
		self.close(None)

	def green(self):
		sel = self["filelist"].getSelection()[0]
		if self["filelist"].getSelection()[1] and self.getDir:
			if (sel.endswith("/")):
				sel = sel[:-1]
			self.close(sel)
		elif not self["filelist"].getSelection()[1] and self.getFile:
			directory = self["filelist"].getCurrentDirectory()
			if (directory.endswith("/")):
				sel = self["filelist"].getCurrentDirectory() + self["filelist"].getFilename()
			else:
				sel = self["filelist"].getCurrentDirectory() + "/" + self["filelist"].getFilename()
			self.close(sel)
		else:
			self["current_selection"].setText(_("Invalid Choice"))

	def up(self):
		self["filelist"].up()
		self.updateFile()

	def down(self):
		self["filelist"].down()
		self.updateFile()

	def left(self):
		self["filelist"].pageUp()
		self.updateFile()

	def right(self):
		self["filelist"].pageDown()
		self.updateFile()

	def ok(self):
		if self["filelist"].canDescent():
			self["filelist"].descent()
			self.updateFile()
		else:
			self.green()

	def updateFile(self):
		currSelection = self["filelist"].getSelection()[0]
		if self["filelist"].getSelection()[1] and self.getDir:
			self["current_selection"].setText(currSelection)
		elif not self["filelist"].getSelection()[1] and self.getFile:
			directory = self["filelist"].getCurrentDirectory()
			if (directory.endswith("/")):
				currSelection = self["filelist"].getCurrentDirectory() + self["filelist"].getFilename()
			else:
				currSelection = self["filelist"].getCurrentDirectory() + "/" + self["filelist"].getFilename()
			self["current_selection"].setText(currSelection)
		else:
			self["current_selection"].setText(_("Invalid Choice"))
