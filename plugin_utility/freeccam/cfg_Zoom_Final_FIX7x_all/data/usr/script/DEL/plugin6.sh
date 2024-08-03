#!/bin/sh
echo "Uninstall"
sleep 1
echo "odinstalace pluginu KodiLite 5.0"
opkg remove enigma2-plugin-extensions-kodilite - 5.0
rm -rf /usr/lib/enigma2/python/Plugins/Extensions/KodiLite/
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

