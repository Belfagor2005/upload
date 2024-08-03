#!/bin/sh
echo "stahuji plugin ...pseudo FAST SCAN"
cd /tmp
curl  -k -Lbk -m 55532 -m 555104 "https://drive.google.com/uc?id=1dUEYvoMSLJAhcL4s0uVG3bcgBDy36L7H&export=download" > /tmp/enigma2-plugin-systemplugins-pseudofastscanfree_6.1-20220207_all.ipk
sleep 1
echo "instaluji plugin...."
cd /tmp
opkg install /tmp/enigma2-plugin-systemplugins-pseudofastscanfree_6.1-20220207_all.ipk
echo ""
echo ""
echo ""
echo ""
echo ""
echo ""
echo ""
echo ""
sleep 1
rm /tmp/enigma2-plugin-systemplugins-pseudofastscanfree_6.1-20220207_all.ipk
sleep 2
killall -9 enigma2
exit