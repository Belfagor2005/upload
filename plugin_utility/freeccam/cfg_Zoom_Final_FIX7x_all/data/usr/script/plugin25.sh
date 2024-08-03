#!/bin/sh
sleep 1
echo "stahuji m3u converter"
echo ""
cd /tmp
curl  -k -Lbk -m 55532 -m 555104 "https://drive.google.com/uc?id=1b5oCguBFo4QWebAutWb3zNUFoQ9RBKe_&export=download" > /tmp/enigma2-plugin-extensions-m2b-0.3-r0.ipk
sleep 1
echo "instaluji ...."
cd /tmp
opkg install /tmp/enigma2-plugin-extensions-m2b-0.3-r0.ipk
echo ""
echo ""
echo ""
echo ""
echo ""
echo ""
echo ""
echo ""
sleep 1
rm /tmp/enigma2-plugin-extensions-m2b-0.3-r0.ipk
echo "OK"
killall -9 enigma2
exit
