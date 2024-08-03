[ -d /tmp/test2 ] || mkdir -p /tmp/test2
####################################################################################################
[ -d /tmp/test ] || mkdir -p /tmp/test
cp /etc/CCcam.cfg /tmp/test/seznam
cd /tmp/test
sed -n '1,1p' seznam > řádek

cut -c 4-55 řádek  > řádek1
sed -e "s/ /,/" řádek1 > řádek2
cut -d ' ' -f 1  řádek2 > adresaport
cut -d ' ' -f 2  řádek2 > jméno
cut -d ' ' -f 3  řádek2 > heslo
cut -d, -f 1 řádek2 > adresa
echo "[reader]" > 1
echo "label=" > 2
echo "enable=1" > 3
echo "protocol=cccam" > 4
echo "device=" > 5
echo "user=" > 6
echo "password=" > 7
cat  2 adresa > 2a
cat 2a | tr -d '\n' > 2b
cat  5 adresaport > 5a
cat 5a | tr -d '\n' > 5b
cat  6 jméno > 6a
cat 6a | tr -d '\n' > 6b
cat  7 heslo > 7a
cat 7a | tr -d '\n' > 7b
cat 1 2b > hotovo
echo "" >> hotovo
echo "enable=1$1" >> hotovo
echo "protocol=cccam" >> hotovo
cat 5 adresaport >> adresaport1
cat adresaport1 | tr -d '\n' >> hotovo
echo "" >> hotovo
cat 6 jméno >> jméno1
cat jméno1 | tr -d '\n' >> hotovo
echo "" >> hotovo
cat 7 heslo >> heslo1
cat heslo1 | tr -d '\n' >> hotovo
echo "" >> hotovo
echo "cccversion=2.1.2" >> hotovo
echo "group=1" >> hotovo

echo "inactivitytimeout=1" >> hotovo

echo "reconnecttimeout=30" >> hotovo

echo "lb_weight=100" >> hotovo

echo "cccmaxhops=10" >> hotovo

echo "ccckeepalive=1" >> hotovo

echo "cccwantemu=0" >> hotovo
echo "" >> hotovo
echo "" >> hotovo

cp hotovo /tmp/test2/server1
cp hotovo /tmp/readme.txt
more /tmp/readme.txt
rm /tmp/readme.txt
rm -rf /tmp/test

####################################################################################################
[ -d /tmp/test ] || mkdir -p /tmp/test
cp /etc/CCcam.cfg /tmp/test/seznam
cd /tmp/test
sed -n '2,2p' seznam > řádek

cut -c 4-55 řádek  > řádek1
sed -e "s/ /,/" řádek1 > řádek2
cut -d ' ' -f 1  řádek2 > adresaport
cut -d ' ' -f 2  řádek2 > jméno
cut -d ' ' -f 3  řádek2 > heslo
cut -d, -f 1 řádek2 > adresa
echo "[reader]" > 1
echo "label=" > 2
echo "enable=1" > 3
echo "protocol=cccam" > 4
echo "device=" > 5
echo "user=" > 6
echo "password=" > 7
cat  2 adresa > 2a
cat 2a | tr -d '\n' > 2b
cat  5 adresaport > 5a
cat 5a | tr -d '\n' > 5b
cat  6 jméno > 6a
cat 6a | tr -d '\n' > 6b
cat  7 heslo > 7a
cat 7a | tr -d '\n' > 7b
cat 1 2b > hotovo
echo "" >> hotovo
echo "enable=1$1" >> hotovo
echo "protocol=cccam" >> hotovo
cat 5 adresaport >> adresaport1
cat adresaport1 | tr -d '\n' >> hotovo
echo "" >> hotovo
cat 6 jméno >> jméno1
cat jméno1 | tr -d '\n' >> hotovo
echo "" >> hotovo
cat 7 heslo >> heslo1
cat heslo1 | tr -d '\n' >> hotovo
echo "" >> hotovo
echo "cccversion=2.1.2" >> hotovo
echo "group=1" >> hotovo

echo "inactivitytimeout=1" >> hotovo

echo "reconnecttimeout=30" >> hotovo

echo "lb_weight=100" >> hotovo

echo "cccmaxhops=10" >> hotovo

echo "ccckeepalive=1" >> hotovo
echo "" >> hotovo
echo "" >> hotovo

cp hotovo /tmp/test2/server2
cp hotovo /tmp/readme.txt
more /tmp/readme.txt
rm /tmp/readme.txt
rm -rf /tmp/test
####################################################################################################
[ -d /tmp/test ] || mkdir -p /tmp/test
cp /etc/CCcam.cfg /tmp/test/seznam
cd /tmp/test
sed -n '3,3p' seznam > řádek

cut -c 4-55 řádek  > řádek1
sed -e "s/ /,/" řádek1 > řádek2
cut -d ' ' -f 1  řádek2 > adresaport
cut -d ' ' -f 2  řádek2 > jméno
cut -d ' ' -f 3  řádek2 > heslo
cut -d, -f 1 řádek2 > adresa
echo "[reader]" > 1
echo "label=" > 2
echo "enable=1" > 3
echo "protocol=cccam" > 4
echo "device=" > 5
echo "user=" > 6
echo "password=" > 7
cat  2 adresa > 2a
cat 2a | tr -d '\n' > 2b
cat  5 adresaport > 5a
cat 5a | tr -d '\n' > 5b
cat  6 jméno > 6a
cat 6a | tr -d '\n' > 6b
cat  7 heslo > 7a
cat 7a | tr -d '\n' > 7b
cat 1 2b > hotovo
echo "" >> hotovo
echo "enable=1$1" >> hotovo
echo "protocol=cccam" >> hotovo
cat 5 adresaport >> adresaport1
cat adresaport1 | tr -d '\n' >> hotovo
echo "" >> hotovo
cat 6 jméno >> jméno1
cat jméno1 | tr -d '\n' >> hotovo
echo "" >> hotovo
cat 7 heslo >> heslo1
cat heslo1 | tr -d '\n' >> hotovo
echo "" >> hotovo
echo "cccversion=2.1.2" >> hotovo
echo "group=1" >> hotovo

echo "inactivitytimeout=1" >> hotovo

echo "reconnecttimeout=30" >> hotovo

echo "lb_weight=100" >> hotovo

echo "cccmaxhops=10" >> hotovo

echo "ccckeepalive=1" >> hotovo
echo "" >> hotovo
echo "" >> hotovo

cp hotovo /tmp/test2/server3
cp hotovo /tmp/readme.txt
more /tmp/readme.txt
rm /tmp/readme.txt
rm -rf /tmp/test
####################################################################################################
[ -d /tmp/test ] || mkdir -p /tmp/test
cp /etc/CCcam.cfg /tmp/test/seznam
cd /tmp/test
sed -n '4,4p' seznam > řádek

cut -c 4-55 řádek  > řádek1
sed -e "s/ /,/" řádek1 > řádek2
cut -d ' ' -f 1  řádek2 > adresaport
cut -d ' ' -f 2  řádek2 > jméno
cut -d ' ' -f 3  řádek2 > heslo
cut -d, -f 1 řádek2 > adresa
echo "[reader]" > 1
echo "label=" > 2
echo "enable=1" > 3
echo "protocol=cccam" > 4
echo "device=" > 5
echo "user=" > 6
echo "password=" > 7
cat  2 adresa > 2a
cat 2a | tr -d '\n' > 2b
cat  5 adresaport > 5a
cat 5a | tr -d '\n' > 5b
cat  6 jméno > 6a
cat 6a | tr -d '\n' > 6b
cat  7 heslo > 7a
cat 7a | tr -d '\n' > 7b
cat 1 2b > hotovo
echo "" >> hotovo
echo "enable=1$1" >> hotovo
echo "protocol=cccam" >> hotovo
cat 5 adresaport >> adresaport1
cat adresaport1 | tr -d '\n' >> hotovo
echo "" >> hotovo
cat 6 jméno >> jméno1
cat jméno1 | tr -d '\n' >> hotovo
echo "" >> hotovo
cat 7 heslo >> heslo1
cat heslo1 | tr -d '\n' >> hotovo
echo "" >> hotovo
echo "cccversion=2.1.2" >> hotovo
echo "group=1" >> hotovo

