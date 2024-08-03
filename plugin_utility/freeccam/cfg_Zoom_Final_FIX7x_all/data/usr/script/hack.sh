#!/bin/bash
#@mino60 By RAED 2018
if opkg list_installed|grep python-requests ; then

echo ""

echo ""

echo "download from ...dhoom.org"

echo ""

else

echo 'python-requests...was not found'

echo ""

opkg update

opkg install python-requests

echo "install python-requests ...?"

fi

echo > /tmp/xtest/souborX

LINE="************************************************************"
python <<'EOF' 

import requests,re,time
S=requests.Session()
def get_bigtezz_com(url):
    r=S.get(url)
    rgx = '''<input type="hidden" name="_token" value="(.+?)">'''
    rgx1 = '''<input type="hidden" name="trial-ok">.+?<input type="hidden" name="trial" value="(.+?)">'''
    rgx2 = '''<input type="hidden" name="ok" value="(.+?)"></form>'''
    _token = re.findall(rgx,r.content)
    _Dream = re.findall(rgx1,r.content,re.S)
    _CS = re.findall(rgx2,r.content)
    print _token
    print _Dream
    print _CS
    prm = {"trial":["trial-ok",_Dream[0]],"CS":["trial-ok",_CS[0]],"ok":["trial-ok",_CS[0]],"x":"105","y":"24","_token":_token[0],"trial-ok":"24"}
    hdr = {'Host': 'dhoom.org',
           'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:72.0) Gecko/20100101 Firefox/72.0',
           'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
           'Accept-Language': 'fr,fr-FR;q=0.8,en-US;q=0.5,en;q=0.3',
           'Accept-Encoding': 'gzip, deflate',
           'Content-Type': 'application/x-www-form-urlencoded',
           'Content-Length': '139',
           'Origin': 'http://dhoom.org',
           'Connection': 'keep-alive',
           'Referer': url,
           'Upgrade-Insecure-Requests': '1'}
    print prm
    time.sleep(5)
    data = S.post(url,headers=hdr,data=prm).content
    tmx = '''color="White"> (.+?)</font>'''
    cline = re.findall(tmx, data)[0]
    print "cline",cline
    with open('/tmp/xtest/souborX', "a") as f: f.write("\n"+cline)
    return cline
    
S1= "http://dhoom.org/test/"
print get_bigtezz_com(S1)
#****************************************************************************** 


r.close()


EOF

sleep 1

sed -i "/^$/d " /tmp/xtest/souborX
echo ""  >> /tmp/xtest/souborX



exit 0        

