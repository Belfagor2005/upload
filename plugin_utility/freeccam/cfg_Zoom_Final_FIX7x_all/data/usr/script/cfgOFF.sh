#!/bin/sh
sleep 1
echo "switching search (cfg) MOD...OFF"
sleep 1
echo "zapínám lokalizaci (cfg) (OFF)"
rm -rf /usr/script/najdiCFG.sh
echo ""
sed -i '/cfgON.sh" confirmation="true" shortcut/s/ (OK)" target="/" target="/g' /etc/openpanel.xml
sed -i '/cfgOFF.sh" confirmation="true" shortcut/s/ (OK)" target="/" target="/g' /etc/openpanel.xml
echo ""
sed -i '/cfgOFF.sh" confirmation="true" shortcut/s/" target="/ (OK)" target="/g' /etc/openpanel.xml
echo ""
cp /etc/openpanel.xml /etc/panel/openpanel.xml
echo ""
echo ""
echo ""
echo ""
sleep 1
echo "OK"
exit
