#!/bin/sh
echo "stahuji BLACKED"
[ -d /tmp/test ] || mkdir -p /tmp/test
more /usr/lib/enigma2/python/Plugins/Extensions/OpenPanel/DATA/x  >> /etc/enigma2/bouquets.tv 
sed -i "s/%/userbouquet.BLACKEDxxx.m3u.tv/" /etc/enigma2/bouquets.tv 
curl -Lbk -m 4555 -m 6555 -k  https://www.redtube.com/channels/blacked > /tmp/test/x1
cd /tmp/test
grep -o -i 'img_rel_videos[^<]*' x1 > x2
sed 's/img_rel_videos//g' x2 > x3
sed 's/"//g' x3 > www
adresa1=`sed -n '1,1p' www`
adresa1=$adresa1
curl -Lbk -m 4555 -m 6555 -k  https://www.redtube.com/$adresa1 > /tmp/test/x1
cd /tmp/test
awk '/1080/ {print}' x1 > x2
sed 's/\(["]\+\)/\n\1/g' x2 > x3
awk '/1080P_4000K/ {print}' x3 > x4
tr -d '[\]' < "x4" > x5
sed -n '1,1p' x5 > seznam
awk '/<h1 class="video_title">/ {print}' x1 >> seznam
#################################################
adresa1=`sed -n '2,2p' www`
adresa1=$adresa1
curl -Lbk -m 4555 -m 6555 -k  https://www.redtube.com/$adresa1 > /tmp/test/x1
cd /tmp/test
awk '/1080/ {print}' x1 > x2
sed 's/\(["]\+\)/\n\1/g' x2 > x3
awk '/1080P_4000K/ {print}' x3 > x4
tr -d '[\]' < "x4" > x5
sed -n '1,1p' x5 >> seznam
awk '/<h1 class="video_title">/ {print}' x1 >> seznam
#################################################
adresa1=`sed -n '3,3p' www`
adresa1=$adresa1
curl -Lbk -m 4555 -m 6555 -k  https://www.redtube.com/$adresa1 > /tmp/test/x1
cd /tmp/test
awk '/1080/ {print}' x1 > x2
sed 's/\(["]\+\)/\n\1/g' x2 > x3
awk '/1080P_4000K/ {print}' x3 > x4
tr -d '[\]' < "x4" > x5
sed -n '1,1p' x5 >> seznam
awk '/<h1 class="video_title">/ {print}' x1 >> seznam
#################################################
adresa1=`sed -n '4,4p' www`
adresa1=$adresa1
curl -Lbk -m 4555 -m 6555 -k  https://www.redtube.com/$adresa1 > /tmp/test/x1
cd /tmp/test
awk '/1080/ {print}' x1 > x2
sed 's/\(["]\+\)/\n\1/g' x2 > x3
awk '/1080P_4000K/ {print}' x3 > x4
tr -d '[\]' < "x4" > x5
sed -n '1,1p' x5 >> seznam
awk '/<h1 class="video_title">/ {print}' x1 >> seznam
#################################################
adresa1=`sed -n '5,5p' www`
adresa1=$adresa1
curl -Lbk -m 4555 -m 6555 -k  https://www.redtube.com/$adresa1 > /tmp/test/x1
cd /tmp/test
awk '/1080/ {print}' x1 > x2
sed 's/\(["]\+\)/\n\1/g' x2 > x3
awk '/1080P_4000K/ {print}' x3 > x4
tr -d '[\]' < "x4" > x5
sed -n '1,1p' x5 >> seznam
awk '/<h1 class="video_title">/ {print}' x1 >> seznam
#################################################
adresa1=`sed -n '6,6p' www`
adresa1=$adresa1
curl -Lbk -m 4555 -m 6555 -k  https://www.redtube.com/$adresa1 > /tmp/test/x1
cd /tmp/test
awk '/1080/ {print}' x1 > x2
sed 's/\(["]\+\)/\n\1/g' x2 > x3
awk '/1080P_4000K/ {print}' x3 > x4
tr -d '[\]' < "x4" > x5
sed -n '1,1p' x5 >> seznam
awk '/<h1 class="video_title">/ {print}' x1 >> seznam
#################################################
adresa1=`sed -n '7,7p' www`
adresa1=$adresa1
curl -Lbk -m 4555 -m 6555 -k  https://www.redtube.com/$adresa1 > /tmp/test/x1
cd /tmp/test
awk '/1080/ {print}' x1 > x2
sed 's/\(["]\+\)/\n\1/g' x2 > x3
awk '/1080P_4000K/ {print}' x3 > x4
tr -d '[\]' < "x4" > x5
sed -n '1,1p' x5 >> seznam
awk '/<h1 class="video_title">/ {print}' x1 >> seznam
#################################################
adresa1=`sed -n '8,8p' www`
adresa1=$adresa1
curl -Lbk -m 4555 -m 6555 -k  https://www.redtube.com/$adresa1 > /tmp/test/x1
cd /tmp/test
awk '/1080/ {print}' x1 > x2
sed 's/\(["]\+\)/\n\1/g' x2 > x3
awk '/1080P_4000K/ {print}' x3 > x4
tr -d '[\]' < "x4" > x5
sed -n '1,1p' x5 >> seznam
awk '/<h1 class="video_title">/ {print}' x1 >> seznam
#################################################
adresa1=`sed -n '9,9p' www`
adresa1=$adresa1
curl -Lbk -m 4555 -m 6555 -k  https://www.redtube.com/$adresa1 > /tmp/test/x1
cd /tmp/test
awk '/1080/ {print}' x1 > x2
sed 's/\(["]\+\)/\n\1/g' x2 > x3
awk '/1080P_4000K/ {print}' x3 > x4
tr -d '[\]' < "x4" > x5
sed -n '1,1p' x5 >> seznam
awk '/<h1 class="video_title">/ {print}' x1 >> seznam
#################################################
adresa1=`sed -n '10,10p' www`
adresa1=$adresa1
curl -Lbk -m 4555 -m 6555 -k  https://www.redtube.com/$adresa1 > /tmp/test/x1
cd /tmp/test
awk '/1080/ {print}' x1 > x2
sed 's/\(["]\+\)/\n\1/g' x2 > x3
awk '/1080P_4000K/ {print}' x3 > x4
tr -d '[\]' < "x4" > x5
sed -n '1,1p' x5 >> seznam
awk '/<h1 class="video_title">/ {print}' x1 >> seznam
#################################################
adresa1=`sed -n '11,11p' www`
adresa1=$adresa1
curl -Lbk -m 4555 -m 6555 -k  https://www.redtube.com/$adresa1 > /tmp/test/x1
cd /tmp/test
awk '/1080/ {print}' x1 > x2
sed 's/\(["]\+\)/\n\1/g' x2 > x3
awk '/1080P_4000K/ {print}' x3 > x4
tr -d '[\]' < "x4" > x5
sed -n '1,1p' x5 >> seznam
awk '/<h1 class="video_title">/ {print}' x1 >> seznam
#################################################
adresa1=`sed -n '12,12p' www`
adresa1=$adresa1
curl -Lbk -m 4555 -m 6555 -k  https://www.redtube.com/$adresa1 > /tmp/test/x1
cd /tmp/test
awk '/1080/ {print}' x1 > x2
sed 's/\(["]\+\)/\n\1/g' x2 > x3
awk '/1080P_4000K/ {print}' x3 > x4
tr -d '[\]' < "x4" > x5
sed -n '1,1p' x5 >> seznam
awk '/<h1 class="video_title">/ {print}' x1 >> seznam
#################################################
adresa1=`sed -n '13,13p' www`
adresa1=$adresa1
curl -Lbk -m 4555 -m 6555 -k  https://www.redtube.com/$adresa1 > /tmp/test/x1
cd /tmp/test
awk '/1080/ {print}' x1 > x2
sed 's/\(["]\+\)/\n\1/g' x2 > x3
awk '/1080P_4000K/ {print}' x3 > x4
tr -d '[\]' < "x4" > x5
sed -n '1,1p' x5 >> seznam
awk '/<h1 class="video_title">/ {print}' x1 >> seznam
#################################################
adresa1=`sed -n '14,14p' www`
adresa1=$adresa1
curl -Lbk -m 4555 -m 6555 -k  https://www.redtube.com/$adresa1 > /tmp/test/x1
cd /tmp/test
awk '/1080/ {print}' x1 > x2
sed 's/\(["]\+\)/\n\1/g' x2 > x3
awk '/1080P_4000K/ {print}' x3 > x4
tr -d '[\]' < "x4" > x5
sed -n '1,1p' x5 >> seznam
awk '/<h1 class="video_title">/ {print}' x1 >> seznam
#################################################
adresa1=`sed -n '15,15p' www`
adresa1=$adresa1
curl -Lbk -m 4555 -m 6555 -k  https://www.redtube.com/$adresa1 > /tmp/test/x1
cd /tmp/test
awk '/1080/ {print}' x1 > x2
sed 's/\(["]\+\)/\n\1/g' x2 > x3
awk '/1080P_4000K/ {print}' x3 > x4
tr -d '[\]' < "x4" > x5
sed -n '1,1p' x5 >> seznam
awk '/<h1 class="video_title">/ {print}' x1 >> seznam
#################################################
adresa1=`sed -n '16,16p' www`
adresa1=$adresa1
curl -Lbk -m 4555 -m 6555 -k  https://www.redtube.com/$adresa1 > /tmp/test/x1
cd /tmp/test
awk '/1080/ {print}' x1 > x2
sed 's/\(["]\+\)/\n\1/g' x2 > x3
awk '/1080P_4000K/ {print}' x3 > x4
tr -d '[\]' < "x4" > x5
sed -n '1,1p' x5 >> seznam
awk '/<h1 class="video_title">/ {print}' x1 >> seznam
#################################################
adresa1=`sed -n '17,17p' www`
adresa1=$adresa1
curl -Lbk -m 4555 -m 6555 -k  https://www.redtube.com/$adresa1 > /tmp/test/x1
cd /tmp/test
awk '/1080/ {print}' x1 > x2
sed 's/\(["]\+\)/\n\1/g' x2 > x3
awk '/1080P_4000K/ {print}' x3 > x4
tr -d '[\]' < "x4" > x5
sed -n '1,1p' x5 >> seznam
awk '/<h1 class="video_title">/ {print}' x1 >> seznam
#################################################
adresa1=`sed -n '18,18p' www`
adresa1=$adresa1
curl -Lbk -m 4555 -m 6555 -k  https://www.redtube.com/$adresa1 > /tmp/test/x1
cd /tmp/test
awk '/1080/ {print}' x1 > x2
sed 's/\(["]\+\)/\n\1/g' x2 > x3
awk '/1080P_4000K/ {print}' x3 > x4
tr -d '[\]' < "x4" > x5
sed -n '1,1p' x5 >> seznam
awk '/<h1 class="video_title">/ {print}' x1 >> seznam
#################################################
adresa1=`sed -n '19,19p' www`
adresa1=$adresa1
curl -Lbk -m 4555 -m 6555 -k  https://www.redtube.com/$adresa1 > /tmp/test/x1
cd /tmp/test
awk '/1080/ {print}' x1 > x2
sed 's/\(["]\+\)/\n\1/g' x2 > x3
awk '/1080P_4000K/ {print}' x3 > x4
tr -d '[\]' < "x4" > x5
sed -n '1,1p' x5 >> seznam
awk '/<h1 class="video_title">/ {print}' x1 >> seznam
#################################################
adresa1=`sed -n '20,20p' www`
adresa1=$adresa1
curl -Lbk -m 4555 -m 6555 -k  https://www.redtube.com/$adresa1 > /tmp/test/x1
cd /tmp/test
awk '/1080/ {print}' x1 > x2
sed 's/\(["]\+\)/\n\1/g' x2 > x3
awk '/1080P_4000K/ {print}' x3 > x4
tr -d '[\]' < "x4" > x5
sed -n '1,1p' x5 >> seznam
awk '/<h1 class="video_title">/ {print}' x1 >> seznam
#################################################
sed -e "s/https:/#SERVICE 4097:0:1128:0:0:0:0:0:0:0:https%3a/" seznam > seznam1
tr -d '["]' < "seznam1" > seznam2
sed -e "s/h1 class=video_title>/#DESCRIPTION /" seznam2 > seznam3
grep -o -i '#[^<]*' seznam3 > seznam4
#################################################
echo "#NAME BLACKEDxxx.m3u" > /etc/enigma2/userbouquet.BLACKEDxxx.m3u.tv
cat seznam4 >> /etc/enigma2/userbouquet.BLACKEDxxx.m3u.tv
cd /
rm -rf /tmp/test
###########################################################################################################
wget -q -O - http://root%s@127.0.0.1/web/servicelistreload?mode=0 >>/dev/null 2>&1 </dev/null &
sleep 2
echo "OK"
exit









