#!/bin/sh
echo 1
echo "stahuji seznam CZ SK TV+Rádio"
echo ""
echo "bude staženo jako m3u"
echo ""
rm -rf /movie
[ -d /movie ] || mkdir -p /movie
curl -k -A -k https://database.freetuxtv.net/playlists/playlist_webtv_cs.m3u > /movie/CZtv.m3u
curl -k -A -k https://database.freetuxtv.net/playlists/playlist_webradio_cs.m3u > /movie/CZrádio.m3u
curl -k -A -k https://database.freetuxtv.net/playlists/playlist_webtv_sk.m3u > /movie/SKtv.m3u
curl -k -A -k https://database.freetuxtv.net/playlists/playlist_webradio_sk.m3u > /movie/SKrádio.m3u
curl -k -A -k 'http://radia.tode.cz/download-playlist.php?type=all&format=m3u' |tr -d '\r\032'|sed '/^$/d' > /movie/CZrádio2.m3u 
echo 1
echo "seznam hotov..."
echo ""
echo 1
echo "uloženo jako (m3u) do..../movie/"
exit

