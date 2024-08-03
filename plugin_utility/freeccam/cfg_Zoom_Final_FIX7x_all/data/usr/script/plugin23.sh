#!/bin/sh
echo "aktivuji Adult"
sleep 1
echo "pro seasondream-NG"
chmod 755 /usr/lib/enigma2/python/Plugins/Extensions/SeasondreamNG/control/adult_content
chmod 755 /usr/lib/enigma2/python/Plugins/Extensions/SeasondreamNG/control/default_skin
/usr/lib/enigma2/python/Plugins/Extensions/SeasondreamNG/control/adult_content enable
sleep 1
echo "hotovo"
exit
