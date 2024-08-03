#!/bin/sh
echo "stahuji curl"
wget http://openpli.ido.cz/openpli-5/mips32el/curl_7.53.1-r0_mips32el.ipk -O /tmp/curl_7.53.1-r0_mips32el.ipk
sleep 1
echo "instaluji curl..."
opkg install /tmp/curl_7.53.1-r0_mips32el.ipk
echo ""
echo ""
echo ""
echo ""
echo ""
echo ""
echo ""
echo ""
sleep 1
rm /tmp/curl_7.53.1-r0_mips32el.ipk
sleep 2
killall -9 enigma2
exit
