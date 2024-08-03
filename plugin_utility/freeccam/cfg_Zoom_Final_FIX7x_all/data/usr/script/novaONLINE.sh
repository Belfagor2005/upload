#!/bin/sh
sleep 1
echo "Stahuji Nova TV ... online vysílání"
sleep 1
sed -i '/userbouquet.NOVAonline.m3u.tv/d' /etc/enigma2/bouquets.tv 
more /usr/lib/enigma2/python/Plugins/Extensions/OpenPanel/DATA/x  >> /etc/enigma2/bouquets.tv 
sed -i "s/%/userbouquet.NOVAonline.m3u.tv/" /etc/enigma2/bouquets.tv 
[ -d /IPTV ] || mkdir -p /IPTV
curl  -k -Lbk -m 55532 -m 555104  "https://www.dropbox.com/s/d3gtwdyao4bed22/NOVA.m3u?dl=1" > /IPTV/NOVAonline.m3u
sleep 1
curl  -k -Lbk -m 55532 -m 555104  "https://www.dropbox.com/s/khmc7uzgw5jhtqo/userbouquet.NOVAonline.m3u.tv?dl=1" > /etc/enigma2/userbouquet.NOVAonline.m3u.tv
cd /
rm -rf /tmp/test
wget -q -O - http://root%s@127.0.0.1/web/servicelistreload?mode=0 >>/dev/null 2>&1 </dev/null &
sleep 1
echo "NOVAonline.m3u ...../IPTV/"
sleep 2
echo "OK"
sleep 1
echo ""
echo "NOVAonline .....setting"
sleep 2
echo "OK"
sleep 1
echo ""
exit
