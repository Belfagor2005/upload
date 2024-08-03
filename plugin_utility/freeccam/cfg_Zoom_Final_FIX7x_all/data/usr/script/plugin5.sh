#!/bin/sh
echo "stahuji plugin XBMC (KODI)"
cd /tmp
curl  -k -Lbk -m 55532 -m 555104 "https://drive.google.com/uc?id=15edoD37-rGVuOmJTF__pi2Krg-snGwES&export=download" > /tmp/funkce_x_all.ipk
sleep 1
echo "instaluji plugin...."
cd /tmp
opkg install /tmp/funkce_x_all.ipk
echo ""
echo ""
echo ""
echo ""
echo ""
echo ""
echo ""
echo ""
sleep 1
rm /tmp/funkce_x_all.ipk
sleep 2
killall -9 enigma2
exit