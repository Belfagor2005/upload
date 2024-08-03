#!/bin/sh
echo "stahuji (m3u) Smart"
echo ""
echo ""
[ -d /IPTV ] || mkdir -p /IPTV
rm -rf /IPTV
[ -d /IPTV ] || mkdir -p /IPTV
[ -d /tmp/test ] || mkdir -p /tmp/test
echo "Stahování Smart.m3u"
echo "Downloading Smart.m3u"
curl  -k -Lbk -A -k -m 8 -m 52 -s  https://cccam4all.net/category/iptv/ > /tmp/test/CCcam
cd /tmp/test
grep -o -i 'https://cccam4all.net/iptv-providers-romania-m3u-liste-unlimited[^<]*' CCcam > CCcam1
sed -n '1,1p' CCcam1 > CCcam2
adresa=`cut -d'"' -f 1 CCcam2`
adresa=$adresa
curl  -k -Lbk -A -k -m 8 -m 52 -s $adresa > /tmp/test/iptv
grep -o '"\([^"]*\)zip.*' iptv > iptvl
sed -ne 's#.*"\([^<]*\)".*#\1#p' iptvl > iptv2
adresa1=`tail -n 1 iptv2`
adresa1=$adresa1
curl  -k -Lbk -A -k -m 8 -m 52 -s  $adresa1 > /tmp/test/x.zip
unzip  x.zip -d  /IPTV
cd /
rm -rf /tmp/test
[ -d /tmp/test2 ] || mkdir -p /tmp/test2
find /IPTV -name \*.m3u | xargs -I {} cp {} /tmp/test2
find /IPTV -name \*.m3u8 | xargs -I {} cp {} /tmp/test2
mv -v /tmp/test2/"iptv romania.m3u" /tmp/test2/"a.m3u"
mv -v /tmp/test2/"Romania_1.iptv.m3u8" /tmp/test2/"0.m3u"
mv -v /tmp/test2/"iptv romania (1).m3u" /tmp/test2/"1.m3u"
mv -v /tmp/test2/"iptv romania (2).m3u" /tmp/test2/"2.m3u"
mv -v /tmp/test2/"iptv romania (3).m3u" /tmp/test2/"3.m3u"
mv -v /tmp/test2/"iptv romania (4).m3u" /tmp/test2/"4.m3u"
mv -v /tmp/test2/"iptv romania (5).m3u" /tmp/test2/"5.m3u"
mv -v /tmp/test2/"iptv romania (6).m3u" /tmp/test2/"6.m3u"
mv -v /tmp/test2/"iptv romania (7).m3u" /tmp/test2/"7.m3u"
mv -v /tmp/test2/"iptv romania (8).m3u" /tmp/test2/"8.m3u"
mv -v /tmp/test2/"iptv romania (9).m3u" /tmp/test2/"9.m3u"
mv -v /tmp/test2/"iptv romania (10).m3u" /tmp/test2/"10.m3u"
mv -v /tmp/test2/"iptv romania (11).m3u" /tmp/test2/"11.m3u"
mv -v /tmp/test2/"iptv romania (12).m3u" /tmp/test2/"12.m3u"
mv -v /tmp/test2/"iptv romania (13).m3u" /tmp/test2/"13.m3u"
mv -v /tmp/test2/"iptv romania (14).m3u" /tmp/test2/"14.m3u"
mv -v /tmp/test2/"iptv romania (15).m3u" /tmp/test2/"15.m3u"
mv -v /tmp/test2/"iptv romania (16).m3u" /tmp/test2/"16.m3u"
mv -v /tmp/test2/"iptv romania (17).m3u" /tmp/test2/"17.m3u"
mv -v /tmp/test2/"iptv romania (18).m3u" /tmp/test2/"18.m3u"
###########################################################################################################
more /usr/lib/enigma2/python/Plugins/Extensions/OpenPanel/DATA/x  >> /etc/enigma2/bouquets.tv 
sed -i "s/%/userbouquet.RomaniaA.m3u.tv/" /etc/enigma2/bouquets.tv 
[ -d /tmp/test ] || mkdir -p /tmp/test
cp /tmp/test2/a.m3u /tmp/test/x.m3u
echo ""
echo "converter RomaniaA.m3u for Enigma"
sleep 1
echo "start"
sed '1,1d' /tmp/test/x.m3u > /tmp/test/Rus.m3u
awk 'BEGIN {FS="png"}{print  $NF}'  /tmp/test/Rus.m3u > /tmp/test/Rus3.m3u
awk 'BEGIN {FS="group-"}{print  $NF}'  /tmp/test/Rus3.m3u > /tmp/test/Rus4.m3u
sed 's/",/#DESCRIPTION /g' /tmp/test/Rus4.m3u > /tmp/test/Rus5.m3u
sed 's/#EXTINF/#DESCRIPTION /g' /tmp/test/Rus5.m3u > /tmp/test/Rus6.m3u
sed 's/:-1,/ /g' /tmp/test/Rus6.m3u > /tmp/test/Rus6a.m3u
sed 's/:0,/ /g' /tmp/test/Rus6a.m3u > /tmp/test/Rus6b.m3u
sed 's/: / /g' /tmp/test/Rus6b.m3u > /tmp/test/Rus6c.m3u
sed 's/:/%3a/g' /tmp/test/Rus6c.m3u > /tmp/test/Rus7.m3u
sed -e "s/http/#SERVICE 4097:0:1128:0:0:0:0:0:0:0:http/" /tmp/test/Rus7.m3u > /tmp/test/Rus8.m3u
sed -e "s/rtmp/#SERVICE 4097:0:1128:0:0:0:0:0:0:0:rtmp/" /tmp/test/Rus8.m3u > /tmp/test/Rus8a.m3u
sed -e "s/mmsh/#SERVICE 4097:0:1128:0:0:0:0:0:0:0:mmsh/" /tmp/test/Rus8a.m3u > /tmp/test/Rus8b.m3u
tr -d '["]' < "/tmp/test/Rus8b.m3u" > /tmp/test/Rus8c.m3u
tr -d '[,]' < "/tmp/test/Rus8c.m3u" > /tmp/test/Rus8.m3u
awk '{print NR " " $0}' /tmp/test/Rus8.m3u  > /tmp/test/Rus9.m3u
sort -n -r "/tmp/test/Rus9.m3u"|grep -o -i '#[^<]*' > /tmp/test/Rus10.m3u
echo "#NAME RomaniaA.m3u" > /etc/enigma2/userbouquet.RomaniaA.m3u.tv
cat /tmp/test/Rus10.m3u >> /etc/enigma2/userbouquet.RomaniaA.m3u.tv
rm -rf /tmp/test
cd /

