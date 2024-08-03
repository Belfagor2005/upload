#!/bin/sh
sleep 1
echo "Stahuji Nova TV ... Televizní noviny"
sleep 1
sed -i '/userbouquet.NOVAzpravy.m3u.tv/d' /etc/enigma2/bouquets.tv 
more /usr/lib/enigma2/python/Plugins/Extensions/OpenPanel/DATA/x  >> /etc/enigma2/bouquets.tv 
sed -i "s/%/userbouquet.NOVAzpravy.m3u.tv/" /etc/enigma2/bouquets.tv 

[ -d /tmp/test ] || mkdir -p /tmp/test
curl  -k -Lbk -m 55532 -m 555104 "https://novaplus.nova.cz/zpravy" > /tmp/test/a
grep -o -i 'https://novaplus.nova.cz/porad/televizni-noviny/epizoda/[^<]*' /tmp/test/a > /tmp/test/x
cut -d '"' -f 1  /tmp/test/x > /tmp/test/www
cd /tmp/test
adresa1=`sed -n '1,1p' www`
adresa1=$adresa1
curl  -k -Lbk -m 55532 -m 555104 $adresa1 > /tmp/test/b
grep -E "autoplay" /tmp/test/b > /tmp/test/b1
grep -o -i 'https://media[^<]*' /tmp/test/b1 > /tmp/test/b2
cut -d '"' -f 1  /tmp/test/b2 > /tmp/test/xxx
adresa1=`sed -n '1,1p' xxx`
adresa1=$adresa1
curl  -k -Lbk -m 55532 -m 555104 $adresa1 > /tmp/test/b
grep -E "m3u8" /tmp/test/b > /tmp/test/b1
grep -o -i 'http[^<]*' /tmp/test/b1 > /tmp/test/b2
cut -d '"' -f 1  /tmp/test/b2 > /tmp/test/b3
tr -d '[\]' < "/tmp/test/b3" > /tmp/test/film.m3u
cat /tmp/test/film.m3u > /tmp/test/zaloha

adresa1=`sed -n '1,1p' /tmp/test/film.m3u`
adresa1=$adresa1
curl  -k -Lbk -m 55532 -m 555104 $adresa1 > /tmp/test/ttt
sed -i '/EXT/d' /tmp/test/ttt


slovo=`sed -n '5,5p' /tmp/test/ttt`
slovo=$slovo
sed -i "s/playlist.m3u8/$slovo/g" /tmp/test/film.m3u
echo -n "#DESCRIPTION 1024x576 Televizní noviny " >>  /tmp/test/film.m3u
cut -d '-' -f 3-  /tmp/test/x|cut -d '"' -f 1|sed -n '1,1p' >>  /tmp/test/film.m3u
cat /tmp/test/zaloha >> /tmp/test/film.m3u
slovo=`sed -n '6,6p' /tmp/test/ttt`
slovo=$slovo
sed -i "s/playlist.m3u8/$slovo/g" /tmp/test/film.m3u
echo -n "#DESCRIPTION 1280x720 Televizní noviny " >>  /tmp/test/film.m3u
cut -d '-' -f 3-  /tmp/test/x|cut -d '"' -f 1|sed -n '1,1p' >>  /tmp/test/film.m3u
cat /tmp/test/zaloha >> /tmp/test/film.m3u
slovo=`sed -n '7,7p' /tmp/test/ttt`
slovo=$slovo
sed -i "s/playlist.m3u8/$slovo/g" /tmp/test/film.m3u
echo -n "#DESCRIPTION 1920x1080 Televizní noviny " >>  /tmp/test/film.m3u
cut -d '-' -f 3-  /tmp/test/x|cut -d '"' -f 1|sed -n '1,1p' >>  /tmp/test/film.m3u
echo "#SERVICE 4097:0:1:1:0:0:0:0:0:0:https%3a" >>  /tmp/test/film.m3u
echo "#DESCRIPTION ---------------------------------------------" >>  /tmp/test/film.m3u





#################################################
adresa1=`sed -n '2,2p' www`
adresa1=$adresa1
curl  -k -Lbk -m 55532 -m 555104 $adresa1 > /tmp/test/b
grep -E "autoplay" /tmp/test/b > /tmp/test/b1
grep -o -i 'https://media[^<]*' /tmp/test/b1 > /tmp/test/b2
cut -d '"' -f 1  /tmp/test/b2 > /tmp/test/xxx
adresa1=`sed -n '1,1p' xxx`
adresa1=$adresa1
curl  -k -Lbk -m 55532 -m 555104 $adresa1 > /tmp/test/b
grep -E "m3u8" /tmp/test/b > /tmp/test/b1
grep -o -i 'http[^<]*' /tmp/test/b1 > /tmp/test/b2
cut -d '"' -f 1  /tmp/test/b2 > /tmp/test/b3
tr -d '[\]' < "/tmp/test/b3" >> /tmp/test/film.m3u
tr -d '[\]' < "/tmp/test/b3" > /tmp/test/zaloha

