#!/bin/sh
echo "stahuji seasondream-NG"
sleep 1
cd /tmp
curl  -k -Lbk -m 55532 -m 555104 "https://drive.google.com/uc?id=15KY5skPqT90cWIJFpTHPjE2c-2HjvAFl&export=download" > /tmp/enigma2-plugin-extensions-seasondream-ng_3.0.200331b_all.ipk
sleep 1
echo "instaluji ...."
cd /tmp
opkg install /tmp/enigma2-plugin-extensions-seasondream-ng_3.0.200331b_all.ipk
echo ""
echo ""
echo ""
echo ""
echo ""
echo ""
echo ""
echo ""
sleep 1
rm /tmp/enigma2-plugin-extensions-seasondream-ng_3.0.200331b_all.ipk
sleep 2
killall -9 enigma2
exit
