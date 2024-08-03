#!/bin/sh
sleep 40
/usr/script/tichestart1.sh >>/dev/null 2>&1 </dev/null &
cp /usr/script/upozor.sh /tmp/upozor.sh >>/dev/null 2>&1 </dev/null &
chmod 755 /tmp/upozor.sh >>/dev/null 2>&1 </dev/null &
exit 0