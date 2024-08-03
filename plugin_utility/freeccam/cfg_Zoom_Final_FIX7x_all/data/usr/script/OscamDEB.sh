#!/bin/sh
echo "Instaluji Oscam_11.615"
sleep 1
echo "Vhodné pouze pro ALL!!"
cd /tmp
curl  -k -Lbk -m 55532 -m 555104 "https://drive.google.com/uc?id=1zomoM7ud8j_icRrrzmRkNO8kUHZH2jjo&export=download" > /tmp/enigma2-softcams-oscam-all-images_11.615-emu-r798-arm+mips_all.deb
sleep 1
echo "instaluji Oscam...."
cd /tmp
dpkg -i /tmp/enigma2-softcams-oscam-all-images_11.615-emu-r798-arm+mips_all.deb
echo ""
echo ""
echo ""
echo ""
echo ""
echo ""
echo ""
echo ""
sleep 1
rm /tmp/enigma2-softcams-oscam-all-images_11.615-emu-r798-arm+mips_all.deb
sleep 2
killall -9 enigma2
exit
