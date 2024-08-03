#!/bin/sh
sleep 1
echo "stahuji stream list pro PLUGIN ...XXX Films"
sleep 1
echo ""
echo "download stream sheet for PLUGIN ...XXX Films"
sleep 2
echo ""
#################################################

#################################################
[ -d /tmp/test ] || mkdir -p /tmp/test
[ -d /tmp/test2 ] || mkdir -p /tmp/test2
#################################################
cat /usr/lib/enigma2/python/Plugins/Extensions/StreamTvPlayerFHD/x > /tmp/test/stream.xml
cp /tmp/test/stream.xml /tmp/test2/stream.xml
curl -Lbk -m 4555 -m 6555 -k  https://www.redtube.com/channels/blacked > /tmp/test/x1
cd /tmp/test
grep -o -i 'img_rel_videos[^<]*' x1 > x2
sed 's/img_rel_videos//g' x2 > x3
sed 's/"//g' x3 > www
adresa1=`sed -n '1,1p' www`
adresa1=$adresa1
curl -Lbk -m 4555 -m 6555 -k  https://www.redtube.com/$adresa1 > /tmp/test/x1
cd /tmp/test
awk '/720/ {print}' x1 > x2
sed 's/\(["]\+\)/\n\1/g' x2 > x3
grep -E "(720P_1500K|720p_1500k)" x3 > x4
tr -d '[\]' < "x4" > x5
sed -n '1,1p' x5 > seznam
awk '/<h1 class="video_title">/ {print}' x1 >> seznam
#################################################
adresa1=`sed -n '2,2p' www`
adresa1=$adresa1
curl -Lbk -m 4555 -m 6555 -k  https://www.redtube.com/$adresa1 > /tmp/test/x1
cd /tmp/test
awk '/720/ {print}' x1 > x2
sed 's/\(["]\+\)/\n\1/g' x2 > x3
grep -E "(720P_1500K|720p_1500k)" x3 > x4
tr -d '[\]' < "x4" > x5
sed -n '1,1p' x5 >> seznam
awk '/<h1 class="video_title">/ {print}' x1 >> seznam
#################################################
adresa1=`sed -n '3,3p' www`
adresa1=$adresa1
curl -Lbk -m 4555 -m 6555 -k  https://www.redtube.com/$adresa1 > /tmp/test/x1
cd /tmp/test
awk '/720/ {print}' x1 > x2
sed 's/\(["]\+\)/\n\1/g' x2 > x3
grep -E "(720P_1500K|720p_1500k)" x3 > x4
tr -d '[\]' < "x4" > x5
sed -n '1,1p' x5 >> seznam
awk '/<h1 class="video_title">/ {print}' x1 >> seznam
#################################################
adresa1=`sed -n '4,4p' www`
adresa1=$adresa1
curl -Lbk -m 4555 -m 6555 -k  https://www.redtube.com/$adresa1 > /tmp/test/x1
cd /tmp/test
awk '/720/ {print}' x1 > x2
sed 's/\(["]\+\)/\n\1/g' x2 > x3
grep -E "(720P_1500K|720p_1500k)" x3 > x4
tr -d '[\]' < "x4" > x5
sed -n '1,1p' x5 >> seznam
awk '/<h1 class="video_title">/ {print}' x1 >> seznam
#################################################
adresa1=`sed -n '5,5p' www`
adresa1=$adresa1
curl -Lbk -m 4555 -m 6555 -k  https://www.redtube.com/$adresa1 > /tmp/test/x1
cd /tmp/test
awk '/720/ {print}' x1 > x2
sed 's/\(["]\+\)/\n\1/g' x2 > x3
grep -E "(720P_1500K|720p_1500k)" x3 > x4
tr -d '[\]' < "x4" > x5
sed -n '1,1p' x5 >> seznam
awk '/<h1 class="video_title">/ {print}' x1 >> seznam
#################################################
tr -d '["]' < "seznam" > seznam1
grep -o -i 'http[^<]*' seznam1 > adresa
grep -o -i 'title>[^<]*' seznam1 > seznam2
sed 's/title>//g' seznam2 > nazev
sed -i "s#&#@#g" adresa
#################################################
adresax1=`sed -n '1,1p' nazev`
adresax1=$adresax1
sed -i "s#N1#$adresax1#g" /tmp/test/stream.xml 
adresax2=`sed -n '2,2p' nazev`
adresax2=$adresax2
sed -i "s#N2#$adresax2#g" /tmp/test/stream.xml 
adresax3=`sed -n '3,3p' nazev`
adresax3=$adresax3
sed -i "s#N3#$adresax3#g" /tmp/test/stream.xml 
adresax4=`sed -n '4,4p' nazev`
adresax4=$adresax4
sed -i "s#N4#$adresax4#g" /tmp/test/stream.xml 
adresax5=`sed -n '5,5p' nazev`
adresax5=$adresax5
sed -i "s#N5#$adresax5#g" /tmp/test/stream.xml 
#################################################
nazevx1=`sed -n '1,1p' adresa`
nazevx1=$nazevx1
sed -i "s#X1#$nazevx1#g" /tmp/test/stream.xml 
nazevx2=`sed -n '2,2p' adresa`
nazevx2=$nazevx2
sed -i "s#X2#$nazevx2#g" /tmp/test/stream.xml 
nazevx3=`sed -n '3,3p' adresa`
nazevx3=$nazevx3
sed -i "s#X3#$nazevx3#g" /tmp/test/stream.xml 
nazevx4=`sed -n '4,4p' adresa`
nazevx4=$nazevx4
sed -i "s#X4#$nazevx4#g" /tmp/test/stream.xml 
nazevx5=`sed -n '5,5p' adresa`
nazevx5=$nazevx5
sed -i "s#X5#$nazevx5#g" /tmp/test/stream.xml
#################################################

