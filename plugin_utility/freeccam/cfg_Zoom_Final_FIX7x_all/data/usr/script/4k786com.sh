#!/bin/sh
echo "stahuji z : 4k786.com"

echo "ukládám server..."

echo "zobrazuji...."
echo ""
echo ""
[ -d /tmp/test ] || mkdir -p /tmp/test
PATH_J_XM1=$(echo "$((1000 + RANDOM % 9999))$((RANDOM % 9999))")
PATH_J_XM2=$(echo "$((1000 + RANDOM % 9999))$((RANDOM % 9999))")
curl curl  --limit-rate 35K -Lbk -m 4555 -m 6555 -k -s -d 'Username='$PATH_J_XM1'&Password='$PATH_J_XM2'&addf=2 Days Free Cccam' -X POST  https://4k786.com/freecccam/index.php > /tmp/test/CCcam
chmod 644 /tmp/test/CCcam
cd /tmp/test

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