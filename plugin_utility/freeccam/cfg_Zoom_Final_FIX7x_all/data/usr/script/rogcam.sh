#!/bin/sh
echo "stahuji z :  rogcam.com"

echo "ukládám server..."

echo "zobrazuji...."
echo ""
echo ""
[ -d /tmp/test ] || mkdir -p /tmp/test

curl -k -A -k -s -X POST --data "name=barrym&get=get" https://www.rogcam.com/free/ https://www.rogcam.com/newfree.php > /tmp/test/CCcam 
cd /tmp/test
grep -o -i "var host = '[^'<]*" CCcam  > /tmp/test/host
sed -i "s#var host = '##g" /tmp/test/host
grep -o -i "html('User : [^'<]*" CCcam > /tmp/test/user
sed -i "s#html('User : # #g" /tmp/test/user
grep -o -i "html('Pass : [^'<]*" CCcam > /tmp/test/pass
sed -i "s#html('Pass : # #g" /tmp/test/pass
cat host user pass > /tmp/test/spojeno
sed -n 'H; $x; $s/\n//gp' spojeno > /tmp/test/CCcam

cd /tmp/test

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

