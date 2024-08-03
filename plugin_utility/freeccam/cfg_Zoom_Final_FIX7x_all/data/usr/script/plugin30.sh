#!/bin/sh
opkg remove najdi - FILM
rm -rf /usr/lib/enigma2/python/Plugins/Extensions/NAJDIcam/
sleep 1
echo "stahuji plugin ...najdi FILM"
echo ""
cd /tmp
curl  -k -Lbk -m 55532 -m 555104 "https://drive.google.com/uc?id=1Rb_BOa0hbZfwHMSSCmA6HkCxulZ-2mM6&export=download" > /tmp/najdi_FILM_all.ipk
sleep 1
echo "instaluji ...."
cd /tmp
opkg install /tmp/najdi_FILM_all.ipk
echo ""
echo ""
echo ""
echo ""
echo ""
echo ""
echo ""
echo ""
sleep 1
rm /tmp/najdi_FILM_all.ipk
echo "OK"
killall -9 enigma2
exit
