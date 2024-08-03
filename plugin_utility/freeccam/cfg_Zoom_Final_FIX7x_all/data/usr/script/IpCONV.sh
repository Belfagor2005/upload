#!/bin/sh
echo "stahuji (m3u) IP"
echo ""
echo ""
[ -d /IPTV ] || mkdir -p /IPTV
rm -rf /IPTV
[ -d /IPTV ] || mkdir -p /IPTV
[ -d /tmp/test ] || mkdir -p /tmp/test
[ -d /IPTV/Ip ] || mkdir -p /IPTV/Ip
curl  -k -Lbk -A -k -m 8 -m 52 -s  https://hdbox.ws/com/news/43-ip-tv-kanaly.html?wpfb_list_page=1 > /tmp/test/CCcam
cd /tmp/test
grep -o -i 'https://hdbox.ws/?wpfb[^<]*' CCcam > iptv
cut -d'"' -f 1 iptv > iptv2
adresa1=`sed -n '1,1p' iptv2`
adresa1=$adresa1
curl -H "User-Agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_1) AppleWebKit/537.36 (K HTML, like Gecko) Chrome/61.0.3163.100 Safari/537.36" --referer "https://hdbox.ws/" $adresa1 > /IPTV/Ip/ip1.m3u
adresa2=`sed -n '2,2p' iptv2`
adresa2=$adresa2
curl -H "User-Agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_1) AppleWebKit/537.36 (K HTML, like Gecko) Chrome/61.0.3163.100 Safari/537.36" --referer "https://hdbox.ws/" $adresa2 > /IPTV/Ip/ip2.m3u
adresa3=`sed -n '3,3p' iptv2`
adresa3=$adresa3
curl -H "User-Agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_1) AppleWebKit/537.36 (K HTML, like Gecko) Chrome/61.0.3163.100 Safari/537.36" --referer "https://hdbox.ws/" $adresa3 > /IPTV/Ip/ip3.m3u
adresa4=`sed -n '4,4p' iptv2`
adresa4=$adresa4
curl -H "User-Agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_1) AppleWebKit/537.36 (K HTML, like Gecko) Chrome/61.0.3163.100 Safari/537.36" --referer "https://hdbox.ws/" $adresa4 > /IPTV/Ip/ip4.m3u
adresa5=`sed -n '5,5p' iptv2`
adresa5=$adresa5
curl -H "User-Agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_1) AppleWebKit/537.36 (K HTML, like Gecko) Chrome/61.0.3163.100 Safari/537.36" --referer "https://hdbox.ws/" $adresa5 > /IPTV/Ip/ip5.m3u
adresa6=`sed -n '6,6p' iptv2`
adresa6=$adresa6
curl -H "User-Agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_1) AppleWebKit/537.36 (K HTML, like Gecko) Chrome/61.0.3163.100 Safari/537.36" --referer "https://hdbox.ws/" $adresa6 > /IPTV/Ip/ip6.m3u
adresa7=`sed -n '7,7p' iptv2`
adresa7=$adresa7
curl -H "User-Agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_1) AppleWebKit/537.36 (K HTML, like Gecko) Chrome/61.0.3163.100 Safari/537.36" --referer "https://hdbox.ws/" $adresa7 > /IPTV/Ip/ip7.m3u
###########################################
curl  -k -Lbk -A -k -m 8 -m 52 -s  https://hdbox.ws/com/news/43-ip-tv-kanaly.html?wpfb_list_page=2 > /tmp/test/CCcam
cd /tmp/test
grep -o -i 'https://hdbox.ws/?wpfb[^<]*' CCcam > iptv
cut -d'"' -f 1 iptv > iptv2
adresa1=`sed -n '1,1p' iptv2`
adresa1=$adresa1
curl -H "User-Agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_1) AppleWebKit/537.36 (K HTML, like Gecko) Chrome/61.0.3163.100 Safari/537.36" --referer "https://hdbox.ws/" $adresa1 > /IPTV/Ip/ip8.m3u
adresa2=`sed -n '2,2p' iptv2`
adresa2=$adresa2
curl -H "User-Agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_1) AppleWebKit/537.36 (K HTML, like Gecko) Chrome/61.0.3163.100 Safari/537.36" --referer "https://hdbox.ws/" $adresa2 > /IPTV/Ip/ip9.m3u
adresa3=`sed -n '3,3p' iptv2`
adresa3=$adresa3
curl -H "User-Agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_1) AppleWebKit/537.36 (K HTML, like Gecko) Chrome/61.0.3163.100 Safari/537.36" --referer "https://hdbox.ws/" $adresa3 > /IPTV/Ip/ip10.m3u

