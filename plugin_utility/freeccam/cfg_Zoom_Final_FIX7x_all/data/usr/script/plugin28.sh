#!/bin/sh
sleep 1
echo "stahuji Tetris"
echo ""
cd /tmp
curl  -k -Lbk -m 55532 -m 555104 "https://drive.google.com/uc?id=1n6hgfg5vPmC9jjuRuiZcwZYQoL97E6cO&export=download" > /tmp/enigma2-plugin-extensions-tetris_0.1_all.ipk
sleep 1
echo "instaluji ...."
cd /tmp
opkg install /tmp/enigma2-plugin-extensions-tetris_0.1_all.ipk
echo ""
echo ""
echo ""
echo ""
echo ""
echo ""
echo ""
echo ""
sleep 1
rm /tmp/enigma2-plugin-extensions-tetris_0.1_all.ipk
echo "OK"
killall -9 enigma2
exit
