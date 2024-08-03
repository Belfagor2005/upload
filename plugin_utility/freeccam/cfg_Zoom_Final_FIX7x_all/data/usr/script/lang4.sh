echo "přepínám menu do Češtiny"
rm /etc/openpanel.xml
cp /etc/LANG/CZ/openpanel.xml /etc/
rm /etc/panel/openpanel.xml
cp /etc/LANG/CZ/openpanel.xml /etc/panel/
rm /etc/panel/lite.xml
cp /etc/LANG/CZ/lite.xml /etc/panel/
cat /usr/script/INFO/cz.sh > /usr/script/BUTTON.sh
exit
