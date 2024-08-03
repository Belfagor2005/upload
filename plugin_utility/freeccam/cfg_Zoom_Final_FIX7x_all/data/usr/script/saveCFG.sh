#!/bin/sh
echo "zálohuji Váš CCcam.cfg"
sleep 1
if [ -e "/usr/keys/CCcam.cfg" ]; then
cp /usr/keys/CCcam.cfg /etc/CCcam1.cfg
more /usr/keys/CCcam.cfg
echo '!!!/usr/keys/!!!'
elif [ -e "/etc/CCcam.cfg" ]; then
cp /etc/CCcam.cfg /etc/CCcam1.cfg
more /etc/CCcam.cfg
echo '!!!/etc/!!!'
fi
sleep 1
echo "uloženo...!!!"
exit
