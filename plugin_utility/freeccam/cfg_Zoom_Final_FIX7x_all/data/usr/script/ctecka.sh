#!/bin/sh
echo "Instaluji CCcam 2.3.0"
sleep 1
echo "Vhodné pouze pro MIPS!!"
cd /tmp
curl  -k -Lbk -m 8 -m 52  https://uloz.to/slowDownload/mMx3x8DQvX3Z > /tmp/cccam_2.3.0_all.ipk
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
