#!/bin/sh
echo "Uninstall"
sleep 1
echo "odinstalace pluginu mediaportal"
opkg remove enigma2-plugin-extensions-mediaportal
rm -rf /usr/lib/enigma2/python/Plugins/Extensions/MediaPortal/
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

