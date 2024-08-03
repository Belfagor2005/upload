#!/bin/sh
echo "stahuji softcam Manager zelda77"
sleep 1
echo "instaluji ...."
cd /tmp
curl  -k -Lbk -m 55532 -m 555104 "https://drive.google.com/uc?id=1K4pKtKet8nknUUckQ_IMhxaZKjR8EPO2&export=download" > /tmp/sm_x_all.ipk
sleep 1
echo "thanks for zelda77"
cd /tmp
opkg install /tmp/sm_x_all.ipk
echo ""
echo ""
echo ""
echo ""
echo ""
echo ""
echo ""
echo ""
sleep 1
rm /tmp/sm_x_all.ipk
sleep 2
killall -9 enigma2
exit
