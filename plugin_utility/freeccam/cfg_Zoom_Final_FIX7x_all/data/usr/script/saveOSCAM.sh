#!/bin/sh
echo "zálohuji Váš oscam.server"
cd /etc/tuxbox/config/
cp oscam.server oscam.server1.txt
cp oscam.server /tmp/readme.txt
sleep 1
more /tmp/readme.txt
rm /tmp/readme.txt
sleep 1
echo "uloženo...!!!"
exit
