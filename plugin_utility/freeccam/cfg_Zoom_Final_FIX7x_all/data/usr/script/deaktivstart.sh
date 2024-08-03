#!/bin/sh
echo "Deaktivuji automatické stažení serverů"
echo ".....po startu E2"
echo ""
echo ""
sed -i '/start/d' /etc/init.d/bootmisc.sh 
rm -rf /usr/script/aktivstart.sh
cp /usr/lib/enigma2/python/Plugins/Extensions/OpenPanel/DATA/akt/aktivstart.sh /usr/script/
chmod 755 /usr/script/aktivstart.sh
echo ""
sed -i '/aktivstart.sh" confirmation="true" shortcut="red"/s/ (OK)" target="/" target="/g' /etc/openpanel.xml
sed -i '/deaktivstart.sh" confirmation="true" shortcut="blue"/s/ (OK)" target="/" target="/g' /etc/openpanel.xml
echo ""
sed -i '/deaktivstart.sh" confirmation="true" shortcut="blue"/s/" target="/ (OK)" target="/g' /etc/openpanel.xml
echo ""
cp /etc/openpanel.xml /etc/panel/openpanel.xml
sleep 1
echo "hotvo..."
exit




