###########################################################################################################
more /usr/lib/enigma2/python/Plugins/Extensions/OpenPanel/DATA/x  >> /etc/enigma2/bouquets.tv 
sed -i "s/%/userbouquet.Romania0.m3u.tv/" /etc/enigma2/bouquets.tv 
[ -d /tmp/test ] || mkdir -p /tmp/test
cp /tmp/test2/0.m3u /tmp/test/x.m3u
echo ""
echo "converter Romania0.m3u for Enigma"
sleep 1
echo "start"
sed '1,1d' /tmp/test/x.m3u > /tmp/test/Rus.m3u
awk 'BEGIN {FS="png"}{print  $NF}'  /tmp/test/Rus.m3u > /tmp/test/Rus3.m3u
awk 'BEGIN {FS="group-"}{print  $NF}'  /tmp/test/Rus3.m3u > /tmp/test/Rus4.m3u
sed 's/",/#DESCRIPTION /g' /tmp/test/Rus4.m3u > /tmp/test/Rus5.m3u
sed 's/#EXTINF/#DESCRIPTION /g' /tmp/test/Rus5.m3u > /tmp/test/Rus6.m3u
sed 's/:-1,/ /g' /tmp/test/Rus6.m3u > /tmp/test/Rus6a.m3u
sed 's/:0,/ /g' /tmp/test/Rus6a.m3u > /tmp/test/Rus6b.m3u
sed 's/: / /g' /tmp/test/Rus6b.m3u > /tmp/test/Rus6c.m3u
sed 's/:/%3a/g' /tmp/test/Rus6c.m3u > /tmp/test/Rus7.m3u
sed -e "s/http/#SERVICE 4097:0:1128:0:0:0:0:0:0:0:http/" /tmp/test/Rus7.m3u > /tmp/test/Rus8.m3u
sed -e "s/rtmp/#SERVICE 4097:0:1128:0:0:0:0:0:0:0:rtmp/" /tmp/test/Rus8.m3u > /tmp/test/Rus8a.m3u
sed -e "s/mmsh/#SERVICE 4097:0:1128:0:0:0:0:0:0:0:mmsh/" /tmp/test/Rus8a.m3u > /tmp/test/Rus8b.m3u
tr -d '["]' < "/tmp/test/Rus8b.m3u" > /tmp/test/Rus8c.m3u
tr -d '[,]' < "/tmp/test/Rus8c.m3u" > /tmp/test/Rus8.m3u
awk '{print NR " " $0}' /tmp/test/Rus8.m3u  > /tmp/test/Rus9.m3u
sort -n -r "/tmp/test/Rus9.m3u"|grep -o -i '#[^<]*' > /tmp/test/Rus10.m3u
echo "#NAME Romania0.m3u" > /etc/enigma2/userbouquet.Romania0.m3u.tv
cat /tmp/test/Rus10.m3u >> /etc/enigma2/userbouquet.Romania0.m3u.tv
rm -rf /tmp/test
cd /
###########################################################################################################
more /usr/lib/enigma2/python/Plugins/Extensions/OpenPanel/DATA/x  >> /etc/enigma2/bouquets.tv 
sed -i "s/%/userbouquet.Romania1.m3u.tv/" /etc/enigma2/bouquets.tv 
[ -d /tmp/test ] || mkdir -p /tmp/test
cp /tmp/test2/1.m3u /tmp/test/x.m3u
echo ""
echo "converter Romania1.m3u for Enigma"
sleep 1
echo "start"
sed '1,1d' /tmp/test/x.m3u > /tmp/test/Rus.m3u
awk 'BEGIN {FS="png"}{print  $NF}'  /tmp/test/Rus.m3u > /tmp/test/Rus3.m3u
awk 'BEGIN {FS="group-"}{print  $NF}'  /tmp/test/Rus3.m3u > /tmp/test/Rus4.m3u
sed 's/",/#DESCRIPTION /g' /tmp/test/Rus4.m3u > /tmp/test/Rus5.m3u
sed 's/#EXTINF/#DESCRIPTION /g' /tmp/test/Rus5.m3u > /tmp/test/Rus6.m3u
sed 's/:-1,/ /g' /tmp/test/Rus6.m3u > /tmp/test/Rus6a.m3u
sed 's/:0,/ /g' /tmp/test/Rus6a.m3u > /tmp/test/Rus6b.m3u
sed 's/: / /g' /tmp/test/Rus6b.m3u > /tmp/test/Rus6c.m3u
sed 's/:/%3a/g' /tmp/test/Rus6c.m3u > /tmp/test/Rus7.m3u
sed -e "s/http/#SERVICE 4097:0:1128:0:0:0:0:0:0:0:http/" /tmp/test/Rus7.m3u > /tmp/test/Rus8.m3u
sed -e "s/rtmp/#SERVICE 4097:0:1128:0:0:0:0:0:0:0:rtmp/" /tmp/test/Rus8.m3u > /tmp/test/Rus8a.m3u
sed -e "s/mmsh/#SERVICE 4097:0:1128:0:0:0:0:0:0:0:mmsh/" /tmp/test/Rus8a.m3u > /tmp/test/Rus8b.m3u
tr -d '["]' < "/tmp/test/Rus8b.m3u" > /tmp/test/Rus8c.m3u
tr -d '[,]' < "/tmp/test/Rus8c.m3u" > /tmp/test/Rus8.m3u
awk '{print NR " " $0}' /tmp/test/Rus8.m3u  > /tmp/test/Rus9.m3u
sort -n -r "/tmp/test/Rus9.m3u"|grep -o -i '#[^<]*' > /tmp/test/Rus10.m3u
echo "#NAME Romania1.m3u" > /etc/enigma2/userbouquet.Romania1.m3u.tv
cat /tmp/test/Rus10.m3u >> /etc/enigma2/userbouquet.Romania1.m3u.tv
rm -rf /tmp/test
cd /
###########################################################################################################
more /usr/lib/enigma2/python/Plugins/Extensions/OpenPanel/DATA/x  >> /etc/enigma2/bouquets.tv 
sed -i "s/%/userbouquet.Romania2.m3u.tv/" /etc/enigma2/bouquets.tv 
[ -d /tmp/test ] || mkdir -p /tmp/test
cp /tmp/test2/2.m3u /tmp/test/x.m3u
echo ""
echo "converter Romania2.m3u for Enigma"
sleep 1
echo "start"
sed '1,1d' /tmp/test/x.m3u > /tmp/test/Rus.m3u
awk 'BEGIN {FS="png"}{print  $NF}'  /tmp/test/Rus.m3u > /tmp/test/Rus3.m3u
awk 'BEGIN {FS="group-"}{print  $NF}'  /tmp/test/Rus3.m3u > /tmp/test/Rus4.m3u
sed 's/",/#DESCRIPTION /g' /tmp/test/Rus4.m3u > /tmp/test/Rus5.m3u
sed 's/#EXTINF/#DESCRIPTION /g' /tmp/test/Rus5.m3u > /tmp/test/Rus6.m3u
sed 's/:-1,/ /g' /tmp/test/Rus6.m3u > /tmp/test/Rus6a.m3u
sed 's/:0,/ /g' /tmp/test/Rus6a.m3u > /tmp/test/Rus6b.m3u
sed 's/: / /g' /tmp/test/Rus6b.m3u > /tmp/test/Rus6c.m3u
sed 's/:/%3a/g' /tmp/test/Rus6c.m3u > /tmp/test/Rus7.m3u
sed -e "s/http/#SERVICE 4097:0:1128:0:0:0:0:0:0:0:http/" /tmp/test/Rus7.m3u > /tmp/test/Rus8.m3u
sed -e "s/rtmp/#SERVICE 4097:0:1128:0:0:0:0:0:0:0:rtmp/" /tmp/test/Rus8.m3u > /tmp/test/Rus8a.m3u
sed -e "s/mmsh/#SERVICE 4097:0:1128:0:0:0:0:0:0:0:mmsh/" /tmp/test/Rus8a.m3u > /tmp/test/Rus8b.m3u
tr -d '["]' < "/tmp/test/Rus8b.m3u" > /tmp/test/Rus8c.m3u
tr -d '[,]' < "/tmp/test/Rus8c.m3u" > /tmp/test/Rus8.m3u
awk '{print NR " " $0}' /tmp/test/Rus8.m3u  > /tmp/test/Rus9.m3u
sort -n -r "/tmp/test/Rus9.m3u"|grep -o -i '#[^<]*' > /tmp/test/Rus10.m3u
echo "#NAME Romania2.m3u" > /etc/enigma2/userbouquet.Romania2.m3u.tv
cat /tmp/test/Rus10.m3u >> /etc/enigma2/userbouquet.Romania2.m3u.tv
rm -rf /tmp/test
cd /
###########################################################################################################
more /usr/lib/enigma2/python/Plugins/Extensions/OpenPanel/DATA/x  >> /etc/enigma2/bouquets.tv 
sed -i "s/%/userbouquet.Romania3.m3u.tv/" /etc/enigma2/bouquets.tv 
[ -d /tmp/test ] || mkdir -p /tmp/test
cp /tmp/test2/3.m3u /tmp/test/x.m3u
echo ""
echo "converter Romania3.m3u for Enigma"
sleep 1
echo "start"
sed '1,1d' /tmp/test/x.m3u > /tmp/test/Rus.m3u
awk 'BEGIN {FS="png"}{print  $NF}'  /tmp/test/Rus.m3u > /tmp/test/Rus3.m3u
awk 'BEGIN {FS="group-"}{print  $NF}'  /tmp/test/Rus3.m3u > /tmp/test/Rus4.m3u
sed 's/",/#DESCRIPTION /g' /tmp/test/Rus4.m3u > /tmp/test/Rus5.m3u
sed 's/#EXTINF/#DESCRIPTION /g' /tmp/test/Rus5.m3u > /tmp/test/Rus6.m3u
sed 's/:-1,/ /g' /tmp/test/Rus6.m3u > /tmp/test/Rus6a.m3u
sed 's/:0,/ /g' /tmp/test/Rus6a.m3u > /tmp/test/Rus6b.m3u
sed 's/: / /g' /tmp/test/Rus6b.m3u > /tmp/test/Rus6c.m3u
sed 's/:/%3a/g' /tmp/test/Rus6c.m3u > /tmp/test/Rus7.m3u
sed -e "s/http/#SERVICE 4097:0:1128:0:0:0:0:0:0:0:http/" /tmp/test/Rus7.m3u > /tmp/test/Rus8.m3u
sed -e "s/rtmp/#SERVICE 4097:0:1128:0:0:0:0:0:0:0:rtmp/" /tmp/test/Rus8.m3u > /tmp/test/Rus8a.m3u
sed -e "s/mmsh/#SERVICE 4097:0:1128:0:0:0:0:0:0:0:mmsh/" /tmp/test/Rus8a.m3u > /tmp/test/Rus8b.m3u
tr -d '["]' < "/tmp/test/Rus8b.m3u" > /tmp/test/Rus8c.m3u
tr -d '[,]' < "/tmp/test/Rus8c.m3u" > /tmp/test/Rus8.m3u
awk '{print NR " " $0}' /tmp/test/Rus8.m3u  > /tmp/test/Rus9.m3u
sort -n -r "/tmp/test/Rus9.m3u"|grep -o -i '#[^<]*' > /tmp/test/Rus10.m3u
echo "#NAME Romania3.m3u" > /etc/enigma2/userbouquet.Romania3.m3u.tv
cat /tmp/test/Rus10.m3u >> /etc/enigma2/userbouquet.Romania3.m3u.tv
rm -rf /tmp/test
cd /
###########################################################################################################
more /usr/lib/enigma2/python/Plugins/Extensions/OpenPanel/DATA/x  >> /etc/enigma2/bouquets.tv 
sed -i "s/%/userbouquet.Romania4.m3u.tv/" /etc/enigma2/bouquets.tv 
[ -d /tmp/test ] || mkdir -p /tmp/test
cp /tmp/test2/4.m3u /tmp/test/x.m3u
echo ""
echo "converter Romania4.m3u for Enigma"
sleep 1
echo "start"
sed '1,1d' /tmp/test/x.m3u > /tmp/test/Rus.m3u
awk 'BEGIN {FS="png"}{print  $NF}'  /tmp/test/Rus.m3u > /tmp/test/Rus3.m3u
awk 'BEGIN {FS="group-"}{print  $NF}'  /tmp/test/Rus3.m3u > /tmp/test/Rus4.m3u
sed 's/",/#DESCRIPTION /g' /tmp/test/Rus4.m3u > /tmp/test/Rus5.m3u
sed 's/#EXTINF/#DESCRIPTION /g' /tmp/test/Rus5.m3u > /tmp/test/Rus6.m3u
sed 's/:-1,/ /g' /tmp/test/Rus6.m3u > /tmp/test/Rus6a.m3u
sed 's/:0,/ /g' /tmp/test/Rus6a.m3u > /tmp/test/Rus6b.m3u
sed 's/: / /g' /tmp/test/Rus6b.m3u > /tmp/test/Rus6c.m3u
sed 's/:/%3a/g' /tmp/test/Rus6c.m3u > /tmp/test/Rus7.m3u
sed -e "s/http/#SERVICE 4097:0:1128:0:0:0:0:0:0:0:http/" /tmp/test/Rus7.m3u > /tmp/test/Rus8.m3u
sed -e "s/rtmp/#SERVICE 4097:0:1128:0:0:0:0:0:0:0:rtmp/" /tmp/test/Rus8.m3u > /tmp/test/Rus8a.m3u
sed -e "s/mmsh/#SERVICE 4097:0:1128:0:0:0:0:0:0:0:mmsh/" /tmp/test/Rus8a.m3u > /tmp/test/Rus8b.m3u
tr -d '["]' < "/tmp/test/Rus8b.m3u" > /tmp/test/Rus8c.m3u
tr -d '[,]' < "/tmp/test/Rus8c.m3u" > /tmp/test/Rus8.m3u
awk '{print NR " " $0}' /tmp/test/Rus8.m3u  > /tmp/test/Rus9.m3u
sort -n -r "/tmp/test/Rus9.m3u"|grep -o -i '#[^<]*' > /tmp/test/Rus10.m3u
echo "#NAME Romania4.m3u" > /etc/enigma2/userbouquet.Romania4.m3u.tv
cat /tmp/test/Rus10.m3u >> /etc/enigma2/userbouquet.Romania4.m3u.tv
rm -rf /tmp/test
cd /
###########################################################################################################
more /usr/lib/enigma2/python/Plugins/Extensions/OpenPanel/DATA/x  >> /etc/enigma2/bouquets.tv 
sed -i "s/%/userbouquet.Romania5.m3u.tv/" /etc/enigma2/bouquets.tv 
[ -d /tmp/test ] || mkdir -p /tmp/test
cp /tmp/test2/5.m3u /tmp/test/x.m3u
echo ""
echo "converter Romania5.m3u for Enigma"
sleep 1
echo "start"
sed '1,1d' /tmp/test/x.m3u > /tmp/test/Rus.m3u
awk 'BEGIN {FS="png"}{print  $NF}'  /tmp/test/Rus.m3u > /tmp/test/Rus3.m3u
awk 'BEGIN {FS="group-"}{print  $NF}'  /tmp/test/Rus3.m3u > /tmp/test/Rus4.m3u
sed 's/",/#DESCRIPTION /g' /tmp/test/Rus4.m3u > /tmp/test/Rus5.m3u
sed 's/#EXTINF/#DESCRIPTION /g' /tmp/test/Rus5.m3u > /tmp/test/Rus6.m3u
sed 's/:-1,/ /g' /tmp/test/Rus6.m3u > /tmp/test/Rus6a.m3u
sed 's/:0,/ /g' /tmp/test/Rus6a.m3u > /tmp/test/Rus6b.m3u
sed 's/: / /g' /tmp/test/Rus6b.m3u > /tmp/test/Rus6c.m3u
sed 's/:/%3a/g' /tmp/test/Rus6c.m3u > /tmp/test/Rus7.m3u
sed -e "s/http/#SERVICE 4097:0:1128:0:0:0:0:0:0:0:http/" /tmp/test/Rus7.m3u > /tmp/test/Rus8.m3u
sed -e "s/rtmp/#SERVICE 4097:0:1128:0:0:0:0:0:0:0:rtmp/" /tmp/test/Rus8.m3u > /tmp/test/Rus8a.m3u
sed -e "s/mmsh/#SERVICE 4097:0:1128:0:0:0:0:0:0:0:mmsh/" /tmp/test/Rus8a.m3u > /tmp/test/Rus8b.m3u
tr -d '["]' < "/tmp/test/Rus8b.m3u" > /tmp/test/Rus8c.m3u
tr -d '[,]' < "/tmp/test/Rus8c.m3u" > /tmp/test/Rus8.m3u
awk '{print NR " " $0}' /tmp/test/Rus8.m3u  > /tmp/test/Rus9.m3u
sort -n -r "/tmp/test/Rus9.m3u"|grep -o -i '#[^<]*' > /tmp/test/Rus10.m3u
echo "#NAME Romania5.m3u" > /etc/enigma2/userbouquet.Romania5.m3u.tv
cat /tmp/test/Rus10.m3u >> /etc/enigma2/userbouquet.Romania5.m3u.tv
rm -rf /tmp/test
cd /
###########################################################################################################
more /usr/lib/enigma2/python/Plugins/Extensions/OpenPanel/DATA/x  >> /etc/enigma2/bouquets.tv 
sed -i "s/%/userbouquet.Romania6.m3u.tv/" /etc/enigma2/bouquets.tv 
[ -d /tmp/test ] || mkdir -p /tmp/test
cp /tmp/test2/6.m3u /tmp/test/x.m3u
echo ""
echo "converter Romania6.m3u for Enigma"
sleep 1
echo "start"
sed '1,1d' /tmp/test/x.m3u > /tmp/test/Rus.m3u
awk 'BEGIN {FS="png"}{print  $NF}'  /tmp/test/Rus.m3u > /tmp/test/Rus3.m3u
awk 'BEGIN {FS="group-"}{print  $NF}'  /tmp/test/Rus3.m3u > /tmp/test/Rus4.m3u
sed 's/",/#DESCRIPTION /g' /tmp/test/Rus4.m3u > /tmp/test/Rus5.m3u
sed 's/#EXTINF/#DESCRIPTION /g' /tmp/test/Rus5.m3u > /tmp/test/Rus6.m3u
sed 's/:-1,/ /g' /tmp/test/Rus6.m3u > /tmp/test/Rus6a.m3u
sed 's/:0,/ /g' /tmp/test/Rus6a.m3u > /tmp/test/Rus6b.m3u
sed 's/: / /g' /tmp/test/Rus6b.m3u > /tmp/test/Rus6c.m3u
sed 's/:/%3a/g' /tmp/test/Rus6c.m3u > /tmp/test/Rus7.m3u
sed -e "s/http/#SERVICE 4097:0:1128:0:0:0:0:0:0:0:http/" /tmp/test/Rus7.m3u > /tmp/test/Rus8.m3u
sed -e "s/rtmp/#SERVICE 4097:0:1128:0:0:0:0:0:0:0:rtmp/" /tmp/test/Rus8.m3u > /tmp/test/Rus8a.m3u
sed -e "s/mmsh/#SERVICE 4097:0:1128:0:0:0:0:0:0:0:mmsh/" /tmp/test/Rus8a.m3u > /tmp/test/Rus8b.m3u
tr -d '["]' < "/tmp/test/Rus8b.m3u" > /tmp/test/Rus8c.m3u
tr -d '[,]' < "/tmp/test/Rus8c.m3u" > /tmp/test/Rus8.m3u
awk '{print NR " " $0}' /tmp/test/Rus8.m3u  > /tmp/test/Rus9.m3u
sort -n -r "/tmp/test/Rus9.m3u"|grep -o -i '#[^<]*' > /tmp/test/Rus10.m3u
echo "#NAME Romania6.m3u" > /etc/enigma2/userbouquet.Romania6.m3u.tv
cat /tmp/test/Rus10.m3u >> /etc/enigma2/userbouquet.Romania6.m3u.tv
rm -rf /tmp/test
cd /
###########################################################################################################
more /usr/lib/enigma2/python/Plugins/Extensions/OpenPanel/DATA/x  >> /etc/enigma2/bouquets.tv 
sed -i "s/%/userbouquet.Romania7.m3u.tv/" /etc/enigma2/bouquets.tv 
[ -d /tmp/test ] || mkdir -p /tmp/test
cp /tmp/test2/7.m3u /tmp/test/x.m3u
echo ""
echo "converter Romania7.m3u for Enigma"
sleep 1
echo "start"
sed '1,1d' /tmp/test/x.m3u > /tmp/test/Rus.m3u
awk 'BEGIN {FS="png"}{print  $NF}'  /tmp/test/Rus.m3u > /tmp/test/Rus3.m3u
awk 'BEGIN {FS="group-"}{print  $NF}'  /tmp/test/Rus3.m3u > /tmp/test/Rus4.m3u
sed 's/",/#DESCRIPTION /g' /tmp/test/Rus4.m3u > /tmp/test/Rus5.m3u
sed 's/#EXTINF/#DESCRIPTION /g' /tmp/test/Rus5.m3u > /tmp/test/Rus6.m3u
sed 's/:-1,/ /g' /tmp/test/Rus6.m3u > /tmp/test/Rus6a.m3u
sed 's/:0,/ /g' /tmp/test/Rus6a.m3u > /tmp/test/Rus6b.m3u
sed 's/: / /g' /tmp/test/Rus6b.m3u > /tmp/test/Rus6c.m3u
sed 's/:/%3a/g' /tmp/test/Rus6c.m3u > /tmp/test/Rus7.m3u
sed -e "s/http/#SERVICE 4097:0:1128:0:0:0:0:0:0:0:http/" /tmp/test/Rus7.m3u > /tmp/test/Rus8.m3u
sed -e "s/rtmp/#SERVICE 4097:0:1128:0:0:0:0:0:0:0:rtmp/" /tmp/test/Rus8.m3u > /tmp/test/Rus8a.m3u
sed -e "s/mmsh/#SERVICE 4097:0:1128:0:0:0:0:0:0:0:mmsh/" /tmp/test/Rus8a.m3u > /tmp/test/Rus8b.m3u
tr -d '["]' < "/tmp/test/Rus8b.m3u" > /tmp/test/Rus8c.m3u
tr -d '[,]' < "/tmp/test/Rus8c.m3u" > /tmp/test/Rus8.m3u
awk '{print NR " " $0}' /tmp/test/Rus8.m3u  > /tmp/test/Rus9.m3u
sort -n -r "/tmp/test/Rus9.m3u"|grep -o -i '#[^<]*' > /tmp/test/Rus10.m3u
echo "#NAME Romania7.m3u" > /etc/enigma2/userbouquet.Romania7.m3u.tv
cat /tmp/test/Rus10.m3u >> /etc/enigma2/userbouquet.Romania7.m3u.tv
rm -rf /tmp/test
cd /
###########################################################################################################
more /usr/lib/enigma2/python/Plugins/Extensions/OpenPanel/DATA/x  >> /etc/enigma2/bouquets.tv 
sed -i "s/%/userbouquet.Romania8.m3u.tv/" /etc/enigma2/bouquets.tv 
[ -d /tmp/test ] || mkdir -p /tmp/test
cp /tmp/test2/8.m3u /tmp/test/x.m3u
echo ""
echo "converter Romania8.m3u for Enigma"
sleep 1
echo "start"
sed '1,1d' /tmp/test/x.m3u > /tmp/test/Rus.m3u
awk 'BEGIN {FS="png"}{print  $NF}'  /tmp/test/Rus.m3u > /tmp/test/Rus3.m3u
awk 'BEGIN {FS="group-"}{print  $NF}'  /tmp/test/Rus3.m3u > /tmp/test/Rus4.m3u
sed 's/",/#DESCRIPTION /g' /tmp/test/Rus4.m3u > /tmp/test/Rus5.m3u
sed 's/#EXTINF/#DESCRIPTION /g' /tmp/test/Rus5.m3u > /tmp/test/Rus6.m3u
sed 's/:-1,/ /g' /tmp/test/Rus6.m3u > /tmp/test/Rus6a.m3u
sed 's/:0,/ /g' /tmp/test/Rus6a.m3u > /tmp/test/Rus6b.m3u
sed 's/: / /g' /tmp/test/Rus6b.m3u > /tmp/test/Rus6c.m3u
sed 's/:/%3a/g' /tmp/test/Rus6c.m3u > /tmp/test/Rus7.m3u
sed -e "s/http/#SERVICE 4097:0:1128:0:0:0:0:0:0:0:http/" /tmp/test/Rus7.m3u > /tmp/test/Rus8.m3u
sed -e "s/rtmp/#SERVICE 4097:0:1128:0:0:0:0:0:0:0:rtmp/" /tmp/test/Rus8.m3u > /tmp/test/Rus8a.m3u
sed -e "s/mmsh/#SERVICE 4097:0:1128:0:0:0:0:0:0:0:mmsh/" /tmp/test/Rus8a.m3u > /tmp/test/Rus8b.m3u
tr -d '["]' < "/tmp/test/Rus8b.m3u" > /tmp/test/Rus8c.m3u
tr -d '[,]' < "/tmp/test/Rus8c.m3u" > /tmp/test/Rus8.m3u
awk '{print NR " " $0}' /tmp/test/Rus8.m3u  > /tmp/test/Rus9.m3u
sort -n -r "/tmp/test/Rus9.m3u"|grep -o -i '#[^<]*' > /tmp/test/Rus10.m3u
echo "#NAME Romania8.m3u" > /etc/enigma2/userbouquet.Romania8.m3u.tv
cat /tmp/test/Rus10.m3u >> /etc/enigma2/userbouquet.Romania8.m3u.tv
rm -rf /tmp/test
cd /
###########################################################################################################
more /usr/lib/enigma2/python/Plugins/Extensions/OpenPanel/DATA/x  >> /etc/enigma2/bouquets.tv 
sed -i "s/%/userbouquet.Romania9.m3u.tv/" /etc/enigma2/bouquets.tv 
[ -d /tmp/test ] || mkdir -p /tmp/test
cp /tmp/test2/9.m3u /tmp/test/x.m3u
echo ""
echo "converter Romania9.m3u for Enigma"
sleep 1
echo "start"
sed '1,1d' /tmp/test/x.m3u > /tmp/test/Rus.m3u
awk 'BEGIN {FS="png"}{print  $NF}'  /tmp/test/Rus.m3u > /tmp/test/Rus3.m3u
awk 'BEGIN {FS="group-"}{print  $NF}'  /tmp/test/Rus3.m3u > /tmp/test/Rus4.m3u
sed 's/",/#DESCRIPTION /g' /tmp/test/Rus4.m3u > /tmp/test/Rus5.m3u
sed 's/#EXTINF/#DESCRIPTION /g' /tmp/test/Rus5.m3u > /tmp/test/Rus6.m3u
sed 's/:-1,/ /g' /tmp/test/Rus6.m3u > /tmp/test/Rus6a.m3u
sed 's/:0,/ /g' /tmp/test/Rus6a.m3u > /tmp/test/Rus6b.m3u
sed 's/: / /g' /tmp/test/Rus6b.m3u > /tmp/test/Rus6c.m3u
sed 's/:/%3a/g' /tmp/test/Rus6c.m3u > /tmp/test/Rus7.m3u
sed -e "s/http/#SERVICE 4097:0:1128:0:0:0:0:0:0:0:http/" /tmp/test/Rus7.m3u > /tmp/test/Rus8.m3u
sed -e "s/rtmp/#SERVICE 4097:0:1128:0:0:0:0:0:0:0:rtmp/" /tmp/test/Rus8.m3u > /tmp/test/Rus8a.m3u
sed -e "s/mmsh/#SERVICE 4097:0:1128:0:0:0:0:0:0:0:mmsh/" /tmp/test/Rus8a.m3u > /tmp/test/Rus8b.m3u
tr -d '["]' < "/tmp/test/Rus8b.m3u" > /tmp/test/Rus8c.m3u
tr -d '[,]' < "/tmp/test/Rus8c.m3u" > /tmp/test/Rus8.m3u
awk '{print NR " " $0}' /tmp/test/Rus8.m3u  > /tmp/test/Rus9.m3u
sort -n -r "/tmp/test/Rus9.m3u"|grep -o -i '#[^<]*' > /tmp/test/Rus10.m3u
echo "#NAME Romania9.m3u" > /etc/enigma2/userbouquet.Romania9.m3u.tv
cat /tmp/test/Rus10.m3u >> /etc/enigma2/userbouquet.Romania9.m3u.tv
rm -rf /tmp/test
cd /
###########################################################################################################
more /usr/lib/enigma2/python/Plugins/Extensions/OpenPanel/DATA/x  >> /etc/enigma2/bouquets.tv 
sed -i "s/%/userbouquet.Romania10.m3u.tv/" /etc/enigma2/bouquets.tv 
[ -d /tmp/test ] || mkdir -p /tmp/test
cp /tmp/test2/10.m3u /tmp/test/x.m3u
echo ""
echo "converter Romania10.m3u for Enigma"
sleep 1
echo "start"
sed '1,1d' /tmp/test/x.m3u > /tmp/test/Rus.m3u
awk 'BEGIN {FS="png"}{print  $NF}'  /tmp/test/Rus.m3u > /tmp/test/Rus3.m3u
awk 'BEGIN {FS="group-"}{print  $NF}'  /tmp/test/Rus3.m3u > /tmp/test/Rus4.m3u
sed 's/",/#DESCRIPTION /g' /tmp/test/Rus4.m3u > /tmp/test/Rus5.m3u
sed 's/#EXTINF/#DESCRIPTION /g' /tmp/test/Rus5.m3u > /tmp/test/Rus6.m3u
sed 's/:-1,/ /g' /tmp/test/Rus6.m3u > /tmp/test/Rus6a.m3u
sed 's/:0,/ /g' /tmp/test/Rus6a.m3u > /tmp/test/Rus6b.m3u
sed 's/: / /g' /tmp/test/Rus6b.m3u > /tmp/test/Rus6c.m3u
sed 's/:/%3a/g' /tmp/test/Rus6c.m3u > /tmp/test/Rus7.m3u
sed -e "s/http/#SERVICE 4097:0:1128:0:0:0:0:0:0:0:http/" /tmp/test/Rus7.m3u > /tmp/test/Rus8.m3u
sed -e "s/rtmp/#SERVICE 4097:0:1128:0:0:0:0:0:0:0:rtmp/" /tmp/test/Rus8.m3u > /tmp/test/Rus8a.m3u
sed -e "s/mmsh/#SERVICE 4097:0:1128:0:0:0:0:0:0:0:mmsh/" /tmp/test/Rus8a.m3u > /tmp/test/Rus8b.m3u
tr -d '["]' < "/tmp/test/Rus8b.m3u" > /tmp/test/Rus8c.m3u
tr -d '[,]' < "/tmp/test/Rus8c.m3u" > /tmp/test/Rus8.m3u
awk '{print NR " " $0}' /tmp/test/Rus8.m3u  > /tmp/test/Rus9.m3u
sort -n -r "/tmp/test/Rus9.m3u"|grep -o -i '#[^<]*' > /tmp/test/Rus10.m3u
echo "#NAME Romania10.m3u" > /etc/enigma2/userbouquet.Romania10.m3u.tv
cat /tmp/test/Rus10.m3u >> /etc/enigma2/userbouquet.Romania10.m3u.tv
rm -rf /tmp/test
cd /
###########################################################################################################
more /usr/lib/enigma2/python/Plugins/Extensions/OpenPanel/DATA/x  >> /etc/enigma2/bouquets.tv 
sed -i "s/%/userbouquet.Romania11.m3u.tv/" /etc/enigma2/bouquets.tv 
[ -d /tmp/test ] || mkdir -p /tmp/test
cp /tmp/test2/11.m3u /tmp/test/x.m3u
echo ""
echo "converter Romania11.m3u for Enigma"
sleep 1
echo "start"
sed '1,1d' /tmp/test/x.m3u > /tmp/test/Rus.m3u
awk 'BEGIN {FS="png"}{print  $NF}'  /tmp/test/Rus.m3u > /tmp/test/Rus3.m3u
awk 'BEGIN {FS="group-"}{print  $NF}'  /tmp/test/Rus3.m3u > /tmp/test/Rus4.m3u
sed 's/",/#DESCRIPTION /g' /tmp/test/Rus4.m3u > /tmp/test/Rus5.m3u
sed 's/#EXTINF/#DESCRIPTION /g' /tmp/test/Rus5.m3u > /tmp/test/Rus6.m3u
sed 's/:-1,/ /g' /tmp/test/Rus6.m3u > /tmp/test/Rus6a.m3u
sed 's/:0,/ /g' /tmp/test/Rus6a.m3u > /tmp/test/Rus6b.m3u
sed 's/: / /g' /tmp/test/Rus6b.m3u > /tmp/test/Rus6c.m3u
sed 's/:/%3a/g' /tmp/test/Rus6c.m3u > /tmp/test/Rus7.m3u
sed -e "s/http/#SERVICE 4097:0:1128:0:0:0:0:0:0:0:http/" /tmp/test/Rus7.m3u > /tmp/test/Rus8.m3u
sed -e "s/rtmp/#SERVICE 4097:0:1128:0:0:0:0:0:0:0:rtmp/" /tmp/test/Rus8.m3u > /tmp/test/Rus8a.m3u
sed -e "s/mmsh/#SERVICE 4097:0:1128:0:0:0:0:0:0:0:mmsh/" /tmp/test/Rus8a.m3u > /tmp/test/Rus8b.m3u
tr -d '["]' < "/tmp/test/Rus8b.m3u" > /tmp/test/Rus8c.m3u
tr -d '[,]' < "/tmp/test/Rus8c.m3u" > /tmp/test/Rus8.m3u
awk '{print NR " " $0}' /tmp/test/Rus8.m3u  > /tmp/test/Rus9.m3u
sort -n -r "/tmp/test/Rus9.m3u"|grep -o -i '#[^<]*' > /tmp/test/Rus10.m3u
echo "#NAME Romania11.m3u" > /etc/enigma2/userbouquet.Romania11.m3u.tv
cat /tmp/test/Rus10.m3u >> /etc/enigma2/userbouquet.Romania11.m3u.tv
rm -rf /tmp/test
cd /
###########################################################################################################
more /usr/lib/enigma2/python/Plugins/Extensions/OpenPanel/DATA/x  >> /etc/enigma2/bouquets.tv 
sed -i "s/%/userbouquet.Romania12.m3u.tv/" /etc/enigma2/bouquets.tv 
[ -d /tmp/test ] || mkdir -p /tmp/test
cp /tmp/test2/12.m3u /tmp/test/x.m3u
echo ""
echo "converter Romania12.m3u for Enigma"
sleep 1
echo "start"
sed '1,1d' /tmp/test/x.m3u > /tmp/test/Rus.m3u
awk 'BEGIN {FS="png"}{print  $NF}'  /tmp/test/Rus.m3u > /tmp/test/Rus3.m3u
awk 'BEGIN {FS="group-"}{print  $NF}'  /tmp/test/Rus3.m3u > /tmp/test/Rus4.m3u
sed 's/",/#DESCRIPTION /g' /tmp/test/Rus4.m3u > /tmp/test/Rus5.m3u
sed 's/#EXTINF/#DESCRIPTION /g' /tmp/test/Rus5.m3u > /tmp/test/Rus6.m3u
sed 's/:-1,/ /g' /tmp/test/Rus6.m3u > /tmp/test/Rus6a.m3u
sed 's/:0,/ /g' /tmp/test/Rus6a.m3u > /tmp/test/Rus6b.m3u
sed 's/: / /g' /tmp/test/Rus6b.m3u > /tmp/test/Rus6c.m3u
sed 's/:/%3a/g' /tmp/test/Rus6c.m3u > /tmp/test/Rus7.m3u
sed -e "s/http/#SERVICE 4097:0:1128:0:0:0:0:0:0:0:http/" /tmp/test/Rus7.m3u > /tmp/test/Rus8.m3u
sed -e "s/rtmp/#SERVICE 4097:0:1128:0:0:0:0:0:0:0:rtmp/" /tmp/test/Rus8.m3u > /tmp/test/Rus8a.m3u
sed -e "s/mmsh/#SERVICE 4097:0:1128:0:0:0:0:0:0:0:mmsh/" /tmp/test/Rus8a.m3u > /tmp/test/Rus8b.m3u
tr -d '["]' < "/tmp/test/Rus8b.m3u" > /tmp/test/Rus8c.m3u
tr -d '[,]' < "/tmp/test/Rus8c.m3u" > /tmp/test/Rus8.m3u
awk '{print NR " " $0}' /tmp/test/Rus8.m3u  > /tmp/test/Rus9.m3u
sort -n -r "/tmp/test/Rus9.m3u"|grep -o -i '#[^<]*' > /tmp/test/Rus10.m3u
echo "#NAME Romania12.m3u" > /etc/enigma2/userbouquet.Romania12.m3u.tv
cat /tmp/test/Rus10.m3u >> /etc/enigma2/userbouquet.Romania12.m3u.tv
rm -rf /tmp/test
cd /
###########################################################################################################
more /usr/lib/enigma2/python/Plugins/Extensions/OpenPanel/DATA/x  >> /etc/enigma2/bouquets.tv 
sed -i "s/%/userbouquet.Romania13.m3u.tv/" /etc/enigma2/bouquets.tv 
[ -d /tmp/test ] || mkdir -p /tmp/test
cp /tmp/test2/13.m3u /tmp/test/x.m3u
echo ""
echo "converter Romania13.m3u for Enigma"
sleep 1
echo "start"
sed '1,1d' /tmp/test/x.m3u > /tmp/test/Rus.m3u
awk 'BEGIN {FS="png"}{print  $NF}'  /tmp/test/Rus.m3u > /tmp/test/Rus3.m3u
awk 'BEGIN {FS="group-"}{print  $NF}'  /tmp/test/Rus3.m3u > /tmp/test/Rus4.m3u
sed 's/",/#DESCRIPTION /g' /tmp/test/Rus4.m3u > /tmp/test/Rus5.m3u
sed 's/#EXTINF/#DESCRIPTION /g' /tmp/test/Rus5.m3u > /tmp/test/Rus6.m3u
sed 's/:-1,/ /g' /tmp/test/Rus6.m3u > /tmp/test/Rus6a.m3u
sed 's/:0,/ /g' /tmp/test/Rus6a.m3u > /tmp/test/Rus6b.m3u
sed 's/: / /g' /tmp/test/Rus6b.m3u > /tmp/test/Rus6c.m3u
sed 's/:/%3a/g' /tmp/test/Rus6c.m3u > /tmp/test/Rus7.m3u
sed -e "s/http/#SERVICE 4097:0:1128:0:0:0:0:0:0:0:http/" /tmp/test/Rus7.m3u > /tmp/test/Rus8.m3u
sed -e "s/rtmp/#SERVICE 4097:0:1128:0:0:0:0:0:0:0:rtmp/" /tmp/test/Rus8.m3u > /tmp/test/Rus8a.m3u
sed -e "s/mmsh/#SERVICE 4097:0:1128:0:0:0:0:0:0:0:mmsh/" /tmp/test/Rus8a.m3u > /tmp/test/Rus8b.m3u
tr -d '["]' < "/tmp/test/Rus8b.m3u" > /tmp/test/Rus8c.m3u
tr -d '[,]' < "/tmp/test/Rus8c.m3u" > /tmp/test/Rus8.m3u
awk '{print NR " " $0}' /tmp/test/Rus8.m3u  > /tmp/test/Rus9.m3u
sort -n -r "/tmp/test/Rus9.m3u"|grep -o -i '#[^<]*' > /tmp/test/Rus10.m3u
echo "#NAME Romania13.m3u" > /etc/enigma2/userbouquet.Romania13.m3u.tv
cat /tmp/test/Rus10.m3u >> /etc/enigma2/userbouquet.Romania13.m3u.tv
rm -rf /tmp/test
cd /
###########################################################################################################
more /usr/lib/enigma2/python/Plugins/Extensions/OpenPanel/DATA/x  >> /etc/enigma2/bouquets.tv 
sed -i "s/%/userbouquet.Romania14.m3u.tv/" /etc/enigma2/bouquets.tv 
[ -d /tmp/test ] || mkdir -p /tmp/test
cp /tmp/test2/14.m3u /tmp/test/x.m3u
echo ""
echo "converter Romania14.m3u for Enigma"
sleep 1
echo "start"
sed '1,1d' /tmp/test/x.m3u > /tmp/test/Rus.m3u
awk 'BEGIN {FS="png"}{print  $NF}'  /tmp/test/Rus.m3u > /tmp/test/Rus3.m3u
awk 'BEGIN {FS="group-"}{print  $NF}'  /tmp/test/Rus3.m3u > /tmp/test/Rus4.m3u
sed 's/",/#DESCRIPTION /g' /tmp/test/Rus4.m3u > /tmp/test/Rus5.m3u
sed 's/#EXTINF/#DESCRIPTION /g' /tmp/test/Rus5.m3u > /tmp/test/Rus6.m3u
sed 's/:-1,/ /g' /tmp/test/Rus6.m3u > /tmp/test/Rus6a.m3u
sed 's/:0,/ /g' /tmp/test/Rus6a.m3u > /tmp/test/Rus6b.m3u
sed 's/: / /g' /tmp/test/Rus6b.m3u > /tmp/test/Rus6c.m3u
sed 's/:/%3a/g' /tmp/test/Rus6c.m3u > /tmp/test/Rus7.m3u
sed -e "s/http/#SERVICE 4097:0:1128:0:0:0:0:0:0:0:http/" /tmp/test/Rus7.m3u > /tmp/test/Rus8.m3u
sed -e "s/rtmp/#SERVICE 4097:0:1128:0:0:0:0:0:0:0:rtmp/" /tmp/test/Rus8.m3u > /tmp/test/Rus8a.m3u
sed -e "s/mmsh/#SERVICE 4097:0:1128:0:0:0:0:0:0:0:mmsh/" /tmp/test/Rus8a.m3u > /tmp/test/Rus8b.m3u
tr -d '["]' < "/tmp/test/Rus8b.m3u" > /tmp/test/Rus8c.m3u
tr -d '[,]' < "/tmp/test/Rus8c.m3u" > /tmp/test/Rus8.m3u
awk '{print NR " " $0}' /tmp/test/Rus8.m3u  > /tmp/test/Rus9.m3u
sort -n -r "/tmp/test/Rus9.m3u"|grep -o -i '#[^<]*' > /tmp/test/Rus10.m3u
echo "#NAME Romania14.m3u" > /etc/enigma2/userbouquet.Romania14.m3u.tv
cat /tmp/test/Rus10.m3u >> /etc/enigma2/userbouquet.Romania14.m3u.tv
rm -rf /tmp/test
cd /
###########################################################################################################
more /usr/lib/enigma2/python/Plugins/Extensions/OpenPanel/DATA/x  >> /etc/enigma2/bouquets.tv 
sed -i "s/%/userbouquet.Romania15.m3u.tv/" /etc/enigma2/bouquets.tv 
[ -d /tmp/test ] || mkdir -p /tmp/test
cp /tmp/test2/15.m3u /tmp/test/x.m3u
echo ""
echo "converter Romania15.m3u for Enigma"
sleep 1
echo "start"
sed '1,1d' /tmp/test/x.m3u > /tmp/test/Rus.m3u
awk 'BEGIN {FS="png"}{print  $NF}'  /tmp/test/Rus.m3u > /tmp/test/Rus3.m3u
awk 'BEGIN {FS="group-"}{print  $NF}'  /tmp/test/Rus3.m3u > /tmp/test/Rus4.m3u
sed 's/",/#DESCRIPTION /g' /tmp/test/Rus4.m3u > /tmp/test/Rus5.m3u
sed 's/#EXTINF/#DESCRIPTION /g' /tmp/test/Rus5.m3u > /tmp/test/Rus6.m3u
sed 's/:-1,/ /g' /tmp/test/Rus6.m3u > /tmp/test/Rus6a.m3u
sed 's/:0,/ /g' /tmp/test/Rus6a.m3u > /tmp/test/Rus6b.m3u
sed 's/: / /g' /tmp/test/Rus6b.m3u > /tmp/test/Rus6c.m3u
sed 's/:/%3a/g' /tmp/test/Rus6c.m3u > /tmp/test/Rus7.m3u
sed -e "s/http/#SERVICE 4097:0:1128:0:0:0:0:0:0:0:http/" /tmp/test/Rus7.m3u > /tmp/test/Rus8.m3u
sed -e "s/rtmp/#SERVICE 4097:0:1128:0:0:0:0:0:0:0:rtmp/" /tmp/test/Rus8.m3u > /tmp/test/Rus8a.m3u
sed -e "s/mmsh/#SERVICE 4097:0:1128:0:0:0:0:0:0:0:mmsh/" /tmp/test/Rus8a.m3u > /tmp/test/Rus8b.m3u
tr -d '["]' < "/tmp/test/Rus8b.m3u" > /tmp/test/Rus8c.m3u
tr -d '[,]' < "/tmp/test/Rus8c.m3u" > /tmp/test/Rus8.m3u
awk '{print NR " " $0}' /tmp/test/Rus8.m3u  > /tmp/test/Rus9.m3u
sort -n -r "/tmp/test/Rus9.m3u"|grep -o -i '#[^<]*' > /tmp/test/Rus10.m3u
echo "#NAME Romania15.m3u" > /etc/enigma2/userbouquet.Romania15.m3u.tv
cat /tmp/test/Rus10.m3u >> /etc/enigma2/userbouquet.Romania15.m3u.tv
rm -rf /tmp/test
cd /
###########################################################################################################
more /usr/lib/enigma2/python/Plugins/Extensions/OpenPanel/DATA/x  >> /etc/enigma2/bouquets.tv 
sed -i "s/%/userbouquet.Romania16.m3u.tv/" /etc/enigma2/bouquets.tv 
[ -d /tmp/test ] || mkdir -p /tmp/test
cp /tmp/test2/16.m3u /tmp/test/x.m3u
echo ""
echo "converter Romania16.m3u for Enigma"
sleep 1
echo "start"
sed '1,1d' /tmp/test/x.m3u > /tmp/test/Rus.m3u
awk 'BEGIN {FS="png"}{print  $NF}'  /tmp/test/Rus.m3u > /tmp/test/Rus3.m3u
awk 'BEGIN {FS="group-"}{print  $NF}'  /tmp/test/Rus3.m3u > /tmp/test/Rus4.m3u
sed 's/",/#DESCRIPTION /g' /tmp/test/Rus4.m3u > /tmp/test/Rus5.m3u
sed 's/#EXTINF/#DESCRIPTION /g' /tmp/test/Rus5.m3u > /tmp/test/Rus6.m3u
sed 's/:-1,/ /g' /tmp/test/Rus6.m3u > /tmp/test/Rus6a.m3u
sed 's/:0,/ /g' /tmp/test/Rus6a.m3u > /tmp/test/Rus6b.m3u
sed 's/: / /g' /tmp/test/Rus6b.m3u > /tmp/test/Rus6c.m3u
sed 's/:/%3a/g' /tmp/test/Rus6c.m3u > /tmp/test/Rus7.m3u
sed -e "s/http/#SERVICE 4097:0:1128:0:0:0:0:0:0:0:http/" /tmp/test/Rus7.m3u > /tmp/test/Rus8.m3u
sed -e "s/rtmp/#SERVICE 4097:0:1128:0:0:0:0:0:0:0:rtmp/" /tmp/test/Rus8.m3u > /tmp/test/Rus8a.m3u
sed -e "s/mmsh/#SERVICE 4097:0:1128:0:0:0:0:0:0:0:mmsh/" /tmp/test/Rus8a.m3u > /tmp/test/Rus8b.m3u
tr -d '["]' < "/tmp/test/Rus8b.m3u" > /tmp/test/Rus8c.m3u
tr -d '[,]' < "/tmp/test/Rus8c.m3u" > /tmp/test/Rus8.m3u
awk '{print NR " " $0}' /tmp/test/Rus8.m3u  > /tmp/test/Rus9.m3u
sort -n -r "/tmp/test/Rus9.m3u"|grep -o -i '#[^<]*' > /tmp/test/Rus10.m3u
echo "#NAME Romania16.m3u" > /etc/enigma2/userbouquet.Romania16.m3u.tv
cat /tmp/test/Rus10.m3u >> /etc/enigma2/userbouquet.Romania16.m3u.tv
rm -rf /tmp/test
cd /
###########################################################################################################
more /usr/lib/enigma2/python/Plugins/Extensions/OpenPanel/DATA/x  >> /etc/enigma2/bouquets.tv 
sed -i "s/%/userbouquet.Romania17.m3u.tv/" /etc/enigma2/bouquets.tv 
[ -d /tmp/test ] || mkdir -p /tmp/test
cp /tmp/test2/17.m3u /tmp/test/x.m3u
echo ""
echo "converter Romania17.m3u for Enigma"
sleep 1
echo "start"
sed '1,1d' /tmp/test/x.m3u > /tmp/test/Rus.m3u
awk 'BEGIN {FS="png"}{print  $NF}'  /tmp/test/Rus.m3u > /tmp/test/Rus3.m3u
awk 'BEGIN {FS="group-"}{print  $NF}'  /tmp/test/Rus3.m3u > /tmp/test/Rus4.m3u
sed 's/",/#DESCRIPTION /g' /tmp/test/Rus4.m3u > /tmp/test/Rus5.m3u
sed 's/#EXTINF/#DESCRIPTION /g' /tmp/test/Rus5.m3u > /tmp/test/Rus6.m3u
sed 's/:-1,/ /g' /tmp/test/Rus6.m3u > /tmp/test/Rus6a.m3u
sed 's/:0,/ /g' /tmp/test/Rus6a.m3u > /tmp/test/Rus6b.m3u
sed 's/: / /g' /tmp/test/Rus6b.m3u > /tmp/test/Rus6c.m3u
sed 's/:/%3a/g' /tmp/test/Rus6c.m3u > /tmp/test/Rus7.m3u
sed -e "s/http/#SERVICE 4097:0:1128:0:0:0:0:0:0:0:http/" /tmp/test/Rus7.m3u > /tmp/test/Rus8.m3u
sed -e "s/rtmp/#SERVICE 4097:0:1128:0:0:0:0:0:0:0:rtmp/" /tmp/test/Rus8.m3u > /tmp/test/Rus8a.m3u
sed -e "s/mmsh/#SERVICE 4097:0:1128:0:0:0:0:0:0:0:mmsh/" /tmp/test/Rus8a.m3u > /tmp/test/Rus8b.m3u
tr -d '["]' < "/tmp/test/Rus8b.m3u" > /tmp/test/Rus8c.m3u
tr -d '[,]' < "/tmp/test/Rus8c.m3u" > /tmp/test/Rus8.m3u
awk '{print NR " " $0}' /tmp/test/Rus8.m3u  > /tmp/test/Rus9.m3u
sort -n -r "/tmp/test/Rus9.m3u"|grep -o -i '#[^<]*' > /tmp/test/Rus10.m3u
echo "#NAME Romania17.m3u" > /etc/enigma2/userbouquet.Romania17.m3u.tv
cat /tmp/test/Rus10.m3u >> /etc/enigma2/userbouquet.Romania17.m3u.tv
rm -rf /tmp/test
cd /
###########################################################################################################
more /usr/lib/enigma2/python/Plugins/Extensions/OpenPanel/DATA/x  >> /etc/enigma2/bouquets.tv 
sed -i "s/%/userbouquet.Romania18.m3u.tv/" /etc/enigma2/bouquets.tv 
[ -d /tmp/test ] || mkdir -p /tmp/test
cp /tmp/test2/18.m3u /tmp/test/x.m3u
echo ""
echo "converter Romania18.m3u for Enigma"
sleep 1
echo "start"
sed '1,1d' /tmp/test/x.m3u > /tmp/test/Rus.m3u
awk 'BEGIN {FS="png"}{print  $NF}'  /tmp/test/Rus.m3u > /tmp/test/Rus3.m3u
awk 'BEGIN {FS="group-"}{print  $NF}'  /tmp/test/Rus3.m3u > /tmp/test/Rus4.m3u
sed 's/",/#DESCRIPTION /g' /tmp/test/Rus4.m3u > /tmp/test/Rus5.m3u
sed 's/#EXTINF/#DESCRIPTION /g' /tmp/test/Rus5.m3u > /tmp/test/Rus6.m3u
sed 's/:-1,/ /g' /tmp/test/Rus6.m3u > /tmp/test/Rus6a.m3u
sed 's/:0,/ /g' /tmp/test/Rus6a.m3u > /tmp/test/Rus6b.m3u
sed 's/: / /g' /tmp/test/Rus6b.m3u > /tmp/test/Rus6c.m3u
sed 's/:/%3a/g' /tmp/test/Rus6c.m3u > /tmp/test/Rus7.m3u
sed -e "s/http/#SERVICE 4097:0:1128:0:0:0:0:0:0:0:http/" /tmp/test/Rus7.m3u > /tmp/test/Rus8.m3u
sed -e "s/rtmp/#SERVICE 4097:0:1128:0:0:0:0:0:0:0:rtmp/" /tmp/test/Rus8.m3u > /tmp/test/Rus8a.m3u
sed -e "s/mmsh/#SERVICE 4097:0:1128:0:0:0:0:0:0:0:mmsh/" /tmp/test/Rus8a.m3u > /tmp/test/Rus8b.m3u
tr -d '["]' < "/tmp/test/Rus8b.m3u" > /tmp/test/Rus8c.m3u
tr -d '[,]' < "/tmp/test/Rus8c.m3u" > /tmp/test/Rus8.m3u
awk '{print NR " " $0}' /tmp/test/Rus8.m3u  > /tmp/test/Rus9.m3u
sort -n -r "/tmp/test/Rus9.m3u"|grep -o -i '#[^<]*' > /tmp/test/Rus10.m3u
echo "#NAME Romania18.m3u" > /etc/enigma2/userbouquet.Romania18.m3u.tv
cat /tmp/test/Rus10.m3u >> /etc/enigma2/userbouquet.Romania18.m3u.tv
rm -rf /tmp/test
cd /
###########################################################################################################
rm -rf /tmp/test2
wget -q -O - http://root%s@127.0.0.1/web/servicelistreload?mode=0 >>/dev/null 2>&1 </dev/null &
sleep 2
echo "OK"
exit







