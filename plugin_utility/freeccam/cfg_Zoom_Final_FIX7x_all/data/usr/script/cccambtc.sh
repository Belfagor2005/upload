#!/bin/sh
echo "stahuji z : cccambtc.com"

echo "ukládám server..."

echo "zobrazuji...."
echo ""
echo ""

[ -d /tmp/test ] || mkdir -p /tmp/test
####################################################################################################
curl  --limit-rate 100K     -k -A -k -s https://cccambtc.com/ > /tmp/test/CCcam 
cd /tmp/test
grep   '>Cccam Generator 1[^<]*' CCcam > CCcam1 
grep -o -i 'https://cccambtc.com/[^"<]*' CCcam1 > CCcam2
adresa1=`sed -n '1,1p' CCcam2`
adresa1=$adresa1
curl  --limit-rate 100K     -k -A -k -s  $adresa1 > /tmp/test/adresa
grep -o -i 'action="[^<]*' adresa > adresa1
grep -o -i 'https://cccambtc.com/[^"<]*' adresa1 > adresa2
adresa2=`sed -n '1,1p' adresa2`
adresa2=$adresa2
curl  --limit-rate 100K     -k -A -k -s  $adresa2 > /tmp/test/adresa2
grep '</span></strong[^<]*' /tmp/test/adresa2 > /tmp/test/adresa3
grep -o -i 'C:[^<]*' /tmp/test/adresa3 > /tmp/test/adresa4
sed -i "s/c:/C:/" /tmp/test/adresa4
cat /tmp/test/adresa4 > /tmp/test/hotovo1
cat hotovo1 > CCcam.cfg



if grep -o -i 'C:[^<]*' CCcam.cfg ; then
grep -o -i 'C:[^<]*' CCcam.cfg  > /etc/CCcam.cfg
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
