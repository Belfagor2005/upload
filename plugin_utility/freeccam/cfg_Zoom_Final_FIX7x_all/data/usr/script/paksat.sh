#!/bin/sh
echo "stahuji z :  paksat.pk"

echo "ukládám server..."

echo "zobrazuji...."
echo ""
echo ""
[ -d /tmp/test/test ] || mkdir -p /tmp/test/test
cd /tmp/test

curl  -k -Lbk -A -k -m 488 -m 552 -s  https://paksat.pk/testline.php > /tmp/test/CCcam
sed -ne 's#.*Username" value="\([^"<]*\).*#\1#p' /tmp/test/CCcam > /tmp/test/a
sed -ne 's#.*Password" value="\([^"<]*\).*#\1#p' /tmp/test/CCcam > /tmp/test/b
PATCH_J_XM=$(cat /tmp/test/a)
PATCH_J_XM2=$(cat /tmp/test/b)
echo "C: f3.kcccam.com 15505" > řádek
cat /tmp/test/b >> řádek
cat /tmp/test/a >> řádek
sed '$!N;s/\n/ /' řádek  > řádek1
sed '$!N;s/\n/ /' řádek1  > CCcam

if grep -o -i 'C:[^<]*' CCcam ; then
grep -o -i 'C:[^<]*' CCcam  > /etc/CCcam.cfg
else
echo 'server není k dispozici!'
echo ""
sleep 2
echo 'the server is not available!'
echo ""
echo ""
echo ""
rm -rf /tmp/test/test
exit
fi

cd /
rm -rf /tmp/test/test



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
