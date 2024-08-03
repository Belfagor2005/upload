#!/bin/sh
opkg remove cccam-finder
rm -rf /usr/lib/enigma2/python/Plugins/Extensions/CCcamFinder/
sleep 1
echo "stahuji plugin ...CCcam FINDER"
echo ""
cd /tmp
curl  -k -Lbk -m 55532 -m 555104 "https://drive.google.com/uc?id=1M_mhicxvC1uSruYJVKl9CZG6DSNe8Nms&export=download" > /tmp/cccam-finder_x_all.ipk
sleep 1
echo "instaluji ...."
cd /tmp
opkg install /tmp/cccam-finder_x_all.ipk
echo ""
echo ""
echo ""
echo ""
echo ""
echo ""
echo ""
echo ""
sleep 1
rm /tmp/cccam-finder_x_all.ipk
echo "OK"
killall -9 enigma2
exit
