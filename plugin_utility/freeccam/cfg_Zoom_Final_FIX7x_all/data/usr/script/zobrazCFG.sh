#!/bin/sh
sleep 1
echo "zobrazuji Váše zálohované CCcam.cfg"
sleep 1


if [ -e "/etc/CCcam1.cfg" ]; then
more /etc/CCcam1.cfg
sleep 1
echo "zobrazeno...!!!"
echo ""
sleep 2
pocet1=`wc -l < /etc/CCcam1.cfg`
pocet1=$pocet1
echo "SERVERS..... "$pocet1
echo ''
else
echo 'záloha neexistuje!!'
echo ''
sleep 2
echo 'the backup does not exist!!'
echo ''
exit
fi

exit
