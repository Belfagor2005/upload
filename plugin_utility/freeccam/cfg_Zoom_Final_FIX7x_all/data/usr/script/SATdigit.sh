#!/bin/sh
echo "stahuji z : satdigitalne.cz"

echo "INFO...SATDIGITALNE"

echo "zobrazuji...."
echo ""
sleep 2
echo "prosím čekejte!!"
echo ""

[ -d /tmp/test ] || mkdir -p /tmp/test
####################################################################################################
curl  -k -Lbk -m 55532 -m 555104 -s     'https://www.forum.satdigitalne.cz/subdom/forum/viewtopic.php?f=257&t=16544&start=20' > /tmp/test/CCcam 
cd /tmp/test


grep   '/viewtopic.php?f=257&amp;t=16544[^<]*' CCcam > CCcam1 
tail -n 2 CCcam1 > CCcam2
sed -n '1,1p' CCcam2 > CCcam3
grep -o -i 'start=[^"<]*' CCcam3 > CCcam4


echo 'curl  -k -Lbk -m 55532 -m 555104 -s' > /tmp/test/skript
echo -n ' ' >> /tmp/test/skript
echo -n '"https://www.forum.satdigitalne.cz/subdom/forum/viewtopic.php?f=257&t=16544&' >> /tmp/test/skript
cat CCcam4 >> /tmp/test/skript
echo -n '"' >> /tmp/test/skript
echo -n ' > /tmp/test/adresa' >> /tmp/test/skript
sed -n 'H; $x; $s/\n//gp' /tmp/test/skript > /tmp/test/skript.sh
chmod 755 /tmp/test/skript.sh
/tmp/test/skript.sh
sed -n 'H; $x; $s/\n//gp' /tmp/test/adresa > /tmp/test/adresa1
sed 's/\([">]\+\)/\n\1/g' /tmp/test/adresa1 > /tmp/test/adresa2
grep -o -i '>[^"<]*' /tmp/test/adresa2 > /tmp/test/adresa3
sed -i "s/>//" /tmp/test/adresa3
sed -i '/^$/d' /tmp/test/adresa3
sed -i '/Všechny příspěvky/,$d' /tmp/test/adresa3
sed  '1,/Příspěvek/d' /tmp/test/adresa3 > /tmp/test/adresa2
sed -i '/^$/d' /tmp/test/adresa2

sed -i '/Kontaktovat/d' /tmp/test/adresa2
sed -i '/poděkování/d' /tmp/test/adresa2
sed -i '/Nahoru/d' /tmp/test/adresa2
sed -i '/Nahoru/d' /tmp/test/adresa2
sed -i '/Citovat/d' /tmp/test/adresa2
sed -i '/ICQ/d' /tmp/test/adresa2
sed -i '/Příspěvek/d' /tmp/test/adresa2
sed -i '/Předmět/d' /tmp/test/adresa2
sed -i '/Poslat/d' /tmp/test/adresa2
sed -i '/Odpovědět/d' /tmp/test/adresa2
sed -i '/&/d' /tmp/test/adresa2
sed -i '/Zobrazit:/d' /tmp/test/adresa2
sed -i '/Poděko/d' /tmp/test/adresa2
sed -i '/Verze pro tisk/,$d' /tmp/test/adresa2 
sed -i "s/>//" /tmp/test/adresa2
sed -i '/^$/d' /tmp/test/adresa2
more /tmp/test/adresa2
cd /
rm -rf /tmp/test

exit 