adresa1=`sed -n '1,1p' /tmp/test/zaloha`
adresa1=$adresa1
curl  -k -Lbk -m 55532 -m 555104 $adresa1 > /tmp/test/ttt
sed -i '/EXT/d' /tmp/test/ttt


slovo=`sed -n '5,5p' /tmp/test/ttt`
slovo=$slovo
sed -i "s/playlist.m3u8/$slovo/g" /tmp/test/film.m3u
echo -n "#DESCRIPTION 1024x576 Televizní noviny " >>  /tmp/test/film.m3u
cut -d '-' -f 3-  /tmp/test/x|cut -d '"' -f 1|sed -n '2,2p' >>  /tmp/test/film.m3u
cat /tmp/test/zaloha >> /tmp/test/film.m3u
slovo=`sed -n '6,6p' /tmp/test/ttt`
slovo=$slovo
sed -i "s/playlist.m3u8/$slovo/g" /tmp/test/film.m3u
echo -n "#DESCRIPTION 1280x720 Televizní noviny " >>  /tmp/test/film.m3u
cut -d '-' -f 3-  /tmp/test/x|cut -d '"' -f 1|sed -n '2,2p' >>  /tmp/test/film.m3u
cat /tmp/test/zaloha >> /tmp/test/film.m3u
slovo=`sed -n '7,7p' /tmp/test/ttt`
slovo=$slovo
sed -i "s/playlist.m3u8/$slovo/g" /tmp/test/film.m3u
echo -n "#DESCRIPTION 1920x1080 Televizní noviny " >>  /tmp/test/film.m3u
cut -d '-' -f 3-  /tmp/test/x|cut -d '"' -f 1|sed -n '2,2p' >>  /tmp/test/film.m3u
echo "#SERVICE 4097:0:1:1:0:0:0:0:0:0:https%3a" >>  /tmp/test/film.m3u
echo "#DESCRIPTION ---------------------------------------------" >>  /tmp/test/film.m3u

#################################################
adresa1=`sed -n '3,3p' www`
adresa1=$adresa1
curl  -k -Lbk -m 55532 -m 555104 $adresa1 > /tmp/test/b
grep -E "autoplay" /tmp/test/b > /tmp/test/b1
grep -o -i 'https://media[^<]*' /tmp/test/b1 > /tmp/test/b2
cut -d '"' -f 1  /tmp/test/b2 > /tmp/test/xxx
adresa1=`sed -n '1,1p' xxx`
adresa1=$adresa1
curl  -k -Lbk -m 55532 -m 555104 $adresa1 > /tmp/test/b
grep -E "m3u8" /tmp/test/b > /tmp/test/b1
grep -o -i 'http[^<]*' /tmp/test/b1 > /tmp/test/b2
cut -d '"' -f 1  /tmp/test/b2 > /tmp/test/b3
tr -d '[\]' < "/tmp/test/b3" >> /tmp/test/film.m3u
tr -d '[\]' < "/tmp/test/b3" > /tmp/test/zaloha

adresa1=`sed -n '1,1p' /tmp/test/zaloha`
adresa1=$adresa1
curl  -k -Lbk -m 55532 -m 555104 $adresa1 > /tmp/test/ttt
sed -i '/EXT/d' /tmp/test/ttt


slovo=`sed -n '5,5p' /tmp/test/ttt`
slovo=$slovo
sed -i "s/playlist.m3u8/$slovo/g" /tmp/test/film.m3u
echo -n "#DESCRIPTION 1024x576 Televizní noviny " >>  /tmp/test/film.m3u
cut -d '-' -f 3-  /tmp/test/x|cut -d '"' -f 1|sed -n '3,3p' >>  /tmp/test/film.m3u
cat /tmp/test/zaloha >> /tmp/test/film.m3u
slovo=`sed -n '6,6p' /tmp/test/ttt`
slovo=$slovo
sed -i "s/playlist.m3u8/$slovo/g" /tmp/test/film.m3u
echo -n "#DESCRIPTION 1280x720 Televizní noviny " >>  /tmp/test/film.m3u
cut -d '-' -f 3-  /tmp/test/x|cut -d '"' -f 1|sed -n '3,3p' >>  /tmp/test/film.m3u
cat /tmp/test/zaloha >> /tmp/test/film.m3u
slovo=`sed -n '7,7p' /tmp/test/ttt`
slovo=$slovo
sed -i "s/playlist.m3u8/$slovo/g" /tmp/test/film.m3u
echo -n "#DESCRIPTION 1920x1080 Televizní noviny " >>  /tmp/test/film.m3u
cut -d '-' -f 3-  /tmp/test/x|cut -d '"' -f 1|sed -n '3,3p' >>  /tmp/test/film.m3u
echo "#SERVICE 4097:0:1:1:0:0:0:0:0:0:https%3a" >>  /tmp/test/film.m3u
echo "#DESCRIPTION ---------------------------------------------" >>  /tmp/test/film.m3u
#################################################



