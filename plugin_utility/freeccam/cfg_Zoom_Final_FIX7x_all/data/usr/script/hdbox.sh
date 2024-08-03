#!/bin/sh
echo "Instaluji Oscam,Ncam pro sh4"
sleep 1
echo "Vhodné pouze pro CPU sh4!!"
opkg remove cams
cd /tmp
curl  -k -Lbk -m 55532 -m 555104 "https://drive.google.com/uc?id=1xOUG9HxSz9BXB_MjjuzPaKMMie1Tuwk5&export=download" > /tmp/cams_HDBOX1_all.ipk
sleep 1
echo "instaluji CAMs...."
cd /tmp
opkg install /tmp/cams_HDBOX1_all.ipk
echo ""
echo ""
echo ""
echo ""
echo ""
echo ""
echo ""
echo ""
sleep 1
rm -rf /tmp/etc
rm -rf /tmp/usr
rm /tmp/cams_HDBOX1_all.ipk
sleep 2
killall -9 enigma2
exit

