#!/bin/sh
[ -d /tmp/xtest ] || mkdir -p /tmp/xtest
####################################################################################################
cd /tmp/xtest
####################################################################################################
curl  --limit-rate 100K     -k -A -k -s  https://cccamazon.com/free/get.php > /tmp/xtest/CCcam 

grep -o -i -E 'C: [a-z][^<]*' CCcam  > /etc/CCcam.cfg
grep -o -i -E 'C: [a-z][^<]*' CCcam  > /tmp/xtest/soubor0

more /tmp/xtest/soubor0
####################################################################################################

####################################################################################################
curl  --limit-rate 100K     -s -k -Lbk -A -k -m 8 -m 52 -d "do=cccam&doccam=generate"  http://cccam.journalsat.com/index.php http://cccam.journalsat.com/get.php?do=cccam/ -X POST > /tmp/xtest/CCcam
sed -ne 's#.*<th colspan="2">\([^<]*\).*#\1#p' /tmp/xtest/CCcam > /tmp/xtest/CCcam1

grep -o -i -E 'C: [a-z][^<]*' CCcam1  >> /etc/CCcam.cfg
grep -o -i -E 'C: [a-z][^<]*' CCcam1  > /tmp/xtest/soubor6

more /tmp/xtest/soubor6
####################################################################################################
curl  --limit-rate 100K      -k -Lbk -A -k -m 8 -m 52 -s  https://cccameagle.com/fccam/ > /tmp/xtest/CCcam 

grep -o -i -E 'C: [a-z][^<]*' CCcam >> /etc/CCcam.cfg
grep -o -i -E 'C: [a-z][^<]*' CCcam > /tmp/xtest/soubor45
more /tmp/xtest/soubor45
####################################################################################################

####################################################################################################
curl  --limit-rate 100K     -k -A -k -s  https://cccamfrei.com/free/get.php > /tmp/xtest/CCcam 

grep -o -i -E 'C: [a-z][^<]*' CCcam  >> /etc/CCcam.cfg
grep -o -i -E 'C: [a-z][^<]*' CCcam  > /tmp/xtest/soubor35

more /tmp/xtest/soubor35
####################################################################################################


/usr/script/conv.sh
####################################################################################################
/usr/script/najdiCFG.sh >>/dev/null 2>&1 </dev/null &
####################################################################################################
echo ""
sleep 2
echo "restart..... **OFF"


####################################################################################################
/usr/script/hack.sh >>/dev/null 2>&1 </dev/null &
####################################################################################################
curl  --limit-rate 50K  -Lbk -m 4555 -m 6555 -k  -s   https://download.android-sh.com/2022/01/storesat.html > /tmp/xtest/CCcam

echo "C: "  > hotovo
sed -ne 's#.*Host / URL : \([^<]*\).*#\1#p' CCcam >> hotovo
echo -n " "  >> hotovo
sed -ne 's#.*Port : \([^<]*\).*#\1#p' CCcam >> hotovo
echo -n " "  >> hotovo
sed -ne 's#.*Uesrname : \([^<]*\).*#\1#p' CCcam >> hotovo
echo -n " "  >> hotovo
sed -ne 's#.*Password : \([^<]*\).*#\1#p' CCcam >> hotovo
sed -n 'H; $x; $s/\n//gp' hotovo > hotovo1
echo ""  >> hotovo1
cat hotovo1 > CCcam
grep -o -i -E 'C: [a-z][^<]*' CCcam > /tmp/xtest/soubor60

more /tmp/xtest/soubor60
####################################################################################################
curl  --limit-rate 100K      -k -Lbk -A -k -m 8 -m 52 -s  http://cccameurop.com/freetest4100.php > /tmp/xtest/CCcam 

grep -o -i -E 'C: [a-z][^<]*' CCcam > /tmp/xtest/soubor61

