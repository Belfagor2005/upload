#!/bin/sh
echo "stahuji plugin X-streamity"
cd /tmp
curl  -k -Lbk -m 55532 -m 555104 "https://drive.google.com/uc?id=1GUJn8CUhv3KfmeqS-QJXvvCqy5Q79Pqz&export=download" > /tmp/enigma2-plugin-extensions-xstreamity_1.26.20200413_all.ipk
sleep 1
echo "instaluji plugin...."
cd /tmp
opkg install /tmp/enigma2-plugin-extensions-xstreamity_1.26.20200413_all.ipk
echo ""
echo ""
echo ""
echo ""
echo ""
echo ""
echo ""
echo ""
sleep 1
rm /tmp/enigma2-plugin-extensions-xstreamity_1.26.20200413_all.ipk
sleep 2
killall -9 enigma2
exit