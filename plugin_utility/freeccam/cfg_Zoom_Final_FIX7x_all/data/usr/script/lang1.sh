echo "switching menu to English"
rm /etc/openpanel.xml
cp /etc/LANG/EN/openpanel.xml /etc/
rm /etc/panel/openpanel.xml
cp /etc/LANG/EN/openpanel.xml /etc/panel/
rm /etc/panel/lite.xml
cp /etc/LANG/EN/lite.xml /etc/panel/
cat /usr/script/INFO/en.sh > /usr/script/BUTTON.sh
exit
