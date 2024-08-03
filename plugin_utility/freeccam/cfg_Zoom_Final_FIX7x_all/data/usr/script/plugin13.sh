#!/bin/sh
echo "stahuji plugin TV panel"
cd /tmp
curl  -k -Lbk -m 55532 -m 555104 "https://drive.google.com/uc?id=1wjP-KXgaK89XP1IU18cGPjxzc8M4EebW&export=download" > /tmp/enigma2-plugin-extensions-tvpanel_1.8.4_all.ipk
sleep 1
echo "instaluji plugin...."
cd /tmp
opkg install /tmp/enigma2-plugin-extensions-tvpanel_1.8.4_all.ipk
echo ""
echo ""
echo ""
echo ""
echo ""
echo ""
echo ""
echo ""
sleep 1
rm /tmp/enigma2-plugin-extensions-tvpanel_1.8.4_all.ipk
sleep 2
killall -9 enigma2
exit