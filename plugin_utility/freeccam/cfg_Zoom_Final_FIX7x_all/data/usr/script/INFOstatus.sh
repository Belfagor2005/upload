#!/bin/sh
echo "Oscam,Ncam"

echo "...status"
[ -d /tmp/test ] || mkdir -p /tmp/test

find /etc/ -name \*ncam.conf | xargs -I {} cp {} /tmp/test/ncam >>/dev/null
find /etc/ -name \*oscam.conf | xargs -I {} cp {} /tmp/test/oscam >>/dev/null
grep -i 'httpport' /tmp/test/ncam  > /tmp/test/ncam1 2> /dev/null
cut -d '=' -f 2 /tmp/test/ncam1 > /tmp/test/ncam2
sed -i 's# ##g' /tmp/test/ncam2
grep -i 'httpport' /tmp/test/oscam  > /tmp/test/oscam1 2> /dev/null
cut -d '=' -f 2 /tmp/test/oscam1 > /tmp/test/oscam2
sed -i 's# ##g' /tmp/test/oscam2
sleep 0
port1=`cat /tmp/test/ncam2`
port1=$port1
port2=`cat /tmp/test/oscam2`
port2=$port2
sleep 0
echo ""
echo ""
echo ""

sleep 0
if  curl -k -A -k -s  http://127.0.0.1:$port1/status.html >>/dev/null ; then
  [ -d /tmp/test ] || mkdir -p /tmp/test
  cd /tmp/test
  sleep 0
  curl -k -A -k -s  http://127.0.0.1:$port1/status.html > /tmp/test/CCcam
  grep -i 'CONNECTED' CCcam  > CCcam1
  sed -i 's#<TD CLASS="statuscol16">CONNECTED<BR><A HREF="entitlements.html?label=#CONNECTED #g' CCcam1
  sed -i 's#" CLASS="tooltip1">##g' CCcam1
  sed -i 's#<BR>reshare1=0<BR>reshare2=0<BR>resharex=0</SPAN></A></TD>##g' CCcam1
  sed -i 's#<BR>##g' CCcam1
  sed -i 's#<SPAN>##g' CCcam1
  cut -d '_' -f 1  CCcam1 > CCcam2
  cut -d '<' -f 1  CCcam2 > CCcam3
  grep -o -i 'CONNECTED[^<]*' CCcam3 > CCcam4
  cat CCcam4
  echo ""
  cd /
  rm -rf /tmp/test
  
elif  curl -k -A -k -s  http://127.0.0.1:$port2/status.html >>/dev/null ; then
  [ -d /tmp/test ] || mkdir -p /tmp/test
  cd /tmp/test
  sleep 0
  curl -k -A -k -s  http://127.0.0.1:$port2/status.html > /tmp/test/CCcam
  grep -i 'CONNECTED' CCcam  > CCcam1
  sed -i 's#<TD CLASS="statuscol16">CONNECTED<BR><A HREF="entitlements.html?label=#CONNECTED #g' CCcam1
  sed -i 's#" CLASS="tooltip1">##g' CCcam1
  sed -i 's#<BR>reshare1=0<BR>reshare2=0<BR>resharex=0</SPAN></A></TD>##g' CCcam1
  sed -i 's#<BR>##g' CCcam1
  sed -i 's#<SPAN>##g' CCcam1
  cut -d '_' -f 1  CCcam1 > CCcam2
  cut -d '<' -f 1  CCcam2 > CCcam3
  grep -o -i 'CONNECTED[^<]*' CCcam3 > CCcam4
  cat CCcam4
  echo ""
  cd /
  rm -rf /tmp/test
  
elif  curl -k -A -k -s  http://127.0.0.1:16001/servers >>/dev/null ; then
  [ -d /tmp/test ] || mkdir -p /tmp/test
  cd /tmp/test
  sleep 0
  curl -k -A -k -s  http://127.0.0.1:16001/servers > /tmp/test/CCcam
  cat CCcam
  echo ""
  cd /
  rm -rf /tmp/test 
  
  
  else
  echo 'Oscam,Ncam ...status'
  sleep 2
  echo 'not found'

fi

rm -rf /tmp/test
exit
