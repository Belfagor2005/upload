#!/bin/sh
echo "stahuji LuxSatMENU"
sleep 1
cd /tmp
curl  -k -Lbk -m 55532 -m 555104 "https://drive.google.com/uc?id=1VPxJcghX3q41dNpvVYngO1a4nkiy6nfP&export=download" > /tmp/enigma2-luxsat-menu_12.9_all.ipk
sleep 1
echo "instaluji ...."
cd /tmp
opkg install /tmp/enigma2-luxsat-menu_12.9_all.ipk
echo ""
echo ""
echo ""
echo ""
echo ""
echo ""
echo ""
echo ""
sleep 1
rm /tmp/enigma2-luxsat-menu_12.9_all.ipk
sleep 2
killall -9 enigma2
exit
