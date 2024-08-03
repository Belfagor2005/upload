#!/bin/sh
sleep 1
echo "aktivuji kopírování souboru (OscamDATAx.cfg)"
sleep 1
echo ""
echo "I activate file copying (OscamDATAx.cfg)"
sleep 2
rm -rf /usr/script/conv.sh
cp /usr/script/conv2.sh /usr/script/conv.sh
chmod 755 /usr/script/conv.sh
echo ""
sed -i '/dataXON.sh" confirmation="true" shortcut/s/ (OK)" target="/" target="/g' /etc/openpanel.xml
sed -i '/dataXOFF.sh" confirmation="true" shortcut/s/ (OK)" target="/" target="/g' /etc/openpanel.xml
echo ""
sed -i '/dataXON.sh" confirmation="true" shortcut/s/" target="/ (OK)" target="/g' /etc/openpanel.xml
echo ""
cp /etc/openpanel.xml /etc/panel/openpanel.xml
sleep 1
echo ""
echo "OK"
exit 