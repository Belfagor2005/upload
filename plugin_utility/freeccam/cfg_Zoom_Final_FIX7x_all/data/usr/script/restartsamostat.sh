#!/bin/sh
echo "restartuji **cam"
echo "MOD ...ON"

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
killbylls=`ps "$aux"| grep -v grep | grep -i cam|sed -n '1p' | grep -oi  '/usr.*'|sed -n '1p' | grep -oi 'cccam.*' | cut -d' ' -f1` 
elif [ "`ps "$aux"|grep -v 'grep'|grep -ic  'oscam'`" -gt '0' ]; then
killbylls=`ps "$aux"| grep -v grep | grep -i cam|sed -n '1p' | grep -oi  '/usr.*'|sed -n '1p' | grep -oi 'oscam.*' | cut -d' ' -f1`
elif [ "`ps "$aux"|grep -v 'grep'|grep -ic  'ncam'`" -gt '0' ]; then
killbylls=`ps "$aux"| grep -v grep | grep -i cam|sed -n '1p' | grep -oi  '/usr.*'|sed -n '1p' | grep -oi 'ncam.*' | cut -d' ' -f1`
elif [ "`ps "$aux"|grep -v 'grep'|grep -ic  'gcam'`" -gt '0' ]; then
killbylls=`ps "$aux"| grep -v grep | grep -i cam|sed -n '1p' | grep -oi  '/usr.*'|sed -n '1p' | grep -oi 'gcam.*' | cut -d' ' -f1`
  fi

camino=`ps -w "$aux"| grep -v grep | grep -i cam | sed -n '1p' | grep -oi  '/usr.*'|sed -n '1p'`
if [ "`echo "$camino"|grep -ci 'oscam'`" -gt '0' ] && [ "`echo "$camino"|grep -c '\-b'`" = '0' ]; then
camino=$camino' -b'
fi
killall -9 "$killbylls" ; sleep 1 ; $camino >>/dev/null 2>&1 </dev/null &

exit 0