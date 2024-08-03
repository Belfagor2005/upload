#!/bin/sh
echo "stahuji plugin mediaportal"
cd /tmp
curl  -k -Lbk -m 55532 -m 555104 "https://drive.google.com/uc?id=1MlV0YlwC-6cumsE1IXn-5Dz-aCfx8Uix&export=download" > /tmp/enigma2-plugin-extensions-mediaportal_2020041901_all.ipk
sleep 1
echo "instaluji plugin...."
cd /tmp
opkg install /tmp/enigma2-plugin-extensions-mediaportal_2020041901_all.ipk
echo ""
echo ""
echo ""
echo ""
echo ""
echo ""
echo ""
echo ""
sleep 1
rm /tmp/enigma2-plugin-extensions-mediaportal_2020041901_all.ipk
sleep 2
killall -9 enigma2
exit
