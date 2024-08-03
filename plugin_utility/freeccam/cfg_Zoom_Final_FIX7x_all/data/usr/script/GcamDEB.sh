#!/bin/sh
echo "Instaluji Gcam_2.1-emu-r0"
sleep 1
echo "Vhodné pouze pro ALL!!"
cd /tmp
curl  -k -Lbk -m 55532 -m 555104 "https://drive.google.com/uc?id=1-HoknjT6R0G7UNsxswxFoypnCFqRxV60&export=download" > /tmp/enigma2-softcams-gcam-all-images_2.1-emu-r0-arm+mips_all.deb
sleep 1
echo "instaluji Gcam...."
cd /tmp
dpkg -i /tmp/enigma2-softcams-gcam-all-images_2.1-emu-r0-arm+mips_all.deb
echo ""
echo ""
echo ""
echo ""
echo ""
echo ""
echo ""
echo ""
sleep 1
rm /tmp/enigma2-softcams-gcam-all-images_2.1-emu-r0-arm+mips_all.deb
sleep 2
killall -9 enigma2
exit
