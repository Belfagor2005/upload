#!/bin/sh
[ -d /tmp/best ] || mkdir -p /tmp/best
####################################################################################################
PATH_J_XM1=$(echo "$((1000 + RANDOM % 9999))$((RANDOM % 9999))")
PATH_J_XM2=$(echo "$((1000 + RANDOM % 9999))$((RANDOM % 9999))")
curl   -Lbk -m 4555 -m 6555 -k   -s -d 'Username='$PATH_J_XM1'&Password='$PATH_J_XM2'&addf=2 Days Free Cccam' -X POST  https://ncccam.com/freecccam/index.php > /tmp/best/CCcam
cd /tmp/best
sed -ne '/Server :/ p' CCcam > CCcam1
sed -ne 's#.*Server \([^<]*\).*#\1#p' CCcam1 > hotovo
sed -ne 's#.*Port :\([^<]*\).*#\1#p' CCcam1 >> hotovo
sed -ne 's#.*User :\([^<]*\).*#\1#p' CCcam1 >> hotovo
sed -ne 's#.*Pass :\([^<]*\).*#\1#p' CCcam1 >> hotovo
sed -n 'H; $x; $s/\n//gp' hotovo > hotovo1
sed -e "s/:/C:/" hotovo1 > CCcam

grep -o -i -E 'C: [a-z][^<]*' CCcam > /tmp/best/soubor29
grep -o -i -E 'C: [a-z][^<]*' CCcam > /tmp/test/CCAM
cd /
more /tmp/best/soubor29
####################################################################################################
PATH_J_XM1=$(echo "$((1000 + RANDOM % 9999))$((RANDOM % 9999))")
PATH_J_XM2=$(echo "$((1000 + RANDOM % 9999))$((RANDOM % 9999))")
curl   -Lbk -m 4555 -m 6555 -k   -s -d 'Username='$PATH_J_XM1'&Password='$PATH_J_XM2'&addf=2 Days Free Cccam' -X POST  https://clinepk.com/freecccam/index.php > /tmp/best/CCcam
cd /tmp/best
sed -ne '/Server :/ p' CCcam > CCcam1
sed -ne 's#.*Server \([^<]*\).*#\1#p' CCcam1 > hotovo
sed -ne 's#.*Port :\([^<]*\).*#\1#p' CCcam1 >> hotovo
sed -ne 's#.*User :\([^<]*\).*#\1#p' CCcam1 >> hotovo
sed -ne 's#.*Pass :\([^<]*\).*#\1#p' CCcam1 >> hotovo
sed -n 'H; $x; $s/\n//gp' hotovo > hotovo1
sed -e "s/:/C:/" hotovo1 > CCcam

