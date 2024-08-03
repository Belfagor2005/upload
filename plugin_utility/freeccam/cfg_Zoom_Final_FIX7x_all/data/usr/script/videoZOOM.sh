#!/bin/sh
echo "stahuji odkaz pro video ...ZOOM"

echo "ukládám ..."

echo "zobrazuji...."
echo ""
echo ""



[ -d /tmp/test ] || mkdir -p /tmp/test



curl -k -A -k  -X POST \
        -d 'v=5.92' \
        -d 'access_token=51b5a4fd4308476d1744a001598b409aca74ebdb1188570a7e535628a8365adfe0d0de1c058fe9a814924' \
        -d  videos=214185242_456241554 \
        https://api.vk.com/method/video.get > /tmp/test/CCcam



cd /tmp/test

grep -o -i '"https:[^"<]*' CCcam  > /tmp/test/CCcam1

if grep   'm3u8[^"<]*' CCcam1 >>/dev/null 2>&1 </dev/null ; then
grep   'm3u8[^"<]*' CCcam1  > /tmp/test/CCcam2
elif grep   '1080.mp4[^"<]*' CCcam1 >>/dev/null 2>&1 </dev/null ; then
grep   '1080.mp4[^"<]*' CCcam1  > /tmp/test/CCcam2
elif grep   '720.mp4[^"<]*' CCcam1 >>/dev/null 2>&1 </dev/null ; then
grep   '720.mp4[^"<]*' CCcam1  > /tmp/test/CCcam2
elif grep   '480.mp4[^"<]*' CCcam1 >>/dev/null 2>&1 </dev/null ; then
grep   '480.mp4[^"<]*' CCcam1  > /tmp/test/CCcam2
elif grep   '360.mp4[^"<]*' CCcam1 >>/dev/null 2>&1 </dev/null ; then
grep   '360.mp4[^"<]*' CCcam1  > /tmp/test/CCcam2
elif grep   '240.mp4[^"<]*' CCcam1 >>/dev/null 2>&1 </dev/null ; then
grep   '240.mp4[^"<]*' CCcam1  > /tmp/test/CCcam2
fi






rm -rf /etc/enigma2/userbouquet.ZOOM.m3u.tv >>/dev/null 2>&1 </dev/null &
sed -i '/userbouquet.ZOOM.m3u.tv/d' /etc/enigma2/bouquets.tv
rm -rf /etc/enigma2/userbouquet.ZOOM.m3u.tv.del >>/dev/null 2>&1 </dev/null &
wget -q -O - http://127.0.0.1/web/servicelistreload?mode=2 > /dev/null 2>&1
sed -i '/ZOOM/d' /etc/enigma2/bouquets.tv
wget -q -O - http://127.0.0.1/web/servicelistreload?mode=2 > /dev/null 2>&1

sed -i 's#\\##g' /tmp/test/CCcam2
sed -i 's/"https:/#SERVICE 4097:0:1:1:0:0:0:0:0:0:https%3a/g' /tmp/test/CCcam2

echo '#NAME ZOOM' > /etc/enigma2/userbouquet.ZOOM.m3u.tv
sed -n '1,1p' /tmp/test/CCcam2 >> /etc/enigma2/userbouquet.ZOOM.m3u.tv
echo '#DESCRIPTION ZOOM' >> /etc/enigma2/userbouquet.ZOOM.m3u.tv


echo '#SERVICE 1:7:1:0:0:0:0:0:0:0:FROM BOUQUET "userbouquet.ZOOM.m3u.tv" ORDER BY bouquet' >> /etc/enigma2/bouquets.tv
wget -q -O - http://127.0.0.1/web/servicelistreload?mode=2 > /dev/null 2>&1
[ -d /tmp/test ] || mkdir -p /tmp/test
[ -d /movie ] || mkdir -p /movie
echo  "#EXTM3U" > /tmp/test/FILM.m3u
echo '#DESCRIPTION ZOOM' >> /tmp/test/FILM.m3u
sed -i 's/#DESCRIPTION /#EXTINF:0,/g' /tmp/test/FILM.m3u
sed -n '1,1p' /tmp/test/CCcam2 >> /tmp/test/FILM.m3u
sed -i 's/#SERVICE 4097:0:1:1:0:0:0:0:0:0://g' /tmp/test/FILM.m3u
sed -i 's/%3a/:/g' /tmp/test/FILM.m3u
cat /tmp/test/FILM.m3u > /movie/ZOOM.m3u
cd /
rm -rf /tmp/test

wget -q -O - http://127.0.0.1/web/zap?sRef=1:7:1:0:0:0:0:0:0:0:FROM%20BOUQUET%20%22userbouquet.ZOOM.m3u.tv%22%20ORDER%20BY%20bouquet  >>/dev/null 2>&1 </dev/null &
exit