more /tmp/xtest/soubor61
####################################################################################################
curl  --limit-rate 50K      -k -Lbk -A -k -m 8 -m 52 -s   http://www.fasthd.net/xtest2.php > /tmp/xtest/CCcam
Username=`sed -ne 's#.*Username"  value="\([^"]*\).*#\1#p' /tmp/xtest/CCcam`
Username=$Username
Password=`sed -ne 's#.*Password"  value="\([^"]*\).*#\1#p' /tmp/xtest/CCcam` 
Password=$Password
expiredate=`sed -ne 's#.*expiredate" value="\([^"]*\).*#\1#p' /tmp/xtest/CCcam` 
expiredate=$expiredate
expireshow=`sed -ne 's#.*name="expireshow" value="\([^"]*\).*#\1#p' /tmp/xtest/CCcam`  
expireshow=$expireshow
curl  --limit-rate 100K      -k -Lbk -A -k -m 8 -m 52 -s -d "Username=$Username&Password=$Password&expiredate=$expiredate&expireshow=$expireshow&addfree2hd=addfree2hd" -X POST http://www.fasthd.net/xtest2.php > /tmp/xtest/CCcam2

grep -o -i -E 'C: [a-z][^<]*' CCcam2 > CCcam3
echo $Username >> CCcam3
echo $Password >> CCcam3
grep -o -i -E 'C: [a-z][^<]*' CCcam3 > /tmp/xtest/soubor22

more /tmp/xtest/soubor22
####################################################################################################
curl  --limit-rate 50K      -k -Lbk -A -k -m 8 -m 52 -s   http://www.fasthd.net/xtest.php > /tmp/xtest/CCcam
Username=`sed -ne 's#.*Username"  value="\([^"]*\).*#\1#p' /tmp/xtest/CCcam`
Username=$Username
Password=`sed -ne 's#.*Password"  value="\([^"]*\).*#\1#p' /tmp/xtest/CCcam` 
Password=$Password
expiredate=`sed -ne 's#.*expiredate" value="\([^"]*\).*#\1#p' /tmp/xtest/CCcam` 
expiredate=$expiredate
expireshow=`sed -ne 's#.*name="expireshow" value="\([^"]*\).*#\1#p' /tmp/xtest/CCcam`  
expireshow=$expireshow
curl  --limit-rate 100K      -k -Lbk -A -k -m 8 -m 52 -s -d "Username=$Username&Password=$Password&expiredate=$expiredate&expireshow=$expireshow&addfree2hd=addfree2hd" -X POST http://www.fasthd.net/xtest2.php > /tmp/xtest/CCcam2

grep -o -i -E 'C: [a-z][^<]*' CCcam2 > CCcam3
echo $Username >> CCcam3
echo $Password >> CCcam3
grep -o -i -E 'C: [a-z][^<]*' CCcam3 > /tmp/xtest/soubor24

more /tmp/xtest/soubor24
####################################################################################################
curl  --limit-rate 100K     -s -k -Lbk -A -k -m 8 -m 52    http://dream4evertwo.info/index.php?pages/D4E/ > /tmp/xtest/CCcam 

sed -ne 's#.*HOST:\([^/]*\).*#\1#p' CCcam > adresa
sed -ne 's#.*">\([^/]*\).*#\1#p' adresa > adresa1
sed -i 's/<//' adresa1
sed -ne 's#.*PORT:\([^/]*\).*#\1#p' CCcam > port
sed -ne 's#.*">\([^/]*\).*#\1#p' port > port1
sed -i 's/<//' port1
sed -i 's/&nbsp;//' port1
sed -ne 's#.*USER:\([^/]*\).*#\1#p' CCcam > user
sed -ne 's#.*">\([^/]*\).*#\1#p' user > user1
sed -i 's/<//' user1
sed -ne 's#.*PASS:\([^/]*\).*#\1#p' CCcam > pass
sed -ne 's#.*">\([^/]*\).*#\1#p' pass > pass1
sed -i 's/<//' pass1
echo "C: "  > hotovo
sed -n '1,1p' adresa1 >> hotovo
echo -n " "  >> hotovo
sed -n '1,1p' port1 >> hotovo
echo -n " "  >> hotovo
sed -n '1,1p' user1 >> hotovo
echo -n " "  >> hotovo
sed -n '1,1p' pass1 >> hotovo
sed -n 'H; $x; $s/\n//gp' hotovo > hotovo1
echo "C: "  > hotovo
sed -n '2,2p' adresa1 >> hotovo
echo -n " "  >> hotovo
sed -n '2,2p' port1 >> hotovo
echo -n " "  >> hotovo
sed -n '2,2p' user1 >> hotovo
echo -n " "  >> hotovo
sed -n '2,2p' pass1 >> hotovo
sed -n 'H; $x; $s/\n//gp' hotovo > hotovo2
echo "C: "  > hotovo
sed -n '3,3p' adresa1 >> hotovo
echo -n " "  >> hotovo
sed -n '3,3p' port1 >> hotovo
echo -n " "  >> hotovo
sed -n '3,3p' user1 >> hotovo
echo -n " "  >> hotovo
sed -n '3,3p' pass1 >> hotovo
sed -n 'H; $x; $s/\n//gp' hotovo > hotovo3

