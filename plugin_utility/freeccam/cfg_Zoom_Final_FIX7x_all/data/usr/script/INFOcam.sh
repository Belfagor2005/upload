#!/bin/sh
echo "INFO ..CAM"

echo "..."
[ -d /tmp/test ] || mkdir -p /tmp/test

find /etc/ -name \*ncam.conf | xargs -I {} cp {} /tmp/test/ncam >>/dev/null
find /etc/ -name \*oscam.conf | xargs -I {} cp {} /tmp/test/oscam >>/dev/null
grep -i 'httpport' /tmp/test/ncam  > /tmp/test/ncam1 2> /dev/null
cut -d '=' -f 2 /tmp/test/ncam1 > /tmp/test/ncam2
sed -i 's# ##g' /tmp/test/ncam2
grep -i 'httpport' /tmp/test/oscam  > /tmp/test/oscam1 2> /dev/null
cut -d '=' -f 2 /tmp/test/oscam1 > /tmp/test/oscam2
sed -i 's# ##g' /tmp/test/oscam2
sleep 0
port1=`cat /tmp/test/ncam2`
port1=$port1
port2=`cat /tmp/test/oscam2`
port2=$port2
sleep 0
echo ""
echo ""
echo ""

echo ""
echo ""      /sbin/ip route |grep -o -i 'src[^<]*'|awk '{print $ 2}'
echo ""

sleep 0
if  curl -k -A -k -s  http://127.0.0.1:$port1/ >>/dev/null ; then
[ -d /tmp/test ] || mkdir -p /tmp/test
cd /tmp/test
sleep 0
curl -k -A -k -s  http://127.0.0.1:$port1/ > /tmp/test/CCcam
grep -i '<title>' CCcam  > CCcam1
sed -i 's#<title>##g' CCcam1
sed -i 's#</title>##g' CCcam1
echo "CAM ...."
echo ""
sleep 2
cat CCcam1
echo ""
cd /
rm -rf /tmp/test
elif curl -k -A -k -s  http://127.0.0.1:$port2/ >>/dev/null ; then
cd /tmp/test
sleep 0
curl -k -A -k -s  http://127.0.0.1:$port2/ > /tmp/test/CCcam
grep -i '<title>' CCcam  > CCcam1
sed -i 's#<title>##g' CCcam1
sed -i 's#</title>##g' CCcam1
echo "CAM ...."
echo ""
sleep 2
cat CCcam1
echo ""
cd /
rm -rf /tmp/test
elif curl -k -A -k -s  http://127.0.0.1:16001/ >>/dev/null ; then
cd /tmp/test
sleep 0
curl -k -A -k -s  http://127.0.0.1:16001/ > /tmp/test/CCcam
grep -i '<title>' CCcam  > CCcam1
sed -i 's#<title>##g' CCcam1
sed -i 's#</title>##g' CCcam1
echo "CAM ...."
echo ""
sleep 2
sed 's/\([>]\+\)/\n\1/g' CCcam1 > CCcam2
grep -i 'CCcam' CCcam2
echo ""
cd /
rm -rf /tmp/test
else
echo '...'
sleep 2
echo 'not found'
fi

exit