cd /
rm -rf /tmp/test
###########################################################################################################
more /usr/lib/enigma2/python/Plugins/Extensions/OpenPanel/DATA/x  >> /etc/enigma2/bouquets.tv 
sed -i "s/%/userbouquet.Ip1.m3u.tv/" /etc/enigma2/bouquets.tv 
[ -d /tmp/test ] || mkdir -p /tmp/test
cp /IPTV/Ip/ip1.m3u /tmp/test/x.m3u
echo ""
echo "converter Ip1.m3u for Enigma"
sleep 1
echo "start"
awk 'BEGIN {FS="png"}{print  $NF}'  /tmp/test/x.m3u > /tmp/test/Rus3.m3u
awk 'BEGIN {FS="group-"}{print  $NF}'  /tmp/test/Rus3.m3u > /tmp/test/Rus4.m3u
sed 's/",/#DESCRIPTION /g' /tmp/test/Rus4.m3u > /tmp/test/Rus5.m3u
sed 's/#EXTINF/#DESCRIPTION /g' /tmp/test/Rus5.m3u > /tmp/test/Rus5a.m3u
sed 's/:-1 ,/ /g' /tmp/test/Rus5a.m3u > /tmp/test/Rus6.m3u
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
echo "#NAME Ip1.m3u" > /etc/enigma2/userbouquet.Ip1.m3u.tv
cat /tmp/test/Rus10.m3u >> /etc/enigma2/userbouquet.Ip1.m3u.tv
rm -rf /tmp/test
cd /
###########################################################################################################
more /usr/lib/enigma2/python/Plugins/Extensions/OpenPanel/DATA/x  >> /etc/enigma2/bouquets.tv 
sed -i "s/%/userbouquet.Ip2.m3u.tv/" /etc/enigma2/bouquets.tv 
[ -d /tmp/test ] || mkdir -p /tmp/test
cp /IPTV/Ip/ip2.m3u /tmp/test/x.m3u
echo ""
echo "converter Ip2.m3u for Enigma"
sleep 1
echo "start"
awk 'BEGIN {FS="png"}{print  $NF}'  /tmp/test/x.m3u > /tmp/test/Rus3.m3u
awk 'BEGIN {FS="group-"}{print  $NF}'  /tmp/test/Rus3.m3u > /tmp/test/Rus4.m3u
sed 's/",/#DESCRIPTION /g' /tmp/test/Rus4.m3u > /tmp/test/Rus5.m3u
sed 's/#EXTINF/#DESCRIPTION /g' /tmp/test/Rus5.m3u > /tmp/test/Rus5a.m3u
sed 's/:-1 ,/ /g' /tmp/test/Rus5a.m3u > /tmp/test/Rus6.m3u
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
echo "#NAME Ip2.m3u" > /etc/enigma2/userbouquet.Ip2.m3u.tv
cat /tmp/test/Rus10.m3u >> /etc/enigma2/userbouquet.Ip2.m3u.tv
rm -rf /tmp/test
cd /
###########################################################################################################
more /usr/lib/enigma2/python/Plugins/Extensions/OpenPanel/DATA/x  >> /etc/enigma2/bouquets.tv 
sed -i "s/%/userbouquet.Ip3.m3u.tv/" /etc/enigma2/bouquets.tv 
[ -d /tmp/test ] || mkdir -p /tmp/test
cp /IPTV/Ip/ip3.m3u /tmp/test/x.m3u
echo ""
echo "converter Ip3.m3u for Enigma"
sleep 1
echo "start"
awk 'BEGIN {FS="png"}{print  $NF}'  /tmp/test/x.m3u > /tmp/test/Rus3.m3u
awk 'BEGIN {FS="group-"}{print  $NF}'  /tmp/test/Rus3.m3u > /tmp/test/Rus4.m3u
sed 's/",/#DESCRIPTION /g' /tmp/test/Rus4.m3u > /tmp/test/Rus5.m3u
sed 's/#EXTINF/#DESCRIPTION /g' /tmp/test/Rus5.m3u > /tmp/test/Rus5a.m3u
sed 's/:-1 ,/ /g' /tmp/test/Rus5a.m3u > /tmp/test/Rus6.m3u
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
echo "#NAME Ip3.m3u" > /etc/enigma2/userbouquet.Ip3.m3u.tv
cat /tmp/test/Rus10.m3u >> /etc/enigma2/userbouquet.Ip3.m3u.tv
rm -rf /tmp/test
cd /
###########################################################################################################
more /usr/lib/enigma2/python/Plugins/Extensions/OpenPanel/DATA/x  >> /etc/enigma2/bouquets.tv 
sed -i "s/%/userbouquet.Ip4.m3u.tv/" /etc/enigma2/bouquets.tv 
[ -d /tmp/test ] || mkdir -p /tmp/test
cp /IPTV/Ip/ip4.m3u /tmp/test/x.m3u
echo ""
echo "converter Ip4.m3u for Enigma"
sleep 1
echo "start"
awk 'BEGIN {FS="png"}{print  $NF}'  /tmp/test/x.m3u > /tmp/test/Rus3.m3u
awk 'BEGIN {FS="group-"}{print  $NF}'  /tmp/test/Rus3.m3u > /tmp/test/Rus4.m3u
sed 's/",/#DESCRIPTION /g' /tmp/test/Rus4.m3u > /tmp/test/Rus5.m3u
sed 's/#EXTINF/#DESCRIPTION /g' /tmp/test/Rus5.m3u > /tmp/test/Rus5a.m3u
sed 's/:-1 ,/ /g' /tmp/test/Rus5a.m3u > /tmp/test/Rus6.m3u
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
echo "#NAME Ip4.m3u" > /etc/enigma2/userbouquet.Ip4.m3u.tv
cat /tmp/test/Rus10.m3u >> /etc/enigma2/userbouquet.Ip4.m3u.tv
rm -rf /tmp/test
cd /
###########################################################################################################
more /usr/lib/enigma2/python/Plugins/Extensions/OpenPanel/DATA/x  >> /etc/enigma2/bouquets.tv 
sed -i "s/%/userbouquet.Ip5.m3u.tv/" /etc/enigma2/bouquets.tv 
[ -d /tmp/test ] || mkdir -p /tmp/test
cp /IPTV/Ip/ip5.m3u /tmp/test/x.m3u
echo ""
echo "converter Ip5.m3u for Enigma"
sleep 1
echo "start"
awk 'BEGIN {FS="png"}{print  $NF}'  /tmp/test/x.m3u > /tmp/test/Rus3.m3u
awk 'BEGIN {FS="group-"}{print  $NF}'  /tmp/test/Rus3.m3u > /tmp/test/Rus4.m3u
sed 's/",/#DESCRIPTION /g' /tmp/test/Rus4.m3u > /tmp/test/Rus5.m3u
sed 's/#EXTINF/#DESCRIPTION /g' /tmp/test/Rus5.m3u > /tmp/test/Rus5a.m3u
sed 's/:-1 ,/ /g' /tmp/test/Rus5a.m3u > /tmp/test/Rus6.m3u
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
echo "#NAME Ip5.m3u" > /etc/enigma2/userbouquet.Ip5.m3u.tv
cat /tmp/test/Rus10.m3u >> /etc/enigma2/userbouquet.Ip5.m3u.tv
rm -rf /tmp/test
cd /
###########################################################################################################
more /usr/lib/enigma2/python/Plugins/Extensions/OpenPanel/DATA/x  >> /etc/enigma2/bouquets.tv 
sed -i "s/%/userbouquet.Ip6.m3u.tv/" /etc/enigma2/bouquets.tv 
[ -d /tmp/test ] || mkdir -p /tmp/test
cp /IPTV/Ip/ip6.m3u /tmp/test/x.m3u
echo ""
echo "converter Ip6.m3u for Enigma"
sleep 1
echo "start"
awk 'BEGIN {FS="png"}{print  $NF}'  /tmp/test/x.m3u > /tmp/test/Rus3.m3u
awk 'BEGIN {FS="group-"}{print  $NF}'  /tmp/test/Rus3.m3u > /tmp/test/Rus4.m3u
sed 's/",/#DESCRIPTION /g' /tmp/test/Rus4.m3u > /tmp/test/Rus5.m3u
sed 's/#EXTINF/#DESCRIPTION /g' /tmp/test/Rus5.m3u > /tmp/test/Rus5a.m3u
sed 's/:-1 ,/ /g' /tmp/test/Rus5a.m3u > /tmp/test/Rus6.m3u
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
echo "#NAME Ip6.m3u" > /etc/enigma2/userbouquet.Ip6.m3u.tv
cat /tmp/test/Rus10.m3u >> /etc/enigma2/userbouquet.Ip6.m3u.tv
rm -rf /tmp/test
cd /
###########################################################################################################
more /usr/lib/enigma2/python/Plugins/Extensions/OpenPanel/DATA/x  >> /etc/enigma2/bouquets.tv 
sed -i "s/%/userbouquet.Ip7.m3u.tv/" /etc/enigma2/bouquets.tv 
[ -d /tmp/test ] || mkdir -p /tmp/test
cp /IPTV/Ip/ip7.m3u /tmp/test/x.m3u
echo ""
echo "converter Ip7.m3u for Enigma"
sleep 1
echo "start"
awk 'BEGIN {FS="png"}{print  $NF}'  /tmp/test/x.m3u > /tmp/test/Rus3.m3u
awk 'BEGIN {FS="group-"}{print  $NF}'  /tmp/test/Rus3.m3u > /tmp/test/Rus4.m3u
sed 's/",/#DESCRIPTION /g' /tmp/test/Rus4.m3u > /tmp/test/Rus5.m3u
sed 's/#EXTINF/#DESCRIPTION /g' /tmp/test/Rus5.m3u > /tmp/test/Rus5a.m3u
sed 's/:-1 ,/ /g' /tmp/test/Rus5a.m3u > /tmp/test/Rus6.m3u
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
echo "#NAME Ip7.m3u" > /etc/enigma2/userbouquet.Ip7.m3u.tv
cat /tmp/test/Rus10.m3u >> /etc/enigma2/userbouquet.Ip7.m3u.tv
rm -rf /tmp/test
cd /
###########################################################################################################
more /usr/lib/enigma2/python/Plugins/Extensions/OpenPanel/DATA/x  >> /etc/enigma2/bouquets.tv 
sed -i "s/%/userbouquet.Ip8.m3u.tv/" /etc/enigma2/bouquets.tv 
[ -d /tmp/test ] || mkdir -p /tmp/test
cp /IPTV/Ip/ip8.m3u /tmp/test/x.m3u
echo ""
echo "converter Ip8.m3u for Enigma"
sleep 1
echo "start"
awk 'BEGIN {FS="png"}{print  $NF}'  /tmp/test/x.m3u > /tmp/test/Rus3.m3u
awk 'BEGIN {FS="group-"}{print  $NF}'  /tmp/test/Rus3.m3u > /tmp/test/Rus4.m3u
sed 's/",/#DESCRIPTION /g' /tmp/test/Rus4.m3u > /tmp/test/Rus5.m3u
sed 's/#EXTINF/#DESCRIPTION /g' /tmp/test/Rus5.m3u > /tmp/test/Rus5a.m3u
sed 's/:-1 ,/ /g' /tmp/test/Rus5a.m3u > /tmp/test/Rus6.m3u
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
echo "#NAME Ip8.m3u" > /etc/enigma2/userbouquet.Ip8.m3u.tv
cat /tmp/test/Rus10.m3u >> /etc/enigma2/userbouquet.Ip8.m3u.tv
rm -rf /tmp/test
cd /
###########################################################################################################
more /usr/lib/enigma2/python/Plugins/Extensions/OpenPanel/DATA/x  >> /etc/enigma2/bouquets.tv 
sed -i "s/%/userbouquet.Ip9.m3u.tv/" /etc/enigma2/bouquets.tv 
[ -d /tmp/test ] || mkdir -p /tmp/test
cp /IPTV/Ip/ip9.m3u /tmp/test/x.m3u
echo ""
echo "converter Ip9.m3u for Enigma"
sleep 1
echo "start"
awk 'BEGIN {FS="png"}{print  $NF}'  /tmp/test/x.m3u > /tmp/test/Rus3.m3u
awk 'BEGIN {FS="group-"}{print  $NF}'  /tmp/test/Rus3.m3u > /tmp/test/Rus4.m3u
sed 's/",/#DESCRIPTION /g' /tmp/test/Rus4.m3u > /tmp/test/Rus5.m3u
sed 's/#EXTINF/#DESCRIPTION /g' /tmp/test/Rus5.m3u > /tmp/test/Rus5a.m3u
sed 's/:-1 ,/ /g' /tmp/test/Rus5a.m3u > /tmp/test/Rus6.m3u
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
echo "#NAME Ip9.m3u" > /etc/enigma2/userbouquet.Ip9.m3u.tv
cat /tmp/test/Rus10.m3u >> /etc/enigma2/userbouquet.Ip9.m3u.tv
rm -rf /tmp/test
cd /
###########################################################################################################
more /usr/lib/enigma2/python/Plugins/Extensions/OpenPanel/DATA/x  >> /etc/enigma2/bouquets.tv 
sed -i "s/%/userbouquet.Ip10.m3u.tv/" /etc/enigma2/bouquets.tv 
[ -d /tmp/test ] || mkdir -p /tmp/test
cp /IPTV/Ip/ip10.m3u /tmp/test/x.m3u
echo ""
echo "converter Ip10.m3u for Enigma"
sleep 1
echo "start"
awk 'BEGIN {FS="png"}{print  $NF}'  /tmp/test/x.m3u > /tmp/test/Rus3.m3u
awk 'BEGIN {FS="group-"}{print  $NF}'  /tmp/test/Rus3.m3u > /tmp/test/Rus4.m3u
sed 's/",/#DESCRIPTION /g' /tmp/test/Rus4.m3u > /tmp/test/Rus5.m3u
sed 's/#EXTINF/#DESCRIPTION /g' /tmp/test/Rus5.m3u > /tmp/test/Rus5a.m3u
sed 's/:-1 ,/ /g' /tmp/test/Rus5a.m3u > /tmp/test/Rus6.m3u
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
echo "#NAME Ip10.m3u" > /etc/enigma2/userbouquet.Ip10.m3u.tv
cat /tmp/test/Rus10.m3u >> /etc/enigma2/userbouquet.Ip10.m3u.tv
rm -rf /tmp/test
cd /
###########################################################################################################
wget -q -O - http://root%s@127.0.0.1/web/servicelistreload?mode=0 >>/dev/null 2>&1 </dev/null &
sleep 2
echo "OK"
exit







