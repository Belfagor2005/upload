#!/bin/sh
echo "IP"
echo ".....?"
echo ""
echo ""
echo ""
sleep 0
if  /sbin/ip route |grep -o -i 'src[^<]*'|awk '{print $ 2}' >>/dev/null ; then
/sbin/ip route |grep -o -i 'src[^<]*'|awk '{print $ 2}'
sleep 0
echo ""
else
echo 'IP ...info'
sleep 2
echo ""
echo 'not found'
fi

exit
