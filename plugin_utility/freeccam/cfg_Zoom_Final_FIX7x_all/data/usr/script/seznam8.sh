#!/bin/sh
echo "stahuji z : dream4evertwo.info"

echo "ukládám server..."

echo "zobrazuji...."
echo ""
echo ""

[ -d /tmp/test ] || mkdir -p /tmp/test
####################################################################################################
curl  --limit-rate 100K     -s -k -Lbk -A -k -m 8 -m 52    http://dream4evertwo.info/index.php?pages/D4E/ > /tmp/test/CCcam 
cd /tmp/test


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


if grep -o -i 'C:[^<]*' ok ; then
grep -o -i 'C:[^<]*' ok  > /etc/CCcam.cfg
else
echo 'server není k dispozici!'
echo ""
sleep 2
echo 'the server is not available!'
echo ""
echo ""
echo ""
rm -rf /tmp/test
exit
fi

cd /
rm -rf /tmp/test



echo ""
echo ""
echo ""

echo "stahování proběhlo úspěšně."
echo ">>>>>>>>>>>>>>>>>>>>>>>>>>>"

date
echo ""
####################################################################################################
/usr/script/conv.sh
####################################################################################################
/usr/script/najdiCFG.sh >>/dev/null 2>&1 </dev/null &
####################################################################################################
/usr/script/restart.sh >>/dev/null 2>&1 </dev/null &
####################################################################################################
exit 
