echo "switching menu to English"
rm /etc/openpanel.xml
cp /etc/ENG/openpanel.xml /etc/
rm -rf /etc/panel
cp -a /etc/ENG/panel /etc/
exit