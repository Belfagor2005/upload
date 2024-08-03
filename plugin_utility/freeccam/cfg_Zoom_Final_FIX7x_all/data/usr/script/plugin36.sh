#!/bin/sh
opkg remove stream
rm -rf /usr/lib/enigma2/python/Plugins/Extensions/StreamHunter/
sleep 1
echo "stahuji plugin ...StreamHunter"
echo ""
cd /tmp
curl  -k -Lbk -m 55532 -m 555104 "https://drive.google.com/uc?id=1uCYL1PRqQsfRIk09BmRKDTZLH4H2pGmw&export=download" > /tmp/stream_hunter8_all.ipk
sleep 1
echo "instaluji ...."
cd /tmp
opkg install /tmp/stream_hunter8_all.ipk
echo ""
echo ""
echo ""
echo ""
echo ""
echo ""
echo ""
echo ""
sleep 1
rm /tmp/stream_hunter8_all.ipk
echo "OK"
killall -9 enigma2
exit
