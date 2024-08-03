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
grep -o -i 'https://cccam4all.net/iptv-smart-tv-exito-magenta-and-mobile[^<]*' CCcam > CCcam1
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
mv -v /tmp/test2/"Smart Tv And Mobile (0).m3u" /tmp/test2/"0.m3u"
mv -v /tmp/test2/"Smart Tv And Mobile (1).m3u" /tmp/test2/"1.m3u"
mv -v /tmp/test2/"Smart Tv And Mobile (2).m3u" /tmp/test2/"2.m3u"
mv -v /tmp/test2/"Smart Tv And Mobile (3).m3u" /tmp/test2/"3.m3u"
mv -v /tmp/test2/"Smart Tv And Mobile (4).m3u" /tmp/test2/"4.m3u"
mv -v /tmp/test2/"Smart Tv And Mobile (5).m3u" /tmp/test2/"5.m3u"
mv -v /tmp/test2/"bein sports (1).m3u" /tmp/test2/"6.m3u"
mv -v /tmp/test2/"bein sports (2).m3u" /tmp/test2/"7.m3u"
mv -v /tmp/test2/"bein sports (3).m3u" /tmp/test2/"8.m3u"
mv -v /tmp/test2/"bein sports (4).m3u" /tmp/test2/"9.m3u"
###########################################################################################################
more /usr/lib/enigma2/python/Plugins/Extensions/OpenPanel/DATA/x  >> /etc/enigma2/bouquets.tv 
sed -i "s/%/userbouquet.Smart0.m3u.tv/" /etc/enigma2/bouquets.tv 
[ -d /tmp/test ] || mkdir -p /tmp/test
cp /tmp/test2/0.m3u /tmp/test/x.m3u
echo ""
echo "converter Smart0.m3u for Enigma"
sleep 1
echo "start"
sed '1,1d' /tmp/test/x.m3u > /tmp/test/Rus.m3u
awk 'BEGIN {FS="png"}{print  $NF}'  /tmp/test/Rus.m3u > /tmp/test/Rus3.m3u
awk 'BEGIN {FS="group-"}{print  $NF}'  /tmp/test/Rus3.m3u > /tmp/test/Rus4.m3u
sed 's/",/#DESCRIPTION /g' /tmp/test/Rus4.m3u > /tmp/test/Rus5.m3u
sed 's/#EXTINF/#DESCRIPTION /g' /tmp/test/Rus5.m3u > /tmp/test/Rus6.m3u
sed 's/:-1,/ /g' /tmp/test/Rus6.m3u > /tmp/test/Rus6a.m3u
sed 's/:0,/ /g' /tmp/test/Rus6a.m3u > /tmp/test/Rus6b.m3u
sed 's/:/%3a/g' /tmp/test/Rus6b.m3u > /tmp/test/Rus7.m3u
sed -e "s/http/#SERVICE 4097:0:1128:0:0:0:0:0:0:0:http/" /tmp/test/Rus7.m3u > /tmp/test/Rus7a.m3u
sed -e "s/rtmp/#SERVICE 4097:0:1128:0:0:0:0:0:0:0:rtmp/" /tmp/test/Rus7a.m3u > /tmp/test/Rus8.m3u
tr -d '["]' < "/tmp/test/Rus8.m3u" > /tmp/test/Rus8a.m3u
tr -d '[,]' < "/tmp/test/Rus8a.m3u" > /tmp/test/Rus8.m3u
awk '{print NR " " $0}' /tmp/test/Rus8.m3u  > /tmp/test/Rus9.m3u
sort -n -r "/tmp/test/Rus9.m3u"|grep -o -i '#[^<]*' > /tmp/test/Rus10.m3u
echo "#NAME Smart0.m3u" > /etc/enigma2/userbouquet.Smart0.m3u.tv
cat /tmp/test/Rus10.m3u >> /etc/enigma2/userbouquet.Smart0.m3u.tv
rm -rf /tmp/test
cd /
###########################################################################################################
more /usr/lib/enigma2/python/Plugins/Extensions/OpenPanel/DATA/x  >> /etc/enigma2/bouquets.tv 
sed -i "s/%/userbouquet.Smart1.m3u.tv/" /etc/enigma2/bouquets.tv 
[ -d /tmp/test ] || mkdir -p /tmp/test
cp /tmp/test2/1.m3u /tmp/test/x.m3u
echo ""
echo "converter Smart1.m3u for Enigma"
sleep 1
echo "start"
sed '1,1d' /tmp/test/x.m3u > /tmp/test/Rus.m3u
awk 'BEGIN {FS="png"}{print  $NF}'  /tmp/test/Rus.m3u > /tmp/test/Rus3.m3u
awk 'BEGIN {FS="group-"}{print  $NF}'  /tmp/test/Rus3.m3u > /tmp/test/Rus4.m3u
sed 's/",/#DESCRIPTION /g' /tmp/test/Rus4.m3u > /tmp/test/Rus5.m3u
sed 's/#EXTINF/#DESCRIPTION /g' /tmp/test/Rus5.m3u > /tmp/test/Rus6.m3u
sed 's/:-1,/ /g' /tmp/test/Rus6.m3u > /tmp/test/Rus6a.m3u
sed 's/:0,/ /g' /tmp/test/Rus6a.m3u > /tmp/test/Rus6b.m3u
sed 's/:/%3a/g' /tmp/test/Rus6b.m3u > /tmp/test/Rus7.m3u
sed -e "s/http/#SERVICE 4097:0:1128:0:0:0:0:0:0:0:http/" /tmp/test/Rus7.m3u > /tmp/test/Rus7a.m3u
sed -e "s/rtmp/#SERVICE 4097:0:1128:0:0:0:0:0:0:0:rtmp/" /tmp/test/Rus7a.m3u > /tmp/test/Rus8.m3u
tr -d '["]' < "/tmp/test/Rus8.m3u" > /tmp/test/Rus8a.m3u
tr -d '[,]' < "/tmp/test/Rus8a.m3u" > /tmp/test/Rus8.m3u
awk '{print NR " " $0}' /tmp/test/Rus8.m3u  > /tmp/test/Rus9.m3u
sort -n -r "/tmp/test/Rus9.m3u"|grep -o -i '#[^<]*' > /tmp/test/Rus10.m3u
echo "#NAME Smart1.m3u" > /etc/enigma2/userbouquet.Smart1.m3u.tv
cat /tmp/test/Rus10.m3u >> /etc/enigma2/userbouquet.Smart1.m3u.tv
rm -rf /tmp/test
cd /
rm -rf /tmp/test
cd /
###########################################################################################################
more /usr/lib/enigma2/python/Plugins/Extensions/OpenPanel/DATA/x  >> /etc/enigma2/bouquets.tv 
sed -i "s/%/userbouquet.Smart2.m3u.tv/" /etc/enigma2/bouquets.tv 
[ -d /tmp/test ] || mkdir -p /tmp/test
cp /tmp/test2/2.m3u /tmp/test/x.m3u
echo ""
echo "converter Smart2.m3u for Enigma"
sleep 1
echo "start"
sed '1,1d' /tmp/test/x.m3u > /tmp/test/Rus.m3u
awk 'BEGIN {FS="png"}{print  $NF}'  /tmp/test/Rus.m3u > /tmp/test/Rus3.m3u
awk 'BEGIN {FS="group-"}{print  $NF}'  /tmp/test/Rus3.m3u > /tmp/test/Rus4.m3u
sed 's/",/#DESCRIPTION /g' /tmp/test/Rus4.m3u > /tmp/test/Rus5.m3u
sed 's/#EXTINF/#DESCRIPTION /g' /tmp/test/Rus5.m3u > /tmp/test/Rus6.m3u
sed 's/:-1,/ /g' /tmp/test/Rus6.m3u > /tmp/test/Rus6a.m3u
sed 's/:0,/ /g' /tmp/test/Rus6a.m3u > /tmp/test/Rus6b.m3u
sed 's/:/%3a/g' /tmp/test/Rus6b.m3u > /tmp/test/Rus7.m3u
sed -e "s/http/#SERVICE 4097:0:1128:0:0:0:0:0:0:0:http/" /tmp/test/Rus7.m3u > /tmp/test/Rus7a.m3u
sed -e "s/rtmp/#SERVICE 4097:0:1128:0:0:0:0:0:0:0:rtmp/" /tmp/test/Rus7a.m3u > /tmp/test/Rus8.m3u
tr -d '["]' < "/tmp/test/Rus8.m3u" > /tmp/test/Rus8a.m3u
tr -d '[,]' < "/tmp/test/Rus8a.m3u" > /tmp/test/Rus8.m3u
awk '{print NR " " $0}' /tmp/test/Rus8.m3u  > /tmp/test/Rus9.m3u
sort -n -r "/tmp/test/Rus9.m3u"|grep -o -i '#[^<]*' > /tmp/test/Rus10.m3u
echo "#NAME Smart2.m3u" > /etc/enigma2/userbouquet.Smart2.m3u.tv
cat /tmp/test/Rus10.m3u >> /etc/enigma2/userbouquet.Smart2.m3u.tv
rm -rf /tmp/test
cd /
###########################################################################################################
more /usr/lib/enigma2/python/Plugins/Extensions/OpenPanel/DATA/x  >> /etc/enigma2/bouquets.tv 
sed -i "s/%/userbouquet.Smart3.m3u.tv/" /etc/enigma2/bouquets.tv 
[ -d /tmp/test ] || mkdir -p /tmp/test
cp /tmp/test2/3.m3u /tmp/test/x.m3u
echo ""
echo "converter Smart3.m3u for Enigma"
sleep 1
echo "start"
sed '1,1d' /tmp/test/x.m3u > /tmp/test/Rus.m3u
awk 'BEGIN {FS="png"}{print  $NF}'  /tmp/test/Rus.m3u > /tmp/test/Rus3.m3u
awk 'BEGIN {FS="group-"}{print  $NF}'  /tmp/test/Rus3.m3u > /tmp/test/Rus4.m3u
sed 's/",/#DESCRIPTION /g' /tmp/test/Rus4.m3u > /tmp/test/Rus5.m3u
sed 's/#EXTINF/#DESCRIPTION /g' /tmp/test/Rus5.m3u > /tmp/test/Rus6.m3u
sed 's/:-1,/ /g' /tmp/test/Rus6.m3u > /tmp/test/Rus6a.m3u
sed 's/:0,/ /g' /tmp/test/Rus6a.m3u > /tmp/test/Rus6b.m3u
sed 's/:/%3a/g' /tmp/test/Rus6b.m3u > /tmp/test/Rus7.m3u
sed -e "s/http/#SERVICE 4097:0:1128:0:0:0:0:0:0:0:http/" /tmp/test/Rus7.m3u > /tmp/test/Rus7a.m3u
sed -e "s/rtmp/#SERVICE 4097:0:1128:0:0:0:0:0:0:0:rtmp/" /tmp/test/Rus7a.m3u > /tmp/test/Rus8.m3u
tr -d '["]' < "/tmp/test/Rus8.m3u" > /tmp/test/Rus8a.m3u
tr -d '[,]' < "/tmp/test/Rus8a.m3u" > /tmp/test/Rus8.m3u
awk '{print NR " " $0}' /tmp/test/Rus8.m3u  > /tmp/test/Rus9.m3u
sort -n -r "/tmp/test/Rus9.m3u"|grep -o -i '#[^<]*' > /tmp/test/Rus10.m3u
echo "#NAME Smart3.m3u" > /etc/enigma2/userbouquet.Smart3.m3u.tv
cat /tmp/test/Rus10.m3u >> /etc/enigma2/userbouquet.Smart3.m3u.tv
rm -rf /tmp/test
cd /
###########################################################################################################
more /usr/lib/enigma2/python/Plugins/Extensions/OpenPanel/DATA/x  >> /etc/enigma2/bouquets.tv 
sed -i "s/%/userbouquet.Smart4.m3u.tv/" /etc/enigma2/bouquets.tv 
[ -d /tmp/test ] || mkdir -p /tmp/test
cp /tmp/test2/4.m3u /tmp/test/x.m3u
echo ""
echo "converter Smart4.m3u for Enigma"
sleep 1
echo "start"
sed '1,1d' /tmp/test/x.m3u > /tmp/test/Rus.m3u
awk 'BEGIN {FS="png"}{print  $NF}'  /tmp/test/Rus.m3u > /tmp/test/Rus3.m3u
awk 'BEGIN {FS="group-"}{print  $NF}'  /tmp/test/Rus3.m3u > /tmp/test/Rus4.m3u
sed 's/",/#DESCRIPTION /g' /tmp/test/Rus4.m3u > /tmp/test/Rus5.m3u
sed 's/#EXTINF/#DESCRIPTION /g' /tmp/test/Rus5.m3u > /tmp/test/Rus6.m3u
sed 's/:-1,/ /g' /tmp/test/Rus6.m3u > /tmp/test/Rus6a.m3u
sed 's/:0,/ /g' /tmp/test/Rus6a.m3u > /tmp/test/Rus6b.m3u
sed 's/:/%3a/g' /tmp/test/Rus6b.m3u > /tmp/test/Rus7.m3u
sed -e "s/http/#SERVICE 4097:0:1128:0:0:0:0:0:0:0:http/" /tmp/test/Rus7.m3u > /tmp/test/Rus7a.m3u
sed -e "s/rtmp/#SERVICE 4097:0:1128:0:0:0:0:0:0:0:rtmp/" /tmp/test/Rus7a.m3u > /tmp/test/Rus8.m3u
tr -d '["]' < "/tmp/test/Rus8.m3u" > /tmp/test/Rus8a.m3u
tr -d '[,]' < "/tmp/test/Rus8a.m3u" > /tmp/test/Rus8.m3u
awk '{print NR " " $0}' /tmp/test/Rus8.m3u  > /tmp/test/Rus9.m3u
sort -n -r "/tmp/test/Rus9.m3u"|grep -o -i '#[^<]*' > /tmp/test/Rus10.m3u
echo "#NAME Smart4.m3u" > /etc/enigma2/userbouquet.Smart4.m3u.tv
cat /tmp/test/Rus10.m3u >> /etc/enigma2/userbouquet.Smart4.m3u.tv
rm -rf /tmp/test
cd /
###########################################################################################################
more /usr/lib/enigma2/python/Plugins/Extensions/OpenPanel/DATA/x  >> /etc/enigma2/bouquets.tv 
sed -i "s/%/userbouquet.Smart5.m3u.tv/" /etc/enigma2/bouquets.tv 
[ -d /tmp/test ] || mkdir -p /tmp/test
cp /tmp/test2/5.m3u /tmp/test/x.m3u
echo ""
echo "converter Smart5.m3u for Enigma"
sleep 1
echo "start"
sed '1,1d' /tmp/test/x.m3u > /tmp/test/Rus.m3u
awk 'BEGIN {FS="png"}{print  $NF}'  /tmp/test/Rus.m3u > /tmp/test/Rus3.m3u
awk 'BEGIN {FS="group-"}{print  $NF}'  /tmp/test/Rus3.m3u > /tmp/test/Rus4.m3u
sed 's/",/#DESCRIPTION /g' /tmp/test/Rus4.m3u > /tmp/test/Rus5.m3u
sed 's/#EXTINF/#DESCRIPTION /g' /tmp/test/Rus5.m3u > /tmp/test/Rus6.m3u
sed 's/:-1,/ /g' /tmp/test/Rus6.m3u > /tmp/test/Rus6a.m3u
sed 's/:0,/ /g' /tmp/test/Rus6a.m3u > /tmp/test/Rus6b.m3u
sed 's/:/%3a/g' /tmp/test/Rus6b.m3u > /tmp/test/Rus7.m3u
sed -e "s/http/#SERVICE 4097:0:1128:0:0:0:0:0:0:0:http/" /tmp/test/Rus7.m3u > /tmp/test/Rus7a.m3u
sed -e "s/rtmp/#SERVICE 4097:0:1128:0:0:0:0:0:0:0:rtmp/" /tmp/test/Rus7a.m3u > /tmp/test/Rus8.m3u
tr -d '["]' < "/tmp/test/Rus8.m3u" > /tmp/test/Rus8a.m3u
tr -d '[,]' < "/tmp/test/Rus8a.m3u" > /tmp/test/Rus8.m3u
awk '{print NR " " $0}' /tmp/test/Rus8.m3u  > /tmp/test/Rus9.m3u
sort -n -r "/tmp/test/Rus9.m3u"|grep -o -i '#[^<]*' > /tmp/test/Rus10.m3u
sleep 1
echo "#NAME Smart5.m3u" > /etc/enigma2/userbouquet.Smart5.m3u.tv
cat /tmp/test/Rus10.m3u >> /etc/enigma2/userbouquet.Smart5.m3u.tv
rm -rf /tmp/test
cd /
###########################################################################################################
more /usr/lib/enigma2/python/Plugins/Extensions/OpenPanel/DATA/x  >> /etc/enigma2/bouquets.tv 
sed -i "s/%/userbouquet.Smart6.m3u.tv/" /etc/enigma2/bouquets.tv 
[ -d /tmp/test ] || mkdir -p /tmp/test
cp /tmp/test2/6.m3u /tmp/test/x.m3u
echo ""
echo "converter Smart6.m3u for Enigma"
sleep 1
echo "start"
sed '1,1d' /tmp/test/x.m3u > /tmp/test/Rus.m3u
awk 'BEGIN {FS="png"}{print  $NF}'  /tmp/test/Rus.m3u > /tmp/test/Rus3.m3u
awk 'BEGIN {FS="group-"}{print  $NF}'  /tmp/test/Rus3.m3u > /tmp/test/Rus4.m3u
sed 's/",/#DESCRIPTION /g' /tmp/test/Rus4.m3u > /tmp/test/Rus5.m3u
sed 's/#EXTINF/#DESCRIPTION /g' /tmp/test/Rus5.m3u > /tmp/test/Rus6.m3u
sed 's/:-1,/ /g' /tmp/test/Rus6.m3u > /tmp/test/Rus6a.m3u
sed 's/:0,/ /g' /tmp/test/Rus6a.m3u > /tmp/test/Rus6b.m3u
sed 's/:/%3a/g' /tmp/test/Rus6b.m3u > /tmp/test/Rus7.m3u
sed -e "s/http/#SERVICE 4097:0:1128:0:0:0:0:0:0:0:http/" /tmp/test/Rus7.m3u > /tmp/test/Rus7a.m3u
sed -e "s/rtmp/#SERVICE 4097:0:1128:0:0:0:0:0:0:0:rtmp/" /tmp/test/Rus7a.m3u > /tmp/test/Rus8.m3u
tr -d '["]' < "/tmp/test/Rus8.m3u" > /tmp/test/Rus8a.m3u
tr -d '[,]' < "/tmp/test/Rus8a.m3u" > /tmp/test/Rus8.m3u
awk '{print NR " " $0}' /tmp/test/Rus8.m3u  > /tmp/test/Rus9.m3u
sort -n -r "/tmp/test/Rus9.m3u"|grep -o -i '#[^<]*' > /tmp/test/Rus10.m3u
echo "#NAME Smart6.m3u" > /etc/enigma2/userbouquet.Smart6.m3u.tv
cat /tmp/test/Rus10.m3u >> /etc/enigma2/userbouquet.Smart6.m3u.tv
rm -rf /tmp/test
cd /
###########################################################################################################
more /usr/lib/enigma2/python/Plugins/Extensions/OpenPanel/DATA/x  >> /etc/enigma2/bouquets.tv 
sed -i "s/%/userbouquet.Smart7.m3u.tv/" /etc/enigma2/bouquets.tv 
[ -d /tmp/test ] || mkdir -p /tmp/test
cp /tmp/test2/7.m3u /tmp/test/x.m3u
echo ""
echo "converter Smart7.m3u for Enigma"
sleep 1
echo "start"
sed '1,1d' /tmp/test/x.m3u > /tmp/test/Rus.m3u
awk 'BEGIN {FS="png"}{print  $NF}'  /tmp/test/Rus.m3u > /tmp/test/Rus3.m3u
awk 'BEGIN {FS="group-"}{print  $NF}'  /tmp/test/Rus3.m3u > /tmp/test/Rus4.m3u
sed 's/",/#DESCRIPTION /g' /tmp/test/Rus4.m3u > /tmp/test/Rus5.m3u
sed 's/#EXTINF/#DESCRIPTION /g' /tmp/test/Rus5.m3u > /tmp/test/Rus6.m3u
sed 's/:-1,/ /g' /tmp/test/Rus6.m3u > /tmp/test/Rus6a.m3u
sed 's/:0,/ /g' /tmp/test/Rus6a.m3u > /tmp/test/Rus6b.m3u
sed 's/:/%3a/g' /tmp/test/Rus6b.m3u > /tmp/test/Rus7.m3u
sed -e "s/http/#SERVICE 4097:0:1128:0:0:0:0:0:0:0:http/" /tmp/test/Rus7.m3u > /tmp/test/Rus7a.m3u
sed -e "s/rtmp/#SERVICE 4097:0:1128:0:0:0:0:0:0:0:rtmp/" /tmp/test/Rus7a.m3u > /tmp/test/Rus8.m3u
tr -d '["]' < "/tmp/test/Rus8.m3u" > /tmp/test/Rus8a.m3u
tr -d '[,]' < "/tmp/test/Rus8a.m3u" > /tmp/test/Rus8.m3u
awk '{print NR " " $0}' /tmp/test/Rus8.m3u  > /tmp/test/Rus9.m3u
sort -n -r "/tmp/test/Rus9.m3u"|grep -o -i '#[^<]*' > /tmp/test/Rus10.m3u
echo "#NAME Smart7.m3u" > /etc/enigma2/userbouquet.Smart7.m3u.tv
cat /tmp/test/Rus10.m3u >> /etc/enigma2/userbouquet.Smart7.m3u.tv
rm -rf /tmp/test
cd /
###########################################################################################################
more /usr/lib/enigma2/python/Plugins/Extensions/OpenPanel/DATA/x  >> /etc/enigma2/bouquets.tv 
sed -i "s/%/userbouquet.Smart8.m3u.tv/" /etc/enigma2/bouquets.tv 
[ -d /tmp/test ] || mkdir -p /tmp/test
cp /tmp/test2/8.m3u /tmp/test/x.m3u
echo ""
echo "converter Smart8.m3u for Enigma"
sleep 1
echo "start"
sed '1,1d' /tmp/test/x.m3u > /tmp/test/Rus.m3u
awk 'BEGIN {FS="png"}{print  $NF}'  /tmp/test/Rus.m3u > /tmp/test/Rus3.m3u
awk 'BEGIN {FS="group-"}{print  $NF}'  /tmp/test/Rus3.m3u > /tmp/test/Rus4.m3u
sed 's/",/#DESCRIPTION /g' /tmp/test/Rus4.m3u > /tmp/test/Rus5.m3u
sed 's/#EXTINF/#DESCRIPTION /g' /tmp/test/Rus5.m3u > /tmp/test/Rus6.m3u
sed 's/:-1,/ /g' /tmp/test/Rus6.m3u > /tmp/test/Rus6a.m3u
sed 's/:0,/ /g' /tmp/test/Rus6a.m3u > /tmp/test/Rus6b.m3u
sed 's/:/%3a/g' /tmp/test/Rus6b.m3u > /tmp/test/Rus7.m3u
sed -e "s/http/#SERVICE 4097:0:1128:0:0:0:0:0:0:0:http/" /tmp/test/Rus7.m3u > /tmp/test/Rus7a.m3u
sed -e "s/rtmp/#SERVICE 4097:0:1128:0:0:0:0:0:0:0:rtmp/" /tmp/test/Rus7a.m3u > /tmp/test/Rus8.m3u
tr -d '["]' < "/tmp/test/Rus8.m3u" > /tmp/test/Rus8a.m3u
tr -d '[,]' < "/tmp/test/Rus8a.m3u" > /tmp/test/Rus8.m3u
awk '{print NR " " $0}' /tmp/test/Rus8.m3u  > /tmp/test/Rus9.m3u
sort -n -r "/tmp/test/Rus9.m3u"|grep -o -i '#[^<]*' > /tmp/test/Rus10.m3u
echo "#NAME Smart8.m3u" > /etc/enigma2/userbouquet.Smart8.m3u.tv
cat /tmp/test/Rus10.m3u >> /etc/enigma2/userbouquet.Smart8.m3u.tv
rm -rf /tmp/test
cd /
###########################################################################################################
more /usr/lib/enigma2/python/Plugins/Extensions/OpenPanel/DATA/x  >> /etc/enigma2/bouquets.tv 
sed -i "s/%/userbouquet.Smart9.m3u.tv/" /etc/enigma2/bouquets.tv 
[ -d /tmp/test ] || mkdir -p /tmp/test
cp /tmp/test2/9.m3u /tmp/test/x.m3u
echo ""
echo "converter Smart9.m3u for Enigma"
sleep 1
echo "start"
sed '1,1d' /tmp/test/x.m3u > /tmp/test/Rus.m3u
awk 'BEGIN {FS="png"}{print  $NF}'  /tmp/test/Rus.m3u > /tmp/test/Rus3.m3u
awk 'BEGIN {FS="group-"}{print  $NF}'  /tmp/test/Rus3.m3u > /tmp/test/Rus4.m3u
sed 's/",/#DESCRIPTION /g' /tmp/test/Rus4.m3u > /tmp/test/Rus5.m3u
sed 's/#EXTINF/#DESCRIPTION /g' /tmp/test/Rus5.m3u > /tmp/test/Rus6.m3u
sed 's/:-1,/ /g' /tmp/test/Rus6.m3u > /tmp/test/Rus6a.m3u
sed 's/:0,/ /g' /tmp/test/Rus6a.m3u > /tmp/test/Rus6b.m3u
sed 's/:/%3a/g' /tmp/test/Rus6b.m3u > /tmp/test/Rus7.m3u
sed -e "s/http/#SERVICE 4097:0:1128:0:0:0:0:0:0:0:http/" /tmp/test/Rus7.m3u > /tmp/test/Rus7a.m3u
sed -e "s/rtmp/#SERVICE 4097:0:1128:0:0:0:0:0:0:0:rtmp/" /tmp/test/Rus7a.m3u > /tmp/test/Rus8.m3u
tr -d '["]' < "/tmp/test/Rus8.m3u" > /tmp/test/Rus8a.m3u
tr -d '[,]' < "/tmp/test/Rus8a.m3u" > /tmp/test/Rus8.m3u
awk '{print NR " " $0}' /tmp/test/Rus8.m3u  > /tmp/test/Rus9.m3u
sort -n -r "/tmp/test/Rus9.m3u"|grep -o -i '#[^<]*' > /tmp/test/Rus10.m3u
echo "#NAME Smart9.m3u" > /etc/enigma2/userbouquet.Smart9.m3u.tv
cat /tmp/test/Rus10.m3u >> /etc/enigma2/userbouquet.Smart9.m3u.tv
rm -rf /tmp/test
cd /
###########################################################################################################
rm -rf /tmp/test2
wget -q -O - http://root%s@127.0.0.1/web/servicelistreload?mode=0 >>/dev/null 2>&1 </dev/null &
sleep 2
echo "OK"
exit







