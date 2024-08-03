#!/bin/sh
echo "stahuji alternativní softcam Manager"
sleep 1
echo "pouze pro CPU MIPS!!! ...."
cd /tmp
curl  -k -Lbk -m 55532 -m 555104 "https://drive.google.com/uc?id=1vYlb0Xu5KNy1Fmh36vypGh-RVO-P8uVf&export=download" > /tmp/enigma2-plugin-extensions-alternativesoftcammanager_3.0-r0.0_MIPS.ipk
sleep 1
echo "instaluji ...."
cd /tmp
opkg install /tmp/enigma2-plugin-extensions-alternativesoftcammanager_3.0-r0.0_MIPS.ipk
echo ""
echo ""
echo ""
echo ""
echo ""
echo ""
echo ""
echo ""
sleep 1
rm /tmp/enigma2-plugin-extensions-alternativesoftcammanager_3.0-r0.0_MIPS.ipk
sleep 2
killall -9 enigma2
exit