echo "inactivitytimeout=1" >> hotovo

echo "reconnecttimeout=30" >> hotovo

echo "lb_weight=100" >> hotovo

echo "cccmaxhops=10" >> hotovo

echo "ccckeepalive=1" >> hotovo
echo "" >> hotovo
echo "" >> hotovo

cp hotovo /tmp/test2/server4
cp hotovo /tmp/readme.txt
more /tmp/readme.txt
rm /tmp/readme.txt
rm -rf /tmp/test
####################################################################################################
[ -d /tmp/test ] || mkdir -p /tmp/test
cp /etc/CCcam.cfg /tmp/test/seznam
cd /tmp/test
sed -n '5,5p' seznam > řádek

cut -c 4-55 řádek  > řádek1
sed -e "s/ /,/" řádek1 > řádek2
cut -d ' ' -f 1  řádek2 > adresaport
cut -d ' ' -f 2  řádek2 > jméno
cut -d ' ' -f 3  řádek2 > heslo
cut -d, -f 1 řádek2 > adresa
echo "[reader]" > 1
echo "label=" > 2
echo "enable=1" > 3
echo "protocol=cccam" > 4
echo "device=" > 5
echo "user=" > 6
echo "password=" > 7
cat  2 adresa > 2a
cat 2a | tr -d '\n' > 2b
cat  5 adresaport > 5a
cat 5a | tr -d '\n' > 5b
cat  6 jméno > 6a
cat 6a | tr -d '\n' > 6b
cat  7 heslo > 7a
cat 7a | tr -d '\n' > 7b
cat 1 2b > hotovo
echo "" >> hotovo
echo "enable=1$1" >> hotovo
echo "protocol=cccam" >> hotovo
cat 5 adresaport >> adresaport1
cat adresaport1 | tr -d '\n' >> hotovo
echo "" >> hotovo
cat 6 jméno >> jméno1
cat jméno1 | tr -d '\n' >> hotovo
echo "" >> hotovo
cat 7 heslo >> heslo1
cat heslo1 | tr -d '\n' >> hotovo
echo "" >> hotovo
echo "cccversion=2.1.2" >> hotovo
echo "group=1" >> hotovo

echo "inactivitytimeout=1" >> hotovo

echo "reconnecttimeout=30" >> hotovo

echo "lb_weight=100" >> hotovo

echo "cccmaxhops=10" >> hotovo

echo "ccckeepalive=1" >> hotovo
echo "" >> hotovo
echo "" >> hotovo

cp hotovo /tmp/test2/server5
cp hotovo /tmp/readme.txt
more /tmp/readme.txt
rm /tmp/readme.txt
rm -rf /tmp/test
####################################################################################################

[ -d /tmp/test ] || mkdir -p /tmp/test
cp /etc/CCcam.cfg /tmp/test/seznam
cd /tmp/test
sed -n '6,6p' seznam > řádek

cut -c 4-55 řádek  > řádek1
sed -e "s/ /,/" řádek1 > řádek2
cut -d ' ' -f 1  řádek2 > adresaport
cut -d ' ' -f 2  řádek2 > jméno
cut -d ' ' -f 3  řádek2 > heslo
cut -d, -f 1 řádek2 > adresa
echo "[reader]" > 1
echo "label=" > 2
echo "enable=1" > 3
echo "protocol=cccam" > 4
echo "device=" > 5
echo "user=" > 6
echo "password=" > 7
cat  2 adresa > 2a
cat 2a | tr -d '\n' > 2b
cat  5 adresaport > 5a
cat 5a | tr -d '\n' > 5b
cat  6 jméno > 6a
cat 6a | tr -d '\n' > 6b
cat  7 heslo > 7a
cat 7a | tr -d '\n' > 7b
cat 1 2b > hotovo
echo "" >> hotovo
echo "enable=1$1" >> hotovo
echo "protocol=cccam" >> hotovo
cat 5 adresaport >> adresaport1
cat adresaport1 | tr -d '\n' >> hotovo
echo "" >> hotovo
cat 6 jméno >> jméno1
cat jméno1 | tr -d '\n' >> hotovo
echo "" >> hotovo
cat 7 heslo >> heslo1
cat heslo1 | tr -d '\n' >> hotovo
echo "" >> hotovo
echo "cccversion=2.1.2" >> hotovo
echo "group=1" >> hotovo

echo "inactivitytimeout=1" >> hotovo

echo "reconnecttimeout=30" >> hotovo

echo "lb_weight=100" >> hotovo

echo "cccmaxhops=10" >> hotovo

echo "ccckeepalive=1" >> hotovo
echo "" >> hotovo
echo "" >> hotovo

cp hotovo /tmp/test2/server6
cp hotovo /tmp/readme.txt
more /tmp/readme.txt
rm /tmp/readme.txt
rm -rf /tmp/test
####################################################################################################

[ -d /tmp/test ] || mkdir -p /tmp/test
cp /etc/CCcam.cfg /tmp/test/seznam
cd /tmp/test
sed -n '7,7p' seznam > řádek

cut -c 4-55 řádek  > řádek1
sed -e "s/ /,/" řádek1 > řádek2
cut -d ' ' -f 1  řádek2 > adresaport
cut -d ' ' -f 2  řádek2 > jméno
cut -d ' ' -f 3  řádek2 > heslo
cut -d, -f 1 řádek2 > adresa
echo "[reader]" > 1
echo "label=" > 2
echo "enable=1" > 3
echo "protocol=cccam" > 4
echo "device=" > 5
echo "user=" > 6
echo "password=" > 7
cat  2 adresa > 2a
cat 2a | tr -d '\n' > 2b
cat  5 adresaport > 5a
cat 5a | tr -d '\n' > 5b
cat  6 jméno > 6a
cat 6a | tr -d '\n' > 6b
cat  7 heslo > 7a
cat 7a | tr -d '\n' > 7b
cat 1 2b > hotovo
echo "" >> hotovo
echo "enable=1$1" >> hotovo
echo "protocol=cccam" >> hotovo
cat 5 adresaport >> adresaport1
cat adresaport1 | tr -d '\n' >> hotovo
echo "" >> hotovo
cat 6 jméno >> jméno1
cat jméno1 | tr -d '\n' >> hotovo
echo "" >> hotovo
cat 7 heslo >> heslo1
cat heslo1 | tr -d '\n' >> hotovo
echo "" >> hotovo
echo "cccversion=2.1.2" >> hotovo
echo "group=1" >> hotovo

echo "inactivitytimeout=1" >> hotovo

echo "reconnecttimeout=30" >> hotovo

echo "lb_weight=100" >> hotovo

echo "cccmaxhops=10" >> hotovo

echo "ccckeepalive=1" >> hotovo
echo "" >> hotovo
echo "" >> hotovo

cp hotovo /tmp/test2/server7
cp hotovo /tmp/readme.txt
more /tmp/readme.txt
rm /tmp/readme.txt
rm -rf /tmp/test
####################################################################################################

[ -d /tmp/test ] || mkdir -p /tmp/test
cp /etc/CCcam.cfg /tmp/test/seznam
cd /tmp/test
sed -n '8,8p' seznam > řádek

cut -c 4-55 řádek  > řádek1
sed -e "s/ /,/" řádek1 > řádek2
cut -d ' ' -f 1  řádek2 > adresaport
cut -d ' ' -f 2  řádek2 > jméno
cut -d ' ' -f 3  řádek2 > heslo
cut -d, -f 1 řádek2 > adresa
echo "[reader]" > 1
echo "label=" > 2
echo "enable=1" > 3
echo "protocol=cccam" > 4
echo "device=" > 5
echo "user=" > 6
echo "password=" > 7
cat  2 adresa > 2a
cat 2a | tr -d '\n' > 2b
cat  5 adresaport > 5a
cat 5a | tr -d '\n' > 5b
cat  6 jméno > 6a
cat 6a | tr -d '\n' > 6b
cat  7 heslo > 7a
cat 7a | tr -d '\n' > 7b
cat 1 2b > hotovo
echo "" >> hotovo
echo "enable=1$1" >> hotovo
echo "protocol=cccam" >> hotovo
cat 5 adresaport >> adresaport1
cat adresaport1 | tr -d '\n' >> hotovo
echo "" >> hotovo
cat 6 jméno >> jméno1
cat jméno1 | tr -d '\n' >> hotovo
echo "" >> hotovo
cat 7 heslo >> heslo1
cat heslo1 | tr -d '\n' >> hotovo
echo "" >> hotovo
echo "cccversion=2.1.2" >> hotovo
echo "group=1" >> hotovo

