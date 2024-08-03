#!/bin/sh
opkg remove enigma2-plugin-extensions-mylust
rm -rf /usr/lib/enigma2/python/Plugins/Extensions/mylust/
sleep 1
echo "stahuji plugin ...Mylust"
echo ""
cd /tmp
curl  -k -Lbk -m 55532 -m 555104 "https://drive.google.com/uc?id=11s_lXYHTEGOTPoFRq7i_snrA-2G40O4J&export=download" > /tmp/enigma2-plugin-extensions-mylust_1.0_all.ipk
sleep 1
echo "instaluji ...."
cd /tmp
opkg install /tmp/enigma2-plugin-extensions-mylust_1.0_all.ipk
echo ""
echo ""
echo ""
echo ""
echo ""
echo ""
echo ""
echo ""
sleep 1
rm /tmp/enigma2-plugin-extensions-mylust_1.0_all.ipk
echo "OK"
killall -9 enigma2
exit

