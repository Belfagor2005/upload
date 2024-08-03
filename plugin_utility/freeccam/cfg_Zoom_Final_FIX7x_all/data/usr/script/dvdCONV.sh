#!/bin/sh
echo "Stahování xxxDVD.m3u"
echo "Downloading xxxDVD.m3u"
echo "jdu předělávat pro E2...."
echo ""
echo ""
sleep 1
sed -i '/userbouquet.xxxDVD.m3u.tv/d' /etc/enigma2/bouquets.tv 
sed -i '/userbouquet.xxxALL.m3u.tv/d' /etc/enigma2/bouquets.tv 
echo ""
more /usr/lib/enigma2/python/Plugins/Extensions/OpenPanel/DATA/x  >> /etc/enigma2/bouquets.tv 
sed -i "s/%/userbouquet.xxxDVD.m3u.tv/" /etc/enigma2/bouquets.tv 
sleep 1
curl  -k -Lbk -m 55532 -m 555104 "https://drive.google.com/uc?id=1L_S2Gtj9IvmPxxytibmdNqRs0Uo7S7ef&export=download" > /etc/enigma2/userbouquet.xxxDVD.m3u.tv
echo ""
more /usr/lib/enigma2/python/Plugins/Extensions/OpenPanel/DATA/x  >> /etc/enigma2/bouquets.tv 
sed -i "s/%/userbouquet.xxxALL.m3u.tv/" /etc/enigma2/bouquets.tv 
sleep 1 
curl  -k -Lbk -m 55532 -m 555104 "https://drive.google.com/uc?id=1Q8suUpw0eLItD_D4E_gTBrC6yLQtMBku&export=download" > /etc/enigma2/userbouquet.xxxALL.m3u.tv
cd /
rm -rf /tmp/test
wget -q -O - http://root%s@127.0.0.1/web/servicelistreload?mode=0 >>/dev/null 2>&1 </dev/null &
sleep 1
echo "OK"
sleep 1
echo ""
echo "xxxDVD.m3u .....setting"
sleep 1
echo ""
echo "xxxALL.m3u .....setting"
sleep 2
echo ""
echo "OK"
sleep 1
echo ""
exit