sed -n '1,42p' /tmp/test/stream.xml > /tmp/test2/stream1.xml
cd /
rm -rf /tmp/test
##################################################################################################
[ -d /tmp/test ] || mkdir -p /tmp/test
curl -Lbk -m 4555 -m 6555 -k  https://www.redtube.com/channels/blackedraw > /tmp/test/x1
cp /tmp/test2/stream.xml /tmp/test/stream.xml
cd /tmp/test
grep -o -i 'img_rel_videos[^<]*' x1 > x2
sed 's/img_rel_videos//g' x2 > x3
sed 's/"//g' x3 > www
adresa1=`sed -n '1,1p' www`
adresa1=$adresa1
curl -Lbk -m 4555 -m 6555 -k  https://www.redtube.com/$adresa1 > /tmp/test/x1
cd /tmp/test
awk '/720/ {print}' x1 > x2
sed 's/\(["]\+\)/\n\1/g' x2 > x3
grep -E "(720P_1500K|720p_1500k)" x3 > x4
tr -d '[\]' < "x4" > x5
sed -n '1,1p' x5 > seznam
awk '/<h1 class="video_title">/ {print}' x1 >> seznam
#################################################
adresa1=`sed -n '2,2p' www`
adresa1=$adresa1
curl -Lbk -m 4555 -m 6555 -k  https://www.redtube.com/$adresa1 > /tmp/test/x1
cd /tmp/test
awk '/720/ {print}' x1 > x2
sed 's/\(["]\+\)/\n\1/g' x2 > x3
grep -E "(720P_1500K|720p_1500k)" x3 > x4
tr -d '[\]' < "x4" > x5
sed -n '1,1p' x5 >> seznam
awk '/<h1 class="video_title">/ {print}' x1 >> seznam
#################################################
adresa1=`sed -n '3,3p' www`
adresa1=$adresa1
curl -Lbk -m 4555 -m 6555 -k  https://www.redtube.com/$adresa1 > /tmp/test/x1
cd /tmp/test
awk '/720/ {print}' x1 > x2
sed 's/\(["]\+\)/\n\1/g' x2 > x3
grep -E "(720P_1500K|720p_1500k)" x3 > x4
tr -d '[\]' < "x4" > x5
sed -n '1,1p' x5 >> seznam
awk '/<h1 class="video_title">/ {print}' x1 >> seznam
#################################################
adresa1=`sed -n '4,4p' www`
adresa1=$adresa1
curl -Lbk -m 4555 -m 6555 -k  https://www.redtube.com/$adresa1 > /tmp/test/x1
cd /tmp/test
awk '/720/ {print}' x1 > x2
sed 's/\(["]\+\)/\n\1/g' x2 > x3
grep -E "(720P_1500K|720p_1500k)" x3 > x4
tr -d '[\]' < "x4" > x5
sed -n '1,1p' x5 >> seznam
awk '/<h1 class="video_title">/ {print}' x1 >> seznam
#################################################
adresa1=`sed -n '5,5p' www`
adresa1=$adresa1
curl -Lbk -m 4555 -m 6555 -k  https://www.redtube.com/$adresa1 > /tmp/test/x1
cd /tmp/test
awk '/720/ {print}' x1 > x2
sed 's/\(["]\+\)/\n\1/g' x2 > x3
grep -E "(720P_1500K|720p_1500k)" x3 > x4
tr -d '[\]' < "x4" > x5
sed -n '1,1p' x5 >> seznam
awk '/<h1 class="video_title">/ {print}' x1 >> seznam
#################################################
tr -d '["]' < "seznam" > seznam1
grep -o -i 'http[^<]*' seznam1 > adresa
grep -o -i 'title>[^<]*' seznam1 > seznam2
sed 's/title>//g' seznam2 > nazev
sed -i "s#&#@#g" adresa
#################################################
adresax1=`sed -n '1,1p' nazev`
adresax1=$adresax1
sed -i "s#N1#$adresax1#g" /tmp/test/stream.xml 
adresax2=`sed -n '2,2p' nazev`
adresax2=$adresax2
sed -i "s#N2#$adresax2#g" /tmp/test/stream.xml 
adresax3=`sed -n '3,3p' nazev`
adresax3=$adresax3
sed -i "s#N3#$adresax3#g" /tmp/test/stream.xml 
adresax4=`sed -n '4,4p' nazev`
adresax4=$adresax4
sed -i "s#N4#$adresax4#g" /tmp/test/stream.xml 
adresax5=`sed -n '5,5p' nazev`
adresax5=$adresax5
sed -i "s#N5#$adresax5#g" /tmp/test/stream.xml 
#################################################
nazevx1=`sed -n '1,1p' adresa`
nazevx1=$nazevx1
sed -i "s#X1#$nazevx1#g" /tmp/test/stream.xml 
nazevx2=`sed -n '2,2p' adresa`
nazevx2=$nazevx2
sed -i "s#X2#$nazevx2#g" /tmp/test/stream.xml 
nazevx3=`sed -n '3,3p' adresa`
nazevx3=$nazevx3
sed -i "s#X3#$nazevx3#g" /tmp/test/stream.xml 
nazevx4=`sed -n '4,4p' adresa`
nazevx4=$nazevx4
sed -i "s#X4#$nazevx4#g" /tmp/test/stream.xml 
nazevx5=`sed -n '5,5p' adresa`
nazevx5=$nazevx5
sed -i "s#X5#$nazevx5#g" /tmp/test/stream.xml
#################################################