adresa1=`sed -n '4,4p' www`
adresa1=$adresa1
curl  -k -Lbk -m 55532 -m 555104 $adresa1 > /tmp/test/b
grep -E "autoplay" /tmp/test/b > /tmp/test/b1
grep -o -i 'https://media[^<]*' /tmp/test/b1 > /tmp/test/b2
cut -d '"' -f 1  /tmp/test/b2 > /tmp/test/xxx
adresa1=`sed -n '1,1p' xxx`
adresa1=$adresa1
curl  -k -Lbk -m 55532 -m 555104 $adresa1 > /tmp/test/b
grep -E "m3u8" /tmp/test/b > /tmp/test/b1
grep -o -i 'http[^<]*' /tmp/test/b1 > /tmp/test/b2
cut -d '"' -f 1  /tmp/test/b2 > /tmp/test/b3
tr -d '[\]' < "/tmp/test/b3" >> /tmp/test/film.m3u
tr -d '[\]' < "/tmp/test/b3" > /tmp/test/zaloha

adresa1=`sed -n '1,1p' /tmp/test/zaloha`
adresa1=$adresa1
curl  -k -Lbk -m 55532 -m 555104 $adresa1 > /tmp/test/ttt
sed -i '/EXT/d' /tmp/test/ttt


slovo=`sed -n '5,5p' /tmp/test/ttt`
slovo=$slovo
sed -i "s/playlist.m3u8/$slovo/g" /tmp/test/film.m3u
echo -n "#DESCRIPTION 1024x576 Televizní noviny " >>  /tmp/test/film.m3u
cut -d '-' -f 3-  /tmp/test/x|cut -d '"' -f 1|sed -n '4,4p' >>  /tmp/test/film.m3u
cat /tmp/test/zaloha >> /tmp/test/film.m3u
slovo=`sed -n '6,6p' /tmp/test/ttt`
slovo=$slovo
sed -i "s/playlist.m3u8/$slovo/g" /tmp/test/film.m3u
echo -n "#DESCRIPTION 1280x720 Televizní noviny " >>  /tmp/test/film.m3u
cut -d '-' -f 3-  /tmp/test/x|cut -d '"' -f 1|sed -n '4,4p' >>  /tmp/test/film.m3u
cat /tmp/test/zaloha >> /tmp/test/film.m3u
slovo=`sed -n '7,7p' /tmp/test/ttt`
slovo=$slovo
sed -i "s/playlist.m3u8/$slovo/g" /tmp/test/film.m3u
echo -n "#DESCRIPTION 1920x1080 Televizní noviny " >>  /tmp/test/film.m3u
cut -d '-' -f 3-  /tmp/test/x|cut -d '"' -f 1|sed -n '4,4p' >>  /tmp/test/film.m3u
echo "#SERVICE 4097:0:1:1:0:0:0:0:0:0:https%3a" >>  /tmp/test/film.m3u
echo "#DESCRIPTION ---------------------------------------------" >>  /tmp/test/film.m3u
#################################################
adresa1=`sed -n '5,5p' www`
adresa1=$adresa1
curl  -k -Lbk -m 55532 -m 555104 $adresa1 > /tmp/test/b
grep -E "autoplay" /tmp/test/b > /tmp/test/b1
grep -o -i 'https://media[^<]*' /tmp/test/b1 > /tmp/test/b2
cut -d '"' -f 1  /tmp/test/b2 > /tmp/test/xxx
adresa1=`sed -n '1,1p' xxx`
adresa1=$adresa1
curl  -k -Lbk -m 55532 -m 555104 $adresa1 > /tmp/test/b
grep -E "m3u8" /tmp/test/b > /tmp/test/b1
grep -o -i 'http[^<]*' /tmp/test/b1 > /tmp/test/b2
cut -d '"' -f 1  /tmp/test/b2 > /tmp/test/b3
tr -d '[\]' < "/tmp/test/b3" >> /tmp/test/film.m3u
tr -d '[\]' < "/tmp/test/b3" > /tmp/test/zaloha

adresa1=`sed -n '1,1p' /tmp/test/zaloha`
adresa1=$adresa1
curl  -k -Lbk -m 55532 -m 555104 $adresa1 > /tmp/test/ttt
sed -i '/EXT/d' /tmp/test/ttt


