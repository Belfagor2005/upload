#!/bin/sh
echo "Instaluji Ncam_V11.3-r0"
sleep 1
echo "Vhodné pouze pro ALL!!"
cd /tmp
curl  -k -Lbk -m 55532 -m 555104 "https://drive.google.com/uc?id=1HCcjdC1quVuMGlZbf0BRU0fvK0cpO-Eu&export=download" > /tmp/enigma2-plugin-softcams-ncam_V11.3-r0_all.ipk
sleep 1
echo "instaluji Ncam...."
cd /tmp
opkg install /tmp/enigma2-plugin-softcams-ncam_V11.3-r0_all.ipk
echo ""
echo ""
echo ""
echo ""
echo ""
echo ""
echo ""
echo ""
sleep 1
rm /tmp/enigma2-plugin-softcams-ncam_V11.3-r0_all.ipk
sleep 2
killall -9 enigma2
exit
