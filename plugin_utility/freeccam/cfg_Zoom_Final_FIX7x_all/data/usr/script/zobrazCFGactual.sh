#!/bin/sh
sleep 1
echo "zobrazuji Váše momentální CCcam.cfg"
sleep 1
if [ -e "/usr/keys/CCcam.cfg" ]; then
more /usr/keys/CCcam.cfg
echo ""
sleep 2
pocet1=`wc -l < /usr/keys/CCcam.cfg`
pocet1=$pocet1
echo "SERVERS..... "$pocet1
echo '!!!/usr/keys/!!!'
elif [ -e "/etc/CCcam.cfg" ]; then
more /etc/CCcam.cfg
echo ""
sleep 2
pocet1=`wc -l < /etc/CCcam.cfg`
pocet1=$pocet1
echo "SERVERS..... "$pocet1
echo '!!!/etc/!!!'
fi


exit 