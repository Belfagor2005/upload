#!/bin/sh
echo "stahuji (m3u) Czech"
echo ""
echo ""
[ -d /IPTV ] || mkdir -p /IPTV
rm -rf /IPTV
[ -d /IPTV ] || mkdir -p /IPTV
[ -d /tmp/test ] || mkdir -p /tmp/test
[ -d /IPTV/CZ ] || mkdir -p /IPTV/CZ
echo "Stahování Czech.m3u"
echo "Downloading Czech.m3u"
[ -d /tmp/test ] || mkdir -p /tmp/test
[ -d /IPTV/CZ ] || mkdir -p /IPTV/CZ
curl  -k -Lbk -A -k -m 8 -m 52 -s  https://iptvcat.com/czech_republic > /tmp/test/CCcam
cd /tmp/test
grep -o -i 'data-clipboard-text=[^<]*' CCcam > iptv
grep -o '"\([^"]*\)com.*' iptv > iptvl
sed -ne 's#.*"\([^<]*\)".*#\1#p' iptvl > iptv2
sort iptv2 | uniq > iptv3

OUTPUT2='/IPTV/CZ/CZ.m3u'
echo -n "Converting ....."
FS=" "      
cat iptv3 |grep -i "^http:.*"|while read line ; do
F1=$(echo $line|cut -d"$FS" -f1)
SERVER=$(echo $line|cut -d"$FS" -f2)
PORT=$(echo $line|cut -d"$FS" -f3)
USER=$(echo $line|cut -d"$FS" -f4)
PASS=$(echo $line|cut -d"$FS" -f5)
#echo "SERVER: $SERVER PORT: $PORT USER: $USER PASS: $PASS"
echo -n "."
echo "#EXTINF:-1,CZ" >> $OUTPUT2
echo "$SERVER" >> $OUTPUT2

done
cd /
rm -rf /tmp/test
[ -d /tmp/test2 ] || mkdir -p /tmp/test2
cp /IPTV/CZ/CZ.m3u /tmp/test2/CZ.m3u
###########################################################################################################
more /usr/lib/enigma2/python/Plugins/Extensions/OpenPanel/DATA/x  >> /etc/enigma2/bouquets.tv 
sed -i "s/%/userbouquet.Czech.m3u.tv/" /etc/enigma2/bouquets.tv 
[ -d /tmp/test ] || mkdir -p /tmp/test
cp /tmp/test2/CZ.m3u /tmp/test/x.m3u
echo ""
echo "converter Czech.m3u for Enigma"
sleep 1
echo "start"
sed '1,1d' /tmp/test/x.m3u > /tmp/test/Rus.m3u
sed -e "s/#EXTINF:-1,/#DESCRIPTION /" /tmp/test/Rus.m3u > /tmp/test/Rus5.m3u
sed -e "s/, / /" /tmp/test/Rus5.m3u > /tmp/test/Rus6.m3u
sed 's/:/%3a/g' /tmp/test/Rus6.m3u > /tmp/test/Rus7.m3u
sed -e "s/http/#SERVICE 4097:0:1128:0:0:0:0:0:0:0:http/" /tmp/test/Rus7.m3u > /tmp/test/Rus8.m3u
sed -e "s/rtmp/#SERVICE 4097:0:1128:0:0:0:0:0:0:0:rtmp/" /tmp/test/Rus8.m3u > /tmp/test/Rus8a.m3u
sed -e "s/mmsh/#SERVICE 4097:0:1128:0:0:0:0:0:0:0:mmsh/" /tmp/test/Rus8a.m3u > /tmp/test/Rus8b.m3u
awk '{print NR " " $0}' /tmp/test/Rus8b.m3u  > /tmp/test/Rus9.m3u
sort -n -r "/tmp/test/Rus9.m3u"|grep -o -i '#[^<]*' > /tmp/test/Rus10.m3u
echo "#NAME Czech.m3u" > /etc/enigma2/userbouquet.Czech.m3u.tv
cat /tmp/test/Rus10.m3u >> /etc/enigma2/userbouquet.Czech.m3u.tv
rm -rf /tmp/test
cd /
rm -rf /tmp/test2
###########################################################################################################
echo "stahuji Czech m3u"

