#!/bin/sh
echo "Plugin ONLINE....INFO"
echo ""
sleep 1
echo "Zoom server Downloader"
sleep 1
echo ""
echo ""
echo ""

if curl  -k -Lbk -m 55532 -m 555104 -s "https://drive.google.com/uc?id=1eAnnQHCoDFzZIdplU76TF_jvWzOc4KDN&export=download" > /tmp/info.txt ; then
more /tmp/info.txt
rm /tmp/info.txt
else
echo 'server není k dispozici!'
echo ""
sleep 2
echo 'the server is not available!'
echo ""
echo ""
echo ""
exit
fi

exit 

