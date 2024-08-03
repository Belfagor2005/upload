#!/bin/sh
echo "stahuji plugin KodiLite 5.0"
cd /tmp
curl  -k -Lbk -m 55532 -m 555104 "https://drive.google.com/uc?id=16KPAzkTvHe6vDUy8Ew8n6rMkyjPdiqx5&export=download" > /tmp/enigma2-plugin-extensions-kodilite_5.0_r0_all.ipk
sleep 1
echo "instaluji plugin...."
cd /tmp
opkg install /tmp/enigma2-plugin-extensions-kodilite_5.0_r0_all.ipk
echo ""
echo ""
echo ""
echo ""
echo ""
echo ""
echo ""
echo ""
sleep 1
rm /tmp/enigma2-plugin-extensions-kodilite_5.0_r0_all.ipk
sleep 2
killall -9 enigma2
exit
