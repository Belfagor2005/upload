#!/bin/sh
echo "Nastavuji automatické stažení serverů"
echo ".....po startu E2"
echo ""
echo ""
sed -i '/start/d' /etc/init.d/bootmisc.sh 
sleep 1
sed -i '/ exit /d' /etc/init.d/bootmisc.sh
echo "" >> /etc/init.d/bootmisc.sh 
echo "/usr/script/start.sh >/dev/null 2>&1 </dev/null &" >> /etc/init.d/bootmisc.sh
echo ": exit 0" >> /etc/init.d/bootmisc.sh
echo ""
sed -i '/aktivstart.sh" confirmation="true" shortcut="red"/s/ (OK)" target="/" target="/g' /etc/openpanel.xml
sed -i '/deaktivstart.sh" confirmation="true" shortcut="blue"/s/ (OK)" target="/" target="/g' /etc/openpanel.xml
echo ""
sed -i '/aktivstart.sh" confirmation="true" shortcut="red"/s/" target="/ (OK)" target="/g' /etc/openpanel.xml
echo ""
cp /etc/openpanel.xml /etc/panel/openpanel.xml
sleep 1
echo "hotvo..."
/usr/script/znovune.sh >/dev/null 2>&1 </dev/null &
exit









