#!/bin/sh
echo "vyhledávání m3u"
echo ""
sleep 1
echo "search m3u"
echo ""
sleep 1
echo "start"
find / -name \*.m3u | xargs -I {} cp {} /tmp/
find / -name \*.m3u8 | xargs -I {} cp {} /tmp/
echo ""
echo ""
echo "ukládám do /tmp/"
echo ""
sleep 1
echo "save to /tmp/"
sleep 1
echo "OK"
exit