echo ""
echo ""
[ -d /tmp/test ] || mkdir -p /tmp/test
[ -d /tmp/testx ] || mkdir -p /tmp/testx

curl -k -A -k -s  https://www.dailyiptvlist.com/european-m3u-iptv/czechia/ > /tmp/test/strana
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
grep -o -i 'https://dailyiptvlist.com/dl/cz[^<]*' adresa > adresa1
tr -d '\r\032' <adresa1 >unix.txt
sed -n '1,3p' unix.txt > adresa4
echo -n "curl  -k -Lbk -m 6 -m 22 -s " > /tmp/test2/skript
sed -n '1,1p' adresa4 >> skript
echo -n " > /tmp/testx/CZtv1.m3u" >> skript
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
echo -n " > /tmp/testx/CZtv2.m3u" >> skript
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
echo -n " > /tmp/testx/CZtv3.m3u" >> skript
cat skript | tr -d '\n' > skriptx
mv /tmp/test4/skriptx skript.sh
chmod 755 /tmp/test4/skript.sh
/tmp/test4/skript.sh

cd /
rm -rf /tmp/test4

###########################################################################################################
more /usr/lib/enigma2/python/Plugins/Extensions/OpenPanel/DATA/x  >> /etc/enigma2/bouquets.tv 
sed -i "s/%/userbouquet.Czech1.m3u.tv/" /etc/enigma2/bouquets.tv 
[ -d /tmp/test ] || mkdir -p /tmp/test
cp /tmp/testx/CZtv1.m3u /tmp/test/x.m3u
echo ""
echo "converter Czech1.m3u for Enigma"
sleep 1
echo "start"
sed '1,1d' /tmp/test/x.m3u > /tmp/test/Rus.m3u
sed -e "s/#EXTINF:-1,/#DESCRIPTION /" /tmp/test/Rus.m3u > /tmp/test/Rus5.m3u
sed -e "s/CZ:/CZ /" /tmp/test/Rus5.m3u > /tmp/test/Rus6.m3u
sed 's/:/%3a/g' /tmp/test/Rus6.m3u > /tmp/test/Rus7.m3u
sed -e "s/http/#SERVICE 4097:0:1128:0:0:0:0:0:0:0:http/" /tmp/test/Rus7.m3u > /tmp/test/Rus8.m3u
sed -e "s/rtmp/#SERVICE 4097:0:1128:0:0:0:0:0:0:0:rtmp/" /tmp/test/Rus8.m3u > /tmp/test/Rus8a.m3u
sed -e "s/mmsh/#SERVICE 4097:0:1128:0:0:0:0:0:0:0:mmsh/" /tmp/test/Rus8a.m3u > /tmp/test/Rus8b.m3u
awk '{print NR " " $0}' /tmp/test/Rus8b.m3u  > /tmp/test/Rus9.m3u
sort -n -r "/tmp/test/Rus9.m3u"|grep -o -i '#[^<]*' > /tmp/test/Rus10.m3u
echo "#NAME Czech1.m3u" > /etc/enigma2/userbouquet.Czech1.m3u.tv
cat /tmp/test/Rus10.m3u >> /etc/enigma2/userbouquet.Czech1.m3u.tv
rm -rf /tmp/test
###########################################################################################################
more /usr/lib/enigma2/python/Plugins/Extensions/OpenPanel/DATA/x  >> /etc/enigma2/bouquets.tv 
sed -i "s/%/userbouquet.Czech2.m3u.tv/" /etc/enigma2/bouquets.tv 
[ -d /tmp/test ] || mkdir -p /tmp/test
cp /tmp/testx/CZtv2.m3u /tmp/test/x.m3u
echo ""
echo "converter Czech2.m3u for Enigma"
sleep 1
echo "start"
sed '1,1d' /tmp/test/x.m3u > /tmp/test/Rus.m3u
sed -e "s/#EXTINF:-1,/#DESCRIPTION /" /tmp/test/Rus.m3u > /tmp/test/Rus5.m3u
sed -e "s/CZ:/CZ /" /tmp/test/Rus5.m3u > /tmp/test/Rus6.m3u
sed 's/:/%3a/g' /tmp/test/Rus6.m3u > /tmp/test/Rus7.m3u
sed -e "s/http/#SERVICE 4097:0:1128:0:0:0:0:0:0:0:http/" /tmp/test/Rus7.m3u > /tmp/test/Rus8.m3u
sed -e "s/rtmp/#SERVICE 4097:0:1128:0:0:0:0:0:0:0:rtmp/" /tmp/test/Rus8.m3u > /tmp/test/Rus8a.m3u
sed -e "s/mmsh/#SERVICE 4097:0:1128:0:0:0:0:0:0:0:mmsh/" /tmp/test/Rus8a.m3u > /tmp/test/Rus8b.m3u
awk '{print NR " " $0}' /tmp/test/Rus8b.m3u  > /tmp/test/Rus9.m3u
sort -n -r "/tmp/test/Rus9.m3u"|grep -o -i '#[^<]*' > /tmp/test/Rus10.m3u
echo "#NAME Czech2.m3u" > /etc/enigma2/userbouquet.Czech2.m3u.tv
cat /tmp/test/Rus10.m3u >> /etc/enigma2/userbouquet.Czech2.m3u.tv
rm -rf /tmp/test
###########################################################################################################
more /usr/lib/enigma2/python/Plugins/Extensions/OpenPanel/DATA/x  >> /etc/enigma2/bouquets.tv 
sed -i "s/%/userbouquet.Czech3.m3u.tv/" /etc/enigma2/bouquets.tv 
[ -d /tmp/test ] || mkdir -p /tmp/test
cp /tmp/testx/CZtv3.m3u /tmp/test/x.m3u
echo ""
echo "converter Czech3.m3u for Enigma"
sleep 1
echo "start"
sed '1,1d' /tmp/test/x.m3u > /tmp/test/Rus.m3u
sed -e "s/#EXTINF:-1,/#DESCRIPTION /" /tmp/test/Rus.m3u > /tmp/test/Rus5.m3u
sed -e "s/CZ:/CZ /" /tmp/test/Rus5.m3u > /tmp/test/Rus6.m3u
sed 's/:/%3a/g' /tmp/test/Rus6.m3u > /tmp/test/Rus7.m3u
sed 's/%3a / /g' /tmp/test/Rus7.m3u > /tmp/test/Rus7a.m3u
sed -e "s/http/#SERVICE 4097:0:1128:0:0:0:0:0:0:0:http/" /tmp/test/Rus7a.m3u > /tmp/test/Rus8.m3u
sed -e "s/mmsh/#SERVICE 4097:0:1128:0:0:0:0:0:0:0:mmsh/" /tmp/test/Rus8.m3u > /tmp/test/Rus8b.m3u
awk '{print NR " " $0}' /tmp/test/Rus8b.m3u  > /tmp/test/Rus9.m3u
sort -n -r "/tmp/test/Rus9.m3u"|grep -o -i '#[^<]*' > /tmp/test/Rus10.m3u
echo "#NAME Czech3.m3u" > /etc/enigma2/userbouquet.Czech3.m3u.tv
cat /tmp/test/Rus10.m3u >> /etc/enigma2/userbouquet.Czech3.m3u.tv
rm -rf /tmp/test
rm -rf /tmp/testx
###########################################################################################################
echo "stahuji seznam CZ SK TV+Rádio"
echo ""
echo "bude staženo jako m3u"
echo ""
[ -d /movie ] || mkdir -p /movie

