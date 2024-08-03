#!/bin/sh
[ -d /movie ] || mkdir -p /movie
mkdir -p /usr/lib/enigma2/python/Plugins/Extensions/XBMCAddons/XBMC/plugin.video.m3u.player/playlists
echo "stahuji z : eporner.com/cat/hd-1080p/"



echo "jdu předělávat na (m3u)...."
echo ""
echo ""

URL="https://www.eporner.com/cat/hd-1080p/";
# Files
TMP=`mktemp -d`
cd / ${TMP}

# Github
#agent="--header='User-Agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_0) AppleWebKit/600.1.17 (KHTML, like Gecko) Version/8.0 Safari/600.1.17'"
#crt="--no-check-certificate"

#wget -q $crt $agent $URL/CCcam
curl -s -Lbk -m 4 -m 6 -k ${URL}/CCcam -o CCcam
sed -n '221,282p' CCcam > CCcam1
cut -c 177-187 CCcam1  > CCcam2
echo "#EXTINF:-1,x1" > m3u.m3u
echo "https://www.eporner.com/dload/" > test 
sed -n '1,1p' CCcam2 >> test
cat test | tr -d '\n' >> m3u.m3u
echo "/1080/3372081-1080p.mp4" >> m3u.m3u
####################################################################################################
echo "#EXTINF:-1,x2" >> m3u.m3u
echo "https://www.eporner.com/dload/" > test 
sed -n '2,2p' CCcam2 >> test
cat test | tr -d '\n' >> m3u.m3u
echo "/1080/3372081-1080p.mp4" >> m3u.m3u
################################################
echo "#EXTINF:-1,x3" >> m3u.m3u
echo "https://www.eporner.com/dload/" > test 
sed -n '3,3p' CCcam2 >> test
cat test | tr -d '\n' >> m3u.m3u
echo "/1080/3372081-1080p.mp4" >> m3u.m3u
################################################
echo "#EXTINF:-1,x4" >> m3u.m3u
echo "https://www.eporner.com/dload/" > test 
sed -n '4,4p' CCcam2 >> test
cat test | tr -d '\n' >> m3u.m3u
echo "/1080/3372081-1080p.mp4" >> m3u.m3u
################################################
echo "#EXTINF:-1,x5" >> m3u.m3u
echo "https://www.eporner.com/dload/" > test 
sed -n '5,5p' CCcam2 >> test
cat test | tr -d '\n' >> m3u.m3u
echo "/1080/3372081-1080p.mp4" >> m3u.m3u
################################################
echo "#EXTINF:-1,x6" >> m3u.m3u
echo "https://www.eporner.com/dload/" > test 
sed -n '6,6p' CCcam2 >> test
cat test | tr -d '\n' >> m3u.m3u
echo "/1080/3372081-1080p.mp4" >> m3u.m3u
################################################
echo "#EXTINF:-1,x7" >> m3u.m3u
echo "https://www.eporner.com/dload/" > test 
sed -n '7,7p' CCcam2 >> test
cat test | tr -d '\n' >> m3u.m3u
echo "/1080/3372081-1080p.mp4" >> m3u.m3u
################################################
echo "#EXTINF:-1,x8" >> m3u.m3u
echo "https://www.eporner.com/dload/" > test 
sed -n '8,8p' CCcam2 >> test
cat test | tr -d '\n' >> m3u.m3u
echo "/1080/3372081-1080p.mp4" >> m3u.m3u
################################################
echo "#EXTINF:-1,x9" >> m3u.m3u
echo "https://www.eporner.com/dload/" > test 
sed -n '9,9p' CCcam2 >> test
cat test | tr -d '\n' >> m3u.m3u
echo "/1080/3372081-1080p.mp4" >> m3u.m3u
################################################
echo "#EXTINF:-1,x10" >> m3u.m3u
echo "https://www.eporner.com/dload/" > test 
sed -n '10,10p' CCcam2 >> test
cat test | tr -d '\n' >> m3u.m3u
echo "/1080/3372081-1080p.mp4" >> m3u.m3u
################################################
echo "#EXTINF:-1,x11" >> m3u.m3u
echo "https://www.eporner.com/dload/" > test 
sed -n '11,11p' CCcam2 >> test
cat test | tr -d '\n' >> m3u.m3u
echo "/1080/3372081-1080p.mp4" >> m3u.m3u
################################################
echo "#EXTINF:-1,x12" >> m3u.m3u
echo "https://www.eporner.com/dload/" > test 
sed -n '12,12p' CCcam2 >> test
cat test | tr -d '\n' >> m3u.m3u
echo "/1080/3372081-1080p.mp4" >> m3u.m3u
################################################
echo "#EXTINF:-1,x13" >> m3u.m3u
echo "https://www.eporner.com/dload/" > test 
sed -n '13,13p' CCcam2 >> test
cat test | tr -d '\n' >> m3u.m3u
echo "/1080/3372081-1080p.mp4" >> m3u.m3u
################################################
echo "#EXTINF:-1,x14" >> m3u.m3u
echo "https://www.eporner.com/dload/" > test 
sed -n '14,14p' CCcam2 >> test
cat test | tr -d '\n' >> m3u.m3u
echo "/1080/3372081-1080p.mp4" >> m3u.m3u
################################################
echo "#EXTINF:-1,x15" >> m3u.m3u
echo "https://www.eporner.com/dload/" > test 
sed -n '15,15p' CCcam2 >> test
cat test | tr -d '\n' >> m3u.m3u
echo "/1080/3372081-1080p.mp4" >> m3u.m3u
################################################
echo "#EXTINF:-1,x16" >> m3u.m3u
echo "https://www.eporner.com/dload/" > test 
sed -n '16,16p' CCcam2 >> test
cat test | tr -d '\n' >> m3u.m3u
echo "/1080/3372081-1080p.mp4" >> m3u.m3u
################################################
echo "#EXTINF:-1,x17" >> m3u.m3u
echo "https://www.eporner.com/dload/" > test 
sed -n '17,17p' CCcam2 >> test
cat test | tr -d '\n' >> m3u.m3u
echo "/1080/3372081-1080p.mp4" >> m3u.m3u
################################################
echo "#EXTINF:-1,x18" >> m3u.m3u
echo "https://www.eporner.com/dload/" > test 
sed -n '18,18p' CCcam2 >> test
cat test | tr -d '\n' >> m3u.m3u
echo "/1080/3372081-1080p.mp4" >> m3u.m3u
################################################
echo "#EXTINF:-1,x19" >> m3u.m3u
echo "https://www.eporner.com/dload/" > test 
sed -n '19,19p' CCcam2 >> test
cat test | tr -d '\n' >> m3u.m3u
echo "/1080/3372081-1080p.mp4" >> m3u.m3u
################################################
echo "#EXTINF:-1,x20" >> m3u.m3u
echo "https://www.eporner.com/dload/" > test 
sed -n '20,20p' CCcam2 >> test
cat test | tr -d '\n' >> m3u.m3u
echo "/1080/3372081-1080p.mp4" >> m3u.m3u
################################################
echo "#EXTINF:-1,x21" >> m3u.m3u
echo "https://www.eporner.com/dload/" > test 
sed -n '21,21p' CCcam2 >> test
cat test | tr -d '\n' >> m3u.m3u
echo "/1080/3372081-1080p.mp4" >> m3u.m3u
################################################
echo "#EXTINF:-1,x22" >> m3u.m3u
echo "https://www.eporner.com/dload/" > test 
sed -n '22,22p' CCcam2 >> test
cat test | tr -d '\n' >> m3u.m3u
echo "/1080/3372081-1080p.mp4" >> m3u.m3u
################################################
echo "#EXTINF:-1,x23" >> m3u.m3u
echo "https://www.eporner.com/dload/" > test 
sed -n '23,23p' CCcam2 >> test
cat test | tr -d '\n' >> m3u.m3u
echo "/1080/3372081-1080p.mp4" >> m3u.m3u
################################################
echo "#EXTINF:-1,x24" >> m3u.m3u
echo "https://www.eporner.com/dload/" > test 
sed -n '24,24p' CCcam2 >> test
cat test | tr -d '\n' >> m3u.m3u
echo "/1080/3372081-1080p.mp4" >> m3u.m3u
################################################
echo "#EXTINF:-1,x25" >> m3u.m3u
echo "https://www.eporner.com/dload/" > test 
sed -n '25,25p' CCcam2 >> test
cat test | tr -d '\n' >> m3u.m3u
echo "/1080/3372081-1080p.mp4" >> m3u.m3u
################################################
echo "#EXTINF:-1,x26" >> m3u.m3u
echo "https://www.eporner.com/dload/" > test 
sed -n '26,26p' CCcam2 >> test
cat test | tr -d '\n' >> m3u.m3u
echo "/1080/3372081-1080p.mp4" >> m3u.m3u
################################################
echo "#EXTINF:-1,x27" >> m3u.m3u
echo "https://www.eporner.com/dload/" > test 
sed -n '27,27p' CCcam2 >> test
cat test | tr -d '\n' >> m3u.m3u
echo "/1080/3372081-1080p.mp4" >> m3u.m3u
################################################
echo "#EXTINF:-1,x28" >> m3u.m3u
echo "https://www.eporner.com/dload/" > test 
sed -n '28,28p' CCcam2 >> test
cat test | tr -d '\n' >> m3u.m3u
echo "/1080/3372081-1080p.mp4" >> m3u.m3u
################################################
echo "#EXTINF:-1,x29" >> m3u.m3u
echo "https://www.eporner.com/dload/" > test 
sed -n '29,29p' CCcam2 >> test
cat test | tr -d '\n' >> m3u.m3u
echo "/1080/3372081-1080p.mp4" >> m3u.m3u
################################################
echo "#EXTINF:-1,x30" >> m3u.m3u
echo "https://www.eporner.com/dload/" > test 
sed -n '30,30p' CCcam2 >> test
cat test | tr -d '\n' >> m3u.m3u
echo "/1080/3372081-1080p.mp4" >> m3u.m3u
################################################
echo "#EXTINF:-1,x31" >> m3u.m3u
echo "https://www.eporner.com/dload/" > test 
sed -n '31,31p' CCcam2 >> test
cat test | tr -d '\n' >> m3u.m3u
echo "/1080/3372081-1080p.mp4" >> m3u.m3u
################################################
echo "#EXTINF:-1,x32" >> m3u.m3u
echo "https://www.eporner.com/dload/" > test 
sed -n '32,32p' CCcam2 >> test
cat test | tr -d '\n' >> m3u.m3u
echo "/1080/3372081-1080p.mp4" >> m3u.m3u
################################################
echo "#EXTINF:-1,x33" >> m3u.m3u
echo "https://www.eporner.com/dload/" > test 
sed -n '33,33p' CCcam2 >> test
cat test | tr -d '\n' >> m3u.m3u
echo "/1080/3372081-1080p.mp4" >> m3u.m3u
################################################
echo "#EXTINF:-1,x34" >> m3u.m3u
echo "https://www.eporner.com/dload/" > test 
sed -n '34,34p' CCcam2 >> test
cat test | tr -d '\n' >> m3u.m3u
echo "/1080/3372081-1080p.mp4" >> m3u.m3u
################################################
echo "#EXTINF:-1,x35" >> m3u.m3u
echo "https://www.eporner.com/dload/" > test 
sed -n '35,35p' CCcam2 >> test
cat test | tr -d '\n' >> m3u.m3u
echo "/1080/3372081-1080p.mp4" >> m3u.m3u
################################################
echo "#EXTINF:-1,x36" >> m3u.m3u
echo "https://www.eporner.com/dload/" > test 
sed -n '36,36p' CCcam2 >> test
cat test | tr -d '\n' >> m3u.m3u
echo "/1080/3372081-1080p.mp4" >> m3u.m3u
################################################
echo "#EXTINF:-1,x37" >> m3u.m3u
echo "https://www.eporner.com/dload/" > test 
sed -n '37,37p' CCcam2 >> test
cat test | tr -d '\n' >> m3u.m3u
echo "/1080/3372081-1080p.mp4" >> m3u.m3u
################################################
echo "#EXTINF:-1,x38" >> m3u.m3u
echo "https://www.eporner.com/dload/" > test 
sed -n '38,38p' CCcam2 >> test
cat test | tr -d '\n' >> m3u.m3u
echo "/1080/3372081-1080p.mp4" >> m3u.m3u
################################################
echo "#EXTINF:-1,x39" >> m3u.m3u
echo "https://www.eporner.com/dload/" > test 
sed -n '39,39p' CCcam2 >> test
cat test | tr -d '\n' >> m3u.m3u
echo "/1080/3372081-1080p.mp4" >> m3u.m3u
################################################
echo "#EXTINF:-1,x40" >> m3u.m3u
echo "https://www.eporner.com/dload/" > test 
sed -n '40,40p' CCcam2 >> test
cat test | tr -d '\n' >> m3u.m3u
echo "/1080/3372081-1080p.mp4" >> m3u.m3u
################################################
echo "#EXTINF:-1,x41" >> m3u.m3u
echo "https://www.eporner.com/dload/" > test 
sed -n '41,41p' CCcam2 >> test
cat test | tr -d '\n' >> m3u.m3u
echo "/1080/3372081-1080p.mp4" >> m3u.m3u
################################################
echo "#EXTINF:-1,x42" >> m3u.m3u
echo "https://www.eporner.com/dload/" > test 
sed -n '42,42p' CCcam2 >> test
cat test | tr -d '\n' >> m3u.m3u
echo "/1080/3372081-1080p.mp4" >> m3u.m3u
################################################
echo "#EXTINF:-1,x43" >> m3u.m3u
echo "https://www.eporner.com/dload/" > test 
sed -n '43,43p' CCcam2 >> test
cat test | tr -d '\n' >> m3u.m3u
echo "/1080/3372081-1080p.mp4" >> m3u.m3u
################################################
echo "#EXTINF:-1,x44" >> m3u.m3u
echo "https://www.eporner.com/dload/" > test 
sed -n '44,44p' CCcam2 >> test
cat test | tr -d '\n' >> m3u.m3u
echo "/1080/3372081-1080p.mp4" >> m3u.m3u
################################################
echo "#EXTINF:-1,x45" >> m3u.m3u
echo "https://www.eporner.com/dload/" > test 
sed -n '45,45p' CCcam2 >> test
cat test | tr -d '\n' >> m3u.m3u
echo "/1080/3372081-1080p.mp4" >> m3u.m3u
################################################
echo "#EXTINF:-1,x46" >> m3u.m3u
echo "https://www.eporner.com/dload/" > test 
sed -n '46,46p' CCcam2 >> test
cat test | tr -d '\n' >> m3u.m3u
echo "/1080/3372081-1080p.mp4" >> m3u.m3u
################################################
echo "#EXTINF:-1,x47" >> m3u.m3u
echo "https://www.eporner.com/dload/" > test 
sed -n '47,47p' CCcam2 >> test
cat test | tr -d '\n' >> m3u.m3u
echo "/1080/3372081-1080p.mp4" >> m3u.m3u
################################################
echo "#EXTINF:-1,x48" >> m3u.m3u
echo "https://www.eporner.com/dload/" > test 
sed -n '48,48p' CCcam2 >> test
cat test | tr -d '\n' >> m3u.m3u
echo "/1080/3372081-1080p.mp4" >> m3u.m3u
################################################
echo "#EXTINF:-1,x49" >> m3u.m3u
echo "https://www.eporner.com/dload/" > test 
sed -n '49,49p' CCcam2 >> test
cat test | tr -d '\n' >> m3u.m3u
echo "/1080/3372081-1080p.mp4" >> m3u.m3u
################################################
echo "#EXTINF:-1,50x" >> m3u.m3u
echo "https://www.eporner.com/dload/" > test 
sed -n '50,50p' CCcam2 >> test
cat test | tr -d '\n' >> m3u.m3u
echo "/1080/3372081-1080p.mp4" >> m3u.m3u
################################################
echo "#EXTINF:-1,x51" >> m3u.m3u
echo "https://www.eporner.com/dload/" > test 
sed -n '51,51p' CCcam2 >> test
cat test | tr -d '\n' >> m3u.m3u
echo "/1080/3372081-1080p.mp4" >> m3u.m3u
################################################
echo "#EXTINF:-1,x52" >> m3u.m3u
echo "https://www.eporner.com/dload/" > test 
sed -n '52,52p' CCcam2 >> test
cat test | tr -d '\n' >> m3u.m3u
echo "/1080/3372081-1080p.mp4" >> m3u.m3u
################################################
echo "#EXTINF:-1,x53" >> m3u.m3u
echo "https://www.eporner.com/dload/" > test 
sed -n '53,53p' CCcam2 >> test
cat test | tr -d '\n' >> m3u.m3u
echo "/1080/3372081-1080p.mp4" >> m3u.m3u
################################################
echo "#EXTINF:-1,x54" >> m3u.m3u
echo "https://www.eporner.com/dload/" > test 
sed -n '54,54p' CCcam2 >> test
cat test | tr -d '\n' >> m3u.m3u
echo "/1080/3372081-1080p.mp4" >> m3u.m3u
################################################
echo "#EXTINF:-1,x55" >> m3u.m3u
echo "https://www.eporner.com/dload/" > test 
sed -n '55,55p' CCcam2 >> test
cat test | tr -d '\n' >> m3u.m3u
echo "/1080/3372081-1080p.mp4" >> m3u.m3u
################################################
echo "#EXTINF:-1,x56" >> m3u.m3u
echo "https://www.eporner.com/dload/" > test 
sed -n '56,56p' CCcam2 >> test
cat test | tr -d '\n' >> m3u.m3u
echo "/1080/3372081-1080p.mp4" >> m3u.m3u
################################################
echo "#EXTINF:-1,x57" >> m3u.m3u
echo "https://www.eporner.com/dload/" > test 
sed -n '57,57p' CCcam2 >> test
cat test | tr -d '\n' >> m3u.m3u
echo "/1080/3372081-1080p.mp4" >> m3u.m3u
################################################
echo "#EXTINF:-1,x58" >> m3u.m3u
echo "https://www.eporner.com/dload/" > test 
sed -n '58,58p' CCcam2 >> test
cat test | tr -d '\n' >> m3u.m3u
echo "/1080/3372081-1080p.mp4" >> m3u.m3u
################################################
echo "#EXTINF:-1,x59" >> m3u.m3u
echo "https://www.eporner.com/dload/" > test 
sed -n '59,59p' CCcam2 >> test
cat test | tr -d '\n' >> m3u.m3u
echo "/1080/3372081-1080p.mp4" >> m3u.m3u
################################################
echo "#EXTINF:-1,x60" >> m3u.m3u
echo "https://www.eporner.com/dload/" > test 
sed -n '60,60p' CCcam2 >> test
cat test | tr -d '\n' >> m3u.m3u
echo "/1080/3372081-1080p.mp4" >> m3u.m3u
################################################
cp m3u.m3u /movie/xxx1080p.m3u
cp m3u.m3u /usr/lib/enigma2/python/Plugins/Extensions/XBMCAddons/XBMC/plugin.video.m3u.player/playlists/xxx1080p.m3u

echo ""
echo ""
echo "uloženo v složce (movie)...."
cd /tmp/
rm -r *
exit