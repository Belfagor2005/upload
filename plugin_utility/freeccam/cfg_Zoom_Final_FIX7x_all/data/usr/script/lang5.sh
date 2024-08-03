echo "switching menu to Slovak"
rm /etc/openpanel.xml
cp /etc/LANG/SL/openpanel.xml /etc/
rm /etc/panel/openpanel.xml
cp /etc/LANG/SL/openpanel.xml /etc/panel/
rm /etc/panel/lite.xml
cp /etc/LANG/SL/lite.xml /etc/panel/
cat /usr/script/INFO/sl.sh > /usr/script/BUTTON.sh
exit
