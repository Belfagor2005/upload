#!/bin/sh
echo "stahuji z : firecccam.com"

echo "ukládám server..."

echo "zobrazuji...."
echo ""
echo ""
[ -d /tmp/test ] || mkdir -p /tmp/test
####################################################################################################
curl  -k -Lbk -A -k -m 8 -m 52 -s -v -d '&addf1=Generator cccam&amp;mgcamd'  -X POST http://firecccam.com/  >>/tmp/test/yyy 2>&1 </tmp/test/yyy &
sleep 1
adresa1=`tr -d '\r\032' </tmp/test/yyy|grep -o -i 'Location:[^<]*'| sed -n '1,1p'|awk '{print $ 2}'`
sleep 1
adresa1=$adresa1
cp /usr/lib/enigma2/python/Plugins/Extensions/OpenPanel/DATA/fire1.sh /tmp/test/fire1.sh
sleep 1
sed -i 's/!!!/'$adresa1'/g' /tmp/test/fire1.sh
chmod 755 /tmp/test/fire1.sh
/tmp/test/fire1.sh
sleep 1
adresa2=`tr -d '\r\032' </tmp/test/xxx|grep -o -i 'Location:[^<]*'| sed -n '1,1p'|awk '{print $ 2}'`
adresa2=$adresa2
cp /usr/lib/enigma2/python/Plugins/Extensions/OpenPanel/DATA/fire.sh /tmp/test/fire.sh
sed -i 's/!!!/'$adresa2'/g' /tmp/test/fire.sh
chmod 755 /tmp/test/fire.sh
/tmp/test/fire.sh
cd /tmp/test

grep -o -i 'C:[^<]*' CCcam  > /etc/CCcam.cfg
grep -o -i 'C:[^<]*' CCcam  > /tmp/readme.txt

cd /
more /tmp/readme.txt
rm /tmp/readme.txt
rm -rf /tmp/test



echo ""
echo ""
echo ""

echo "stahování proběhlo úspěšně."
echo ">>>>>>>>>>>>>>>>>>>>>>>>>>>"

date
echo ""
####################################################################################################
/usr/script/conv.sh
####################################################################################################
/usr/script/najdiCFG.sh >>/dev/null 2>&1 </dev/null &
####################################################################################################
/usr/script/restart.sh >>/dev/null 2>&1 </dev/null &
####################################################################################################
exit







