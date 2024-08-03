#!/bin/sh
if [ ! -e "/usr/bin/curl" ]; then
echo 'CURL INFO....'
echo ''
sleep 1
echo 'CURL nebyl nalezen!'
sleep 1
echo 'nejspíš ho nemáš nainstalovaný banáne!'
sleep 3
echo ''
echo 'CURL not found!'
sleep 1
echo 'you probably dont have a banana :-) installed!'
else
echo 'CURL INFO....'
echo ''
sleep 1
echo 'CURL byl nalezen'
echo ""
sleep 2
echo 'CURL OK'
echo ""
sleep 2
echo 'version....'
echo ""
sleep 2
curl --version
fi
sleep 1
echo ""
echo ""
exit 
