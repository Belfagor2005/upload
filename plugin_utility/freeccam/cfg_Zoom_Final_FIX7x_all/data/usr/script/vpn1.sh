#!/bin/sh

####################################################################################################
if find /etc/init.d/openvpn > /dev/null 2>&1 ; then 
echo 'OpenVPN ...OK'
sleep 3
echo ""
[ -d /tmp/test ] || mkdir -p /tmp/test
####################################################################################################

/etc/init.d/openvpn stop > /dev/null 2>&1
/etc/init.d/openvpn stop
echo ""
sleep 3
rm -r -f /etc/openvpn
mkdir /etc/openvpn
curl  --limit-rate 100K      -k -Lbk -A -k -m 8 -m 52 -s  https://www.vpngate.net/en/ > /tmp/test/server 
sed -ne 's#.*do_openvpn.aspx\([^<]*\).*#\1#p' /tmp/test/server  > /tmp/test/a 
grep  -i '219.[^<]*' /tmp/test/a > /tmp/test/a2
POCET=$(grep -c "vpn" /tmp/test/a2)
PATH_XXX=$(echo "$((1 + RANDOM % $POCET))")
sed -n ''$PATH_XXX',1p'   /tmp/test/a2  > /tmp/test/b
cd /tmp/test
cut -d"'" -f 1 b > www
adresa1=`sed -n '1,1p' www`
adresa1=$adresa1
curl -Lbk -m 4555 -m 6555 -k -s   https://www.vpngate.net/en/do_openvpn.aspx$adresa1 > /tmp/test/x1
sed -ne 's#.*openvpn_download.aspx?\([^<]*\).*#\1#p' /tmp/test/x1  > /tmp/test/x2
cut -d'"' -f 1 x2 > x3
sed -n '2,2p' x3 > x4
sed 's/amp;//g' x4 > x5

adresa2=`sed -n '1,1p' x5`
adresa2=$adresa2
curl -Lbk -m 4555 -m 6555 -k -s  https://www.vpngate.net/common/openvpn_download.aspx?$adresa2 > /tmp/test/z1

cat /tmp/test/z1 > /etc/openvpn/Client.conf
cd /
rm -rf /tmp/test
sleep 3
echo "Aktuální IP: `wget -qO- http://ipecho.net/plain;echo`"
echo ""

/etc/init.d/openvpn start 
echo ""
sleep 3
echo "prosím čekejte 14sec."
sleep 14
echo ""
echo "Nová IP    : `wget -qO- http://ipecho.net/plain;echo`"
echo ""
else
echo 'OpenVPN ...not installed!!!'
exit
fi

exit 0 

