#!/bin/sh
echo "za 30 vteřin vytvořím foto"
echo ""
echo "I'll create a photo in 30 seconds"
echo ""
[ -d /photo ] || mkdir -p /photo
echo ""
/usr/script/photoSTART.sh >>/dev/null 2>&1 </dev/null &
exit 
