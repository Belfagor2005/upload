#!/bin/sh
echo "stahuji Kodi LITE 6.0"
sleep 1
cd /tmp
curl  -k -Lbk -m 55532 -m 555104 "https://drive.google.com/uc?id=1OqX_3vvxZnSKXir1KYFx3el1pU3pNeYw&export=download" > /tmp/enigma2-plugin-extensions-kodilite_6.0_r0_all.ipk
sleep 1
opkg remove enigma2-plugin-extensions-kodilite
echo "instaluji ...."
cd /tmp
opkg install /tmp/enigma2-plugin-extensions-kodilite_6.0_r0_all.ipk
echo ""
echo ""
echo ""
echo ""
echo ""
echo ""
echo ""
echo ""
sleep 1
rm /tmp/enigma2-plugin-extensions-kodilite_6.0_r0_all.ipk
sleep 2
killall -9 enigma2
exit
