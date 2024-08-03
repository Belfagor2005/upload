#!/bin/sh
echo "Uninstall"
sleep 1
echo "odinstalace pluginu TV panel"
opkg remove enigma2-plugin-extensions-tvpanel
rm -rf /usr/lib/enigma2/python/Plugins/Extensions/tvPanel/
echo ""
echo ""
echo ""
echo ""
echo ""
echo ""
echo ""
sleep 1
echo "OK"
exit
