#!/bin/sh
sleep 1
echo "stahuji stream list musicBoxHitsOLD.m3u"
sleep 2
[ -d /movie ] || mkdir -p /movie
#################################################
rm -rf /etc/enigma2/userbouquet.musicBoxHitsOLD.m3u.tv >>/dev/null 2>&1 </dev/null &
sed -i '/userbouquet.musicBoxHitsOLD.m3u.tv/d' /etc/enigma2/bouquets.tv
wget -q -O - http://root%s@127.0.0.1/web/servicelistreload?mode=0 >>/dev/null 2>&1 </dev/null &
#################################################
[ -d /tmp/test ] || mkdir -p /tmp/test
#################################################
curl  -k -Lbk -m 55532 -m 555104 https://m.vk.com/video-114889127_456239375 > /tmp/test/a
grep -o -i '"VideoPageInfoRow__title">[^<]*' /tmp/test/a > /tmp/test/b
sed -i 's/"VideoPageInfoRow__title">/#EXTINF:-1,/g' /tmp/test/b
grep -o -i '<source src=[^<]*' /tmp/test/a > /tmp/test/a1
sed -i 's#%2F#/#g' /tmp/test/a1 
sed -i 's#%3A#:#g' /tmp/test/a1 
sed -i 's#=# #g' /tmp/test/a1 
sed -i 's#&# #g' /tmp/test/a1 
sed -i 's#?# #g' /tmp/test/a1 
sed -i 's#dirs%5B#!#g' /tmp/test/a1 
sed 's/\([!]\+\)/\n\1/g' /tmp/test/a1 > /tmp/test/a2
awk '{print NR " " $0}' /tmp/test/a2  > /tmp/test/a3
sort -n -r "/tmp/test/a3"|grep -o -i ' [^<]*'  > /tmp/test/y
sed -i 's#%5D#.mp4#g' /tmp/test/y
sed -i '$d' /tmp/test/y
sed -i 's#src "#!240.mp4 #g' /tmp/test/y
cut -d '/' -f -7  /tmp/test/y > /tmp/test/x
sed -i 's#videos#videos/#g' /tmp/test/x
cd /tmp/test
if grep -E "720.mp4" x > /dev/null; then
awk '/720/ {print}' x > x1
elif grep -E "720.mp4" x > /dev/null; then
awk '/720/ {print}' x > x1
elif grep -E "480.mp4" x > /dev/null; then
awk '/480/ {print}' x > x1
elif grep -E "240.mp4" x > /dev/null; then
awk '/240/ {print}' x > x1
fi
sed -n '1,1p' x1 > xx
awk '{print $ 2}' xx > stream
grep -o -i 'amp;tag[^<]*' /tmp/test/a3 |awk '{print $ 2}' >> stream
awk '{print $ 1}' x1|sed -n '1,1p' >> stream
cat stream | tr -d '\n' > adresa
sed -i 's#!#.#g' adresa 
cat /tmp/test/b > /tmp/music.m3u
cat /tmp/test/adresa >> /tmp/music.m3u
echo "" >> /tmp/music.m3u
#################################################
curl  -k -Lbk -m 55532 -m 555104 https://m.vk.com/video-139684770_456240744 > /tmp/test/a
grep -o -i '"VideoPageInfoRow__title">[^<]*' /tmp/test/a > /tmp/test/b
sed -i 's/"VideoPageInfoRow__title">/#EXTINF:-1,/g' /tmp/test/b
grep -o -i '<source src=[^<]*' /tmp/test/a > /tmp/test/a1
sed -i 's#%2F#/#g' /tmp/test/a1 
sed -i 's#%3A#:#g' /tmp/test/a1 
sed -i 's#=# #g' /tmp/test/a1 
sed -i 's#&# #g' /tmp/test/a1 
sed -i 's#?# #g' /tmp/test/a1 
sed -i 's#dirs%5B#!#g' /tmp/test/a1 
sed 's/\([!]\+\)/\n\1/g' /tmp/test/a1 > /tmp/test/a2
awk '{print NR " " $0}' /tmp/test/a2  > /tmp/test/a3
sort -n -r "/tmp/test/a3"|grep -o -i ' [^<]*'  > /tmp/test/y
sed -i 's#%5D#.mp4#g' /tmp/test/y
sed -i '$d' /tmp/test/y
sed -i 's#src "#!240.mp4 #g' /tmp/test/y
cut -d '/' -f -7  /tmp/test/y > /tmp/test/x
sed -i 's#videos#videos/#g' /tmp/test/x
cd /tmp/test
if grep -E "720.mp4" x > /dev/null; then
awk '/720/ {print}' x > x1
elif grep -E "720.mp4" x > /dev/null; then
awk '/720/ {print}' x > x1
elif grep -E "480.mp4" x > /dev/null; then
awk '/480/ {print}' x > x1
elif grep -E "240.mp4" x > /dev/null; then
awk '/240/ {print}' x > x1
fi
sed -n '1,1p' x1 > xx
awk '{print $ 2}' xx > stream
grep -o -i 'amp;tag[^<]*' /tmp/test/a3 |awk '{print $ 2}' >> stream
awk '{print $ 1}' x1|sed -n '1,1p' >> stream
cat stream | tr -d '\n' > adresa
sed -i 's#!#.#g' adresa 
cat /tmp/test/b >> /tmp/music.m3u
cat /tmp/test/adresa >> /tmp/music.m3u
echo "" >> /tmp/music.m3u
#################################################
curl  -k -Lbk -m 55532 -m 555104 https://m.vk.com/video89120072_171305931 > /tmp/test/a
grep -o -i '"VideoPageInfoRow__title">[^<]*' /tmp/test/a > /tmp/test/b
sed -i 's/"VideoPageInfoRow__title">/#EXTINF:-1,/g' /tmp/test/b
grep -o -i '<source src=[^<]*' /tmp/test/a > /tmp/test/a1
sed -i 's#%2F#/#g' /tmp/test/a1 
sed -i 's#%3A#:#g' /tmp/test/a1 
sed -i 's#=# #g' /tmp/test/a1 
sed -i 's#&# #g' /tmp/test/a1 
sed -i 's#?# #g' /tmp/test/a1 
sed -i 's#dirs%5B#!#g' /tmp/test/a1 
sed 's/\([!]\+\)/\n\1/g' /tmp/test/a1 > /tmp/test/a2
awk '{print NR " " $0}' /tmp/test/a2  > /tmp/test/a3
sort -n -r "/tmp/test/a3"|grep -o -i ' [^<]*'  > /tmp/test/y
sed -i 's#%5D#.mp4#g' /tmp/test/y
sed -i '$d' /tmp/test/y
sed -i 's#src "#!240.mp4 #g' /tmp/test/y
cut -d '/' -f -7  /tmp/test/y > /tmp/test/x
sed -i 's#videos#videos/#g' /tmp/test/x
cd /tmp/test
if grep -E "720.mp4" x > /dev/null; then
awk '/720/ {print}' x > x1
elif grep -E "720.mp4" x > /dev/null; then
awk '/720/ {print}' x > x1
elif grep -E "480.mp4" x > /dev/null; then
awk '/480/ {print}' x > x1
elif grep -E "240.mp4" x > /dev/null; then
awk '/240/ {print}' x > x1
fi
sed -n '1,1p' x1 > xx
awk '{print $ 2}' xx > stream
grep -o -i 'amp;tag[^<]*' /tmp/test/a3 |awk '{print $ 2}' >> stream
awk '{print $ 1}' x1|sed -n '1,1p' >> stream
cat stream | tr -d '\n' > adresa
sed -i 's#!#.#g' adresa 
cat /tmp/test/b >> /tmp/music.m3u
cat /tmp/test/adresa >> /tmp/music.m3u
echo "" >> /tmp/music.m3u
#################################################
curl  -k -Lbk -m 55532 -m 555104 https://m.vk.com/video318774445_456239676 > /tmp/test/a
grep -o -i '"VideoPageInfoRow__title">[^<]*' /tmp/test/a > /tmp/test/b
sed -i 's/"VideoPageInfoRow__title">/#EXTINF:-1,/g' /tmp/test/b
grep -o -i '<source src=[^<]*' /tmp/test/a > /tmp/test/a1
sed -i 's#%2F#/#g' /tmp/test/a1 
sed -i 's#%3A#:#g' /tmp/test/a1 
sed -i 's#=# #g' /tmp/test/a1 
sed -i 's#&# #g' /tmp/test/a1 
sed -i 's#?# #g' /tmp/test/a1 
sed -i 's#dirs%5B#!#g' /tmp/test/a1 
sed 's/\([!]\+\)/\n\1/g' /tmp/test/a1 > /tmp/test/a2
awk '{print NR " " $0}' /tmp/test/a2  > /tmp/test/a3
sort -n -r "/tmp/test/a3"|grep -o -i ' [^<]*'  > /tmp/test/y
sed -i 's#%5D#.mp4#g' /tmp/test/y
sed -i '$d' /tmp/test/y
sed -i 's#src "#!240.mp4 #g' /tmp/test/y
cut -d '/' -f -7  /tmp/test/y > /tmp/test/x
sed -i 's#videos#videos/#g' /tmp/test/x
cd /tmp/test
if grep -E "720.mp4" x > /dev/null; then
awk '/720/ {print}' x > x1
elif grep -E "720.mp4" x > /dev/null; then
awk '/720/ {print}' x > x1
elif grep -E "480.mp4" x > /dev/null; then
awk '/480/ {print}' x > x1
elif grep -E "240.mp4" x > /dev/null; then
awk '/240/ {print}' x > x1
fi
sed -n '1,1p' x1 > xx
awk '{print $ 2}' xx > stream
grep -o -i 'amp;tag[^<]*' /tmp/test/a3 |awk '{print $ 2}' >> stream
awk '{print $ 1}' x1|sed -n '1,1p' >> stream
cat stream | tr -d '\n' > adresa
sed -i 's#!#.#g' adresa 
cat /tmp/test/b >> /tmp/music.m3u
cat /tmp/test/adresa >> /tmp/music.m3u
echo "" >> /tmp/music.m3u
#################################################
curl  -k -Lbk -m 55532 -m 555104 https://m.vk.com/video216250843_456245103 > /tmp/test/a
grep -o -i '"VideoPageInfoRow__title">[^<]*' /tmp/test/a > /tmp/test/b
sed -i 's/"VideoPageInfoRow__title">/#EXTINF:-1,/g' /tmp/test/b
grep -o -i '<source src=[^<]*' /tmp/test/a > /tmp/test/a1
sed -i 's#%2F#/#g' /tmp/test/a1 
sed -i 's#%3A#:#g' /tmp/test/a1 
sed -i 's#=# #g' /tmp/test/a1 
sed -i 's#&# #g' /tmp/test/a1 
sed -i 's#?# #g' /tmp/test/a1 
sed -i 's#dirs%5B#!#g' /tmp/test/a1 
sed 's/\([!]\+\)/\n\1/g' /tmp/test/a1 > /tmp/test/a2
awk '{print NR " " $0}' /tmp/test/a2  > /tmp/test/a3
sort -n -r "/tmp/test/a3"|grep -o -i ' [^<]*'  > /tmp/test/y
sed -i 's#%5D#.mp4#g' /tmp/test/y
sed -i '$d' /tmp/test/y
sed -i 's#src "#!240.mp4 #g' /tmp/test/y
cut -d '/' -f -7  /tmp/test/y > /tmp/test/x
sed -i 's#videos#videos/#g' /tmp/test/x
cd /tmp/test
if grep -E "720.mp4" x > /dev/null; then
awk '/720/ {print}' x > x1
elif grep -E "720.mp4" x > /dev/null; then
awk '/720/ {print}' x > x1
elif grep -E "480.mp4" x > /dev/null; then
awk '/480/ {print}' x > x1
elif grep -E "240.mp4" x > /dev/null; then
awk '/240/ {print}' x > x1
fi
sed -n '1,1p' x1 > xx
awk '{print $ 2}' xx > stream
grep -o -i 'amp;tag[^<]*' /tmp/test/a3 |awk '{print $ 2}' >> stream
awk '{print $ 1}' x1|sed -n '1,1p' >> stream
cat stream | tr -d '\n' > adresa
sed -i 's#!#.#g' adresa 
cat /tmp/test/b >> /tmp/music.m3u
cat /tmp/test/adresa >> /tmp/music.m3u
echo "" >> /tmp/music.m3u
#################################################
curl  -k -Lbk -m 55532 -m 555104 https://m.vk.com/video-179704540_456239025 > /tmp/test/a
grep -o -i '"VideoPageInfoRow__title">[^<]*' /tmp/test/a > /tmp/test/b
sed -i 's/"VideoPageInfoRow__title">/#EXTINF:-1,/g' /tmp/test/b
grep -o -i '<source src=[^<]*' /tmp/test/a > /tmp/test/a1
sed -i 's#%2F#/#g' /tmp/test/a1 
sed -i 's#%3A#:#g' /tmp/test/a1 
sed -i 's#=# #g' /tmp/test/a1 
sed -i 's#&# #g' /tmp/test/a1 
sed -i 's#?# #g' /tmp/test/a1 
sed -i 's#dirs%5B#!#g' /tmp/test/a1 
sed 's/\([!]\+\)/\n\1/g' /tmp/test/a1 > /tmp/test/a2
awk '{print NR " " $0}' /tmp/test/a2  > /tmp/test/a3
sort -n -r "/tmp/test/a3"|grep -o -i ' [^<]*'  > /tmp/test/y
sed -i 's#%5D#.mp4#g' /tmp/test/y
sed -i '$d' /tmp/test/y
sed -i 's#src "#!240.mp4 #g' /tmp/test/y
cut -d '/' -f -7  /tmp/test/y > /tmp/test/x
sed -i 's#videos#videos/#g' /tmp/test/x
cd /tmp/test
if grep -E "720.mp4" x > /dev/null; then
awk '/720/ {print}' x > x1
elif grep -E "720.mp4" x > /dev/null; then
awk '/720/ {print}' x > x1
elif grep -E "480.mp4" x > /dev/null; then
awk '/480/ {print}' x > x1
elif grep -E "240.mp4" x > /dev/null; then
awk '/240/ {print}' x > x1
fi
sed -n '1,1p' x1 > xx
awk '{print $ 2}' xx > stream
grep -o -i 'amp;tag[^<]*' /tmp/test/a3 |awk '{print $ 2}' >> stream
awk '{print $ 1}' x1|sed -n '1,1p' >> stream
cat stream | tr -d '\n' > adresa
sed -i 's#!#.#g' adresa 
cat /tmp/test/b >> /tmp/music.m3u
cat /tmp/test/adresa >> /tmp/music.m3u
echo "" >> /tmp/music.m3u
#################################################
curl  -k -Lbk -m 55532 -m 555104 https://m.vk.com/video238946541_456239469 > /tmp/test/a
grep -o -i '"VideoPageInfoRow__title">[^<]*' /tmp/test/a > /tmp/test/b
sed -i 's/"VideoPageInfoRow__title">/#EXTINF:-1,/g' /tmp/test/b
grep -o -i '<source src=[^<]*' /tmp/test/a > /tmp/test/a1
sed -i 's#%2F#/#g' /tmp/test/a1 
sed -i 's#%3A#:#g' /tmp/test/a1 
sed -i 's#=# #g' /tmp/test/a1 
sed -i 's#&# #g' /tmp/test/a1 
sed -i 's#?# #g' /tmp/test/a1 
sed -i 's#dirs%5B#!#g' /tmp/test/a1 
sed 's/\([!]\+\)/\n\1/g' /tmp/test/a1 > /tmp/test/a2
awk '{print NR " " $0}' /tmp/test/a2  > /tmp/test/a3
sort -n -r "/tmp/test/a3"|grep -o -i ' [^<]*'  > /tmp/test/y
sed -i 's#%5D#.mp4#g' /tmp/test/y
sed -i '$d' /tmp/test/y
sed -i 's#src "#!240.mp4 #g' /tmp/test/y
cut -d '/' -f -7  /tmp/test/y > /tmp/test/x
sed -i 's#videos#videos/#g' /tmp/test/x
cd /tmp/test
if grep -E "720.mp4" x > /dev/null; then
awk '/720/ {print}' x > x1
elif grep -E "720.mp4" x > /dev/null; then
awk '/720/ {print}' x > x1
elif grep -E "480.mp4" x > /dev/null; then
awk '/480/ {print}' x > x1
elif grep -E "240.mp4" x > /dev/null; then
awk '/240/ {print}' x > x1
fi
sed -n '1,1p' x1 > xx
awk '{print $ 2}' xx > stream
grep -o -i 'amp;tag[^<]*' /tmp/test/a3 |awk '{print $ 2}' >> stream
awk '{print $ 1}' x1|sed -n '1,1p' >> stream
cat stream | tr -d '\n' > adresa
sed -i 's#!#.#g' adresa 
cat /tmp/test/b >> /tmp/music.m3u
cat /tmp/test/adresa >> /tmp/music.m3u
echo "" >> /tmp/music.m3u
#################################################
curl  -k -Lbk -m 55532 -m 555104 https://m.vk.com/video-49654036_171546748 > /tmp/test/a
grep -o -i '"VideoPageInfoRow__title">[^<]*' /tmp/test/a > /tmp/test/b
sed -i 's/"VideoPageInfoRow__title">/#EXTINF:-1,/g' /tmp/test/b
grep -o -i '<source src=[^<]*' /tmp/test/a > /tmp/test/a1
sed -i 's#%2F#/#g' /tmp/test/a1 
sed -i 's#%3A#:#g' /tmp/test/a1 
sed -i 's#=# #g' /tmp/test/a1 
sed -i 's#&# #g' /tmp/test/a1 
sed -i 's#?# #g' /tmp/test/a1 
sed -i 's#dirs%5B#!#g' /tmp/test/a1 
sed 's/\([!]\+\)/\n\1/g' /tmp/test/a1 > /tmp/test/a2
awk '{print NR " " $0}' /tmp/test/a2  > /tmp/test/a3
sort -n -r "/tmp/test/a3"|grep -o -i ' [^<]*'  > /tmp/test/y
sed -i 's#%5D#.mp4#g' /tmp/test/y
sed -i '$d' /tmp/test/y
sed -i 's#src "#!240.mp4 #g' /tmp/test/y
cut -d '/' -f -7  /tmp/test/y > /tmp/test/x
sed -i 's#videos#videos/#g' /tmp/test/x
cd /tmp/test
if grep -E "720.mp4" x > /dev/null; then
awk '/720/ {print}' x > x1
elif grep -E "720.mp4" x > /dev/null; then
awk '/720/ {print}' x > x1
elif grep -E "480.mp4" x > /dev/null; then
awk '/480/ {print}' x > x1
elif grep -E "240.mp4" x > /dev/null; then
awk '/240/ {print}' x > x1
fi
sed -n '1,1p' x1 > xx
awk '{print $ 2}' xx > stream
grep -o -i 'amp;tag[^<]*' /tmp/test/a3 |awk '{print $ 2}' >> stream
awk '{print $ 1}' x1|sed -n '1,1p' >> stream
cat stream | tr -d '\n' > adresa
sed -i 's#!#.#g' adresa 
cat /tmp/test/b >> /tmp/music.m3u
cat /tmp/test/adresa >> /tmp/music.m3u
echo "" >> /tmp/music.m3u
#################################################
curl  -k -Lbk -m 55532 -m 555104 https://m.vk.com/video216250843_456245787 > /tmp/test/a
grep -o -i '"VideoPageInfoRow__title">[^<]*' /tmp/test/a > /tmp/test/b
sed -i 's/"VideoPageInfoRow__title">/#EXTINF:-1,/g' /tmp/test/b
grep -o -i '<source src=[^<]*' /tmp/test/a > /tmp/test/a1
sed -i 's#%2F#/#g' /tmp/test/a1 
sed -i 's#%3A#:#g' /tmp/test/a1 
sed -i 's#=# #g' /tmp/test/a1 
sed -i 's#&# #g' /tmp/test/a1 
sed -i 's#?# #g' /tmp/test/a1 
sed -i 's#dirs%5B#!#g' /tmp/test/a1 
sed 's/\([!]\+\)/\n\1/g' /tmp/test/a1 > /tmp/test/a2
awk '{print NR " " $0}' /tmp/test/a2  > /tmp/test/a3
sort -n -r "/tmp/test/a3"|grep -o -i ' [^<]*'  > /tmp/test/y
sed -i 's#%5D#.mp4#g' /tmp/test/y
sed -i '$d' /tmp/test/y
sed -i 's#src "#!240.mp4 #g' /tmp/test/y
cut -d '/' -f -7  /tmp/test/y > /tmp/test/x
sed -i 's#videos#videos/#g' /tmp/test/x
cd /tmp/test
if grep -E "720.mp4" x > /dev/null; then
awk '/720/ {print}' x > x1
elif grep -E "720.mp4" x > /dev/null; then
awk '/720/ {print}' x > x1
elif grep -E "480.mp4" x > /dev/null; then
awk '/480/ {print}' x > x1
elif grep -E "240.mp4" x > /dev/null; then
awk '/240/ {print}' x > x1
fi
sed -n '1,1p' x1 > xx
awk '{print $ 2}' xx > stream
grep -o -i 'amp;tag[^<]*' /tmp/test/a3 |awk '{print $ 2}' >> stream
awk '{print $ 1}' x1|sed -n '1,1p' >> stream
cat stream | tr -d '\n' > adresa
sed -i 's#!#.#g' adresa 
cat /tmp/test/b >> /tmp/music.m3u
cat /tmp/test/adresa >> /tmp/music.m3u
echo "" >> /tmp/music.m3u
#################################################
curl  -k -Lbk -m 55532 -m 555104 https://m.vk.com/video-153970065_456239453 > /tmp/test/a
grep -o -i '"VideoPageInfoRow__title">[^<]*' /tmp/test/a > /tmp/test/b
sed -i 's/"VideoPageInfoRow__title">/#EXTINF:-1,/g' /tmp/test/b
grep -o -i '<source src=[^<]*' /tmp/test/a > /tmp/test/a1
sed -i 's#%2F#/#g' /tmp/test/a1 
sed -i 's#%3A#:#g' /tmp/test/a1 
sed -i 's#=# #g' /tmp/test/a1 
sed -i 's#&# #g' /tmp/test/a1 
sed -i 's#?# #g' /tmp/test/a1 
sed -i 's#dirs%5B#!#g' /tmp/test/a1 
sed 's/\([!]\+\)/\n\1/g' /tmp/test/a1 > /tmp/test/a2
awk '{print NR " " $0}' /tmp/test/a2  > /tmp/test/a3
sort -n -r "/tmp/test/a3"|grep -o -i ' [^<]*'  > /tmp/test/y
sed -i 's#%5D#.mp4#g' /tmp/test/y
sed -i '$d' /tmp/test/y
sed -i 's#src "#!240.mp4 #g' /tmp/test/y
cut -d '/' -f -7  /tmp/test/y > /tmp/test/x
sed -i 's#videos#videos/#g' /tmp/test/x
cd /tmp/test
if grep -E "720.mp4" x > /dev/null; then
awk '/720/ {print}' x > x1
elif grep -E "720.mp4" x > /dev/null; then
awk '/720/ {print}' x > x1
elif grep -E "480.mp4" x > /dev/null; then
awk '/480/ {print}' x > x1
elif grep -E "240.mp4" x > /dev/null; then
awk '/240/ {print}' x > x1
fi
sed -n '1,1p' x1 > xx
awk '{print $ 2}' xx > stream
grep -o -i 'amp;tag[^<]*' /tmp/test/a3 |awk '{print $ 2}' >> stream
awk '{print $ 1}' x1|sed -n '1,1p' >> stream
cat stream | tr -d '\n' > adresa
sed -i 's#!#.#g' adresa 
cat /tmp/test/b >> /tmp/music.m3u
cat /tmp/test/adresa >> /tmp/music.m3u
echo "" >> /tmp/music.m3u
#################################################
curl  -k -Lbk -m 55532 -m 555104 https://m.vk.com/video335534338_456243245 > /tmp/test/a
grep -o -i '"VideoPageInfoRow__title">[^<]*' /tmp/test/a > /tmp/test/b
sed -i 's/"VideoPageInfoRow__title">/#EXTINF:-1,/g' /tmp/test/b
grep -o -i '<source src=[^<]*' /tmp/test/a > /tmp/test/a1
sed -i 's#%2F#/#g' /tmp/test/a1 
sed -i 's#%3A#:#g' /tmp/test/a1 
sed -i 's#=# #g' /tmp/test/a1 
sed -i 's#&# #g' /tmp/test/a1 
sed -i 's#?# #g' /tmp/test/a1 
sed -i 's#dirs%5B#!#g' /tmp/test/a1 
sed 's/\([!]\+\)/\n\1/g' /tmp/test/a1 > /tmp/test/a2
awk '{print NR " " $0}' /tmp/test/a2  > /tmp/test/a3
sort -n -r "/tmp/test/a3"|grep -o -i ' [^<]*'  > /tmp/test/y
sed -i 's#%5D#.mp4#g' /tmp/test/y
sed -i '$d' /tmp/test/y
sed -i 's#src "#!240.mp4 #g' /tmp/test/y
cut -d '/' -f -7  /tmp/test/y > /tmp/test/x
sed -i 's#videos#videos/#g' /tmp/test/x
cd /tmp/test
if grep -E "720.mp4" x > /dev/null; then
awk '/720/ {print}' x > x1
elif grep -E "720.mp4" x > /dev/null; then
awk '/720/ {print}' x > x1
elif grep -E "480.mp4" x > /dev/null; then
awk '/480/ {print}' x > x1
elif grep -E "240.mp4" x > /dev/null; then
awk '/240/ {print}' x > x1
fi
sed -n '1,1p' x1 > xx
awk '{print $ 2}' xx > stream
grep -o -i 'amp;tag[^<]*' /tmp/test/a3 |awk '{print $ 2}' >> stream
awk '{print $ 1}' x1|sed -n '1,1p' >> stream
cat stream | tr -d '\n' > adresa
sed -i 's#!#.#g' adresa 
cat /tmp/test/b >> /tmp/music.m3u
cat /tmp/test/adresa >> /tmp/music.m3u
echo "" >> /tmp/music.m3u
#################################################
curl  -k -Lbk -m 55532 -m 555104 https://m.vk.com/video169160623_456239421 > /tmp/test/a
grep -o -i '"VideoPageInfoRow__title">[^<]*' /tmp/test/a > /tmp/test/b
sed -i 's/"VideoPageInfoRow__title">/#EXTINF:-1,/g' /tmp/test/b
grep -o -i '<source src=[^<]*' /tmp/test/a > /tmp/test/a1
sed -i 's#%2F#/#g' /tmp/test/a1 
sed -i 's#%3A#:#g' /tmp/test/a1 
sed -i 's#=# #g' /tmp/test/a1 
sed -i 's#&# #g' /tmp/test/a1 
sed -i 's#?# #g' /tmp/test/a1 
sed -i 's#dirs%5B#!#g' /tmp/test/a1 
sed 's/\([!]\+\)/\n\1/g' /tmp/test/a1 > /tmp/test/a2
awk '{print NR " " $0}' /tmp/test/a2  > /tmp/test/a3
sort -n -r "/tmp/test/a3"|grep -o -i ' [^<]*'  > /tmp/test/y
sed -i 's#%5D#.mp4#g' /tmp/test/y
sed -i '$d' /tmp/test/y
sed -i 's#src "#!240.mp4 #g' /tmp/test/y
cut -d '/' -f -7  /tmp/test/y > /tmp/test/x
sed -i 's#videos#videos/#g' /tmp/test/x
cd /tmp/test
if grep -E "720.mp4" x > /dev/null; then
awk '/720/ {print}' x > x1
elif grep -E "720.mp4" x > /dev/null; then
awk '/720/ {print}' x > x1
elif grep -E "480.mp4" x > /dev/null; then
awk '/480/ {print}' x > x1
elif grep -E "240.mp4" x > /dev/null; then
awk '/240/ {print}' x > x1
fi
sed -n '1,1p' x1 > xx
awk '{print $ 2}' xx > stream
grep -o -i 'amp;tag[^<]*' /tmp/test/a3 |awk '{print $ 2}' >> stream
awk '{print $ 1}' x1|sed -n '1,1p' >> stream
cat stream | tr -d '\n' > adresa
sed -i 's#!#.#g' adresa 
cat /tmp/test/b >> /tmp/music.m3u
cat /tmp/test/adresa >> /tmp/music.m3u
echo "" >> /tmp/music.m3u
#################################################
curl  -k -Lbk -m 55532 -m 555104 https://m.vk.com/video265693995_456240957 > /tmp/test/a
grep -o -i '"VideoPageInfoRow__title">[^<]*' /tmp/test/a > /tmp/test/b
sed -i 's/"VideoPageInfoRow__title">/#EXTINF:-1,/g' /tmp/test/b
grep -o -i '<source src=[^<]*' /tmp/test/a > /tmp/test/a1
sed -i 's#%2F#/#g' /tmp/test/a1 
sed -i 's#%3A#:#g' /tmp/test/a1 
sed -i 's#=# #g' /tmp/test/a1 
sed -i 's#&# #g' /tmp/test/a1 
sed -i 's#?# #g' /tmp/test/a1 
sed -i 's#dirs%5B#!#g' /tmp/test/a1 
sed 's/\([!]\+\)/\n\1/g' /tmp/test/a1 > /tmp/test/a2
awk '{print NR " " $0}' /tmp/test/a2  > /tmp/test/a3
sort -n -r "/tmp/test/a3"|grep -o -i ' [^<]*'  > /tmp/test/y
sed -i 's#%5D#.mp4#g' /tmp/test/y
sed -i '$d' /tmp/test/y
sed -i 's#src "#!240.mp4 #g' /tmp/test/y
cut -d '/' -f -7  /tmp/test/y > /tmp/test/x
sed -i 's#videos#videos/#g' /tmp/test/x
cd /tmp/test
if grep -E "720.mp4" x > /dev/null; then
awk '/720/ {print}' x > x1
elif grep -E "720.mp4" x > /dev/null; then
awk '/720/ {print}' x > x1
elif grep -E "480.mp4" x > /dev/null; then
awk '/480/ {print}' x > x1
elif grep -E "240.mp4" x > /dev/null; then
awk '/240/ {print}' x > x1
fi
sed -n '1,1p' x1 > xx
awk '{print $ 2}' xx > stream
grep -o -i 'amp;tag[^<]*' /tmp/test/a3 |awk '{print $ 2}' >> stream
awk '{print $ 1}' x1|sed -n '1,1p' >> stream
cat stream | tr -d '\n' > adresa
sed -i 's#!#.#g' adresa 
cat /tmp/test/b >> /tmp/music.m3u
cat /tmp/test/adresa >> /tmp/music.m3u
echo "" >> /tmp/music.m3u
#################################################
curl  -k -Lbk -m 55532 -m 555104 https://m.vk.com/video-10577052_456239910 > /tmp/test/a
grep -o -i '"VideoPageInfoRow__title">[^<]*' /tmp/test/a > /tmp/test/b
sed -i 's/"VideoPageInfoRow__title">/#EXTINF:-1,/g' /tmp/test/b
grep -o -i '<source src=[^<]*' /tmp/test/a > /tmp/test/a1
sed -i 's#%2F#/#g' /tmp/test/a1 
sed -i 's#%3A#:#g' /tmp/test/a1 
sed -i 's#=# #g' /tmp/test/a1 
sed -i 's#&# #g' /tmp/test/a1 
sed -i 's#?# #g' /tmp/test/a1 
sed -i 's#dirs%5B#!#g' /tmp/test/a1 
sed 's/\([!]\+\)/\n\1/g' /tmp/test/a1 > /tmp/test/a2
awk '{print NR " " $0}' /tmp/test/a2  > /tmp/test/a3
sort -n -r "/tmp/test/a3"|grep -o -i ' [^<]*'  > /tmp/test/y
sed -i 's#%5D#.mp4#g' /tmp/test/y
sed -i '$d' /tmp/test/y
sed -i 's#src "#!240.mp4 #g' /tmp/test/y
cut -d '/' -f -7  /tmp/test/y > /tmp/test/x
sed -i 's#videos#videos/#g' /tmp/test/x
cd /tmp/test
if grep -E "720.mp4" x > /dev/null; then
awk '/720/ {print}' x > x1
elif grep -E "720.mp4" x > /dev/null; then
awk '/720/ {print}' x > x1
elif grep -E "480.mp4" x > /dev/null; then
awk '/480/ {print}' x > x1
elif grep -E "240.mp4" x > /dev/null; then
awk '/240/ {print}' x > x1
fi
sed -n '1,1p' x1 > xx
awk '{print $ 2}' xx > stream
grep -o -i 'amp;tag[^<]*' /tmp/test/a3 |awk '{print $ 2}' >> stream
awk '{print $ 1}' x1|sed -n '1,1p' >> stream
cat stream | tr -d '\n' > adresa
sed -i 's#!#.#g' adresa 
cat /tmp/test/b >> /tmp/music.m3u
cat /tmp/test/adresa >> /tmp/music.m3u
echo "" >> /tmp/music.m3u
#################################################
curl  -k -Lbk -m 55532 -m 555104 https://m.vk.com/video-98558760_456241354 > /tmp/test/a
grep -o -i '"VideoPageInfoRow__title">[^<]*' /tmp/test/a > /tmp/test/b
sed -i 's/"VideoPageInfoRow__title">/#EXTINF:-1,/g' /tmp/test/b
grep -o -i '<source src=[^<]*' /tmp/test/a > /tmp/test/a1
sed -i 's#%2F#/#g' /tmp/test/a1 
sed -i 's#%3A#:#g' /tmp/test/a1 
sed -i 's#=# #g' /tmp/test/a1 
sed -i 's#&# #g' /tmp/test/a1 
sed -i 's#?# #g' /tmp/test/a1 
sed -i 's#dirs%5B#!#g' /tmp/test/a1 
sed 's/\([!]\+\)/\n\1/g' /tmp/test/a1 > /tmp/test/a2
awk '{print NR " " $0}' /tmp/test/a2  > /tmp/test/a3
sort -n -r "/tmp/test/a3"|grep -o -i ' [^<]*'  > /tmp/test/y
sed -i 's#%5D#.mp4#g' /tmp/test/y
sed -i '$d' /tmp/test/y
sed -i 's#src "#!240.mp4 #g' /tmp/test/y
cut -d '/' -f -7  /tmp/test/y > /tmp/test/x
sed -i 's#videos#videos/#g' /tmp/test/x
cd /tmp/test
if grep -E "720.mp4" x > /dev/null; then
awk '/720/ {print}' x > x1
elif grep -E "720.mp4" x > /dev/null; then
awk '/720/ {print}' x > x1
elif grep -E "480.mp4" x > /dev/null; then
awk '/480/ {print}' x > x1
elif grep -E "240.mp4" x > /dev/null; then
awk '/240/ {print}' x > x1
fi
sed -n '1,1p' x1 > xx
awk '{print $ 2}' xx > stream
grep -o -i 'amp;tag[^<]*' /tmp/test/a3 |awk '{print $ 2}' >> stream
awk '{print $ 1}' x1|sed -n '1,1p' >> stream
cat stream | tr -d '\n' > adresa
sed -i 's#!#.#g' adresa 
cat /tmp/test/b >> /tmp/music.m3u
cat /tmp/test/adresa >> /tmp/music.m3u
echo "" >> /tmp/music.m3u
#################################################
curl  -k -Lbk -m 55532 -m 555104 https://m.vk.com/video-88133688_171771584 > /tmp/test/a
grep -o -i '"VideoPageInfoRow__title">[^<]*' /tmp/test/a > /tmp/test/b
sed -i 's/"VideoPageInfoRow__title">/#EXTINF:-1,/g' /tmp/test/b
grep -o -i '<source src=[^<]*' /tmp/test/a > /tmp/test/a1
sed -i 's#%2F#/#g' /tmp/test/a1 
sed -i 's#%3A#:#g' /tmp/test/a1 
sed -i 's#=# #g' /tmp/test/a1 
sed -i 's#&# #g' /tmp/test/a1 
sed -i 's#?# #g' /tmp/test/a1 
sed -i 's#dirs%5B#!#g' /tmp/test/a1 
sed 's/\([!]\+\)/\n\1/g' /tmp/test/a1 > /tmp/test/a2
awk '{print NR " " $0}' /tmp/test/a2  > /tmp/test/a3
sort -n -r "/tmp/test/a3"|grep -o -i ' [^<]*'  > /tmp/test/y
sed -i 's#%5D#.mp4#g' /tmp/test/y
sed -i '$d' /tmp/test/y
sed -i 's#src "#!240.mp4 #g' /tmp/test/y
cut -d '/' -f -7  /tmp/test/y > /tmp/test/x
sed -i 's#videos#videos/#g' /tmp/test/x
cd /tmp/test
if grep -E "720.mp4" x > /dev/null; then
awk '/720/ {print}' x > x1
elif grep -E "720.mp4" x > /dev/null; then
awk '/720/ {print}' x > x1
elif grep -E "480.mp4" x > /dev/null; then
awk '/480/ {print}' x > x1
elif grep -E "240.mp4" x > /dev/null; then
awk '/240/ {print}' x > x1
fi
sed -n '1,1p' x1 > xx
awk '{print $ 2}' xx > stream
grep -o -i 'amp;tag[^<]*' /tmp/test/a3 |awk '{print $ 2}' >> stream
awk '{print $ 1}' x1|sed -n '1,1p' >> stream
cat stream | tr -d '\n' > adresa
sed -i 's#!#.#g' adresa 
cat /tmp/test/b >> /tmp/music.m3u
cat /tmp/test/adresa >> /tmp/music.m3u
echo "" >> /tmp/music.m3u
#################################################
curl  -k -Lbk -m 55532 -m 555104 https://m.vk.com/video-88133688_456239367 > /tmp/test/a
grep -o -i '"VideoPageInfoRow__title">[^<]*' /tmp/test/a > /tmp/test/b
sed -i 's/"VideoPageInfoRow__title">/#EXTINF:-1,/g' /tmp/test/b
grep -o -i '<source src=[^<]*' /tmp/test/a > /tmp/test/a1
sed -i 's#%2F#/#g' /tmp/test/a1 
sed -i 's#%3A#:#g' /tmp/test/a1 
sed -i 's#=# #g' /tmp/test/a1 
sed -i 's#&# #g' /tmp/test/a1 
sed -i 's#?# #g' /tmp/test/a1 
sed -i 's#dirs%5B#!#g' /tmp/test/a1 
sed 's/\([!]\+\)/\n\1/g' /tmp/test/a1 > /tmp/test/a2
awk '{print NR " " $0}' /tmp/test/a2  > /tmp/test/a3
sort -n -r "/tmp/test/a3"|grep -o -i ' [^<]*'  > /tmp/test/y
sed -i 's#%5D#.mp4#g' /tmp/test/y
sed -i '$d' /tmp/test/y
sed -i 's#src "#!240.mp4 #g' /tmp/test/y
cut -d '/' -f -7  /tmp/test/y > /tmp/test/x
sed -i 's#videos#videos/#g' /tmp/test/x
cd /tmp/test
if grep -E "720.mp4" x > /dev/null; then
awk '/720/ {print}' x > x1
elif grep -E "720.mp4" x > /dev/null; then
awk '/720/ {print}' x > x1
elif grep -E "480.mp4" x > /dev/null; then
awk '/480/ {print}' x > x1
elif grep -E "240.mp4" x > /dev/null; then
awk '/240/ {print}' x > x1
fi
sed -n '1,1p' x1 > xx
awk '{print $ 2}' xx > stream
grep -o -i 'amp;tag[^<]*' /tmp/test/a3 |awk '{print $ 2}' >> stream
awk '{print $ 1}' x1|sed -n '1,1p' >> stream
cat stream | tr -d '\n' > adresa
sed -i 's#!#.#g' adresa 
cat /tmp/test/b >> /tmp/music.m3u
cat /tmp/test/adresa >> /tmp/music.m3u
echo "" >> /tmp/music.m3u
#################################################
curl  -k -Lbk -m 55532 -m 555104 https://m.vk.com/video-77912396_171474649 > /tmp/test/a
grep -o -i '"VideoPageInfoRow__title">[^<]*' /tmp/test/a > /tmp/test/b
sed -i 's/"VideoPageInfoRow__title">/#EXTINF:-1,/g' /tmp/test/b
grep -o -i '<source src=[^<]*' /tmp/test/a > /tmp/test/a1
sed -i 's#%2F#/#g' /tmp/test/a1 
sed -i 's#%3A#:#g' /tmp/test/a1 
sed -i 's#=# #g' /tmp/test/a1 
sed -i 's#&# #g' /tmp/test/a1 
sed -i 's#?# #g' /tmp/test/a1 
sed -i 's#dirs%5B#!#g' /tmp/test/a1 
sed 's/\([!]\+\)/\n\1/g' /tmp/test/a1 > /tmp/test/a2
awk '{print NR " " $0}' /tmp/test/a2  > /tmp/test/a3
sort -n -r "/tmp/test/a3"|grep -o -i ' [^<]*'  > /tmp/test/y
sed -i 's#%5D#.mp4#g' /tmp/test/y
sed -i '$d' /tmp/test/y
sed -i 's#src "#!240.mp4 #g' /tmp/test/y
cut -d '/' -f -7  /tmp/test/y > /tmp/test/x
sed -i 's#videos#videos/#g' /tmp/test/x
cd /tmp/test
if grep -E "720.mp4" x > /dev/null; then
awk '/720/ {print}' x > x1
elif grep -E "720.mp4" x > /dev/null; then
awk '/720/ {print}' x > x1
elif grep -E "480.mp4" x > /dev/null; then
awk '/480/ {print}' x > x1
elif grep -E "240.mp4" x > /dev/null; then
awk '/240/ {print}' x > x1
fi
sed -n '1,1p' x1 > xx
awk '{print $ 2}' xx > stream
grep -o -i 'amp;tag[^<]*' /tmp/test/a3 |awk '{print $ 2}' >> stream
awk '{print $ 1}' x1|sed -n '1,1p' >> stream
cat stream | tr -d '\n' > adresa
sed -i 's#!#.#g' adresa 
cat /tmp/test/b >> /tmp/music.m3u
cat /tmp/test/adresa >> /tmp/music.m3u
echo "" >> /tmp/music.m3u
#################################################
curl  -k -Lbk -m 55532 -m 555104 https://m.vk.com/video135039543_456239295 > /tmp/test/a
grep -o -i '"VideoPageInfoRow__title">[^<]*' /tmp/test/a > /tmp/test/b
sed -i 's/"VideoPageInfoRow__title">/#EXTINF:-1,/g' /tmp/test/b
grep -o -i '<source src=[^<]*' /tmp/test/a > /tmp/test/a1
sed -i 's#%2F#/#g' /tmp/test/a1 
sed -i 's#%3A#:#g' /tmp/test/a1 
sed -i 's#=# #g' /tmp/test/a1 
sed -i 's#&# #g' /tmp/test/a1 
sed -i 's#?# #g' /tmp/test/a1 
sed -i 's#dirs%5B#!#g' /tmp/test/a1 
sed 's/\([!]\+\)/\n\1/g' /tmp/test/a1 > /tmp/test/a2
awk '{print NR " " $0}' /tmp/test/a2  > /tmp/test/a3
sort -n -r "/tmp/test/a3"|grep -o -i ' [^<]*'  > /tmp/test/y
sed -i 's#%5D#.mp4#g' /tmp/test/y
sed -i '$d' /tmp/test/y
sed -i 's#src "#!240.mp4 #g' /tmp/test/y
cut -d '/' -f -7  /tmp/test/y > /tmp/test/x
sed -i 's#videos#videos/#g' /tmp/test/x
cd /tmp/test
if grep -E "720.mp4" x > /dev/null; then
awk '/720/ {print}' x > x1
elif grep -E "720.mp4" x > /dev/null; then
awk '/720/ {print}' x > x1
elif grep -E "480.mp4" x > /dev/null; then
awk '/480/ {print}' x > x1
elif grep -E "240.mp4" x > /dev/null; then
awk '/240/ {print}' x > x1
fi
sed -n '1,1p' x1 > xx
awk '{print $ 2}' xx > stream
grep -o -i 'amp;tag[^<]*' /tmp/test/a3 |awk '{print $ 2}' >> stream
awk '{print $ 1}' x1|sed -n '1,1p' >> stream
cat stream | tr -d '\n' > adresa
sed -i 's#!#.#g' adresa 
cat /tmp/test/b >> /tmp/music.m3u
cat /tmp/test/adresa >> /tmp/music.m3u
echo "" >> /tmp/music.m3u
#################################################
curl  -k -Lbk -m 55532 -m 555104 https://m.vk.com/video-88133688_456239480 > /tmp/test/a
grep -o -i '"VideoPageInfoRow__title">[^<]*' /tmp/test/a > /tmp/test/b
sed -i 's/"VideoPageInfoRow__title">/#EXTINF:-1,/g' /tmp/test/b
grep -o -i '<source src=[^<]*' /tmp/test/a > /tmp/test/a1
sed -i 's#%2F#/#g' /tmp/test/a1 
sed -i 's#%3A#:#g' /tmp/test/a1 
sed -i 's#=# #g' /tmp/test/a1 
sed -i 's#&# #g' /tmp/test/a1 
sed -i 's#?# #g' /tmp/test/a1 
sed -i 's#dirs%5B#!#g' /tmp/test/a1 
sed 's/\([!]\+\)/\n\1/g' /tmp/test/a1 > /tmp/test/a2
awk '{print NR " " $0}' /tmp/test/a2  > /tmp/test/a3
sort -n -r "/tmp/test/a3"|grep -o -i ' [^<]*'  > /tmp/test/y
sed -i 's#%5D#.mp4#g' /tmp/test/y
sed -i '$d' /tmp/test/y
sed -i 's#src "#!240.mp4 #g' /tmp/test/y
cut -d '/' -f -7  /tmp/test/y > /tmp/test/x
sed -i 's#videos#videos/#g' /tmp/test/x
cd /tmp/test
if grep -E "720.mp4" x > /dev/null; then
awk '/720/ {print}' x > x1
elif grep -E "720.mp4" x > /dev/null; then
awk '/720/ {print}' x > x1
elif grep -E "480.mp4" x > /dev/null; then
awk '/480/ {print}' x > x1
elif grep -E "240.mp4" x > /dev/null; then
awk '/240/ {print}' x > x1
fi
sed -n '1,1p' x1 > xx
awk '{print $ 2}' xx > stream
grep -o -i 'amp;tag[^<]*' /tmp/test/a3 |awk '{print $ 2}' >> stream
awk '{print $ 1}' x1|sed -n '1,1p' >> stream
cat stream | tr -d '\n' > adresa
sed -i 's#!#.#g' adresa 
cat /tmp/test/b >> /tmp/music.m3u
cat /tmp/test/adresa >> /tmp/music.m3u
echo "" >> /tmp/music.m3u
#################################################
curl  -k -Lbk -m 55532 -m 555104 https://m.vk.com/video-88133688_456239598 > /tmp/test/a
grep -o -i '"VideoPageInfoRow__title">[^<]*' /tmp/test/a > /tmp/test/b
sed -i 's/"VideoPageInfoRow__title">/#EXTINF:-1,/g' /tmp/test/b
grep -o -i '<source src=[^<]*' /tmp/test/a > /tmp/test/a1
sed -i 's#%2F#/#g' /tmp/test/a1 
sed -i 's#%3A#:#g' /tmp/test/a1 
sed -i 's#=# #g' /tmp/test/a1 
sed -i 's#&# #g' /tmp/test/a1 
sed -i 's#?# #g' /tmp/test/a1 
sed -i 's#dirs%5B#!#g' /tmp/test/a1 
sed 's/\([!]\+\)/\n\1/g' /tmp/test/a1 > /tmp/test/a2
awk '{print NR " " $0}' /tmp/test/a2  > /tmp/test/a3
sort -n -r "/tmp/test/a3"|grep -o -i ' [^<]*'  > /tmp/test/y
sed -i 's#%5D#.mp4#g' /tmp/test/y
sed -i '$d' /tmp/test/y
sed -i 's#src "#!240.mp4 #g' /tmp/test/y
cut -d '/' -f -7  /tmp/test/y > /tmp/test/x
sed -i 's#videos#videos/#g' /tmp/test/x
cd /tmp/test
if grep -E "720.mp4" x > /dev/null; then
awk '/720/ {print}' x > x1
elif grep -E "720.mp4" x > /dev/null; then
awk '/720/ {print}' x > x1
elif grep -E "480.mp4" x > /dev/null; then
awk '/480/ {print}' x > x1
elif grep -E "240.mp4" x > /dev/null; then
awk '/240/ {print}' x > x1
fi
sed -n '1,1p' x1 > xx
awk '{print $ 2}' xx > stream
grep -o -i 'amp;tag[^<]*' /tmp/test/a3 |awk '{print $ 2}' >> stream
awk '{print $ 1}' x1|sed -n '1,1p' >> stream
cat stream | tr -d '\n' > adresa
sed -i 's#!#.#g' adresa 
cat /tmp/test/b >> /tmp/music.m3u
cat /tmp/test/adresa >> /tmp/music.m3u
echo "" >> /tmp/music.m3u
#################################################
curl  -k -Lbk -m 55532 -m 555104 https://m.vk.com/video69931116_456239125 > /tmp/test/a
grep -o -i '"VideoPageInfoRow__title">[^<]*' /tmp/test/a > /tmp/test/b
sed -i 's/"VideoPageInfoRow__title">/#EXTINF:-1,/g' /tmp/test/b
grep -o -i '<source src=[^<]*' /tmp/test/a > /tmp/test/a1
sed -i 's#%2F#/#g' /tmp/test/a1 
sed -i 's#%3A#:#g' /tmp/test/a1 
sed -i 's#=# #g' /tmp/test/a1 
sed -i 's#&# #g' /tmp/test/a1 
sed -i 's#?# #g' /tmp/test/a1 
sed -i 's#dirs%5B#!#g' /tmp/test/a1 
sed 's/\([!]\+\)/\n\1/g' /tmp/test/a1 > /tmp/test/a2
awk '{print NR " " $0}' /tmp/test/a2  > /tmp/test/a3
sort -n -r "/tmp/test/a3"|grep -o -i ' [^<]*'  > /tmp/test/y
sed -i 's#%5D#.mp4#g' /tmp/test/y
sed -i '$d' /tmp/test/y
sed -i 's#src "#!240.mp4 #g' /tmp/test/y
cut -d '/' -f -7  /tmp/test/y > /tmp/test/x
sed -i 's#videos#videos/#g' /tmp/test/x
cd /tmp/test
if grep -E "720.mp4" x > /dev/null; then
awk '/720/ {print}' x > x1
elif grep -E "720.mp4" x > /dev/null; then
awk '/720/ {print}' x > x1
elif grep -E "480.mp4" x > /dev/null; then
awk '/480/ {print}' x > x1
elif grep -E "240.mp4" x > /dev/null; then
awk '/240/ {print}' x > x1
fi
sed -n '1,1p' x1 > xx
awk '{print $ 2}' xx > stream
grep -o -i 'amp;tag[^<]*' /tmp/test/a3 |awk '{print $ 2}' >> stream
awk '{print $ 1}' x1|sed -n '1,1p' >> stream
cat stream | tr -d '\n' > adresa
sed -i 's#!#.#g' adresa 
cat /tmp/test/b >> /tmp/music.m3u
cat /tmp/test/adresa >> /tmp/music.m3u
echo "" >> /tmp/music.m3u
#################################################
curl  -k -Lbk -m 55532 -m 555104 https://m.vk.com/video-88133688_456239421 > /tmp/test/a
grep -o -i '"VideoPageInfoRow__title">[^<]*' /tmp/test/a > /tmp/test/b
sed -i 's/"VideoPageInfoRow__title">/#EXTINF:-1,/g' /tmp/test/b
grep -o -i '<source src=[^<]*' /tmp/test/a > /tmp/test/a1
sed -i 's#%2F#/#g' /tmp/test/a1 
sed -i 's#%3A#:#g' /tmp/test/a1 
sed -i 's#=# #g' /tmp/test/a1 
sed -i 's#&# #g' /tmp/test/a1 
sed -i 's#?# #g' /tmp/test/a1 
sed -i 's#dirs%5B#!#g' /tmp/test/a1 
sed 's/\([!]\+\)/\n\1/g' /tmp/test/a1 > /tmp/test/a2
awk '{print NR " " $0}' /tmp/test/a2  > /tmp/test/a3
sort -n -r "/tmp/test/a3"|grep -o -i ' [^<]*'  > /tmp/test/y
sed -i 's#%5D#.mp4#g' /tmp/test/y
sed -i '$d' /tmp/test/y
sed -i 's#src "#!240.mp4 #g' /tmp/test/y
cut -d '/' -f -7  /tmp/test/y > /tmp/test/x
sed -i 's#videos#videos/#g' /tmp/test/x
cd /tmp/test
if grep -E "720.mp4" x > /dev/null; then
awk '/720/ {print}' x > x1
elif grep -E "720.mp4" x > /dev/null; then
awk '/720/ {print}' x > x1
elif grep -E "480.mp4" x > /dev/null; then
awk '/480/ {print}' x > x1
elif grep -E "240.mp4" x > /dev/null; then
awk '/240/ {print}' x > x1
fi
sed -n '1,1p' x1 > xx
awk '{print $ 2}' xx > stream
grep -o -i 'amp;tag[^<]*' /tmp/test/a3 |awk '{print $ 2}' >> stream
awk '{print $ 1}' x1|sed -n '1,1p' >> stream
cat stream | tr -d '\n' > adresa
sed -i 's#!#.#g' adresa 
cat /tmp/test/b >> /tmp/music.m3u
cat /tmp/test/adresa >> /tmp/music.m3u
echo "" >> /tmp/music.m3u
#################################################
curl  -k -Lbk -m 55532 -m 555104 https://m.vk.com/video329337007_456240063 > /tmp/test/a
grep -o -i '"VideoPageInfoRow__title">[^<]*' /tmp/test/a > /tmp/test/b
sed -i 's/"VideoPageInfoRow__title">/#EXTINF:-1,/g' /tmp/test/b
grep -o -i '<source src=[^<]*' /tmp/test/a > /tmp/test/a1
sed -i 's#%2F#/#g' /tmp/test/a1 
sed -i 's#%3A#:#g' /tmp/test/a1 
sed -i 's#=# #g' /tmp/test/a1 
sed -i 's#&# #g' /tmp/test/a1 
sed -i 's#?# #g' /tmp/test/a1 
sed -i 's#dirs%5B#!#g' /tmp/test/a1 
sed 's/\([!]\+\)/\n\1/g' /tmp/test/a1 > /tmp/test/a2
awk '{print NR " " $0}' /tmp/test/a2  > /tmp/test/a3
sort -n -r "/tmp/test/a3"|grep -o -i ' [^<]*'  > /tmp/test/y
sed -i 's#%5D#.mp4#g' /tmp/test/y
sed -i '$d' /tmp/test/y
sed -i 's#src "#!240.mp4 #g' /tmp/test/y
cut -d '/' -f -7  /tmp/test/y > /tmp/test/x
sed -i 's#videos#videos/#g' /tmp/test/x
cd /tmp/test
if grep -E "720.mp4" x > /dev/null; then
awk '/720/ {print}' x > x1
elif grep -E "720.mp4" x > /dev/null; then
awk '/720/ {print}' x > x1
elif grep -E "480.mp4" x > /dev/null; then
awk '/480/ {print}' x > x1
elif grep -E "240.mp4" x > /dev/null; then
awk '/240/ {print}' x > x1
fi
sed -n '1,1p' x1 > xx
awk '{print $ 2}' xx > stream
grep -o -i 'amp;tag[^<]*' /tmp/test/a3 |awk '{print $ 2}' >> stream
awk '{print $ 1}' x1|sed -n '1,1p' >> stream
cat stream | tr -d '\n' > adresa
sed -i 's#!#.#g' adresa 
cat /tmp/test/b >> /tmp/music.m3u
cat /tmp/test/adresa >> /tmp/music.m3u
echo "" >> /tmp/music.m3u
#################################################
curl  -k -Lbk -m 55532 -m 555104 https://m.vk.com/video-110058424_456240229 > /tmp/test/a
grep -o -i '"VideoPageInfoRow__title">[^<]*' /tmp/test/a > /tmp/test/b
sed -i 's/"VideoPageInfoRow__title">/#EXTINF:-1,/g' /tmp/test/b
grep -o -i '<source src=[^<]*' /tmp/test/a > /tmp/test/a1
sed -i 's#%2F#/#g' /tmp/test/a1 
sed -i 's#%3A#:#g' /tmp/test/a1 
sed -i 's#=# #g' /tmp/test/a1 
sed -i 's#&# #g' /tmp/test/a1 
sed -i 's#?# #g' /tmp/test/a1 
sed -i 's#dirs%5B#!#g' /tmp/test/a1 
sed 's/\([!]\+\)/\n\1/g' /tmp/test/a1 > /tmp/test/a2
awk '{print NR " " $0}' /tmp/test/a2  > /tmp/test/a3
sort -n -r "/tmp/test/a3"|grep -o -i ' [^<]*'  > /tmp/test/y
sed -i 's#%5D#.mp4#g' /tmp/test/y
sed -i '$d' /tmp/test/y
sed -i 's#src "#!240.mp4 #g' /tmp/test/y
cut -d '/' -f -7  /tmp/test/y > /tmp/test/x
sed -i 's#videos#videos/#g' /tmp/test/x
cd /tmp/test
if grep -E "720.mp4" x > /dev/null; then
awk '/720/ {print}' x > x1
elif grep -E "720.mp4" x > /dev/null; then
awk '/720/ {print}' x > x1
elif grep -E "480.mp4" x > /dev/null; then
awk '/480/ {print}' x > x1
elif grep -E "240.mp4" x > /dev/null; then
awk '/240/ {print}' x > x1
fi
sed -n '1,1p' x1 > xx
awk '{print $ 2}' xx > stream
grep -o -i 'amp;tag[^<]*' /tmp/test/a3 |awk '{print $ 2}' >> stream
awk '{print $ 1}' x1|sed -n '1,1p' >> stream
cat stream | tr -d '\n' > adresa
sed -i 's#!#.#g' adresa 
cat /tmp/test/b >> /tmp/music.m3u
cat /tmp/test/adresa >> /tmp/music.m3u
echo "" >> /tmp/music.m3u
#################################################
curl  -k -Lbk -m 55532 -m 555104 https://m.vk.com/video-46439852_456239022 > /tmp/test/a
grep -o -i '"VideoPageInfoRow__title">[^<]*' /tmp/test/a > /tmp/test/b
sed -i 's/"VideoPageInfoRow__title">/#EXTINF:-1,/g' /tmp/test/b
grep -o -i '<source src=[^<]*' /tmp/test/a > /tmp/test/a1
sed -i 's#%2F#/#g' /tmp/test/a1 
sed -i 's#%3A#:#g' /tmp/test/a1 
sed -i 's#=# #g' /tmp/test/a1 
sed -i 's#&# #g' /tmp/test/a1 
sed -i 's#?# #g' /tmp/test/a1 
sed -i 's#dirs%5B#!#g' /tmp/test/a1 
sed 's/\([!]\+\)/\n\1/g' /tmp/test/a1 > /tmp/test/a2
awk '{print NR " " $0}' /tmp/test/a2  > /tmp/test/a3
sort -n -r "/tmp/test/a3"|grep -o -i ' [^<]*'  > /tmp/test/y
sed -i 's#%5D#.mp4#g' /tmp/test/y
sed -i '$d' /tmp/test/y
sed -i 's#src "#!240.mp4 #g' /tmp/test/y
cut -d '/' -f -7  /tmp/test/y > /tmp/test/x
sed -i 's#videos#videos/#g' /tmp/test/x
cd /tmp/test
if grep -E "720.mp4" x > /dev/null; then
awk '/720/ {print}' x > x1
elif grep -E "720.mp4" x > /dev/null; then
awk '/720/ {print}' x > x1
elif grep -E "480.mp4" x > /dev/null; then
awk '/480/ {print}' x > x1
elif grep -E "240.mp4" x > /dev/null; then
awk '/240/ {print}' x > x1
fi
sed -n '1,1p' x1 > xx
awk '{print $ 2}' xx > stream
grep -o -i 'amp;tag[^<]*' /tmp/test/a3 |awk '{print $ 2}' >> stream
awk '{print $ 1}' x1|sed -n '1,1p' >> stream
cat stream | tr -d '\n' > adresa
sed -i 's#!#.#g' adresa 
cat /tmp/test/b >> /tmp/music.m3u
cat /tmp/test/adresa >> /tmp/music.m3u
echo "" >> /tmp/music.m3u
#################################################
curl  -k -Lbk -m 55532 -m 555104 https://m.vk.com/video21815640_456249660 > /tmp/test/a
grep -o -i '"VideoPageInfoRow__title">[^<]*' /tmp/test/a > /tmp/test/b
sed -i 's/"VideoPageInfoRow__title">/#EXTINF:-1,/g' /tmp/test/b
grep -o -i '<source src=[^<]*' /tmp/test/a > /tmp/test/a1
sed -i 's#%2F#/#g' /tmp/test/a1 
sed -i 's#%3A#:#g' /tmp/test/a1 
sed -i 's#=# #g' /tmp/test/a1 
sed -i 's#&# #g' /tmp/test/a1 
sed -i 's#?# #g' /tmp/test/a1 
sed -i 's#dirs%5B#!#g' /tmp/test/a1 
sed 's/\([!]\+\)/\n\1/g' /tmp/test/a1 > /tmp/test/a2
awk '{print NR " " $0}' /tmp/test/a2  > /tmp/test/a3
sort -n -r "/tmp/test/a3"|grep -o -i ' [^<]*'  > /tmp/test/y
sed -i 's#%5D#.mp4#g' /tmp/test/y
sed -i '$d' /tmp/test/y
sed -i 's#src "#!240.mp4 #g' /tmp/test/y
cut -d '/' -f -7  /tmp/test/y > /tmp/test/x
sed -i 's#videos#videos/#g' /tmp/test/x
cd /tmp/test
if grep -E "720.mp4" x > /dev/null; then
awk '/720/ {print}' x > x1
elif grep -E "720.mp4" x > /dev/null; then
awk '/720/ {print}' x > x1
elif grep -E "480.mp4" x > /dev/null; then
awk '/480/ {print}' x > x1
elif grep -E "240.mp4" x > /dev/null; then
awk '/240/ {print}' x > x1
fi
sed -n '1,1p' x1 > xx
awk '{print $ 2}' xx > stream
grep -o -i 'amp;tag[^<]*' /tmp/test/a3 |awk '{print $ 2}' >> stream
awk '{print $ 1}' x1|sed -n '1,1p' >> stream
cat stream | tr -d '\n' > adresa
sed -i 's#!#.#g' adresa 
cat /tmp/test/b >> /tmp/music.m3u
cat /tmp/test/adresa >> /tmp/music.m3u
echo "" >> /tmp/music.m3u
#################################################
curl  -k -Lbk -m 55532 -m 555104 https://m.vk.com/video23615574_456239280 > /tmp/test/a
grep -o -i '"VideoPageInfoRow__title">[^<]*' /tmp/test/a > /tmp/test/b
sed -i 's/"VideoPageInfoRow__title">/#EXTINF:-1,/g' /tmp/test/b
grep -o -i '<source src=[^<]*' /tmp/test/a > /tmp/test/a1
sed -i 's#%2F#/#g' /tmp/test/a1 
sed -i 's#%3A#:#g' /tmp/test/a1 
sed -i 's#=# #g' /tmp/test/a1 
sed -i 's#&# #g' /tmp/test/a1 
sed -i 's#?# #g' /tmp/test/a1 
sed -i 's#dirs%5B#!#g' /tmp/test/a1 
sed 's/\([!]\+\)/\n\1/g' /tmp/test/a1 > /tmp/test/a2
awk '{print NR " " $0}' /tmp/test/a2  > /tmp/test/a3
sort -n -r "/tmp/test/a3"|grep -o -i ' [^<]*'  > /tmp/test/y
sed -i 's#%5D#.mp4#g' /tmp/test/y
sed -i '$d' /tmp/test/y
sed -i 's#src "#!240.mp4 #g' /tmp/test/y
cut -d '/' -f -7  /tmp/test/y > /tmp/test/x
sed -i 's#videos#videos/#g' /tmp/test/x
cd /tmp/test
if grep -E "720.mp4" x > /dev/null; then
awk '/720/ {print}' x > x1
elif grep -E "720.mp4" x > /dev/null; then
awk '/720/ {print}' x > x1
elif grep -E "480.mp4" x > /dev/null; then
awk '/480/ {print}' x > x1
elif grep -E "240.mp4" x > /dev/null; then
awk '/240/ {print}' x > x1
fi
sed -n '1,1p' x1 > xx
awk '{print $ 2}' xx > stream
grep -o -i 'amp;tag[^<]*' /tmp/test/a3 |awk '{print $ 2}' >> stream
awk '{print $ 1}' x1|sed -n '1,1p' >> stream
cat stream | tr -d '\n' > adresa
sed -i 's#!#.#g' adresa 
cat /tmp/test/b >> /tmp/music.m3u
cat /tmp/test/adresa >> /tmp/music.m3u
echo "" >> /tmp/music.m3u
#################################################
curl  -k -Lbk -m 55532 -m 555104 https://m.vk.com/video-6890_456239125 > /tmp/test/a
grep -o -i '"VideoPageInfoRow__title">[^<]*' /tmp/test/a > /tmp/test/b
sed -i 's/"VideoPageInfoRow__title">/#EXTINF:-1,/g' /tmp/test/b
grep -o -i '<source src=[^<]*' /tmp/test/a > /tmp/test/a1
sed -i 's#%2F#/#g' /tmp/test/a1 
sed -i 's#%3A#:#g' /tmp/test/a1 
sed -i 's#=# #g' /tmp/test/a1 
sed -i 's#&# #g' /tmp/test/a1 
sed -i 's#?# #g' /tmp/test/a1 
sed -i 's#dirs%5B#!#g' /tmp/test/a1 
sed 's/\([!]\+\)/\n\1/g' /tmp/test/a1 > /tmp/test/a2
awk '{print NR " " $0}' /tmp/test/a2  > /tmp/test/a3
sort -n -r "/tmp/test/a3"|grep -o -i ' [^<]*'  > /tmp/test/y
sed -i 's#%5D#.mp4#g' /tmp/test/y
sed -i '$d' /tmp/test/y
sed -i 's#src "#!240.mp4 #g' /tmp/test/y
cut -d '/' -f -7  /tmp/test/y > /tmp/test/x
sed -i 's#videos#videos/#g' /tmp/test/x
cd /tmp/test
if grep -E "720.mp4" x > /dev/null; then
awk '/720/ {print}' x > x1
elif grep -E "720.mp4" x > /dev/null; then
awk '/720/ {print}' x > x1
elif grep -E "480.mp4" x > /dev/null; then
awk '/480/ {print}' x > x1
elif grep -E "240.mp4" x > /dev/null; then
awk '/240/ {print}' x > x1
fi
sed -n '1,1p' x1 > xx
awk '{print $ 2}' xx > stream
grep -o -i 'amp;tag[^<]*' /tmp/test/a3 |awk '{print $ 2}' >> stream
awk '{print $ 1}' x1|sed -n '1,1p' >> stream
cat stream | tr -d '\n' > adresa
sed -i 's#!#.#g' adresa 
cat /tmp/test/b >> /tmp/music.m3u
cat /tmp/test/adresa >> /tmp/music.m3u
echo "" >> /tmp/music.m3u
#################################################
curl  -k -Lbk -m 55532 -m 555104 https://m.vk.com/video-154792724_456239080 > /tmp/test/a
grep -o -i '"VideoPageInfoRow__title">[^<]*' /tmp/test/a > /tmp/test/b
sed -i 's/"VideoPageInfoRow__title">/#EXTINF:-1,/g' /tmp/test/b
grep -o -i '<source src=[^<]*' /tmp/test/a > /tmp/test/a1
sed -i 's#%2F#/#g' /tmp/test/a1 
sed -i 's#%3A#:#g' /tmp/test/a1 
sed -i 's#=# #g' /tmp/test/a1 
sed -i 's#&# #g' /tmp/test/a1 
sed -i 's#?# #g' /tmp/test/a1 
sed -i 's#dirs%5B#!#g' /tmp/test/a1 
sed 's/\([!]\+\)/\n\1/g' /tmp/test/a1 > /tmp/test/a2
awk '{print NR " " $0}' /tmp/test/a2  > /tmp/test/a3
sort -n -r "/tmp/test/a3"|grep -o -i ' [^<]*'  > /tmp/test/y
sed -i 's#%5D#.mp4#g' /tmp/test/y
sed -i '$d' /tmp/test/y
sed -i 's#src "#!240.mp4 #g' /tmp/test/y
cut -d '/' -f -7  /tmp/test/y > /tmp/test/x
sed -i 's#videos#videos/#g' /tmp/test/x
cd /tmp/test
if grep -E "720.mp4" x > /dev/null; then
awk '/720/ {print}' x > x1
elif grep -E "720.mp4" x > /dev/null; then
awk '/720/ {print}' x > x1
elif grep -E "480.mp4" x > /dev/null; then
awk '/480/ {print}' x > x1
elif grep -E "240.mp4" x > /dev/null; then
awk '/240/ {print}' x > x1
fi
sed -n '1,1p' x1 > xx
awk '{print $ 2}' xx > stream
grep -o -i 'amp;tag[^<]*' /tmp/test/a3 |awk '{print $ 2}' >> stream
awk '{print $ 1}' x1|sed -n '1,1p' >> stream
cat stream | tr -d '\n' > adresa
sed -i 's#!#.#g' adresa 
cat /tmp/test/b >> /tmp/music.m3u
cat /tmp/test/adresa >> /tmp/music.m3u
echo "" >> /tmp/music.m3u
#################################################
curl  -k -Lbk -m 55532 -m 555104 https://m.vk.com/video182444048_456239166 > /tmp/test/a
grep -o -i '"VideoPageInfoRow__title">[^<]*' /tmp/test/a > /tmp/test/b
sed -i 's/"VideoPageInfoRow__title">/#EXTINF:-1,/g' /tmp/test/b
grep -o -i '<source src=[^<]*' /tmp/test/a > /tmp/test/a1
sed -i 's#%2F#/#g' /tmp/test/a1 
sed -i 's#%3A#:#g' /tmp/test/a1 
sed -i 's#=# #g' /tmp/test/a1 
sed -i 's#&# #g' /tmp/test/a1 
sed -i 's#?# #g' /tmp/test/a1 
sed -i 's#dirs%5B#!#g' /tmp/test/a1 
sed 's/\([!]\+\)/\n\1/g' /tmp/test/a1 > /tmp/test/a2
awk '{print NR " " $0}' /tmp/test/a2  > /tmp/test/a3
sort -n -r "/tmp/test/a3"|grep -o -i ' [^<]*'  > /tmp/test/y
sed -i 's#%5D#.mp4#g' /tmp/test/y
sed -i '$d' /tmp/test/y
sed -i 's#src "#!240.mp4 #g' /tmp/test/y
cut -d '/' -f -7  /tmp/test/y > /tmp/test/x
sed -i 's#videos#videos/#g' /tmp/test/x
cd /tmp/test
if grep -E "720.mp4" x > /dev/null; then
awk '/720/ {print}' x > x1
elif grep -E "720.mp4" x > /dev/null; then
awk '/720/ {print}' x > x1
elif grep -E "480.mp4" x > /dev/null; then
awk '/480/ {print}' x > x1
elif grep -E "240.mp4" x > /dev/null; then
awk '/240/ {print}' x > x1
fi
sed -n '1,1p' x1 > xx
awk '{print $ 2}' xx > stream
grep -o -i 'amp;tag[^<]*' /tmp/test/a3 |awk '{print $ 2}' >> stream
awk '{print $ 1}' x1|sed -n '1,1p' >> stream
cat stream | tr -d '\n' > adresa
sed -i 's#!#.#g' adresa 
cat /tmp/test/b >> /tmp/music.m3u
cat /tmp/test/adresa >> /tmp/music.m3u
echo "" >> /tmp/music.m3u
#################################################
curl  -k -Lbk -m 55532 -m 555104 https://m.vk.com/video-124346381_456241193 > /tmp/test/a
grep -o -i '"VideoPageInfoRow__title">[^<]*' /tmp/test/a > /tmp/test/b
sed -i 's/"VideoPageInfoRow__title">/#EXTINF:-1,/g' /tmp/test/b
grep -o -i '<source src=[^<]*' /tmp/test/a > /tmp/test/a1
sed -i 's#%2F#/#g' /tmp/test/a1 
sed -i 's#%3A#:#g' /tmp/test/a1 
sed -i 's#=# #g' /tmp/test/a1 
sed -i 's#&# #g' /tmp/test/a1 
sed -i 's#?# #g' /tmp/test/a1 
sed -i 's#dirs%5B#!#g' /tmp/test/a1 
sed 's/\([!]\+\)/\n\1/g' /tmp/test/a1 > /tmp/test/a2
awk '{print NR " " $0}' /tmp/test/a2  > /tmp/test/a3
sort -n -r "/tmp/test/a3"|grep -o -i ' [^<]*'  > /tmp/test/y
sed -i 's#%5D#.mp4#g' /tmp/test/y
sed -i '$d' /tmp/test/y
sed -i 's#src "#!240.mp4 #g' /tmp/test/y
cut -d '/' -f -7  /tmp/test/y > /tmp/test/x
sed -i 's#videos#videos/#g' /tmp/test/x
cd /tmp/test
if grep -E "720.mp4" x > /dev/null; then
awk '/720/ {print}' x > x1
elif grep -E "720.mp4" x > /dev/null; then
awk '/720/ {print}' x > x1
elif grep -E "480.mp4" x > /dev/null; then
awk '/480/ {print}' x > x1
elif grep -E "240.mp4" x > /dev/null; then
awk '/240/ {print}' x > x1
fi
sed -n '1,1p' x1 > xx
awk '{print $ 2}' xx > stream
grep -o -i 'amp;tag[^<]*' /tmp/test/a3 |awk '{print $ 2}' >> stream
awk '{print $ 1}' x1|sed -n '1,1p' >> stream
cat stream | tr -d '\n' > adresa
sed -i 's#!#.#g' adresa 
cat /tmp/test/b >> /tmp/music.m3u
cat /tmp/test/adresa >> /tmp/music.m3u
echo "" >> /tmp/music.m3u
#################################################
curl  -k -Lbk -m 55532 -m 555104 https://m.vk.com/video214185242_170908031 > /tmp/test/a
grep -o -i '"VideoPageInfoRow__title">[^<]*' /tmp/test/a > /tmp/test/b
sed -i 's/"VideoPageInfoRow__title">/#EXTINF:-1,/g' /tmp/test/b
grep -o -i '<source src=[^<]*' /tmp/test/a > /tmp/test/a1
sed -i 's#%2F#/#g' /tmp/test/a1 
sed -i 's#%3A#:#g' /tmp/test/a1 
sed -i 's#=# #g' /tmp/test/a1 
sed -i 's#&# #g' /tmp/test/a1 
sed -i 's#?# #g' /tmp/test/a1 
sed -i 's#dirs%5B#!#g' /tmp/test/a1 
sed 's/\([!]\+\)/\n\1/g' /tmp/test/a1 > /tmp/test/a2
awk '{print NR " " $0}' /tmp/test/a2  > /tmp/test/a3
sort -n -r "/tmp/test/a3"|grep -o -i ' [^<]*'  > /tmp/test/y
sed -i 's#%5D#.mp4#g' /tmp/test/y
sed -i '$d' /tmp/test/y
sed -i 's#src "#!240.mp4 #g' /tmp/test/y
cut -d '/' -f -7  /tmp/test/y > /tmp/test/x
sed -i 's#videos#videos/#g' /tmp/test/x
cd /tmp/test
if grep -E "720.mp4" x > /dev/null; then
awk '/720/ {print}' x > x1
elif grep -E "720.mp4" x > /dev/null; then
awk '/720/ {print}' x > x1
elif grep -E "480.mp4" x > /dev/null; then
awk '/480/ {print}' x > x1
elif grep -E "240.mp4" x > /dev/null; then
awk '/240/ {print}' x > x1
fi
sed -n '1,1p' x1 > xx
awk '{print $ 2}' xx > stream
grep -o -i 'amp;tag[^<]*' /tmp/test/a3 |awk '{print $ 2}' >> stream
awk '{print $ 1}' x1|sed -n '1,1p' >> stream
cat stream | tr -d '\n' > adresa
sed -i 's#!#.#g' adresa 
cat /tmp/test/b >> /tmp/music.m3u
cat /tmp/test/adresa >> /tmp/music.m3u
echo "" >> /tmp/music.m3u
#################################################
curl  -k -Lbk -m 55532 -m 555104 https://m.vk.com/video-88133688_171553493 > /tmp/test/a
grep -o -i '"VideoPageInfoRow__title">[^<]*' /tmp/test/a > /tmp/test/b
sed -i 's/"VideoPageInfoRow__title">/#EXTINF:-1,/g' /tmp/test/b
grep -o -i '<source src=[^<]*' /tmp/test/a > /tmp/test/a1
sed -i 's#%2F#/#g' /tmp/test/a1 
sed -i 's#%3A#:#g' /tmp/test/a1 
sed -i 's#=# #g' /tmp/test/a1 
sed -i 's#&# #g' /tmp/test/a1 
sed -i 's#?# #g' /tmp/test/a1 
sed -i 's#dirs%5B#!#g' /tmp/test/a1 
sed 's/\([!]\+\)/\n\1/g' /tmp/test/a1 > /tmp/test/a2
awk '{print NR " " $0}' /tmp/test/a2  > /tmp/test/a3
sort -n -r "/tmp/test/a3"|grep -o -i ' [^<]*'  > /tmp/test/y
sed -i 's#%5D#.mp4#g' /tmp/test/y
sed -i '$d' /tmp/test/y
sed -i 's#src "#!240.mp4 #g' /tmp/test/y
cut -d '/' -f -7  /tmp/test/y > /tmp/test/x
sed -i 's#videos#videos/#g' /tmp/test/x
cd /tmp/test
if grep -E "720.mp4" x > /dev/null; then
awk '/720/ {print}' x > x1
elif grep -E "720.mp4" x > /dev/null; then
awk '/720/ {print}' x > x1
elif grep -E "480.mp4" x > /dev/null; then
awk '/480/ {print}' x > x1
elif grep -E "240.mp4" x > /dev/null; then
awk '/240/ {print}' x > x1
fi
sed -n '1,1p' x1 > xx
awk '{print $ 2}' xx > stream
grep -o -i 'amp;tag[^<]*' /tmp/test/a3 |awk '{print $ 2}' >> stream
awk '{print $ 1}' x1|sed -n '1,1p' >> stream
cat stream | tr -d '\n' > adresa
sed -i 's#!#.#g' adresa 
cat /tmp/test/b >> /tmp/music.m3u
cat /tmp/test/adresa >> /tmp/music.m3u
echo "" >> /tmp/music.m3u
#################################################
curl  -k -Lbk -m 55532 -m 555104 https://m.vk.com/video209477801_456239120 > /tmp/test/a
grep -o -i '"VideoPageInfoRow__title">[^<]*' /tmp/test/a > /tmp/test/b
sed -i 's/"VideoPageInfoRow__title">/#EXTINF:-1,/g' /tmp/test/b
grep -o -i '<source src=[^<]*' /tmp/test/a > /tmp/test/a1
sed -i 's#%2F#/#g' /tmp/test/a1 
sed -i 's#%3A#:#g' /tmp/test/a1 
sed -i 's#=# #g' /tmp/test/a1 
sed -i 's#&# #g' /tmp/test/a1 
sed -i 's#?# #g' /tmp/test/a1 
sed -i 's#dirs%5B#!#g' /tmp/test/a1 
sed 's/\([!]\+\)/\n\1/g' /tmp/test/a1 > /tmp/test/a2
awk '{print NR " " $0}' /tmp/test/a2  > /tmp/test/a3
sort -n -r "/tmp/test/a3"|grep -o -i ' [^<]*'  > /tmp/test/y
sed -i 's#%5D#.mp4#g' /tmp/test/y
sed -i '$d' /tmp/test/y
sed -i 's#src "#!240.mp4 #g' /tmp/test/y
cut -d '/' -f -7  /tmp/test/y > /tmp/test/x
sed -i 's#videos#videos/#g' /tmp/test/x
cd /tmp/test
if grep -E "720.mp4" x > /dev/null; then
awk '/720/ {print}' x > x1
elif grep -E "720.mp4" x > /dev/null; then
awk '/720/ {print}' x > x1
elif grep -E "480.mp4" x > /dev/null; then
awk '/480/ {print}' x > x1
elif grep -E "240.mp4" x > /dev/null; then
awk '/240/ {print}' x > x1
fi
sed -n '1,1p' x1 > xx
awk '{print $ 2}' xx > stream
grep -o -i 'amp;tag[^<]*' /tmp/test/a3 |awk '{print $ 2}' >> stream
awk '{print $ 1}' x1|sed -n '1,1p' >> stream
cat stream | tr -d '\n' > adresa
sed -i 's#!#.#g' adresa 
cat /tmp/test/b >> /tmp/music.m3u
cat /tmp/test/adresa >> /tmp/music.m3u
echo "" >> /tmp/music.m3u
#################################################
curl  -k -Lbk -m 55532 -m 555104 https://m.vk.com/video-48714381_456239782 > /tmp/test/a
grep -o -i '"VideoPageInfoRow__title">[^<]*' /tmp/test/a > /tmp/test/b
sed -i 's/"VideoPageInfoRow__title">/#EXTINF:-1,/g' /tmp/test/b
grep -o -i '<source src=[^<]*' /tmp/test/a > /tmp/test/a1
sed -i 's#%2F#/#g' /tmp/test/a1 
sed -i 's#%3A#:#g' /tmp/test/a1 
sed -i 's#=# #g' /tmp/test/a1 
sed -i 's#&# #g' /tmp/test/a1 
sed -i 's#?# #g' /tmp/test/a1 
sed -i 's#dirs%5B#!#g' /tmp/test/a1 
sed 's/\([!]\+\)/\n\1/g' /tmp/test/a1 > /tmp/test/a2
awk '{print NR " " $0}' /tmp/test/a2  > /tmp/test/a3
sort -n -r "/tmp/test/a3"|grep -o -i ' [^<]*'  > /tmp/test/y
sed -i 's#%5D#.mp4#g' /tmp/test/y
sed -i '$d' /tmp/test/y
sed -i 's#src "#!240.mp4 #g' /tmp/test/y
cut -d '/' -f -7  /tmp/test/y > /tmp/test/x
sed -i 's#videos#videos/#g' /tmp/test/x
cd /tmp/test
if grep -E "720.mp4" x > /dev/null; then
awk '/720/ {print}' x > x1
elif grep -E "720.mp4" x > /dev/null; then
awk '/720/ {print}' x > x1
elif grep -E "480.mp4" x > /dev/null; then
awk '/480/ {print}' x > x1
elif grep -E "240.mp4" x > /dev/null; then
awk '/240/ {print}' x > x1
fi
sed -n '1,1p' x1 > xx
awk '{print $ 2}' xx > stream
grep -o -i 'amp;tag[^<]*' /tmp/test/a3 |awk '{print $ 2}' >> stream
awk '{print $ 1}' x1|sed -n '1,1p' >> stream
cat stream | tr -d '\n' > adresa
sed -i 's#!#.#g' adresa 
cat /tmp/test/b >> /tmp/music.m3u
cat /tmp/test/adresa >> /tmp/music.m3u
echo "" >> /tmp/music.m3u
#################################################
curl  -k -Lbk -m 55532 -m 555104 https://m.vk.com/video12801966_456241618 > /tmp/test/a
grep -o -i '"VideoPageInfoRow__title">[^<]*' /tmp/test/a > /tmp/test/b
sed -i 's/"VideoPageInfoRow__title">/#EXTINF:-1,/g' /tmp/test/b
grep -o -i '<source src=[^<]*' /tmp/test/a > /tmp/test/a1
sed -i 's#%2F#/#g' /tmp/test/a1 
sed -i 's#%3A#:#g' /tmp/test/a1 
sed -i 's#=# #g' /tmp/test/a1 
sed -i 's#&# #g' /tmp/test/a1 
sed -i 's#?# #g' /tmp/test/a1 
sed -i 's#dirs%5B#!#g' /tmp/test/a1 
sed 's/\([!]\+\)/\n\1/g' /tmp/test/a1 > /tmp/test/a2
awk '{print NR " " $0}' /tmp/test/a2  > /tmp/test/a3
sort -n -r "/tmp/test/a3"|grep -o -i ' [^<]*'  > /tmp/test/y
sed -i 's#%5D#.mp4#g' /tmp/test/y
sed -i '$d' /tmp/test/y
sed -i 's#src "#!240.mp4 #g' /tmp/test/y
cut -d '/' -f -7  /tmp/test/y > /tmp/test/x
sed -i 's#videos#videos/#g' /tmp/test/x
cd /tmp/test
if grep -E "720.mp4" x > /dev/null; then
awk '/720/ {print}' x > x1
elif grep -E "720.mp4" x > /dev/null; then
awk '/720/ {print}' x > x1
elif grep -E "480.mp4" x > /dev/null; then
awk '/480/ {print}' x > x1
elif grep -E "240.mp4" x > /dev/null; then
awk '/240/ {print}' x > x1
fi
sed -n '1,1p' x1 > xx
awk '{print $ 2}' xx > stream
grep -o -i 'amp;tag[^<]*' /tmp/test/a3 |awk '{print $ 2}' >> stream
awk '{print $ 1}' x1|sed -n '1,1p' >> stream
cat stream | tr -d '\n' > adresa
sed -i 's#!#.#g' adresa 
cat /tmp/test/b >> /tmp/music.m3u
cat /tmp/test/adresa >> /tmp/music.m3u
echo "" >> /tmp/music.m3u
#################################################
curl  -k -Lbk -m 55532 -m 555104 https://m.vk.com/video230502772_456239399 > /tmp/test/a
grep -o -i '"VideoPageInfoRow__title">[^<]*' /tmp/test/a > /tmp/test/b
sed -i 's/"VideoPageInfoRow__title">/#EXTINF:-1,/g' /tmp/test/b
grep -o -i '<source src=[^<]*' /tmp/test/a > /tmp/test/a1
sed -i 's#%2F#/#g' /tmp/test/a1 
sed -i 's#%3A#:#g' /tmp/test/a1 
sed -i 's#=# #g' /tmp/test/a1 
sed -i 's#&# #g' /tmp/test/a1 
sed -i 's#?# #g' /tmp/test/a1 
sed -i 's#dirs%5B#!#g' /tmp/test/a1 
sed 's/\([!]\+\)/\n\1/g' /tmp/test/a1 > /tmp/test/a2
awk '{print NR " " $0}' /tmp/test/a2  > /tmp/test/a3
sort -n -r "/tmp/test/a3"|grep -o -i ' [^<]*'  > /tmp/test/y
sed -i 's#%5D#.mp4#g' /tmp/test/y
sed -i '$d' /tmp/test/y
sed -i 's#src "#!240.mp4 #g' /tmp/test/y
cut -d '/' -f -7  /tmp/test/y > /tmp/test/x
sed -i 's#videos#videos/#g' /tmp/test/x
cd /tmp/test
if grep -E "720.mp4" x > /dev/null; then
awk '/720/ {print}' x > x1
elif grep -E "720.mp4" x > /dev/null; then
awk '/720/ {print}' x > x1
elif grep -E "480.mp4" x > /dev/null; then
awk '/480/ {print}' x > x1
elif grep -E "240.mp4" x > /dev/null; then
awk '/240/ {print}' x > x1
fi
sed -n '1,1p' x1 > xx
awk '{print $ 2}' xx > stream
grep -o -i 'amp;tag[^<]*' /tmp/test/a3 |awk '{print $ 2}' >> stream
awk '{print $ 1}' x1|sed -n '1,1p' >> stream
cat stream | tr -d '\n' > adresa
sed -i 's#!#.#g' adresa 
cat /tmp/test/b >> /tmp/music.m3u
cat /tmp/test/adresa >> /tmp/music.m3u
echo "" >> /tmp/music.m3u
#################################################
curl  -k -Lbk -m 55532 -m 555104 https://m.vk.com/video17035552_456239720 > /tmp/test/a
grep -o -i '"VideoPageInfoRow__title">[^<]*' /tmp/test/a > /tmp/test/b
sed -i 's/"VideoPageInfoRow__title">/#EXTINF:-1,/g' /tmp/test/b
grep -o -i '<source src=[^<]*' /tmp/test/a > /tmp/test/a1
sed -i 's#%2F#/#g' /tmp/test/a1 
sed -i 's#%3A#:#g' /tmp/test/a1 
sed -i 's#=# #g' /tmp/test/a1 
sed -i 's#&# #g' /tmp/test/a1 
sed -i 's#?# #g' /tmp/test/a1 
sed -i 's#dirs%5B#!#g' /tmp/test/a1 
sed 's/\([!]\+\)/\n\1/g' /tmp/test/a1 > /tmp/test/a2
awk '{print NR " " $0}' /tmp/test/a2  > /tmp/test/a3
sort -n -r "/tmp/test/a3"|grep -o -i ' [^<]*'  > /tmp/test/y
sed -i 's#%5D#.mp4#g' /tmp/test/y
sed -i '$d' /tmp/test/y
sed -i 's#src "#!240.mp4 #g' /tmp/test/y
cut -d '/' -f -7  /tmp/test/y > /tmp/test/x
sed -i 's#videos#videos/#g' /tmp/test/x
cd /tmp/test
if grep -E "720.mp4" x > /dev/null; then
awk '/720/ {print}' x > x1
elif grep -E "720.mp4" x > /dev/null; then
awk '/720/ {print}' x > x1
elif grep -E "480.mp4" x > /dev/null; then
awk '/480/ {print}' x > x1
elif grep -E "240.mp4" x > /dev/null; then
awk '/240/ {print}' x > x1
fi
sed -n '1,1p' x1 > xx
awk '{print $ 2}' xx > stream
grep -o -i 'amp;tag[^<]*' /tmp/test/a3 |awk '{print $ 2}' >> stream
awk '{print $ 1}' x1|sed -n '1,1p' >> stream
cat stream | tr -d '\n' > adresa
sed -i 's#!#.#g' adresa 
cat /tmp/test/b >> /tmp/music.m3u
cat /tmp/test/adresa >> /tmp/music.m3u
echo "" >> /tmp/music.m3u
#################################################
curl  -k -Lbk -m 55532 -m 555104 https://m.vk.com/video216250843_456245185 > /tmp/test/a
grep -o -i '"VideoPageInfoRow__title">[^<]*' /tmp/test/a > /tmp/test/b
sed -i 's/"VideoPageInfoRow__title">/#EXTINF:-1,/g' /tmp/test/b
grep -o -i '<source src=[^<]*' /tmp/test/a > /tmp/test/a1
sed -i 's#%2F#/#g' /tmp/test/a1 
sed -i 's#%3A#:#g' /tmp/test/a1 
sed -i 's#=# #g' /tmp/test/a1 
sed -i 's#&# #g' /tmp/test/a1 
sed -i 's#?# #g' /tmp/test/a1 
sed -i 's#dirs%5B#!#g' /tmp/test/a1 
sed 's/\([!]\+\)/\n\1/g' /tmp/test/a1 > /tmp/test/a2
awk '{print NR " " $0}' /tmp/test/a2  > /tmp/test/a3
sort -n -r "/tmp/test/a3"|grep -o -i ' [^<]*'  > /tmp/test/y
sed -i 's#%5D#.mp4#g' /tmp/test/y
sed -i '$d' /tmp/test/y
sed -i 's#src "#!240.mp4 #g' /tmp/test/y
cut -d '/' -f -7  /tmp/test/y > /tmp/test/x
sed -i 's#videos#videos/#g' /tmp/test/x
cd /tmp/test
if grep -E "720.mp4" x > /dev/null; then
awk '/720/ {print}' x > x1
elif grep -E "720.mp4" x > /dev/null; then
awk '/720/ {print}' x > x1
elif grep -E "480.mp4" x > /dev/null; then
awk '/480/ {print}' x > x1
elif grep -E "240.mp4" x > /dev/null; then
awk '/240/ {print}' x > x1
fi
sed -n '1,1p' x1 > xx
awk '{print $ 2}' xx > stream
grep -o -i 'amp;tag[^<]*' /tmp/test/a3 |awk '{print $ 2}' >> stream
awk '{print $ 1}' x1|sed -n '1,1p' >> stream
cat stream | tr -d '\n' > adresa
sed -i 's#!#.#g' adresa 
cat /tmp/test/b >> /tmp/music.m3u
cat /tmp/test/adresa >> /tmp/music.m3u
echo "" >> /tmp/music.m3u
#################################################
curl  -k -Lbk -m 55532 -m 555104 https://m.vk.com/video3651750_456239497 > /tmp/test/a
grep -o -i '"VideoPageInfoRow__title">[^<]*' /tmp/test/a > /tmp/test/b
sed -i 's/"VideoPageInfoRow__title">/#EXTINF:-1,/g' /tmp/test/b
grep -o -i '<source src=[^<]*' /tmp/test/a > /tmp/test/a1
sed -i 's#%2F#/#g' /tmp/test/a1 
sed -i 's#%3A#:#g' /tmp/test/a1 
sed -i 's#=# #g' /tmp/test/a1 
sed -i 's#&# #g' /tmp/test/a1 
sed -i 's#?# #g' /tmp/test/a1 
sed -i 's#dirs%5B#!#g' /tmp/test/a1 
sed 's/\([!]\+\)/\n\1/g' /tmp/test/a1 > /tmp/test/a2
awk '{print NR " " $0}' /tmp/test/a2  > /tmp/test/a3
sort -n -r "/tmp/test/a3"|grep -o -i ' [^<]*'  > /tmp/test/y
sed -i 's#%5D#.mp4#g' /tmp/test/y
sed -i '$d' /tmp/test/y
sed -i 's#src "#!240.mp4 #g' /tmp/test/y
cut -d '/' -f -7  /tmp/test/y > /tmp/test/x
sed -i 's#videos#videos/#g' /tmp/test/x
cd /tmp/test
if grep -E "720.mp4" x > /dev/null; then
awk '/720/ {print}' x > x1
elif grep -E "720.mp4" x > /dev/null; then
awk '/720/ {print}' x > x1
elif grep -E "480.mp4" x > /dev/null; then
awk '/480/ {print}' x > x1
elif grep -E "240.mp4" x > /dev/null; then
awk '/240/ {print}' x > x1
fi
sed -n '1,1p' x1 > xx
awk '{print $ 2}' xx > stream
grep -o -i 'amp;tag[^<]*' /tmp/test/a3 |awk '{print $ 2}' >> stream
awk '{print $ 1}' x1|sed -n '1,1p' >> stream
cat stream | tr -d '\n' > adresa
sed -i 's#!#.#g' adresa 
cat /tmp/test/b >> /tmp/music.m3u
cat /tmp/test/adresa >> /tmp/music.m3u
echo "" >> /tmp/music.m3u
#################################################
curl  -k -Lbk -m 55532 -m 555104 https://m.vk.com/video462530405_456240483 > /tmp/test/a
grep -o -i '"VideoPageInfoRow__title">[^<]*' /tmp/test/a > /tmp/test/b
sed -i 's/"VideoPageInfoRow__title">/#EXTINF:-1,/g' /tmp/test/b
grep -o -i '<source src=[^<]*' /tmp/test/a > /tmp/test/a1
sed -i 's#%2F#/#g' /tmp/test/a1 
sed -i 's#%3A#:#g' /tmp/test/a1 
sed -i 's#=# #g' /tmp/test/a1 
sed -i 's#&# #g' /tmp/test/a1 
sed -i 's#?# #g' /tmp/test/a1 
sed -i 's#dirs%5B#!#g' /tmp/test/a1 
sed 's/\([!]\+\)/\n\1/g' /tmp/test/a1 > /tmp/test/a2
awk '{print NR " " $0}' /tmp/test/a2  > /tmp/test/a3
sort -n -r "/tmp/test/a3"|grep -o -i ' [^<]*'  > /tmp/test/y
sed -i 's#%5D#.mp4#g' /tmp/test/y
sed -i '$d' /tmp/test/y
sed -i 's#src "#!240.mp4 #g' /tmp/test/y
cut -d '/' -f -7  /tmp/test/y > /tmp/test/x
sed -i 's#videos#videos/#g' /tmp/test/x
cd /tmp/test
if grep -E "720.mp4" x > /dev/null; then
awk '/720/ {print}' x > x1
elif grep -E "720.mp4" x > /dev/null; then
awk '/720/ {print}' x > x1
elif grep -E "480.mp4" x > /dev/null; then
awk '/480/ {print}' x > x1
elif grep -E "240.mp4" x > /dev/null; then
awk '/240/ {print}' x > x1
fi
sed -n '1,1p' x1 > xx
awk '{print $ 2}' xx > stream
grep -o -i 'amp;tag[^<]*' /tmp/test/a3 |awk '{print $ 2}' >> stream
awk '{print $ 1}' x1|sed -n '1,1p' >> stream
cat stream | tr -d '\n' > adresa
sed -i 's#!#.#g' adresa 
cat /tmp/test/b >> /tmp/music.m3u
cat /tmp/test/adresa >> /tmp/music.m3u
echo "" >> /tmp/music.m3u
#################################################
curl  -k -Lbk -m 55532 -m 555104 https://m.vk.com/video-53281593_456244260 > /tmp/test/a
grep -o -i '"VideoPageInfoRow__title">[^<]*' /tmp/test/a > /tmp/test/b
sed -i 's/"VideoPageInfoRow__title">/#EXTINF:-1,/g' /tmp/test/b
grep -o -i '<source src=[^<]*' /tmp/test/a > /tmp/test/a1
sed -i 's#%2F#/#g' /tmp/test/a1 
sed -i 's#%3A#:#g' /tmp/test/a1 
sed -i 's#=# #g' /tmp/test/a1 
sed -i 's#&# #g' /tmp/test/a1 
sed -i 's#?# #g' /tmp/test/a1 
sed -i 's#dirs%5B#!#g' /tmp/test/a1 
sed 's/\([!]\+\)/\n\1/g' /tmp/test/a1 > /tmp/test/a2
awk '{print NR " " $0}' /tmp/test/a2  > /tmp/test/a3
sort -n -r "/tmp/test/a3"|grep -o -i ' [^<]*'  > /tmp/test/y
sed -i 's#%5D#.mp4#g' /tmp/test/y
sed -i '$d' /tmp/test/y
sed -i 's#src "#!240.mp4 #g' /tmp/test/y
cut -d '/' -f -7  /tmp/test/y > /tmp/test/x
sed -i 's#videos#videos/#g' /tmp/test/x
cd /tmp/test
if grep -E "720.mp4" x > /dev/null; then
awk '/720/ {print}' x > x1
elif grep -E "720.mp4" x > /dev/null; then
awk '/720/ {print}' x > x1
elif grep -E "480.mp4" x > /dev/null; then
awk '/480/ {print}' x > x1
elif grep -E "240.mp4" x > /dev/null; then
awk '/240/ {print}' x > x1
fi
sed -n '1,1p' x1 > xx
awk '{print $ 2}' xx > stream
grep -o -i 'amp;tag[^<]*' /tmp/test/a3 |awk '{print $ 2}' >> stream
awk '{print $ 1}' x1|sed -n '1,1p' >> stream
cat stream | tr -d '\n' > adresa
sed -i 's#!#.#g' adresa 
cat /tmp/test/b >> /tmp/music.m3u
cat /tmp/test/adresa >> /tmp/music.m3u
echo "" >> /tmp/music.m3u
#################################################
curl  -k -Lbk -m 55532 -m 555104 https://m.vk.com/video330978220_456239615 > /tmp/test/a
grep -o -i '"VideoPageInfoRow__title">[^<]*' /tmp/test/a > /tmp/test/b
sed -i 's/"VideoPageInfoRow__title">/#EXTINF:-1,/g' /tmp/test/b
grep -o -i '<source src=[^<]*' /tmp/test/a > /tmp/test/a1
sed -i 's#%2F#/#g' /tmp/test/a1 
sed -i 's#%3A#:#g' /tmp/test/a1 
sed -i 's#=# #g' /tmp/test/a1 
sed -i 's#&# #g' /tmp/test/a1 
sed -i 's#?# #g' /tmp/test/a1 
sed -i 's#dirs%5B#!#g' /tmp/test/a1 
sed 's/\([!]\+\)/\n\1/g' /tmp/test/a1 > /tmp/test/a2
awk '{print NR " " $0}' /tmp/test/a2  > /tmp/test/a3
sort -n -r "/tmp/test/a3"|grep -o -i ' [^<]*'  > /tmp/test/y
sed -i 's#%5D#.mp4#g' /tmp/test/y
sed -i '$d' /tmp/test/y
sed -i 's#src "#!240.mp4 #g' /tmp/test/y
cut -d '/' -f -7  /tmp/test/y > /tmp/test/x
sed -i 's#videos#videos/#g' /tmp/test/x
cd /tmp/test
if grep -E "720.mp4" x > /dev/null; then
awk '/720/ {print}' x > x1
elif grep -E "720.mp4" x > /dev/null; then
awk '/720/ {print}' x > x1
elif grep -E "480.mp4" x > /dev/null; then
awk '/480/ {print}' x > x1
elif grep -E "240.mp4" x > /dev/null; then
awk '/240/ {print}' x > x1
fi
sed -n '1,1p' x1 > xx
awk '{print $ 2}' xx > stream
grep -o -i 'amp;tag[^<]*' /tmp/test/a3 |awk '{print $ 2}' >> stream
awk '{print $ 1}' x1|sed -n '1,1p' >> stream
cat stream | tr -d '\n' > adresa
sed -i 's#!#.#g' adresa 
cat /tmp/test/b >> /tmp/music.m3u
cat /tmp/test/adresa >> /tmp/music.m3u
echo "" >> /tmp/music.m3u
#################################################
curl  -k -Lbk -m 55532 -m 555104 https://m.vk.com/video265693995_456243012 > /tmp/test/a
grep -o -i '"VideoPageInfoRow__title">[^<]*' /tmp/test/a > /tmp/test/b
sed -i 's/"VideoPageInfoRow__title">/#EXTINF:-1,/g' /tmp/test/b
grep -o -i '<source src=[^<]*' /tmp/test/a > /tmp/test/a1
sed -i 's#%2F#/#g' /tmp/test/a1 
sed -i 's#%3A#:#g' /tmp/test/a1 
sed -i 's#=# #g' /tmp/test/a1 
sed -i 's#&# #g' /tmp/test/a1 
sed -i 's#?# #g' /tmp/test/a1 
sed -i 's#dirs%5B#!#g' /tmp/test/a1 
sed 's/\([!]\+\)/\n\1/g' /tmp/test/a1 > /tmp/test/a2
awk '{print NR " " $0}' /tmp/test/a2  > /tmp/test/a3
sort -n -r "/tmp/test/a3"|grep -o -i ' [^<]*'  > /tmp/test/y
sed -i 's#%5D#.mp4#g' /tmp/test/y
sed -i '$d' /tmp/test/y
sed -i 's#src "#!240.mp4 #g' /tmp/test/y
cut -d '/' -f -7  /tmp/test/y > /tmp/test/x
sed -i 's#videos#videos/#g' /tmp/test/x
cd /tmp/test
if grep -E "720.mp4" x > /dev/null; then
awk '/720/ {print}' x > x1
elif grep -E "720.mp4" x > /dev/null; then
awk '/720/ {print}' x > x1
elif grep -E "480.mp4" x > /dev/null; then
awk '/480/ {print}' x > x1
elif grep -E "240.mp4" x > /dev/null; then
awk '/240/ {print}' x > x1
fi
sed -n '1,1p' x1 > xx
awk '{print $ 2}' xx > stream
grep -o -i 'amp;tag[^<]*' /tmp/test/a3 |awk '{print $ 2}' >> stream
awk '{print $ 1}' x1|sed -n '1,1p' >> stream
cat stream | tr -d '\n' > adresa
sed -i 's#!#.#g' adresa 
cat /tmp/test/b >> /tmp/music.m3u
cat /tmp/test/adresa >> /tmp/music.m3u
echo "" >> /tmp/music.m3u
#################################################
curl  -k -Lbk -m 55532 -m 555104 https://m.vk.com/video-114889127_456239354 > /tmp/test/a
grep -o -i '"VideoPageInfoRow__title">[^<]*' /tmp/test/a > /tmp/test/b
sed -i 's/"VideoPageInfoRow__title">/#EXTINF:-1,/g' /tmp/test/b
grep -o -i '<source src=[^<]*' /tmp/test/a > /tmp/test/a1
sed -i 's#%2F#/#g' /tmp/test/a1 
sed -i 's#%3A#:#g' /tmp/test/a1 
sed -i 's#=# #g' /tmp/test/a1 
sed -i 's#&# #g' /tmp/test/a1 
sed -i 's#?# #g' /tmp/test/a1 
sed -i 's#dirs%5B#!#g' /tmp/test/a1 
sed 's/\([!]\+\)/\n\1/g' /tmp/test/a1 > /tmp/test/a2
awk '{print NR " " $0}' /tmp/test/a2  > /tmp/test/a3
sort -n -r "/tmp/test/a3"|grep -o -i ' [^<]*'  > /tmp/test/y
sed -i 's#%5D#.mp4#g' /tmp/test/y
sed -i '$d' /tmp/test/y
sed -i 's#src "#!240.mp4 #g' /tmp/test/y
cut -d '/' -f -7  /tmp/test/y > /tmp/test/x
sed -i 's#videos#videos/#g' /tmp/test/x
cd /tmp/test
if grep -E "720.mp4" x > /dev/null; then
awk '/720/ {print}' x > x1
elif grep -E "720.mp4" x > /dev/null; then
awk '/720/ {print}' x > x1
elif grep -E "480.mp4" x > /dev/null; then
awk '/480/ {print}' x > x1
elif grep -E "240.mp4" x > /dev/null; then
awk '/240/ {print}' x > x1
fi
sed -n '1,1p' x1 > xx
awk '{print $ 2}' xx > stream
grep -o -i 'amp;tag[^<]*' /tmp/test/a3 |awk '{print $ 2}' >> stream
awk '{print $ 1}' x1|sed -n '1,1p' >> stream
cat stream | tr -d '\n' > adresa
sed -i 's#!#.#g' adresa 
cat /tmp/test/b >> /tmp/music.m3u
cat /tmp/test/adresa >> /tmp/music.m3u
echo "" >> /tmp/music.m3u
#################################################
curl  -k -Lbk -m 55532 -m 555104 https://m.vk.com/video-91438212_456242546 > /tmp/test/a
grep -o -i '"VideoPageInfoRow__title">[^<]*' /tmp/test/a > /tmp/test/b
sed -i 's/"VideoPageInfoRow__title">/#EXTINF:-1,/g' /tmp/test/b
grep -o -i '<source src=[^<]*' /tmp/test/a > /tmp/test/a1
sed -i 's#%2F#/#g' /tmp/test/a1 
sed -i 's#%3A#:#g' /tmp/test/a1 
sed -i 's#=# #g' /tmp/test/a1 
sed -i 's#&# #g' /tmp/test/a1 
sed -i 's#?# #g' /tmp/test/a1 
sed -i 's#dirs%5B#!#g' /tmp/test/a1 
sed 's/\([!]\+\)/\n\1/g' /tmp/test/a1 > /tmp/test/a2
awk '{print NR " " $0}' /tmp/test/a2  > /tmp/test/a3
sort -n -r "/tmp/test/a3"|grep -o -i ' [^<]*'  > /tmp/test/y
sed -i 's#%5D#.mp4#g' /tmp/test/y
sed -i '$d' /tmp/test/y
sed -i 's#src "#!240.mp4 #g' /tmp/test/y
cut -d '/' -f -7  /tmp/test/y > /tmp/test/x
sed -i 's#videos#videos/#g' /tmp/test/x
cd /tmp/test
if grep -E "720.mp4" x > /dev/null; then
awk '/720/ {print}' x > x1
elif grep -E "720.mp4" x > /dev/null; then
awk '/720/ {print}' x > x1
elif grep -E "480.mp4" x > /dev/null; then
awk '/480/ {print}' x > x1
elif grep -E "240.mp4" x > /dev/null; then
awk '/240/ {print}' x > x1
fi
sed -n '1,1p' x1 > xx
awk '{print $ 2}' xx > stream
grep -o -i 'amp;tag[^<]*' /tmp/test/a3 |awk '{print $ 2}' >> stream
awk '{print $ 1}' x1|sed -n '1,1p' >> stream
cat stream | tr -d '\n' > adresa
sed -i 's#!#.#g' adresa 
cat /tmp/test/b >> /tmp/music.m3u
cat /tmp/test/adresa >> /tmp/music.m3u
echo "" >> /tmp/music.m3u
#################################################
curl  -k -Lbk -m 55532 -m 555104 https://m.vk.com/video216250843_456242765 > /tmp/test/a
grep -o -i '"VideoPageInfoRow__title">[^<]*' /tmp/test/a > /tmp/test/b
sed -i 's/"VideoPageInfoRow__title">/#EXTINF:-1,/g' /tmp/test/b
grep -o -i '<source src=[^<]*' /tmp/test/a > /tmp/test/a1
sed -i 's#%2F#/#g' /tmp/test/a1 
sed -i 's#%3A#:#g' /tmp/test/a1 
sed -i 's#=# #g' /tmp/test/a1 
sed -i 's#&# #g' /tmp/test/a1 
sed -i 's#?# #g' /tmp/test/a1 
sed -i 's#dirs%5B#!#g' /tmp/test/a1 
sed 's/\([!]\+\)/\n\1/g' /tmp/test/a1 > /tmp/test/a2
awk '{print NR " " $0}' /tmp/test/a2  > /tmp/test/a3
sort -n -r "/tmp/test/a3"|grep -o -i ' [^<]*'  > /tmp/test/y
sed -i 's#%5D#.mp4#g' /tmp/test/y
sed -i '$d' /tmp/test/y
sed -i 's#src "#!240.mp4 #g' /tmp/test/y
cut -d '/' -f -7  /tmp/test/y > /tmp/test/x
sed -i 's#videos#videos/#g' /tmp/test/x
cd /tmp/test
if grep -E "720.mp4" x > /dev/null; then
awk '/720/ {print}' x > x1
elif grep -E "720.mp4" x > /dev/null; then
awk '/720/ {print}' x > x1
elif grep -E "480.mp4" x > /dev/null; then
awk '/480/ {print}' x > x1
elif grep -E "240.mp4" x > /dev/null; then
awk '/240/ {print}' x > x1
fi
sed -n '1,1p' x1 > xx
awk '{print $ 2}' xx > stream
grep -o -i 'amp;tag[^<]*' /tmp/test/a3 |awk '{print $ 2}' >> stream
awk '{print $ 1}' x1|sed -n '1,1p' >> stream
cat stream | tr -d '\n' > adresa
sed -i 's#!#.#g' adresa 
cat /tmp/test/b >> /tmp/music.m3u
cat /tmp/test/adresa >> /tmp/music.m3u
echo "" >> /tmp/music.m3u
#################################################
curl  -k -Lbk -m 55532 -m 555104 https://m.vk.com/video50861944_456248242 > /tmp/test/a
grep -o -i '"VideoPageInfoRow__title">[^<]*' /tmp/test/a > /tmp/test/b
sed -i 's/"VideoPageInfoRow__title">/#EXTINF:-1,/g' /tmp/test/b
grep -o -i '<source src=[^<]*' /tmp/test/a > /tmp/test/a1
sed -i 's#%2F#/#g' /tmp/test/a1 
sed -i 's#%3A#:#g' /tmp/test/a1 
sed -i 's#=# #g' /tmp/test/a1 
sed -i 's#&# #g' /tmp/test/a1 
sed -i 's#?# #g' /tmp/test/a1 
sed -i 's#dirs%5B#!#g' /tmp/test/a1 
sed 's/\([!]\+\)/\n\1/g' /tmp/test/a1 > /tmp/test/a2
awk '{print NR " " $0}' /tmp/test/a2  > /tmp/test/a3
sort -n -r "/tmp/test/a3"|grep -o -i ' [^<]*'  > /tmp/test/y
sed -i 's#%5D#.mp4#g' /tmp/test/y
sed -i '$d' /tmp/test/y
sed -i 's#src "#!240.mp4 #g' /tmp/test/y
cut -d '/' -f -7  /tmp/test/y > /tmp/test/x
sed -i 's#videos#videos/#g' /tmp/test/x
cd /tmp/test
if grep -E "720.mp4" x > /dev/null; then
awk '/720/ {print}' x > x1
elif grep -E "720.mp4" x > /dev/null; then
awk '/720/ {print}' x > x1
elif grep -E "480.mp4" x > /dev/null; then
awk '/480/ {print}' x > x1
elif grep -E "240.mp4" x > /dev/null; then
awk '/240/ {print}' x > x1
fi
sed -n '1,1p' x1 > xx
awk '{print $ 2}' xx > stream
grep -o -i 'amp;tag[^<]*' /tmp/test/a3 |awk '{print $ 2}' >> stream
awk '{print $ 1}' x1|sed -n '1,1p' >> stream
cat stream | tr -d '\n' > adresa
sed -i 's#!#.#g' adresa 
cat /tmp/test/b >> /tmp/music.m3u
cat /tmp/test/adresa >> /tmp/music.m3u
echo "" >> /tmp/music.m3u
#################################################
curl  -k -Lbk -m 55532 -m 555104 https://m.vk.com/video-8065254_456239074 > /tmp/test/a
grep -o -i '"VideoPageInfoRow__title">[^<]*' /tmp/test/a > /tmp/test/b
sed -i 's/"VideoPageInfoRow__title">/#EXTINF:-1,/g' /tmp/test/b
grep -o -i '<source src=[^<]*' /tmp/test/a > /tmp/test/a1
sed -i 's#%2F#/#g' /tmp/test/a1 
sed -i 's#%3A#:#g' /tmp/test/a1 
sed -i 's#=# #g' /tmp/test/a1 
sed -i 's#&# #g' /tmp/test/a1 
sed -i 's#?# #g' /tmp/test/a1 
sed -i 's#dirs%5B#!#g' /tmp/test/a1 
sed 's/\([!]\+\)/\n\1/g' /tmp/test/a1 > /tmp/test/a2
awk '{print NR " " $0}' /tmp/test/a2  > /tmp/test/a3
sort -n -r "/tmp/test/a3"|grep -o -i ' [^<]*'  > /tmp/test/y
sed -i 's#%5D#.mp4#g' /tmp/test/y
sed -i '$d' /tmp/test/y
sed -i 's#src "#!240.mp4 #g' /tmp/test/y
cut -d '/' -f -7  /tmp/test/y > /tmp/test/x
sed -i 's#videos#videos/#g' /tmp/test/x
cd /tmp/test
if grep -E "720.mp4" x > /dev/null; then
awk '/720/ {print}' x > x1
elif grep -E "720.mp4" x > /dev/null; then
awk '/720/ {print}' x > x1
elif grep -E "480.mp4" x > /dev/null; then
awk '/480/ {print}' x > x1
elif grep -E "240.mp4" x > /dev/null; then
awk '/240/ {print}' x > x1
fi
sed -n '1,1p' x1 > xx
awk '{print $ 2}' xx > stream
grep -o -i 'amp;tag[^<]*' /tmp/test/a3 |awk '{print $ 2}' >> stream
awk '{print $ 1}' x1|sed -n '1,1p' >> stream
cat stream | tr -d '\n' > adresa
sed -i 's#!#.#g' adresa 
cat /tmp/test/b >> /tmp/music.m3u
cat /tmp/test/adresa >> /tmp/music.m3u
echo "" >> /tmp/music.m3u
#################################################
curl  -k -Lbk -m 55532 -m 555104 https://m.vk.com/video50861944_171536379 > /tmp/test/a
grep -o -i '"VideoPageInfoRow__title">[^<]*' /tmp/test/a > /tmp/test/b
sed -i 's/"VideoPageInfoRow__title">/#EXTINF:-1,/g' /tmp/test/b
grep -o -i '<source src=[^<]*' /tmp/test/a > /tmp/test/a1
sed -i 's#%2F#/#g' /tmp/test/a1 
sed -i 's#%3A#:#g' /tmp/test/a1 
sed -i 's#=# #g' /tmp/test/a1 
sed -i 's#&# #g' /tmp/test/a1 
sed -i 's#?# #g' /tmp/test/a1 
sed -i 's#dirs%5B#!#g' /tmp/test/a1 
sed 's/\([!]\+\)/\n\1/g' /tmp/test/a1 > /tmp/test/a2
awk '{print NR " " $0}' /tmp/test/a2  > /tmp/test/a3
sort -n -r "/tmp/test/a3"|grep -o -i ' [^<]*'  > /tmp/test/y
sed -i 's#%5D#.mp4#g' /tmp/test/y
sed -i '$d' /tmp/test/y
sed -i 's#src "#!240.mp4 #g' /tmp/test/y
cut -d '/' -f -7  /tmp/test/y > /tmp/test/x
sed -i 's#videos#videos/#g' /tmp/test/x
cd /tmp/test
if grep -E "720.mp4" x > /dev/null; then
awk '/720/ {print}' x > x1
elif grep -E "720.mp4" x > /dev/null; then
awk '/720/ {print}' x > x1
elif grep -E "480.mp4" x > /dev/null; then
awk '/480/ {print}' x > x1
elif grep -E "240.mp4" x > /dev/null; then
awk '/240/ {print}' x > x1
fi
sed -n '1,1p' x1 > xx
awk '{print $ 2}' xx > stream
grep -o -i 'amp;tag[^<]*' /tmp/test/a3 |awk '{print $ 2}' >> stream
awk '{print $ 1}' x1|sed -n '1,1p' >> stream
cat stream | tr -d '\n' > adresa
sed -i 's#!#.#g' adresa 
cat /tmp/test/b >> /tmp/music.m3u
cat /tmp/test/adresa >> /tmp/music.m3u
echo "" >> /tmp/music.m3u
#################################################
curl  -k -Lbk -m 55532 -m 555104 https://m.vk.com/video166586003_456239432 > /tmp/test/a
grep -o -i '"VideoPageInfoRow__title">[^<]*' /tmp/test/a > /tmp/test/b
sed -i 's/"VideoPageInfoRow__title">/#EXTINF:-1,/g' /tmp/test/b
grep -o -i '<source src=[^<]*' /tmp/test/a > /tmp/test/a1
sed -i 's#%2F#/#g' /tmp/test/a1 
sed -i 's#%3A#:#g' /tmp/test/a1 
sed -i 's#=# #g' /tmp/test/a1 
sed -i 's#&# #g' /tmp/test/a1 
sed -i 's#?# #g' /tmp/test/a1 
sed -i 's#dirs%5B#!#g' /tmp/test/a1 
sed 's/\([!]\+\)/\n\1/g' /tmp/test/a1 > /tmp/test/a2
awk '{print NR " " $0}' /tmp/test/a2  > /tmp/test/a3
sort -n -r "/tmp/test/a3"|grep -o -i ' [^<]*'  > /tmp/test/y
sed -i 's#%5D#.mp4#g' /tmp/test/y
sed -i '$d' /tmp/test/y
sed -i 's#src "#!240.mp4 #g' /tmp/test/y
cut -d '/' -f -7  /tmp/test/y > /tmp/test/x
sed -i 's#videos#videos/#g' /tmp/test/x
cd /tmp/test
if grep -E "720.mp4" x > /dev/null; then
awk '/720/ {print}' x > x1
elif grep -E "720.mp4" x > /dev/null; then
awk '/720/ {print}' x > x1
elif grep -E "480.mp4" x > /dev/null; then
awk '/480/ {print}' x > x1
elif grep -E "240.mp4" x > /dev/null; then
awk '/240/ {print}' x > x1
fi
sed -n '1,1p' x1 > xx
awk '{print $ 2}' xx > stream
grep -o -i 'amp;tag[^<]*' /tmp/test/a3 |awk '{print $ 2}' >> stream
awk '{print $ 1}' x1|sed -n '1,1p' >> stream
cat stream | tr -d '\n' > adresa
sed -i 's#!#.#g' adresa 
cat /tmp/test/b >> /tmp/music.m3u
cat /tmp/test/adresa >> /tmp/music.m3u
echo "" >> /tmp/music.m3u
#################################################
curl  -k -Lbk -m 55532 -m 555104 https://m.vk.com/video-198273640_456239042 > /tmp/test/a
grep -o -i '"VideoPageInfoRow__title">[^<]*' /tmp/test/a > /tmp/test/b
sed -i 's/"VideoPageInfoRow__title">/#EXTINF:-1,/g' /tmp/test/b
grep -o -i '<source src=[^<]*' /tmp/test/a > /tmp/test/a1
sed -i 's#%2F#/#g' /tmp/test/a1 
sed -i 's#%3A#:#g' /tmp/test/a1 
sed -i 's#=# #g' /tmp/test/a1 
sed -i 's#&# #g' /tmp/test/a1 
sed -i 's#?# #g' /tmp/test/a1 
sed -i 's#dirs%5B#!#g' /tmp/test/a1 
sed 's/\([!]\+\)/\n\1/g' /tmp/test/a1 > /tmp/test/a2
awk '{print NR " " $0}' /tmp/test/a2  > /tmp/test/a3
sort -n -r "/tmp/test/a3"|grep -o -i ' [^<]*'  > /tmp/test/y
sed -i 's#%5D#.mp4#g' /tmp/test/y
sed -i '$d' /tmp/test/y
sed -i 's#src "#!240.mp4 #g' /tmp/test/y
cut -d '/' -f -7  /tmp/test/y > /tmp/test/x
sed -i 's#videos#videos/#g' /tmp/test/x
cd /tmp/test
if grep -E "720.mp4" x > /dev/null; then
awk '/720/ {print}' x > x1
elif grep -E "720.mp4" x > /dev/null; then
awk '/720/ {print}' x > x1
elif grep -E "480.mp4" x > /dev/null; then
awk '/480/ {print}' x > x1
elif grep -E "240.mp4" x > /dev/null; then
awk '/240/ {print}' x > x1
fi
sed -n '1,1p' x1 > xx
awk '{print $ 2}' xx > stream
grep -o -i 'amp;tag[^<]*' /tmp/test/a3 |awk '{print $ 2}' >> stream
awk '{print $ 1}' x1|sed -n '1,1p' >> stream
cat stream | tr -d '\n' > adresa
sed -i 's#!#.#g' adresa 
cat /tmp/test/b >> /tmp/music.m3u
cat /tmp/test/adresa >> /tmp/music.m3u
echo "" >> /tmp/music.m3u
#################################################
curl  -k -Lbk -m 55532 -m 555104 https://m.vk.com/video-26901452_171423280 > /tmp/test/a
grep -o -i '"VideoPageInfoRow__title">[^<]*' /tmp/test/a > /tmp/test/b
sed -i 's/"VideoPageInfoRow__title">/#EXTINF:-1,/g' /tmp/test/b
grep -o -i '<source src=[^<]*' /tmp/test/a > /tmp/test/a1
sed -i 's#%2F#/#g' /tmp/test/a1 
sed -i 's#%3A#:#g' /tmp/test/a1 
sed -i 's#=# #g' /tmp/test/a1 
sed -i 's#&# #g' /tmp/test/a1 
sed -i 's#?# #g' /tmp/test/a1 
sed -i 's#dirs%5B#!#g' /tmp/test/a1 
sed 's/\([!]\+\)/\n\1/g' /tmp/test/a1 > /tmp/test/a2
awk '{print NR " " $0}' /tmp/test/a2  > /tmp/test/a3
sort -n -r "/tmp/test/a3"|grep -o -i ' [^<]*'  > /tmp/test/y
sed -i 's#%5D#.mp4#g' /tmp/test/y
sed -i '$d' /tmp/test/y
sed -i 's#src "#!240.mp4 #g' /tmp/test/y
cut -d '/' -f -7  /tmp/test/y > /tmp/test/x
sed -i 's#videos#videos/#g' /tmp/test/x
cd /tmp/test
if grep -E "720.mp4" x > /dev/null; then
awk '/720/ {print}' x > x1
elif grep -E "720.mp4" x > /dev/null; then
awk '/720/ {print}' x > x1
elif grep -E "480.mp4" x > /dev/null; then
awk '/480/ {print}' x > x1
elif grep -E "240.mp4" x > /dev/null; then
awk '/240/ {print}' x > x1
fi
sed -n '1,1p' x1 > xx
awk '{print $ 2}' xx > stream
grep -o -i 'amp;tag[^<]*' /tmp/test/a3 |awk '{print $ 2}' >> stream
awk '{print $ 1}' x1|sed -n '1,1p' >> stream
cat stream | tr -d '\n' > adresa
sed -i 's#!#.#g' adresa 
cat /tmp/test/b >> /tmp/music.m3u
cat /tmp/test/adresa >> /tmp/music.m3u
echo "" >> /tmp/music.m3u
#################################################
curl  -k -Lbk -m 55532 -m 555104 https://m.vk.com/video33694874_164219690 > /tmp/test/a
grep -o -i '"VideoPageInfoRow__title">[^<]*' /tmp/test/a > /tmp/test/b
sed -i 's/"VideoPageInfoRow__title">/#EXTINF:-1,/g' /tmp/test/b
grep -o -i '<source src=[^<]*' /tmp/test/a > /tmp/test/a1
sed -i 's#%2F#/#g' /tmp/test/a1 
sed -i 's#%3A#:#g' /tmp/test/a1 
sed -i 's#=# #g' /tmp/test/a1 
sed -i 's#&# #g' /tmp/test/a1 
sed -i 's#?# #g' /tmp/test/a1 
sed -i 's#dirs%5B#!#g' /tmp/test/a1 
sed 's/\([!]\+\)/\n\1/g' /tmp/test/a1 > /tmp/test/a2
awk '{print NR " " $0}' /tmp/test/a2  > /tmp/test/a3
sort -n -r "/tmp/test/a3"|grep -o -i ' [^<]*'  > /tmp/test/y
sed -i 's#%5D#.mp4#g' /tmp/test/y
sed -i '$d' /tmp/test/y
sed -i 's#src "#!240.mp4 #g' /tmp/test/y
cut -d '/' -f -7  /tmp/test/y > /tmp/test/x
sed -i 's#videos#videos/#g' /tmp/test/x
cd /tmp/test
if grep -E "720.mp4" x > /dev/null; then
awk '/720/ {print}' x > x1
elif grep -E "720.mp4" x > /dev/null; then
awk '/720/ {print}' x > x1
elif grep -E "480.mp4" x > /dev/null; then
awk '/480/ {print}' x > x1
elif grep -E "240.mp4" x > /dev/null; then
awk '/240/ {print}' x > x1
fi
sed -n '1,1p' x1 > xx
awk '{print $ 2}' xx > stream
grep -o -i 'amp;tag[^<]*' /tmp/test/a3 |awk '{print $ 2}' >> stream
awk '{print $ 1}' x1|sed -n '1,1p' >> stream
cat stream | tr -d '\n' > adresa
sed -i 's#!#.#g' adresa 
cat /tmp/test/b >> /tmp/music.m3u
cat /tmp/test/adresa >> /tmp/music.m3u
echo "" >> /tmp/music.m3u
#################################################
curl  -k -Lbk -m 55532 -m 555104 https://m.vk.com/video34745483_456240149 > /tmp/test/a
grep -o -i '"VideoPageInfoRow__title">[^<]*' /tmp/test/a > /tmp/test/b
sed -i 's/"VideoPageInfoRow__title">/#EXTINF:-1,/g' /tmp/test/b
grep -o -i '<source src=[^<]*' /tmp/test/a > /tmp/test/a1
sed -i 's#%2F#/#g' /tmp/test/a1 
sed -i 's#%3A#:#g' /tmp/test/a1 
sed -i 's#=# #g' /tmp/test/a1 
sed -i 's#&# #g' /tmp/test/a1 
sed -i 's#?# #g' /tmp/test/a1 
sed -i 's#dirs%5B#!#g' /tmp/test/a1 
sed 's/\([!]\+\)/\n\1/g' /tmp/test/a1 > /tmp/test/a2
awk '{print NR " " $0}' /tmp/test/a2  > /tmp/test/a3
sort -n -r "/tmp/test/a3"|grep -o -i ' [^<]*'  > /tmp/test/y
sed -i 's#%5D#.mp4#g' /tmp/test/y
sed -i '$d' /tmp/test/y
sed -i 's#src "#!240.mp4 #g' /tmp/test/y
cut -d '/' -f -7  /tmp/test/y > /tmp/test/x
sed -i 's#videos#videos/#g' /tmp/test/x
cd /tmp/test
if grep -E "720.mp4" x > /dev/null; then
awk '/720/ {print}' x > x1
elif grep -E "720.mp4" x > /dev/null; then
awk '/720/ {print}' x > x1
elif grep -E "480.mp4" x > /dev/null; then
awk '/480/ {print}' x > x1
elif grep -E "240.mp4" x > /dev/null; then
awk '/240/ {print}' x > x1
fi
sed -n '1,1p' x1 > xx
awk '{print $ 2}' xx > stream
grep -o -i 'amp;tag[^<]*' /tmp/test/a3 |awk '{print $ 2}' >> stream
awk '{print $ 1}' x1|sed -n '1,1p' >> stream
cat stream | tr -d '\n' > adresa
sed -i 's#!#.#g' adresa 
cat /tmp/test/b >> /tmp/music.m3u
cat /tmp/test/adresa >> /tmp/music.m3u
echo "" >> /tmp/music.m3u
#################################################
curl  -k -Lbk -m 55532 -m 555104 https://m.vk.com/video141811137_456239083 > /tmp/test/a
grep -o -i '"VideoPageInfoRow__title">[^<]*' /tmp/test/a > /tmp/test/b
sed -i 's/"VideoPageInfoRow__title">/#EXTINF:-1,/g' /tmp/test/b
grep -o -i '<source src=[^<]*' /tmp/test/a > /tmp/test/a1
sed -i 's#%2F#/#g' /tmp/test/a1 
sed -i 's#%3A#:#g' /tmp/test/a1 
sed -i 's#=# #g' /tmp/test/a1 
sed -i 's#&# #g' /tmp/test/a1 
sed -i 's#?# #g' /tmp/test/a1 
sed -i 's#dirs%5B#!#g' /tmp/test/a1 
sed 's/\([!]\+\)/\n\1/g' /tmp/test/a1 > /tmp/test/a2
awk '{print NR " " $0}' /tmp/test/a2  > /tmp/test/a3
sort -n -r "/tmp/test/a3"|grep -o -i ' [^<]*'  > /tmp/test/y
sed -i 's#%5D#.mp4#g' /tmp/test/y
sed -i '$d' /tmp/test/y
sed -i 's#src "#!240.mp4 #g' /tmp/test/y
cut -d '/' -f -7  /tmp/test/y > /tmp/test/x
sed -i 's#videos#videos/#g' /tmp/test/x
cd /tmp/test
if grep -E "720.mp4" x > /dev/null; then
awk '/720/ {print}' x > x1
elif grep -E "720.mp4" x > /dev/null; then
awk '/720/ {print}' x > x1
elif grep -E "480.mp4" x > /dev/null; then
awk '/480/ {print}' x > x1
elif grep -E "240.mp4" x > /dev/null; then
awk '/240/ {print}' x > x1
fi
sed -n '1,1p' x1 > xx
awk '{print $ 2}' xx > stream
grep -o -i 'amp;tag[^<]*' /tmp/test/a3 |awk '{print $ 2}' >> stream
awk '{print $ 1}' x1|sed -n '1,1p' >> stream
cat stream | tr -d '\n' > adresa
sed -i 's#!#.#g' adresa 
cat /tmp/test/b >> /tmp/music.m3u
cat /tmp/test/adresa >> /tmp/music.m3u
echo "" >> /tmp/music.m3u
#################################################
curl  -k -Lbk -m 55532 -m 555104 https://m.vk.com/video-102943864_456239053 > /tmp/test/a
grep -o -i '"VideoPageInfoRow__title">[^<]*' /tmp/test/a > /tmp/test/b
sed -i 's/"VideoPageInfoRow__title">/#EXTINF:-1,/g' /tmp/test/b
grep -o -i '<source src=[^<]*' /tmp/test/a > /tmp/test/a1
sed -i 's#%2F#/#g' /tmp/test/a1 
sed -i 's#%3A#:#g' /tmp/test/a1 
sed -i 's#=# #g' /tmp/test/a1 
sed -i 's#&# #g' /tmp/test/a1 
sed -i 's#?# #g' /tmp/test/a1 
sed -i 's#dirs%5B#!#g' /tmp/test/a1 
sed 's/\([!]\+\)/\n\1/g' /tmp/test/a1 > /tmp/test/a2
awk '{print NR " " $0}' /tmp/test/a2  > /tmp/test/a3
sort -n -r "/tmp/test/a3"|grep -o -i ' [^<]*'  > /tmp/test/y
sed -i 's#%5D#.mp4#g' /tmp/test/y
sed -i '$d' /tmp/test/y
sed -i 's#src "#!240.mp4 #g' /tmp/test/y
cut -d '/' -f -7  /tmp/test/y > /tmp/test/x
sed -i 's#videos#videos/#g' /tmp/test/x
cd /tmp/test
if grep -E "720.mp4" x > /dev/null; then
awk '/720/ {print}' x > x1
elif grep -E "720.mp4" x > /dev/null; then
awk '/720/ {print}' x > x1
elif grep -E "480.mp4" x > /dev/null; then
awk '/480/ {print}' x > x1
elif grep -E "240.mp4" x > /dev/null; then
awk '/240/ {print}' x > x1
fi
sed -n '1,1p' x1 > xx
awk '{print $ 2}' xx > stream
grep -o -i 'amp;tag[^<]*' /tmp/test/a3 |awk '{print $ 2}' >> stream
awk '{print $ 1}' x1|sed -n '1,1p' >> stream
cat stream | tr -d '\n' > adresa
sed -i 's#!#.#g' adresa 
cat /tmp/test/b >> /tmp/music.m3u
cat /tmp/test/adresa >> /tmp/music.m3u
echo "" >> /tmp/music.m3u
#################################################
curl  -k -Lbk -m 55532 -m 555104 https://m.vk.com/video-53281593_456250724 > /tmp/test/a
grep -o -i '"VideoPageInfoRow__title">[^<]*' /tmp/test/a > /tmp/test/b
sed -i 's/"VideoPageInfoRow__title">/#EXTINF:-1,/g' /tmp/test/b
grep -o -i '<source src=[^<]*' /tmp/test/a > /tmp/test/a1
sed -i 's#%2F#/#g' /tmp/test/a1 
sed -i 's#%3A#:#g' /tmp/test/a1 
sed -i 's#=# #g' /tmp/test/a1 
sed -i 's#&# #g' /tmp/test/a1 
sed -i 's#?# #g' /tmp/test/a1 
sed -i 's#dirs%5B#!#g' /tmp/test/a1 
sed 's/\([!]\+\)/\n\1/g' /tmp/test/a1 > /tmp/test/a2
awk '{print NR " " $0}' /tmp/test/a2  > /tmp/test/a3
sort -n -r "/tmp/test/a3"|grep -o -i ' [^<]*'  > /tmp/test/y
sed -i 's#%5D#.mp4#g' /tmp/test/y
sed -i '$d' /tmp/test/y
sed -i 's#src "#!240.mp4 #g' /tmp/test/y
cut -d '/' -f -7  /tmp/test/y > /tmp/test/x
sed -i 's#videos#videos/#g' /tmp/test/x
cd /tmp/test
if grep -E "720.mp4" x > /dev/null; then
awk '/720/ {print}' x > x1
elif grep -E "720.mp4" x > /dev/null; then
awk '/720/ {print}' x > x1
elif grep -E "480.mp4" x > /dev/null; then
awk '/480/ {print}' x > x1
elif grep -E "240.mp4" x > /dev/null; then
awk '/240/ {print}' x > x1
fi
sed -n '1,1p' x1 > xx
awk '{print $ 2}' xx > stream
grep -o -i 'amp;tag[^<]*' /tmp/test/a3 |awk '{print $ 2}' >> stream
awk '{print $ 1}' x1|sed -n '1,1p' >> stream
cat stream | tr -d '\n' > adresa
sed -i 's#!#.#g' adresa 
cat /tmp/test/b >> /tmp/music.m3u
cat /tmp/test/adresa >> /tmp/music.m3u
echo "" >> /tmp/music.m3u
#################################################
curl  -k -Lbk -m 55532 -m 555104 https://m.vk.com/video-183188668_456241860 > /tmp/test/a
grep -o -i '"VideoPageInfoRow__title">[^<]*' /tmp/test/a > /tmp/test/b
sed -i 's/"VideoPageInfoRow__title">/#EXTINF:-1,/g' /tmp/test/b
grep -o -i '<source src=[^<]*' /tmp/test/a > /tmp/test/a1
sed -i 's#%2F#/#g' /tmp/test/a1 
sed -i 's#%3A#:#g' /tmp/test/a1 
sed -i 's#=# #g' /tmp/test/a1 
sed -i 's#&# #g' /tmp/test/a1 
sed -i 's#?# #g' /tmp/test/a1 
sed -i 's#dirs%5B#!#g' /tmp/test/a1 
sed 's/\([!]\+\)/\n\1/g' /tmp/test/a1 > /tmp/test/a2
awk '{print NR " " $0}' /tmp/test/a2  > /tmp/test/a3
sort -n -r "/tmp/test/a3"|grep -o -i ' [^<]*'  > /tmp/test/y
sed -i 's#%5D#.mp4#g' /tmp/test/y
sed -i '$d' /tmp/test/y
sed -i 's#src "#!240.mp4 #g' /tmp/test/y
cut -d '/' -f -7  /tmp/test/y > /tmp/test/x
sed -i 's#videos#videos/#g' /tmp/test/x
cd /tmp/test
if grep -E "720.mp4" x > /dev/null; then
awk '/720/ {print}' x > x1
elif grep -E "720.mp4" x > /dev/null; then
awk '/720/ {print}' x > x1
elif grep -E "480.mp4" x > /dev/null; then
awk '/480/ {print}' x > x1
elif grep -E "240.mp4" x > /dev/null; then
awk '/240/ {print}' x > x1
fi
sed -n '1,1p' x1 > xx
awk '{print $ 2}' xx > stream
grep -o -i 'amp;tag[^<]*' /tmp/test/a3 |awk '{print $ 2}' >> stream
awk '{print $ 1}' x1|sed -n '1,1p' >> stream
cat stream | tr -d '\n' > adresa
sed -i 's#!#.#g' adresa 
cat /tmp/test/b >> /tmp/music.m3u
cat /tmp/test/adresa >> /tmp/music.m3u
echo "" >> /tmp/music.m3u
#################################################
curl  -k -Lbk -m 55532 -m 555104 https://m.vk.com/video325353815_171541127 > /tmp/test/a
grep -o -i '"VideoPageInfoRow__title">[^<]*' /tmp/test/a > /tmp/test/b
sed -i 's/"VideoPageInfoRow__title">/#EXTINF:-1,/g' /tmp/test/b
grep -o -i '<source src=[^<]*' /tmp/test/a > /tmp/test/a1
sed -i 's#%2F#/#g' /tmp/test/a1 
sed -i 's#%3A#:#g' /tmp/test/a1 
sed -i 's#=# #g' /tmp/test/a1 
sed -i 's#&# #g' /tmp/test/a1 
sed -i 's#?# #g' /tmp/test/a1 
sed -i 's#dirs%5B#!#g' /tmp/test/a1 
sed 's/\([!]\+\)/\n\1/g' /tmp/test/a1 > /tmp/test/a2
awk '{print NR " " $0}' /tmp/test/a2  > /tmp/test/a3
sort -n -r "/tmp/test/a3"|grep -o -i ' [^<]*'  > /tmp/test/y
sed -i 's#%5D#.mp4#g' /tmp/test/y
sed -i '$d' /tmp/test/y
sed -i 's#src "#!240.mp4 #g' /tmp/test/y
cut -d '/' -f -7  /tmp/test/y > /tmp/test/x
sed -i 's#videos#videos/#g' /tmp/test/x
cd /tmp/test
if grep -E "720.mp4" x > /dev/null; then
awk '/720/ {print}' x > x1
elif grep -E "720.mp4" x > /dev/null; then
awk '/720/ {print}' x > x1
elif grep -E "480.mp4" x > /dev/null; then
awk '/480/ {print}' x > x1
elif grep -E "240.mp4" x > /dev/null; then
awk '/240/ {print}' x > x1
fi
sed -n '1,1p' x1 > xx
awk '{print $ 2}' xx > stream
grep -o -i 'amp;tag[^<]*' /tmp/test/a3 |awk '{print $ 2}' >> stream
awk '{print $ 1}' x1|sed -n '1,1p' >> stream
cat stream | tr -d '\n' > adresa
sed -i 's#!#.#g' adresa 
cat /tmp/test/b >> /tmp/music.m3u
cat /tmp/test/adresa >> /tmp/music.m3u
echo "" >> /tmp/music.m3u
#################################################
curl  -k -Lbk -m 55532 -m 555104 https://m.vk.com/video-173758523_456239514 > /tmp/test/a
grep -o -i '"VideoPageInfoRow__title">[^<]*' /tmp/test/a > /tmp/test/b
sed -i 's/"VideoPageInfoRow__title">/#EXTINF:-1,/g' /tmp/test/b
grep -o -i '<source src=[^<]*' /tmp/test/a > /tmp/test/a1
sed -i 's#%2F#/#g' /tmp/test/a1 
sed -i 's#%3A#:#g' /tmp/test/a1 
sed -i 's#=# #g' /tmp/test/a1 
sed -i 's#&# #g' /tmp/test/a1 
sed -i 's#?# #g' /tmp/test/a1 
sed -i 's#dirs%5B#!#g' /tmp/test/a1 
sed 's/\([!]\+\)/\n\1/g' /tmp/test/a1 > /tmp/test/a2
awk '{print NR " " $0}' /tmp/test/a2  > /tmp/test/a3
sort -n -r "/tmp/test/a3"|grep -o -i ' [^<]*'  > /tmp/test/y
sed -i 's#%5D#.mp4#g' /tmp/test/y
sed -i '$d' /tmp/test/y
sed -i 's#src "#!240.mp4 #g' /tmp/test/y
cut -d '/' -f -7  /tmp/test/y > /tmp/test/x
sed -i 's#videos#videos/#g' /tmp/test/x
cd /tmp/test
if grep -E "720.mp4" x > /dev/null; then
awk '/720/ {print}' x > x1
elif grep -E "720.mp4" x > /dev/null; then
awk '/720/ {print}' x > x1
elif grep -E "480.mp4" x > /dev/null; then
awk '/480/ {print}' x > x1
elif grep -E "240.mp4" x > /dev/null; then
awk '/240/ {print}' x > x1
fi
sed -n '1,1p' x1 > xx
awk '{print $ 2}' xx > stream
grep -o -i 'amp;tag[^<]*' /tmp/test/a3 |awk '{print $ 2}' >> stream
awk '{print $ 1}' x1|sed -n '1,1p' >> stream
cat stream | tr -d '\n' > adresa
sed -i 's#!#.#g' adresa 
cat /tmp/test/b >> /tmp/music.m3u
cat /tmp/test/adresa >> /tmp/music.m3u
echo "" >> /tmp/music.m3u
#################################################
curl  -k -Lbk -m 55532 -m 555104 https://m.vk.com/video-101777083_456247527 > /tmp/test/a
grep -o -i '"VideoPageInfoRow__title">[^<]*' /tmp/test/a > /tmp/test/b
sed -i 's/"VideoPageInfoRow__title">/#EXTINF:-1,/g' /tmp/test/b
grep -o -i '<source src=[^<]*' /tmp/test/a > /tmp/test/a1
sed -i 's#%2F#/#g' /tmp/test/a1 
sed -i 's#%3A#:#g' /tmp/test/a1 
sed -i 's#=# #g' /tmp/test/a1 
sed -i 's#&# #g' /tmp/test/a1 
sed -i 's#?# #g' /tmp/test/a1 
sed -i 's#dirs%5B#!#g' /tmp/test/a1 
sed 's/\([!]\+\)/\n\1/g' /tmp/test/a1 > /tmp/test/a2
awk '{print NR " " $0}' /tmp/test/a2  > /tmp/test/a3
sort -n -r "/tmp/test/a3"|grep -o -i ' [^<]*'  > /tmp/test/y
sed -i 's#%5D#.mp4#g' /tmp/test/y
sed -i '$d' /tmp/test/y
sed -i 's#src "#!240.mp4 #g' /tmp/test/y
cut -d '/' -f -7  /tmp/test/y > /tmp/test/x
sed -i 's#videos#videos/#g' /tmp/test/x
cd /tmp/test
if grep -E "720.mp4" x > /dev/null; then
awk '/720/ {print}' x > x1
elif grep -E "720.mp4" x > /dev/null; then
awk '/720/ {print}' x > x1
elif grep -E "480.mp4" x > /dev/null; then
awk '/480/ {print}' x > x1
elif grep -E "240.mp4" x > /dev/null; then
awk '/240/ {print}' x > x1
fi
sed -n '1,1p' x1 > xx
awk '{print $ 2}' xx > stream
grep -o -i 'amp;tag[^<]*' /tmp/test/a3 |awk '{print $ 2}' >> stream
awk '{print $ 1}' x1|sed -n '1,1p' >> stream
cat stream | tr -d '\n' > adresa
sed -i 's#!#.#g' adresa 
cat /tmp/test/b >> /tmp/music.m3u
cat /tmp/test/adresa >> /tmp/music.m3u
echo "" >> /tmp/music.m3u
#################################################
curl  -k -Lbk -m 55532 -m 555104 https://m.vk.com/video50861944_456239902 > /tmp/test/a
grep -o -i '"VideoPageInfoRow__title">[^<]*' /tmp/test/a > /tmp/test/b
sed -i 's/"VideoPageInfoRow__title">/#EXTINF:-1,/g' /tmp/test/b
grep -o -i '<source src=[^<]*' /tmp/test/a > /tmp/test/a1
sed -i 's#%2F#/#g' /tmp/test/a1 
sed -i 's#%3A#:#g' /tmp/test/a1 
sed -i 's#=# #g' /tmp/test/a1 
sed -i 's#&# #g' /tmp/test/a1 
sed -i 's#?# #g' /tmp/test/a1 
sed -i 's#dirs%5B#!#g' /tmp/test/a1 
sed 's/\([!]\+\)/\n\1/g' /tmp/test/a1 > /tmp/test/a2
awk '{print NR " " $0}' /tmp/test/a2  > /tmp/test/a3
sort -n -r "/tmp/test/a3"|grep -o -i ' [^<]*'  > /tmp/test/y
sed -i 's#%5D#.mp4#g' /tmp/test/y
sed -i '$d' /tmp/test/y
sed -i 's#src "#!240.mp4 #g' /tmp/test/y
cut -d '/' -f -7  /tmp/test/y > /tmp/test/x
sed -i 's#videos#videos/#g' /tmp/test/x
cd /tmp/test
if grep -E "720.mp4" x > /dev/null; then
awk '/720/ {print}' x > x1
elif grep -E "720.mp4" x > /dev/null; then
awk '/720/ {print}' x > x1
elif grep -E "480.mp4" x > /dev/null; then
awk '/480/ {print}' x > x1
elif grep -E "240.mp4" x > /dev/null; then
awk '/240/ {print}' x > x1
fi
sed -n '1,1p' x1 > xx
awk '{print $ 2}' xx > stream
grep -o -i 'amp;tag[^<]*' /tmp/test/a3 |awk '{print $ 2}' >> stream
awk '{print $ 1}' x1|sed -n '1,1p' >> stream
cat stream | tr -d '\n' > adresa
sed -i 's#!#.#g' adresa 
cat /tmp/test/b >> /tmp/music.m3u
cat /tmp/test/adresa >> /tmp/music.m3u
echo "" >> /tmp/music.m3u
#################################################
curl  -k -Lbk -m 55532 -m 555104 https://m.vk.com/video297425198_456239075 > /tmp/test/a
grep -o -i '"VideoPageInfoRow__title">[^<]*' /tmp/test/a > /tmp/test/b
sed -i 's/"VideoPageInfoRow__title">/#EXTINF:-1,/g' /tmp/test/b
grep -o -i '<source src=[^<]*' /tmp/test/a > /tmp/test/a1
sed -i 's#%2F#/#g' /tmp/test/a1 
sed -i 's#%3A#:#g' /tmp/test/a1 
sed -i 's#=# #g' /tmp/test/a1 
sed -i 's#&# #g' /tmp/test/a1 
sed -i 's#?# #g' /tmp/test/a1 
sed -i 's#dirs%5B#!#g' /tmp/test/a1 
sed 's/\([!]\+\)/\n\1/g' /tmp/test/a1 > /tmp/test/a2
awk '{print NR " " $0}' /tmp/test/a2  > /tmp/test/a3
sort -n -r "/tmp/test/a3"|grep -o -i ' [^<]*'  > /tmp/test/y
sed -i 's#%5D#.mp4#g' /tmp/test/y
sed -i '$d' /tmp/test/y
sed -i 's#src "#!240.mp4 #g' /tmp/test/y
cut -d '/' -f -7  /tmp/test/y > /tmp/test/x
sed -i 's#videos#videos/#g' /tmp/test/x
cd /tmp/test
if grep -E "720.mp4" x > /dev/null; then
awk '/720/ {print}' x > x1
elif grep -E "720.mp4" x > /dev/null; then
awk '/720/ {print}' x > x1
elif grep -E "480.mp4" x > /dev/null; then
awk '/480/ {print}' x > x1
elif grep -E "240.mp4" x > /dev/null; then
awk '/240/ {print}' x > x1
fi
sed -n '1,1p' x1 > xx
awk '{print $ 2}' xx > stream
grep -o -i 'amp;tag[^<]*' /tmp/test/a3 |awk '{print $ 2}' >> stream
awk '{print $ 1}' x1|sed -n '1,1p' >> stream
cat stream | tr -d '\n' > adresa
sed -i 's#!#.#g' adresa 
cat /tmp/test/b >> /tmp/music.m3u
cat /tmp/test/adresa >> /tmp/music.m3u
echo "" >> /tmp/music.m3u
#################################################
rm -rf /tmp/test
#################################################
[ -d /tmp/test ] || mkdir -p /tmp/test
#################################################
cp /tmp/music.m3u /tmp/test/music.m3u
cp /tmp/music.m3u /movie/musicBoxHitsOLD.m3u

#################################################
more /usr/lib/enigma2/python/Plugins/Extensions/OpenPanel/DATA/x  >> /etc/enigma2/bouquets.tv 
sed -i "s/%/userbouquet.musicBoxHitsOLD.m3u.tv/" /etc/enigma2/bouquets.tv 

awk 'BEGIN {FS="png"}{print  $NF}'  /tmp/test/music.m3u > /tmp/test/Rus3.m3u
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
echo "#NAME musicBoxHitsOLD.m3u" > /etc/enigma2/userbouquet.musicBoxHitsOLD.m3u.tv
cat /tmp/test/Rus10.m3u >> /etc/enigma2/userbouquet.musicBoxHitsOLD.m3u.tv
rm -rf /tmp/test
rm -rf /tmp/music.m3u
cd /
wget -q -O - http://root%s@127.0.0.1/web/servicelistreload?mode=0 >>/dev/null 2>&1 </dev/null &
sleep 2
echo "OK"
exit








