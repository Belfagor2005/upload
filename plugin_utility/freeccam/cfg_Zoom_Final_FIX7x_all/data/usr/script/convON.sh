#!/bin/sh
echo "Aktivuji converzi"
echo "po stažení serverů"
echo ""
echo ""
rm -rf /usr/script/tichestart1.sh
cp  /usr/script/tichestart3.sh /usr/script/tichestart1.sh
chmod 755 /usr/script/tichestart1.sh
rm -rf /usr/script/conv.sh
cp  /usr/script/conv1.sh /usr/script/conv.sh
chmod 755 /usr/script/conv.sh
echo ""
sed -i '/convON.sh" confirmation="true" shortcut/s/ (OK)" target="/" target="/g' /etc/openpanel.xml
sed -i '/convOFF.sh" confirmation="true" shortcut/s/ (OK)" target="/" target="/g' /etc/openpanel.xml
echo ""
sed -i '/convON.sh" confirmation="true" shortcut/s/" target="/ (OK)" target="/g' /etc/openpanel.xml
echo ""
cp /etc/openpanel.xml /etc/panel/openpanel.xml
sleep 1
echo "OK..."
exit









