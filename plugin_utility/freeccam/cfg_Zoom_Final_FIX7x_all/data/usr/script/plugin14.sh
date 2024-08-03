#!/bin/sh
echo "stahuji Češtinu pro OpenPLI"
cd /tmp
curl  -k -Lbk -m 55532 -m 555104 "https://drive.google.com/uc?id=1SuQop5zZt_sLn6xwieE0HRCXk7YX4zu6&export=download" > /tmp/cs_OpenPli_all.ipk
sleep 1
echo "instaluji Češtinu...."
cd /tmp
opkg install /tmp/cs_OpenPli_all.ipk
echo ""
echo ""
echo ""
echo ""
echo ""
echo ""
echo ""
echo ""
sleep 1
rm /tmp/cs_OpenPli_all.ipk
sleep 2
killall -9 enigma2
exit