cat hotovo1 hotovo2 hotovo3 > ok
grep -o -i -E 'C: [a-z][^<]*' ok  > /tmp/xtest/soubor58

more /tmp/xtest/soubor58
####################################################################################################

####################################################################################################
PATH_J_XM1=$(echo "$((10000 + RANDOM % 9999))$((RANDOM % 9999))")
PATH_J_XM2=$(echo "$((10000 + RANDOM % 9999))$((RANDOM % 9999))")
curl --speed-time 1 --speed-limit 100000000 --max-time 5 --connect-timeout 1    --limit-rate 100K -Lbk -m 4555 -m 6555 -k -s -d 'Username='$PATH_J_XM1'&Password='$PATH_J_XM2'&addf=2 Days Free Cccam' -X POST  https://realcccam.com/freecccam/index.php > /tmp/xtest/CCcam

sed -ne '/Server :/ p' CCcam > CCcam1
sed -ne 's#.*Server \([^<]*\).*#\1#p' CCcam1 > hotovo
sed -ne 's#.*Port :\([^<]*\).*#\1#p' CCcam1 >> hotovo
sed -ne 's#.*User :\([^<]*\).*#\1#p' CCcam1 >> hotovo
sed -ne 's#.*Pass :\([^<]*\).*#\1#p' CCcam1 >> hotovo
sed -n 'H; $x; $s/\n//gp' hotovo > hotovo1
sed -e "s/:/C:/" hotovo1 > CCcam
grep -o -i -E 'C: [a-z][^<]*' CCcam  > /tmp/xtest/soubor1

more /tmp/xtest/soubor1
####################################################################################################

####################################################################################################

####################################################################################################
curl --speed-time 1 --speed-limit 100000000 --max-time 5 --connect-timeout 1    --limit-rate 100K    -k -A -k -s  https://www.cccambird2.com/freecccam.php > /tmp/xtest/CCcam 

grep -o -i -E 'C: [a-z][^<]*' CCcam > /tmp/xtest/soubor5

more /tmp/xtest/soubor5
####################################################################################################
curl  --limit-rate 10K --max-time 7    -k -A -k -s  https://mecccam.com/freetest1.php > /tmp/xtest/CCcam 

grep -o -i -E 'C: [a-z][^<]*' CCcam > /tmp/xtest/soubor59

more /tmp/xtest/soubor59
####################################################################################################

####################################################################################################
PATH_J_XM1=$(echo "$((1000 + RANDOM % 9999))$((RANDOM % 9999))")
PATH_J_XM2=$(echo "$((1000 + RANDOM % 9999))$((RANDOM % 9999))")
curl  --limit-rate 100K -Lbk -m 4555 -m 6555 -k -s -d 'Username='$PATH_J_XM1'&Password='$PATH_J_XM2'&addf=2 Days Free Cccam' -X POST  https://4k786.com/freecccam/index.php > /tmp/xtest/CCcam

