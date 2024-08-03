echo "switching menu to Turkish"
rm /etc/openpanel.xml
cp /etc/LANG/TU/openpanel.xml /etc/
rm /etc/panel/openpanel.xml
cp /etc/LANG/TU/openpanel.xml /etc/panel/
rm /etc/panel/lite.xml
cp /etc/LANG/TU/lite.xml /etc/panel/
cat /usr/script/INFO/tu.sh > /usr/script/BUTTON.sh
exit
