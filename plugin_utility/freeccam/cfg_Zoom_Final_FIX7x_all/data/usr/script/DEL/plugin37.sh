#!/bin/sh
echo "Uninstall"
sleep 1
echo "odinstalace pluginu najdi MultiStalker"
opkg remove MultiStalker
rm -rf /usr/lib/enigma2/python/Plugins/Extensions/MultiStalker/
rm -rf /home/stalker.conf

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

