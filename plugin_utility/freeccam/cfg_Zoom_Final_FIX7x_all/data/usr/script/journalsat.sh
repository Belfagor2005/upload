#!/bin/sh
echo "stahuji z : journalsat.com"

echo "ukládám server..."

echo "zobrazuji...."
echo ""
echo ""
[ -d /tmp/test ] || mkdir -p /tmp/test

curl  -s -k -Lbk -A -k -m 8 -m 52 -d "do=cccam&doccam=generate"  http://cccam.journalsat.com/index.php http://cccam.journalsat.com/get.php?do=cccam/ -X POST > /tmp/test/CCcam
sed -ne 's#.*<th colspan="2">\([^<]*\).*#\1#p' /tmp/test/CCcam > /tmp/test/CCcam1
cd /tmp/test

if grep -o -i 'C:[^<]*' CCcam1 ; then
grep -o -i 'C:[^<]*' CCcam1  > /etc/CCcam.cfg
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