slovo=`sed -n '5,5p' /tmp/test/ttt`
slovo=$slovo
sed -i "s/playlist.m3u8/$slovo/g" /tmp/test/film.m3u
echo -n "#DESCRIPTION 1024x576 Televizní noviny " >>  /tmp/test/film.m3u
cut -d '-' -f 3-  /tmp/test/x|cut -d '"' -f 1|sed -n '5,5p' >>  /tmp/test/film.m3u
cat /tmp/test/zaloha >> /tmp/test/film.m3u
slovo=`sed -n '6,6p' /tmp/test/ttt`
slovo=$slovo
sed -i "s/playlist.m3u8/$slovo/g" /tmp/test/film.m3u
echo -n "#DESCRIPTION 1280x720 Televizní noviny " >>  /tmp/test/film.m3u
cut -d '-' -f 3-  /tmp/test/x|cut -d '"' -f 1|sed -n '5,5p' >>  /tmp/test/film.m3u
cat /tmp/test/zaloha >> /tmp/test/film.m3u
slovo=`sed -n '7,7p' /tmp/test/ttt`
slovo=$slovo
sed -i "s/playlist.m3u8/$slovo/g" /tmp/test/film.m3u
echo -n "#DESCRIPTION 1920x1080 Televizní noviny " >>  /tmp/test/film.m3u
cut -d '-' -f 3-  /tmp/test/x|cut -d '"' -f 1|sed -n '5,5p' >>  /tmp/test/film.m3u
echo "#SERVICE 4097:0:1:1:0:0:0:0:0:0:https%3a" >>  /tmp/test/film.m3u
echo "#DESCRIPTION ---------------------------------------------" >>  /tmp/test/film.m3u
#################################################
#################################################
grep -o -i 'https://novaplus.nova.cz/porad/poledni-televizni-noviny/epizoda/[^<]*' /tmp/test/a > /tmp/test/x
cut -d '"' -f 1  /tmp/test/x > /tmp/test/www
adresa1=`sed -n '1,1p' www`
adresa1=$adresa1
curl  -k -Lbk -m 55532 -m 555104 $adresa1 > /tmp/test/b
grep -E "autoplay" /tmp/test/b > /tmp/test/b1
grep -o -i 'https://media[^<]*' /tmp/test/b1 > /tmp/test/b2
cut -d '"' -f 1  /tmp/test/b2 > /tmp/test/xxx
adresa1=`sed -n '1,1p' xxx`
adresa1=$adresa1
curl  -k -Lbk -m 55532 -m 555104 $adresa1 > /tmp/test/b
grep -E "m3u8" /tmp/test/b > /tmp/test/b1
grep -o -i 'http[^<]*' /tmp/test/b1 > /tmp/test/b2
cut -d '"' -f 1  /tmp/test/b2 > /tmp/test/b3
tr -d '[\]' < "/tmp/test/b3" >> /tmp/test/film.m3u
tr -d '[\]' < "/tmp/test/b3" > /tmp/test/zaloha

adresa1=`sed -n '1,1p' /tmp/test/zaloha`
adresa1=$adresa1
curl  -k -Lbk -m 55532 -m 555104 $adresa1 > /tmp/test/ttt
sed -i '/EXT/d' /tmp/test/ttt


slovo=`sed -n '5,5p' /tmp/test/ttt`
slovo=$slovo
sed -i "s/playlist.m3u8/$slovo/g" /tmp/test/film.m3u
echo -n "#DESCRIPTION 1024x576 Polední televizní noviny " >>  /tmp/test/film.m3u
cut -d '-' -f 4-  /tmp/test/x|cut -d '"' -f 1|sed -n '1,1p' >>  /tmp/test/film.m3u
cat /tmp/test/zaloha >> /tmp/test/film.m3u
slovo=`sed -n '6,6p' /tmp/test/ttt`
slovo=$slovo
sed -i "s/playlist.m3u8/$slovo/g" /tmp/test/film.m3u
echo -n "#DESCRIPTION 1280x720 Polední televizní noviny " >>  /tmp/test/film.m3u
cut -d '-' -f 4-  /tmp/test/x|cut -d '"' -f 1|sed -n '1,1p' >>  /tmp/test/film.m3u
cat /tmp/test/zaloha >> /tmp/test/film.m3u
slovo=`sed -n '7,7p' /tmp/test/ttt`
slovo=$slovo
sed -i "s/playlist.m3u8/$slovo/g" /tmp/test/film.m3u
echo -n "#DESCRIPTION 1920x1080 Polední televizní noviny " >>  /tmp/test/film.m3u
cut -d '-' -f 4-  /tmp/test/x|cut -d '"' -f 1|sed -n '1,1p' >>  /tmp/test/film.m3u
echo "#SERVICE 4097:0:1:1:0:0:0:0:0:0:https%3a" >>  /tmp/test/film.m3u
echo "#DESCRIPTION ---------------------------------------------" >>  /tmp/test/film.m3u



#################################################
#################################################
adresa1=`sed -n '2,2p' www`
adresa1=$adresa1
curl  -k -Lbk -m 55532 -m 555104 $adresa1 > /tmp/test/b
grep -E "autoplay" /tmp/test/b > /tmp/test/b1
grep -o -i 'https://media[^<]*' /tmp/test/b1 > /tmp/test/b2
cut -d '"' -f 1  /tmp/test/b2 > /tmp/test/xxx
adresa1=`sed -n '1,1p' xxx`
adresa1=$adresa1
curl  -k -Lbk -m 55532 -m 555104 $adresa1 > /tmp/test/b
grep -E "m3u8" /tmp/test/b > /tmp/test/b1
grep -o -i 'http[^<]*' /tmp/test/b1 > /tmp/test/b2
cut -d '"' -f 1  /tmp/test/b2 > /tmp/test/b3
tr -d '[\]' < "/tmp/test/b3" >> /tmp/test/film.m3u
tr -d '[\]' < "/tmp/test/b3" > /tmp/test/zaloha

adresa1=`sed -n '1,1p' /tmp/test/zaloha`
adresa1=$adresa1
curl  -k -Lbk -m 55532 -m 555104 $adresa1 > /tmp/test/ttt
sed -i '/EXT/d' /tmp/test/ttt


