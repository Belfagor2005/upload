#!/bin/sh
echo "stahuji z : nebo.ddns.net"
sleep 1
echo "ukládám server..."
sleep 1
echo "zobrazuji...."
echo ""
echo ""
[ -d /tmp/test ] || mkdir -p /tmp/test

curl -k -A -k -s  http://nebo.ddns.net:8881/temp.php > /tmp/test/CCcam
chmod 644 /tmp/test/CCcam
cd /tmp/test
grep -o -i 'C:[^<]*' CCcam > CCcam1
cut -d '"' -f 1 CCcam1 > CCcam2


cat CCcam2  > /etc/CCcam.cfg 
cat CCcam2  > /tmp/readme.txt
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


