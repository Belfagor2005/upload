#!/bin/sh
sleep 1
echo "stahuji OPKG pro AZBOX HD Elite"
echo ""
sleep 1
echo "pro OpenPLI 7.0 ver. !!DOM!!"
cd /tmp
curl  -k -Lbk -m 55532 -m 555104 "https://drive.google.com/uc?id=1AAsBiRy4YPGJ7BDShDDVVoTjyFz34nZy&export=download" > /tmp/opkg_AZBOX_all.ipk
sleep 1
echo "instaluji ...."
cd /tmp
opkg install /tmp/opkg_AZBOX_all.ipk
echo ""
echo ""
echo ""
echo ""
echo ""
echo ""
echo ""
echo ""
sleep 1
rm /tmp/opkg_AZBOX_all.ipk
echo "OK"
killall -9 enigma2
exit
