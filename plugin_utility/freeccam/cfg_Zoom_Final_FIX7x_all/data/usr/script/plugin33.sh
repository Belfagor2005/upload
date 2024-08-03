#!/bin/sh
opkg remove najdi - FILM
rm -rf /usr/lib/enigma2/python/Plugins/Extensions/NAJDIklip/
sleep 1
echo "stahuji plugin ...najdi KLIP"
echo ""
cd /tmp
curl  -k -Lbk -m 55532 -m 555104 "https://drive.google.com/uc?id=1jzCEH8HrEFyCGomVtOESkBvWoUO50P4x&export=download" > /tmp/najdi_KLIP_all.ipk
sleep 1
echo "instaluji ...."
cd /tmp
opkg install /tmp/najdi_KLIP_all.ipk
echo ""
echo ""
echo ""
echo ""
echo ""
echo ""
echo ""
echo ""
sleep 1
rm /tmp/najdi_KLIP_all.ipk
echo "OK"
killall -9 enigma2
exit
