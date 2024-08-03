echo "switching menu to Polish"
rm /etc/openpanel.xml
cp /etc/LANG/PL/openpanel.xml /etc/
rm /etc/panel/openpanel.xml
cp /etc/LANG/PL/openpanel.xml /etc/panel/
rm /etc/panel/lite.xml
cp /etc/LANG/PL/lite.xml /etc/panel/
cat /usr/script/INFO/pl.sh > /usr/script/BUTTON.sh
exit
