#!/bin/sh
echo "...FILTR (OK) servers"
rm -rf /tmp/ncam.log
rm -rf /tmp/gcam.log
rm -rf /tmp/oscam.log
[ -d /tmp/test ] || mkdir -p /tmp/test
sleep 2
echo ""
echo "actual servers ....."
sleep 2
echo ""
more /etc/CCcam.cfg
sleep 2
echo ""


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
  cat CCcam4  > /tmp/test/ncam.log
  echo ""
  cd /
  
  
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
  cat CCcam4 > /tmp/test/ncam.log 
  echo ""
  cd /
  
  
elif  curl -k -A -k -s  http://127.0.0.1:16001/servers >>/dev/null ; then
  [ -d /tmp/test ] || mkdir -p /tmp/test
  cd /tmp/test
  sleep 0
  curl -k -A -k -s  http://127.0.0.1:16001/servers > /tmp/test/CCcam
  cat CCcam > /tmp/test/ncam.log
  echo ""
  cd /

  
  
  else
  echo 'FILTR ...nepodporuje CAM'
  echo ''
  sleep 2
  echo 'FILTR ...does not support CAM'
  echo ''
  sleep 2
  echo 'EXIT'
  exit

fi





if  grep  -i -o 'CONNECTED [^(<"]*' /tmp/test/ncam.log > /tmp/test/ncam1.log >>/dev/null 2>&1 </dev/null  ; then 
 grep  -i -o 'CONNECTED [^(<"]*' /tmp/test/ncam.log > /tmp/test/ncam1.log 
 cut -f2 -d" " /tmp/test/ncam1.log > /tmp/test/ncam2.log
 echo ''
 echo 'log ...OK'
 echo ''
  
  
  else
  echo 'FILTR ...nepodporuje CAM'
  echo ''
  sleep 2
  echo 'FILTR ...does not support CAM'
  echo ''
  sleep 2
  echo 'EXIT'
  exit
fi


echo ''
sleep 2
cp /etc/CCcam.cfg /tmp/CCcam.cfg 
echo -n "Filtering ....."
FS=" "
cat /tmp/test/ncam2.log |grep -i "^.*"|while read line ; do
# F1=$(echo $line|cut -d"$FS" -f1)

XXX=$(echo $line)

# echo "SERVER: $SERVER PORT: $PORT USER: $USER PASS: $PASS"
echo -n "."

sed  -i "/$line/p" /tmp/CCcam.cfg  
done
sleep 2
echo ""
echo "filtered servers ....."

uniq -d /tmp/CCcam.cfg > /tmp/CCcam1.cfg


rm -rf /tmp/test
rm -rf /etc/CCcam.cfg
sleep 1
cp /tmp/CCcam1.cfg /etc/CCcam.cfg
rm -rf /tmp/CCcam.cfg
rm -rf /tmp/CCcam1.cfg
sleep 2
echo ""
more /etc/CCcam.cfg
sleep 3
echo ""
####################################################################################################
/usr/script/conv.sh
####################################################################################################
/usr/script/najdiCFG.sh >>/dev/null 2>&1 </dev/null &
####################################################################################################
/usr/script/restart.sh 
####################################################################################################
sleep 3
####################################################################################################
/tmp/upozor1.sh >>/dev/null 2>&1 </dev/null &
####################################################################################################
sleep 3
rm -rf /tmp/upozor1.sh >>/dev/null 2>&1 </dev/null &

exit
