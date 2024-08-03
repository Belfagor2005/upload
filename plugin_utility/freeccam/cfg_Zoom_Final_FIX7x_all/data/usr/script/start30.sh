#!/bin/sh
sleep 1
echo "nastavuji stažení na 30 vteřin od startu E2"
sleep 1
echo ""
echo "I set the download to 30 seconds from the start of E2"
sleep 2
sed -i 's/sleep 10/\sleep 30/g' /usr/script/start.sh
sed -i 's/sleep 20/\sleep 30/g' /usr/script/start.sh
sed -i 's/sleep 30/\sleep 30/g' /usr/script/start.sh
sed -i 's/sleep 40/\sleep 30/g' /usr/script/start.sh
sed -i 's/sleep 50/\sleep 30/g' /usr/script/start.sh
echo ""
sed -i '/start10.sh/s/ (OK)" target="/" target="/g' /etc/openpanel.xml
sed -i '/start20.sh/s/ (OK)" target="/" target="/g' /etc/openpanel.xml
sed -i '/start30.sh/s/ (OK)" target="/" target="/g' /etc/openpanel.xml
sed -i '/start40.sh/s/ (OK)" target="/" target="/g' /etc/openpanel.xml
sed -i '/start50.sh/s/ (OK)" target="/" target="/g' /etc/openpanel.xml
echo ""
sed -i '/start30.sh/s/" target="/ (OK)" target="/g' /etc/openpanel.xml
echo ""
cp /etc/openpanel.xml /etc/panel/openpanel.xml
sleep 1
echo ""
echo "OK"
exit 