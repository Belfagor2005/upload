#!/bin/sh
sleep 1
echo "Stahuji SETTING ...ver2 "
echo ""
sleep 1
echo "Skylink Astra 3A"
opkg remove set
sleep 1
echo ""
cd /tmp
curl  -k -Lbk -m 55532 -m 555104 "https://drive.google.com/uc?id=1Vl8OPkz3mVjRascZ1B_rtXj4ZCx4MQKb&export=download" > /tmp/set_Skylink_ASTRA3a2_all.ipk
sleep 1
echo "instaluji ...."
cd /tmp
opkg install /tmp/set_Skylink_ASTRA3a2_all.ipk
echo ""
echo ""
echo ""
echo ""
echo ""
echo ""
echo ""
echo ""
sleep 1
rm /tmp/set_Skylink_ASTRA3a2_all.ipk
echo "OK"
killall -9 enigma2
exit 

