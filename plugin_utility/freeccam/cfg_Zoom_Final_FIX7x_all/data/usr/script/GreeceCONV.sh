#!/bin/sh
echo "stahuji (m3u) Greek"
echo ""
echo ""
[ -d /IPTV ] || mkdir -p /IPTV
rm -rf /IPTV
[ -d /IPTV ] || mkdir -p /IPTV
[ -d /tmp/test ] || mkdir -p /tmp/test
[ -d /IPTV/GR ] || mkdir -p /IPTV/GR
echo "Stahování Greek.m3u"
echo "Downloading Greek.m3u"
[ -d /tmp/test ] || mkdir -p /tmp/test
[ -d /IPTV/GR ] || mkdir -p /IPTV/GR

###########################################################################################################
echo "stahuji Greek m3u"

echo ""
echo ""
[ -d /tmp/test ] || mkdir -p /tmp/test
[ -d /tmp/testx ] || mkdir -p /tmp/testx

curl -k -A -k -s  https://www.dailyiptvlist.com/european-m3u-iptv/greece-greek/ > /tmp/test/strana
chmod 644 /tmp/test/strana

cd /tmp/test
sed -n '368,368p' strana > strana1
sed 's/\(["]\+\)/\n\1/g' strana1 > strana2
sed -n '2,2p' strana2 > strana3
tr -d '["]' < "strana3" > strana4
echo "curl -k -A -k -s " > /tmp/test/skript
more strana4 >> /tmp/test/skript
cat skript | tr -d '\n' > skript1
echo " > /tmp/test/adresa" >> /tmp/test/skript1
cat skript1 | tr -d '\n' > skript2
mv /tmp/test/skript2 skript.sh
chmod 755 /tmp/test/skript.sh
/tmp/test/skript.sh
[ -d /tmp/test2 ] || mkdir -p /tmp/test2
cp adresa /tmp/test2/adresa
cd /
rm -rf /tmp/test
cd /tmp/test2
grep -o -i 'https://dailyiptvlist.com/dl/gr[^<]*' adresa > adresa1
tr -d '\r\032' <adresa1 >unix.txt
sed -n '1,3p' unix.txt > adresa4
echo -n "curl  -k -Lbk -m 6 -m 22 -s " > /tmp/test2/skript
sed -n '1,1p' adresa4 >> skript
echo -n " > /tmp/testx/GRtv1.m3u" >> skript
cat skript | tr -d '\n' > skriptx
mv /tmp/test2/skriptx skript.sh
chmod 755 /tmp/test2/skript.sh
/tmp/test2/skript.sh
[ -d /tmp/test3 ] || mkdir -p /tmp/test3
cp adresa4 /tmp/test3/adresa4
cd /
rm -rf /tmp/test2
cd /tmp/test3
echo -n "curl  -k -Lbk -m 6 -m 22 -s " > /tmp/test3/skript
sed -n '2,2p' adresa4 >> skript
echo -n " > /tmp/testx/GRtv2.m3u" >> skript
cat skript | tr -d '\n' > skriptx
mv /tmp/test3/skriptx skript.sh
chmod 755 /tmp/test3/skript.sh
/tmp/test3/skript.sh
[ -d /tmp/test4 ] || mkdir -p /tmp/test4
cp adresa4 /tmp/test4/adresa4
cd /
rm -rf /tmp/test3
cd /tmp/test4
echo -n "curl  -k -Lbk -m 6 -m 22 -s " > /tmp/test4/skript
sed -n '3,3p' adresa4 >> skript
echo -n " > /tmp/testx/GRtv3.m3u" >> skript
cat skript | tr -d '\n' > skriptx
mv /tmp/test4/skriptx skript.sh
chmod 755 /tmp/test4/skript.sh
/tmp/test4/skript.sh

