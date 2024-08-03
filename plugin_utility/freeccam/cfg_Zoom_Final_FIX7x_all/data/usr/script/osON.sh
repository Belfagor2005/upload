#!/bin/sh
echo "Nastavuji automatické vyhledání"
echo "a nahrazení každého ...oscam.server"
echo ""
echo ""
cp /usr/lib/enigma2/python/Plugins/Extensions/OpenPanel/DATA/conv.sh /usr/script/conv.sh
cp /usr/lib/enigma2/python/Plugins/Extensions/OpenPanel/DATA/conv.sh /usr/script/conv1.sh
echo ""
sed -i '/osON.sh" confirmation="true" shortcut/s/ (OK)" target="/" target="/g' /etc/openpanel.xml
sed -i '/osFF.sh" confirmation="true" shortcut/s/ (OK)" target="/" target="/g' /etc/openpanel.xml
echo ""
sed -i '/osON.sh" confirmation="true" shortcut/s/" target="/ (OK)" target="/g' /etc/openpanel.xml
echo ""
cp /etc/openpanel.xml /etc/panel/openpanel.xml
sleep 1
echo ".......ON"
sleep 1
echo "OK"


exit