grep -o -i -E 'C: [a-z][^<]*' CCcam > /tmp/best/soubor8
grep -o -i -E 'C: [a-z][^<]*' CCcam >> /tmp/test/CCAM
cd /
more /tmp/best/soubor8
####################################################################################################
PATH_J_XM1=$(echo "$((1000 + RANDOM % 9999))$((RANDOM % 9999))")
PATH_J_XM2=$(echo "$((1000 + RANDOM % 9999))$((RANDOM % 9999))")
curl   -Lbk -m 4555 -m 6555 -k   -s -d 'Username='$PATH_J_XM1'&Password='$PATH_J_XM2'&addf=2 Days Free Cccam' -X POST  https://videocon.vip/freecccam/index.php > /tmp/best/CCcam
cd /tmp/best
sed -ne '/Server :/ p' CCcam > CCcam1
sed -ne 's#.*Server \([^<]*\).*#\1#p' CCcam1 > hotovo
sed -ne 's#.*Port :\([^<]*\).*#\1#p' CCcam1 >> hotovo
sed -ne 's#.*User :\([^<]*\).*#\1#p' CCcam1 >> hotovo
sed -ne 's#.*Pass :\([^<]*\).*#\1#p' CCcam1 >> hotovo
sed -n 'H; $x; $s/\n//gp' hotovo > hotovo1
sed -e "s/:/C:/" hotovo1 > CCcam
grep -o -i -E 'C: [a-z][^<]*' CCcam > /tmp/best/soubor62
grep -o -i -E 'C: [a-z][^<]*' CCcam >> /tmp/test/CCAM
cd /
more /tmp/best/soubor62
####################################################################################################
PATH_J_XM1=$(echo "$((10000 + RANDOM % 9999))$((RANDOM % 9999))")
PATH_J_XM2=$(echo "$((10000 + RANDOM % 9999))$((RANDOM % 9999))")
curl  -Lbk -m 4555 -m 6555 -k -s -d 'Username='$PATH_J_XM1'&Password='$PATH_J_XM2'&addf=2 Days Free Cccam' -X POST  https://dishtvsd.com/freecccam/index.php > /tmp/best/CCcam
cd /tmp/best
sed -ne '/Server :/ p' CCcam > CCcam1
sed -ne 's#.*Server \([^<]*\).*#\1#p' CCcam1 > hotovo
sed -ne 's#.*Port :\([^<]*\).*#\1#p' CCcam1 >> hotovo
sed -ne 's#.*User :\([^<]*\).*#\1#p' CCcam1 >> hotovo
sed -ne 's#.*Pass :\([^<]*\).*#\1#p' CCcam1 >> hotovo
sed -n 'H; $x; $s/\n//gp' hotovo > hotovo1
sed -e "s/:/C:/" hotovo1 > CCcam
grep -o -i -E 'C: [a-z][^<]*' CCcam  > /tmp/best/soubor57
grep -o -i -E 'C: [a-z][^<]*' CCcam >> /tmp/test/CCAM
cd /
more /tmp/best/soubor57
####################################################################################################
PATH_J_XM1=$(echo "$((1000 + RANDOM % 9999))$((RANDOM % 9999))")
PATH_J_XM2=$(echo "$((1000 + RANDOM % 9999))$((RANDOM % 9999))")
curl   -Lbk -m 4555 -m 6555 -k   -s -d 'Username='$PATH_J_XM1'&Password='$PATH_J_XM2'&addf=2 Days Free Cccam' -X POST  https://tatasky.us/freecccam/index.php > /tmp/best/CCcam
cd /tmp/best
sed -ne '/Server :/ p' CCcam > CCcam1
sed -ne 's#.*Server \([^<]*\).*#\1#p' CCcam1 > hotovo
sed -ne 's#.*Port :\([^<]*\).*#\1#p' CCcam1 >> hotovo
sed -ne 's#.*User :\([^<]*\).*#\1#p' CCcam1 >> hotovo
sed -ne 's#.*Pass :\([^<]*\).*#\1#p' CCcam1 >> hotovo
sed -n 'H; $x; $s/\n//gp' hotovo > hotovo1
sed -e "s/:/C:/" hotovo1 > CCcam
grep -o -i -E 'C: [a-z][^<]*' CCcam > /tmp/best/soubor40
grep -o -i -E 'C: [a-z][^<]*' CCcam >> /tmp/test/CCAM
cd /
more /tmp/best/soubor40
####################################################################################################
PATH_J_XM1=$(echo "$((1000 + RANDOM % 9999))$((RANDOM % 9999))")
PATH_J_XM2=$(echo "$((1000 + RANDOM % 9999))$((RANDOM % 9999))")
curl   -Lbk -m 4555 -m 6555 -k   -s -d 'Username='$PATH_J_XM1'&Password='$PATH_J_XM2'&addf=2 Days Free Cccam' -X POST  https://clinepk.com/freecccam/index.php > /tmp/best/CCcam
cd /tmp/best
sed -ne '/Server :/ p' CCcam > CCcam1
sed -ne 's#.*Server \([^<]*\).*#\1#p' CCcam1 > hotovo
sed -ne 's#.*Port :\([^<]*\).*#\1#p' CCcam1 >> hotovo
sed -ne 's#.*User :\([^<]*\).*#\1#p' CCcam1 >> hotovo
sed -ne 's#.*Pass :\([^<]*\).*#\1#p' CCcam1 >> hotovo
sed -n 'H; $x; $s/\n//gp' hotovo > hotovo1
sed -e "s/:/C:/" hotovo1 > CCcam
grep -o -i -E 'C: [a-z][^<]*' CCcam > /tmp/best/soubor47
grep -o -i -E 'C: [a-z][^<]*' CCcam >> /tmp/test/CCAM
cd /
more /tmp/best/soubor47
####################################################################################################
PATH_J_XM1=$(echo "$((1000 + RANDOM % 9999))$((RANDOM % 9999))")
PATH_J_XM2=$(echo "$((1000 + RANDOM % 9999))$((RANDOM % 9999))")
curl  -Lbk -m 4555 -m 6555 -k -s -d 'Username='$PATH_J_XM1'&Password='$PATH_J_XM2'&addf=2 Days Free Cccam' -X POST  https://clinepk.com/freecccam/index.php > /tmp/best/CCcam
cd /tmp/best
sed -ne '/Server :/ p' CCcam > CCcam1
sed -ne 's#.*Server \([^<]*\).*#\1#p' CCcam1 > hotovo
sed -ne 's#.*Port :\([^<]*\).*#\1#p' CCcam1 >> hotovo
sed -ne 's#.*User :\([^<]*\).*#\1#p' CCcam1 >> hotovo
sed -ne 's#.*Pass :\([^<]*\).*#\1#p' CCcam1 >> hotovo
sed -n 'H; $x; $s/\n//gp' hotovo > hotovo1
sed -e "s/:/C:/" hotovo1 > CCcam
grep -o -i -E 'C: [a-z][^<]*' CCcam > /tmp/best/soubor48
grep -o -i -E 'C: [a-z][^<]*' CCcam >> /tmp/test/CCAM
cd /
more /tmp/best/soubor48
####################################################################################################
PATH_J_XM1=$(echo "$((1000 + RANDOM % 9999))$((RANDOM % 9999))")
PATH_J_XM2=$(echo "$((1000 + RANDOM % 9999))$((RANDOM % 9999))")
curl  -Lbk -m 4555 -m 6555 -k -s -d 'Username='$PATH_J_XM1'&Password='$PATH_J_XM2'&addf=2 Days Free Cccam' -X POST  https://cline.eu/freecccam/index.php > /tmp/best/CCcam
cd /tmp/best
sed -ne '/Server :/ p' CCcam > CCcam1
sed -ne 's#.*Server \([^<]*\).*#\1#p' CCcam1 > hotovo
sed -ne 's#.*Port :\([^<]*\).*#\1#p' CCcam1 >> hotovo
sed -ne 's#.*User :\([^<]*\).*#\1#p' CCcam1 >> hotovo
sed -ne 's#.*Pass :\([^<]*\).*#\1#p' CCcam1 >> hotovo
sed -n 'H; $x; $s/\n//gp' hotovo > hotovo1
sed -e "s/:/C:/" hotovo1 > CCcam
grep -o -i -E 'C: [a-z][^<]*' CCcam > /tmp/best/soubor49
grep -o -i -E 'C: [a-z][^<]*' CCcam >> /tmp/test/CCAM
cd /
more /tmp/best/soubor49
####################################################################################################
PATH_J_XM1=$(echo "$((1000 + RANDOM % 9999))$((RANDOM % 9999))")
PATH_J_XM2=$(echo "$((1000 + RANDOM % 9999))$((RANDOM % 9999))")
curl   -Lbk -m 4555 -m 6555 -k -s -d 'Username='$PATH_J_XM1'&Password='$PATH_J_XM2'&addf=2 Days Free Cccam' -X POST  https://sunnyhd.top/freecccam/index.php > /tmp/best/CCcam
cd /tmp/best
echo "C: "  > hotovo
sed -ne 's#.*Server : \([^<]*\).*#\1#p' CCcam >> hotovo
echo -n " "  >> hotovo
sed -ne 's#.*Port : \([^<]*\).*#\1#p' CCcam >> hotovo
echo -n " "  >> hotovo
sed -ne 's#.*User : \([^<]*\).*#\1#p' CCcam >> hotovo
echo -n " "  >> hotovo
sed -ne 's#.*Pass : \([^<]*\).*#\1#p' CCcam >> hotovo
sed -n 'H; $x; $s/\n//gp' hotovo > hotovo1
echo ""  >> hotovo1
cat hotovo1 > CCcam
echo ""  > CCcam1
cat 'CCcam' | while read radek ; do
pocet=`echo $radek| wc -w`
if [ $pocet -gt 4 ]; then
echo $radek > CCcam1
fi 
done
grep -o -i 'C: [^<]*' CCcam1  > /tmp/best/soubor15
grep -o -i 'C: [^<]*' CCcam1 >> /tmp/test/CCAM
cd /
more /tmp/best/soubor15
####################################################################################################