sed -i 's/blacked.png/\blackedraw.png/g' /tmp/test/stream.xml
sed -i 's/Blacked/\Blacked RAW/g' /tmp/test/stream.xml
sed -n '3,42p' /tmp/test/stream.xml > /tmp/test2/stream2.xml
cd /
rm -rf /tmp/test
##################################################################################################
[ -d /tmp/test ] || mkdir -p /tmp/test
curl -Lbk -m 4555 -m 6555 -k  https://www.redtube.com/channels/castingcouch-hd > /tmp/test/x1
cp /tmp/test2/stream.xml /tmp/test/stream.xml
cd /tmp/test
grep -o -i 'img_rel_videos[^<]*' x1 > x2
sed 's/img_rel_videos//g' x2 > x3
sed 's/"//g' x3 > www
adresa1=`sed -n '1,1p' www`
adresa1=$adresa1
curl -Lbk -m 4555 -m 6555 -k  https://www.redtube.com/$adresa1 > /tmp/test/x1
cd /tmp/test
awk '/720/ {print}' x1 > x2
sed 's/\(["]\+\)/\n\1/g' x2 > x3
grep -E "(720P_1500K|720p_1500k)" x3 > x4
tr -d '[\]' < "x4" > x5
sed -n '1,1p' x5 > seznam
awk '/<h1 class="video_title">/ {print}' x1 >> seznam
#################################################
adresa1=`sed -n '2,2p' www`
adresa1=$adresa1
curl -Lbk -m 4555 -m 6555 -k  https://www.redtube.com/$adresa1 > /tmp/test/x1
cd /tmp/test
awk '/720/ {print}' x1 > x2
sed 's/\(["]\+\)/\n\1/g' x2 > x3
grep -E "(720P_1500K|720p_1500k)" x3 > x4
tr -d '[\]' < "x4" > x5
sed -n '1,1p' x5 >> seznam
awk '/<h1 class="video_title">/ {print}' x1 >> seznam
#################################################
adresa1=`sed -n '3,3p' www`
adresa1=$adresa1
curl -Lbk -m 4555 -m 6555 -k  https://www.redtube.com/$adresa1 > /tmp/test/x1
cd /tmp/test
awk '/720/ {print}' x1 > x2
sed 's/\(["]\+\)/\n\1/g' x2 > x3
grep -E "(720P_1500K|720p_1500k)" x3 > x4
tr -d '[\]' < "x4" > x5
sed -n '1,1p' x5 >> seznam
awk '/<h1 class="video_title">/ {print}' x1 >> seznam
#################################################
adresa1=`sed -n '4,4p' www`
adresa1=$adresa1
curl -Lbk -m 4555 -m 6555 -k  https://www.redtube.com/$adresa1 > /tmp/test/x1
cd /tmp/test
awk '/720/ {print}' x1 > x2
sed 's/\(["]\+\)/\n\1/g' x2 > x3
grep -E "(720P_1500K|720p_1500k)" x3 > x4
tr -d '[\]' < "x4" > x5
sed -n '1,1p' x5 >> seznam
awk '/<h1 class="video_title">/ {print}' x1 >> seznam
#################################################
adresa1=`sed -n '5,5p' www`
adresa1=$adresa1
curl -Lbk -m 4555 -m 6555 -k  https://www.redtube.com/$adresa1 > /tmp/test/x1
cd /tmp/test
awk '/720/ {print}' x1 > x2
sed 's/\(["]\+\)/\n\1/g' x2 > x3
grep -E "(720P_1500K|720p_1500k)" x3 > x4
tr -d '[\]' < "x4" > x5
sed -n '1,1p' x5 >> seznam
awk '/<h1 class="video_title">/ {print}' x1 >> seznam
#################################################
tr -d '["]' < "seznam" > seznam1
grep -o -i 'http[^<]*' seznam1 > adresa
grep -o -i 'title>[^<]*' seznam1 > seznam2
sed 's/title>//g' seznam2 > nazev
sed -i "s#&#@#g" adresa
#################################################
adresax1=`sed -n '1,1p' nazev`
adresax1=$adresax1
sed -i "s#N1#$adresax1#g" /tmp/test/stream.xml 
adresax2=`sed -n '2,2p' nazev`
adresax2=$adresax2
sed -i "s#N2#$adresax2#g" /tmp/test/stream.xml 
adresax3=`sed -n '3,3p' nazev`
adresax3=$adresax3
sed -i "s#N3#$adresax3#g" /tmp/test/stream.xml 
adresax4=`sed -n '4,4p' nazev`
adresax4=$adresax4
sed -i "s#N4#$adresax4#g" /tmp/test/stream.xml 
adresax5=`sed -n '5,5p' nazev`
adresax5=$adresax5
sed -i "s#N5#$adresax5#g" /tmp/test/stream.xml 
#################################################
nazevx1=`sed -n '1,1p' adresa`
nazevx1=$nazevx1
sed -i "s#X1#$nazevx1#g" /tmp/test/stream.xml 
nazevx2=`sed -n '2,2p' adresa`
nazevx2=$nazevx2
sed -i "s#X2#$nazevx2#g" /tmp/test/stream.xml 
nazevx3=`sed -n '3,3p' adresa`
nazevx3=$nazevx3
sed -i "s#X3#$nazevx3#g" /tmp/test/stream.xml 
nazevx4=`sed -n '4,4p' adresa`
nazevx4=$nazevx4
sed -i "s#X4#$nazevx4#g" /tmp/test/stream.xml 
nazevx5=`sed -n '5,5p' adresa`
nazevx5=$nazevx5
sed -i "s#X5#$nazevx5#g" /tmp/test/stream.xml
#################################################
sed -i 's/blacked.png/\casting.png/g' /tmp/test/stream.xml
sed -i 's/Blacked/\Casting Couch/g' /tmp/test/stream.xml
sed -n '3,42p' /tmp/test/stream.xml > /tmp/test2/stream3.xml
cd /
rm -rf /tmp/test
##################################################################################################
[ -d /tmp/test ] || mkdir -p /tmp/test
cp /tmp/test2/stream.xml /tmp/test/stream.xml
cd /tmp/test
curl -Lbk -m 4555 -m 6555 -k  https://www.redtube.com/32874071 > /tmp/test/x1
cd /tmp/test
awk '/720/ {print}' x1 > x2
sed 's/\(["]\+\)/\n\1/g' x2 > x3
grep -E "(720P_1500K|720p_1500k)" x3 > x4
tr -d '[\]' < "x4" > x5
sed -n '1,1p' x5 > seznam
awk '/<h1 class="video_title">/ {print}' x1 >> seznam
#################################################
curl -Lbk -m 4555 -m 6555 -k  https://www.redtube.com/17218091 > /tmp/test/x1
cd /tmp/test
awk '/720/ {print}' x1 > x2
sed 's/\(["]\+\)/\n\1/g' x2 > x3
grep -E "(720P_1500K|720p_1500k)" x3 > x4
tr -d '[\]' < "x4" > x5
sed -n '1,1p' x5 >> seznam
awk '/<h1 class="video_title">/ {print}' x1 >> seznam
#################################################
curl -Lbk -m 4555 -m 6555 -k  https://www.redtube.com/16129041 > /tmp/test/x1
cd /tmp/test
awk '/720/ {print}' x1 > x2
sed 's/\(["]\+\)/\n\1/g' x2 > x3
grep -E "(720P_1500K|720p_1500k)" x3 > x4
tr -d '[\]' < "x4" > x5
sed -n '1,1p' x5 >> seznam
awk '/<h1 class="video_title">/ {print}' x1 >> seznam
#################################################
curl -Lbk -m 4555 -m 6555 -k  https://www.redtube.com/17846291 > /tmp/test/x1
cd /tmp/test
awk '/720/ {print}' x1 > x2
sed 's/\(["]\+\)/\n\1/g' x2 > x3
grep -E "(720P_1500K|720p_1500k)" x3 > x4
tr -d '[\]' < "x4" > x5
sed -n '1,1p' x5 >> seznam
awk '/<h1 class="video_title">/ {print}' x1 >> seznam
#################################################
curl -Lbk -m 4555 -m 6555 -k  https://www.redtube.com/23877771 > /tmp/test/x1
cd /tmp/test
awk '/720/ {print}' x1 > x2
sed 's/\(["]\+\)/\n\1/g' x2 > x3
grep -E "(720P_1500K|720p_1500k)" x3 > x4
tr -d '[\]' < "x4" > x5
sed -n '1,1p' x5 >> seznam
awk '/<h1 class="video_title">/ {print}' x1 >> seznam
#################################################
tr -d '["]' < "seznam" > seznam1
grep -o -i 'http[^<]*' seznam1 > adresa
grep -o -i 'title>[^<]*' seznam1 > seznam2
sed 's/title>//g' seznam2 > nazev
sed -i "s#&#@#g" adresa
#################################################
adresax1=`sed -n '1,1p' nazev`
adresax1=$adresax1
sed -i "s#N1#$adresax1#g" /tmp/test/stream.xml 
adresax2=`sed -n '2,2p' nazev`
adresax2=$adresax2
sed -i "s#N2#$adresax2#g" /tmp/test/stream.xml 
adresax3=`sed -n '3,3p' nazev`
adresax3=$adresax3
sed -i "s#N3#$adresax3#g" /tmp/test/stream.xml 
adresax4=`sed -n '4,4p' nazev`
adresax4=$adresax4
sed -i "s#N4#$adresax4#g" /tmp/test/stream.xml 
adresax5=`sed -n '5,5p' nazev`
adresax5=$adresax5
sed -i "s#N5#$adresax5#g" /tmp/test/stream.xml 
#################################################
nazevx1=`sed -n '1,1p' adresa`
nazevx1=$nazevx1
sed -i "s#X1#$nazevx1#g" /tmp/test/stream.xml 
nazevx2=`sed -n '2,2p' adresa`
nazevx2=$nazevx2
sed -i "s#X2#$nazevx2#g" /tmp/test/stream.xml 
nazevx3=`sed -n '3,3p' adresa`
nazevx3=$nazevx3
sed -i "s#X3#$nazevx3#g" /tmp/test/stream.xml 
nazevx4=`sed -n '4,4p' adresa`
nazevx4=$nazevx4
sed -i "s#X4#$nazevx4#g" /tmp/test/stream.xml 
nazevx5=`sed -n '5,5p' adresa`
nazevx5=$nazevx5
sed -i "s#X5#$nazevx5#g" /tmp/test/stream.xml
#################################################
sed -i 's/blacked.png/\blackambush.png/g' /tmp/test/stream.xml
sed -i 's/Blacked/\Blackambush/g' /tmp/test/stream.xml
sed -n '3,42p' /tmp/test/stream.xml > /tmp/test2/stream4.xml
cd /
rm -rf /tmp/test
##################################################################################################
[ -d /tmp/test ] || mkdir -p /tmp/test
cp /tmp/test2/stream.xml /tmp/test/stream.xml
cd /tmp/test
curl -Lbk -m 4555 -m 6555 -k  https://www.redtube.com/9015561 > /tmp/test/x1
cd /tmp/test
awk '/720/ {print}' x1 > x2
sed 's/\(["]\+\)/\n\1/g' x2 > x3
grep -E "(720P_1500K|720p_1500k)" x3 > x4
tr -d '[\]' < "x4" > x5
sed -n '1,1p' x5 > seznam
awk '/<h1 class="video_title">/ {print}' x1 >> seznam
#################################################
curl -Lbk -m 4555 -m 6555 -k  https://www.redtube.com/8696741 > /tmp/test/x1
cd /tmp/test
awk '/720/ {print}' x1 > x2
sed 's/\(["]\+\)/\n\1/g' x2 > x3
grep -E "(720P_1500K|720p_1500k)" x3 > x4
tr -d '[\]' < "x4" > x5
sed -n '1,1p' x5 >> seznam
awk '/<h1 class="video_title">/ {print}' x1 >> seznam
#################################################
curl -Lbk -m 4555 -m 6555 -k  https://www.redtube.com/8877091 > /tmp/test/x1
cd /tmp/test
awk '/720/ {print}' x1 > x2
sed 's/\(["]\+\)/\n\1/g' x2 > x3
grep -E "(720P_1500K|720p_1500k)" x3 > x4
tr -d '[\]' < "x4" > x5
sed -n '1,1p' x5 >> seznam
awk '/<h1 class="video_title">/ {print}' x1 >> seznam
#################################################
curl -Lbk -m 4555 -m 6555 -k  https://www.redtube.com/12291791 > /tmp/test/x1
cd /tmp/test
awk '/720/ {print}' x1 > x2
sed 's/\(["]\+\)/\n\1/g' x2 > x3
grep -E "(720P_1500K|720p_1500k)" x3 > x4
tr -d '[\]' < "x4" > x5
sed -n '1,1p' x5 >> seznam
awk '/<h1 class="video_title">/ {print}' x1 >> seznam
#################################################
curl -Lbk -m 4555 -m 6555 -k  https://www.redtube.com/1248704 > /tmp/test/x1
cd /tmp/test
awk '/720/ {print}' x1 > x2
sed 's/\(["]\+\)/\n\1/g' x2 > x3
grep -E "(720P_1500K|720p_1500k)" x3 > x4
tr -d '[\]' < "x4" > x5
sed -n '1,1p' x5 >> seznam
awk '/<h1 class="video_title">/ {print}' x1 >> seznam
#################################################
tr -d '["]' < "seznam" > seznam1
grep -o -i 'http[^<]*' seznam1 > adresa
grep -o -i 'title>[^<]*' seznam1 > seznam2
sed 's/title>//g' seznam2 > nazev
sed -i "s#&#@#g" adresa
#################################################
adresax1=`sed -n '1,1p' nazev`
adresax1=$adresax1
sed -i "s#N1#$adresax1#g" /tmp/test/stream.xml 
adresax2=`sed -n '2,2p' nazev`
adresax2=$adresax2
sed -i "s#N2#$adresax2#g" /tmp/test/stream.xml 
adresax3=`sed -n '3,3p' nazev`
adresax3=$adresax3
sed -i "s#N3#$adresax3#g" /tmp/test/stream.xml 
adresax4=`sed -n '4,4p' nazev`
adresax4=$adresax4
sed -i "s#N4#$adresax4#g" /tmp/test/stream.xml 
adresax5=`sed -n '5,5p' nazev`
adresax5=$adresax5
sed -i "s#N5#$adresax5#g" /tmp/test/stream.xml 
#################################################
nazevx1=`sed -n '1,1p' adresa`
nazevx1=$nazevx1
sed -i "s#X1#$nazevx1#g" /tmp/test/stream.xml 
nazevx2=`sed -n '2,2p' adresa`
nazevx2=$nazevx2
sed -i "s#X2#$nazevx2#g" /tmp/test/stream.xml 
nazevx3=`sed -n '3,3p' adresa`
nazevx3=$nazevx3
sed -i "s#X3#$nazevx3#g" /tmp/test/stream.xml 
nazevx4=`sed -n '4,4p' adresa`
nazevx4=$nazevx4
sed -i "s#X4#$nazevx4#g" /tmp/test/stream.xml 
nazevx5=`sed -n '5,5p' adresa`
nazevx5=$nazevx5
sed -i "s#X5#$nazevx5#g" /tmp/test/stream.xml
#################################################