slovo=`sed -n '5,5p' /tmp/test/ttt`
slovo=$slovo
sed -i "s/playlist.m3u8/$slovo/g" /tmp/test/film.m3u
echo -n "#DESCRIPTION 1024x576 Polední televizní noviny " >>  /tmp/test/film.m3u
cut -d '-' -f 4-  /tmp/test/x|cut -d '"' -f 1|sed -n '2,2p' >>  /tmp/test/film.m3u
cat /tmp/test/zaloha >> /tmp/test/film.m3u
slovo=`sed -n '6,6p' /tmp/test/ttt`
slovo=$slovo
sed -i "s/playlist.m3u8/$slovo/g" /tmp/test/film.m3u
echo -n "#DESCRIPTION 1280x720 Polední televizní noviny " >>  /tmp/test/film.m3u
cut -d '-' -f 4-  /tmp/test/x|cut -d '"' -f 1|sed -n '2,2p' >>  /tmp/test/film.m3u
cat /tmp/test/zaloha >> /tmp/test/film.m3u
slovo=`sed -n '7,7p' /tmp/test/ttt`
slovo=$slovo
sed -i "s/playlist.m3u8/$slovo/g" /tmp/test/film.m3u
echo -n "#DESCRIPTION 1920x1080 Polední televizní noviny " >>  /tmp/test/film.m3u
cut -d '-' -f 4-  /tmp/test/x|cut -d '"' -f 1|sed -n '2,2p' >>  /tmp/test/film.m3u
echo "#SERVICE 4097:0:1:1:0:0:0:0:0:0:https%3a" >>  /tmp/test/film.m3u
echo "#DESCRIPTION ---------------------------------------------" >>  /tmp/test/film.m3u
#################################################
adresa1=`sed -n '3,3p' www`
adresa1=$adresa1
curl  -k -Lbk -m 55532 -m 555104 $adresa1 > /tmp/test/b
grep -E "autoplay" /tmp/test/b > /tmp/test/b1
grep -o -i 'https://media[^<]*' /tmp/test/b1 > /tmp/test/b2
cut -d '"' -f 1  /tmp/test/b2 > /tmp/test/xxx
adresa1=`sed -n '1,1p' xxx`
adresa1=$adresa1
curl  -k -Lbk -m 55532 -m 555104 $adresa1 > /tmp/test/b
grep -E "m3u8" /tmp/test/b > /tmp/test/b1
grep -o -i 'http[^<]*' /tmp/test/b1 > /tmp/test/b2
cut -d '"' -f 1  /tmp/test/b2 > /tmp/test/b3
tr -d '[\]' < "/tmp/test/b3" >> /tmp/test/film.m3u
tr -d '[\]' < "/tmp/test/b3" > /tmp/test/zaloha

adresa1=`sed -n '1,1p' /tmp/test/zaloha`
adresa1=$adresa1
curl  -k -Lbk -m 55532 -m 555104 $adresa1 > /tmp/test/ttt
sed -i '/EXT/d' /tmp/test/ttt


slovo=`sed -n '5,5p' /tmp/test/ttt`
slovo=$slovo
sed -i "s/playlist.m3u8/$slovo/g" /tmp/test/film.m3u
echo -n "#DESCRIPTION 1024x576 Polední televizní noviny " >>  /tmp/test/film.m3u
cut -d '-' -f 4-  /tmp/test/x|cut -d '"' -f 1|sed -n '3,3p' >>  /tmp/test/film.m3u
cat /tmp/test/zaloha >> /tmp/test/film.m3u
slovo=`sed -n '6,6p' /tmp/test/ttt`
slovo=$slovo
sed -i "s/playlist.m3u8/$slovo/g" /tmp/test/film.m3u
echo -n "#DESCRIPTION 1280x720 Polední televizní noviny " >>  /tmp/test/film.m3u
cut -d '-' -f 4-  /tmp/test/x|cut -d '"' -f 1|sed -n '3,3p' >>  /tmp/test/film.m3u
cat /tmp/test/zaloha >> /tmp/test/film.m3u
slovo=`sed -n '7,7p' /tmp/test/ttt`
slovo=$slovo
sed -i "s/playlist.m3u8/$slovo/g" /tmp/test/film.m3u
echo -n "#DESCRIPTION 1920x1080 Polední televizní noviny " >>  /tmp/test/film.m3u
cut -d '-' -f 4-  /tmp/test/x|cut -d '"' -f 1|sed -n '3,3p' >>  /tmp/test/film.m3u
echo "#SERVICE 4097:0:1:1:0:0:0:0:0:0:https%3a" >>  /tmp/test/film.m3u
echo "#DESCRIPTION ---------------------------------------------" >>  /tmp/test/film.m3u
#################################################
adresa1=`sed -n '4,4p' www`
adresa1=$adresa1
curl  -k -Lbk -m 55532 -m 555104 $adresa1 > /tmp/test/b
grep -E "autoplay" /tmp/test/b > /tmp/test/b1
grep -o -i 'https://media[^<]*' /tmp/test/b1 > /tmp/test/b2
cut -d '"' -f 1  /tmp/test/b2 > /tmp/test/xxx
adresa1=`sed -n '1,1p' xxx`
adresa1=$adresa1
curl  -k -Lbk -m 55532 -m 555104 $adresa1 > /tmp/test/b
grep -E "m3u8" /tmp/test/b > /tmp/test/b1
grep -o -i 'http[^<]*' /tmp/test/b1 > /tmp/test/b2
cut -d '"' -f 1  /tmp/test/b2 > /tmp/test/b3
tr -d '[\]' < "/tmp/test/b3" >> /tmp/test/film.m3u
tr -d '[\]' < "/tmp/test/b3" > /tmp/test/zaloha

