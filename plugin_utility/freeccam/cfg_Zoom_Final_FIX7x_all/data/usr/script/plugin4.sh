#!/bin/sh
echo "stahuji plugin XC Player"
opkg remove xc
cd /tmp
curl  -k -Lbk -m 55532 -m 555104 "https://drive.google.com/uc?id=1mAfVL9TslUX7AUKThjYDm8PNgJ0DFAxr&export=download" > /tmp/xc_player_m3u_all.ipk
sleep 1
echo "instaluji plugin...."
cd /tmp
opkg install /tmp/xc_player_m3u_all.ipk
echo ""
echo ""
echo ""
echo ""
echo ""
echo ""
echo ""
echo ""
sleep 1
rm /tmp/xc_player_m3u_all.ipk
sleep 2
killall -9 enigma2
exit