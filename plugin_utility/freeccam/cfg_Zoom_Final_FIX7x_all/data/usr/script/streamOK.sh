#!/bin/sh
echo "pokouším se o aktualizaci"
opkg update
opkg install ffmpeg
opkg install exteplayer3
opkg install enigma2-plugin-systemplugins-serviceapp
sleep 1
echo "hotovo"
sleep 1
echo "nyní provedu restart...."
sleep 2
killall -9 enigma2
exit