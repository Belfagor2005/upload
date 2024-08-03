#!/bin/sh
echo ""
echo "restartuji..... **cam"

killbylls=`sed -n '1,1p' /tmp/c1`
killbylls=$killbylls

camino=`sed -n '1,1p' /tmp/c2`
camino=$camino

sleep 0
killall -9 $killbylls ; sleep 1 ; $camino >>/dev/null 2>&1 </dev/null &
echo ""
rm -rf /tmp/c1
rm -rf /tmp/c2
exit 0

