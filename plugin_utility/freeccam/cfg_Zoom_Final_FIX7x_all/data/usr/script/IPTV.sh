#!/bin/sh
echo "stahuji (m3u) IPTV"
echo ""
echo ""
[ -d /IPTV ] || mkdir -p /IPTV
rm -rf /IPTV
[ -d /IPTV ] || mkdir -p /IPTV
curl  -k -Lbk -m 55532 -m 555104 "https://drive.google.com/uc?id=1S7bmru3T6Z1y8_2zGyOCfwFys1HE2LyK&export=download" > /IPTV/IPTV.m3u
curl  -k -Lbk -m 55532 -m 555104 "https://drive.google.com/uc?id=1IlY1yBxU9hnP7pHNhQ2WaVfEevfnH4Oy&export=download" > /IPTV/X.m3u
[ -d /IPTV/Adult ] || mkdir -p /IPTV/Adult
[ -d /IPTV/Ru ] || mkdir -p /IPTV/Ru
curl  -k -Lbk -A -k -m 8 -m 52   https://webarmen.com/my/iptv/auto.xxx.m3u > /IPTV/Adult/x.m3u
curl  -k -Lbk -A -k -m 8 -m 52   http://adultiptv.net/lists/all.m3u > /IPTV/Adult/xx.m3u
curl  -k -Lbk -A -k -m 8 -m 52   http://adultiptv.net/vods.m3u8 > /IPTV/Adult/xxx.m3u
curl  -k -Lbk -A -k -m 8 -m 52   https://webarmen.com/my/iptv/auto.all.m3u > /IPTV/Ru/Rus.m3u
curl  -k -Lbk -A -k -m 8 -m 52   https://iptv-org.github.io/iptv/index.sfw.m3u > /IPTV/IPTV3.m3u
[ -d /tmp/test ] || mkdir -p /tmp/test
curl  -s -k -Lbk -A -k -m 8 -m 52 -d 'do=cccam&doccam=generate' -X POST  http://iptv.journalsat.com/index.php http://iptv.journalsat.com/get.php?do=cccam/  > /tmp/test/CCcam
grep   'type=m3u&output=mpegts[^<]*' /tmp/test/CCcam > /tmp/test/CCcam1
sed 's/\([ ]\+\)/\n\1/g' /tmp/test/CCcam1 > /tmp/test/CCcam2
grep -o -i 'href=[^<]*' /tmp/test/CCcam2 > /tmp/test/CCcam3
sed -e "s/href=/curl -Lbk -m 4555 -m 6555 -k /" /tmp/test/CCcam3 > /tmp/test/CCcam4
echo -n " > /tmp/test/iptv" >> /tmp/test/CCcam4
sed '$!N;s/\n/ /' /tmp/test/CCcam4 > /tmp/test/iptv.sh
chmod 755 /tmp/test/iptv.sh
sleep 1
/tmp/test/iptv.sh >>/dev/null 2>&1 </dev/null &
sleep 1
cat /tmp/test/iptv > /IPTV/IPTV2.m3u
echo ""
echo ""
echo ""
sleep 1
echo "OK"
sleep 1
echo "staženo do /IPTV/"
sleep 1
rm -rf /tmp/test
exit 