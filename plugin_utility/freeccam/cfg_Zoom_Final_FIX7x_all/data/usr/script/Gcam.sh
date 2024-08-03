#!/bin/sh
echo "Instaluji Gcam_2.1-emu-r0"
sleep 1
echo "Vhodné pouze pro ALL!!"
cd /tmp
curl  -k -Lbk -m 55532 -m 555104 "https://drive.google.com/uc?id=19CPWpocITJOEbULARQN7xR8J68ZQ8pWF&export=download" > /tmp/enigma2-softcams-gcam-all-images_2.1-emu-r0-arm+mips_all.ipk
sleep 1
echo "instaluji Gcam...."
cd /tmp
opkg install /tmp/enigma2-softcams-gcam-all-images_2.1-emu-r0-arm+mips_all.ipk
echo ""
echo ""
echo ""
echo ""
echo ""
echo ""
echo ""
echo ""
sleep 1
rm /tmp/enigma2-softcams-gcam-all-images_2.1-emu-r0-arm+mips_all.ipk
sleep 2
killall -9 enigma2
exit
