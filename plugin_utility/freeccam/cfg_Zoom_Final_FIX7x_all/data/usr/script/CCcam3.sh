#!/bin/sh
echo "Instaluji CCcam 2.3.2 SkyDE"
sleep 1
echo "Vhodné pro ALL!!"
cd /tmp
curl  -k -Lbk -m 55532 -m 555104 "https://drive.google.com/uc?id=1m1gVNfPc6MdcY88uRA3CpLhCQqhyK6mP&export=download" > /tmp/enigma2-softcams-cccam-all-images_2.3.2-emu-r3-arm+mips_all.ipk
sleep 1
echo "instaluji CCcam...."
cd /tmp
opkg install /tmp/enigma2-softcams-cccam-all-images_2.3.2-emu-r3-arm+mips_all.ipk
echo ""
echo ""
echo ""
echo ""
echo ""
echo ""
echo ""
sleep 1
rm /tmp/enigma2-softcams-cccam-all-images_2.3.2-emu-r3-arm+mips_all.ipk
sleep 2
killall -9 enigma2
exit