adresa1=`sed -n '1,1p' /tmp/test/zaloha`
adresa1=$adresa1
curl  -k -Lbk -m 55532 -m 555104 $adresa1 > /tmp/test/ttt
sed -i '/EXT/d' /tmp/test/ttt


slovo=`sed -n '5,5p' /tmp/test/ttt`
slovo=$slovo
sed -i "s/playlist.m3u8/$slovo/g" /tmp/test/film.m3u
echo -n "#DESCRIPTION 1024x576 Polední televizní noviny " >>  /tmp/test/film.m3u
cut -d '-' -f 4-  /tmp/test/x|cut -d '"' -f 1|sed -n '4,4p' >>  /tmp/test/film.m3u
cat /tmp/test/zaloha >> /tmp/test/film.m3u
slovo=`sed -n '6,6p' /tmp/test/ttt`
slovo=$slovo
sed -i "s/playlist.m3u8/$slovo/g" /tmp/test/film.m3u
echo -n "#DESCRIPTION 1280x720 Polední televizní noviny " >>  /tmp/test/film.m3u
cut -d '-' -f 4-  /tmp/test/x|cut -d '"' -f 1|sed -n '4,4p' >>  /tmp/test/film.m3u
cat /tmp/test/zaloha >> /tmp/test/film.m3u
slovo=`sed -n '7,7p' /tmp/test/ttt`
slovo=$slovo
sed -i "s/playlist.m3u8/$slovo/g" /tmp/test/film.m3u
echo -n "#DESCRIPTION 1920x1080 Polední televizní noviny " >>  /tmp/test/film.m3u
cut -d '-' -f 4-  /tmp/test/x|cut -d '"' -f 1|sed -n '4,4p' >>  /tmp/test/film.m3u
echo "#SERVICE 4097:0:1:1:0:0:0:0:0:0:https%3a" >>  /tmp/test/film.m3u
echo "#DESCRIPTION ---------------------------------------------" >>  /tmp/test/film.m3u
#################################################
#################################################
#################################################
grep -o -i 'https://novaplus.nova.cz/porad/odpoledni-televizni-noviny/epizoda/[^<]*' /tmp/test/a > /tmp/test/x
cut -d '"' -f 1  /tmp/test/x > /tmp/test/www
adresa1=`sed -n '1,1p' www`
adresa1=$adresa1
curl  -k -Lbk -m 55532 -m 555104 $adresa1 > /tmp/test/b
grep -E "autoplay" /tmp/test/b > /tmp/test/b1
grep -o -i 'https://media[^<]*' /tmp/test/b1 > /tmp/test/b2
cut -d '"' -f 1  /tmp/test/b2 > /tmp/test/xxx
adresa1=`sed -n '1,1p' xxx`
adresa1=$adresa1
curl  -k -Lbk -m 55532 -m 555104 $adresa1 > /tmp/test/b
grep -E "m3u8" /tmp/test/b > /tmp/test/b1
grep -o -i 'http[^<]*' /tmp/test/b1 > /tmp/test/b2
cut -d '"' -f 1  /tmp/test/b2 > /tmp/test/b3
tr -d '[\]' < "/tmp/test/b3" >> /tmp/test/film.m3u
tr -d '[\]' < "/tmp/test/b3" > /tmp/test/zaloha

adresa1=`sed -n '1,1p' /tmp/test/zaloha`
adresa1=$adresa1
curl  -k -Lbk -m 55532 -m 555104 $adresa1 > /tmp/test/ttt
sed -i '/EXT/d' /tmp/test/ttt


slovo=`sed -n '5,5p' /tmp/test/ttt`
slovo=$slovo
sed -i "s/playlist.m3u8/$slovo/g" /tmp/test/film.m3u
echo -n "#DESCRIPTION 1024x576 Odpolední televizní noviny " >>  /tmp/test/film.m3u
cut -d '-' -f 4-  /tmp/test/x|cut -d '"' -f 1|sed -n '1,1p' >>  /tmp/test/film.m3u
cat /tmp/test/zaloha >> /tmp/test/film.m3u
slovo=`sed -n '6,6p' /tmp/test/ttt`
slovo=$slovo
sed -i "s/playlist.m3u8/$slovo/g" /tmp/test/film.m3u
echo -n "#DESCRIPTION 1280x720 Odpolední televizní noviny " >>  /tmp/test/film.m3u
cut -d '-' -f 4-  /tmp/test/x|cut -d '"' -f 1|sed -n '1,1p' >>  /tmp/test/film.m3u
cat /tmp/test/zaloha >> /tmp/test/film.m3u
slovo=`sed -n '7,7p' /tmp/test/ttt`
slovo=$slovo
sed -i "s/playlist.m3u8/$slovo/g" /tmp/test/film.m3u
echo -n "#DESCRIPTION 1920x1080 Odpolední televizní noviny " >>  /tmp/test/film.m3u
cut -d '-' -f 4-  /tmp/test/x|cut -d '"' -f 1|sed -n '1,1p' >>  /tmp/test/film.m3u
echo "#SERVICE 4097:0:1:1:0:0:0:0:0:0:https%3a" >>  /tmp/test/film.m3u
echo "#DESCRIPTION ---------------------------------------------" >>  /tmp/test/film.m3u

