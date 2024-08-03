#!/bin/sh

if find /etc/init.d/openvpn > /dev/null 2>&1 ; then 
sleep 2
echo "Aktuální IP: `wget -qO- http://ipecho.net/plain;echo`"
sleep 2
echo ""
echo "zastavuji VPN"
echo ""
echo "VPN ...STOP"
/etc/init.d/openvpn stop > /dev/null 2>&1
/etc/init.d/openvpn stop
echo ""
sleep 2
echo "Aktuální IP: `wget -qO- http://ipecho.net/plain;echo`"
echo ""
else
echo 'OpenVPN ...NONE'
exit
fi

exit 0
