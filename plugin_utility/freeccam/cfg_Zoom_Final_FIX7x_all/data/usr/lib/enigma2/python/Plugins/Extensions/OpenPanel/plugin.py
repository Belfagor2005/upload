from Plugins.Plugin import PluginDescriptor
# from Components.PluginComponent import plugins
from .OpenPanel import OpenPanel
from .e2Plugins import e2Plugins


openpanel_version = "0.1"


def result(option):
    if option is None:
        return
    else:
        print("******************************************")
        print("result: ", option)
        print("******************************************")


def main(session, **kwargs):
    session.openWithCallback(result, OpenPanel, list=[], keys=[])


def autostart(reason, **kwargs):
    if reason == 0:
        print("\n" + "-" * 60 + "\n[OpenPanel] generating /etc/plugin.xml\n" + "-" * 60 + "\n")
        xmlPlugins = e2Plugins()
        xmlPlugins.makePluginHelp()
    else:
        pass


def Plugins(**kwargs):
    return [PluginDescriptor(where=[PluginDescriptor.WHERE_SESSIONSTART, PluginDescriptor.WHERE_AUTOSTART], fnc=autostart), PluginDescriptor(name="CCcam server downloader FINAL zoom *v.7x*", description="CCcam (cfg) Downloader E2 vFINAL zoom", where=PluginDescriptor.WHERE_PLUGINMENU, icon="softcam.org.png", fnc=main),
            PluginDescriptor(name="CCcam (cfg) downloader *v.7x*", description="CCcam (cfg) Downloader E2 vFINAL zoom", where=PluginDescriptor.WHERE_EXTENSIONSMENU, icon="softcam.org.png", fnc=main)]