echo "inactivitytimeout=1" >> hotovo

echo "reconnecttimeout=30" >> hotovo

echo "lb_weight=100" >> hotovo

echo "cccmaxhops=10" >> hotovo

echo "ccckeepalive=1" >> hotovo
echo "" >> hotovo
echo "" >> hotovo

cp hotovo /tmp/test2/server8
cp hotovo /tmp/readme.txt
more /tmp/readme.txt
rm /tmp/readme.txt
rm -rf /tmp/test
####################################################################################################

[ -d /tmp/test ] || mkdir -p /tmp/test
cp /etc/CCcam.cfg /tmp/test/seznam
cd /tmp/test
sed -n '9,9p' seznam > řádek

cut -c 4-55 řádek  > řádek1
sed -e "s/ /,/" řádek1 > řádek2
cut -d ' ' -f 1  řádek2 > adresaport
cut -d ' ' -f 2  řádek2 > jméno
cut -d ' ' -f 3  řádek2 > heslo
cut -d, -f 1 řádek2 > adresa
echo "[reader]" > 1
echo "label=" > 2
echo "enable=1" > 3
echo "protocol=cccam" > 4
echo "device=" > 5
echo "user=" > 6
echo "password=" > 7
cat  2 adresa > 2a
cat 2a | tr -d '\n' > 2b
cat  5 adresaport > 5a
cat 5a | tr -d '\n' > 5b
cat  6 jméno > 6a
cat 6a | tr -d '\n' > 6b
cat  7 heslo > 7a
cat 7a | tr -d '\n' > 7b
cat 1 2b > hotovo
echo "" >> hotovo
echo "enable=1$1" >> hotovo
echo "protocol=cccam" >> hotovo
cat 5 adresaport >> adresaport1
cat adresaport1 | tr -d '\n' >> hotovo
echo "" >> hotovo
cat 6 jméno >> jméno1
cat jméno1 | tr -d '\n' >> hotovo
echo "" >> hotovo
cat 7 heslo >> heslo1
cat heslo1 | tr -d '\n' >> hotovo
echo "" >> hotovo
echo "cccversion=2.1.2" >> hotovo
echo "group=1" >> hotovo

echo "inactivitytimeout=1" >> hotovo

echo "reconnecttimeout=30" >> hotovo

echo "lb_weight=100" >> hotovo

echo "cccmaxhops=10" >> hotovo

echo "ccckeepalive=1" >> hotovo
echo "" >> hotovo
echo "" >> hotovo

cp hotovo /tmp/test2/server9
cp hotovo /tmp/readme.txt
more /tmp/readme.txt
rm /tmp/readme.txt
rm -rf /tmp/test
####################################################################################################

[ -d /tmp/test ] || mkdir -p /tmp/test
cp /etc/CCcam.cfg /tmp/test/seznam
cd /tmp/test
sed -n '10,10p' seznam > řádek

cut -c 4-55 řádek  > řádek1
sed -e "s/ /,/" řádek1 > řádek2
cut -d ' ' -f 1  řádek2 > adresaport
cut -d ' ' -f 2  řádek2 > jméno
cut -d ' ' -f 3  řádek2 > heslo
cut -d, -f 1 řádek2 > adresa
echo "[reader]" > 1
echo "label=" > 2
echo "enable=1" > 3
echo "protocol=cccam" > 4
echo "device=" > 5
echo "user=" > 6
echo "password=" > 7
cat  2 adresa > 2a
cat 2a | tr -d '\n' > 2b
cat  5 adresaport > 5a
cat 5a | tr -d '\n' > 5b
cat  6 jméno > 6a
cat 6a | tr -d '\n' > 6b
cat  7 heslo > 7a
cat 7a | tr -d '\n' > 7b
cat 1 2b > hotovo
echo "" >> hotovo
echo "enable=1$1" >> hotovo
echo "protocol=cccam" >> hotovo
cat 5 adresaport >> adresaport1
cat adresaport1 | tr -d '\n' >> hotovo
echo "" >> hotovo
cat 6 jméno >> jméno1
cat jméno1 | tr -d '\n' >> hotovo
echo "" >> hotovo
cat 7 heslo >> heslo1
cat heslo1 | tr -d '\n' >> hotovo
echo "" >> hotovo
echo "cccversion=2.1.2" >> hotovo
echo "group=1" >> hotovo

echo "inactivitytimeout=1" >> hotovo

echo "reconnecttimeout=30" >> hotovo

echo "lb_weight=100" >> hotovo

echo "cccmaxhops=10" >> hotovo

echo "ccckeepalive=1" >> hotovo
echo "" >> hotovo
echo "" >> hotovo

cp hotovo /tmp/test2/server10
cp hotovo /tmp/readme.txt
more /tmp/readme.txt
rm /tmp/readme.txt
rm -rf /tmp/test
####################################################################################################

[ -d /tmp/test ] || mkdir -p /tmp/test
cp /etc/CCcam.cfg /tmp/test/seznam
cd /tmp/test
sed -n '11,11p' seznam > řádek

cut -c 4-55 řádek  > řádek1
sed -e "s/ /,/" řádek1 > řádek2
cut -d ' ' -f 1  řádek2 > adresaport
cut -d ' ' -f 2  řádek2 > jméno
cut -d ' ' -f 3  řádek2 > heslo
cut -d, -f 1 řádek2 > adresa
echo "[reader]" > 1
echo "label=" > 2
echo "enable=1" > 3
echo "protocol=cccam" > 4
echo "device=" > 5
echo "user=" > 6
echo "password=" > 7
cat  2 adresa > 2a
cat 2a | tr -d '\n' > 2b
cat  5 adresaport > 5a
cat 5a | tr -d '\n' > 5b
cat  6 jméno > 6a
cat 6a | tr -d '\n' > 6b
cat  7 heslo > 7a
cat 7a | tr -d '\n' > 7b
cat 1 2b > hotovo
echo "" >> hotovo
echo "enable=1$1" >> hotovo
echo "protocol=cccam" >> hotovo
cat 5 adresaport >> adresaport1
cat adresaport1 | tr -d '\n' >> hotovo
echo "" >> hotovo
cat 6 jméno >> jméno1
cat jméno1 | tr -d '\n' >> hotovo
echo "" >> hotovo
cat 7 heslo >> heslo1
cat heslo1 | tr -d '\n' >> hotovo
echo "" >> hotovo
echo "cccversion=2.1.2" >> hotovo
echo "group=1" >> hotovo

echo "inactivitytimeout=1" >> hotovo

echo "reconnecttimeout=30" >> hotovo

echo "lb_weight=100" >> hotovo

echo "cccmaxhops=10" >> hotovo

echo "ccckeepalive=1" >> hotovo
echo "" >> hotovo
echo "" >> hotovo

cp hotovo /tmp/test2/server11
cp hotovo /tmp/readme.txt
more /tmp/readme.txt
rm /tmp/readme.txt
rm -rf /tmp/test
####################################################################################################

[ -d /tmp/test ] || mkdir -p /tmp/test
cp /etc/CCcam.cfg /tmp/test/seznam
cd /tmp/test
sed -n '12,12p' seznam > řádek

