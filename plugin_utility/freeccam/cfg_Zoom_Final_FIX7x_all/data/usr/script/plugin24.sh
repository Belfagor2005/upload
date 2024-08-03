#!/bin/sh
echo "stahuji glasssysutil 10.78"
sleep 1
cd /tmp
curl  -k -Lbk -m 55532 -m 555104 "https://drive.google.com/uc?id=1nc92QK5Fcd /tZcvilAaYQYdpeLlTnXAVq&export=download" > /tmp/enigma2-plugin-glasssysutil_10.78_all.ipk
sleep 1
echo "instaluji ...."
cd /tmp
opkg install /tmp/enigma2-plugin-glasssysutil_10.78_all.ipk
echo ""
echo ""
echo ""
echo ""
echo ""
echo ""
echo ""
echo ""
sleep 1
rm /tmp/enigma2-plugin-glasssysutil_10.78_all.ipk
sleep 2
killall -9 enigma2
exit