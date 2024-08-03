#!/bin/sh
echo "stahuji z : ab-forum.info"

echo "INFO...AB forum"

echo "zobrazuji...."
echo ""
echo ""

[ -d /tmp/test ] || mkdir -p /tmp/test
####################################################################################################
curl  -k -Lbk -m 55532 -m 555104 -s     'http://www.ab-forum.info/viewtopic.php?f=468&t=75677&start=20' > /tmp/test/CCcam 
cd /tmp/test


grep   '/viewtopic.php?f=468&amp;t=75677[^<]*' CCcam > CCcam1 
tail -n 2 CCcam1 > CCcam2
sed -n '1,1p' CCcam2 > CCcam3
grep -o -i 'start=[^"<]*' CCcam3 > CCcam4


echo 'curl  -k -Lbk -m 55532 -m 555104 -s' > /tmp/test/skript
echo -n ' ' >> /tmp/test/skript
echo -n '"http://www.ab-forum.info/viewtopic.php?f=468&t=75677&' >> /tmp/test/skript
cat CCcam4 >> /tmp/test/skript
echo -n '"' >> /tmp/test/skript
echo -n ' > /tmp/test/adresa' >> /tmp/test/skript
sed -n 'H; $x; $s/\n//gp' /tmp/test/skript > /tmp/test/skript.sh
chmod 755 /tmp/test/skript.sh
/tmp/test/skript.sh

grep  'post[^<]*' /tmp/test/adresa > /tmp/test/adresa1
grep -o -i '>[^"<]*' /tmp/test/adresa1 > /tmp/test/adresa2
sed -i "s/&nbsp;//" /tmp/test/adresa2

sed -i '/Re:/d' /tmp/test/adresa2
sed -i '/Příspěvek/d' /tmp/test/adresa2
sed -i '/Předmět/d' /tmp/test/adresa2
sed -i '/Poslat/d' /tmp/test/adresa2
sed -i '/Odpovědět/d' /tmp/test/adresa2
sed -i '/&/d' /tmp/test/adresa2
sed -i '/krát/d' /tmp/test/adresa2
sed -i '/Poděko/d' /tmp/test/adresa2
sed -i '/>Zobrazit příspěvky za poslední:/,$d' /tmp/test/adresa2 
sed -i "s/>//" /tmp/test/adresa2
sed -i '/^$/d' /tmp/test/adresa2
more /tmp/test/adresa2
cd /
rm -rf /tmp/test

exit 