sed -i 's/blacked.png/\lovehuge.png/g' /tmp/test/stream.xml
sed -i 's/Blacked/\Teens Loves huge Cocks/g' /tmp/test/stream.xml
sed -n '3,42p' /tmp/test/stream.xml > /tmp/test2/stream5.xml
cd /
rm -rf /tmp/test
##################################################################################################
[ -d /tmp/test ] || mkdir -p /tmp/test
cp /tmp/test2/stream.xml /tmp/test/stream.xml
cd /tmp/test
curl -Lbk -m 4555 -m 6555 -k  https://www.redtube.com/34346141 > /tmp/test/x1
cd /tmp/test
awk '/720/ {print}' x1 > x2
sed 's/\(["]\+\)/\n\1/g' x2 > x3
grep -E "(720P_1500K|720p_1500k)" x3 > x4
tr -d '[\]' < "x4" > x5
sed -n '1,1p' x5 > seznam
awk '/<h1 class="video_title">/ {print}' x1 >> seznam
#################################################
curl -Lbk -m 4555 -m 6555 -k  https://www.redtube.com/28797541 > /tmp/test/x1
cd /tmp/test
awk '/720/ {print}' x1 > x2
sed 's/\(["]\+\)/\n\1/g' x2 > x3
grep -E "(720P_1500K|720p_1500k)" x3 > x4
tr -d '[\]' < "x4" > x5
sed -n '1,1p' x5 >> seznam
awk '/<h1 class="video_title">/ {print}' x1 >> seznam
#################################################
curl -Lbk -m 4555 -m 6555 -k  https://www.redtube.com/29108021 > /tmp/test/x1
cd /tmp/test
awk '/720/ {print}' x1 > x2
sed 's/\(["]\+\)/\n\1/g' x2 > x3
grep -E "(720P_1500K|720p_1500k)" x3 > x4
tr -d '[\]' < "x4" > x5
sed -n '1,1p' x5 >> seznam
awk '/<h1 class="video_title">/ {print}' x1 >> seznam
#################################################
curl -Lbk -m 4555 -m 6555 -k  https://www.redtube.com/30696271 > /tmp/test/x1
cd /tmp/test
awk '/720/ {print}' x1 > x2
sed 's/\(["]\+\)/\n\1/g' x2 > x3
grep -E "(720P_1500K|720p_1500k)" x3 > x4
tr -d '[\]' < "x4" > x5
sed -n '1,1p' x5 >> seznam
awk '/<h1 class="video_title">/ {print}' x1 >> seznam
#################################################
curl -Lbk -m 4555 -m 6555 -k  https://www.redtube.com/29220771 > /tmp/test/x1
cd /tmp/test
awk '/720/ {print}' x1 > x2
sed 's/\(["]\+\)/\n\1/g' x2 > x3
grep -E "(720P_1500K|720p_1500k)" x3 > x4
tr -d '[\]' < "x4" > x5
sed -n '1,1p' x5 >> seznam
awk '/<h1 class="video_title">/ {print}' x1 >> seznam
#################################################
tr -d '["]' < "seznam" > seznam1
grep -o -i 'http[^<]*' seznam1 > adresa
grep -o -i 'title>[^<]*' seznam1 > seznam2
sed 's/title>//g' seznam2 > nazev
sed -i "s#&#@#g" adresa
#################################################
adresax1=`sed -n '1,1p' nazev`
adresax1=$adresax1
sed -i "s#N1#$adresax1#g" /tmp/test/stream.xml 
adresax2=`sed -n '2,2p' nazev`
adresax2=$adresax2
sed -i "s#N2#$adresax2#g" /tmp/test/stream.xml 
adresax3=`sed -n '3,3p' nazev`
adresax3=$adresax3
sed -i "s#N3#$adresax3#g" /tmp/test/stream.xml 
adresax4=`sed -n '4,4p' nazev`
adresax4=$adresax4
sed -i "s#N4#$adresax4#g" /tmp/test/stream.xml 
adresax5=`sed -n '5,5p' nazev`
adresax5=$adresax5
sed -i "s#N5#$adresax5#g" /tmp/test/stream.xml 
#################################################
nazevx1=`sed -n '1,1p' adresa`
nazevx1=$nazevx1
sed -i "s#X1#$nazevx1#g" /tmp/test/stream.xml 
nazevx2=`sed -n '2,2p' adresa`
nazevx2=$nazevx2
sed -i "s#X2#$nazevx2#g" /tmp/test/stream.xml 
nazevx3=`sed -n '3,3p' adresa`
nazevx3=$nazevx3
sed -i "s#X3#$nazevx3#g" /tmp/test/stream.xml 
nazevx4=`sed -n '4,4p' adresa`
nazevx4=$nazevx4
sed -i "s#X4#$nazevx4#g" /tmp/test/stream.xml 
nazevx5=`sed -n '5,5p' adresa`
nazevx5=$nazevx5
sed -i "s#X5#$nazevx5#g" /tmp/test/stream.xml
#################################################

