#!/bin/sh
echo "stahuji z : satdz.net"

echo "ukládám server..."

echo "zobrazuji...."
echo ""
echo ""
[ -d /tmp/test ] || mkdir -p /tmp/test

PATH_X=$(echo "$((1000 + RANDOM % 9999))$((RANDOM % 9999))")
curl  --limit-rate 100K     -s -k -Lbk -A -k -m 8 -m 52 -d 'Username='$(echo "$PATH_X")'&Password='$(echo "$PATH_X")'&addf1= Activation   '  -X POST http://cccam.satdz.net/5day/index.php http://cccam.satdz.net/5day/get.php  > /tmp/test/CCcam
sed -ne "s#.*CCCAM</font><br></center><center><font size='5' color='black' >\([^<]*\).*#\1#p" /tmp/test/CCcam > /tmp/test/CCcam1
cd /tmp/test

if grep -o -i 'C:[^<]*' CCcam1 ; then
grep -o -i 'C:[^<]*' CCcam1  > /tmp/test/soubor1
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
####################################################################################################
PATH_X=$(echo "$((1000 + RANDOM % 9999))$((RANDOM % 9999))")
curl  --limit-rate 100K     -s -k -Lbk -A -k -m 8 -m 52 -d 'Username='$(echo "$PATH_X")'&Password='$(echo "$PATH_X")'&addf1= Activation   '  -X POST http://cccam.satdz.net/3day/cccam/index.php http://cccam.satdz.net/3day/cccam/get.php  > /tmp/test/CCcam
sed -ne "s#.*CCCAM</font><br></center><center><font size='5' color='black' >\([^<]*\).*#\1#p" /tmp/test/CCcam > /tmp/test/CCcam1
cd /tmp/test

if grep -o -i 'C:[^<]*' CCcam1 ; then
grep -o -i 'C:[^<]*' CCcam1  > /tmp/test/soubor2
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
####################################################################################################
cat soubor1 soubor2 > /etc/CCcam.cfg

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

