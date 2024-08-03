#!/bin/sh
sleep 1
echo "stahuji stream list SKTonline ..Koncerty"
sleep 2
[ -d /movie ] || mkdir -p /movie
#################################################

#################################################
[ -d /tmp/test ] || mkdir -p /tmp/test

#################################################
curl  -k -Lbk -m 55532 -m 555104 "http://online.sktorrent.eu/videos/hudba?o=mv" > /tmp/test/a
grep -o -i '<a href="/video/[^<]*' /tmp/test/a > /tmp/test/a1
curl  -k -Lbk -m 55532 -m 555104 "http://online.sktorrent.eu/videos/hudba?o=mv&page=2" > /tmp/test/b
grep -o -i '<a href="/video/[^<]*' /tmp/test/b > /tmp/test/b1
cat /tmp/test/a1 /tmp/test/b1 > /tmp/test/c
grep -o -i '/video[^<]*' /tmp/test/c  > /tmp/test/c1
cut -d '"' -f 1  /tmp/test/c1 > /tmp/test/www
#################################################
cut -d '/' -f 4  /tmp/test/www > /tmp/test/nazev

cd /tmp/test
#################################################
adresa1=`sed -n '1,1p' www`
adresa1=$adresa1
curl -Lbk -m 4555 -m 6555 -k  http://online.sktorrent.eu$adresa1 > /tmp/test/x
if grep -E "1080p.mp4" x > /dev/null; then
awk '/1080p/ {print}' x > x1
elif grep -E "720p.mp4" x > /dev/null; then
awk '/720/ {print}' x > x1
elif grep -E "480p.mp4" x > /dev/null; then
awk '/480/ {print}' x > x1
elif grep -E "240p.mp4" x > /dev/null; then
awk '/240/ {print}' x > x1
fi
sed 's/\(["]\+\)/\n\1/g' x1 > x2
awk '/videos/ {print}' x2 > x3
echo "#EXTINF:-1," > film
sed -n '1,1p' nazev >> film
cat film | tr -d '\n' > film.m3u
echo "" >> film.m3u
sed 's/"//g' x3 >> film.m3u
#################################################
adresa1=`sed -n '2,2p' www`
adresa1=$adresa1
curl -Lbk -m 4555 -m 6555 -k  http://online.sktorrent.eu$adresa1 > /tmp/test/x
if grep -E "1080p.mp4" x > /dev/null; then
awk '/1080p/ {print}' x > x1
elif grep -E "720p.mp4" x > /dev/null; then
awk '/720/ {print}' x > x1
elif grep -E "480p.mp4" x > /dev/null; then
awk '/480/ {print}' x > x1
elif grep -E "240p.mp4" x > /dev/null; then
awk '/240/ {print}' x > x1
fi
sed 's/\(["]\+\)/\n\1/g' x1 > x2
awk '/videos/ {print}' x2 > x3
echo "#EXTINF:-1," > film
sed -n '2,2p' nazev >> film
cat film | tr -d '\n' >> film.m3u
echo "" >> film.m3u
sed 's/"//g' x3 >> film.m3u
#################################################
adresa1=`sed -n '3,3p' www`
adresa1=$adresa1
curl -Lbk -m 4555 -m 6555 -k  http://online.sktorrent.eu$adresa1 > /tmp/test/x
if grep -E "1080p.mp4" x > /dev/null; then
awk '/1080p/ {print}' x > x1
elif grep -E "720p.mp4" x > /dev/null; then
awk '/720/ {print}' x > x1
elif grep -E "480p.mp4" x > /dev/null; then
awk '/480/ {print}' x > x1
elif grep -E "240p.mp4" x > /dev/null; then
awk '/240/ {print}' x > x1
fi
sed 's/\(["]\+\)/\n\1/g' x1 > x2
awk '/videos/ {print}' x2 > x3
echo "#EXTINF:-1," > film
sed -n '3,3p' nazev >> film
cat film | tr -d '\n' >> film.m3u
echo "" >> film.m3u
sed 's/"//g' x3 >> film.m3u
#################################################
adresa1=`sed -n '4,4p' www`
adresa1=$adresa1
curl -Lbk -m 4555 -m 6555 -k  http://online.sktorrent.eu$adresa1 > /tmp/test/x
if grep -E "1080p.mp4" x > /dev/null; then
awk '/1080p/ {print}' x > x1
elif grep -E "720p.mp4" x > /dev/null; then
awk '/720/ {print}' x > x1
elif grep -E "480p.mp4" x > /dev/null; then
awk '/480/ {print}' x > x1
elif grep -E "240p.mp4" x > /dev/null; then
awk '/240/ {print}' x > x1
fi
sed 's/\(["]\+\)/\n\1/g' x1 > x2
awk '/videos/ {print}' x2 > x3
echo "#EXTINF:-1," > film
sed -n '4,4p' nazev >> film
cat film | tr -d '\n' >> film.m3u
echo "" >> film.m3u
sed 's/"//g' x3 >> film.m3u
#################################################
adresa1=`sed -n '5,5p' www`
adresa1=$adresa1
curl -Lbk -m 4555 -m 6555 -k  http://online.sktorrent.eu$adresa1 > /tmp/test/x
if grep -E "1080p.mp4" x > /dev/null; then
awk '/1080p/ {print}' x > x1
elif grep -E "720p.mp4" x > /dev/null; then
awk '/720/ {print}' x > x1
elif grep -E "480p.mp4" x > /dev/null; then
awk '/480/ {print}' x > x1
elif grep -E "240p.mp4" x > /dev/null; then
awk '/240/ {print}' x > x1
fi
sed 's/\(["]\+\)/\n\1/g' x1 > x2
awk '/videos/ {print}' x2 > x3
echo "#EXTINF:-1," > film
sed -n '5,5p' nazev >> film
cat film | tr -d '\n' >> film.m3u
echo "" >> film.m3u
sed 's/"//g' x3 >> film.m3u
#################################################
adresa1=`sed -n '6,6p' www`
adresa1=$adresa1
curl -Lbk -m 4555 -m 6555 -k  http://online.sktorrent.eu$adresa1 > /tmp/test/x
if grep -E "1080p.mp4" x > /dev/null; then
awk '/1080p/ {print}' x > x1
elif grep -E "720p.mp4" x > /dev/null; then
awk '/720/ {print}' x > x1
elif grep -E "480p.mp4" x > /dev/null; then
awk '/480/ {print}' x > x1
elif grep -E "240p.mp4" x > /dev/null; then
awk '/240/ {print}' x > x1
fi
sed 's/\(["]\+\)/\n\1/g' x1 > x2
awk '/videos/ {print}' x2 > x3
echo "#EXTINF:-1," > film
sed -n '6,6p' nazev >> film
cat film | tr -d '\n' >> film.m3u
echo "" >> film.m3u
sed 's/"//g' x3 >> film.m3u
#################################################
adresa1=`sed -n '7,7p' www`
adresa1=$adresa1
curl -Lbk -m 4555 -m 6555 -k  http://online.sktorrent.eu$adresa1 > /tmp/test/x
if grep -E "1080p.mp4" x > /dev/null; then
awk '/1080p/ {print}' x > x1
elif grep -E "720p.mp4" x > /dev/null; then
awk '/720/ {print}' x > x1
elif grep -E "480p.mp4" x > /dev/null; then
awk '/480/ {print}' x > x1
elif grep -E "240p.mp4" x > /dev/null; then
awk '/240/ {print}' x > x1
fi
sed 's/\(["]\+\)/\n\1/g' x1 > x2
awk '/videos/ {print}' x2 > x3
echo "#EXTINF:-1," > film
sed -n '7,7p' nazev >> film
cat film | tr -d '\n' >> film.m3u
echo "" >> film.m3u
sed 's/"//g' x3 >> film.m3u
#################################################
adresa1=`sed -n '8,8p' www`
adresa1=$adresa1
curl -Lbk -m 4555 -m 6555 -k  http://online.sktorrent.eu$adresa1 > /tmp/test/x
if grep -E "1080p.mp4" x > /dev/null; then
awk '/1080p/ {print}' x > x1
elif grep -E "720p.mp4" x > /dev/null; then
awk '/720/ {print}' x > x1
elif grep -E "480p.mp4" x > /dev/null; then
awk '/480/ {print}' x > x1
elif grep -E "240p.mp4" x > /dev/null; then
awk '/240/ {print}' x > x1
fi
sed 's/\(["]\+\)/\n\1/g' x1 > x2
awk '/videos/ {print}' x2 > x3
echo "#EXTINF:-1," > film
sed -n '8,8p' nazev >> film
cat film | tr -d '\n' >> film.m3u
echo "" >> film.m3u
sed 's/"//g' x3 >> film.m3u
#################################################
adresa1=`sed -n '9,9p' www`
adresa1=$adresa1
curl -Lbk -m 4555 -m 6555 -k  http://online.sktorrent.eu$adresa1 > /tmp/test/x
if grep -E "1080p.mp4" x > /dev/null; then
awk '/1080p/ {print}' x > x1
elif grep -E "720p.mp4" x > /dev/null; then
awk '/720/ {print}' x > x1
elif grep -E "480p.mp4" x > /dev/null; then
awk '/480/ {print}' x > x1
elif grep -E "240p.mp4" x > /dev/null; then
awk '/240/ {print}' x > x1
fi
sed 's/\(["]\+\)/\n\1/g' x1 > x2
awk '/videos/ {print}' x2 > x3
echo "#EXTINF:-1," > film
sed -n '9,9p' nazev >> film
cat film | tr -d '\n' >> film.m3u
echo "" >> film.m3u
sed 's/"//g' x3 >> film.m3u
#################################################
adresa1=`sed -n '10,10p' www`
adresa1=$adresa1
curl -Lbk -m 4555 -m 6555 -k  http://online.sktorrent.eu$adresa1 > /tmp/test/x
if grep -E "1080p.mp4" x > /dev/null; then
awk '/1080p/ {print}' x > x1
elif grep -E "720p.mp4" x > /dev/null; then
awk '/720/ {print}' x > x1
elif grep -E "480p.mp4" x > /dev/null; then
awk '/480/ {print}' x > x1
elif grep -E "240p.mp4" x > /dev/null; then
awk '/240/ {print}' x > x1
fi
sed 's/\(["]\+\)/\n\1/g' x1 > x2
awk '/videos/ {print}' x2 > x3
echo "#EXTINF:-1," > film
sed -n '10,10p' nazev >> film
cat film | tr -d '\n' >> film.m3u
echo "" >> film.m3u
sed 's/"//g' x3 >> film.m3u
#################################################
adresa1=`sed -n '11,11p' www`
adresa1=$adresa1
curl -Lbk -m 4555 -m 6555 -k  http://online.sktorrent.eu$adresa1 > /tmp/test/x
if grep -E "1080p.mp4" x > /dev/null; then
awk '/1080p/ {print}' x > x1
elif grep -E "720p.mp4" x > /dev/null; then
awk '/720/ {print}' x > x1
elif grep -E "480p.mp4" x > /dev/null; then
awk '/480/ {print}' x > x1
elif grep -E "240p.mp4" x > /dev/null; then
awk '/240/ {print}' x > x1
fi
sed 's/\(["]\+\)/\n\1/g' x1 > x2
awk '/videos/ {print}' x2 > x3
echo "#EXTINF:-1," > film
sed -n '11,11p' nazev >> film
cat film | tr -d '\n' >> film.m3u
echo "" >> film.m3u
sed 's/"//g' x3 >> film.m3u
#################################################
adresa1=`sed -n '12,12p' www`
adresa1=$adresa1
curl -Lbk -m 4555 -m 6555 -k  http://online.sktorrent.eu$adresa1 > /tmp/test/x
if grep -E "1080p.mp4" x > /dev/null; then
awk '/1080p/ {print}' x > x1
elif grep -E "720p.mp4" x > /dev/null; then
awk '/720/ {print}' x > x1
elif grep -E "480p.mp4" x > /dev/null; then
awk '/480/ {print}' x > x1
elif grep -E "240p.mp4" x > /dev/null; then
awk '/240/ {print}' x > x1
fi
sed 's/\(["]\+\)/\n\1/g' x1 > x2
awk '/videos/ {print}' x2 > x3
echo "#EXTINF:-1," > film
sed -n '12,12p' nazev >> film
cat film | tr -d '\n' >> film.m3u
echo "" >> film.m3u
sed 's/"//g' x3 >> film.m3u
#################################################
adresa1=`sed -n '13,13p' www`
adresa1=$adresa1
curl -Lbk -m 4555 -m 6555 -k  http://online.sktorrent.eu$adresa1 > /tmp/test/x
if grep -E "1080p.mp4" x > /dev/null; then
awk '/1080p/ {print}' x > x1
elif grep -E "720p.mp4" x > /dev/null; then
awk '/720/ {print}' x > x1
elif grep -E "480p.mp4" x > /dev/null; then
awk '/480/ {print}' x > x1
elif grep -E "240p.mp4" x > /dev/null; then
awk '/240/ {print}' x > x1
fi
sed 's/\(["]\+\)/\n\1/g' x1 > x2
awk '/videos/ {print}' x2 > x3
echo "#EXTINF:-1," > film
sed -n '13,13p' nazev >> film
cat film | tr -d '\n' >> film.m3u
echo "" >> film.m3u
sed 's/"//g' x3 >> film.m3u
#################################################
adresa1=`sed -n '14,14p' www`
adresa1=$adresa1
curl -Lbk -m 4555 -m 6555 -k  http://online.sktorrent.eu$adresa1 > /tmp/test/x
if grep -E "1080p.mp4" x > /dev/null; then
awk '/1080p/ {print}' x > x1
elif grep -E "720p.mp4" x > /dev/null; then
awk '/720/ {print}' x > x1
elif grep -E "480p.mp4" x > /dev/null; then
awk '/480/ {print}' x > x1
elif grep -E "240p.mp4" x > /dev/null; then
awk '/240/ {print}' x > x1
fi
sed 's/\(["]\+\)/\n\1/g' x1 > x2
awk '/videos/ {print}' x2 > x3
echo "#EXTINF:-1," > film
sed -n '14,14p' nazev >> film
cat film | tr -d '\n' >> film.m3u
echo "" >> film.m3u
sed 's/"//g' x3 >> film.m3u
#################################################
adresa1=`sed -n '15,15p' www`
adresa1=$adresa1
curl -Lbk -m 4555 -m 6555 -k  http://online.sktorrent.eu$adresa1 > /tmp/test/x
if grep -E "1080p.mp4" x > /dev/null; then
awk '/1080p/ {print}' x > x1
elif grep -E "720p.mp4" x > /dev/null; then
awk '/720/ {print}' x > x1
elif grep -E "480p.mp4" x > /dev/null; then
awk '/480/ {print}' x > x1
elif grep -E "240p.mp4" x > /dev/null; then
awk '/240/ {print}' x > x1
fi
sed 's/\(["]\+\)/\n\1/g' x1 > x2
awk '/videos/ {print}' x2 > x3
echo "#EXTINF:-1," > film
sed -n '15,15p' nazev >> film
cat film | tr -d '\n' >> film.m3u
echo "" >> film.m3u
sed 's/"//g' x3 >> film.m3u
#################################################
adresa1=`sed -n '16,16p' www`
adresa1=$adresa1
curl -Lbk -m 4555 -m 6555 -k  http://online.sktorrent.eu$adresa1 > /tmp/test/x
if grep -E "1080p.mp4" x > /dev/null; then
awk '/1080p/ {print}' x > x1
elif grep -E "720p.mp4" x > /dev/null; then
awk '/720/ {print}' x > x1
elif grep -E "480p.mp4" x > /dev/null; then
awk '/480/ {print}' x > x1
elif grep -E "240p.mp4" x > /dev/null; then
awk '/240/ {print}' x > x1
fi
sed 's/\(["]\+\)/\n\1/g' x1 > x2
awk '/videos/ {print}' x2 > x3
echo "#EXTINF:-1," > film
sed -n '16,16p' nazev >> film
cat film | tr -d '\n' >> film.m3u
echo "" >> film.m3u
sed 's/"//g' x3 >> film.m3u
#################################################
adresa1=`sed -n '17,17p' www`
adresa1=$adresa1
curl -Lbk -m 4555 -m 6555 -k  http://online.sktorrent.eu$adresa1 > /tmp/test/x
if grep -E "1080p.mp4" x > /dev/null; then
awk '/1080p/ {print}' x > x1
elif grep -E "720p.mp4" x > /dev/null; then
awk '/720/ {print}' x > x1
elif grep -E "480p.mp4" x > /dev/null; then
awk '/480/ {print}' x > x1
elif grep -E "240p.mp4" x > /dev/null; then
awk '/240/ {print}' x > x1
fi
sed 's/\(["]\+\)/\n\1/g' x1 > x2
awk '/videos/ {print}' x2 > x3
echo "#EXTINF:-1," > film
sed -n '17,17p' nazev >> film
cat film | tr -d '\n' >> film.m3u
echo "" >> film.m3u
sed 's/"//g' x3 >> film.m3u
#################################################
adresa1=`sed -n '18,18p' www`
adresa1=$adresa1
curl -Lbk -m 4555 -m 6555 -k  http://online.sktorrent.eu$adresa1 > /tmp/test/x
if grep -E "1080p.mp4" x > /dev/null; then
awk '/1080p/ {print}' x > x1
elif grep -E "720p.mp4" x > /dev/null; then
awk '/720/ {print}' x > x1
elif grep -E "480p.mp4" x > /dev/null; then
awk '/480/ {print}' x > x1
elif grep -E "240p.mp4" x > /dev/null; then
awk '/240/ {print}' x > x1
fi
sed 's/\(["]\+\)/\n\1/g' x1 > x2
awk '/videos/ {print}' x2 > x3
echo "#EXTINF:-1," > film
sed -n '18,18p' nazev >> film
cat film | tr -d '\n' >> film.m3u
echo "" >> film.m3u
sed 's/"//g' x3 >> film.m3u
#################################################
adresa1=`sed -n '19,19p' www`
adresa1=$adresa1
curl -Lbk -m 4555 -m 6555 -k  http://online.sktorrent.eu$adresa1 > /tmp/test/x
if grep -E "1080p.mp4" x > /dev/null; then
awk '/1080p/ {print}' x > x1
elif grep -E "720p.mp4" x > /dev/null; then
awk '/720/ {print}' x > x1
elif grep -E "480p.mp4" x > /dev/null; then
awk '/480/ {print}' x > x1
elif grep -E "240p.mp4" x > /dev/null; then
awk '/240/ {print}' x > x1
fi
sed 's/\(["]\+\)/\n\1/g' x1 > x2
awk '/videos/ {print}' x2 > x3
echo "#EXTINF:-1," > film
sed -n '19,19p' nazev >> film
cat film | tr -d '\n' >> film.m3u
echo "" >> film.m3u
sed 's/"//g' x3 >> film.m3u
#################################################
adresa1=`sed -n '20,20p' www`
adresa1=$adresa1
curl -Lbk -m 4555 -m 6555 -k  http://online.sktorrent.eu$adresa1 > /tmp/test/x
if grep -E "1080p.mp4" x > /dev/null; then
awk '/1080p/ {print}' x > x1
elif grep -E "720p.mp4" x > /dev/null; then
awk '/720/ {print}' x > x1
elif grep -E "480p.mp4" x > /dev/null; then
awk '/480/ {print}' x > x1
elif grep -E "240p.mp4" x > /dev/null; then
awk '/240/ {print}' x > x1
fi
sed 's/\(["]\+\)/\n\1/g' x1 > x2
awk '/videos/ {print}' x2 > x3
echo "#EXTINF:-1," > film
sed -n '20,20p' nazev >> film
cat film | tr -d '\n' >> film.m3u
echo "" >> film.m3u
sed 's/"//g' x3 >> film.m3u
#################################################
adresa1=`sed -n '21,21p' www`
adresa1=$adresa1
curl -Lbk -m 4555 -m 6555 -k  http://online.sktorrent.eu$adresa1 > /tmp/test/x
if grep -E "1080p.mp4" x > /dev/null; then
awk '/1080p/ {print}' x > x1
elif grep -E "720p.mp4" x > /dev/null; then
awk '/720/ {print}' x > x1
elif grep -E "480p.mp4" x > /dev/null; then
awk '/480/ {print}' x > x1
elif grep -E "240p.mp4" x > /dev/null; then
awk '/240/ {print}' x > x1
fi
sed 's/\(["]\+\)/\n\1/g' x1 > x2
awk '/videos/ {print}' x2 > x3
echo "#EXTINF:-1," > film
sed -n '21,21p' nazev >> film
cat film | tr -d '\n' >> film.m3u
echo "" >> film.m3u
sed 's/"//g' x3 >> film.m3u
#################################################
adresa1=`sed -n '22,22p' www`
adresa1=$adresa1
curl -Lbk -m 4555 -m 6555 -k  http://online.sktorrent.eu$adresa1 > /tmp/test/x
if grep -E "1080p.mp4" x > /dev/null; then
awk '/1080p/ {print}' x > x1
elif grep -E "720p.mp4" x > /dev/null; then
awk '/720/ {print}' x > x1
elif grep -E "480p.mp4" x > /dev/null; then
awk '/480/ {print}' x > x1
elif grep -E "240p.mp4" x > /dev/null; then
awk '/240/ {print}' x > x1
fi
sed 's/\(["]\+\)/\n\1/g' x1 > x2
awk '/videos/ {print}' x2 > x3
echo "#EXTINF:-1," > film
sed -n '12,12p' nazev >> film
cat film | tr -d '\n' >> film.m3u
echo "" >> film.m3u
sed 's/"//g' x3 >> film.m3u
#################################################
adresa1=`sed -n '23,23p' www`
adresa1=$adresa1
curl -Lbk -m 4555 -m 6555 -k  http://online.sktorrent.eu$adresa1 > /tmp/test/x
if grep -E "1080p.mp4" x > /dev/null; then
awk '/1080p/ {print}' x > x1
elif grep -E "720p.mp4" x > /dev/null; then
awk '/720/ {print}' x > x1
elif grep -E "480p.mp4" x > /dev/null; then
awk '/480/ {print}' x > x1
elif grep -E "240p.mp4" x > /dev/null; then
awk '/240/ {print}' x > x1
fi
sed 's/\(["]\+\)/\n\1/g' x1 > x2
awk '/videos/ {print}' x2 > x3
echo "#EXTINF:-1," > film
sed -n '23,23p' nazev >> film
cat film | tr -d '\n' >> film.m3u
echo "" >> film.m3u
sed 's/"//g' x3 >> film.m3u
#################################################
adresa1=`sed -n '24,24p' www`
adresa1=$adresa1
curl -Lbk -m 4555 -m 6555 -k  http://online.sktorrent.eu$adresa1 > /tmp/test/x
if grep -E "1080p.mp4" x > /dev/null; then
awk '/1080p/ {print}' x > x1
elif grep -E "720p.mp4" x > /dev/null; then
awk '/720/ {print}' x > x1
elif grep -E "480p.mp4" x > /dev/null; then
awk '/480/ {print}' x > x1
elif grep -E "240p.mp4" x > /dev/null; then
awk '/240/ {print}' x > x1
fi
sed 's/\(["]\+\)/\n\1/g' x1 > x2
awk '/videos/ {print}' x2 > x3
echo "#EXTINF:-1," > film
sed -n '24,24p' nazev >> film
cat film | tr -d '\n' >> film.m3u
echo "" >> film.m3u
sed 's/"//g' x3 >> film.m3u
#################################################
adresa1=`sed -n '25,25p' www`
adresa1=$adresa1
curl -Lbk -m 4555 -m 6555 -k  http://online.sktorrent.eu$adresa1 > /tmp/test/x
if grep -E "1080p.mp4" x > /dev/null; then
awk '/1080p/ {print}' x > x1
elif grep -E "720p.mp4" x > /dev/null; then
awk '/720/ {print}' x > x1
elif grep -E "480p.mp4" x > /dev/null; then
awk '/480/ {print}' x > x1
elif grep -E "240p.mp4" x > /dev/null; then
awk '/240/ {print}' x > x1
fi
sed 's/\(["]\+\)/\n\1/g' x1 > x2
awk '/videos/ {print}' x2 > x3
echo "#EXTINF:-1," > film
sed -n '25,25p' nazev >> film
cat film | tr -d '\n' >> film.m3u
echo "" >> film.m3u
sed 's/"//g' x3 >> film.m3u
#################################################
adresa1=`sed -n '26,26p' www`
adresa1=$adresa1
curl -Lbk -m 4555 -m 6555 -k  http://online.sktorrent.eu$adresa1 > /tmp/test/x
if grep -E "1080p.mp4" x > /dev/null; then
awk '/1080p/ {print}' x > x1
elif grep -E "720p.mp4" x > /dev/null; then
awk '/720/ {print}' x > x1
elif grep -E "480p.mp4" x > /dev/null; then
awk '/480/ {print}' x > x1
elif grep -E "240p.mp4" x > /dev/null; then
awk '/240/ {print}' x > x1
fi
sed 's/\(["]\+\)/\n\1/g' x1 > x2
awk '/videos/ {print}' x2 > x3
echo "#EXTINF:-1," > film
sed -n '26,26p' nazev >> film
cat film | tr -d '\n' >> film.m3u
echo "" >> film.m3u
sed 's/"//g' x3 >> film.m3u
#################################################
adresa1=`sed -n '27,27p' www`
adresa1=$adresa1
curl -Lbk -m 4555 -m 6555 -k  http://online.sktorrent.eu$adresa1 > /tmp/test/x
if grep -E "1080p.mp4" x > /dev/null; then
awk '/1080p/ {print}' x > x1
elif grep -E "720p.mp4" x > /dev/null; then
awk '/720/ {print}' x > x1
elif grep -E "480p.mp4" x > /dev/null; then
awk '/480/ {print}' x > x1
elif grep -E "240p.mp4" x > /dev/null; then
awk '/240/ {print}' x > x1
fi
sed 's/\(["]\+\)/\n\1/g' x1 > x2
awk '/videos/ {print}' x2 > x3
echo "#EXTINF:-1," > film
sed -n '27,27p' nazev >> film
cat film | tr -d '\n' >> film.m3u
echo "" >> film.m3u
sed 's/"//g' x3 >> film.m3u
#################################################
adresa1=`sed -n '28,28p' www`
adresa1=$adresa1
curl -Lbk -m 4555 -m 6555 -k  http://online.sktorrent.eu$adresa1 > /tmp/test/x
if grep -E "1080p.mp4" x > /dev/null; then
awk '/1080p/ {print}' x > x1
elif grep -E "720p.mp4" x > /dev/null; then
awk '/720/ {print}' x > x1
elif grep -E "480p.mp4" x > /dev/null; then
awk '/480/ {print}' x > x1
elif grep -E "240p.mp4" x > /dev/null; then
awk '/240/ {print}' x > x1
fi
sed 's/\(["]\+\)/\n\1/g' x1 > x2
awk '/videos/ {print}' x2 > x3
echo "#EXTINF:-1," > film
sed -n '28,28p' nazev >> film
cat film | tr -d '\n' >> film.m3u
echo "" >> film.m3u
sed 's/"//g' x3 >> film.m3u
#################################################
adresa1=`sed -n '29,29p' www`
adresa1=$adresa1
curl -Lbk -m 4555 -m 6555 -k  http://online.sktorrent.eu$adresa1 > /tmp/test/x
if grep -E "1080p.mp4" x > /dev/null; then
awk '/1080p/ {print}' x > x1
elif grep -E "720p.mp4" x > /dev/null; then
awk '/720/ {print}' x > x1
elif grep -E "480p.mp4" x > /dev/null; then
awk '/480/ {print}' x > x1
elif grep -E "240p.mp4" x > /dev/null; then
awk '/240/ {print}' x > x1
fi
sed 's/\(["]\+\)/\n\1/g' x1 > x2
awk '/videos/ {print}' x2 > x3
echo "#EXTINF:-1," > film
sed -n '29,29p' nazev >> film
cat film | tr -d '\n' >> film.m3u
echo "" >> film.m3u
sed 's/"//g' x3 >> film.m3u
#################################################
adresa1=`sed -n '30,30p' www`
adresa1=$adresa1
curl -Lbk -m 4555 -m 6555 -k  http://online.sktorrent.eu$adresa1 > /tmp/test/x
if grep -E "1080p.mp4" x > /dev/null; then
awk '/1080p/ {print}' x > x1
elif grep -E "720p.mp4" x > /dev/null; then
awk '/720/ {print}' x > x1
elif grep -E "480p.mp4" x > /dev/null; then
awk '/480/ {print}' x > x1
elif grep -E "240p.mp4" x > /dev/null; then
awk '/240/ {print}' x > x1
fi
sed 's/\(["]\+\)/\n\1/g' x1 > x2
awk '/videos/ {print}' x2 > x3
echo "#EXTINF:-1," > film
sed -n '30,30p' nazev >> film
cat film | tr -d '\n' >> film.m3u
echo "" >> film.m3u
sed 's/"//g' x3 >> film.m3u
#################################################
adresa1=`sed -n '31,31p' www`
adresa1=$adresa1
curl -Lbk -m 4555 -m 6555 -k  http://online.sktorrent.eu$adresa1 > /tmp/test/x
if grep -E "1080p.mp4" x > /dev/null; then
awk '/1080p/ {print}' x > x1
elif grep -E "720p.mp4" x > /dev/null; then
awk '/720/ {print}' x > x1
elif grep -E "480p.mp4" x > /dev/null; then
awk '/480/ {print}' x > x1
elif grep -E "240p.mp4" x > /dev/null; then
awk '/240/ {print}' x > x1
fi
sed 's/\(["]\+\)/\n\1/g' x1 > x2
awk '/videos/ {print}' x2 > x3
echo "#EXTINF:-1," > film
sed -n '31,31p' nazev >> film
cat film | tr -d '\n' >> film.m3u
echo "" >> film.m3u
sed 's/"//g' x3 >> film.m3u
#################################################
adresa1=`sed -n '32,32p' www`
adresa1=$adresa1
curl -Lbk -m 4555 -m 6555 -k  http://online.sktorrent.eu$adresa1 > /tmp/test/x
if grep -E "1080p.mp4" x > /dev/null; then
awk '/1080p/ {print}' x > x1
elif grep -E "720p.mp4" x > /dev/null; then
awk '/720/ {print}' x > x1
elif grep -E "480p.mp4" x > /dev/null; then
awk '/480/ {print}' x > x1
elif grep -E "240p.mp4" x > /dev/null; then
awk '/240/ {print}' x > x1
fi
sed 's/\(["]\+\)/\n\1/g' x1 > x2
awk '/videos/ {print}' x2 > x3
echo "#EXTINF:-1," > film
sed -n '32,32p' nazev >> film
cat film | tr -d '\n' >> film.m3u
echo "" >> film.m3u
sed 's/"//g' x3 >> film.m3u
#################################################
adresa1=`sed -n '33,33p' www`
adresa1=$adresa1
curl -Lbk -m 4555 -m 6555 -k  http://online.sktorrent.eu$adresa1 > /tmp/test/x
if grep -E "1080p.mp4" x > /dev/null; then
awk '/1080p/ {print}' x > x1
elif grep -E "720p.mp4" x > /dev/null; then
awk '/720/ {print}' x > x1
elif grep -E "480p.mp4" x > /dev/null; then
awk '/480/ {print}' x > x1
elif grep -E "240p.mp4" x > /dev/null; then
awk '/240/ {print}' x > x1
fi
sed 's/\(["]\+\)/\n\1/g' x1 > x2
awk '/videos/ {print}' x2 > x3
echo "#EXTINF:-1," > film
sed -n '33,33p' nazev >> film
cat film | tr -d '\n' >> film.m3u
echo "" >> film.m3u
sed 's/"//g' x3 >> film.m3u
#################################################
adresa1=`sed -n '34,34p' www`
adresa1=$adresa1
curl -Lbk -m 4555 -m 6555 -k  http://online.sktorrent.eu$adresa1 > /tmp/test/x
if grep -E "1080p.mp4" x > /dev/null; then
awk '/1080p/ {print}' x > x1
elif grep -E "720p.mp4" x > /dev/null; then
awk '/720/ {print}' x > x1
elif grep -E "480p.mp4" x > /dev/null; then
awk '/480/ {print}' x > x1
elif grep -E "240p.mp4" x > /dev/null; then
awk '/240/ {print}' x > x1
fi
sed 's/\(["]\+\)/\n\1/g' x1 > x2
awk '/videos/ {print}' x2 > x3
echo "#EXTINF:-1," > film
sed -n '34,34p' nazev >> film
cat film | tr -d '\n' >> film.m3u
echo "" >> film.m3u
sed 's/"//g' x3 >> film.m3u
#################################################
adresa1=`sed -n '35,35p' www`
adresa1=$adresa1
curl -Lbk -m 4555 -m 6555 -k  http://online.sktorrent.eu$adresa1 > /tmp/test/x
if grep -E "1080p.mp4" x > /dev/null; then
awk '/1080p/ {print}' x > x1
elif grep -E "720p.mp4" x > /dev/null; then
awk '/720/ {print}' x > x1
elif grep -E "480p.mp4" x > /dev/null; then
awk '/480/ {print}' x > x1
elif grep -E "240p.mp4" x > /dev/null; then
awk '/240/ {print}' x > x1
fi
sed 's/\(["]\+\)/\n\1/g' x1 > x2
awk '/videos/ {print}' x2 > x3
echo "#EXTINF:-1," > film
sed -n '35,35p' nazev >> film
cat film | tr -d '\n' >> film.m3u
echo "" >> film.m3u
sed 's/"//g' x3 >> film.m3u
#################################################
adresa1=`sed -n '36,36p' www`
adresa1=$adresa1
curl -Lbk -m 4555 -m 6555 -k  http://online.sktorrent.eu$adresa1 > /tmp/test/x
if grep -E "1080p.mp4" x > /dev/null; then
awk '/1080p/ {print}' x > x1
elif grep -E "720p.mp4" x > /dev/null; then
awk '/720/ {print}' x > x1
elif grep -E "480p.mp4" x > /dev/null; then
awk '/480/ {print}' x > x1
elif grep -E "240p.mp4" x > /dev/null; then
awk '/240/ {print}' x > x1
fi
sed 's/\(["]\+\)/\n\1/g' x1 > x2
awk '/videos/ {print}' x2 > x3
echo "#EXTINF:-1," > film
sed -n '36,36p' nazev >> film
cat film | tr -d '\n' >> film.m3u
echo "" >> film.m3u
sed 's/"//g' x3 >> film.m3u
#################################################
awk '/EXTINF/ {print}''/mp4/ {print}' film.m3u > /tmp/film.m3u
cd /
rm -rf /tmp/test


