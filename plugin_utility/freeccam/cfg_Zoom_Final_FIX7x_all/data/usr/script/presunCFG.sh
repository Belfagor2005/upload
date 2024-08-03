#!/bin/sh
echo "přesouvám CCcam.cfg"
sleep 1
if [ -e "/etc/CCcam.cfg" ]; then
echo '/etc/---> /usr/keys/'
sleep 1
cp /etc/CCcam.cfg /usr/keys/
more /usr/keys/CCcam.cfg
echo 'přesunuto...!!!'
sleep 1
echo '!!!/usr/keys/!!!...OK'
rm -rf /etc/CCcam.cfg
elif [ -e "/usr/keys/CCcam.cfg" ]; then
echo '(cfg) už je v /usr/keys/'
fi
exit







