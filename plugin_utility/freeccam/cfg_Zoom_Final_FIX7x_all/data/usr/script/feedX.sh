#!/bin/sh
sleep 1
echo "stahuji feed + exteplayer3 pro AZBOX HD Elite"
echo ""
sleep 1
echo "pro OpenPLI 7.0 ver. !!DOM!!"
echo ""
sleep 1
echo "pouze pro instalaci s enigmou na USB"
echo ""
sleep 1
echo "pozor!! bude to chvilku trvat!"
echo ""
sleep 1
cd /tmp
curl  -k -Lbk -m 5532 -m 55104 "https://drive.google.com/uc?id=1gGe6m-aRBNn333bKIORXSg2pFmK4W3H7&export=download" > /tmp/ext3_Player_ServiceApp_all.ipk
sleep 1
echo "instaluji ...."
cd /tmp
opkg install /tmp/ext3_Player_ServiceApp_all.ipk
echo ""
echo ""
echo ""
echo ""
echo ""
echo ""
echo ""
echo ""
sleep 1
rm /tmp/ext3_Player_ServiceApp_all.ipk
echo "OK"
killall -9 enigma2
exit
