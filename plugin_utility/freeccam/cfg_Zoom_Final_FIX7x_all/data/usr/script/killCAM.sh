#!/bin/sh
sleep 1
echo "KILL all CAM"
sleep 1
echo "vypínám všechny CAMy"

  if [ -f  "/etc/systemd/system.conf" ] || [ -f "/usr/lib/python2.7/urllib.pyo" ]; then 
if [ -d '/usr/lib/enigma2/python/Plugins/PLi' ];then
aux=''
else
aux='aux'
fi
else
aux=''
  fi
  if [ "`ps "$aux"|grep -v 'grep'|grep -ic  'cccam'`" -gt '0' ]; then
killbylls=`ps "$aux"| grep -v grep | grep cam|sed -n '1p' | grep -oi  '/usr.*'|sed -n '1p' | grep -oi 'cccam.*' | cut -d' ' -f1` 
elif [ "`ps "$aux"|grep -v 'grep'|grep -ic  'oscam'`" -gt '0' ]; then
killbylls=`ps "$aux"| grep -v grep | grep cam|sed -n '1p' | grep -oi  '/usr.*'|sed -n '1p' | grep -oi 'oscam.*' | cut -d' ' -f1`
elif [ "`ps "$aux"|grep -v 'grep'|grep -ic  'ncam'`" -gt '0' ]; then
killbylls=`ps "$aux"| grep -v grep | grep cam|sed -n '1p' | grep -oi  '/usr.*'|sed -n '1p' | grep -oi 'ncam.*' | cut -d' ' -f1`
elif [ "`ps "$aux"|grep -v 'grep'|grep -ic  'gcam'`" -gt '0' ]; then
killbylls=`ps "$aux"| grep -v grep | grep cam|sed -n '1p' | grep -oi  '/usr.*'|sed -n '1p' | grep -oi 'gcam.*' | cut -d' ' -f1`
  fi

killall -9 "$killbylls" >>/dev/null 2>&1 </dev/null &
killall -9 CCcam >>/dev/null 2>&1 </dev/null &
killall -9 oscam >>/dev/null 2>&1 </dev/null &
killall -9 ncam >>/dev/null 2>&1 </dev/null &
killall -9 gcam >>/dev/null 2>&1 </dev/null &
echo "OK"
exit