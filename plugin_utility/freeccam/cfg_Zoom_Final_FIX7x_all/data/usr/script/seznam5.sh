#!/bin/sh
echo "stahuji z : pktelcos.com"
sleep 1
echo "ukládám server..."
sleep 1
echo "zobrazuji...."
echo ""
echo ""
[ -d /tmp/test ] || mkdir -p /tmp/test

curl -k -A -k -s  https://www.pktelcos.com/dish-tv-free-cccam-test-cline-nss6-daily-updated/ > /tmp/test/CCcam
cd /tmp/test
sleep 1
echo -n "C: " > adresa
grep -o -i '<strong>[^<]*' CCcam  > CCcam1
grep -n -o -i 'IP=[^<]*' CCcam1|cut -d ' ' -f 2 >> adresa
grep -n -o -i 'Port:[^<]*' CCcam1|cut -d ' ' -f 2 >> adresa
sed -i '$!N;s/\n/ /' adresa
adresa1=`sed -n '1,1p' adresa`
adresa1=$adresa1
grep -o -i 'data-sheets-value=[^<]*' CCcam  > CCcam1
grep -o -i '">[^<]*' CCcam1  > CCcam2
sed -i 's/">/ /' CCcam2
sed -i '$!N;s/\n/ /' CCcam2
sed -i "s/ /$adresa1 /" CCcam2
cat CCcam2 > /etc/CCcam.cfg
cat CCcam2 > /tmp/readme.txt
sleep 1
cd /
more /tmp/readme.txt
rm /tmp/readme.txt
rm -rf /tmp/test



echo ""
echo ""
echo ""
sleep 1
echo "stahování proběhlo úspěšně."
echo ">>>>>>>>>>>>>>>>>>>>>>>>>>>"
sleep 1
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