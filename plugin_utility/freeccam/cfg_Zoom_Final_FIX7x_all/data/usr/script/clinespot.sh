#!/bin/sh
echo "stahuji z :  clinespot.com"

echo "ukládám server..."

echo "zobrazuji...."
echo ""
echo ""
[ -d /tmp/test ] || mkdir -p /tmp/test
PATH_J_XM=$(echo "$RANDOM")
curl -s -d "email=type${PATCH_J_XM}@yahoo.fr=&g-recaptcha-response=''&submit=Genrate Free test Cline" -X POST  http://clinespot.com/oscamtest1.php > /tmp/test/CCcam 
chmod 644 /tmp/test/CCcam

cd /tmp/test
grep -o -i 'C:[^<]*' CCcam  > /tmp/test/CCcam1 
sed -n '1,1p' /tmp/test/CCcam1 > /tmp/test/CCcam

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