cd /
cp /tmp/testx/GRtv1.m3u /IPTV/GR/GRtv1.m3u
cp /tmp/testx/GRtv2.m3u /IPTV/GR/GRtv2.m3u
cp /tmp/testx/GRtv3.m3u /IPTV/GR/GRtv3.m3u
rm -rf /tmp/test4
###########################################################################################################
more /usr/lib/enigma2/python/Plugins/Extensions/OpenPanel/DATA/x  >> /etc/enigma2/bouquets.tv 
sed -i "s/%/userbouquet.Greek1.m3u.tv/" /etc/enigma2/bouquets.tv 
[ -d /tmp/test ] || mkdir -p /tmp/test
cp /tmp/testx/GRtv1.m3u /tmp/test/x.m3u
echo ""
echo "converter Greek1.m3u for Enigma"
sleep 1
echo "start"
sed '1,1d' /tmp/test/x.m3u > /tmp/test/Rus.m3u
sed -e "s/#EXTINF:-1,/#DESCRIPTION /" /tmp/test/Rus.m3u > /tmp/test/Rus5.m3u
sed -e "s/CZ:/CZ /" /tmp/test/Rus5.m3u > /tmp/test/Rus6.m3u
sed 's/:/%3a/g' /tmp/test/Rus6.m3u > /tmp/test/Rus6c.m3u
sed 's/%3a / /g' /tmp/test/Rus6c.m3u > /tmp/test/Rus6d.m3u
sed 's/ %3a/ /g' /tmp/test/Rus6d.m3u > /tmp/test/Rus7.m3u
sed -e "s/http/#SERVICE 4097:0:1128:0:0:0:0:0:0:0:http/" /tmp/test/Rus7.m3u > /tmp/test/Rus8.m3u
sed -e "s/rtmp/#SERVICE 4097:0:1128:0:0:0:0:0:0:0:rtmp/" /tmp/test/Rus8.m3u > /tmp/test/Rus8a.m3u
sed -e "s/mmsh/#SERVICE 4097:0:1128:0:0:0:0:0:0:0:mmsh/" /tmp/test/Rus8a.m3u > /tmp/test/Rus8b.m3u
awk '{print NR " " $0}' /tmp/test/Rus8b.m3u  > /tmp/test/Rus9.m3u
sort -n -r "/tmp/test/Rus9.m3u"|grep -o -i '#[^<]*' > /tmp/test/Rus10.m3u
echo "#NAME Greek1.m3u" > /etc/enigma2/userbouquet.Greek1.m3u.tv
cat /tmp/test/Rus10.m3u >> /etc/enigma2/userbouquet.Greek1.m3u.tv
rm -rf /tmp/test
###########################################################################################################
more /usr/lib/enigma2/python/Plugins/Extensions/OpenPanel/DATA/x  >> /etc/enigma2/bouquets.tv 
sed -i "s/%/userbouquet.Greek2.m3u.tv/" /etc/enigma2/bouquets.tv 
[ -d /tmp/test ] || mkdir -p /tmp/test
cp /tmp/testx/GRtv2.m3u /tmp/test/x.m3u
echo ""
echo "converter Greek2.m3u for Enigma"
sleep 1
echo "start"
sed '1,1d' /tmp/test/x.m3u > /tmp/test/Rus.m3u
sed -e "s/#EXTINF:-1,/#DESCRIPTION /" /tmp/test/Rus.m3u > /tmp/test/Rus5.m3u
sed -e "s/CZ:/CZ /" /tmp/test/Rus5.m3u > /tmp/test/Rus6.m3u
sed 's/:/%3a/g' /tmp/test/Rus6.m3u > /tmp/test/Rus6c.m3u
sed 's/%3a / /g' /tmp/test/Rus6c.m3u > /tmp/test/Rus6d.m3u
sed 's/ %3a/ /g' /tmp/test/Rus6d.m3u > /tmp/test/Rus6e.m3u
sed '/#DESCRIPTION/s/%3a/ /g' /tmp/test/Rus6e.m3u > /tmp/test/Rus7.m3u
sed -e "s/http/#SERVICE 4097:0:1128:0:0:0:0:0:0:0:http/" /tmp/test/Rus7.m3u > /tmp/test/Rus8.m3u
sed -e "s/rtmp/#SERVICE 4097:0:1128:0:0:0:0:0:0:0:rtmp/" /tmp/test/Rus8.m3u > /tmp/test/Rus8a.m3u
sed -e "s/mmsh/#SERVICE 4097:0:1128:0:0:0:0:0:0:0:mmsh/" /tmp/test/Rus8a.m3u > /tmp/test/Rus8b.m3u
awk '{print NR " " $0}' /tmp/test/Rus8b.m3u  > /tmp/test/Rus9.m3u
sort -n -r "/tmp/test/Rus9.m3u"|grep -o -i '#[^<]*' > /tmp/test/Rus10.m3u
echo "#NAME Greek2.m3u" > /etc/enigma2/userbouquet.Greek2.m3u.tv
cat /tmp/test/Rus10.m3u >> /etc/enigma2/userbouquet.Greek2.m3u.tv
rm -rf /tmp/test
###########################################################################################################
more /usr/lib/enigma2/python/Plugins/Extensions/OpenPanel/DATA/x  >> /etc/enigma2/bouquets.tv 
sed -i "s/%/userbouquet.Greek3.m3u.tv/" /etc/enigma2/bouquets.tv 
[ -d /tmp/test ] || mkdir -p /tmp/test
cp /tmp/testx/GRtv3.m3u /tmp/test/x.m3u
echo ""
echo "converter Greek3.m3u for Enigma"
sleep 1
echo "start"
sed '1,1d' /tmp/test/x.m3u > /tmp/test/Rus.m3u
sed -e "s/#EXTINF:-1,/#DESCRIPTION /" /tmp/test/Rus.m3u > /tmp/test/Rus5.m3u
sed -e "s/CZ:/CZ /" /tmp/test/Rus5.m3u > /tmp/test/Rus6.m3u
sed 's/:/%3a/g' /tmp/test/Rus6.m3u > /tmp/test/Rus6c.m3u
sed 's/%3a / /g' /tmp/test/Rus6c.m3u > /tmp/test/Rus6d.m3u
sed 's/ %3a/ /g' /tmp/test/Rus6d.m3u > /tmp/test/Rus7.m3u
sed -e "s/http/#SERVICE 4097:0:1128:0:0:0:0:0:0:0:http/" /tmp/test/Rus7.m3u > /tmp/test/Rus8.m3u
sed -e "s/rtmp/#SERVICE 4097:0:1128:0:0:0:0:0:0:0:rtmp/" /tmp/test/Rus8.m3u > /tmp/test/Rus8a.m3u
sed -e "s/mmsh/#SERVICE 4097:0:1128:0:0:0:0:0:0:0:mmsh/" /tmp/test/Rus8a.m3u > /tmp/test/Rus8b.m3u
awk '{print NR " " $0}' /tmp/test/Rus8b.m3u  > /tmp/test/Rus9.m3u
sort -n -r "/tmp/test/Rus9.m3u"|grep -o -i '#[^<]*' > /tmp/test/Rus10.m3u
echo "#NAME Greek3.m3u" > /etc/enigma2/userbouquet.Greek3.m3u.tv
cat /tmp/test/Rus10.m3u >> /etc/enigma2/userbouquet.Greek3.m3u.tv
rm -rf /tmp/test
rm -rf /tmp/testx
###########################################################################################################


wget -q -O - http://root%s@127.0.0.1/web/servicelistreload?mode=0 >>/dev/null 2>&1 </dev/null &
sleep 2
echo "OK"
exit







