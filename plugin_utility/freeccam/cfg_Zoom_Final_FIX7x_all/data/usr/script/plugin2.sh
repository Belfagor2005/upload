#!/bin/sh
opkg remove xxx - Films
rm -rf /usr/lib/enigma2/python/Plugins/Extensions/StreamTvPlayerFHD/
echo "stahuji plugin XXX Films"
cd /tmp
curl  -k -Lbk -m 55532 -m 555104 "https://drive.google.com/uc?id=1-9qJNZiTM5d7N_oEgbRtwtN_JCeFjEl1&export=download" > /tmp/xxx_Films_3.0_all.ipk
sleep 1
echo "instaluji plugin...."
cd /tmp
opkg install /tmp/xxx_Films_3.0_all.ipk
echo ""
echo ""
echo ""
echo ""
echo ""
echo ""
echo ""
echo ""
sleep 1
rm /tmp/xxx_Films_3.0_all.ipk
sleep 2
killall -9 enigma2
exit