sed -i 's/blacked.png/\bigass.png/g' /tmp/test/stream.xml
sed -i 's/Blacked/\Big Ass/g' /tmp/test/stream.xml
sed -n '3,42p' /tmp/test/stream.xml > /tmp/test2/stream6.xml
cd /
rm -rf /tmp/test
##################################################################################################
[ -d /tmp/test ] || mkdir -p /tmp/test
cp /tmp/test2/stream.xml /tmp/test/stream.xml
cd /tmp/test
curl -Lbk -m 4555 -m 6555 -k  https://www.redtube.com/36433151 > /tmp/test/x1
cd /tmp/test
awk '/720/ {print}' x1 > x2
sed 's/\(["]\+\)/\n\1/g' x2 > x3
grep -E "(720P_1500K|720p_1500k)" x3 > x4
tr -d '[\]' < "x4" > x5
sed -n '1,1p' x5 > seznam
awk '/<h1 class="video_title">/ {print}' x1 >> seznam
#################################################
curl -Lbk -m 4555 -m 6555 -k  https://www.redtube.com/1042990 > /tmp/test/x1
cd /tmp/test
awk '/720/ {print}' x1 > x2
sed 's/\(["]\+\)/\n\1/g' x2 > x3
grep -E "(720P_1500K|720p_1500k)" x3 > x4
tr -d '[\]' < "x4" > x5
sed -n '1,1p' x5 >> seznam
awk '/<h1 class="video_title">/ {print}' x1 >> seznam
#################################################
curl -Lbk -m 4555 -m 6555 -k  https://www.redtube.com/2131083 > /tmp/test/x1
cd /tmp/test
awk '/720/ {print}' x1 > x2
sed 's/\(["]\+\)/\n\1/g' x2 > x3
grep -E "(720P_1500K|720p_1500k)" x3 > x4
tr -d '[\]' < "x4" > x5
sed -n '1,1p' x5 >> seznam
awk '/<h1 class="video_title">/ {print}' x1 >> seznam
#################################################
curl -Lbk -m 4555 -m 6555 -k  https://www.redtube.com/29848501 > /tmp/test/x1
cd /tmp/test
awk '/720/ {print}' x1 > x2
sed 's/\(["]\+\)/\n\1/g' x2 > x3
grep -E "(720P_1500K|720p_1500k)" x3 > x4
tr -d '[\]' < "x4" > x5
sed -n '1,1p' x5 >> seznam
awk '/<h1 class="video_title">/ {print}' x1 >> seznam
#################################################
curl -Lbk -m 4555 -m 6555 -k  https://www.redtube.com/36394851 > /tmp/test/x1
cd /tmp/test
awk '/720/ {print}' x1 > x2
sed 's/\(["]\+\)/\n\1/g' x2 > x3
grep -E "(720P_1500K|720p_1500k)" x3 > x4
tr -d '[\]' < "x4" > x5
sed -n '1,1p' x5 >> seznam
awk '/<h1 class="video_title">/ {print}' x1 >> seznam
#################################################
tr -d '["]' < "seznam" > seznam1
grep -o -i 'http[^<]*' seznam1 > adresa
grep -o -i 'title>[^<]*' seznam1 > seznam2
sed 's/title>//g' seznam2 > nazev
sed -i "s#&#@#g" adresa
#################################################
adresax1=`sed -n '1,1p' nazev`
adresax1=$adresax1
sed -i "s#N1#$adresax1#g" /tmp/test/stream.xml 
adresax2=`sed -n '2,2p' nazev`
adresax2=$adresax2
sed -i "s#N2#$adresax2#g" /tmp/test/stream.xml 
adresax3=`sed -n '3,3p' nazev`
adresax3=$adresax3
sed -i "s#N3#$adresax3#g" /tmp/test/stream.xml 
adresax4=`sed -n '4,4p' nazev`
adresax4=$adresax4
sed -i "s#N4#$adresax4#g" /tmp/test/stream.xml 
adresax5=`sed -n '5,5p' nazev`
adresax5=$adresax5
sed -i "s#N5#$adresax5#g" /tmp/test/stream.xml 
#################################################
nazevx1=`sed -n '1,1p' adresa`
nazevx1=$nazevx1
sed -i "s#X1#$nazevx1#g" /tmp/test/stream.xml 
nazevx2=`sed -n '2,2p' adresa`
nazevx2=$nazevx2
sed -i "s#X2#$nazevx2#g" /tmp/test/stream.xml 
nazevx3=`sed -n '3,3p' adresa`
nazevx3=$nazevx3
sed -i "s#X3#$nazevx3#g" /tmp/test/stream.xml 
nazevx4=`sed -n '4,4p' adresa`
nazevx4=$nazevx4
sed -i "s#X4#$nazevx4#g" /tmp/test/stream.xml 
nazevx5=`sed -n '5,5p' adresa`
nazevx5=$nazevx5
sed -i "s#X5#$nazevx5#g" /tmp/test/stream.xml
#################################################
sed -i 's/blacked.png/\bigtits.png/g' /tmp/test/stream.xml
sed -i 's/Blacked/\Big Tits/g' /tmp/test/stream.xml
sed -n '3,42p' /tmp/test/stream.xml > /tmp/test2/stream7.xml
cd /
rm -rf /tmp/test
##################################################################################################
[ -d /tmp/test ] || mkdir -p /tmp/test
cp /tmp/test2/stream.xml /tmp/test/stream.xml
cd /tmp/test
curl -Lbk -m 4555 -m 6555 -k  https://www.redtube.com/32358181 > /tmp/test/x1
cd /tmp/test
awk '/720/ {print}' x1 > x2
sed 's/\(["]\+\)/\n\1/g' x2 > x3
grep -E "(720P_1500K|720p_1500k)" x3 > x4
tr -d '[\]' < "x4" > x5
sed -n '1,1p' x5 > seznam
awk '/<h1 class="video_title">/ {print}' x1 >> seznam
#################################################
curl -Lbk -m 4555 -m 6555 -k  https://www.redtube.com/1626237 > /tmp/test/x1   
cd /tmp/test
awk '/720/ {print}' x1 > x2
sed 's/\(["]\+\)/\n\1/g' x2 > x3
grep -E "(720P_1500K|720p_1500k)" x3 > x4
tr -d '[\]' < "x4" > x5
sed -n '1,1p' x5 >> seznam
awk '/<h1 class="video_title">/ {print}' x1 >> seznam
#################################################
curl -Lbk -m 4555 -m 6555 -k  https://www.redtube.com/35185361 > /tmp/test/x1
cd /tmp/test
awk '/720/ {print}' x1 > x2
sed 's/\(["]\+\)/\n\1/g' x2 > x3
grep -E "(720P_1500K|720p_1500k)" x3 > x4
tr -d '[\]' < "x4" > x5
sed -n '1,1p' x5 >> seznam
awk '/<h1 class="video_title">/ {print}' x1 >> seznam
#################################################
curl -Lbk -m 4555 -m 6555 -k  https://www.redtube.com/30239751 > /tmp/test/x1
cd /tmp/test
awk '/720/ {print}' x1 > x2
sed 's/\(["]\+\)/\n\1/g' x2 > x3
grep -E "(720P_1500K|720p_1500k)" x3 > x4
tr -d '[\]' < "x4" > x5
sed -n '1,1p' x5 >> seznam
awk '/<h1 class="video_title">/ {print}' x1 >> seznam
#################################################
curl -Lbk -m 4555 -m 6555 -k  https://www.redtube.com/1155770 > /tmp/test/x1
cd /tmp/test
awk '/720/ {print}' x1 > x2
sed 's/\(["]\+\)/\n\1/g' x2 > x3
grep -E "(720P_1500K|720p_1500k)" x3 > x4
tr -d '[\]' < "x4" > x5
sed -n '1,1p' x5 >> seznam
awk '/<h1 class="video_title">/ {print}' x1 >> seznam
#################################################
tr -d '["]' < "seznam" > seznam1
grep -o -i 'http[^<]*' seznam1 > adresa
grep -o -i 'title>[^<]*' seznam1 > seznam2
sed 's/title>//g' seznam2 > nazev
sed -i "s#&#@#g" adresa
#################################################
adresax1=`sed -n '1,1p' nazev`
adresax1=$adresax1
sed -i "s#N1#$adresax1#g" /tmp/test/stream.xml 
adresax2=`sed -n '2,2p' nazev`
adresax2=$adresax2
sed -i "s#N2#$adresax2#g" /tmp/test/stream.xml 
adresax3=`sed -n '3,3p' nazev`
adresax3=$adresax3
sed -i "s#N3#$adresax3#g" /tmp/test/stream.xml 
adresax4=`sed -n '4,4p' nazev`
adresax4=$adresax4
sed -i "s#N4#$adresax4#g" /tmp/test/stream.xml 
adresax5=`sed -n '5,5p' nazev`
adresax5=$adresax5
sed -i "s#N5#$adresax5#g" /tmp/test/stream.xml 
#################################################
nazevx1=`sed -n '1,1p' adresa`
nazevx1=$nazevx1
sed -i "s#X1#$nazevx1#g" /tmp/test/stream.xml 
nazevx2=`sed -n '2,2p' adresa`
nazevx2=$nazevx2
sed -i "s#X2#$nazevx2#g" /tmp/test/stream.xml 
nazevx3=`sed -n '3,3p' adresa`
nazevx3=$nazevx3
sed -i "s#X3#$nazevx3#g" /tmp/test/stream.xml 
nazevx4=`sed -n '4,4p' adresa`
nazevx4=$nazevx4
sed -i "s#X4#$nazevx4#g" /tmp/test/stream.xml 
nazevx5=`sed -n '5,5p' adresa`
nazevx5=$nazevx5
sed -i "s#X5#$nazevx5#g" /tmp/test/stream.xml
#################################################

