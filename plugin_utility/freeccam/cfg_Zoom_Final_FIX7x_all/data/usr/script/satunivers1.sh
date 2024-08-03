#!/bin/sh
echo "stahuji z : satunivers.tv1"

echo "ukládám server..."

echo "zobrazuji...."
echo ""
echo ""
[ -d /tmp/test ] || mkdir -p /tmp/test

curl -k -A -k -s  http://infosat.satunivers.tv/cgn/index1.php > /tmp/test/CCcam
chmod 644 /tmp/test/CCcam

cd /tmp/test

echo "C: "  > hotovo
sed -ne 's#.*host: \([^<]*\).*#\1#p' CCcam >> hotovo
echo -n " "  >> hotovo
sed -ne 's#.*port: \([^<]*\).*#\1#p' CCcam >> hotovo

sed -ne 's#.*user: \([^<]*\).*#\1#p' CCcam >> hotovo
echo -n " "  >> hotovo
sed -ne 's#.*pass: \([^<]*\).*#\1#p' CCcam >> hotovo
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

