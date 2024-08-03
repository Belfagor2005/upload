#!/bin/sh
echo "přesouvám CCcam.cfg"
sleep 1
if [ -e "/usr/keys/CCcam.cfg" ]; then
echo '/usr/keys/---> /etc/'
sleep 1
cp /usr/keys/CCcam.cfg /etc/
more /etc/CCcam.cfg
echo 'přesunuto...!!!'
sleep 1
echo '!!!/etc/!!!...OK'
rm -rf /usr/keys/CCcam.cfg
elif [ -e "/etc/CCcam.cfg" ]; then
echo '(cfg) už je v /etc/'
fi
exit
