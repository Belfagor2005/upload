echo "switching menu to Russian"
rm /etc/openpanel.xml
cp /etc/LANG/RU/openpanel.xml /etc/
rm /etc/panel/openpanel.xml
cp /etc/LANG/RU/openpanel.xml /etc/panel/
rm /etc/panel/lite.xml
cp /etc/LANG/RU/lite.xml /etc/panel/
cat /usr/script/INFO/ru.sh > /usr/script/BUTTON.sh
exit
