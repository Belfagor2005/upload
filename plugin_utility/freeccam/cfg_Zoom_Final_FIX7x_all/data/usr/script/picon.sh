#!/bin/sh
sleep 1
echo "Stahuji PICON ... "
echo ""
sleep 1
echo "Pozor!!! Potřebné místo.... 5Mb"
[ -d /tmp/test ] || mkdir -p /tmp/test
curl  -k -Lbk -m 55532 -m 555104  "https://www.dropbox.com/s/4ghk3pxtusnf98m/picon.zip?dl=1" > /tmp/test/picon.zip
rm -rf /usr/share/enigma2/picon
sleep 1
unzip /tmp/test/picon.zip -d /usr/share/enigma2/
chmod 644 /usr/share/enigma2/picon
sleep 1
cd /
rm -rf /tmp/test
echo ""
sleep 1
echo "OK"
sleep 2
echo ""
echo "REBOOTING!!!!"
sleep 2
echo ""
reboot
exit