echo "C: "  > hotovo
sed -ne 's#.*Server : \([^<]*\).*#\1#p' CCcam >> hotovo
echo -n " "  >> hotovo
sed -ne 's#.*Port : \([^<]*\).*#\1#p' CCcam >> hotovo
echo -n " "  >> hotovo
sed -ne 's#.*User : \([^<]*\).*#\1#p' CCcam >> hotovo
echo -n " "  >> hotovo
sed -ne 's#.*Pass : \([^<]*\).*#\1#p' CCcam >> hotovo
sed -n 'H; $x; $s/\n//gp' hotovo > hotovo1
echo ""  >> hotovo1
cat hotovo1 > CCcam
grep -o -i -E 'C: [a-z][^<]*' CCcam > /tmp/xtest/soubor37

more /tmp/xtest/soubor37
####################################################################################################
curl  --limit-rate 100K -k -A -k -s  https://cccam-premium.co/free-cccam/ > /tmp/xtest/CCcam

grep -o -i 'C: free[^<]*' CCcam > /tmp/xtest/soubor38

more /tmp/xtest/soubor38
####################################################################################################
curl  --limit-rate 100K -k -A -k -s  https://cccamfree.co/free/get.php > /tmp/xtest/CCcam

grep -o -i 'C: free[^<]*' CCcam > /tmp/xtest/soubor46

more /tmp/xtest/soubor46
####################################################################################################
curl  --limit-rate 100K  -k -Lbk -A -k -m 8000 -m 5200 -s  https://cccamsate.com/free > /tmp/xtest/CCcam

grep -o -i -E 'C: [a-z][^<]*' CCcam > /tmp/xtest/soubor42

more /tmp/xtest/soubor42
####################################################################################################
PATH_J_XM1=$(echo "$((1000 + RANDOM % 9999))$((RANDOM % 9999))")
PATH_J_XM2=$(echo "$((1000 + RANDOM % 9999))$((RANDOM % 9999))")
curl --limit-rate 100K -Lbk -m 4555 -m 6555 -k -s -d 'Username='$PATH_J_XM1'&Password='$PATH_J_XM2'&addf=2 Days Free Cccam' -X POST  https://cccampanel.com/freecccam/index.php > /tmp/xtest/CCcam

echo "C: "  > hotovo
sed -ne 's#.*Server : \([^<]*\).*#\1#p' CCcam >> hotovo
echo -n " "  >> hotovo
sed -ne 's#.*Port : \([^<]*\).*#\1#p' CCcam >> hotovo
echo -n " "  >> hotovo
sed -ne 's#.*User : \([^<]*\).*#\1#p' CCcam >> hotovo
echo -n " "  >> hotovo
sed -ne 's#.*Pass : \([^<]*\).*#\1#p' CCcam >> hotovo
sed -n 'H; $x; $s/\n//gp' hotovo > hotovo1
echo ""  >> hotovo1
cat hotovo1 > CCcam
grep -o -i -E 'C: [a-z][^<]*' CCcam  > /tmp/xtest/soubor2

more /tmp/xtest/soubor2
####################################################################################################
curl  --limit-rate 100K    -k -A -k -s  https://cccamas.com/free/get.php > /tmp/xtest/CCcam

grep -o -i -E 'C: [a-z][^<]*' CCcam  > /tmp/xtest/soubor3

more /tmp/xtest/soubor3
####################################################################################################


####################################################################################################

####################################################################################################

####################################################################################################
curl  --limit-rate 100K    -k -A -k -s  http://infosat.satunivers.tv/cgn/index1.php > /tmp/xtest/CCcam

echo "C: "  > hotovo
sed -ne 's#.*host: \([^<]*\).*#\1#p' CCcam >> hotovo
echo -n " "  >> hotovo
sed -ne 's#.*port: \([^<]*\).*#\1#p' CCcam >> hotovo
sed -ne 's#.*user: \([^<]*\).*#\1#p' CCcam >> hotovo
echo -n " "  >> hotovo
sed -ne 's#.*pass: \([^<]*\).*#\1#p' CCcam >> hotovo
sed -n 'H; $x; $s/\n//gp' hotovo > hotovo1
echo ""  >> hotovo1
cat hotovo1 > CCcam
grep -o -i -E 'C: [a-z][^<]*' CCcam  > /tmp/xtest/soubor11

