#!/bin/sh
echo "stahuji z : tvlivepro.com"

echo "ukládám server..."

echo "zobrazuji...."
echo ""
echo ""
[ -d /tmp/test ] || mkdir -p /tmp/test

curl    -k -A -k -s  https://www.tvlivepro.com/free_cccam_48h/ > /tmp/test/CCcam
cd /tmp/test
grep   'Host  </th><th>[^<]*' CCcam > CCcam1
sed -i "s#</th></tr><th id='t1'># #g" CCcam1 
sed -i "s#</th><th>##g" CCcam1 
sed -i "s#Host #C:#g" CCcam1
sed -i "s#Port  ##g" CCcam1
sed -i "s#User  ##g" CCcam1
sed -i "s#Password  ##g" CCcam1
grep -o -i 'C:[^<]*' CCcam1 > CCcam


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


