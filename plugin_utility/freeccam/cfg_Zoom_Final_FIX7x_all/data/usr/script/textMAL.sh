#!/bin/sh
echo "switching TEXT to MOD... SLIM"
rm -rf /usr/lib/enigma2/python/Plugins/Extensions/OpenPanel/OpenPanelList.py
cp /usr/lib/enigma2/python/Plugins/Extensions/OpenPanel/DATA/OpenPanelListMAL.py /usr/lib/enigma2/python/Plugins/Extensions/OpenPanel/OpenPanelList.py
echo ""
echo ""
sed -i '/textVEL.sh" confirmation="true" shortcut="blue"/s/ (OK)" target="/" target="/g' /etc/openpanel.xml
sed -i '/textMAL.sh" confirmation="true" shortcut="red"/s/ (OK)" target="/" target="/g' /etc/openpanel.xml
echo ""
sed -i '/textMAL.sh" confirmation="true" shortcut="red"/s/" target="/ (OK)" target="/g' /etc/openpanel.xml
echo ""
cp /etc/openpanel.xml /etc/panel/openpanel.xml
echo ""
echo "OK"
sleep 1
echo "Restart....."
sleep 2
killall -9 enigma2
exit