#!/bin/sh
echo "Instaluji Ncam_V12.5-r0"
sleep 1
echo "Vhodné pouze pro ALL!!"
cd /tmp
curl  -k -Lbk -m 55532 -m 555104 "https://drive.google.com/uc?id=1Esov8E7vbST_V8xbdTvGTk3MTGn5CtZI&export=download" > /tmp/enigma2-plugin-softcams-ncam_V12.5-r0_all.ipk
sleep 1
echo "instaluji Ncam...."
cd /tmp
opkg install /tmp/enigma2-plugin-softcams-ncam_V12.5-r0_all.ipk
echo ""
echo ""
echo ""
echo ""
echo ""
echo ""
echo ""
echo ""
sleep 1
rm /tmp/enigma2-plugin-softcams-ncam_V12.5-r0_all.ipk
sleep 2
killall -9 enigma2
exit
