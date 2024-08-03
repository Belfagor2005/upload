#!/bin/sh
sleep 1
echo "stahuji stream list MUSIC"
sleep 1
echo ""
echo "download stream sheet MUSIC"
sleep 2
echo ""
#################################################
more /usr/lib/enigma2/python/Plugins/Extensions/OpenPanel/DATA/x  >> /etc/enigma2/bouquets.tv 
sed -i "s/%/userbouquet.MUSIC.m3u.tv/" /etc/enigma2/bouquets.tv 
#################################################
[ -d /tmp/test ] || mkdir -p /tmp/test
cd /tmp/test
#################################################
curl -Lbk -m 4555 -m 6555 -k  https://music.163.com/artist/mv?id=964321 > /tmp/test/x
awk '/"tit f-thide s-fc0"/ {print}' x > y
grep -o -i '/mv?id=[^"<]*' y > www
#################################################
#################################################
adresa1=`sed -n '1,1p' www`
adresa1=$adresa1
curl -Lbk -m 4555 -m 6555 -k  https://music.163.com$adresa1 > /tmp/test/x1
cd /tmp/test
awk '/og:video/ {print}' x1 > x2
grep -o -i 'http[^"<]*' x2 > seznam
awk '/"title":/ {print}' x1 >> seznam
#################################################
adresa1=`sed -n '2,2p' www`
adresa1=$adresa1
curl -Lbk -m 4555 -m 6555 -k  https://music.163.com$adresa1 > /tmp/test/x1
cd /tmp/test
awk '/og:video/ {print}' x1 > x2
grep -o -i 'http[^"<]*' x2 >> seznam
awk '/"title":/ {print}' x1 >> seznam
#################################################
adresa1=`sed -n '3,3p' www`
adresa1=$adresa1
curl -Lbk -m 4555 -m 6555 -k  https://music.163.com$adresa1 > /tmp/test/x1
cd /tmp/test
awk '/og:video/ {print}' x1 > x2
grep -o -i 'http[^"<]*' x2 >> seznam
awk '/"title":/ {print}' x1 >> seznam
#################################################
adresa1=`sed -n '4,4p' www`
adresa1=$adresa1
curl -Lbk -m 4555 -m 6555 -k  https://music.163.com$adresa1 > /tmp/test/x1
cd /tmp/test
awk '/og:video/ {print}' x1 > x2
grep -o -i 'http[^"<]*' x2 >> seznam
awk '/"title":/ {print}' x1 >> seznam
#################################################
adresa1=`sed -n '5,5p' www`
adresa1=$adresa1
curl -Lbk -m 4555 -m 6555 -k  https://music.163.com$adresa1 > /tmp/test/x1
cd /tmp/test
awk '/og:video/ {print}' x1 > x2
grep -o -i 'http[^"<]*' x2 >> seznam
awk '/"title":/ {print}' x1 >> seznam
#################################################
adresa1=`sed -n '6,6p' www`
adresa1=$adresa1
curl -Lbk -m 4555 -m 6555 -k  https://music.163.com$adresa1 > /tmp/test/x1
cd /tmp/test
awk '/og:video/ {print}' x1 > x2
grep -o -i 'http[^"<]*' x2 >> seznam
awk '/"title":/ {print}' x1 >> seznam
#################################################
adresa1=`sed -n '7,7p' www`
adresa1=$adresa1
curl -Lbk -m 4555 -m 6555 -k  https://music.163.com$adresa1 > /tmp/test/x1
cd /tmp/test
awk '/og:video/ {print}' x1 > x2
grep -o -i 'http[^"<]*' x2 >> seznam
awk '/"title":/ {print}' x1 >> seznam
#################################################
adresa1=`sed -n '8,8p' www`
adresa1=$adresa1
curl -Lbk -m 4555 -m 6555 -k  https://music.163.com$adresa1 > /tmp/test/x1
cd /tmp/test
awk '/og:video/ {print}' x1 > x2
grep -o -i 'http[^"<]*' x2 >> seznam
awk '/"title":/ {print}' x1 >> seznam
#################################################
adresa1=`sed -n '9,9p' www`
adresa1=$adresa1
curl -Lbk -m 4555 -m 6555 -k  https://music.163.com$adresa1 > /tmp/test/x1
cd /tmp/test
awk '/og:video/ {print}' x1 > x2
grep -o -i 'http[^"<]*' x2 >> seznam
awk '/"title":/ {print}' x1 >> seznam
#################################################
adresa1=`sed -n '10,10p' www`
adresa1=$adresa1
curl -Lbk -m 4555 -m 6555 -k  https://music.163.com$adresa1 > /tmp/test/x1
cd /tmp/test
awk '/og:video/ {print}' x1 > x2
grep -o -i 'http[^"<]*' x2 >> seznam
awk '/"title":/ {print}' x1 >> seznam
#################################################
adresa1=`sed -n '11,11p' www`
adresa1=$adresa1
curl -Lbk -m 4555 -m 6555 -k  https://music.163.com$adresa1 > /tmp/test/x1
cd /tmp/test
awk '/og:video/ {print}' x1 > x2
grep -o -i 'http[^"<]*' x2 >> seznam
awk '/"title":/ {print}' x1 >> seznam
#################################################
adresa1=`sed -n '12,12p' www`
adresa1=$adresa1
curl -Lbk -m 4555 -m 6555 -k  https://music.163.com$adresa1 > /tmp/test/x1
cd /tmp/test
awk '/og:video/ {print}' x1 > x2
grep -o -i 'http[^"<]*' x2 >> seznam
awk '/"title":/ {print}' x1 >> seznam
#################################################
#################################################
cd /tmp/test
curl -A "Mozilla/2.02E (Win95; U)" -e "http://music.163.com" "https://music.163.com/artist/mv?id=964321&limit=12&offset=12" > /tmp/test/x  
awk '/"tit f-thide s-fc0"/ {print}' x > y
grep -o -i '/mv?id=[^"<]*' y > www
#################################################
#################################################
adresa1=`sed -n '1,1p' www`
adresa1=$adresa1
curl -Lbk -m 4555 -m 6555 -k  https://music.163.com$adresa1 > /tmp/test/x1
cd /tmp/test
awk '/og:video/ {print}' x1 > x2
grep -o -i 'http[^"<]*' x2 >> seznam
awk '/"title":/ {print}' x1 >> seznam
#################################################
adresa1=`sed -n '2,2p' www`
adresa1=$adresa1
curl -Lbk -m 4555 -m 6555 -k  https://music.163.com$adresa1 > /tmp/test/x1
cd /tmp/test
awk '/og:video/ {print}' x1 > x2
grep -o -i 'http[^"<]*' x2 >> seznam
awk '/"title":/ {print}' x1 >> seznam
#################################################
adresa1=`sed -n '3,3p' www`
adresa1=$adresa1
curl -Lbk -m 4555 -m 6555 -k  https://music.163.com$adresa1 > /tmp/test/x1
cd /tmp/test
awk '/og:video/ {print}' x1 > x2
grep -o -i 'http[^"<]*' x2 >> seznam
awk '/"title":/ {print}' x1 >> seznam
#################################################
adresa1=`sed -n '4,4p' www`
adresa1=$adresa1
curl -Lbk -m 4555 -m 6555 -k  https://music.163.com$adresa1 > /tmp/test/x1
cd /tmp/test
awk '/og:video/ {print}' x1 > x2
grep -o -i 'http[^"<]*' x2 >> seznam
awk '/"title":/ {print}' x1 >> seznam
#################################################
adresa1=`sed -n '5,5p' www`
adresa1=$adresa1
curl -Lbk -m 4555 -m 6555 -k  https://music.163.com$adresa1 > /tmp/test/x1
cd /tmp/test
awk '/og:video/ {print}' x1 > x2
grep -o -i 'http[^"<]*' x2 >> seznam
awk '/"title":/ {print}' x1 >> seznam
#################################################
adresa1=`sed -n '6,6p' www`
adresa1=$adresa1
curl -Lbk -m 4555 -m 6555 -k  https://music.163.com$adresa1 > /tmp/test/x1
cd /tmp/test
awk '/og:video/ {print}' x1 > x2
grep -o -i 'http[^"<]*' x2 >> seznam
awk '/"title":/ {print}' x1 >> seznam
#################################################
adresa1=`sed -n '7,7p' www`
adresa1=$adresa1
curl -Lbk -m 4555 -m 6555 -k  https://music.163.com$adresa1 > /tmp/test/x1
cd /tmp/test
awk '/og:video/ {print}' x1 > x2
grep -o -i 'http[^"<]*' x2 >> seznam
awk '/"title":/ {print}' x1 >> seznam
#################################################
adresa1=`sed -n '8,8p' www`
adresa1=$adresa1
curl -Lbk -m 4555 -m 6555 -k  https://music.163.com$adresa1 > /tmp/test/x1
cd /tmp/test
awk '/og:video/ {print}' x1 > x2
grep -o -i 'http[^"<]*' x2 >> seznam
awk '/"title":/ {print}' x1 >> seznam
#################################################
adresa1=`sed -n '9,9p' www`
adresa1=$adresa1
curl -Lbk -m 4555 -m 6555 -k  https://music.163.com$adresa1 > /tmp/test/x1
cd /tmp/test
awk '/og:video/ {print}' x1 > x2
grep -o -i 'http[^"<]*' x2 >> seznam
awk '/"title":/ {print}' x1 >> seznam
#################################################
adresa1=`sed -n '10,10p' www`
adresa1=$adresa1
curl -Lbk -m 4555 -m 6555 -k  https://music.163.com$adresa1 > /tmp/test/x1
cd /tmp/test
awk '/og:video/ {print}' x1 > x2
grep -o -i 'http[^"<]*' x2 >> seznam
awk '/"title":/ {print}' x1 >> seznam
#################################################
adresa1=`sed -n '11,11p' www`
adresa1=$adresa1
curl -Lbk -m 4555 -m 6555 -k  https://music.163.com$adresa1 > /tmp/test/x1
cd /tmp/test
awk '/og:video/ {print}' x1 > x2
grep -o -i 'http[^"<]*' x2 >> seznam
awk '/"title":/ {print}' x1 >> seznam
#################################################
adresa1=`sed -n '12,12p' www`
adresa1=$adresa1
curl -Lbk -m 4555 -m 6555 -k  https://music.163.com$adresa1 > /tmp/test/x1
cd /tmp/test
awk '/og:video/ {print}' x1 > x2
grep -o -i 'http[^"<]*' x2 >> seznam
awk '/"title":/ {print}' x1 >> seznam
#################################################
#################################################
#################################################
#################################################
cd /tmp/test
curl -A "Mozilla/2.02E (Win95; U)" -e "http://music.163.com" "https://music.163.com/artist/mv?id=964321&limit=12&offset=24" > /tmp/test/x  
awk '/"tit f-thide s-fc0"/ {print}' x > y
grep -o -i '/mv?id=[^"<]*' y > www
#################################################
#################################################
adresa1=`sed -n '1,1p' www`
adresa1=$adresa1
curl -Lbk -m 4555 -m 6555 -k  https://music.163.com$adresa1 > /tmp/test/x1
cd /tmp/test
awk '/og:video/ {print}' x1 > x2
grep -o -i 'http[^"<]*' x2 >> seznam
awk '/"title":/ {print}' x1 >> seznam
#################################################
adresa1=`sed -n '2,2p' www`
adresa1=$adresa1
curl -Lbk -m 4555 -m 6555 -k  https://music.163.com$adresa1 > /tmp/test/x1
cd /tmp/test
awk '/og:video/ {print}' x1 > x2
grep -o -i 'http[^"<]*' x2 >> seznam
awk '/"title":/ {print}' x1 >> seznam
#################################################
adresa1=`sed -n '3,3p' www`
adresa1=$adresa1
curl -Lbk -m 4555 -m 6555 -k  https://music.163.com$adresa1 > /tmp/test/x1
cd /tmp/test
awk '/og:video/ {print}' x1 > x2
grep -o -i 'http[^"<]*' x2 >> seznam
awk '/"title":/ {print}' x1 >> seznam
#################################################
adresa1=`sed -n '4,4p' www`
adresa1=$adresa1
curl -Lbk -m 4555 -m 6555 -k  https://music.163.com$adresa1 > /tmp/test/x1
cd /tmp/test
awk '/og:video/ {print}' x1 > x2
grep -o -i 'http[^"<]*' x2 >> seznam
awk '/"title":/ {print}' x1 >> seznam
#################################################
adresa1=`sed -n '5,5p' www`
adresa1=$adresa1
curl -Lbk -m 4555 -m 6555 -k  https://music.163.com$adresa1 > /tmp/test/x1
cd /tmp/test
awk '/og:video/ {print}' x1 > x2
grep -o -i 'http[^"<]*' x2 >> seznam
awk '/"title":/ {print}' x1 >> seznam
#################################################
adresa1=`sed -n '6,6p' www`
adresa1=$adresa1
curl -Lbk -m 4555 -m 6555 -k  https://music.163.com$adresa1 > /tmp/test/x1
cd /tmp/test
awk '/og:video/ {print}' x1 > x2
grep -o -i 'http[^"<]*' x2 >> seznam
awk '/"title":/ {print}' x1 >> seznam
#################################################
adresa1=`sed -n '7,7p' www`
adresa1=$adresa1
curl -Lbk -m 4555 -m 6555 -k  https://music.163.com$adresa1 > /tmp/test/x1
cd /tmp/test
awk '/og:video/ {print}' x1 > x2
grep -o -i 'http[^"<]*' x2 >> seznam
awk '/"title":/ {print}' x1 >> seznam
#################################################
adresa1=`sed -n '8,8p' www`
adresa1=$adresa1
curl -Lbk -m 4555 -m 6555 -k  https://music.163.com$adresa1 > /tmp/test/x1
cd /tmp/test
awk '/og:video/ {print}' x1 > x2
grep -o -i 'http[^"<]*' x2 >> seznam
awk '/"title":/ {print}' x1 >> seznam
#################################################
adresa1=`sed -n '9,9p' www`
adresa1=$adresa1
curl -Lbk -m 4555 -m 6555 -k  https://music.163.com$adresa1 > /tmp/test/x1
cd /tmp/test
awk '/og:video/ {print}' x1 > x2
grep -o -i 'http[^"<]*' x2 >> seznam
awk '/"title":/ {print}' x1 >> seznam
#################################################
adresa1=`sed -n '10,10p' www`
adresa1=$adresa1
curl -Lbk -m 4555 -m 6555 -k  https://music.163.com$adresa1 > /tmp/test/x1
cd /tmp/test
awk '/og:video/ {print}' x1 > x2
grep -o -i 'http[^"<]*' x2 >> seznam
awk '/"title":/ {print}' x1 >> seznam
#################################################
adresa1=`sed -n '11,11p' www`
adresa1=$adresa1
curl -Lbk -m 4555 -m 6555 -k  https://music.163.com$adresa1 > /tmp/test/x1
cd /tmp/test
awk '/og:video/ {print}' x1 > x2
grep -o -i 'http[^"<]*' x2 >> seznam
awk '/"title":/ {print}' x1 >> seznam
#################################################
adresa1=`sed -n '12,12p' www`
adresa1=$adresa1
curl -Lbk -m 4555 -m 6555 -k  https://music.163.com$adresa1 > /tmp/test/x1
cd /tmp/test
awk '/og:video/ {print}' x1 > x2
grep -o -i 'http[^"<]*' x2 >> seznam
awk '/"title":/ {print}' x1 >> seznam
#################################################
#################################################
#################################################
#################################################
#################################################
#################################################
cd /tmp/test
curl -A "Mozilla/2.02E (Win95; U)" -e "http://music.163.com" "https://music.163.com/artist/mv?id=964321&limit=12&offset=36" > /tmp/test/x  
awk '/"tit f-thide s-fc0"/ {print}' x > y
grep -o -i '/mv?id=[^"<]*' y > www
#################################################
#################################################
adresa1=`sed -n '1,1p' www`
adresa1=$adresa1
curl -Lbk -m 4555 -m 6555 -k  https://music.163.com$adresa1 > /tmp/test/x1
cd /tmp/test
awk '/og:video/ {print}' x1 > x2
grep -o -i 'http[^"<]*' x2 >> seznam
awk '/"title":/ {print}' x1 >> seznam
#################################################
adresa1=`sed -n '2,2p' www`
adresa1=$adresa1
curl -Lbk -m 4555 -m 6555 -k  https://music.163.com$adresa1 > /tmp/test/x1
cd /tmp/test
awk '/og:video/ {print}' x1 > x2
grep -o -i 'http[^"<]*' x2 >> seznam
awk '/"title":/ {print}' x1 >> seznam
#################################################
adresa1=`sed -n '3,3p' www`
adresa1=$adresa1
curl -Lbk -m 4555 -m 6555 -k  https://music.163.com$adresa1 > /tmp/test/x1
cd /tmp/test
awk '/og:video/ {print}' x1 > x2
grep -o -i 'http[^"<]*' x2 >> seznam
awk '/"title":/ {print}' x1 >> seznam
#################################################
adresa1=`sed -n '4,4p' www`
adresa1=$adresa1
curl -Lbk -m 4555 -m 6555 -k  https://music.163.com$adresa1 > /tmp/test/x1
cd /tmp/test
awk '/og:video/ {print}' x1 > x2
grep -o -i 'http[^"<]*' x2 >> seznam
awk '/"title":/ {print}' x1 >> seznam
#################################################
adresa1=`sed -n '5,5p' www`
adresa1=$adresa1
curl -Lbk -m 4555 -m 6555 -k  https://music.163.com$adresa1 > /tmp/test/x1
cd /tmp/test
awk '/og:video/ {print}' x1 > x2
grep -o -i 'http[^"<]*' x2 >> seznam
awk '/"title":/ {print}' x1 >> seznam
#################################################
adresa1=`sed -n '6,6p' www`
adresa1=$adresa1
curl -Lbk -m 4555 -m 6555 -k  https://music.163.com$adresa1 > /tmp/test/x1
cd /tmp/test
awk '/og:video/ {print}' x1 > x2
grep -o -i 'http[^"<]*' x2 >> seznam
awk '/"title":/ {print}' x1 >> seznam
#################################################
adresa1=`sed -n '7,7p' www`
adresa1=$adresa1
curl -Lbk -m 4555 -m 6555 -k  https://music.163.com$adresa1 > /tmp/test/x1
cd /tmp/test
awk '/og:video/ {print}' x1 > x2
grep -o -i 'http[^"<]*' x2 >> seznam
awk '/"title":/ {print}' x1 >> seznam
#################################################
adresa1=`sed -n '8,8p' www`
adresa1=$adresa1
curl -Lbk -m 4555 -m 6555 -k  https://music.163.com$adresa1 > /tmp/test/x1
cd /tmp/test
awk '/og:video/ {print}' x1 > x2
grep -o -i 'http[^"<]*' x2 >> seznam
awk '/"title":/ {print}' x1 >> seznam
#################################################
adresa1=`sed -n '9,9p' www`
adresa1=$adresa1
curl -Lbk -m 4555 -m 6555 -k  https://music.163.com$adresa1 > /tmp/test/x1
cd /tmp/test
awk '/og:video/ {print}' x1 > x2
grep -o -i 'http[^"<]*' x2 >> seznam
awk '/"title":/ {print}' x1 >> seznam
#################################################
adresa1=`sed -n '10,10p' www`
adresa1=$adresa1
curl -Lbk -m 4555 -m 6555 -k  https://music.163.com$adresa1 > /tmp/test/x1
cd /tmp/test
awk '/og:video/ {print}' x1 > x2
grep -o -i 'http[^"<]*' x2 >> seznam
awk '/"title":/ {print}' x1 >> seznam
#################################################
adresa1=`sed -n '11,11p' www`
adresa1=$adresa1
curl -Lbk -m 4555 -m 6555 -k  https://music.163.com$adresa1 > /tmp/test/x1
cd /tmp/test
awk '/og:video/ {print}' x1 > x2
grep -o -i 'http[^"<]*' x2 >> seznam
awk '/"title":/ {print}' x1 >> seznam
#################################################
adresa1=`sed -n '12,12p' www`
adresa1=$adresa1
curl -Lbk -m 4555 -m 6555 -k  https://music.163.com$adresa1 > /tmp/test/x1
cd /tmp/test
awk '/og:video/ {print}' x1 > x2
grep -o -i 'http[^"<]*' x2 >> seznam
awk '/"title":/ {print}' x1 >> seznam
#################################################
#################################################
sed -i 's/http/#SERVICE 4097:0:1128:0:0:0:0:0:0:0:http/g' seznam
sed -i 's/"title":/#DESCRIPTION /g' seznam
sed -i 's/",//g' seznam
sed -i 's/"//g' seznam
#################################################
echo "#NAME MUSIC.m3u" > /etc/enigma2/userbouquet.MUSIC.m3u.tv
cat /tmp/test/seznam >> /etc/enigma2/userbouquet.MUSIC.m3u.tv
cd /
rm -rf /tmp/test
wget -q -O - http://root%s@127.0.0.1/web/servicelistreload?mode=0 >>/dev/null 2>&1 </dev/null &
sleep 2
echo "OK"
sleep 1
echo ""
exit












