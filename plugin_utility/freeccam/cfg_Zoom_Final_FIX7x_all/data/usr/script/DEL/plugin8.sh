#!/bin/sh
echo "Uninstall"
sleep 1
echo "odinstalace pluginu freeserver_7.0.2"
opkg remove enigma2-plugin-extensions-freeserver - 7.0.2
rm -rf /usr/lib/enigma2/python/Plugins/Extensions/FreeServer/
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

