#!/bin/sh
echo "stahuji curl"
wget http://dev.myslug.de/builds/curl/curl_7.17.1-1_armeb.ipk -O /tmp/curl_7.17.1-1_armeb.ipk
sleep 1
echo "instaluji curl..."
opkg install /tmp/curl_7.17.1-1_armeb.ipk
echo ""
echo ""
echo ""
echo ""
echo ""
echo ""
echo ""
echo ""
sleep 1
rm /tmp/curl_7.17.1-1_armeb.ipk
sleep 2
killall -9 enigma2
exit