cut -c 4-55 řádek  > řádek1
sed -e "s/ /,/" řádek1 > řádek2
cut -d ' ' -f 1  řádek2 > adresaport
cut -d ' ' -f 2  řádek2 > jméno
cut -d ' ' -f 3  řádek2 > heslo
cut -d, -f 1 řádek2 > adresa
echo "[reader]" > 1
echo "label=" > 2
echo "enable=1" > 3
echo "protocol=cccam" > 4
echo "device=" > 5
echo "user=" > 6
echo "password=" > 7
cat  2 adresa > 2a
cat 2a | tr -d '\n' > 2b
cat  5 adresaport > 5a
cat 5a | tr -d '\n' > 5b
cat  6 jméno > 6a
cat 6a | tr -d '\n' > 6b
cat  7 heslo > 7a
cat 7a | tr -d '\n' > 7b
cat 1 2b > hotovo
echo "" >> hotovo
echo "enable=1$1" >> hotovo
echo "protocol=cccam" >> hotovo
cat 5 adresaport >> adresaport1
cat adresaport1 | tr -d '\n' >> hotovo
echo "" >> hotovo
cat 6 jméno >> jméno1
cat jméno1 | tr -d '\n' >> hotovo
echo "" >> hotovo
cat 7 heslo >> heslo1
cat heslo1 | tr -d '\n' >> hotovo
echo "" >> hotovo
echo "cccversion=2.1.2" >> hotovo
echo "group=1" >> hotovo

echo "inactivitytimeout=1" >> hotovo

echo "reconnecttimeout=30" >> hotovo

echo "lb_weight=100" >> hotovo

echo "cccmaxhops=10" >> hotovo

echo "ccckeepalive=1" >> hotovo
echo "" >> hotovo
echo "" >> hotovo

cp hotovo /tmp/test2/server12
cp hotovo /tmp/readme.txt
more /tmp/readme.txt
rm /tmp/readme.txt
rm -rf /tmp/test
####################################################################################################

[ -d /tmp/test ] || mkdir -p /tmp/test
cp /etc/CCcam.cfg /tmp/test/seznam
cd /tmp/test
sed -n '13,13p' seznam > řádek

cut -c 4-55 řádek  > řádek1
sed -e "s/ /,/" řádek1 > řádek2
cut -d ' ' -f 1  řádek2 > adresaport
cut -d ' ' -f 2  řádek2 > jméno
cut -d ' ' -f 3  řádek2 > heslo
cut -d, -f 1 řádek2 > adresa
echo "[reader]" > 1
echo "label=" > 2
echo "enable=1" > 3
echo "protocol=cccam" > 4
echo "device=" > 5
echo "user=" > 6
echo "password=" > 7
cat  2 adresa > 2a
cat 2a | tr -d '\n' > 2b
cat  5 adresaport > 5a
cat 5a | tr -d '\n' > 5b
cat  6 jméno > 6a
cat 6a | tr -d '\n' > 6b
cat  7 heslo > 7a
cat 7a | tr -d '\n' > 7b
cat 1 2b > hotovo
echo "" >> hotovo
echo "enable=1$1" >> hotovo
echo "protocol=cccam" >> hotovo
cat 5 adresaport >> adresaport1
cat adresaport1 | tr -d '\n' >> hotovo
echo "" >> hotovo
cat 6 jméno >> jméno1
cat jméno1 | tr -d '\n' >> hotovo
echo "" >> hotovo
cat 7 heslo >> heslo1
cat heslo1 | tr -d '\n' >> hotovo
echo "" >> hotovo
echo "cccversion=2.1.2" >> hotovo
echo "group=1" >> hotovo

echo "inactivitytimeout=1" >> hotovo

echo "reconnecttimeout=30" >> hotovo

echo "lb_weight=100" >> hotovo

echo "cccmaxhops=10" >> hotovo

echo "ccckeepalive=1" >> hotovo
echo "" >> hotovo
echo "" >> hotovo

cp hotovo /tmp/test2/server13
cp hotovo /tmp/readme.txt
more /tmp/readme.txt
rm /tmp/readme.txt
rm -rf /tmp/test
####################################################################################################

[ -d /tmp/test ] || mkdir -p /tmp/test
cp /etc/CCcam.cfg /tmp/test/seznam
cd /tmp/test
sed -n '14,14p' seznam > řádek

cut -c 4-55 řádek  > řádek1
sed -e "s/ /,/" řádek1 > řádek2
cut -d ' ' -f 1  řádek2 > adresaport
cut -d ' ' -f 2  řádek2 > jméno
cut -d ' ' -f 3  řádek2 > heslo
cut -d, -f 1 řádek2 > adresa
echo "[reader]" > 1
echo "label=" > 2
echo "enable=1" > 3
echo "protocol=cccam" > 4
echo "device=" > 5
echo "user=" > 6
echo "password=" > 7
cat  2 adresa > 2a
cat 2a | tr -d '\n' > 2b
cat  5 adresaport > 5a
cat 5a | tr -d '\n' > 5b
cat  6 jméno > 6a
cat 6a | tr -d '\n' > 6b
cat  7 heslo > 7a
cat 7a | tr -d '\n' > 7b
cat 1 2b > hotovo
echo "" >> hotovo
echo "enable=1$1" >> hotovo
echo "protocol=cccam" >> hotovo
cat 5 adresaport >> adresaport1
cat adresaport1 | tr -d '\n' >> hotovo
echo "" >> hotovo
cat 6 jméno >> jméno1
cat jméno1 | tr -d '\n' >> hotovo
echo "" >> hotovo
cat 7 heslo >> heslo1
cat heslo1 | tr -d '\n' >> hotovo
echo "" >> hotovo
echo "cccversion=2.1.2" >> hotovo
echo "group=1" >> hotovo

echo "inactivitytimeout=1" >> hotovo

echo "reconnecttimeout=30" >> hotovo

echo "lb_weight=100" >> hotovo

echo "cccmaxhops=10" >> hotovo

echo "ccckeepalive=1" >> hotovo
echo "" >> hotovo
echo "" >> hotovo

cp hotovo /tmp/test2/server14
cp hotovo /tmp/readme.txt
more /tmp/readme.txt
rm /tmp/readme.txt
rm -rf /tmp/test
####################################################################################################

[ -d /tmp/test ] || mkdir -p /tmp/test
cp /etc/CCcam.cfg /tmp/test/seznam
cd /tmp/test
sed -n '15,15p' seznam > řádek

cut -c 4-55 řádek  > řádek1
sed -e "s/ /,/" řádek1 > řádek2
cut -d ' ' -f 1  řádek2 > adresaport
cut -d ' ' -f 2  řádek2 > jméno
cut -d ' ' -f 3  řádek2 > heslo
cut -d, -f 1 řádek2 > adresa
echo "[reader]" > 1
echo "label=" > 2
echo "enable=1" > 3
echo "protocol=cccam" > 4
echo "device=" > 5
echo "user=" > 6
echo "password=" > 7
cat  2 adresa > 2a
cat 2a | tr -d '\n' > 2b
cat  5 adresaport > 5a
cat 5a | tr -d '\n' > 5b
cat  6 jméno > 6a
cat 6a | tr -d '\n' > 6b
cat  7 heslo > 7a
cat 7a | tr -d '\n' > 7b
cat 1 2b > hotovo
echo "" >> hotovo
echo "enable=1$1" >> hotovo
echo "protocol=cccam" >> hotovo
cat 5 adresaport >> adresaport1
cat adresaport1 | tr -d '\n' >> hotovo
echo "" >> hotovo
cat 6 jméno >> jméno1
cat jméno1 | tr -d '\n' >> hotovo
echo "" >> hotovo
cat 7 heslo >> heslo1
cat heslo1 | tr -d '\n' >> hotovo
echo "" >> hotovo
echo "cccversion=2.1.2" >> hotovo
echo "group=1" >> hotovo

echo "inactivitytimeout=1" >> hotovo

echo "reconnecttimeout=30" >> hotovo

echo "lb_weight=100" >> hotovo

echo "cccmaxhops=10" >> hotovo

echo "ccckeepalive=1" >> hotovo
echo "" >> hotovo
echo "" >> hotovo

cp hotovo /tmp/test2/server15
cp hotovo /tmp/readme.txt
more /tmp/readme.txt
rm /tmp/readme.txt
rm -rf /tmp/test
####################################################################################################

[ -d /tmp/test ] || mkdir -p /tmp/test
cp /etc/CCcam.cfg /tmp/test/seznam
cd /tmp/test
sed -n '16,16p' seznam > řádek

