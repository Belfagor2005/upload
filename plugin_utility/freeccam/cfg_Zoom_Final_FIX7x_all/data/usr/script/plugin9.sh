#!/bin/sh
echo ""
echo "vítám Vás u instalace pluginu archivCZSK"
sleep 1
echo "stahuji .....subssupport"
echo ""
echo ""
echo ""
echo ""
sleep 2
cd /tmp
curl  -k -Lbk -m 1232 -m 5104  http://github.com/mx3L/archivczsk/releases/download/v1.0/subssupport_1.5.5-20170116_all.ipk > /tmp/subssupport_1.5.5-20170116_all.ipk
sleep 1
echo "instaluji subssupport_1.5.5-20170116"
cd /tmp
opkg install /tmp/subssupport_1.5.5-20170116_all.ipk
echo ""
echo ""
echo ""
echo ""
echo ""
echo ""
echo ""
echo ""
sleep 1
rm /tmp/subssupport_1.5.5-20170116_all.ipk
echo ""
echo "stahuji plugin Archiv CZSK"
sleep 1
cd /tmp
curl  -k -Lbk -m 55532 -m 555104 "https://drive.google.com/uc?id=1zCZ1BgRbI3rONZK8qRxXoIbhxA6RFXpO&export=download" > /tmp/enigma2-plugin-extensions-archivczsk_1.2.2_all.ipk
sleep 1
echo "instaluji ....archivczsk_1.2.3-....."
cd /tmp
opkg install /tmp/enigma2-plugin-extensions-archivczsk_1.2.2_all.ipk
echo ""
echo ""
echo ""
echo ""
echo ""
echo ""
echo ""
echo ""
sleep 1
rm /tmp/enigma2-plugin-extensions-archivczsk_1.2.2_all.ipk
sleep 2
init 4
init 3
killall -9 enigma2
exit
