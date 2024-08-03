#!/bin/sh
echo "stahuji CAM Manager Tivu"
sleep 1
cd /tmp
curl  -k -Lbk -m 55532 -m 555104 "https://drive.google.com/uc?id=1q_BrDjZWHkzE3rcJsivpMBfid0UV-RvR&export=download" > /tmp/enigma2-plugin-extensions-tvmanager_1.2k_all.ipk
sleep 1
echo "instaluji ...."
cd /tmp
opkg install /tmp/enigma2-plugin-extensions-tvmanager_1.2k_all.ipk
echo ""
echo ""
echo ""
echo ""
echo ""
echo ""
echo ""
echo ""
sleep 1
rm /tmp/enigma2-plugin-extensions-tvmanager_1.2k_all.ipk
sleep 2
killall -9 enigma2
exit
