#!/bin/sh
echo "ECM info"
echo ".....?"
echo ""
echo ""
echo ""
sleep 0
if [ -e /tmp/ecm.info ] ; then
cat /tmp/ecm.info
sleep 0
echo ""
else
echo ""
echo 'ECM ...info'
sleep 2
echo ""
echo 'not found'
echo ""
fi

exit
