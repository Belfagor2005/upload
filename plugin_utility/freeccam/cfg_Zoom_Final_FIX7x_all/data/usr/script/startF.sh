#!/bin/sh
echo ""
echo "please wait 30sec......"
echo ""
sleep 30
cp /usr/script/upozor1.sh /tmp/upozor1.sh >>/dev/null 2>&1 </dev/null &
chmod 755 /tmp/upozor1.sh >>/dev/null 2>&1 </dev/null &
sleep 3
/usr/script/FILTR.sh 
exit 0