[ -d /tmp/test ] || mkdir -p /tmp/test

#################################################
curl  -k -Lbk -m 55532 -m 555104 "http://online.sktorrent.eu/videos/hudba?o=mv&page=3" > /tmp/test/a
grep -o -i '<a href="/video/[^<]*' /tmp/test/a > /tmp/test/a1
curl  -k -Lbk -m 55532 -m 555104 "http://online.sktorrent.eu/videos/hudba?o=mv&page=4" > /tmp/test/b
grep -o -i '<a href="/video/[^<]*' /tmp/test/b > /tmp/test/b1
cat /tmp/test/a1 /tmp/test/b1 > /tmp/test/c
grep -o -i '/video[^<]*' /tmp/test/c  > /tmp/test/c1
cut -d '"' -f 1  /tmp/test/c1 > /tmp/test/www
#################################################
cut -d '/' -f 4  /tmp/test/www > /tmp/test/nazev

cd /tmp/test
#################################################
adresa1=`sed -n '1,1p' www`
adresa1=$adresa1
curl -Lbk -m 4555 -m 6555 -k  http://online.sktorrent.eu$adresa1 > /tmp/test/x
if grep -E "1080p.mp4" x > /dev/null; then
awk '/1080p/ {print}' x > x1
elif grep -E "720p.mp4" x > /dev/null; then
awk '/720/ {print}' x > x1
elif grep -E "480p.mp4" x > /dev/null; then
awk '/480/ {print}' x > x1
elif grep -E "240p.mp4" x > /dev/null; then
awk '/240/ {print}' x > x1
fi
sed 's/\(["]\+\)/\n\1/g' x1 > x2
awk '/videos/ {print}' x2 > x3
echo "#EXTINF:-1," > film
sed -n '1,1p' nazev >> film
cat film | tr -d '\n' > film.m3u
echo "" >> film.m3u
sed 's/"//g' x3 >> film.m3u
#################################################
adresa1=`sed -n '2,2p' www`
adresa1=$adresa1
curl -Lbk -m 4555 -m 6555 -k  http://online.sktorrent.eu$adresa1 > /tmp/test/x
if grep -E "1080p.mp4" x > /dev/null; then
awk '/1080p/ {print}' x > x1
elif grep -E "720p.mp4" x > /dev/null; then
awk '/720/ {print}' x > x1
elif grep -E "480p.mp4" x > /dev/null; then
awk '/480/ {print}' x > x1
elif grep -E "240p.mp4" x > /dev/null; then
awk '/240/ {print}' x > x1
fi
sed 's/\(["]\+\)/\n\1/g' x1 > x2
awk '/videos/ {print}' x2 > x3
echo "#EXTINF:-1," > film
sed -n '2,2p' nazev >> film
cat film | tr -d '\n' >> film.m3u
echo "" >> film.m3u
sed 's/"//g' x3 >> film.m3u
#################################################
adresa1=`sed -n '3,3p' www`
adresa1=$adresa1
curl -Lbk -m 4555 -m 6555 -k  http://online.sktorrent.eu$adresa1 > /tmp/test/x
if grep -E "1080p.mp4" x > /dev/null; then
awk '/1080p/ {print}' x > x1
elif grep -E "720p.mp4" x > /dev/null; then
awk '/720/ {print}' x > x1
elif grep -E "480p.mp4" x > /dev/null; then
awk '/480/ {print}' x > x1
elif grep -E "240p.mp4" x > /dev/null; then
awk '/240/ {print}' x > x1
fi
sed 's/\(["]\+\)/\n\1/g' x1 > x2
awk '/videos/ {print}' x2 > x3
echo "#EXTINF:-1," > film
sed -n '3,3p' nazev >> film
cat film | tr -d '\n' >> film.m3u
echo "" >> film.m3u
sed 's/"//g' x3 >> film.m3u
#################################################
adresa1=`sed -n '4,4p' www`
adresa1=$adresa1
curl -Lbk -m 4555 -m 6555 -k  http://online.sktorrent.eu$adresa1 > /tmp/test/x
if grep -E "1080p.mp4" x > /dev/null; then
awk '/1080p/ {print}' x > x1
elif grep -E "720p.mp4" x > /dev/null; then
awk '/720/ {print}' x > x1
elif grep -E "480p.mp4" x > /dev/null; then
awk '/480/ {print}' x > x1
elif grep -E "240p.mp4" x > /dev/null; then
awk '/240/ {print}' x > x1
fi
sed 's/\(["]\+\)/\n\1/g' x1 > x2
awk '/videos/ {print}' x2 > x3
echo "#EXTINF:-1," > film
sed -n '4,4p' nazev >> film
cat film | tr -d '\n' >> film.m3u
echo "" >> film.m3u
sed 's/"//g' x3 >> film.m3u
#################################################
adresa1=`sed -n '5,5p' www`
adresa1=$adresa1
curl -Lbk -m 4555 -m 6555 -k  http://online.sktorrent.eu$adresa1 > /tmp/test/x
if grep -E "1080p.mp4" x > /dev/null; then
awk '/1080p/ {print}' x > x1
elif grep -E "720p.mp4" x > /dev/null; then
awk '/720/ {print}' x > x1
elif grep -E "480p.mp4" x > /dev/null; then
awk '/480/ {print}' x > x1
elif grep -E "240p.mp4" x > /dev/null; then
awk '/240/ {print}' x > x1
fi
sed 's/\(["]\+\)/\n\1/g' x1 > x2
awk '/videos/ {print}' x2 > x3
echo "#EXTINF:-1," > film
sed -n '5,5p' nazev >> film
cat film | tr -d '\n' >> film.m3u
echo "" >> film.m3u
sed 's/"//g' x3 >> film.m3u
#################################################
adresa1=`sed -n '6,6p' www`
adresa1=$adresa1
curl -Lbk -m 4555 -m 6555 -k  http://online.sktorrent.eu$adresa1 > /tmp/test/x
if grep -E "1080p.mp4" x > /dev/null; then
awk '/1080p/ {print}' x > x1
elif grep -E "720p.mp4" x > /dev/null; then
awk '/720/ {print}' x > x1
elif grep -E "480p.mp4" x > /dev/null; then
awk '/480/ {print}' x > x1
elif grep -E "240p.mp4" x > /dev/null; then
awk '/240/ {print}' x > x1
fi
sed 's/\(["]\+\)/\n\1/g' x1 > x2
awk '/videos/ {print}' x2 > x3
echo "#EXTINF:-1," > film
sed -n '6,6p' nazev >> film
cat film | tr -d '\n' >> film.m3u
echo "" >> film.m3u
sed 's/"//g' x3 >> film.m3u
#################################################
adresa1=`sed -n '7,7p' www`
adresa1=$adresa1
curl -Lbk -m 4555 -m 6555 -k  http://online.sktorrent.eu$adresa1 > /tmp/test/x
if grep -E "1080p.mp4" x > /dev/null; then
awk '/1080p/ {print}' x > x1
elif grep -E "720p.mp4" x > /dev/null; then
awk '/720/ {print}' x > x1
elif grep -E "480p.mp4" x > /dev/null; then
awk '/480/ {print}' x > x1
elif grep -E "240p.mp4" x > /dev/null; then
awk '/240/ {print}' x > x1
fi
sed 's/\(["]\+\)/\n\1/g' x1 > x2
awk '/videos/ {print}' x2 > x3
echo "#EXTINF:-1," > film
sed -n '7,7p' nazev >> film
cat film | tr -d '\n' >> film.m3u
echo "" >> film.m3u
sed 's/"//g' x3 >> film.m3u
#################################################
adresa1=`sed -n '8,8p' www`
adresa1=$adresa1
curl -Lbk -m 4555 -m 6555 -k  http://online.sktorrent.eu$adresa1 > /tmp/test/x
if grep -E "1080p.mp4" x > /dev/null; then
awk '/1080p/ {print}' x > x1
elif grep -E "720p.mp4" x > /dev/null; then
awk '/720/ {print}' x > x1
elif grep -E "480p.mp4" x > /dev/null; then
awk '/480/ {print}' x > x1
elif grep -E "240p.mp4" x > /dev/null; then
awk '/240/ {print}' x > x1
fi
sed 's/\(["]\+\)/\n\1/g' x1 > x2
awk '/videos/ {print}' x2 > x3
echo "#EXTINF:-1," > film
sed -n '8,8p' nazev >> film
cat film | tr -d '\n' >> film.m3u
echo "" >> film.m3u
sed 's/"//g' x3 >> film.m3u
#################################################
adresa1=`sed -n '9,9p' www`
adresa1=$adresa1
curl -Lbk -m 4555 -m 6555 -k  http://online.sktorrent.eu$adresa1 > /tmp/test/x
if grep -E "1080p.mp4" x > /dev/null; then
awk '/1080p/ {print}' x > x1
elif grep -E "720p.mp4" x > /dev/null; then
awk '/720/ {print}' x > x1
elif grep -E "480p.mp4" x > /dev/null; then
awk '/480/ {print}' x > x1
elif grep -E "240p.mp4" x > /dev/null; then
awk '/240/ {print}' x > x1
fi
sed 's/\(["]\+\)/\n\1/g' x1 > x2
awk '/videos/ {print}' x2 > x3
echo "#EXTINF:-1," > film
sed -n '9,9p' nazev >> film
cat film | tr -d '\n' >> film.m3u
echo "" >> film.m3u
sed 's/"//g' x3 >> film.m3u
#################################################
adresa1=`sed -n '10,10p' www`
adresa1=$adresa1
curl -Lbk -m 4555 -m 6555 -k  http://online.sktorrent.eu$adresa1 > /tmp/test/x
if grep -E "1080p.mp4" x > /dev/null; then
awk '/1080p/ {print}' x > x1
elif grep -E "720p.mp4" x > /dev/null; then
awk '/720/ {print}' x > x1
elif grep -E "480p.mp4" x > /dev/null; then
awk '/480/ {print}' x > x1
elif grep -E "240p.mp4" x > /dev/null; then
awk '/240/ {print}' x > x1
fi
sed 's/\(["]\+\)/\n\1/g' x1 > x2
awk '/videos/ {print}' x2 > x3
echo "#EXTINF:-1," > film
sed -n '10,10p' nazev >> film
cat film | tr -d '\n' >> film.m3u
echo "" >> film.m3u
sed 's/"//g' x3 >> film.m3u
#################################################
adresa1=`sed -n '11,11p' www`
adresa1=$adresa1
curl -Lbk -m 4555 -m 6555 -k  http://online.sktorrent.eu$adresa1 > /tmp/test/x
if grep -E "1080p.mp4" x > /dev/null; then
awk '/1080p/ {print}' x > x1
elif grep -E "720p.mp4" x > /dev/null; then
awk '/720/ {print}' x > x1
elif grep -E "480p.mp4" x > /dev/null; then
awk '/480/ {print}' x > x1
elif grep -E "240p.mp4" x > /dev/null; then
awk '/240/ {print}' x > x1
fi
sed 's/\(["]\+\)/\n\1/g' x1 > x2
awk '/videos/ {print}' x2 > x3
echo "#EXTINF:-1," > film
sed -n '11,11p' nazev >> film
cat film | tr -d '\n' >> film.m3u
echo "" >> film.m3u
sed 's/"//g' x3 >> film.m3u
#################################################
adresa1=`sed -n '12,12p' www`
adresa1=$adresa1
curl -Lbk -m 4555 -m 6555 -k  http://online.sktorrent.eu$adresa1 > /tmp/test/x
if grep -E "1080p.mp4" x > /dev/null; then
awk '/1080p/ {print}' x > x1
elif grep -E "720p.mp4" x > /dev/null; then
awk '/720/ {print}' x > x1
elif grep -E "480p.mp4" x > /dev/null; then
awk '/480/ {print}' x > x1
elif grep -E "240p.mp4" x > /dev/null; then
awk '/240/ {print}' x > x1
fi
sed 's/\(["]\+\)/\n\1/g' x1 > x2
awk '/videos/ {print}' x2 > x3
echo "#EXTINF:-1," > film
sed -n '12,12p' nazev >> film
cat film | tr -d '\n' >> film.m3u
echo "" >> film.m3u
sed 's/"//g' x3 >> film.m3u
#################################################
adresa1=`sed -n '13,13p' www`
adresa1=$adresa1
curl -Lbk -m 4555 -m 6555 -k  http://online.sktorrent.eu$adresa1 > /tmp/test/x
if grep -E "1080p.mp4" x > /dev/null; then
awk '/1080p/ {print}' x > x1
elif grep -E "720p.mp4" x > /dev/null; then
awk '/720/ {print}' x > x1
elif grep -E "480p.mp4" x > /dev/null; then
awk '/480/ {print}' x > x1
elif grep -E "240p.mp4" x > /dev/null; then
awk '/240/ {print}' x > x1
fi
sed 's/\(["]\+\)/\n\1/g' x1 > x2
awk '/videos/ {print}' x2 > x3
echo "#EXTINF:-1," > film
sed -n '13,13p' nazev >> film
cat film | tr -d '\n' >> film.m3u
echo "" >> film.m3u
sed 's/"//g' x3 >> film.m3u
#################################################
adresa1=`sed -n '14,14p' www`
adresa1=$adresa1
curl -Lbk -m 4555 -m 6555 -k  http://online.sktorrent.eu$adresa1 > /tmp/test/x
if grep -E "1080p.mp4" x > /dev/null; then
awk '/1080p/ {print}' x > x1
elif grep -E "720p.mp4" x > /dev/null; then
awk '/720/ {print}' x > x1
elif grep -E "480p.mp4" x > /dev/null; then
awk '/480/ {print}' x > x1
elif grep -E "240p.mp4" x > /dev/null; then
awk '/240/ {print}' x > x1
fi
sed 's/\(["]\+\)/\n\1/g' x1 > x2
awk '/videos/ {print}' x2 > x3
echo "#EXTINF:-1," > film
sed -n '14,14p' nazev >> film
cat film | tr -d '\n' >> film.m3u
echo "" >> film.m3u
sed 's/"//g' x3 >> film.m3u
#################################################
adresa1=`sed -n '15,15p' www`
adresa1=$adresa1
curl -Lbk -m 4555 -m 6555 -k  http://online.sktorrent.eu$adresa1 > /tmp/test/x
if grep -E "1080p.mp4" x > /dev/null; then
awk '/1080p/ {print}' x > x1
elif grep -E "720p.mp4" x > /dev/null; then
awk '/720/ {print}' x > x1
elif grep -E "480p.mp4" x > /dev/null; then
awk '/480/ {print}' x > x1
elif grep -E "240p.mp4" x > /dev/null; then
awk '/240/ {print}' x > x1
fi
sed 's/\(["]\+\)/\n\1/g' x1 > x2
awk '/videos/ {print}' x2 > x3
echo "#EXTINF:-1," > film
sed -n '15,15p' nazev >> film
cat film | tr -d '\n' >> film.m3u
echo "" >> film.m3u
sed 's/"//g' x3 >> film.m3u
#################################################
adresa1=`sed -n '16,16p' www`
adresa1=$adresa1
curl -Lbk -m 4555 -m 6555 -k  http://online.sktorrent.eu$adresa1 > /tmp/test/x
if grep -E "1080p.mp4" x > /dev/null; then
awk '/1080p/ {print}' x > x1
elif grep -E "720p.mp4" x > /dev/null; then
awk '/720/ {print}' x > x1
elif grep -E "480p.mp4" x > /dev/null; then
awk '/480/ {print}' x > x1
elif grep -E "240p.mp4" x > /dev/null; then
awk '/240/ {print}' x > x1
fi
sed 's/\(["]\+\)/\n\1/g' x1 > x2
awk '/videos/ {print}' x2 > x3
echo "#EXTINF:-1," > film
sed -n '16,16p' nazev >> film
cat film | tr -d '\n' >> film.m3u
echo "" >> film.m3u
sed 's/"//g' x3 >> film.m3u
#################################################
adresa1=`sed -n '17,17p' www`
adresa1=$adresa1
curl -Lbk -m 4555 -m 6555 -k  http://online.sktorrent.eu$adresa1 > /tmp/test/x
if grep -E "1080p.mp4" x > /dev/null; then
awk '/1080p/ {print}' x > x1
elif grep -E "720p.mp4" x > /dev/null; then
awk '/720/ {print}' x > x1
elif grep -E "480p.mp4" x > /dev/null; then
awk '/480/ {print}' x > x1
elif grep -E "240p.mp4" x > /dev/null; then
awk '/240/ {print}' x > x1
fi
sed 's/\(["]\+\)/\n\1/g' x1 > x2
awk '/videos/ {print}' x2 > x3
echo "#EXTINF:-1," > film
sed -n '17,17p' nazev >> film
cat film | tr -d '\n' >> film.m3u
echo "" >> film.m3u
sed 's/"//g' x3 >> film.m3u
#################################################
adresa1=`sed -n '18,18p' www`
adresa1=$adresa1
curl -Lbk -m 4555 -m 6555 -k  http://online.sktorrent.eu$adresa1 > /tmp/test/x
if grep -E "1080p.mp4" x > /dev/null; then
awk '/1080p/ {print}' x > x1
elif grep -E "720p.mp4" x > /dev/null; then
awk '/720/ {print}' x > x1
elif grep -E "480p.mp4" x > /dev/null; then
awk '/480/ {print}' x > x1
elif grep -E "240p.mp4" x > /dev/null; then
awk '/240/ {print}' x > x1
fi
sed 's/\(["]\+\)/\n\1/g' x1 > x2
awk '/videos/ {print}' x2 > x3
echo "#EXTINF:-1," > film
sed -n '18,18p' nazev >> film
cat film | tr -d '\n' >> film.m3u
echo "" >> film.m3u
sed 's/"//g' x3 >> film.m3u
#################################################
adresa1=`sed -n '19,19p' www`
adresa1=$adresa1
curl -Lbk -m 4555 -m 6555 -k  http://online.sktorrent.eu$adresa1 > /tmp/test/x
if grep -E "1080p.mp4" x > /dev/null; then
awk '/1080p/ {print}' x > x1
elif grep -E "720p.mp4" x > /dev/null; then
awk '/720/ {print}' x > x1
elif grep -E "480p.mp4" x > /dev/null; then
awk '/480/ {print}' x > x1
elif grep -E "240p.mp4" x > /dev/null; then
awk '/240/ {print}' x > x1
fi
sed 's/\(["]\+\)/\n\1/g' x1 > x2
awk '/videos/ {print}' x2 > x3
echo "#EXTINF:-1," > film
sed -n '19,19p' nazev >> film
cat film | tr -d '\n' >> film.m3u
echo "" >> film.m3u
sed 's/"//g' x3 >> film.m3u
#################################################
adresa1=`sed -n '20,20p' www`
adresa1=$adresa1
curl -Lbk -m 4555 -m 6555 -k  http://online.sktorrent.eu$adresa1 > /tmp/test/x
if grep -E "1080p.mp4" x > /dev/null; then
awk '/1080p/ {print}' x > x1
elif grep -E "720p.mp4" x > /dev/null; then
awk '/720/ {print}' x > x1
elif grep -E "480p.mp4" x > /dev/null; then
awk '/480/ {print}' x > x1
elif grep -E "240p.mp4" x > /dev/null; then
awk '/240/ {print}' x > x1
fi
sed 's/\(["]\+\)/\n\1/g' x1 > x2
awk '/videos/ {print}' x2 > x3
echo "#EXTINF:-1," > film
sed -n '20,20p' nazev >> film
cat film | tr -d '\n' >> film.m3u
echo "" >> film.m3u
sed 's/"//g' x3 >> film.m3u
#################################################
adresa1=`sed -n '21,21p' www`
adresa1=$adresa1
curl -Lbk -m 4555 -m 6555 -k  http://online.sktorrent.eu$adresa1 > /tmp/test/x
if grep -E "1080p.mp4" x > /dev/null; then
awk '/1080p/ {print}' x > x1
elif grep -E "720p.mp4" x > /dev/null; then
awk '/720/ {print}' x > x1
elif grep -E "480p.mp4" x > /dev/null; then
awk '/480/ {print}' x > x1
elif grep -E "240p.mp4" x > /dev/null; then
awk '/240/ {print}' x > x1
fi
sed 's/\(["]\+\)/\n\1/g' x1 > x2
awk '/videos/ {print}' x2 > x3
echo "#EXTINF:-1," > film
sed -n '21,21p' nazev >> film
cat film | tr -d '\n' >> film.m3u
echo "" >> film.m3u
sed 's/"//g' x3 >> film.m3u
#################################################
adresa1=`sed -n '22,22p' www`
adresa1=$adresa1
curl -Lbk -m 4555 -m 6555 -k  http://online.sktorrent.eu$adresa1 > /tmp/test/x
if grep -E "1080p.mp4" x > /dev/null; then
awk '/1080p/ {print}' x > x1
elif grep -E "720p.mp4" x > /dev/null; then
awk '/720/ {print}' x > x1
elif grep -E "480p.mp4" x > /dev/null; then
awk '/480/ {print}' x > x1
elif grep -E "240p.mp4" x > /dev/null; then
awk '/240/ {print}' x > x1
fi
sed 's/\(["]\+\)/\n\1/g' x1 > x2
awk '/videos/ {print}' x2 > x3
echo "#EXTINF:-1," > film
sed -n '12,12p' nazev >> film
cat film | tr -d '\n' >> film.m3u
echo "" >> film.m3u
sed 's/"//g' x3 >> film.m3u
#################################################
adresa1=`sed -n '23,23p' www`
adresa1=$adresa1
curl -Lbk -m 4555 -m 6555 -k  http://online.sktorrent.eu$adresa1 > /tmp/test/x
if grep -E "1080p.mp4" x > /dev/null; then
awk '/1080p/ {print}' x > x1
elif grep -E "720p.mp4" x > /dev/null; then
awk '/720/ {print}' x > x1
elif grep -E "480p.mp4" x > /dev/null; then
awk '/480/ {print}' x > x1
elif grep -E "240p.mp4" x > /dev/null; then
awk '/240/ {print}' x > x1
fi
sed 's/\(["]\+\)/\n\1/g' x1 > x2
awk '/videos/ {print}' x2 > x3
echo "#EXTINF:-1," > film
sed -n '23,23p' nazev >> film
cat film | tr -d '\n' >> film.m3u
echo "" >> film.m3u
sed 's/"//g' x3 >> film.m3u
#################################################
adresa1=`sed -n '24,24p' www`
adresa1=$adresa1
curl -Lbk -m 4555 -m 6555 -k  http://online.sktorrent.eu$adresa1 > /tmp/test/x
if grep -E "1080p.mp4" x > /dev/null; then
awk '/1080p/ {print}' x > x1
elif grep -E "720p.mp4" x > /dev/null; then
awk '/720/ {print}' x > x1
elif grep -E "480p.mp4" x > /dev/null; then
awk '/480/ {print}' x > x1
elif grep -E "240p.mp4" x > /dev/null; then
awk '/240/ {print}' x > x1
fi
sed 's/\(["]\+\)/\n\1/g' x1 > x2
awk '/videos/ {print}' x2 > x3
echo "#EXTINF:-1," > film
sed -n '24,24p' nazev >> film
cat film | tr -d '\n' >> film.m3u
echo "" >> film.m3u
sed 's/"//g' x3 >> film.m3u
#################################################
adresa1=`sed -n '25,25p' www`
adresa1=$adresa1
curl -Lbk -m 4555 -m 6555 -k  http://online.sktorrent.eu$adresa1 > /tmp/test/x
if grep -E "1080p.mp4" x > /dev/null; then
awk '/1080p/ {print}' x > x1
elif grep -E "720p.mp4" x > /dev/null; then
awk '/720/ {print}' x > x1
elif grep -E "480p.mp4" x > /dev/null; then
awk '/480/ {print}' x > x1
elif grep -E "240p.mp4" x > /dev/null; then
awk '/240/ {print}' x > x1
fi
sed 's/\(["]\+\)/\n\1/g' x1 > x2
awk '/videos/ {print}' x2 > x3
echo "#EXTINF:-1," > film
sed -n '25,25p' nazev >> film
cat film | tr -d '\n' >> film.m3u
echo "" >> film.m3u
sed 's/"//g' x3 >> film.m3u
#################################################
adresa1=`sed -n '26,26p' www`
adresa1=$adresa1
curl -Lbk -m 4555 -m 6555 -k  http://online.sktorrent.eu$adresa1 > /tmp/test/x
if grep -E "1080p.mp4" x > /dev/null; then
awk '/1080p/ {print}' x > x1
elif grep -E "720p.mp4" x > /dev/null; then
awk '/720/ {print}' x > x1
elif grep -E "480p.mp4" x > /dev/null; then
awk '/480/ {print}' x > x1
elif grep -E "240p.mp4" x > /dev/null; then
awk '/240/ {print}' x > x1
fi
sed 's/\(["]\+\)/\n\1/g' x1 > x2
awk '/videos/ {print}' x2 > x3
echo "#EXTINF:-1," > film
sed -n '26,26p' nazev >> film
cat film | tr -d '\n' >> film.m3u
echo "" >> film.m3u
sed 's/"//g' x3 >> film.m3u
#################################################
adresa1=`sed -n '27,27p' www`
adresa1=$adresa1
curl -Lbk -m 4555 -m 6555 -k  http://online.sktorrent.eu$adresa1 > /tmp/test/x
if grep -E "1080p.mp4" x > /dev/null; then
awk '/1080p/ {print}' x > x1
elif grep -E "720p.mp4" x > /dev/null; then
awk '/720/ {print}' x > x1
elif grep -E "480p.mp4" x > /dev/null; then
awk '/480/ {print}' x > x1
elif grep -E "240p.mp4" x > /dev/null; then
awk '/240/ {print}' x > x1
fi
sed 's/\(["]\+\)/\n\1/g' x1 > x2
awk '/videos/ {print}' x2 > x3
echo "#EXTINF:-1," > film
sed -n '27,27p' nazev >> film
cat film | tr -d '\n' >> film.m3u
echo "" >> film.m3u
sed 's/"//g' x3 >> film.m3u
#################################################
adresa1=`sed -n '28,28p' www`
adresa1=$adresa1
curl -Lbk -m 4555 -m 6555 -k  http://online.sktorrent.eu$adresa1 > /tmp/test/x
if grep -E "1080p.mp4" x > /dev/null; then
awk '/1080p/ {print}' x > x1
elif grep -E "720p.mp4" x > /dev/null; then
awk '/720/ {print}' x > x1
elif grep -E "480p.mp4" x > /dev/null; then
awk '/480/ {print}' x > x1
elif grep -E "240p.mp4" x > /dev/null; then
awk '/240/ {print}' x > x1
fi
sed 's/\(["]\+\)/\n\1/g' x1 > x2
awk '/videos/ {print}' x2 > x3
echo "#EXTINF:-1," > film
sed -n '28,28p' nazev >> film
cat film | tr -d '\n' >> film.m3u
echo "" >> film.m3u
sed 's/"//g' x3 >> film.m3u
#################################################
adresa1=`sed -n '29,29p' www`
adresa1=$adresa1
curl -Lbk -m 4555 -m 6555 -k  http://online.sktorrent.eu$adresa1 > /tmp/test/x
if grep -E "1080p.mp4" x > /dev/null; then
awk '/1080p/ {print}' x > x1
elif grep -E "720p.mp4" x > /dev/null; then
awk '/720/ {print}' x > x1
elif grep -E "480p.mp4" x > /dev/null; then
awk '/480/ {print}' x > x1
elif grep -E "240p.mp4" x > /dev/null; then
awk '/240/ {print}' x > x1
fi
sed 's/\(["]\+\)/\n\1/g' x1 > x2
awk '/videos/ {print}' x2 > x3
echo "#EXTINF:-1," > film
sed -n '29,29p' nazev >> film
cat film | tr -d '\n' >> film.m3u
echo "" >> film.m3u
sed 's/"//g' x3 >> film.m3u
#################################################
adresa1=`sed -n '30,30p' www`
adresa1=$adresa1
curl -Lbk -m 4555 -m 6555 -k  http://online.sktorrent.eu$adresa1 > /tmp/test/x
if grep -E "1080p.mp4" x > /dev/null; then
awk '/1080p/ {print}' x > x1
elif grep -E "720p.mp4" x > /dev/null; then
awk '/720/ {print}' x > x1
elif grep -E "480p.mp4" x > /dev/null; then
awk '/480/ {print}' x > x1
elif grep -E "240p.mp4" x > /dev/null; then
awk '/240/ {print}' x > x1
fi
sed 's/\(["]\+\)/\n\1/g' x1 > x2
awk '/videos/ {print}' x2 > x3
echo "#EXTINF:-1," > film
sed -n '30,30p' nazev >> film
cat film | tr -d '\n' >> film.m3u
echo "" >> film.m3u
sed 's/"//g' x3 >> film.m3u
#################################################
adresa1=`sed -n '31,31p' www`
adresa1=$adresa1
curl -Lbk -m 4555 -m 6555 -k  http://online.sktorrent.eu$adresa1 > /tmp/test/x
if grep -E "1080p.mp4" x > /dev/null; then
awk '/1080p/ {print}' x > x1
elif grep -E "720p.mp4" x > /dev/null; then
awk '/720/ {print}' x > x1
elif grep -E "480p.mp4" x > /dev/null; then
awk '/480/ {print}' x > x1
elif grep -E "240p.mp4" x > /dev/null; then
awk '/240/ {print}' x > x1
fi
sed 's/\(["]\+\)/\n\1/g' x1 > x2
awk '/videos/ {print}' x2 > x3
echo "#EXTINF:-1," > film
sed -n '31,31p' nazev >> film
cat film | tr -d '\n' >> film.m3u
echo "" >> film.m3u
sed 's/"//g' x3 >> film.m3u
#################################################
adresa1=`sed -n '32,32p' www`
adresa1=$adresa1
curl -Lbk -m 4555 -m 6555 -k  http://online.sktorrent.eu$adresa1 > /tmp/test/x
if grep -E "1080p.mp4" x > /dev/null; then
awk '/1080p/ {print}' x > x1
elif grep -E "720p.mp4" x > /dev/null; then
awk '/720/ {print}' x > x1
elif grep -E "480p.mp4" x > /dev/null; then
awk '/480/ {print}' x > x1
elif grep -E "240p.mp4" x > /dev/null; then
awk '/240/ {print}' x > x1
fi
sed 's/\(["]\+\)/\n\1/g' x1 > x2
awk '/videos/ {print}' x2 > x3
echo "#EXTINF:-1," > film
sed -n '32,32p' nazev >> film
cat film | tr -d '\n' >> film.m3u
echo "" >> film.m3u
sed 's/"//g' x3 >> film.m3u
#################################################
adresa1=`sed -n '33,33p' www`
adresa1=$adresa1
curl -Lbk -m 4555 -m 6555 -k  http://online.sktorrent.eu$adresa1 > /tmp/test/x
if grep -E "1080p.mp4" x > /dev/null; then
awk '/1080p/ {print}' x > x1
elif grep -E "720p.mp4" x > /dev/null; then
awk '/720/ {print}' x > x1
elif grep -E "480p.mp4" x > /dev/null; then
awk '/480/ {print}' x > x1
elif grep -E "240p.mp4" x > /dev/null; then
awk '/240/ {print}' x > x1
fi
sed 's/\(["]\+\)/\n\1/g' x1 > x2
awk '/videos/ {print}' x2 > x3
echo "#EXTINF:-1," > film
sed -n '33,33p' nazev >> film
cat film | tr -d '\n' >> film.m3u
echo "" >> film.m3u
sed 's/"//g' x3 >> film.m3u
#################################################
adresa1=`sed -n '34,34p' www`
adresa1=$adresa1
curl -Lbk -m 4555 -m 6555 -k  http://online.sktorrent.eu$adresa1 > /tmp/test/x
if grep -E "1080p.mp4" x > /dev/null; then
awk '/1080p/ {print}' x > x1
elif grep -E "720p.mp4" x > /dev/null; then
awk '/720/ {print}' x > x1
elif grep -E "480p.mp4" x > /dev/null; then
awk '/480/ {print}' x > x1
elif grep -E "240p.mp4" x > /dev/null; then
awk '/240/ {print}' x > x1
fi
sed 's/\(["]\+\)/\n\1/g' x1 > x2
awk '/videos/ {print}' x2 > x3
echo "#EXTINF:-1," > film
sed -n '34,34p' nazev >> film
cat film | tr -d '\n' >> film.m3u
echo "" >> film.m3u
sed 's/"//g' x3 >> film.m3u
#################################################
adresa1=`sed -n '35,35p' www`
adresa1=$adresa1
curl -Lbk -m 4555 -m 6555 -k  http://online.sktorrent.eu$adresa1 > /tmp/test/x
if grep -E "1080p.mp4" x > /dev/null; then
awk '/1080p/ {print}' x > x1
elif grep -E "720p.mp4" x > /dev/null; then
awk '/720/ {print}' x > x1
elif grep -E "480p.mp4" x > /dev/null; then
awk '/480/ {print}' x > x1
elif grep -E "240p.mp4" x > /dev/null; then
awk '/240/ {print}' x > x1
fi
sed 's/\(["]\+\)/\n\1/g' x1 > x2
awk '/videos/ {print}' x2 > x3
echo "#EXTINF:-1," > film
sed -n '35,35p' nazev >> film
cat film | tr -d '\n' >> film.m3u
echo "" >> film.m3u
sed 's/"//g' x3 >> film.m3u
#################################################
adresa1=`sed -n '36,36p' www`
adresa1=$adresa1
curl -Lbk -m 4555 -m 6555 -k  http://online.sktorrent.eu$adresa1 > /tmp/test/x
if grep -E "1080p.mp4" x > /dev/null; then
awk '/1080p/ {print}' x > x1
elif grep -E "720p.mp4" x > /dev/null; then
awk '/720/ {print}' x > x1
elif grep -E "480p.mp4" x > /dev/null; then
awk '/480/ {print}' x > x1
elif grep -E "240p.mp4" x > /dev/null; then
awk '/240/ {print}' x > x1
fi
sed 's/\(["]\+\)/\n\1/g' x1 > x2
awk '/videos/ {print}' x2 > x3
echo "#EXTINF:-1," > film
sed -n '36,36p' nazev >> film
cat film | tr -d '\n' >> film.m3u
echo "" >> film.m3u
sed 's/"//g' x3 >> film.m3u
#################################################
awk '/EXTINF/ {print}''/mp4/ {print}' film.m3u >> /tmp/film.m3u

#################################################
#################################################
cp /tmp/film.m3u /movie/Koncerty72.m3u
cd /
rm -rf /tmp/test
#################################################
[ -d /tmp/test ] || mkdir -p /tmp/test
#################################################
cp /tmp/film.m3u /tmp/test/film.m3u
rm -rf /tmp/film.m3u
#################################################
more /usr/lib/enigma2/python/Plugins/Extensions/OpenPanel/DATA/x  >> /etc/enigma2/bouquets.tv 
sed -i "s/%/userbouquet.Koncerty72.m3u.tv/" /etc/enigma2/bouquets.tv 

awk 'BEGIN {FS="png"}{print  $NF}'  /tmp/test/film.m3u > /tmp/test/Rus3.m3u
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
echo "#NAME Koncerty72.m3u" > /etc/enigma2/userbouquet.Koncerty72.m3u.tv
cat /tmp/test/Rus10.m3u >> /etc/enigma2/userbouquet.Koncerty72.m3u.tv
rm -rf /tmp/test
cd /
wget -q -O - http://root%s@127.0.0.1/web/servicelistreload?mode=0 >>/dev/null 2>&1 </dev/null &
sleep 2
echo "OK"
exit
