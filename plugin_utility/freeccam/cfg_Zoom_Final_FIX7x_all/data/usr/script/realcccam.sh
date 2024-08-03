#!/bin/sh
echo "stahuji z : realcccam.com"

echo "ukládám server..."

echo "zobrazuji...."
echo ""
echo ""
[ -d /tmp/test ] || mkdir -p /tmp/test
PATH_J_XM1=$(echo "$((1000 + RANDOM % 9999))$((RANDOM % 9999))")
PATH_J_XM2=$(echo "$((1000 + RANDOM % 9999))$((RANDOM % 9999))")
curl -s -d 'Username='$PATH_J_XM1'&Password='$PATH_J_XM2'&addf=2 Days Free Cccam' -X POST  https://realcccam.com/freecccam/index.php > /tmp/test/CCcam

cd /tmp/test
sed -ne '/Server :/ p' CCcam > CCcam1
sed -ne 's#.*Server \([^<]*\).*#\1#p' CCcam1 > hotovo
sed -ne 's#.*Port :\([^<]*\).*#\1#p' CCcam1 >> hotovo
sed -ne 's#.*User :\([^<]*\).*#\1#p' CCcam1 >> hotovo
sed -ne 's#.*Pass :\([^<]*\).*#\1#p' CCcam1 >> hotovo
sed -n 'H; $x; $s/\n//gp' hotovo > hotovo1
sed -e "s/:/C:/" hotovo1 > CCcam


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

