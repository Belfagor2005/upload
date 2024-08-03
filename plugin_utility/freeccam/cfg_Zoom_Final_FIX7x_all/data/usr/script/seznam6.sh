#!/bin/sh
echo "stahuji z : cccam3.com"

echo "ukládám server..."

echo "zobrazuji...."
echo ""
echo ""

[ -d /tmp/test ] || mkdir -p /tmp/test
####################################################################################################
curl  --limit-rate 100K     -s -k -Lbk -A -k -m 8 -m 52   https://www.cccam3.com/  > /tmp/test/CCcam 
cd /tmp/test



grep -i 'BY CCCAM3.COM[^"]*' CCcam > adresa


grep -o -i 'https://www.cccam3.com[^"]*'  adresa > adresa1

adresa1=`sed -n '1,1p' adresa1`
adresa1=$adresa1
curl  --limit-rate 100K     -s -k -Lbk -A -k -m 8 -m 52    $adresa1 > /tmp/test/CCcam
grep -o -i 'C:[^<]*' CCcam  > CCcam1

sed -i '1,1d' CCcam1



if grep -o -i 'C:[^<]*' CCcam1 ; then
grep -o -i 'C:[^<]*' CCcam1  > /etc/CCcam.cfg
else
echo 'server není k dispozici!'
echo ""
sleep 2
echo 'the server is not available!'
echo ""
echo ""
echo ""
rm -rf /tmp/test
exit
fi

cd /
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

