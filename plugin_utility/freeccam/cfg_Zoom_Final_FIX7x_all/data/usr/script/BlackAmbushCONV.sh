#!/bin/sh
echo "stahuji BlackAmbush"
[ -d /tmp/test ] || mkdir -p /tmp/test
more /usr/lib/enigma2/python/Plugins/Extensions/OpenPanel/DATA/x  >> /etc/enigma2/bouquets.tv 
sed -i "s/%/userbouquet.BlackAmbushxxx.m3u.tv/" /etc/enigma2/bouquets.tv 
cd /tmp/test

curl -Lbk -m 4555 -m 6555 -k  https://www.redtube.com/32874071 > /tmp/test/x1
cd /tmp/test
awk '/1080/ {print}' x1 > x2
sed 's/\(["]\+\)/\n\1/g' x2 > x3
awk '/1080P_4000K/ {print}' x3 > x4
tr -d '[\]' < "x4" > x5
sed -n '1,1p' x5 > seznam
awk '/<h1 class="video_title">/ {print}' x1 >> seznam
#################################################
curl -Lbk -m 4555 -m 6555 -k  https://www.redtube.com/17218091 > /tmp/test/x1
cd /tmp/test
awk '/1080/ {print}' x1 > x2
sed 's/\(["]\+\)/\n\1/g' x2 > x3
awk '/1080P_4000K/ {print}' x3 > x4
tr -d '[\]' < "x4" > x5
sed -n '1,1p' x5 >> seznam
awk '/<h1 class="video_title">/ {print}' x1 >> seznam
#################################################
curl -Lbk -m 4555 -m 6555 -k  https://www.redtube.com/21415821 > /tmp/test/x1
cd /tmp/test
awk '/1080/ {print}' x1 > x2
sed 's/\(["]\+\)/\n\1/g' x2 > x3
awk '/1080P_4000K/ {print}' x3 > x4
tr -d '[\]' < "x4" > x5
sed -n '1,1p' x5 >> seznam
awk '/<h1 class="video_title">/ {print}' x1 >> seznam
#################################################
curl -Lbk -m 4555 -m 6555 -k  https://www.redtube.com/16129041 > /tmp/test/x1
cd /tmp/test
awk '/1080/ {print}' x1 > x2
sed 's/\(["]\+\)/\n\1/g' x2 > x3
awk '/1080P_4000K/ {print}' x3 > x4
tr -d '[\]' < "x4" > x5
sed -n '1,1p' x5 >> seznam
awk '/<h1 class="video_title">/ {print}' x1 >> seznam
#################################################
curl -Lbk -m 4555 -m 6555 -k  https://www.redtube.com/17846291 > /tmp/test/x1
cd /tmp/test
awk '/1080/ {print}' x1 > x2
sed 's/\(["]\+\)/\n\1/g' x2 > x3
awk '/1080P_4000K/ {print}' x3 > x4
tr -d '[\]' < "x4" > x5
sed -n '1,1p' x5 >> seznam
awk '/<h1 class="video_title">/ {print}' x1 >> seznam
#################################################
curl -Lbk -m 4555 -m 6555 -k  https://www.redtube.com/18162211 > /tmp/test/x1
cd /tmp/test
awk '/1080/ {print}' x1 > x2
sed 's/\(["]\+\)/\n\1/g' x2 > x3
awk '/1080P_4000K/ {print}' x3 > x4
tr -d '[\]' < "x4" > x5
sed -n '1,1p' x5 >> seznam
awk '/<h1 class="video_title">/ {print}' x1 >> seznam
#################################################
curl -Lbk -m 4555 -m 6555 -k  https://www.redtube.com/23877771 > /tmp/test/x1
cd /tmp/test
awk '/1080/ {print}' x1 > x2
sed 's/\(["]\+\)/\n\1/g' x2 > x3
awk '/1080P_4000K/ {print}' x3 > x4
tr -d '[\]' < "x4" > x5
sed -n '1,1p' x5 >> seznam
awk '/<h1 class="video_title">/ {print}' x1 >> seznam
#################################################
curl -Lbk -m 4555 -m 6555 -k  https://www.redtube.com/18882541 > /tmp/test/x1
cd /tmp/test
awk '/1080/ {print}' x1 > x2
sed 's/\(["]\+\)/\n\1/g' x2 > x3
awk '/1080P_4000K/ {print}' x3 > x4
tr -d '[\]' < "x4" > x5
sed -n '1,1p' x5 >> seznam
awk '/<h1 class="video_title">/ {print}' x1 >> seznam
#################################################
curl -Lbk -m 4555 -m 6555 -k  https://www.redtube.com/24869241 > /tmp/test/x1
cd /tmp/test
awk '/1080/ {print}' x1 > x2
sed 's/\(["]\+\)/\n\1/g' x2 > x3
awk '/1080P_4000K/ {print}' x3 > x4
tr -d '[\]' < "x4" > x5
sed -n '1,1p' x5 >> seznam
awk '/<h1 class="video_title">/ {print}' x1 >> seznam
#################################################
curl -Lbk -m 4555 -m 6555 -k  https://www.redtube.com/16936241 > /tmp/test/x1
cd /tmp/test
awk '/1080/ {print}' x1 > x2
sed 's/\(["]\+\)/\n\1/g' x2 > x3
awk '/1080P_4000K/ {print}' x3 > x4
tr -d '[\]' < "x4" > x5
sed -n '1,1p' x5 >> seznam
awk '/<h1 class="video_title">/ {print}' x1 >> seznam
#################################################
curl -Lbk -m 4555 -m 6555 -k  https://www.redtube.com/17704871 > /tmp/test/x1
cd /tmp/test
awk '/1080/ {print}' x1 > x2
sed 's/\(["]\+\)/\n\1/g' x2 > x3
awk '/1080P_4000K/ {print}' x3 > x4
tr -d '[\]' < "x4" > x5
sed -n '1,1p' x5 >> seznam
awk '/<h1 class="video_title">/ {print}' x1 >> seznam
#################################################
curl -Lbk -m 4555 -m 6555 -k  https://www.redtube.com/19489581 > /tmp/test/x1
cd /tmp/test
awk '/1080/ {print}' x1 > x2
sed 's/\(["]\+\)/\n\1/g' x2 > x3
awk '/1080P_4000K/ {print}' x3 > x4
tr -d '[\]' < "x4" > x5
sed -n '1,1p' x5 >> seznam
awk '/<h1 class="video_title">/ {print}' x1 >> seznam
#################################################
curl -Lbk -m 4555 -m 6555 -k  https://www.redtube.com/25223041 > /tmp/test/x1
cd /tmp/test
awk '/1080/ {print}' x1 > x2
sed 's/\(["]\+\)/\n\1/g' x2 > x3
awk '/1080P_4000K/ {print}' x3 > x4
tr -d '[\]' < "x4" > x5
sed -n '1,1p' x5 >> seznam
awk '/<h1 class="video_title">/ {print}' x1 >> seznam
#################################################
curl -Lbk -m 4555 -m 6555 -k  https://www.redtube.com/24196651 > /tmp/test/x1
cd /tmp/test
awk '/1080/ {print}' x1 > x2
sed 's/\(["]\+\)/\n\1/g' x2 > x3
awk '/1080P_4000K/ {print}' x3 > x4
tr -d '[\]' < "x4" > x5
sed -n '1,1p' x5 >> seznam
awk '/<h1 class="video_title">/ {print}' x1 >> seznam
#################################################
curl -Lbk -m 4555 -m 6555 -k  https://www.redtube.com/28575981 > /tmp/test/x1
cd /tmp/test
awk '/1080/ {print}' x1 > x2
sed 's/\(["]\+\)/\n\1/g' x2 > x3
awk '/1080P_4000K/ {print}' x3 > x4
tr -d '[\]' < "x4" > x5
sed -n '1,1p' x5 >> seznam
awk '/<h1 class="video_title">/ {print}' x1 >> seznam
#################################################
curl -Lbk -m 4555 -m 6555 -k  https://www.redtube.com/27803631 > /tmp/test/x1
cd /tmp/test
awk '/1080/ {print}' x1 > x2
sed 's/\(["]\+\)/\n\1/g' x2 > x3
awk '/1080P_4000K/ {print}' x3 > x4
tr -d '[\]' < "x4" > x5
sed -n '1,1p' x5 >> seznam
awk '/<h1 class="video_title">/ {print}' x1 >> seznam
#################################################
curl -Lbk -m 4555 -m 6555 -k  https://www.redtube.com/30576281 > /tmp/test/x1
cd /tmp/test
awk '/1080/ {print}' x1 > x2
sed 's/\(["]\+\)/\n\1/g' x2 > x3
awk '/1080P_4000K/ {print}' x3 > x4
tr -d '[\]' < "x4" > x5
sed -n '1,1p' x5 >> seznam
awk '/<h1 class="video_title">/ {print}' x1 >> seznam
#################################################
curl -Lbk -m 4555 -m 6555 -k  https://www.redtube.com/30239751 > /tmp/test/x1
cd /tmp/test
awk '/1080/ {print}' x1 > x2
sed 's/\(["]\+\)/\n\1/g' x2 > x3
awk '/1080P_4000K/ {print}' x3 > x4
tr -d '[\]' < "x4" > x5
sed -n '1,1p' x5 >> seznam
awk '/<h1 class="video_title">/ {print}' x1 >> seznam
#################################################
curl -Lbk -m 4555 -m 6555 -k  https://www.redtube.com/22640351 > /tmp/test/x1
cd /tmp/test
awk '/1080/ {print}' x1 > x2
sed 's/\(["]\+\)/\n\1/g' x2 > x3
awk '/1080P_4000K/ {print}' x3 > x4
tr -d '[\]' < "x4" > x5
sed -n '1,1p' x5 >> seznam
awk '/<h1 class="video_title">/ {print}' x1 >> seznam
#################################################
curl -Lbk -m 4555 -m 6555 -k  https://www.redtube.com/30421021 > /tmp/test/x1
cd /tmp/test
awk '/1080/ {print}' x1 > x2
sed 's/\(["]\+\)/\n\1/g' x2 > x3
awk '/1080P_4000K/ {print}' x3 > x4
tr -d '[\]' < "x4" > x5
sed -n '1,1p' x5 >> seznam
awk '/<h1 class="video_title">/ {print}' x1 >> seznam
#################################################
curl -Lbk -m 4555 -m 6555 -k  https://www.redtube.com/18082361 > /tmp/test/x1
cd /tmp/test
awk '/1080/ {print}' x1 > x2
sed 's/\(["]\+\)/\n\1/g' x2 > x3
awk '/1080P_4000K/ {print}' x3 > x4
tr -d '[\]' < "x4" > x5
sed -n '1,1p' x5 >> seznam
awk '/<h1 class="video_title">/ {print}' x1 >> seznam
#################################################
curl -Lbk -m 4555 -m 6555 -k  https://www.redtube.com/18987901 > /tmp/test/x1
cd /tmp/test
awk '/1080/ {print}' x1 > x2
sed 's/\(["]\+\)/\n\1/g' x2 > x3
awk '/1080P_4000K/ {print}' x3 > x4
tr -d '[\]' < "x4" > x5
sed -n '1,1p' x5 >> seznam
awk '/<h1 class="video_title">/ {print}' x1 >> seznam
#################################################
curl -Lbk -m 4555 -m 6555 -k  https://www.redtube.com/28904211 > /tmp/test/x1
cd /tmp/test
awk '/1080/ {print}' x1 > x2
sed 's/\(["]\+\)/\n\1/g' x2 > x3
awk '/1080P_4000K/ {print}' x3 > x4
tr -d '[\]' < "x4" > x5
sed -n '1,1p' x5 >> seznam
awk '/<h1 class="video_title">/ {print}' x1 >> seznam
#################################################
curl -Lbk -m 4555 -m 6555 -k  https://www.redtube.com/30025081 > /tmp/test/x1
cd /tmp/test
awk '/1080/ {print}' x1 > x2
sed 's/\(["]\+\)/\n\1/g' x2 > x3
awk '/1080P_4000K/ {print}' x3 > x4
tr -d '[\]' < "x4" > x5
sed -n '1,1p' x5 >> seznam
awk '/<h1 class="video_title">/ {print}' x1 >> seznam
#################################################
curl -Lbk -m 4555 -m 6555 -k  https://www.redtube.com/29108311 > /tmp/test/x1
cd /tmp/test
awk '/1080/ {print}' x1 > x2
sed 's/\(["]\+\)/\n\1/g' x2 > x3
awk '/1080P_4000K/ {print}' x3 > x4
tr -d '[\]' < "x4" > x5
sed -n '1,1p' x5 >> seznam
awk '/<h1 class="video_title">/ {print}' x1 >> seznam
#################################################
curl -Lbk -m 4555 -m 6555 -k  https://www.redtube.com/29264501 > /tmp/test/x1
cd /tmp/test
awk '/1080/ {print}' x1 > x2
sed 's/\(["]\+\)/\n\1/g' x2 > x3
awk '/1080P_4000K/ {print}' x3 > x4
tr -d '[\]' < "x4" > x5
sed -n '1,1p' x5 >> seznam
awk '/<h1 class="video_title">/ {print}' x1 >> seznam
#################################################
curl -Lbk -m 4555 -m 6555 -k  https://www.redtube.com/29569181> /tmp/test/x1
cd /tmp/test
awk '/1080/ {print}' x1 > x2
sed 's/\(["]\+\)/\n\1/g' x2 > x3
awk '/1080P_4000K/ {print}' x3 > x4
tr -d '[\]' < "x4" > x5
sed -n '1,1p' x5 >> seznam
awk '/<h1 class="video_title">/ {print}' x1 >> seznam
#################################################
curl -Lbk -m 4555 -m 6555 -k  https://www.redtube.com/30143331> /tmp/test/x1
cd /tmp/test
awk '/1080/ {print}' x1 > x2
sed 's/\(["]\+\)/\n\1/g' x2 > x3
awk '/1080P_4000K/ {print}' x3 > x4
tr -d '[\]' < "x4" > x5
sed -n '1,1p' x5 >> seznam
awk '/<h1 class="video_title">/ {print}' x1 >> seznam
#################################################
curl -Lbk -m 4555 -m 6555 -k  https://www.redtube.com/5620631> /tmp/test/x1
cd /tmp/test
awk '/1080/ {print}' x1 > x2
sed 's/\(["]\+\)/\n\1/g' x2 > x3
awk '/1080P_4000K/ {print}' x3 > x4
tr -d '[\]' < "x4" > x5
sed -n '1,1p' x5 >> seznam
awk '/<h1 class="video_title">/ {print}' x1 >> seznam
#################################################
curl -Lbk -m 4555 -m 6555 -k  https://www.redtube.com/5100451> /tmp/test/x1
cd /tmp/test
awk '/1080/ {print}' x1 > x2
sed 's/\(["]\+\)/\n\1/g' x2 > x3
awk '/1080P_4000K/ {print}' x3 > x4
tr -d '[\]' < "x4" > x5
sed -n '1,1p' x5 >> seznam
awk '/<h1 class="video_title">/ {print}' x1 >> seznam
#################################################
curl -Lbk -m 4555 -m 6555 -k  https://www.redtube.com/10858531> /tmp/test/x1
cd /tmp/test
awk '/1080/ {print}' x1 > x2
sed 's/\(["]\+\)/\n\1/g' x2 > x3
awk '/1080P_4000K/ {print}' x3 > x4
tr -d '[\]' < "x4" > x5
sed -n '1,1p' x5 >> seznam
awk '/<h1 class="video_title">/ {print}' x1 >> seznam
#################################################
curl -Lbk -m 4555 -m 6555 -k  https://www.redtube.com/4047041> /tmp/test/x1
cd /tmp/test
awk '/1080/ {print}' x1 > x2
sed 's/\(["]\+\)/\n\1/g' x2 > x3
awk '/1080P_4000K/ {print}' x3 > x4
tr -d '[\]' < "x4" > x5
sed -n '1,1p' x5 >> seznam
awk '/<h1 class="video_title">/ {print}' x1 >> seznam
#################################################
curl -Lbk -m 4555 -m 6555 -k  https://www.redtube.com/1126328> /tmp/test/x1
cd /tmp/test
awk '/1080/ {print}' x1 > x2
sed 's/\(["]\+\)/\n\1/g' x2 > x3
awk '/1080P_4000K/ {print}' x3 > x4
tr -d '[\]' < "x4" > x5
sed -n '1,1p' x5 >> seznam
awk '/<h1 class="video_title">/ {print}' x1 >> seznam
#################################################
curl -Lbk -m 4555 -m 6555 -k  https://www.redtube.com/1506442> /tmp/test/x1
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
echo "#NAME BlackAmbushxxx.m3u" > /etc/enigma2/userbouquet.BlackAmbushxxx.m3u.tv
cat seznam4 >> /etc/enigma2/userbouquet.BlackAmbushxxx.m3u.tv
cd /
rm -rf /tmp/test
###########################################################################################################
wget -q -O - http://root%s@127.0.0.1/web/servicelistreload?mode=0 >>/dev/null 2>&1 </dev/null &
sleep 2
echo "OK"
exit








