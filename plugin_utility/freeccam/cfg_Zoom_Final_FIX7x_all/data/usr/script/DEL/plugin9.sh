#!/bin/sh
echo "Uninstall"
sleep 1
echo "odinstalace pluginu archivCZSK"
sleep 1
echo "odinstalace pluginu subssupport"
opkg remove enigma2-plugin-extensions-archivczsk
opkg remove enigma2-plugin-extensions-subssupport
opkg remove subssupport 
rm -rf /usr/lib/enigma2/python/Plugins/Extensions/archivCZSK/
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

