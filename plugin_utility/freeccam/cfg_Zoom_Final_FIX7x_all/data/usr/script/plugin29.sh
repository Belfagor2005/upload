#!/bin/sh
opkg remove hledej - FILM
rm -rf /usr/lib/enigma2/python/Plugins/Extensions/FILMcam/
sleep 1
echo "stahuji plugin ...hledej FILM"
echo ""
cd /tmp
curl  -k -Lbk -m 55532 -m 555104 "https://drive.google.com/uc?id=1LiQwKCAvoi6qF9H6v98nkGWGXvzbxvTS&export=download" > /tmp/hledej_FILM5_all.ipk
sleep 1
echo "instaluji ...."
cd /tmp
opkg install /tmp/hledej_FILM5_all.ipk
echo ""
echo ""
echo ""
echo ""
echo ""
echo ""
echo ""
echo ""
sleep 1
rm /tmp/hledej_FILM5_all.ipk
echo "OK"
killall -9 enigma2
exit
