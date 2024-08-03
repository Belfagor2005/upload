#!/bin/sh
sleep 1
echo "stahuji stream list SKTonline"
sleep 2
[ -d /movie ] || mkdir -p /movie
#################################################

#################################################
[ -d /tmp/test ] || mkdir -p /tmp/test

#################################################
curl  -k -Lbk -m 55532 -m 555104 "http://online.sktorrent.eu/videos/filmy-cz-sk?o=mv" > /tmp/test/a
grep -o -i '<a href="/video/[^<]*' /tmp/test/a > /tmp/test/a1
curl  -k -Lbk -m 55532 -m 555104 "http://online.sktorrent.eu/videos/filmy-cz-sk?o=mv&page=2" > /tmp/test/b
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
curl  -k -Lbk -m 55532 -m 555104 "http://online.sktorrent.eu/videos/filmy-cz-sk?o=mv&page=3" > /tmp/test/a
grep -o -i '<a href="/video/[^<]*' /tmp/test/a > /tmp/test/a1
curl  -k -Lbk -m 55532 -m 555104 "http://online.sktorrent.eu/videos/filmy-cz-sk?o=mv&page=4" > /tmp/test/b
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
cd /
rm -rf /tmp/test                                                          1
##################################################################################################  
#################################################
[ -d /tmp/test ] || mkdir -p /tmp/test

#################################################
curl  -k -Lbk -m 55532 -m 555104 "http://online.sktorrent.eu/videos/filmy-cz-sk?o=mv&page=5" > /tmp/test/a
grep -o -i '<a href="/video/[^<]*' /tmp/test/a > /tmp/test/a1
curl  -k -Lbk -m 55532 -m 555104 "http://online.sktorrent.eu/videos/filmy-cz-sk?o=mv&page=6" > /tmp/test/b
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
cd /
rm -rf /tmp/test


[ -d /tmp/test ] || mkdir -p /tmp/test

#################################################
curl  -k -Lbk -m 55532 -m 555104 "http://online.sktorrent.eu/videos/filmy-cz-sk?o=mv&page=7" > /tmp/test/a
grep -o -i '<a href="/video/[^<]*' /tmp/test/a > /tmp/test/a1
curl  -k -Lbk -m 55532 -m 555104 "http://online.sktorrent.eu/videos/filmy-cz-sk?o=mv&page=8" > /tmp/test/b
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
cd /
rm -rf /tmp/test                                                          2
##################################################################################################  
#################################################
[ -d /tmp/test ] || mkdir -p /tmp/test

#################################################
curl  -k -Lbk -m 55532 -m 555104 "http://online.sktorrent.eu/videos/filmy-cz-sk?o=mv&page=9" > /tmp/test/a
grep -o -i '<a href="/video/[^<]*' /tmp/test/a > /tmp/test/a1
curl  -k -Lbk -m 55532 -m 555104 "http://online.sktorrent.eu/videos/filmy-cz-sk?o=mv&page=10" > /tmp/test/b
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
cd /
rm -rf /tmp/test


[ -d /tmp/test ] || mkdir -p /tmp/test

#################################################
curl  -k -Lbk -m 55532 -m 555104 "http://online.sktorrent.eu/videos/filmy-cz-sk?o=mv&page=11" > /tmp/test/a
grep -o -i '<a href="/video/[^<]*' /tmp/test/a > /tmp/test/a1
curl  -k -Lbk -m 55532 -m 555104 "http://online.sktorrent.eu/videos/filmy-cz-sk?o=mv&page=12" > /tmp/test/b
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
cd /
rm -rf /tmp/test                                                          3
##################################################################################################  
#################################################
[ -d /tmp/test ] || mkdir -p /tmp/test

#################################################
curl  -k -Lbk -m 55532 -m 555104 "http://online.sktorrent.eu/videos/filmy-cz-sk?o=mv&page=13" > /tmp/test/a
grep -o -i '<a href="/video/[^<]*' /tmp/test/a > /tmp/test/a1
curl  -k -Lbk -m 55532 -m 555104 "http://online.sktorrent.eu/videos/filmy-cz-sk?o=mv&page=14" > /tmp/test/b
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
cd /
rm -rf /tmp/test


[ -d /tmp/test ] || mkdir -p /tmp/test

#################################################
curl  -k -Lbk -m 55532 -m 555104 "http://online.sktorrent.eu/videos/filmy-cz-sk?o=mv&page=15" > /tmp/test/a
grep -o -i '<a href="/video/[^<]*' /tmp/test/a > /tmp/test/a1
curl  -k -Lbk -m 55532 -m 555104 "http://online.sktorrent.eu/videos/filmy-cz-sk?o=mv&page=16" > /tmp/test/b
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
cp /tmp/film.m3u /movie/SkTonline288.m3u
cd /
rm -rf /tmp/film.m3u
rm -rf /tmp/test                                                          4
################################################################################################## 
echo "OK"
exit 









