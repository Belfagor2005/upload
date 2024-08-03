#!/bin/sh
echo "stahuji z : VK.com"

echo "ukládám server..."

echo "zobrazuji...."
echo ""
echo ""

sed -i '/userbouquet.VKporn.m3u.tv/d' /etc/enigma2/bouquets.tv
more /usr/lib/enigma2/python/Plugins/Extensions/OpenPanel/DATA/x  >> /etc/enigma2/bouquets.tv 
sed -i "s/%/userbouquet.VKporn.m3u.tv/" /etc/enigma2/bouquets.tv 

[ -d /tmp/test ] || mkdir -p /tmp/test

curl -k -A -k  -X POST \
        -d 'v=5.92' \
        -d 'access_token=51b5a4fd4308476d1744a001598b409aca74ebdb1188570a7e535628a8365adfe0d0de1c058fe9a814924' \
        -d 'video214185242_456240239' \
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





grep   'm3u8[^"<]*' CCcam1  > /tmp/test/CCcam2

sed -i 's#\\##g' /tmp/test/CCcam2

sed -i 's#"#" #g' /tmp/test/CCcam2

sed -i 's#"#%#g' /tmp/test/CCcam2

sed -i 's#m3u8#m3u#g' /tmp/test/CCcam2
grep  -n '%[^"<]*' /tmp/test/CCcam2 > /tmp/test/CCcam3
sed -i 's#:%# %#g' /tmp/test/CCcam3
awk '{print $2,$1,$3} ' /tmp/test/CCcam3 > /tmp/test/CCcam4
sed -i 's#% #%#g' /tmp/test/CCcam4



sed 's/\([ ]\+\)/\n\1/g' CCcam4  > /tmp/test/CCcam5

sed -i 's# https:#https:#g' /tmp/test/CCcam5

sed -i 's"%"#DESCRIPTION XXX"g'  /tmp/test/CCcam5

sed -i 's"https:"#SERVICE 4097:0:1128:0:0:0:0:0:0:0:https%3a"g' /tmp/test/CCcam5




echo "#NAME VKporn.m3u" > /etc/enigma2/userbouquet.VKporn.m3u.tv
cat /tmp/test/CCcam5 >> /etc/enigma2/userbouquet.VKporn.m3u.tv

cd /
wget -q -O - http://root%s@127.0.0.1/web/servicelistreload?mode=0 >>/dev/null 2>&1 </dev/null &
sleep 2

rm -rf /tmp/test
echo "OK"
exit


