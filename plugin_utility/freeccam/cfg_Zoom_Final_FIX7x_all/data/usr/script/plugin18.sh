#!/bin/sh
echo "stahuji Mediaplayer2"
sleep 1
cd /tmp
curl  -k -Lbk -m 55532 -m 555104 "https://drive.google.com/uc?id=1W9ozfMhRVahDDJWe3ySnI6EXNI8g1of7&export=download" > /tmp/enigma2-plugin-extensions-mediaplayer2_0.41_20140201_all.ipk
sleep 1
opkg remove enigma2-plugin-mediaplayer2
opkg remove enigma2-plugin-mediaplayer2ab
opkg remove enigma2-plugin-extensions-mediaplayer2
opkg remove enigma2-plugin-extensions-mediaplayer
echo "instaluji ...."
cd /tmp
opkg install /tmp/enigma2-plugin-extensions-mediaplayer2_0.41_20140201_all.ipk
echo ""
echo ""
echo ""
echo ""
echo ""
echo ""
echo ""
echo ""
sleep 1
rm /tmp/enigma2-plugin-extensions-mediaplayer2_0.41_20140201_all.ipk
sleep 2
killall -9 enigma2
exit
