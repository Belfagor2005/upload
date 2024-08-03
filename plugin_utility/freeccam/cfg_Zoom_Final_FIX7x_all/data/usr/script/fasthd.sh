#!/bin/sh
echo "stahuji z  ....fasthd.net"

echo "ukládám server..."

echo "zobrazuji...."
echo ""
echo ""
[ -d /tmp/test ] || mkdir -p /tmp/test

curl  --limit-rate 50K      -k -Lbk -A -k -m 8 -m 52 -s   http://www.fasthd.net/test2.php > /tmp/test/CCcam
Username=`sed -ne 's#.*Username"  value="\([^"]*\).*#\1#p' /tmp/test/CCcam`
Username=$Username
Password=`sed -ne 's#.*Password"  value="\([^"]*\).*#\1#p' /tmp/test/CCcam` 
Password=$Password
expiredate=`sed -ne 's#.*expiredate" value="\([^"]*\).*#\1#p' /tmp/test/CCcam` 
expiredate=$expiredate
expireshow=`sed -ne 's#.*name="expireshow" value="\([^"]*\).*#\1#p' /tmp/test/CCcam`  
expireshow=$expireshow
curl  --limit-rate 100K      -k -Lbk -A -k -m 8 -m 52 -s -d "Username=$Username&Password=$Password&expiredate=$expiredate&expireshow=$expireshow&addfree2hd=addfree2hd" -X POST http://www.fasthd.net/test2.php > /tmp/test/CCcam2
cd /tmp/test
grep -o -i 'C:[^<]*' CCcam2 > CCcam3
echo $Username >> CCcam3
echo $Password >> CCcam3

cd /

cd /tmp/test

if grep -o -i 'C:[^<]*' CCcam3 ; then
grep -o -i 'C:[^<]*' CCcam3  > /etc/CCcam.cfg
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