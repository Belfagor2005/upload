#!/bin/sh
sleep 1
echo "zobrazuji Váše momentální .....CCcamDATAx.cfg"
sleep 1
if [ -e "/etc/CCcamDATAx.cfg" ]; then
echo ""
more /etc/CCcamDATAx.cfg
sleep 1
echo ""
echo ""
echo "zobrazeno...!!!"
echo ""
sleep 2
pocet1=`wc -l < /etc/CCcamDATAx.cfg`
pocet1=$pocet1
echo "SERVERS..... "$pocet1
echo ''
else
echo 'CCcamDATAx.cfg ...prázdné nebo neexistuje!!'
echo ''
sleep 2
echo 'CCcamDATAx.cfg ...empty or does not exist!!'
echo ''
exit
fi


exit 