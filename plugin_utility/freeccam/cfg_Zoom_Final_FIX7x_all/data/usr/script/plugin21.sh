#!/bin/sh
echo "stahuji AddonsPanel od Levi45"
sleep 1
cd /tmp
curl  -k -Lbk -m 55532 -m 555104 "https://drive.google.com/uc?id=1NvMzp6Cw26Ky1FkMnVomi2mpI-XvuNHR&export=download" > /tmp/enigma2-plugin-extensions-levi45-addonsmanager_2.8_all.ipk
sleep 1
echo "instaluji ...."
cd /tmp
opkg install /tmp/enigma2-plugin-extensions-levi45-addonsmanager_2.8_all.ipk
echo ""
echo ""
echo ""
echo ""
echo ""
echo ""
echo ""
echo ""
sleep 1
rm /tmp/enigma2-plugin-extensions-levi45-addonsmanager_2.8_all.ipk
sleep 2
killall -9 enigma2
exit
