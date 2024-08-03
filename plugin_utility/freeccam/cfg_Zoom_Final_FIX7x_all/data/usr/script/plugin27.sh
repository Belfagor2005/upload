#!/bin/sh
sleep 1
echo "stahuji SatVenusPANEL"
echo ""
cd /tmp
curl  -k -Lbk -m 55532 -m 555104 "https://drive.google.com/uc?id=1RvNBCQ5vM94njHQM8hhe6a-ICr5_1AVi&export=download" > /tmp/enigma2-plugin-extensions-satvenus-panel_7.3.2_all.ipk
sleep 1
echo "instaluji ...."
cd /tmp
opkg install /tmp/enigma2-plugin-extensions-satvenus-panel_7.3.2_all.ipk
echo ""
echo ""
echo ""
echo ""
echo ""
echo ""
echo ""
echo ""
sleep 1
rm /tmp/enigma2-plugin-extensions-satvenus-panel_7.3.2_all.ipk
echo "OK"
killall -9 enigma2
exit