curl   -k -Lbk -A -vk -m 800 -m 5200 -s  https://iptvcccam.co/cccamfree/get.php > /tmp/best/CCcam
cd /tmp/best
grep -o -i 'C: [^<]*' CCcam  > /tmp/best/soubor24
grep -o -i 'C: [^<]*' CCcam >> /tmp/test/CCAM
cd / 
more /tmp/best/soubor24
####################################################################################################
PATH_J_XM1=$(echo "$((1000 + RANDOM % 9999))$((RANDOM % 9999))")
PATH_J_XM2=$(echo "$((1000 + RANDOM % 9999))$((RANDOM % 9999))")
curl --speed-time 3 --speed-limit 1000 -Lbk -m 4555 -m 6555 -k -s -d 'Username='$PATH_J_XM1'&Password='$PATH_J_XM2'&addf=2 Days Free Cccam' -X POST  https://dreamcccam.com/freecccam/index.php > /tmp/best/CCcam
cd /tmp/best
sed -ne '/Server :/ p' CCcam > CCcam1
sed -ne 's#.*Server \([^<]*\).*#\1#p' CCcam1 > hotovo
sed -ne 's#.*Port :\([^<]*\).*#\1#p' CCcam1 >> hotovo
sed -ne 's#.*User :\([^<]*\).*#\1#p' CCcam1 >> hotovo
sed -ne 's#.*Pass :\([^<]*\).*#\1#p' CCcam1 >> hotovo
sed -n 'H; $x; $s/\n//gp' hotovo > hotovo1
sed -e "s/:/C:/" hotovo1 > CCcam
grep -o -i -E 'C: [a-z][^<]*' CCcam > /tmp/best/soubor9
grep -o -i -E 'C: [a-z][^<]*' CCcam >> /tmp/test/CCAM
cd /
more /tmp/best/soubor9
####################################################################################################








sleep 2
cd /


rm -rf /CCcam*
rm -rf /hotovo*


sleep 1








exit
