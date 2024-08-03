#!/bin/sh
echo "INFO"
[ -d /tmp/test ] || mkdir -p /tmp/test
cd /tmp/test
curl -k -A -k -s  'https://www.cas-presny.cz/' > /tmp/test/CCcam
grep  'atime[^<]*' CCcam  > CCcam1
sed -i 's/\([ ]\+\)/\n\1/g' CCcam1 
sed -i 's#class="col-sm-2##g' CCcam1
sed -i 's#class="hodnota">##g' CCcam1
sed -i 's#</span></div><div##g' CCcam1
sed -i 's#udaj">##g' CCcam1
sed -i "s#</b>##g" CCcam1
sed -i "s#<div>##g" CCcam1
sed -i "s#</div>##g" CCcam1
sed -i "s#</span>##g" CCcam1
sed -i "s#<span>##g" CCcam1
sed -i "s#<span##g" CCcam1
sed -i 's#"><div##g' CCcam1
sed -i 's#id="##g' CCcam1
sed -i 's#class="row##g' CCcam1
sed -i 's#casy"><div##g' CCcam1
sed -i 's#<div##g' CCcam1
sed -i 's#class="column##g' CCcam1
sed -i 's#class="text-center##g' CCcam1
sed -i 's#">#  #g' CCcam1
sed -i 's#class="loc##g' CCcam1
sed -i 's#cas"##g' CCcam1
sed -i 's#tdiff"##g' CCcam1
sed -i 's#<hr>##g' CCcam1
sed  '/#atime/d' CCcam1 > čas
curl -k -A -k -s  'https://www.okhelp.cz/presny-cas/index.php' > /tmp/test/CCcam
cd /tmp/test

grep  'Datum[^<]*' CCcam  > CCcam1
sed -i 's/\([</b>]\+\)/\n\1/g' CCcam1 
sed -i "s#</b>##g" CCcam1 
sed -i "s#<br##g" CCcam1 
sed -i "s#/>##g" CCcam1 
sed -i "s#<b>##g" CCcam1
sed -i "s#>##g" CCcam1  
sed -i "s#<##g" CCcam1 
sed -i '/&/d' CCcam1
sed -i '/href=/d' CCcam1 
sed '/^$/d' CCcam1 > datum

sed -n '1339,1372p' CCcam > CCcamx1

sed -i "s#</b>##g" CCcamx1
sed -i "s#<div>##g" CCcamx1
sed -i "s#</div>##g" CCcamx1
sed -i "s#<b>##g" CCcamx1
sed -i "s#<hr##g" CCcamx1
sed -i "s#<br##g" CCcamx1
sed -i "s#h3>##g" CCcamx1

sed -i "s#<##g" CCcamx1 
sed -i "s#>##g" CCcamx1
sed -i "s#/##g" CCcamx1
sed -i "s#strong##g" CCcamx1
sed  "s#strong##g" CCcamx1 > pran
more datum 
sleep 5
echo ""
echo ""

more pran 
echo ""
echo ""
sleep 5
more čas



rm -rf /tmp/test

####################################################################################################

exit

