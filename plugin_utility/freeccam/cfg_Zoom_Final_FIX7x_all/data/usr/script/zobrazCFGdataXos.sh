#!/bin/sh
sleep 1
echo "zobrazuji Váše momentální .....OscamDATAx.cfg"
sleep 1
if [ -e "/etc/OscamDATAx.cfg" ]; then
echo ""
more /etc/OscamDATAx.cfg
sleep 1
echo ""
echo ""
echo "zobrazeno...!!!"
echo ""
sleep 2
echo ''
else
echo 'OscamDATAx.cfg ...prázdné nebo neexistuje!!'
echo ''
sleep 2
echo 'OscamDATAx.cfg ...empty or does not exist!!'
echo ''
exit
fi


exit 