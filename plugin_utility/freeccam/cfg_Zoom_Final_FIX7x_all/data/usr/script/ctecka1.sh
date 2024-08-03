#!/bin/sh
sleep 1
echo "Kopíruji (cfg) pro čtečku"
more /usr/lib/enigma2/python/Plugins/Extensions/OpenPanel/DATA/CCcam.cfg >> /etc/CCcam.cfg
cp /etc/CCcam.cfg /tmp/readme.txt
more /tmp/readme.txt
rm /tmp/readme.txt
sleep 1
/usr/script/restarthlavni.sh >/dev/null 2>&1 </dev/null &
echo ""
echo "Hotovo..."

exit
