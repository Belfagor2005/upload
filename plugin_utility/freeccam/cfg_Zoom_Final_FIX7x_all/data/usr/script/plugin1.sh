#!/bin/sh
echo "stahuji plugin Youtube"
cd /tmp
curl  -k -Lbk -m 55532 -m 555104 "https://drive.google.com/uc?id=1fRMHaM_37YEbZ6Zk87cFdyIXYuQjype8&export=download" > /tmp/enigma2-plugin-extensions-youtube_h1+git486+1f8bc35-r0.0_all.ipk
sleep 1
echo "instaluji plugin...."
cd /tmp
opkg install /tmp/enigma2-plugin-extensions-youtube_h1+git486+1f8bc35-r0.0_all.ipk
echo ""
echo ""
echo ""
echo ""
echo ""
echo ""
echo ""
echo ""
sleep 1
rm /tmp/enigma2-plugin-extensions-youtube_h1+git486+1f8bc35-r0.0_all.ipk
sleep 2
killall -9 enigma2
exit