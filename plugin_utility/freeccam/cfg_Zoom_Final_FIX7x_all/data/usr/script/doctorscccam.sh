#!/bin/sh
echo "stahuji z : doctorscccam.ga"

echo "ukládám server..."

echo "zobrazuji...."
echo ""
echo ""
[ -d /tmp/test ] || mkdir -p /tmp/test

PATH_J_XM=$(echo "$((1000 + RANDOM % 9999))$((RANDOM % 9999))")
PATH_J_XM=$(echo "$((1000 + RANDOM % 9999))$((RANDOM % 9999))")
curl -s -d "Username=${PATH_J_XM}&formiid=${PATH_J_XM}&cline= ! ŘŁŘ·Ů„Ř¨ Ř§Ů„Ř˘Ů† " -X POST http://doctorscccam.ga/cccam/ > /tmp/test/CCcam

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

