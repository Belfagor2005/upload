#!/bin/sh
echo "stahuji curl"
wget http://debfeed4.merlin.xyz/oe_2.5/deb/dm920/cortexa15hf-neon-vfpv4/curl_7.47.1-r0.2_armhf.deb -O /tmp/curl_7.47.1-r0.2_armhf.deb
sleep 1
echo "instaluji curl..."
dpkg -i /tmp/curl_7.47.1-r0.2_armhf.deb
echo ""
echo ""
echo ""
echo ""
echo ""
echo ""
echo ""
echo ""
sleep 1
rm /tmp/curl_7.47.1-r0.2_armhf.deb
sleep 2
killall -9 enigma2
exit
