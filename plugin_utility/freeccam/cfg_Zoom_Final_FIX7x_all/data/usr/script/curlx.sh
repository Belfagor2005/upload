#!/bin/sh
echo "install Curl"
sleep 2
echo "AZBOX HD Elite"
sleep 2
echo "Open PLI 7.0 vr. !DOM!"
echo ""
cp /usr/lib/enigma2/python/Plugins/Extensions/OpenPanel/DATA/AZBOX/curl_XXX_all.ipk /tmp/
sleep 1
echo "instaluji curl..."
opkg install /tmp/curl_XXX_all.ipk
echo ""
echo ""
echo ""
echo ""
echo ""
echo ""
echo ""
echo ""
sleep 1
rm /tmp/curl_XXX_all.ipk
killall -9 enigma2
exit