#!/bin/sh
cd /
OUTPUT2='/tmp/servery'
echo -n "Converting ....."
FS=" "      
cat /etc/CCcam.cfg |grep -i "^C:.*"|while read line ; do
F1=$(echo $line|cut -d"$FS" -f1)
SERVER=$(echo $line|cut -d"$FS" -f2)
PORT=$(echo $line|cut -d"$FS" -f3)
USER=$(echo $line|cut -d"$FS" -f4)
PASS=$(echo $line|cut -d"$FS" -f5)
#echo "SERVER: $SERVER PORT: $PORT USER: $USER PASS: $PASS"
echo -n "."
echo "[reader]" >> $OUTPUT2
echo "label = $SERVER" >> $OUTPUT2
echo "protocol = cccam" >> $OUTPUT2
echo "device = $SERVER,$PORT" >> $OUTPUT2
echo "user = $USER" >> $OUTPUT2		
echo "password = $PASS" >> $OUTPUT2		
echo "disablecrccws_only_for = 0E00:000000,0500:030B00,050F00;098C:000000;09C4:000000" >> $OUTPUT2
echo "inactivitytimeout = 30" >> $OUTPUT2
echo "group = 1" >> $OUTPUT2
echo "cccversion = 2.3.2" >> $OUTPUT2
echo "ccckeepalive = 1" >> $OUTPUT2
echo "audisabled = 0" >> $OUTPUT2
echo "disablecrccws = 0" >> $OUTPUT2 				
echo "" >> $OUTPUT2
done
cp /tmp/servery /etc/tuxbox/config/oscam/oscam.server  >/dev/null 2>&1 </dev/null &
sleep 0
cp /tmp/servery /etc/tuxbox/config/oscam_atv_free/oscam.server  >/dev/null 2>&1 </dev/null &
sleep 0
cp /tmp/servery /etc/tuxbox/config/oscam.server  >/dev/null 2>&1 </dev/null &
sleep 0
cp /tmp/servery /etc/tuxbox/config/gcam.server  >/dev/null 2>&1 </dev/null &
sleep 0
cp /tmp/servery /etc/tuxbox/config/ncam.server  >/dev/null 2>&1 </dev/null &
sleep 0
rm -rf /tmp/servery
/usr/script/restart.sh >>/dev/null 2>&1 </dev/null &
exit 

