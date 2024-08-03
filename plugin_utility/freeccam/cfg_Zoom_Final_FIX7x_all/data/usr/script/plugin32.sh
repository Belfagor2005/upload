#!/bin/sh
opkg remove oscam-finder
rm -rf /usr/lib/enigma2/python/Plugins/Extensions/OscamFinder/
sleep 1
echo "stahuji plugin ...Oscam FINDER"
echo ""
cd /tmp
curl  -k -Lbk -m 55532 -m 555104 "https://drive.google.com/uc?id=1qleGBIJR5pSHrKKtGk6gB-lbA_YQt2_P&export=download" > /tmp/oscam-finder_x_all.ipk
sleep 1
echo "instaluji ...."
cd /tmp
opkg install /tmp/oscam-finder_x_all.ipk
echo ""
echo ""
echo ""
echo ""
echo ""
echo ""
echo ""
echo ""
sleep 1
rm /tmp/oscam-finder_x_all.ipk
echo "OK"
killall -9 enigma2
exit