cut -c 4-55 řádek  > řádek1
sed -e "s/ /,/" řádek1 > řádek2
cut -d ' ' -f 1  řádek2 > adresaport
cut -d ' ' -f 2  řádek2 > jméno
cut -d ' ' -f 3  řádek2 > heslo
cut -d, -f 1 řádek2 > adresa
echo "[reader]" > 1
echo "label=" > 2
echo "enable=1" > 3
echo "protocol=cccam" > 4
echo "device=" > 5
echo "user=" > 6
echo "password=" > 7
cat  2 adresa > 2a
cat 2a | tr -d '\n' > 2b
cat  5 adresaport > 5a
cat 5a | tr -d '\n' > 5b
cat  6 jméno > 6a
cat 6a | tr -d '\n' > 6b
cat  7 heslo > 7a
cat 7a | tr -d '\n' > 7b
cat 1 2b > hotovo
echo "" >> hotovo
echo "enable=1$1" >> hotovo
echo "protocol=cccam" >> hotovo
cat 5 adresaport >> adresaport1
cat adresaport1 | tr -d '\n' >> hotovo
echo "" >> hotovo
cat 6 jméno >> jméno1
cat jméno1 | tr -d '\n' >> hotovo
echo "" >> hotovo
cat 7 heslo >> heslo1
cat heslo1 | tr -d '\n' >> hotovo
echo "" >> hotovo
echo "cccversion=2.1.2" >> hotovo
echo "group=1" >> hotovo

echo "inactivitytimeout=1" >> hotovo

echo "reconnecttimeout=30" >> hotovo

echo "lb_weight=100" >> hotovo

echo "cccmaxhops=10" >> hotovo

echo "ccckeepalive=1" >> hotovo
echo "" >> hotovo
echo "" >> hotovo

cp hotovo /tmp/test2/server16
cp hotovo /tmp/readme.txt
more /tmp/readme.txt
rm /tmp/readme.txt
rm -rf /tmp/test
####################################################################################################

[ -d /tmp/test ] || mkdir -p /tmp/test
cp /etc/CCcam.cfg /tmp/test/seznam
cd /tmp/test
sed -n '17,17p' seznam > řádek

cut -c 4-55 řádek  > řádek1
sed -e "s/ /,/" řádek1 > řádek2
cut -d ' ' -f 1  řádek2 > adresaport
cut -d ' ' -f 2  řádek2 > jméno
cut -d ' ' -f 3  řádek2 > heslo
cut -d, -f 1 řádek2 > adresa
echo "[reader]" > 1
echo "label=" > 2
echo "enable=1" > 3
echo "protocol=cccam" > 4
echo "device=" > 5
echo "user=" > 6
echo "password=" > 7
cat  2 adresa > 2a
cat 2a | tr -d '\n' > 2b
cat  5 adresaport > 5a
cat 5a | tr -d '\n' > 5b
cat  6 jméno > 6a
cat 6a | tr -d '\n' > 6b
cat  7 heslo > 7a
cat 7a | tr -d '\n' > 7b
cat 1 2b > hotovo
echo "" >> hotovo
echo "enable=1$1" >> hotovo
echo "protocol=cccam" >> hotovo
cat 5 adresaport >> adresaport1
cat adresaport1 | tr -d '\n' >> hotovo
echo "" >> hotovo
cat 6 jméno >> jméno1
cat jméno1 | tr -d '\n' >> hotovo
echo "" >> hotovo
cat 7 heslo >> heslo1
cat heslo1 | tr -d '\n' >> hotovo
echo "" >> hotovo
echo "cccversion=2.1.2" >> hotovo
echo "group=1" >> hotovo

echo "inactivitytimeout=1" >> hotovo

echo "reconnecttimeout=30" >> hotovo

echo "lb_weight=100" >> hotovo

echo "cccmaxhops=10" >> hotovo

echo "ccckeepalive=1" >> hotovo
echo "" >> hotovo
echo "" >> hotovo

cp hotovo /tmp/test2/server17
cp hotovo /tmp/readme.txt
more /tmp/readme.txt
rm /tmp/readme.txt
rm -rf /tmp/test
####################################################################################################

[ -d /tmp/test ] || mkdir -p /tmp/test
cp /etc/CCcam.cfg /tmp/test/seznam
cd /tmp/test
sed -n '18,18p' seznam > řádek

cut -c 4-55 řádek  > řádek1
sed -e "s/ /,/" řádek1 > řádek2
cut -d ' ' -f 1  řádek2 > adresaport
cut -d ' ' -f 2  řádek2 > jméno
cut -d ' ' -f 3  řádek2 > heslo
cut -d, -f 1 řádek2 > adresa
echo "[reader]" > 1
echo "label=" > 2
echo "enable=1" > 3
echo "protocol=cccam" > 4
echo "device=" > 5
echo "user=" > 6
echo "password=" > 7
cat  2 adresa > 2a
cat 2a | tr -d '\n' > 2b
cat  5 adresaport > 5a
cat 5a | tr -d '\n' > 5b
cat  6 jméno > 6a
cat 6a | tr -d '\n' > 6b
cat  7 heslo > 7a
cat 7a | tr -d '\n' > 7b
cat 1 2b > hotovo
echo "" >> hotovo
echo "enable=1$1" >> hotovo
echo "protocol=cccam" >> hotovo
cat 5 adresaport >> adresaport1
cat adresaport1 | tr -d '\n' >> hotovo
echo "" >> hotovo
cat 6 jméno >> jméno1
cat jméno1 | tr -d '\n' >> hotovo
echo "" >> hotovo
cat 7 heslo >> heslo1
cat heslo1 | tr -d '\n' >> hotovo
echo "" >> hotovo
echo "cccversion=2.1.2" >> hotovo
echo "group=1" >> hotovo

echo "inactivitytimeout=1" >> hotovo

echo "reconnecttimeout=30" >> hotovo

echo "lb_weight=100" >> hotovo

echo "cccmaxhops=10" >> hotovo

echo "ccckeepalive=1" >> hotovo
echo "" >> hotovo
echo "" >> hotovo

cp hotovo /tmp/test2/server18
cp hotovo /tmp/readme.txt
more /tmp/readme.txt
rm /tmp/readme.txt
rm -rf /tmp/test
####################################################################################################

[ -d /tmp/test ] || mkdir -p /tmp/test
cp /etc/CCcam.cfg /tmp/test/seznam
cd /tmp/test
sed -n '19,19p' seznam > řádek

cut -c 4-55 řádek  > řádek1
sed -e "s/ /,/" řádek1 > řádek2
cut -d ' ' -f 1  řádek2 > adresaport
cut -d ' ' -f 2  řádek2 > jméno
cut -d ' ' -f 3  řádek2 > heslo
cut -d, -f 1 řádek2 > adresa
echo "[reader]" > 1
echo "label=" > 2
echo "enable=1" > 3
echo "protocol=cccam" > 4
echo "device=" > 5
echo "user=" > 6
echo "password=" > 7
cat  2 adresa > 2a
cat 2a | tr -d '\n' > 2b
cat  5 adresaport > 5a
cat 5a | tr -d '\n' > 5b
cat  6 jméno > 6a
cat 6a | tr -d '\n' > 6b
cat  7 heslo > 7a
cat 7a | tr -d '\n' > 7b
cat 1 2b > hotovo
echo "" >> hotovo
echo "enable=1$1" >> hotovo
echo "protocol=cccam" >> hotovo
cat 5 adresaport >> adresaport1
cat adresaport1 | tr -d '\n' >> hotovo
echo "" >> hotovo
cat 6 jméno >> jméno1
cat jméno1 | tr -d '\n' >> hotovo
echo "" >> hotovo
cat 7 heslo >> heslo1
cat heslo1 | tr -d '\n' >> hotovo
echo "" >> hotovo
echo "cccversion=2.1.2" >> hotovo
echo "group=1" >> hotovo

echo "inactivitytimeout=1" >> hotovo

echo "reconnecttimeout=30" >> hotovo

echo "lb_weight=100" >> hotovo

echo "cccmaxhops=10" >> hotovo

echo "ccckeepalive=1" >> hotovo
echo "" >> hotovo
echo "" >> hotovo

cp hotovo /tmp/test2/server19
cp hotovo /tmp/readme.txt
more /tmp/readme.txt
rm /tmp/readme.txt
rm -rf /tmp/test
####################################################################################################

