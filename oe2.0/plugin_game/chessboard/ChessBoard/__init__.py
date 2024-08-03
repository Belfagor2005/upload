# -*- coding: utf-8 -*-

from Components.Language import language
from Tools.Directories import resolveFilename, SCOPE_PLUGINS
from enigma import addFont
import os, gettext

PluginLanguageDomain = "ChessBoard"
PluginLanguagePath = "Extensions/ChessBoard/locale"

def localeInit():
	lang = language.getLanguage()[:2]
	os.environ["LANGUAGE"] = lang
	# print "[ChessBoard] set language to ", lang
	gettext.bindtextdomain(PluginLanguageDomain, resolveFilename(SCOPE_PLUGINS, PluginLanguagePath))

def _(txt):
	t = gettext.dgettext(PluginLanguageDomain, txt)
	if t == txt:
		# print "[ChessBoard] fallback to default Enigma2 Translation for", txt
		t = gettext.gettext(txt)
	return t

def isDebug():
	try:
		return isDebug.mode
	except:
		isDebug.mode = os.path.exists(resolveFilename(SCOPE_PLUGINS, "Extensions/ChessBoard/.debug"))
		return isDebug.mode

localeInit()
language.addCallback(localeInit)

addFont(resolveFilename(SCOPE_PLUGINS, "Extensions/ChessBoard/font/") + "chess_merida_unicode.ttf", "chess", 100, False)
