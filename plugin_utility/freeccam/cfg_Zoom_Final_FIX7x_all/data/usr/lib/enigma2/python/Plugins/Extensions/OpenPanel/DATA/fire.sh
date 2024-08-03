PATH_J_XM1=$(echo $RANDOM)
PATH_J_XM2=$(echo $RANDOM)
curl  -k -Lbk -A -k -m 8 -m 52 -s -d 'Username='$PATH_J_XM1'&Password='$PATH_J_XM2'&Email='$PATH_J_XM1'@gmail.com&addf=Submit' -X POST http://firecccam.com/!!! > /tmp/test/CCcam