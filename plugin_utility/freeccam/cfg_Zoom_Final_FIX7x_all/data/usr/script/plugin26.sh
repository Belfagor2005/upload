#!/bin/sh
sleep 1
echo "stahuji netspeedtest"
echo ""
cd /tmp
curl  -k -Lbk -m 55532 -m 555104 "https://drive.google.com/uc?id=1MUKwgGWaCKdonUIS_m7xuAOel6zUpUjZ&export=download" > /tmp/enigma2-plugin-extensions-netspeedtest_1.0_all.ipk
sleep 1
echo "instaluji ...."
cd /tmp
opkg install /tmp/enigma2-plugin-extensions-netspeedtest_1.0_all.ipk
echo ""
echo ""
echo ""
echo ""
echo ""
echo ""
echo ""
echo ""
sleep 1
rm /tmp/enigma2-plugin-extensions-netspeedtest_1.0_all.ipk
echo "OK"
killall -9 enigma2
exit