curl -k -A -k -s http://database.freetuxtv.net/playlists/playlist_webtv_cs.m3u > /movie/CZtv.m3u
curl -k -A -k -s http://database.freetuxtv.net/playlists/playlist_webradio_cs.m3u > /movie/CZrádio.m3u
curl -k -A -k -s http://database.freetuxtv.net/playlists/playlist_webtv_sk.m3u > /movie/SKtv.m3u
curl -k -A -k -s http://database.freetuxtv.net/playlists/playlist_webradio_sk.m3u > /movie/SKrádio.m3u
###########################################################################################################
more /usr/lib/enigma2/python/Plugins/Extensions/OpenPanel/DATA/x  >> /etc/enigma2/bouquets.tv 
sed -i "s/%/userbouquet.Czech4.m3u.tv/" /etc/enigma2/bouquets.tv 
[ -d /tmp/test ] || mkdir -p /tmp/test
cp /movie/CZtv.m3u /tmp/test/x.m3u
echo ""
echo "converter Czech4.m3u for Enigma"
sleep 1
echo "start"
sed '1,1d' /tmp/test/x.m3u > /tmp/test/Rus.m3u
sed -e "s/#EXTINF/#DESCRIPTION /" /tmp/test/Rus.m3u > /tmp/test/Rus5.m3u
sed -e "s/:0,/ /" /tmp/test/Rus5.m3u > /tmp/test/Rus6.m3u
sed 's/:/%3a/g' /tmp/test/Rus6.m3u > /tmp/test/Rus7.m3u
sed -e "s/http/#SERVICE 4097:0:1128:0:0:0:0:0:0:0:http/" /tmp/test/Rus7.m3u > /tmp/test/Rus8.m3u
sed -e "s/rtmp/#SERVICE 4097:0:1128:0:0:0:0:0:0:0:rtmp/" /tmp/test/Rus8.m3u > /tmp/test/Rus8a.m3u
sed -e "s/mmsh/#SERVICE 4097:0:1128:0:0:0:0:0:0:0:mmsh/" /tmp/test/Rus8a.m3u > /tmp/test/Rus8b.m3u
awk '{print NR " " $0}' /tmp/test/Rus8b.m3u  > /tmp/test/Rus9.m3u
sort -n -r "/tmp/test/Rus9.m3u"|grep -o -i '#[^<]*' > /tmp/test/Rus10.m3u
echo "#NAME Czech4.m3u" > /etc/enigma2/userbouquet.Czech4.m3u.tv
cat /tmp/test/Rus10.m3u >> /etc/enigma2/userbouquet.Czech4.m3u.tv
rm -rf /tmp/test
###########################################################################################################
more /usr/lib/enigma2/python/Plugins/Extensions/OpenPanel/DATA/x  >> /etc/enigma2/bouquets.tv 
sed -i "s/%/userbouquet.CzechRÁDIO.m3u.tv/" /etc/enigma2/bouquets.tv 
[ -d /tmp/test ] || mkdir -p /tmp/test
cp /movie/CZrádio.m3u /tmp/test/x.m3u
echo ""
echo "converter CzechRÁDIO.m3u for Enigma"
sleep 1
echo "start"
sed '1,1d' /tmp/test/x.m3u > /tmp/test/Rus.m3u
sed -e "s/#EXTINF/#DESCRIPTION /" /tmp/test/Rus.m3u > /tmp/test/Rus5.m3u
sed -e "s/:0,/ /" /tmp/test/Rus5.m3u > /tmp/test/Rus6.m3u
sed 's/:/%3a/g' /tmp/test/Rus6.m3u > /tmp/test/Rus7.m3u
sed -e "s/http/#SERVICE 4097:0:1128:0:0:0:0:0:0:0:http/" /tmp/test/Rus7.m3u > /tmp/test/Rus8.m3u
sed -e "s/rtmp/#SERVICE 4097:0:1128:0:0:0:0:0:0:0:rtmp/" /tmp/test/Rus8.m3u > /tmp/test/Rus8a.m3u
sed -e "s/mmsh/#SERVICE 4097:0:1128:0:0:0:0:0:0:0:mmsh/" /tmp/test/Rus8a.m3u > /tmp/test/Rus8b.m3u
awk '{print NR " " $0}' /tmp/test/Rus8b.m3u  > /tmp/test/Rus9.m3u
sort -n -r "/tmp/test/Rus9.m3u"|grep -o -i '#[^<]*' > /tmp/test/Rus10.m3u
echo "#NAME CzechRÁDIO.m3u" > /etc/enigma2/userbouquet.CzechRÁDIO.m3u.tv
cat /tmp/test/Rus10.m3u >> /etc/enigma2/userbouquet.CzechRÁDIO.m3u.tv
rm -rf /tmp/test
###########################################################################################################
more /usr/lib/enigma2/python/Plugins/Extensions/OpenPanel/DATA/x  >> /etc/enigma2/bouquets.tv 
sed -i "s/%/userbouquet.SKtv.m3u.tv/" /etc/enigma2/bouquets.tv 
[ -d /tmp/test ] || mkdir -p /tmp/test
cp /movie/SKtv.m3u /tmp/test/x.m3u
echo ""
echo "converter SKtv.m3u for Enigma"
sleep 1
echo "start"
sed '1,1d' /tmp/test/x.m3u > /tmp/test/Rus.m3u
sed -e "s/#EXTINF/#DESCRIPTION /" /tmp/test/Rus.m3u > /tmp/test/Rus5.m3u
sed -e "s/:0,/ /" /tmp/test/Rus5.m3u > /tmp/test/Rus6.m3u
sed 's/:/%3a/g' /tmp/test/Rus6.m3u > /tmp/test/Rus7.m3u
sed -e "s/http/#SERVICE 4097:0:1128:0:0:0:0:0:0:0:http/" /tmp/test/Rus7.m3u > /tmp/test/Rus8.m3u
sed -e "s/rtmp/#SERVICE 4097:0:1128:0:0:0:0:0:0:0:rtmp/" /tmp/test/Rus8.m3u > /tmp/test/Rus8a.m3u
sed -e "s/mmsh/#SERVICE 4097:0:1128:0:0:0:0:0:0:0:mmsh/" /tmp/test/Rus8a.m3u > /tmp/test/Rus8b.m3u
awk '{print NR " " $0}' /tmp/test/Rus8b.m3u  > /tmp/test/Rus9.m3u
sort -n -r "/tmp/test/Rus9.m3u"|grep -o -i '#[^<]*' > /tmp/test/Rus10.m3u
echo "#NAME SKtv.m3u" > /etc/enigma2/userbouquet.SKtv.m3u.tv
cat /tmp/test/Rus10.m3u >> /etc/enigma2/userbouquet.SKtv.m3u.tv
rm -rf /tmp/test
###########################################################################################################
more /usr/lib/enigma2/python/Plugins/Extensions/OpenPanel/DATA/x  >> /etc/enigma2/bouquets.tv 
sed -i "s/%/userbouquet.SkRÁDIO.m3u.tv/" /etc/enigma2/bouquets.tv 
[ -d /tmp/test ] || mkdir -p /tmp/test
cp /movie/SKrádio.m3u /tmp/test/x.m3u
echo ""
echo "converter SkRÁDIO.m3u for Enigma"
sleep 1
echo "start"
sed '1,1d' /tmp/test/x.m3u > /tmp/test/Rus.m3u
sed -e "s/#EXTINF/#DESCRIPTION /" /tmp/test/Rus.m3u > /tmp/test/Rus5.m3u
sed -e "s/:0,/ /" /tmp/test/Rus5.m3u > /tmp/test/Rus6.m3u
sed 's/:/%3a/g' /tmp/test/Rus6.m3u > /tmp/test/Rus7.m3u
sed -e "s/http/#SERVICE 4097:0:1128:0:0:0:0:0:0:0:http/" /tmp/test/Rus7.m3u > /tmp/test/Rus8.m3u
sed -e "s/rtmp/#SERVICE 4097:0:1128:0:0:0:0:0:0:0:rtmp/" /tmp/test/Rus8.m3u > /tmp/test/Rus8a.m3u
sed -e "s/mmsh/#SERVICE 4097:0:1128:0:0:0:0:0:0:0:mmsh/" /tmp/test/Rus8a.m3u > /tmp/test/Rus8b.m3u
awk '{print NR " " $0}' /tmp/test/Rus8b.m3u  > /tmp/test/Rus9.m3u
sort -n -r "/tmp/test/Rus9.m3u"|grep -o -i '#[^<]*' > /tmp/test/Rus10.m3u
echo "#NAME SkRÁDIO.m3u" > /etc/enigma2/userbouquet.SkRÁDIO.m3u.tv
cat /tmp/test/Rus10.m3u >> /etc/enigma2/userbouquet.SkRÁDIO.m3u.tv
rm -rf /tmp/test
###########################################################################################################
wget -q -O - http://root%s@127.0.0.1/web/servicelistreload?mode=0 >>/dev/null 2>&1 </dev/null &
sleep 2
echo "OK"
exit







