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
rm -rf /etc/CCcam.cfg
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
    with open('/etc/CCcam.cfg', "a") as f: f.write("\n"+cline)
    return cline
    
S1= "http://dhoom.org/test/"
print get_bigtezz_com(S1)
#****************************************************************************** 

ncamfile="/etc/tuxbox/config/ncam.server"
oscamfile="/etc/tuxbox/config/oscam.server"
ccamfile="/etc/CCcam.cfg"
## We read the CCcam.cfg and convert it to oscam.server
r=open(oscamfile,'a')
r=open(ncamfile,'a')
r.close()


for line in open(ccamfile,'r').readlines():
    lines = re.match(r'(.*)C: (.*?) (.*?) (.*?) (.*)',line)
    if lines:
        w=open(oscamfile,'a')
        w.write("\n")
        w.write("[reader]"+"\n")
        w.write("enable = 1"+"\n")
        w.write("label = "+ lines.group(2)+"\n")
        w.write("protocol = cccam"+"\n")         
        w.write("device = "+lines.group(2)+","+lines.group(3)+"\n")
        w.write("user = "+lines.group(4)+"\n")
        w.write("password = "+lines.group(5)+"\n")
        w.write("inactivitytimeout = 5"+"\n")
        w.write("reconnecttimeout = 5"+"\n")
        w.write("group = 1"+"\n")
        w.write("emmcache = 1,3,2,0"+"\n")
        w.write("blockemm-unknown = 1"+"\n")
        w.write("blockemm-u = 1"+"\n")
        w.write("blockemm-s = 1"+"\n")
        w.write("blockemm-g = 1"+"\n")
        w.write("cccversion = 2.0.11"+"\n")
        w.write("ccckeepalive = 1"+"\n")
        w.close()
        
for line in open(ccamfile,'r').readlines():
    lines = re.match(r'(.*)C: (.*?) (.*?) (.*?) (.*)',line)
    if lines:
        w=open(ncamfile,'a')
        w.write("\n")
        w.write("[reader]"+"\n")
        w.write("enable = 1"+"\n")
        w.write("label = "+ lines.group(2)+"\n")
        w.write("protocol = cccam"+"\n")         
        w.write("device = "+lines.group(2)+","+lines.group(3)+"\n")
        w.write("user = "+lines.group(4)+"\n")
        w.write("password = "+lines.group(5)+"\n")
        w.write("inactivitytimeout = 5"+"\n")
        w.write("reconnecttimeout = 5"+"\n")
        w.write("group = 1"+"\n")
        w.write("emmcache = 1,3,2,0"+"\n")
        w.write("blockemm-unknown = 1"+"\n")
        w.write("blockemm-u = 1"+"\n")
        w.write("blockemm-s = 1"+"\n")
        w.write("blockemm-g = 1"+"\n")
        w.write("cccversion = 2.0.11"+"\n")
        w.write("ccckeepalive = 1"+"\n")
        w.close()  
        
EOF
sleep 1
####################################################################################################
/usr/script/conv.sh
####################################################################################################
/usr/script/najdiCFG.sh >>/dev/null 2>&1 </dev/null &
####################################################################################################
/usr/script/restart.sh
####################################################################################################


exit 0        

