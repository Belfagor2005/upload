#!/bin/sh
[ -d /tmp/test ] || mkdir -p /tmp/test
[ -d /IPTV/World ] || mkdir -p /IPTV/World

more /usr/lib/enigma2/python/Plugins/Extensions/OpenPanel/DATA/x  >> /etc/enigma2/bouquets.tv 
sed -i "s/%/userbouquet.BeinSport.m3u.tv/" /etc/enigma2/bouquets.tv 

echo "Stahování BeinSport.m3u"
echo "Downloading BeinSport.m3u"
curl  -k -Lbk -A -k -m 8 -m 52 -s  https://iptv-org.github.io/iptv/categories/sport.m3u	 > /IPTV/World/BeinSport.m3u
cd /
rm -rf /tmp/test
echo ""
echo "converter BeinSport.m3u for Enigma"
sleep 1
echo "start"
[ -d /tmp/test ] || mkdir -p /tmp/test
cp /IPTV/World/BeinSport.m3u /tmp/test/Ru.m3u
sed '1,1d' /tmp/test/Ru.m3u > /tmp/test/Rus.m3u
awk 'BEGIN {FS="png"}{print  $NF}'  /tmp/test/Rus.m3u > /tmp/test/Rus3.m3u
awk 'BEGIN {FS="group-"}{print  $NF}'  /tmp/test/Rus3.m3u > /tmp/test/Rus4.m3u
sed 's/",/#DESCRIPTION /g' /tmp/test/Rus4.m3u > /tmp/test/Rus5.m3u
sed 's/#EXTINF/#DESCRIPTION /g' /tmp/test/Rus5.m3u > /tmp/test/Rus5a.m3u
sed 's/:-1 ,/ /g' /tmp/test/Rus5a.m3u > /tmp/test/Rus6.m3u
sed 's/:-1,/ /g' /tmp/test/Rus6.m3u > /tmp/test/Rus6a.m3u
sed 's/:0,/ /g' /tmp/test/Rus6a.m3u > /tmp/test/Rus6b.m3u
sed 's/: / /g' /tmp/test/Rus6b.m3u > /tmp/test/Rus6c.m3u
sed 's/:/%3a/g' /tmp/test/Rus6c.m3u > /tmp/test/Rus7.m3u
sed -e "s/http/#SERVICE 4097:0:1128:0:0:0:0:0:0:0:http/" /tmp/test/Rus7.m3u > /tmp/test/Rus8.m3u
tr -d '["]' < "/tmp/test/Rus8.m3u" > /tmp/test/Rus8c.m3u
tr -d '[,]' < "/tmp/test/Rus8c.m3u" > /tmp/test/Rus8.m3u
awk '{print NR " " $0}' /tmp/test/Rus8.m3u  > /tmp/test/Rus9.m3u
sort -n -r "/tmp/test/Rus9.m3u"|grep -o -i '#[^<]*' > /tmp/test/Rus10.m3u
echo "#NAME BeinSport.m3u" > /etc/enigma2/userbouquet.BeinSport.m3u.tv
cat /tmp/test/Rus10.m3u >> /etc/enigma2/userbouquet.BeinSport.m3u.tv
rm -rf /tmp/test
cd /
wget -q -O - http://root%s@127.0.0.1/web/servicelistreload?mode=0 >>/dev/null 2>&1 </dev/null &
sleep 2
echo "OK"
exit







