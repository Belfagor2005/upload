#!/bin/sh
echo "stahuji plugin Freeserver od Mino6060"
cd /tmp
curl  -k -Lbk -m 55532 -m 555104 "https://drive.google.com/uc?id=1N34KTD2WXkf1y3eOStzqizJu6RqyxVEI&export=download" > /tmp/enigma2-plugin-extensions-freeserver_7.0.2_all.ipk
sleep 1
echo "instaluji plugin...."
cd /tmp
opkg install /tmp/enigma2-plugin-extensions-freeserver_7.0.2_all.ipk
echo ""
echo ""
echo ""
echo ""
echo ""
echo ""
echo ""
echo ""
sleep 1
rm /tmp/enigma2-plugin-extensions-freeserver_7.0.2_all.ipk
sleep 2
killall -9 enigma2
exit
