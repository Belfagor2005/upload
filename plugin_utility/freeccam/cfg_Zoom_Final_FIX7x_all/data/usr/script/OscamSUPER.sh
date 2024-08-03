#!/bin/sh
echo "Instaluji Oscam-supcam_11.681"
sleep 1
echo "Vhodné pouze pro ALL!!"
cd /tmp
curl  -k -Lbk -m 55532 -m 555104 "https://drive.google.com/uc?id=1GpA1Y4J61H9wUHX9MrD2HEZRJuY7Ueco&export=download" > /tmp/enigma2-plugin-softcams-oscam-supcam_11.681-emu-r798_all.ipk
sleep 1
echo "instaluji Oscam...."
cd /tmp
opkg install /tmp/enigma2-plugin-softcams-oscam-supcam_11.681-emu-r798_all.ipk
echo ""
echo ""
echo ""
echo ""
echo ""
echo ""
echo ""
echo ""
sleep 1
rm /tmp/enigma2-plugin-softcams-oscam-supcam_11.681-emu-r798_all.ipk
sleep 2
killall -9 enigma2
exit
