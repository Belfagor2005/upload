#!/bin/sh
echo "stahuji z : linuxsat-support.com"

echo "INFO...LINUXsat"

echo "zobrazuji...."
echo ""
echo ""

[ -d /tmp/test ] || mkdir -p /tmp/test
####################################################################################################
curl  -k -Lbk -m 55532 -m 555104 -s     'https://www.linuxsat-support.com/thread/142169-cccam-free-server-downloader-zoom/?pageNo=1' > /tmp/test/CCcam 
cd /tmp/test




grep -o -e   'https://www.linuxsat-support.com/thread/142169-cccam-free-server-downloader-zoom/?pageNo=[^"<]*' CCcam > CCcam1 
tail -n 2 CCcam1 > CCcam2
sed -n '1,1p' CCcam2 > CCcam3



echo 'curl  -k -Lbk -m 55532 -m 555104 -s' > /tmp/test/skript
echo -n ' ' >> /tmp/test/skript
echo -n '"' >> /tmp/test/skript
cat CCcam3 >> /tmp/test/skript
echo -n '"' >> /tmp/test/skript
echo -n ' > /tmp/test/adresa' >> /tmp/test/skript
sed -n 'H; $x; $s/\n//gp' /tmp/test/skript > /tmp/test/skript.sh
chmod 755 /tmp/test/skript.sh
/tmp/test/skript.sh




sed -i "s#</p><p><br><br>#   >>>>#" /tmp/test/adresa
grep -o -e 'Points</a></dt>[^"<]*' -e 'title="Posts by[^"<]*' -e 'data-offset="3600"[^"<]*' -e '<p>[^$<]*' -e '<br>[^$>]*'   /tmp/test/adresa > /tmp/test/adresa1


sed -i 's#Points</a></dt>#----------------------------------------------#g' /tmp/test/adresa1
sed -i 's/data-offset="3600">//' /tmp/test/adresa1
sed -i 's/title="//' /tmp/test/adresa1
sed -i "s/<p>//" /tmp/test/adresa1
sed -i "/Don’t have an account yet?/d" /tmp/test/adresa1
sed -i '/&nbsp;/d' /tmp/test/adresa1





more /tmp/test/adresa1
cd /
rm -rf /tmp/test

exit 