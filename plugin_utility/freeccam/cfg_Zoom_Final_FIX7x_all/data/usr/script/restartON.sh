#!/bin/sh
sleep 1
echo "nastavuji restart CAM* po stažení serverů"
sleep 1
echo ""
echo "After downloading the servers, I activate the CAM* restart"
sleep 2
rm -rf /usr/script/restart.sh
cp /usr/lib/enigma2/python/Plugins/Extensions/OpenPanel/DATA/restart.sh /usr/script/restart.sh
chmod 755 /usr/script/restart.sh
rm -rf /usr/script/tichestart1.sh
cp /usr/script/tichestart3.sh /usr/script/tichestart1.sh
chmod 755 /usr/script/tichestart1.sh
echo ""
sed -i '/restartON.sh" confirmation="true" shortcut=""/s/ (OK)" target="/" target="/g' /etc/openpanel.xml
sed -i '/restartOFF.sh" confirmation="true" shortcut=""/s/ (OK)" target="/" target="/g' /etc/openpanel.xml
echo ""
sed -i '/restartON.sh" confirmation="true" shortcut=""/s/" target="/ (OK)" target="/g' /etc/openpanel.xml
echo ""
cp /etc/openpanel.xml /etc/panel/openpanel.xml
sleep 1
echo ""
echo "OK"
exit 