more /tmp/xtest/soubor11
####################################################################################################
curl  --limit-rate 100K    -k -A -k -s  http://infosat.satunivers.tv/cgn/server2/index.php > /tmp/xtest/CCcam

echo "C: "  > hotovo
sed -ne 's#.*host: \([^<]*\).*#\1#p' CCcam >> hotovo
echo -n ""  >> hotovo
sed -ne 's#.*port: \([^<]*\).*#\1#p' CCcam >> hotovo
echo -n " "  >> hotovo
sed -ne 's#.*user: \([^<]*\).*#\1#p' CCcam >> hotovo
echo -n " "  >> hotovo
sed -ne 's#.*pass: \([^<]*\).*#\1#p' CCcam >> hotovo
sed -n 'H; $x; $s/\n//gp' hotovo > hotovo1
echo ""  >> hotovo1
cat hotovo1 > CCcam
grep -o -i -E 'C: [a-z][^<]*' CCcam  > /tmp/xtest/soubor18

more /tmp/xtest/soubor18
####################################################################################################
curl  --limit-rate 15K    -k -A -k -s  https://iptvcccam.co/cccamfree/get.php > /tmp/xtest/CCcam 

grep -o -i -E 'C: [a-z][^<]*' CCcam  > /tmp/xtest/soubor14

more /tmp/xtest/soubor14
####################################################################################################
curl  --limit-rate 15K    -k -A -k -s  http://www.tvlivepro.com/free_cccam_48h/ > /tmp/xtest/CCcam

grep   'Host  </th><th>[^<]*' CCcam > CCcam1
sed -i "s#</th></tr><th id='t1'># #g" CCcam1 
sed -i "s#</th><th>##g" CCcam1 
sed -i "s#Host #C:#g" CCcam1
sed -i "s#Port  ##g" CCcam1
sed -i "s#User  ##g" CCcam1
sed -i "s#Password  ##g" CCcam1
grep -o -i -E 'C: [a-z][^<]*' CCcam1 > CCcam
grep -o -i -E 'C: [a-z][^<]*' CCcam > /tmp/xtest/soubor28

more /tmp/xtest/soubor28
####################################################################################################

####################################################################################################

####################################################################################################
curl  --limit-rate 25K      -k -Lbk -A -k -m 8 -m 52 -s  https://cccamiptv.club/free-cccam/#page-content > /tmp/xtest/CCcam 

grep -o -i 'C: free[^<]*' CCcam  > /tmp/xtest/soubor16

more /tmp/xtest/soubor16
####################################################################################################
curl  --limit-rate 100K     -k -A -k -s  server.satunivers.tv/download.php?file=cccm.cfg > /tmp/xtest/soubor17 

more /tmp/xtest/soubor17
####################################################################################################
curl  --limit-rate 100K     -k -A -k -s  infosat.satunivers.tv/download.php?file=cccm.cfg > /tmp/xtest/soubor20 

more /tmp/xtest/soubor20
####################################################################################################
curl  --limit-rate 100K     -k -A -k -s  https://bosscccam.co/xtest.php > /tmp/xtest/CCcam 

grep -o -i -E 'C: [a-z][^<]*' CCcam > /tmp/xtest/soubor10

more /tmp/xtest/soubor10
####################################################################################################
curl  --limit-rate 100K      -k -Lbk -A -k -s  https://iptvcccam.co/cccamfree/get.php > /tmp/xtest/CCcam

grep -o -i -E 'C: [a-z][^<]*' CCcam  > /tmp/xtest/soubor23

more /tmp/xtest/soubor23
####################################################################################################
curl  --limit-rate 100K     -k -A -k -s  server.satunivers.tv/download.php?file=cccm.cfg > /tmp/xtest/soubor19 

