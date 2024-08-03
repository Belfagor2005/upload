#!/bin/sh
opkg remove epodown 
rm -rf /usr/lib/enigma2/python/Plugins/Extensions/eporner/
echo "stahuji plugin Eporner"
cd /tmp
curl  -k -Lbk -m 55532 -m 555104 "https://drive.google.com/uc?id=1t_cgjJEBZmyM184C7drMT3VhVd4aMLax&export=download" > /tmp/epodown_2.0_all.ipk
sleep 1
echo "instaluji plugin...."
cd /tmp
opkg install /tmp/epodown_2.0_all.ipk
echo ""
echo ""
echo ""
echo ""
echo ""
echo ""
echo ""
echo ""
sleep 1
rm /tmp/epodown_2.0_all.ipk
sleep 2
killall -9 enigma2
exit