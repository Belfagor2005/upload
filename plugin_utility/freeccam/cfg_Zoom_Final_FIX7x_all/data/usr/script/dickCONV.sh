#!/bin/sh
echo "Stahování xxxBigDick.m3u"
echo "Downloading xxxBigDick.m3u"
echo "jdu předělávat pro E2...."
echo ""
echo ""

sed -i '/userbouquet.xxxBigDick.m3u.tv/d' /etc/enigma2/bouquets.tv 
more /usr/lib/enigma2/python/Plugins/Extensions/OpenPanel/DATA/x  >> /etc/enigma2/bouquets.tv 
sed -i "s/%/userbouquet.xxxBigDick.m3u.tv/" /etc/enigma2/bouquets.tv 

URL="https://www.eporner.com/cat/big-dick/";
# Files
TMP=`mktemp -d`
cd / ${TMP}

# Github
#agent="--header='User-Agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_0) AppleWebKit/600.1.17 (KHTML, like Gecko) Version/8.0 Safari/600.1.17'"
#crt="--no-check-certificate"

#wget -q $crt $agent $URL/CCcam
curl -s -Lbk -m 4 -m 6 -k ${URL}/CCcam -o CCcam
awk '/1080/ {print}' CCcam > CCcamX
awk '/data-id=/ {print}' CCcamX > CCcamXX
awk '/video-/ {print}' CCcamXX > CCcamXXX
sed -i 's"mbunder"%"g' CCcamXXX
cut -d '%' -f 1  CCcamXXX > CCcamX1
sed -i 's/\<video\>/!!X!!/2' CCcamX1
grep -E -o -i  '(alt="[^"<]*|video-[^/"<]*|data-st="[^"<]*)' CCcamX1 > CCcam1
sed -i 's"|":%"g' CCcam1
cut -d% -f 1 CCcam1 > CCcam2
sed 'N0,$!N;s/\n/ /' CCcam2 > CCcam3
sed -i 's# data-st="#/1080/#g' CCcam3
sed -i '/video-/s/:/-1080p.mp4/g' CCcam3
sed -i 's"video-"#SERVICE 4097:0:1128:0:0:0:0:0:0:0:https%3a//www.eporner.com/dload/"g' CCcam3
sed -i 's"alt="#DESCRIPTION "g' CCcam3
sed -i '/DESCRIPTION/s/"//g' CCcam3
echo "#NAME xxxBigDick.m3u" > /etc/enigma2/userbouquet.xxxBigDick.m3u.tv
cat CCcam3 >> /etc/enigma2/userbouquet.xxxBigDick.m3u.tv

cd /
wget -q -O - http://root%s@127.0.0.1/web/servicelistreload?mode=0 >>/dev/null 2>&1 </dev/null &
sleep 2
cd /tmp
rm -r *
echo "OK"
exit