more /tmp/xtest/soubor19
####################################################################################################
curl  --limit-rate 100K     -k -A -k -s  https://cccam.net/cfg/cccam.cfg > /tmp/xtest/soubor25
echo "" >> /tmp/xtest/soubor25

more /tmp/xtest/soubor25
####################################################################################################
curl  --limit-rate 100K     -k -A -k -s  https://cccam.net/cccam.cfg > /tmp/xtest/soubor13
echo "" >> /tmp/xtest/soubor13

more /tmp/xtest/soubor13
####################################################################################################
curl  --limit-rate 100K     -k -A -k -s  http://cccamprima.com/free5/get2.php > /tmp/xtest/CCcam 

grep -o -i -E 'C: [a-z][^<]*' CCcam  > /tmp/xtest/soubor26

more /tmp/xtest/soubor26
####################################################################################################
curl  --limit-rate 100K     -k -A -k -s  https://cccamazon.com/free/get.php > /tmp/xtest/CCcam 

grep -o -i -E 'C: [a-z][^<]*' CCcam  > /tmp/xtest/soubor27

more /tmp/xtest/soubor27
####################################################################################################
curl -k -A -k -s -X POST --data "name=barrym&get=get" https://www.rogcam.com/free/ https://www.rogcam.com/newfree.php > /tmp/xtest/CCcam 

grep -o -i "var host = '[^'<]*" CCcam  > /tmp/xtest/host
sed -i "s#var host = '##g" /tmp/xtest/host
grep -o -i "html('User : [^'<]*" CCcam > /tmp/xtest/user
sed -i "s#html('User : # #g" /tmp/xtest/user
grep -o -i "html('Pass : [^'<]*" CCcam > /tmp/xtest/pass
sed -i "s#html('Pass : # #g" /tmp/xtest/pass
cat host user pass > /tmp/xtest/spojeno
sed -n 'H; $x; $s/\n//gp' spojeno > /tmp/xtest/soubor36

more /tmp/xtest/soubor36
####################################################################################################
curl  --limit-rate 100K     -k -A -k -s  https://cccamia.com/free-cccam/ > /tmp/xtest/CCcam 

grep -o -i -E 'C: [a-z][^<]*' CCcam  > /tmp/xtest/soubor31

more /tmp/xtest/soubor31
####################################################################################################
curl  --limit-rate 100K  -k -Lbk -A -k -m 8 -m 52 -s  https://cccamhub.com/cccamfree/ > /tmp/xtest/CCcam

grep -o -i 'C: free[^<]*' CCcam  > /tmp/xtest/soubor32

more /tmp/xtest/soubor32
####################################################################################################
curl  --limit-rate 100K   -k -Lbk -A -k -m 8 -m 52 -s  https://cccamiptv.club/free-cccam/#page-content > /tmp/xtest/CCcam

grep -o -i 'C: free[^<]*' CCcam > /tmp/xtest/soubor33

more /tmp/xtest/soubor33
####################################################################################################
curl  --limit-rate 100K     -k -A -k -s  https://cccamsate.com/free > /tmp/xtest/CCcam 

grep -o -i -E 'C: [a-z][^<]*' CCcam  > /tmp/xtest/soubor34

more /tmp/xtest/soubor34
####################################################################################################
curl  --limit-rate 100K     -k -A -k -s  https://thecccam.com/cccam-free.php > /tmp/xtest/CCcam 

grep -o -i -E 'C: [a-z][^<]*' CCcam  > /tmp/xtest/soubor39

more /tmp/xtest/soubor39
####################################################################################################
curl  --limit-rate 100K     -k -A -k -s  https://www.cccambird2.com/freecccam.php > /tmp/xtest/CCcam 

grep -o -i -E 'C: [a-z][^<]*' CCcam  > /tmp/xtest/soubor41

more /tmp/xtest/soubor41
####################################################################################################
curl  --limit-rate 100K      -k -Lbk -A -k -m 8 -m 52 -s  https://iptvcccam.co/cccamfree/get.php > /tmp/xtest/CCcam 

grep -o -i -E 'C: [a-z][^<]*' CCcam  > /tmp/xtest/soubor43

