#!/bin/sh
echo "Deaktivuji automatické vyhledání"
echo "a nahrazení každého ...oscam.server"
echo ""
echo ""
sed -i '/xargs/d' /usr/script/conv.sh 
sed -i '/xargs/d' /usr/script/conv1.sh 
echo ""
sed -i '/osON.sh" confirmation="true" shortcut/s/ (OK)" target="/" target="/g' /etc/openpanel.xml
sed -i '/osFF.sh" confirmation="true" shortcut/s/ (OK)" target="/" target="/g' /etc/openpanel.xml
echo ""
sed -i '/osFF.sh" confirmation="true" shortcut/s/" target="/ (OK)" target="/g' /etc/openpanel.xml
echo ""
cp /etc/openpanel.xml /etc/panel/openpanel.xml
sleep 1
echo ".......OFF"
sleep 1
echo "OK"





exit









