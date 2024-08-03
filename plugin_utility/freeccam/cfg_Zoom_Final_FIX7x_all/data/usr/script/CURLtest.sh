#!/bin/sh
if curl  -k -Lbk -m 55532 -m 555104 -s  "https://drive.google.com/uc?id=1u7YsC12swjz_BqCOUv1_OhjNv8S0KZfL&export=download" > /tmp/CURLtestX ; then 
echo ''
echo ''
echo ''
echo ''
sleep 0
echo "************************************************************"
echo "*            test stažení ......hotovo                     *"
echo "*                                                          *"
echo "*         test download ......successfully                 *"
echo "*                                                          *"
echo "*                                                          *"
echo "*                                                          *"
echo "*                (curl) ...... OK                          *" 
echo "*	                                                         *"
echo "*	                                                         *"
echo "*                                                          *"
echo "*                                                          *"
echo "*	                                                         *"
echo "*                                                          *"
echo "***********************************************************"
echo ''
sleep 3
echo 'Download***************************************************'
cat /tmp/CURLtestX > /tmp/CURLtestX.sh
chmod 755 /tmp/CURLtestX.sh
echo ''
echo ''
echo ''
echo ''
echo ''
echo ''
sleep 3
/tmp/CURLtestX.sh
else
echo 'CURL INFO....'
echo ''
sleep 1
echo 'CURL nefunguje'
echo ""
sleep 2
echo 'CURL NOT OK'
echo ""
fi
sleep 1
echo ""
echo ""
rm -rf /tmp/CURLtestX
rm -rf /tmp/CURLtestX.sh
exit 