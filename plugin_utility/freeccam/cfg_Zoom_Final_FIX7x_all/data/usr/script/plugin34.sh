#!/bin/sh
opkg remove najdi - BILIBILI
rm -rf /usr/lib/enigma2/python/Plugins/Extensions/NAJDIbilibili/
sleep 1
echo "stahuji plugin ...najdi BILIBILI"
echo ""
cd /tmp
curl  -k -Lbk -m 55532 -m 555104 "https://drive.google.com/uc?id=15BqqIuNyLxPklSSaym5JxY5TUuxD8l9_&export=download" > /tmp/najdi_BILIBILI2_all.ipk
sleep 1
echo "instaluji ...."
cd /tmp
opkg install /tmp/najdi_BILIBILI2_all.ipk
echo ""
echo ""
echo ""
echo ""
echo ""
echo ""
echo ""
echo ""
sleep 1
rm /tmp/najdi_BILIBILI2_all.ipk
echo "OK"
killall -9 enigma2
exit
