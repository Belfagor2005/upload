#!/bin/sh
[ -d /tmp/test ] || mkdir -p /tmp/test
[ -d /IPTV/Ru ] || mkdir -p /IPTV/Ru

more /usr/lib/enigma2/python/Plugins/Extensions/OpenPanel/DATA/x  >> /etc/enigma2/bouquets.tv 
sed -i "s/%/userbouquet.Rus.m3u.tv/" /etc/enigma2/bouquets.tv 

echo "Stahování Rus.m3u"
echo "Downloading Rus.m3u"
curl  -k -Lbk -A -k -m 8 -m 52 -s  https://webarmen.com/my/iptv/auto.all.m3u > /IPTV/Ru/Rus.m3u
cd /
rm -rf /tmp/test
echo ""
echo "converter Rus.m3u for Enigma"
sleep 1
echo "start"
[ -d /tmp/test ] || mkdir -p /tmp/test
cp /IPTV/Ru/Rus.m3u /tmp/test/Ru.m3u
sed '1,1d' /tmp/test/Ru.m3u > /tmp/test/Rus.m3u
awk '/http/#EXTINF/ {print}' /tmp/test/Rus.m3u > /tmp/test/Rus2.m3u
awk 'BEGIN {FS="tvg-"}{print  $NF}'  /tmp/test/Rus2.m3u > /tmp/test/Rus3.m3u
cut -d ',' -f 1  /tmp/test/Rus3.m3u > /tmp/test/Rus4.m3u
sed -e "s/name=/#DESCRIPTION /" /tmp/test/Rus4.m3u > /tmp/test/Rus5.m3u
tr -d '["]' < "/tmp/test/Rus5.m3u" > /tmp/test/Rus6.m3u
sed 's/:/%3a/g' /tmp/test/Rus6.m3u > /tmp/test/Rus7.m3u
sed -e "s/http/#SERVICE 4097:0:1128:0:0:0:0:0:0:0:http/" /tmp/test/Rus7.m3u > /tmp/test/Rus8.m3u
awk '{print NR " " $0}' /tmp/test/Rus8.m3u  > /tmp/test/Rus9.m3u
sort -n -r "/tmp/test/Rus9.m3u"|grep -o -i '#[^<]*' > /tmp/test/Rus10.m3u
echo "#NAME Rus.m3u" > /etc/enigma2/userbouquet.Rus.m3u.tv
cat /tmp/test/Rus10.m3u >> /etc/enigma2/userbouquet.Rus.m3u.tv
rm -rf /tmp/test
cd /
wget -q -O - http://root%s@127.0.0.1/web/servicelistreload?mode=0 >>/dev/null 2>&1 </dev/null &
sleep 2
echo "OK"
exit