[ -d /tmp/test ] || mkdir -p /tmp/test
cp /etc/CCcam.cfg /tmp/test/seznam
cd /tmp/test
sed -n '20,20p' seznam > řádek

cut -c 4-55 řádek  > řádek1
sed -e "s/ /,/" řádek1 > řádek2
cut -d ' ' -f 1  řádek2 > adresaport
cut -d ' ' -f 2  řádek2 > jméno
cut -d ' ' -f 3  řádek2 > heslo
cut -d, -f 1 řádek2 > adresa
echo "[reader]" > 1
echo "label=" > 2
echo "enable=1" > 3
echo "protocol=cccam" > 4
echo "device=" > 5
echo "user=" > 6
echo "password=" > 7
cat  2 adresa > 2a
cat 2a | tr -d '\n' > 2b
cat  5 adresaport > 5a
cat 5a | tr -d '\n' > 5b
cat  6 jméno > 6a
cat 6a | tr -d '\n' > 6b
cat  7 heslo > 7a
cat 7a | tr -d '\n' > 7b
cat 1 2b > hotovo
echo "" >> hotovo
echo "enable=1$1" >> hotovo
echo "protocol=cccam" >> hotovo
cat 5 adresaport >> adresaport1
cat adresaport1 | tr -d '\n' >> hotovo
echo "" >> hotovo
cat 6 jméno >> jméno1
cat jméno1 | tr -d '\n' >> hotovo
echo "" >> hotovo
cat 7 heslo >> heslo1
cat heslo1 | tr -d '\n' >> hotovo
echo "" >> hotovo
echo "cccversion=2.1.2" >> hotovo
echo "group=1" >> hotovo

echo "inactivitytimeout=1" >> hotovo

echo "reconnecttimeout=30" >> hotovo

echo "lb_weight=100" >> hotovo

echo "cccmaxhops=10" >> hotovo

echo "ccckeepalive=1" >> hotovo
echo "" >> hotovo
echo "" >> hotovo

cp hotovo /tmp/test2/server20
cp hotovo /tmp/readme.txt
more /tmp/readme.txt
rm /tmp/readme.txt
rm -rf /tmp/test
####################################################################################################

[ -d /tmp/test ] || mkdir -p /tmp/test
cp /etc/CCcam.cfg /tmp/test/seznam
cd /tmp/test
sed -n '21,21p' seznam > řádek

cut -c 4-55 řádek  > řádek1
sed -e "s/ /,/" řádek1 > řádek2
cut -d ' ' -f 1  řádek2 > adresaport
cut -d ' ' -f 2  řádek2 > jméno
cut -d ' ' -f 3  řádek2 > heslo
cut -d, -f 1 řádek2 > adresa
echo "[reader]" > 1
echo "label=" > 2
echo "enable=1" > 3
echo "protocol=cccam" > 4
echo "device=" > 5
echo "user=" > 6
echo "password=" > 7
cat  2 adresa > 2a
cat 2a | tr -d '\n' > 2b
cat  5 adresaport > 5a
cat 5a | tr -d '\n' > 5b
cat  6 jméno > 6a
cat 6a | tr -d '\n' > 6b
cat  7 heslo > 7a
cat 7a | tr -d '\n' > 7b
cat 1 2b > hotovo
echo "" >> hotovo
echo "enable=1$1" >> hotovo
echo "protocol=cccam" >> hotovo
cat 5 adresaport >> adresaport1
cat adresaport1 | tr -d '\n' >> hotovo
echo "" >> hotovo
cat 6 jméno >> jméno1
cat jméno1 | tr -d '\n' >> hotovo
echo "" >> hotovo
cat 7 heslo >> heslo1
cat heslo1 | tr -d '\n' >> hotovo
echo "" >> hotovo
echo "cccversion=2.1.2" >> hotovo
echo "group=1" >> hotovo

echo "inactivitytimeout=1" >> hotovo

echo "reconnecttimeout=30" >> hotovo

echo "lb_weight=100" >> hotovo

echo "cccmaxhops=10" >> hotovo

echo "ccckeepalive=1" >> hotovo
echo "" >> hotovo
echo "" >> hotovo

cp hotovo /tmp/test2/server21
cp hotovo /tmp/readme.txt
more /tmp/readme.txt
rm /tmp/readme.txt
rm -rf /tmp/test
####################################################################################################

[ -d /tmp/test ] || mkdir -p /tmp/test
cp /etc/CCcam.cfg /tmp/test/seznam
cd /tmp/test
sed -n '22,22p' seznam > řádek

cut -c 4-55 řádek  > řádek1
sed -e "s/ /,/" řádek1 > řádek2
cut -d ' ' -f 1  řádek2 > adresaport
cut -d ' ' -f 2  řádek2 > jméno
cut -d ' ' -f 3  řádek2 > heslo
cut -d, -f 1 řádek2 > adresa
echo "[reader]" > 1
echo "label=" > 2
echo "enable=1" > 3
echo "protocol=cccam" > 4
echo "device=" > 5
echo "user=" > 6
echo "password=" > 7
cat  2 adresa > 2a
cat 2a | tr -d '\n' > 2b
cat  5 adresaport > 5a
cat 5a | tr -d '\n' > 5b
cat  6 jméno > 6a
cat 6a | tr -d '\n' > 6b
cat  7 heslo > 7a
cat 7a | tr -d '\n' > 7b
cat 1 2b > hotovo
echo "" >> hotovo
echo "enable=1$1" >> hotovo
echo "protocol=cccam" >> hotovo
cat 5 adresaport >> adresaport1
cat adresaport1 | tr -d '\n' >> hotovo
echo "" >> hotovo
cat 6 jméno >> jméno1
cat jméno1 | tr -d '\n' >> hotovo
echo "" >> hotovo
cat 7 heslo >> heslo1
cat heslo1 | tr -d '\n' >> hotovo
echo "" >> hotovo
echo "cccversion=2.1.2" >> hotovo
echo "group=1" >> hotovo

echo "inactivitytimeout=1" >> hotovo

echo "reconnecttimeout=30" >> hotovo

echo "lb_weight=100" >> hotovo

echo "cccmaxhops=10" >> hotovo

echo "ccckeepalive=1" >> hotovo
echo "" >> hotovo
echo "" >> hotovo

cp hotovo /tmp/test2/server22
cp hotovo /tmp/readme.txt
more /tmp/readme.txt
rm /tmp/readme.txt
rm -rf /tmp/test
####################################################################################################

[ -d /tmp/test ] || mkdir -p /tmp/test
cp /etc/CCcam.cfg /tmp/test/seznam
cd /tmp/test
sed -n '23,23p' seznam > řádek

cut -c 4-55 řádek  > řádek1
sed -e "s/ /,/" řádek1 > řádek2
cut -d ' ' -f 1  řádek2 > adresaport
cut -d ' ' -f 2  řádek2 > jméno
cut -d ' ' -f 3  řádek2 > heslo
cut -d, -f 1 řádek2 > adresa
echo "[reader]" > 1
echo "label=" > 2
echo "enable=1" > 3
echo "protocol=cccam" > 4
echo "device=" > 5
echo "user=" > 6
echo "password=" > 7
cat  2 adresa > 2a
cat 2a | tr -d '\n' > 2b
cat  5 adresaport > 5a
cat 5a | tr -d '\n' > 5b
cat  6 jméno > 6a
cat 6a | tr -d '\n' > 6b
cat  7 heslo > 7a
cat 7a | tr -d '\n' > 7b
cat 1 2b > hotovo
echo "" >> hotovo
echo "enable=1$1" >> hotovo
echo "protocol=cccam" >> hotovo
cat 5 adresaport >> adresaport1
cat adresaport1 | tr -d '\n' >> hotovo
echo "" >> hotovo
cat 6 jméno >> jméno1
cat jméno1 | tr -d '\n' >> hotovo
echo "" >> hotovo
cat 7 heslo >> heslo1
cat heslo1 | tr -d '\n' >> hotovo
echo "" >> hotovo
echo "cccversion=2.1.2" >> hotovo
echo "group=1" >> hotovo

echo "inactivitytimeout=1" >> hotovo

echo "reconnecttimeout=30" >> hotovo

