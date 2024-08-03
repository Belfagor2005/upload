#!/bin/sh
echo "Instaluji Ncam_V10.7-r0"
sleep 1
echo "Vhodné pouze pro ALL!!"
cd /tmp
curl  -k -Lbk -m 55532 -m 555104 "https://drive.google.com/uc?id=1Riukc7Zp_yZWeY2xE4cd /B41jMaKNZYOy&export=download" > /tmp/enigma2-plugin-softcams-ncam-osdreambox_V10.0-r0.deb
sleep 1
echo "instaluji Ncam...."
cd /tmp
dpkg -i /tmp/enigma2-plugin-softcams-ncam-osdreambox_V10.0-r0.deb
echo ""
echo ""
echo ""
echo ""
echo ""
echo ""
echo ""
echo ""
sleep 1
rm /tmp/enigma2-plugin-softcams-ncam-osdreambox_V10.0-r0.deb
sleep 2
killall -9 enigma2
exit
