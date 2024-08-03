#!/bin/sh
opkg remove dreamsatpanel
rm -rf /usr/lib/enigma2/python/Plugins/Extensions/DreamSat/
sleep 1
echo "stahuji plugin ...dreamsatpanel"
echo ""
cd /tmp
curl  -k -Lbk -m 55532 -m 555104 "https://drive.google.com/uc?id=1TIqu34-EOVx6oC02n3ABrXGrrK75YvP6&export=download" > /tmp/enigma2-plugin-extensions-dreamsatpanel_1.1_all.ipk
sleep 1
echo "instaluji ...."
cd /tmp
opkg install /tmp/enigma2-plugin-extensions-dreamsatpanel_1.1_all.ipk
echo ""
echo ""
echo ""
echo ""
echo ""
echo ""
echo ""
echo ""
sleep 1
rm /tmp/enigma2-plugin-extensions-dreamsatpanel_1.1_all.ipk
echo "OK"
killall -9 enigma2
exit