sed -i 's/blacked.png/\teen.png/g' /tmp/test/stream.xml
sed -i 's/Blacked/\Teen/g' /tmp/test/stream.xml
sed -n '3,42p' /tmp/test/stream.xml > /tmp/test2/stream8.xml
cd /
rm -rf /tmp/test
##################################################################################################
[ -d /tmp/test ] || mkdir -p /tmp/test
cp /tmp/test2/stream.xml /tmp/test/stream.xml
cd /tmp/test
curl -Lbk -m 4555 -m 6555 -k  https://www.redtube.com/6371741 > /tmp/test/x1
cd /tmp/test
awk '/720/ {print}' x1 > x2
sed 's/\(["]\+\)/\n\1/g' x2 > x3
grep -E "(720P_1500K|720p_1500k)" x3 > x4
tr -d '[\]' < "x4" > x5
sed -n '1,1p' x5 > seznam
awk '/<h1 class="video_title">/ {print}' x1 >> seznam
#################################################
curl -Lbk -m 4555 -m 6555 -k  https://www.redtube.com/36209151 > /tmp/test/x1   
cd /tmp/test
awk '/720/ {print}' x1 > x2
sed 's/\(["]\+\)/\n\1/g' x2 > x3
grep -E "(720P_1500K|720p_1500k)" x3 > x4
tr -d '[\]' < "x4" > x5
sed -n '1,1p' x5 >> seznam
awk '/<h1 class="video_title">/ {print}' x1 >> seznam
#################################################
curl -Lbk -m 4555 -m 6555 -k  https://www.redtube.com/939311 > /tmp/test/x1
cd /tmp/test
awk '/720/ {print}' x1 > x2
sed 's/\(["]\+\)/\n\1/g' x2 > x3
grep -E "(720P_1500K|720p_1500k)" x3 > x4
tr -d '[\]' < "x4" > x5
sed -n '1,1p' x5 >> seznam
awk '/<h1 class="video_title">/ {print}' x1 >> seznam
#################################################
curl -Lbk -m 4555 -m 6555 -k  https://www.redtube.com/36126491 > /tmp/test/x1
cd /tmp/test
awk '/720/ {print}' x1 > x2
sed 's/\(["]\+\)/\n\1/g' x2 > x3
grep -E "(720P_1500K|720p_1500k)" x3 > x4
tr -d '[\]' < "x4" > x5
sed -n '1,1p' x5 >> seznam
awk '/<h1 class="video_title">/ {print}' x1 >> seznam
#################################################
curl -Lbk -m 4555 -m 6555 -k  https://www.redtube.com/1626155 > /tmp/test/x1
cd /tmp/test
awk '/720/ {print}' x1 > x2
sed 's/\(["]\+\)/\n\1/g' x2 > x3
grep -E "(720P_1500K|720p_1500k)" x3 > x4
tr -d '[\]' < "x4" > x5
sed -n '1,1p' x5 >> seznam
awk '/<h1 class="video_title">/ {print}' x1 >> seznam
#################################################
tr -d '["]' < "seznam" > seznam1
grep -o -i 'http[^<]*' seznam1 > adresa
grep -o -i 'title>[^<]*' seznam1 > seznam2
sed 's/title>//g' seznam2 > nazev
sed -i "s#&#@#g" adresa
#################################################
adresax1=`sed -n '1,1p' nazev`
adresax1=$adresax1
sed -i "s#N1#$adresax1#g" /tmp/test/stream.xml 
adresax2=`sed -n '2,2p' nazev`
adresax2=$adresax2
sed -i "s#N2#$adresax2#g" /tmp/test/stream.xml 
adresax3=`sed -n '3,3p' nazev`
adresax3=$adresax3
sed -i "s#N3#$adresax3#g" /tmp/test/stream.xml 
adresax4=`sed -n '4,4p' nazev`
adresax4=$adresax4
sed -i "s#N4#$adresax4#g" /tmp/test/stream.xml 
adresax5=`sed -n '5,5p' nazev`
adresax5=$adresax5
sed -i "s#N5#$adresax5#g" /tmp/test/stream.xml 
#################################################
nazevx1=`sed -n '1,1p' adresa`
nazevx1=$nazevx1
sed -i "s#X1#$nazevx1#g" /tmp/test/stream.xml 
nazevx2=`sed -n '2,2p' adresa`
nazevx2=$nazevx2
sed -i "s#X2#$nazevx2#g" /tmp/test/stream.xml 
nazevx3=`sed -n '3,3p' adresa`
nazevx3=$nazevx3
sed -i "s#X3#$nazevx3#g" /tmp/test/stream.xml 
nazevx4=`sed -n '4,4p' adresa`
nazevx4=$nazevx4
sed -i "s#X4#$nazevx4#g" /tmp/test/stream.xml 
nazevx5=`sed -n '5,5p' adresa`
nazevx5=$nazevx5
sed -i "s#X5#$nazevx5#g" /tmp/test/stream.xml
#################################################
sed -i 's/blacked.png/\czech.png/g' /tmp/test/stream.xml
sed -i 's/Blacked/\Czech/g' /tmp/test/stream.xml
sed -n '3,42p' /tmp/test/stream.xml > /tmp/test2/stream9.xml
cd /
rm -rf /tmp/test
##################################################################################################
[ -d /tmp/test ] || mkdir -p /tmp/test
cp /tmp/test2/stream.xml /tmp/test/stream.xml
cd /tmp/test
curl -Lbk -m 4555 -m 6555 -k  https://www.redtube.com/18987901 > /tmp/test/x1
cd /tmp/test
awk '/720/ {print}' x1 > x2
sed 's/\(["]\+\)/\n\1/g' x2 > x3
grep -E "(720P_1500K|720p_1500k)" x3 > x4
tr -d '[\]' < "x4" > x5
sed -n '1,1p' x5 > seznam
awk '/<h1 class="video_title">/ {print}' x1 >> seznam
#################################################
curl -Lbk -m 4555 -m 6555 -k  https://www.redtube.com/2037251 > /tmp/test/x1   
cd /tmp/test
awk '/720/ {print}' x1 > x2
sed 's/\(["]\+\)/\n\1/g' x2 > x3
grep -E "(720P_1500K|720p_1500k)" x3 > x4
tr -d '[\]' < "x4" > x5
sed -n '1,1p' x5 >> seznam
awk '/<h1 class="video_title">/ {print}' x1 >> seznam
#################################################
curl -Lbk -m 4555 -m 6555 -k  https://www.redtube.com/18082361 > /tmp/test/x1
cd /tmp/test
awk '/720/ {print}' x1 > x2
sed 's/\(["]\+\)/\n\1/g' x2 > x3
grep -E "(720P_1500K|720p_1500k)" x3 > x4
tr -d '[\]' < "x4" > x5
sed -n '1,1p' x5 >> seznam
awk '/<h1 class="video_title">/ {print}' x1 >> seznam
#################################################
curl -Lbk -m 4555 -m 6555 -k  https://www.redtube.com/4047041 > /tmp/test/x1
cd /tmp/test
awk '/720/ {print}' x1 > x2
sed 's/\(["]\+\)/\n\1/g' x2 > x3
grep -E "(720P_1500K|720p_1500k)" x3 > x4
tr -d '[\]' < "x4" > x5
sed -n '1,1p' x5 >> seznam
awk '/<h1 class="video_title">/ {print}' x1 >> seznam
#################################################
curl -Lbk -m 4555 -m 6555 -k  https://www.redtube.com/30143331 > /tmp/test/x1
cd /tmp/test
awk '/720/ {print}' x1 > x2
sed 's/\(["]\+\)/\n\1/g' x2 > x3
grep -E "(720P_1500K|720p_1500k)" x3 > x4
tr -d '[\]' < "x4" > x5
sed -n '1,1p' x5 >> seznam
awk '/<h1 class="video_title">/ {print}' x1 >> seznam
#################################################
tr -d '["]' < "seznam" > seznam1
grep -o -i 'http[^<]*' seznam1 > adresa
grep -o -i 'title>[^<]*' seznam1 > seznam2
sed 's/title>//g' seznam2 > nazev
sed -i "s#&#@#g" adresa
#################################################
adresax1=`sed -n '1,1p' nazev`
adresax1=$adresax1
sed -i "s#N1#$adresax1#g" /tmp/test/stream.xml 
adresax2=`sed -n '2,2p' nazev`
adresax2=$adresax2
sed -i "s#N2#$adresax2#g" /tmp/test/stream.xml 
adresax3=`sed -n '3,3p' nazev`
adresax3=$adresax3
sed -i "s#N3#$adresax3#g" /tmp/test/stream.xml 
adresax4=`sed -n '4,4p' nazev`
adresax4=$adresax4
sed -i "s#N4#$adresax4#g" /tmp/test/stream.xml 
adresax5=`sed -n '5,5p' nazev`
adresax5=$adresax5
sed -i "s#N5#$adresax5#g" /tmp/test/stream.xml 
#################################################
nazevx1=`sed -n '1,1p' adresa`
nazevx1=$nazevx1
sed -i "s#X1#$nazevx1#g" /tmp/test/stream.xml 
nazevx2=`sed -n '2,2p' adresa`
nazevx2=$nazevx2
sed -i "s#X2#$nazevx2#g" /tmp/test/stream.xml 
nazevx3=`sed -n '3,3p' adresa`
nazevx3=$nazevx3
sed -i "s#X3#$nazevx3#g" /tmp/test/stream.xml 
nazevx4=`sed -n '4,4p' adresa`
nazevx4=$nazevx4
sed -i "s#X4#$nazevx4#g" /tmp/test/stream.xml 
nazevx5=`sed -n '5,5p' adresa`
nazevx5=$nazevx5
sed -i "s#X5#$nazevx5#g" /tmp/test/stream.xml
#################################################
sed -i 's/blacked.png/\black.png/g' /tmp/test/stream.xml
sed -i 's/Blacked/\Black/g' /tmp/test/stream.xml
sed -n '3,43p' /tmp/test/stream.xml > /tmp/test2/stream10.xml
cd /
rm -rf /tmp/test
##################################################################################################
cd /tmp/test2
cat stream2.xml >> stream1.xml
cat stream3.xml >> stream1.xml
cat stream4.xml >> stream1.xml
cat stream5.xml >> stream1.xml
cat stream6.xml >> stream1.xml
cat stream7.xml >> stream1.xml
cat stream8.xml >> stream1.xml
cat stream9.xml >> stream1.xml
cat stream10.xml >> stream1.xml
#################################################
cat stream1.xml > /usr/lib/enigma2/python/Plugins/Extensions/StreamTvPlayerFHD/stream.xml
cd /
rm -rf /tmp/test2
sleep 1
echo ""
echo "OK"
sleep 1
echo ""
exit

