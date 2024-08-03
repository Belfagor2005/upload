#!/bin/sh
echo "navracím zpět Váš CCcam.cfg ze zálohy"
sleep 1
if [ -e "/usr/keys/CCcam.cfg" ]; then
cp /etc/CCcam1.cfg /usr/keys/CCcam.cfg
more /usr/keys/CCcam.cfg
echo '!!!/usr/keys/!!!'
elif [ -e "/etc/CCcam.cfg" ]; then
cp /etc/CCcam1.cfg /etc/CCcam.cfg
more /etc/CCcam.cfg
echo '!!!/etc/!!!'
fi
sleep 1
echo "uloženo...!!!"
exit
