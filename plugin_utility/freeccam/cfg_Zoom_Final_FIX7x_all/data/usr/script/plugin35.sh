#!/bin/sh
opkg remove filmon
rm -rf /usr/lib/enigma2/python/Plugins/Extensions/Filmon/
sleep 1
echo "stahuji plugin ...Filmon"
echo ""
cd /tmp
curl  -k -Lbk -m 55532 -m 555104 "https://drive.google.com/uc?id=12MM0rIgulhlB4NPx-lkqaOtrDvXc1Tsp&export=download" > /tmp/filmon_x_all.ipk
sleep 1
echo "instaluji ...."
cd /tmp
opkg install /tmp/filmon_x_all.ipk
echo ""
echo ""
echo ""
echo ""
echo ""
echo ""
echo ""
echo ""
sleep 1
rm /tmp/filmon_x_all.ipk
echo "OK"
killall -9 enigma2
exit