echo "lb_weight=100" >> hotovo

echo "cccmaxhops=10" >> hotovo

echo "ccckeepalive=1" >> hotovo
echo "" >> hotovo
echo "" >> hotovo

cp hotovo /tmp/test2/server23
cp hotovo /tmp/readme.txt
more /tmp/readme.txt
rm /tmp/readme.txt
rm -rf /tmp/test
####################################################################################################

[ -d /tmp/test ] || mkdir -p /tmp/test
cp /etc/CCcam.cfg /tmp/test/seznam
cd /tmp/test
sed -n '24,24p' seznam > řádek

cut -c 4-55 řádek  > řádek1
sed -e "s/ /,/" řádek1 > řádek2
cut -d ' ' -f 1  řádek2 > adresaport
cut -d ' ' -f 2  řádek2 > jméno
cut -d ' ' -f 3  řádek2 > heslo
cut -d, -f 1 řádek2 > adresa
echo "[reader]" > 1
echo "label=" > 2
echo "enable=1" > 3
echo "protocol=cccam" > 4
echo "device=" > 5
echo "user=" > 6
echo "password=" > 7
cat  2 adresa > 2a
cat 2a | tr -d '\n' > 2b
cat  5 adresaport > 5a
cat 5a | tr -d '\n' > 5b
cat  6 jméno > 6a
cat 6a | tr -d '\n' > 6b
cat  7 heslo > 7a
cat 7a | tr -d '\n' > 7b
cat 1 2b > hotovo
echo "" >> hotovo
echo "enable=1$1" >> hotovo
echo "protocol=cccam" >> hotovo
cat 5 adresaport >> adresaport1
cat adresaport1 | tr -d '\n' >> hotovo
echo "" >> hotovo
cat 6 jméno >> jméno1
cat jméno1 | tr -d '\n' >> hotovo
echo "" >> hotovo
cat 7 heslo >> heslo1
cat heslo1 | tr -d '\n' >> hotovo
echo "" >> hotovo
echo "cccversion=2.1.2" >> hotovo
echo "group=1" >> hotovo

echo "inactivitytimeout=1" >> hotovo

echo "reconnecttimeout=30" >> hotovo

echo "lb_weight=100" >> hotovo

echo "cccmaxhops=10" >> hotovo

echo "ccckeepalive=1" >> hotovo
echo "" >> hotovo
echo "" >> hotovo

cp hotovo /tmp/test2/server24
cp hotovo /tmp/readme.txt
more /tmp/readme.txt
rm /tmp/readme.txt
rm -rf /tmp/test
####################################################################################################

[ -d /tmp/test ] || mkdir -p /tmp/test
cp /etc/CCcam.cfg /tmp/test/seznam
cd /tmp/test
sed -n '25,25p' seznam > řádek

cut -c 4-55 řádek  > řádek1
sed -e "s/ /,/" řádek1 > řádek2
cut -d ' ' -f 1  řádek2 > adresaport
cut -d ' ' -f 2  řádek2 > jméno
cut -d ' ' -f 3  řádek2 > heslo
cut -d, -f 1 řádek2 > adresa
echo "[reader]" > 1
echo "label=" > 2
echo "enable=1" > 3
echo "protocol=cccam" > 4
echo "device=" > 5
echo "user=" > 6
echo "password=" > 7
cat  2 adresa > 2a
cat 2a | tr -d '\n' > 2b
cat  5 adresaport > 5a
cat 5a | tr -d '\n' > 5b
cat  6 jméno > 6a
cat 6a | tr -d '\n' > 6b
cat  7 heslo > 7a
cat 7a | tr -d '\n' > 7b
cat 1 2b > hotovo
echo "" >> hotovo
echo "enable=1$1" >> hotovo
echo "protocol=cccam" >> hotovo
cat 5 adresaport >> adresaport1
cat adresaport1 | tr -d '\n' >> hotovo
echo "" >> hotovo
cat 6 jméno >> jméno1
cat jméno1 | tr -d '\n' >> hotovo
echo "" >> hotovo
cat 7 heslo >> heslo1
cat heslo1 | tr -d '\n' >> hotovo
echo "" >> hotovo
echo "cccversion=2.1.2" >> hotovo
echo "group=1" >> hotovo

echo "inactivitytimeout=1" >> hotovo

echo "reconnecttimeout=30" >> hotovo

echo "lb_weight=100" >> hotovo

echo "cccmaxhops=10" >> hotovo

echo "ccckeepalive=1" >> hotovo
echo "" >> hotovo
echo "" >> hotovo

cp hotovo /tmp/test2/server25
cp hotovo /tmp/readme.txt
more /tmp/readme.txt
rm /tmp/readme.txt
rm -rf /tmp/test
####################################################################################################

[ -d /tmp/test ] || mkdir -p /tmp/test
cp /etc/CCcam.cfg /tmp/test/seznam
cd /tmp/test
sed -n '26,26p' seznam > řádek

cut -c 4-55 řádek  > řádek1
sed -e "s/ /,/" řádek1 > řádek2
cut -d ' ' -f 1  řádek2 > adresaport
cut -d ' ' -f 2  řádek2 > jméno
cut -d ' ' -f 3  řádek2 > heslo
cut -d, -f 1 řádek2 > adresa
echo "[reader]" > 1
echo "label=" > 2
echo "enable=1" > 3
echo "protocol=cccam" > 4
echo "device=" > 5
echo "user=" > 6
echo "password=" > 7
cat  2 adresa > 2a
cat 2a | tr -d '\n' > 2b
cat  5 adresaport > 5a
cat 5a | tr -d '\n' > 5b
cat  6 jméno > 6a
cat 6a | tr -d '\n' > 6b
cat  7 heslo > 7a
cat 7a | tr -d '\n' > 7b
cat 1 2b > hotovo
echo "" >> hotovo
echo "enable=1$1" >> hotovo
echo "protocol=cccam" >> hotovo
cat 5 adresaport >> adresaport1
cat adresaport1 | tr -d '\n' >> hotovo
echo "" >> hotovo
cat 6 jméno >> jméno1
cat jméno1 | tr -d '\n' >> hotovo
echo "" >> hotovo
cat 7 heslo >> heslo1
cat heslo1 | tr -d '\n' >> hotovo
echo "" >> hotovo
echo "cccversion=2.1.2" >> hotovo
echo "group=1" >> hotovo

echo "inactivitytimeout=1" >> hotovo

echo "reconnecttimeout=30" >> hotovo

echo "lb_weight=100" >> hotovo

echo "cccmaxhops=10" >> hotovo

echo "ccckeepalive=1" >> hotovo
echo "" >> hotovo
echo "" >> hotovo

cp hotovo /tmp/test2/server26
cp hotovo /tmp/readme.txt
more /tmp/readme.txt
rm /tmp/readme.txt
rm -rf /tmp/test
####################################################################################################

[ -d /tmp/test ] || mkdir -p /tmp/test
cp /etc/CCcam.cfg /tmp/test/seznam
cd /tmp/test
sed -n '27,27p' seznam > řádek

cut -c 4-55 řádek  > řádek1
sed -e "s/ /,/" řádek1 > řádek2
cut -d ' ' -f 1  řádek2 > adresaport
cut -d ' ' -f 2  řádek2 > jméno
cut -d ' ' -f 3  řádek2 > heslo
cut -d, -f 1 řádek2 > adresa
echo "[reader]" > 1
echo "label=" > 2
echo "enable=1" > 3
echo "protocol=cccam" > 4
echo "device=" > 5
echo "user=" > 6
echo "password=" > 7
cat  2 adresa > 2a
cat 2a | tr -d '\n' > 2b
cat  5 adresaport > 5a
cat 5a | tr -d '\n' > 5b
cat  6 jméno > 6a
cat 6a | tr -d '\n' > 6b
cat  7 heslo > 7a
cat 7a | tr -d '\n' > 7b
cat 1 2b > hotovo
echo "" >> hotovo
echo "enable=1$1" >> hotovo
echo "protocol=cccam" >> hotovo
cat 5 adresaport >> adresaport1
cat adresaport1 | tr -d '\n' >> hotovo
echo "" >> hotovo
cat 6 jméno >> jméno1
cat jméno1 | tr -d '\n' >> hotovo
echo "" >> hotovo
cat 7 heslo >> heslo1
cat heslo1 | tr -d '\n' >> hotovo
echo "" >> hotovo
echo "cccversion=2.1.2" >> hotovo
echo "group=1" >> hotovo

