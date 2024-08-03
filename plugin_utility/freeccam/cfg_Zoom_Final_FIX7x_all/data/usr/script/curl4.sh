#!/bin/sh
echo "stahuji curl"
wget http://titannit.dyndns.tv/6.3/spark7162/sh4/curl_7.62.0-r0_sh4.ipk -O /tmp/curl_7.62.0-r0_sh4.ipk
sleep 1
echo "instaluji curl..."
opkg install /tmp/curl_7.62.0-r0_sh4.ipk
echo ""
echo ""
echo ""
echo ""
echo ""
echo ""
echo ""
echo ""
sleep 1
rm /tmp/curl_7.62.0-r0_sh4.ipk
sleep 2
killall -9 enigma2
exit


