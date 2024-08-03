#!/bin/sh
echo "stahuji z : testcline.com"
sleep 1
echo "ukládám server..."
sleep 1
echo "zobrazuji...."
echo ""
echo ""
[ -d /tmp/test ] || mkdir -p /tmp/test

curl -k -A -k -s  https://testcline.com/free-cccam-server.php > /tmp/test/CCcam
chmod 644 /tmp/test/CCcam


cd /tmp/test
grep -o -i 'C:[^<]*' CCcam > CCcam1

cat CCcam1  > /etc/CCcam.cfg 
cat CCcam1  > /tmp/readme.txt
sleep 1
cd /
more /tmp/readme.txt
rm /tmp/readme.txt
rm -rf /tmp/test



echo ""
echo ""
echo ""
sleep 1
echo "stahování proběhlo úspěšně."
echo ">>>>>>>>>>>>>>>>>>>>>>>>>>>"
sleep 1
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