#################################################
adresa1=`sed -n '2,2p' www`
adresa1=$adresa1
curl  -k -Lbk -m 55532 -m 555104 $adresa1 > /tmp/test/b
grep -E "autoplay" /tmp/test/b > /tmp/test/b1
grep -o -i 'https://media[^<]*' /tmp/test/b1 > /tmp/test/b2
cut -d '"' -f 1  /tmp/test/b2 > /tmp/test/xxx
adresa1=`sed -n '1,1p' xxx`
adresa1=$adresa1
curl  -k -Lbk -m 55532 -m 555104 $adresa1 > /tmp/test/b
grep -E "m3u8" /tmp/test/b > /tmp/test/b1
grep -o -i 'http[^<]*' /tmp/test/b1 > /tmp/test/b2
cut -d '"' -f 1  /tmp/test/b2 > /tmp/test/b3
tr -d '[\]' < "/tmp/test/b3" >> /tmp/test/film.m3u
tr -d '[\]' < "/tmp/test/b3" > /tmp/test/zaloha

adresa1=`sed -n '1,1p' /tmp/test/zaloha`
adresa1=$adresa1
curl  -k -Lbk -m 55532 -m 555104 $adresa1 > /tmp/test/ttt
sed -i '/EXT/d' /tmp/test/ttt


slovo=`sed -n '5,5p' /tmp/test/ttt`
slovo=$slovo
sed -i "s/playlist.m3u8/$slovo/g" /tmp/test/film.m3u
echo -n "#DESCRIPTION 1024x576 Odpolední televizní noviny " >>  /tmp/test/film.m3u
cut -d '-' -f 4-  /tmp/test/x|cut -d '"' -f 1|sed -n '2,2p' >>  /tmp/test/film.m3u
cat /tmp/test/zaloha >> /tmp/test/film.m3u
slovo=`sed -n '6,6p' /tmp/test/ttt`
slovo=$slovo
sed -i "s/playlist.m3u8/$slovo/g" /tmp/test/film.m3u
echo -n "#DESCRIPTION 1280x720 Odpolední televizní noviny " >>  /tmp/test/film.m3u
cut -d '-' -f 4-  /tmp/test/x|cut -d '"' -f 1|sed -n '2,2p' >>  /tmp/test/film.m3u
cat /tmp/test/zaloha >> /tmp/test/film.m3u
slovo=`sed -n '7,7p' /tmp/test/ttt`
slovo=$slovo
sed -i "s/playlist.m3u8/$slovo/g" /tmp/test/film.m3u
echo -n "#DESCRIPTION 1920x1080 Odpolední televizní noviny " >>  /tmp/test/film.m3u
cut -d '-' -f 4-  /tmp/test/x|cut -d '"' -f 1|sed -n '2,2p' >>  /tmp/test/film.m3u
echo "#SERVICE 4097:0:1:1:0:0:0:0:0:0:https%3a" >>  /tmp/test/film.m3u
echo "#DESCRIPTION ---------------------------------------------" >>  /tmp/test/film.m3u
#################################################
adresa1=`sed -n '3,3p' www`
adresa1=$adresa1
curl  -k -Lbk -m 55532 -m 555104 $adresa1 > /tmp/test/b
grep -E "autoplay" /tmp/test/b > /tmp/test/b1
grep -o -i 'https://media[^<]*' /tmp/test/b1 > /tmp/test/b2
cut -d '"' -f 1  /tmp/test/b2 > /tmp/test/xxx
adresa1=`sed -n '1,1p' xxx`
adresa1=$adresa1
curl  -k -Lbk -m 55532 -m 555104 $adresa1 > /tmp/test/b
grep -E "m3u8" /tmp/test/b > /tmp/test/b1
grep -o -i 'http[^<]*' /tmp/test/b1 > /tmp/test/b2
cut -d '"' -f 1  /tmp/test/b2 > /tmp/test/b3
tr -d '[\]' < "/tmp/test/b3" >> /tmp/test/film.m3u
tr -d '[\]' < "/tmp/test/b3" > /tmp/test/zaloha

adresa1=`sed -n '1,1p' /tmp/test/zaloha`
adresa1=$adresa1
curl  -k -Lbk -m 55532 -m 555104 $adresa1 > /tmp/test/ttt
sed -i '/EXT/d' /tmp/test/ttt