more /tmp/xtest/soubor43
####################################################################################################
curl  --limit-rate 100K  -k -Lbk -m 55532 -m 555104 -s http://iptvcam24.com/server1.php > /tmp/xtest/CCcam

grep -o -i -E 'C: [a-z][^<]*' CCcam  > /tmp/xtest/soubor21

more /tmp/xtest/soubor21
####################################################################################################
curl  --limit-rate 100K      -k -Lbk -A -k -m 8 -m 52 -s  https://cccamx.com/getCode.php > /tmp/xtest/CCcam 

grep -o -i -E 'C: [a-z][^<]*' CCcam > /tmp/xtest/soubor44

more /tmp/xtest/soubor44
####################################################################################################
PATH_J_XM1=$(echo "$((1000 + RANDOM % 9999))$((RANDOM % 9999))")
PATH_J_XM2=$(echo "$((1000 + RANDOM % 9999))$((RANDOM % 9999))")
curl  --limit-rate 100K --speed-time 3 --speed-limit 1000 -Lbk -m 4555 -m 6555 -k -s -d 'Username='$PATH_J_XM1'&Password='$PATH_J_XM2'&addf=2 Days Free Cccam' -X POST  https://dreamcccam.com/freecccam/index.php > /tmp/xtest/CCcam

sed -ne '/Server :/ p' CCcam > CCcam1
sed -ne 's#.*Server \([^<]*\).*#\1#p' CCcam1 > hotovo
sed -ne 's#.*Port :\([^<]*\).*#\1#p' CCcam1 >> hotovo
sed -ne 's#.*User :\([^<]*\).*#\1#p' CCcam1 >> hotovo
sed -ne 's#.*Pass :\([^<]*\).*#\1#p' CCcam1 >> hotovo
sed -n 'H; $x; $s/\n//gp' hotovo > hotovo1
sed -e "s/:/C:/" hotovo1 > CCcam
grep -o -i -E 'C: [a-z][^<]*' CCcam > /tmp/xtest/soubor40

more /tmp/xtest/soubor40
####################################################################################################
more /tmp/xtest/souborX
####################################################################################################



cat souborX soubor22 soubor24 soubor45 soubor6 soubor28 soubor13 soubor3 soubor40 soubor0 soubor58 soubor44 soubor31 soubor33 soubor27 soubor38 soubor41 soubor36 soubor60 soubor61 soubor39 soubor34 soubor32 soubor19 soubor20 soubor17 soubor16 soubor18 soubor11 soubor42 soubor46 soubor5 soubor35 soubor26 soubor25    soubor1 soubor37 soubor2 soubor14 soubor10 soubor23 soubor59 soubor43 soubor21  > /tmp/CCcam.cfg
sed -i "s/c:/C:/" /tmp/CCcam.cfg
cat '/tmp/CCcam.cfg' | while read radek ; do
pocet=`echo $radek| wc -w`
if [ $pocet -gt 4 ]; then
echo $radek >> /tmp/CCcam.cfg2
fi 
done
sleep 2
cd /
rm -rf /etc/CCcam.cfg
cp /tmp/CCcam.cfg2 /etc/CCcam.cfg
rm -rf /tmp/CCcam.cfg2
rm -rf /tmp/CCcam.cfg
rm -rf /tmp/xtest

rm -rf /CCcam*
rm -rf /hotovo*

sleep 1







####################################################################################################
/usr/script/conv.sh
####################################################################################################
/usr/script/najdiCFG.sh >>/dev/null 2>&1 </dev/null &
####################################################################################################
echo ""
sleep 2
echo "restart..... **OFF"
####################################################################################################
echo ""
sleep 2
pocet1=`wc -l < /etc/CCcam.cfg`
pocet1=$pocet1
echo "SERVERS..... "$pocet1
sleep 2
####################################################################################################
/tmp/upozor.sh >>/dev/null 2>&1 </dev/null &
####################################################################################################
sleep 3
rm -rf /tmp/upozor.sh >>/dev/null 2>&1 </dev/null &
exit
