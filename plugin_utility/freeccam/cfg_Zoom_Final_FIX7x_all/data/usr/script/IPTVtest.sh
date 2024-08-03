#!/bin/sh
echo "stahuji a instaluji"
sleep 1
echo "IPTV + X"
sleep 1
echo "do ....settingu"
sleep 1
echo "do ..../movie/ jako m3u"
sleep 2
echo "downloading and installing"
sleep 1
echo "IPTV + X"
sleep 1
echo "to in ....setting"
sleep 1
echo "to in ..../movie/ like m3u"
echo ""
echo ""
[ -d /movie ] || mkdir -p /movie
more /usr/lib/enigma2/python/Plugins/Extensions/OpenPanel/DATA/x  >> /etc/enigma2/bouquets.tv 
sed -i "s/%/userbouquet.IPTV.m3u.tv/" /etc/enigma2/bouquets.tv
more /usr/lib/enigma2/python/Plugins/Extensions/OpenPanel/DATA/x  >> /etc/enigma2/bouquets.tv 
sed -i "s/%/userbouquet.X.m3u8.tv/" /etc/enigma2/bouquets.tv

curl  -k -Lbk -m 55532 -m 555104 "https://drive.google.com/uc?id=1S7bmru3T6Z1y8_2zGyOCfwFys1HE2LyK&export=download" > /movie/IPTV.m3u
curl  -k -Lbk -m 55532 -m 555104 "https://drive.google.com/uc?id=1IlY1yBxU9hnP7pHNhQ2WaVfEevfnH4Oy&export=download" > /movie/X.m3u8
curl  -k -Lbk -m 55532 -m 555104 "https://drive.google.com/uc?id=1rpvSYxOY9uk5WN4JH2TYlZPmZCJZ4xtB&export=download" > /etc/enigma2/userbouquet.IPTV.m3u.tv
curl  -k -Lbk -m 55532 -m 555104 "https://drive.google.com/uc?id=1Qv-PfWcBn39NBxLklswZjf80xyPKRDbg&export=download" > /etc/enigma2/userbouquet.X.m3u8.tv


###########################################################################################################
wget -q -O - http://root%s@127.0.0.1/web/servicelistreload?mode=0 >>/dev/null 2>&1 </dev/null &
sleep 2
echo "OK"
exit