slovo=`sed -n '5,5p' /tmp/test/ttt`
slovo=$slovo
sed -i "s/playlist.m3u8/$slovo/g" /tmp/test/film.m3u
echo -n "#DESCRIPTION 1024x576 Odpolední televizní noviny " >>  /tmp/test/film.m3u
cut -d '-' -f 4-  /tmp/test/x|cut -d '"' -f 1|sed -n '3,3p' >>  /tmp/test/film.m3u
cat /tmp/test/zaloha >> /tmp/test/film.m3u
slovo=`sed -n '6,6p' /tmp/test/ttt`
slovo=$slovo
sed -i "s/playlist.m3u8/$slovo/g" /tmp/test/film.m3u
echo -n "#DESCRIPTION 1280x720 Odpolední televizní noviny " >>  /tmp/test/film.m3u
cut -d '-' -f 4-  /tmp/test/x|cut -d '"' -f 1|sed -n '3,3p' >>  /tmp/test/film.m3u
cat /tmp/test/zaloha >> /tmp/test/film.m3u
slovo=`sed -n '7,7p' /tmp/test/ttt`
slovo=$slovo
sed -i "s/playlist.m3u8/$slovo/g" /tmp/test/film.m3u
echo -n "#DESCRIPTION 1920x1080 Odpolední televizní noviny " >>  /tmp/test/film.m3u
cut -d '-' -f 4-  /tmp/test/x|cut -d '"' -f 1|sed -n '3,3p' >>  /tmp/test/film.m3u
echo "#SERVICE 4097:0:1:1:0:0:0:0:0:0:https%3a" >>  /tmp/test/film.m3u
echo "#DESCRIPTION ---------------------------------------------" >>  /tmp/test/film.m3u
#################################################
adresa1=`sed -n '4,4p' www`
adresa1=$adresa1
curl  -k -Lbk -m 55532 -m 555104 $adresa1 > /tmp/test/b
grep -E "autoplay" /tmp/test/b > /tmp/test/b1
grep -o -i 'https://media[^<]*' /tmp/test/b1 > /tmp/test/b2
cut -d '"' -f 1  /tmp/test/b2 > /tmp/test/xxx
adresa1=`sed -n '1,1p' xxx`
adresa1=$adresa1
curl  -k -Lbk -m 55532 -m 555104 $adresa1 > /tmp/test/b
grep -E "m3u8" /tmp/test/b > /tmp/test/b1
grep -o -i 'http[^<]*' /tmp/test/b1 > /tmp/test/b2
cut -d '"' -f 1  /tmp/test/b2 > /tmp/test/b3
tr -d '[\]' < "/tmp/test/b3" >> /tmp/test/film.m3u
tr -d '[\]' < "/tmp/test/b3" > /tmp/test/zaloha

adresa1=`sed -n '1,1p' /tmp/test/zaloha`
adresa1=$adresa1
curl  -k -Lbk -m 55532 -m 555104 $adresa1 > /tmp/test/ttt
sed -i '/EXT/d' /tmp/test/ttt


slovo=`sed -n '5,5p' /tmp/test/ttt`
slovo=$slovo
sed -i "s/playlist.m3u8/$slovo/g" /tmp/test/film.m3u
echo -n "#DESCRIPTION 1024x576 Odpolední televizní noviny " >>  /tmp/test/film.m3u
cut -d '-' -f 4-  /tmp/test/x|cut -d '"' -f 1|sed -n '4,4p' >>  /tmp/test/film.m3u
cat /tmp/test/zaloha >> /tmp/test/film.m3u
slovo=`sed -n '6,6p' /tmp/test/ttt`
slovo=$slovo
sed -i "s/playlist.m3u8/$slovo/g" /tmp/test/film.m3u
echo -n "#DESCRIPTION 1280x720 Odpolední televizní noviny " >>  /tmp/test/film.m3u
cut -d '-' -f 4-  /tmp/test/x|cut -d '"' -f 1|sed -n '4,4p' >>  /tmp/test/film.m3u
cat /tmp/test/zaloha >> /tmp/test/film.m3u
slovo=`sed -n '7,7p' /tmp/test/ttt`
slovo=$slovo
sed -i "s/playlist.m3u8/$slovo/g" /tmp/test/film.m3u
echo -n "#DESCRIPTION 1920x1080 Odpolední televizní noviny " >>  /tmp/test/film.m3u
cut -d '-' -f 4-  /tmp/test/x|cut -d '"' -f 1|sed -n '4,4p' >>  /tmp/test/film.m3u

##################################################################################################
sed -i 's/https:/#SERVICE 4097:0:1:1:0:0:0:0:0:0:https%3a/g' /tmp/test/film.m3u
echo "#NAME NOVAzpravy.m3u" > /etc/enigma2/userbouquet.NOVAzpravy.m3u.tv
cat /tmp/test/film.m3u >> /etc/enigma2/userbouquet.NOVAzpravy.m3u.tv
cd /
rm -rf /tmp/test
wget -q -O - http://root%s@127.0.0.1/web/servicelistreload?mode=0 >>/dev/null 2>&1 </dev/null &
sleep 2
echo "OK"
exit









