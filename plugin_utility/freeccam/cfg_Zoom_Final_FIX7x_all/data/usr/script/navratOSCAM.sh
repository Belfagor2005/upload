#!/bin/sh
echo "navracím zpět Váš oscam.server ze zálohy"
cd /etc/tuxbox/config/
cp oscam.server1.txt oscam.server
cp oscam.server1.txt /tmp/readme.txt
sleep 1
more /tmp/readme.txt
rm /tmp/readme.txt
sleep 1
echo "uloženo...!!!"
exit