echo "inactivitytimeout=1" >> hotovo

echo "reconnecttimeout=30" >> hotovo

echo "lb_weight=100" >> hotovo

echo "cccmaxhops=10" >> hotovo

echo "ccckeepalive=1" >> hotovo
echo "" >> hotovo
echo "" >> hotovo

cp hotovo /tmp/test2/server27
cp hotovo /tmp/readme.txt
more /tmp/readme.txt
rm /tmp/readme.txt
rm -rf /tmp/test
####################################################################################################

[ -d /tmp/test ] || mkdir -p /tmp/test
cp /etc/CCcam.cfg /tmp/test/seznam
cd /tmp/test
sed -n '28,28p' seznam > řádek

cut -c 4-55 řádek  > řádek1
sed -e "s/ /,/" řádek1 > řádek2
cut -d ' ' -f 1  řádek2 > adresaport
cut -d ' ' -f 2  řádek2 > jméno
cut -d ' ' -f 3  řádek2 > heslo
cut -d, -f 1 řádek2 > adresa
echo "[reader]" > 1
echo "label=" > 2
echo "enable=1" > 3
echo "protocol=cccam" > 4
echo "device=" > 5
echo "user=" > 6
echo "password=" > 7
cat  2 adresa > 2a
cat 2a | tr -d '\n' > 2b
cat  5 adresaport > 5a
cat 5a | tr -d '\n' > 5b
cat  6 jméno > 6a
cat 6a | tr -d '\n' > 6b
cat  7 heslo > 7a
cat 7a | tr -d '\n' > 7b
cat 1 2b > hotovo
echo "" >> hotovo
echo "enable=1$1" >> hotovo
echo "protocol=cccam" >> hotovo
cat 5 adresaport >> adresaport1
cat adresaport1 | tr -d '\n' >> hotovo
echo "" >> hotovo
cat 6 jméno >> jméno1
cat jméno1 | tr -d '\n' >> hotovo
echo "" >> hotovo
cat 7 heslo >> heslo1
cat heslo1 | tr -d '\n' >> hotovo
echo "" >> hotovo
echo "cccversion=2.1.2" >> hotovo
echo "group=1" >> hotovo

echo "inactivitytimeout=1" >> hotovo

echo "reconnecttimeout=30" >> hotovo

echo "lb_weight=100" >> hotovo

echo "cccmaxhops=10" >> hotovo

echo "ccckeepalive=1" >> hotovo
echo "" >> hotovo
echo "" >> hotovo

cp hotovo /tmp/test2/server28
cp hotovo /tmp/readme.txt
more /tmp/readme.txt
rm /tmp/readme.txt
rm -rf /tmp/test
####################################################################################################

[ -d /tmp/test ] || mkdir -p /tmp/test
cp /etc/CCcam.cfg /tmp/test/seznam
cd /tmp/test
sed -n '29,29p' seznam > řádek

cut -c 4-55 řádek  > řádek1
sed -e "s/ /,/" řádek1 > řádek2
cut -d ' ' -f 1  řádek2 > adresaport
cut -d ' ' -f 2  řádek2 > jméno
cut -d ' ' -f 3  řádek2 > heslo
cut -d, -f 1 řádek2 > adresa
echo "[reader]" > 1
echo "label=" > 2
echo "enable=1" > 3
echo "protocol=cccam" > 4
echo "device=" > 5
echo "user=" > 6
echo "password=" > 7
cat  2 adresa > 2a
cat 2a | tr -d '\n' > 2b
cat  5 adresaport > 5a
cat 5a | tr -d '\n' > 5b
cat  6 jméno > 6a
cat 6a | tr -d '\n' > 6b
cat  7 heslo > 7a
cat 7a | tr -d '\n' > 7b
cat 1 2b > hotovo
echo "" >> hotovo
echo "enable=1$1" >> hotovo
echo "protocol=cccam" >> hotovo
cat 5 adresaport >> adresaport1
cat adresaport1 | tr -d '\n' >> hotovo
echo "" >> hotovo
cat 6 jméno >> jméno1
cat jméno1 | tr -d '\n' >> hotovo
echo "" >> hotovo
cat 7 heslo >> heslo1
cat heslo1 | tr -d '\n' >> hotovo
echo "" >> hotovo
echo "cccversion=2.1.2" >> hotovo
echo "group=1" >> hotovo

echo "inactivitytimeout=1" >> hotovo

echo "reconnecttimeout=30" >> hotovo

echo "lb_weight=100" >> hotovo

echo "cccmaxhops=10" >> hotovo

echo "ccckeepalive=1" >> hotovo
echo "" >> hotovo
echo "" >> hotovo

cp hotovo /tmp/test2/server29
cp hotovo /tmp/readme.txt
more /tmp/readme.txt
rm /tmp/readme.txt
rm -rf /tmp/test
####################################################################################################

[ -d /tmp/test ] || mkdir -p /tmp/test
cp /etc/CCcam.cfg /tmp/test/seznam
cd /tmp/test
sed -n '30,30p' seznam > řádek

cut -c 4-55 řádek  > řádek1
sed -e "s/ /,/" řádek1 > řádek2
cut -d ' ' -f 1  řádek2 > adresaport
cut -d ' ' -f 2  řádek2 > jméno
cut -d ' ' -f 3  řádek2 > heslo
cut -d, -f 1 řádek2 > adresa
echo "[reader]" > 1
echo "label=" > 2
echo "enable=1" > 3
echo "protocol=cccam" > 4
echo "device=" > 5
echo "user=" > 6
echo "password=" > 7
cat  2 adresa > 2a
cat 2a | tr -d '\n' > 2b
cat  5 adresaport > 5a
cat 5a | tr -d '\n' > 5b
cat  6 jméno > 6a
cat 6a | tr -d '\n' > 6b
cat  7 heslo > 7a
cat 7a | tr -d '\n' > 7b
cat 1 2b > hotovo
echo "" >> hotovo
echo "enable=1$1" >> hotovo
echo "protocol=cccam" >> hotovo
cat 5 adresaport >> adresaport1
cat adresaport1 | tr -d '\n' >> hotovo
echo "" >> hotovo
cat 6 jméno >> jméno1
cat jméno1 | tr -d '\n' >> hotovo
echo "" >> hotovo
cat 7 heslo >> heslo1
cat heslo1 | tr -d '\n' >> hotovo
echo "" >> hotovo
echo "cccversion=2.1.2" >> hotovo
echo "group=1" >> hotovo

echo "inactivitytimeout=1" >> hotovo

echo "reconnecttimeout=30" >> hotovo

echo "lb_weight=100" >> hotovo

echo "cccmaxhops=10" >> hotovo

echo "ccckeepalive=1" >> hotovo
echo "" >> hotovo
echo "" >> hotovo

cp hotovo /tmp/test2/server30
cp hotovo /tmp/readme.txt
more /tmp/readme.txt
rm /tmp/readme.txt
rm -rf /tmp/test
####################################################################################################
cd /
cd /tmp/test2
cat server1 server2 server3 server4 server5 server6 server7 server8 server9 server10 server11 server12 server13 server14 server15 server16 server17 server18 server19 server20 server21 server22 server23 server24 server25 server26 server27 server28 server29 server30 > servery
cp servery /etc/tuxbox/config/oscam/oscam.server  >/dev/null 2>&1 </dev/null &
cp servery /etc/tuxbox/config/oscam_atv_free/oscam.server  >/dev/null 2>&1 </dev/null &
cp servery /etc/tuxbox/config/oscam.server  >/dev/null 2>&1 </dev/null &
cp servery /etc/tuxbox/config/gcam.server  >/dev/null 2>&1 </dev/null &
cp servery /etc/tuxbox/config/ncam.server  >/dev/null 2>&1 </dev/null &
rm -rf /tmp/test2
/etc/init.d/softcam restart  >/dev/null 2>&1 </dev/null &

exit
