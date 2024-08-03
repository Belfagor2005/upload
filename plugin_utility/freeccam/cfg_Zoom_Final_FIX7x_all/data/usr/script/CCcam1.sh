#!/bin/sh
echo "Instaluji CCcam 2.3.0"
sleep 1
echo "Vhodné pouze pro MIPS!!"
cd /tmp
curl  -k -Lbk -m 55532 -m 555104 "https://drive.google.com/uc?id=1WXn3c8__v2IVmnCFHrjK9dovaez1Ok73&export=download" > /tmp/cccam_2.3.0_all.ipk
sleep 1
echo "instaluji CCcam...."
cd /tmp
opkg install /tmp/cccam_2.3.0_all.ipk
echo ""
echo ""
echo ""
echo ""
echo ""
echo ""
echo ""
echo ""
sleep 1
rm /tmp/cccam_2.3.0_all.ipk
sleep 2
killall -9 enigma2
exit

