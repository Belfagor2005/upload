#!/bin/sh
echo "stahuji seznam filmů"
echo ""
echo "předpokládaný čas 4 minuty"
echo ""





echo ""
echo ""
[ -d /movie ] || mkdir -p /movie
[ -d /tmp/test ] || mkdir -p /tmp/test
[ -d /tmp/film ] || mkdir -p /tmp/film




curl -k -A -k   https://prehraj.to/blade-1998-bluray-1080p/5bc0ac559468c > /tmp/test/CCcam
chmod 644 /tmp/test/CCcam
cd /tmp/test
sed -n '75,75p' CCcam > CCcam1
sed 's/\(["]\+\)/\n\1/g' CCcam1 > CCcam2
sed -n '2,2p' CCcam2 > CCcam3
tr -d '["]' < "CCcam3" > CCcam4
tr -d '[\]' < "CCcam4" > /tmp/film/film1
cd /
rm -rf /tmp/test
####################################################################################################
[ -d /tmp/test ] || mkdir -p /tmp/test

curl -k -A -k   https://prehraj.to/blade-2-2002-1080p-cz/5b28d873e17be > /tmp/test/CCcam
chmod 644 /tmp/test/CCcam
cd /tmp/test
sed -n '75,75p' CCcam > CCcam1
sed 's/\(["]\+\)/\n\1/g' CCcam1 > CCcam2
sed -n '2,2p' CCcam2 > CCcam3
tr -d '["]' < "CCcam3" > CCcam4
tr -d '[\]' < "CCcam4" > /tmp/film/film2
cd /
rm -rf /tmp/test
####################################################################################################
[ -d /tmp/test ] || mkdir -p /tmp/test

curl -k -A -k   https://prehraj.to/blade-trinity-2004/5ac71830063ec > /tmp/test/CCcam
chmod 644 /tmp/test/CCcam
cd /tmp/test
sed -n '75,75p' CCcam > CCcam1
sed 's/\(["]\+\)/\n\1/g' CCcam1 > CCcam2
sed -n '2,2p' CCcam2 > CCcam3
tr -d '["]' < "CCcam3" > CCcam4
tr -d '[\]' < "CCcam4" > /tmp/film/film3
cd /
rm -rf /tmp/test
####################################################################################################
[ -d /tmp/test ] || mkdir -p /tmp/test

curl -k -A -k   https://prehraj.to/iron-man-1-cz-dabing-hd/5db4c570e2c0d > /tmp/test/CCcam
chmod 644 /tmp/test/CCcam
cd /tmp/test
sed -n '75,75p' CCcam > CCcam1
sed 's/\(["]\+\)/\n\1/g' CCcam1 > CCcam2
sed -n '2,2p' CCcam2 > CCcam3
tr -d '["]' < "CCcam3" > CCcam4
tr -d '[\]' < "CCcam4" > /tmp/film/film4
cd /
rm -rf /tmp/test
####################################################################################################
[ -d /tmp/test ] || mkdir -p /tmp/test

curl -k -A -k   https://prehraj.to/iron-man-2-cz-dabing-2010/5a429908594ce > /tmp/test/CCcam
chmod 644 /tmp/test/CCcam
cd /tmp/test
sed -n '75,75p' CCcam > CCcam1
sed 's/\(["]\+\)/\n\1/g' CCcam1 > CCcam2
sed -n '2,2p' CCcam2 > CCcam3
tr -d '["]' < "CCcam3" > CCcam4
tr -d '[\]' < "CCcam4" > /tmp/film/film5
cd /
rm -rf /tmp/test
####################################################################################################
[ -d /tmp/test ] || mkdir -p /tmp/test

curl -k -A -k   https://prehraj.to/iron-man-3-2013-cz/5e4718acbeb30 > /tmp/test/CCcam
chmod 644 /tmp/test/CCcam
cd /tmp/test
sed -n '75,75p' CCcam > CCcam1
sed 's/\(["]\+\)/\n\1/g' CCcam1 > CCcam2
sed -n '2,2p' CCcam2 > CCcam3
tr -d '["]' < "CCcam3" > CCcam4
tr -d '[\]' < "CCcam4" > /tmp/film/film6
cd /
rm -rf /tmp/test
####################################################################################################
[ -d /tmp/test ] || mkdir -p /tmp/test

curl -k -A -k   https://prehraj.to/resident-evil-1-2002-cz-dabing-hit/56169e293c4ad > /tmp/test/CCcam
chmod 644 /tmp/test/CCcam
cd /tmp/test
sed -n '75,75p' CCcam > CCcam1
sed 's/\(["]\+\)/\n\1/g' CCcam1 > CCcam2
sed -n '2,2p' CCcam2 > CCcam3
tr -d '["]' < "CCcam3" > CCcam4
tr -d '[\]' < "CCcam4" > /tmp/film/film7
cd /
rm -rf /tmp/test
####################################################################################################
[ -d /tmp/test ] || mkdir -p /tmp/test

curl -k -A -k   https://prehraj.to/resident-evil-2-apokalypsa-cz-dabing-nejlepsi-kvalita/5ada0fad7e66b > /tmp/test/CCcam
chmod 644 /tmp/test/CCcam
cd /tmp/test
sed -n '75,75p' CCcam > CCcam1
sed 's/\(["]\+\)/\n\1/g' CCcam1 > CCcam2
sed -n '2,2p' CCcam2 > CCcam3
tr -d '["]' < "CCcam3" > CCcam4
tr -d '[\]' < "CCcam4" > /tmp/film/film8
cd /
rm -rf /tmp/test
####################################################################################################
[ -d /tmp/test ] || mkdir -p /tmp/test

curl -k -A -k   https://prehraj.to/resident-evil-3-zanik-2007-cz-dabing/58b462738af8d > /tmp/test/CCcam
chmod 644 /tmp/test/CCcam
cd /tmp/test
sed -n '75,75p' CCcam > CCcam1
sed 's/\(["]\+\)/\n\1/g' CCcam1 > CCcam2
sed -n '2,2p' CCcam2 > CCcam3
tr -d '["]' < "CCcam3" > CCcam4
tr -d '[\]' < "CCcam4" > /tmp/film/film9
cd /
rm -rf /tmp/test
####################################################################################################
[ -d /tmp/test ] || mkdir -p /tmp/test

curl -k -A -k   https://prehraj.to/resident-evil-4-afterlife-2010-cz-dabing-hit/591036bee4104 > /tmp/test/CCcam
chmod 644 /tmp/test/CCcam
cd /tmp/test
sed -n '75,75p' CCcam > CCcam1
sed 's/\(["]\+\)/\n\1/g' CCcam1 > CCcam2
sed -n '2,2p' CCcam2 > CCcam3
tr -d '["]' < "CCcam3" > CCcam4
tr -d '[\]' < "CCcam4" > /tmp/film/film10
cd /
rm -rf /tmp/test
####################################################################################################
[ -d /tmp/test ] || mkdir -p /tmp/test

curl -k -A -k   https://prehraj.to/resident-evil-5/58bfcb0b9d235 > /tmp/test/CCcam
chmod 644 /tmp/test/CCcam
cd /tmp/test
sed -n '75,75p' CCcam > CCcam1
sed 's/\(["]\+\)/\n\1/g' CCcam1 > CCcam2
sed -n '2,2p' CCcam2 > CCcam3
tr -d '["]' < "CCcam3" > CCcam4
tr -d '[\]' < "CCcam4" > /tmp/film/film11
cd /
rm -rf /tmp/test
####################################################################################################
[ -d /tmp/test ] || mkdir -p /tmp/test

curl -k -A -k   https://prehraj.to/resident-evil-6-posledni-kapitola-cz-dabing-2016-akcni/5a1b04f1dc639 > /tmp/test/CCcam
chmod 644 /tmp/test/CCcam
cd /tmp/test
sed -n '75,75p' CCcam > CCcam1
sed 's/\(["]\+\)/\n\1/g' CCcam1 > CCcam2
sed -n '2,2p' CCcam2 > CCcam3
tr -d '["]' < "CCcam3" > CCcam4
tr -d '[\]' < "CCcam4" > /tmp/film/film12
cd /
rm -rf /tmp/test
####################################################################################################
[ -d /tmp/test ] || mkdir -p /tmp/test

curl -k -A -k   https://prehraj.to/spiderman-1-cz-dabing-2002/57f9e9838c485 > /tmp/test/CCcam
chmod 644 /tmp/test/CCcam
cd /tmp/test
sed -n '75,75p' CCcam > CCcam1
sed 's/\(["]\+\)/\n\1/g' CCcam1 > CCcam2
sed -n '2,2p' CCcam2 > CCcam3
tr -d '["]' < "CCcam3" > CCcam4
tr -d '[\]' < "CCcam4" > /tmp/film/film13
cd /
rm -rf /tmp/test
####################################################################################################
[ -d /tmp/test ] || mkdir -p /tmp/test

curl -k -A -k   https://prehraj.to/spiderman-2-cz-dabing/58137b6e04746 > /tmp/test/CCcam
chmod 644 /tmp/test/CCcam
cd /tmp/test
sed -n '75,75p' CCcam > CCcam1
sed 's/\(["]\+\)/\n\1/g' CCcam1 > CCcam2
sed -n '2,2p' CCcam2 > CCcam3
tr -d '["]' < "CCcam3" > CCcam4
tr -d '[\]' < "CCcam4" > /tmp/film/film14
cd /
rm -rf /tmp/test
####################################################################################################
[ -d /tmp/test ] || mkdir -p /tmp/test

curl -k -A -k   https://prehraj.to/spiderman-3-2007-czdab/57dcb53207666 > /tmp/test/CCcam
chmod 644 /tmp/test/CCcam
cd /tmp/test
sed -n '75,75p' CCcam > CCcam1
sed 's/\(["]\+\)/\n\1/g' CCcam1 > CCcam2
sed -n '2,2p' CCcam2 > CCcam3
tr -d '["]' < "CCcam3" > CCcam4
tr -d '[\]' < "CCcam4" > /tmp/film/film15
cd /
rm -rf /tmp/test
####################################################################################################
[ -d /tmp/test ] || mkdir -p /tmp/test

curl -k -A -k   https://prehraj.to/avengers-1-2012-hdrip-cz-dabing-m3/5a268a02ebc1a > /tmp/test/CCcam
chmod 644 /tmp/test/CCcam
cd /tmp/test
sed -n '75,75p' CCcam > CCcam1
sed 's/\(["]\+\)/\n\1/g' CCcam1 > CCcam2
sed -n '2,2p' CCcam2 > CCcam3
tr -d '["]' < "CCcam3" > CCcam4
tr -d '[\]' < "CCcam4" > /tmp/film/film16
cd /
rm -rf /tmp/test
####################################################################################################
[ -d /tmp/test ] || mkdir -p /tmp/test

curl -k -A -k   https://prehraj.to/avengers-2-vek-ultrona-cz-dabing-2015/599b230088bdc > /tmp/test/CCcam
chmod 644 /tmp/test/CCcam
cd /tmp/test
sed -n '75,75p' CCcam > CCcam1
sed 's/\(["]\+\)/\n\1/g' CCcam1 > CCcam2
sed -n '2,2p' CCcam2 > CCcam3
tr -d '["]' < "CCcam3" > CCcam4
tr -d '[\]' < "CCcam4" > /tmp/film/film17
cd /
rm -rf /tmp/test
####################################################################################################
[ -d /tmp/test ] || mkdir -p /tmp/test

curl -k -A -k   https://prehraj.to/avengers-3-nekonecna-vojna-cz-dabing-2018/5be2ba3582b0d > /tmp/test/CCcam
chmod 644 /tmp/test/CCcam
cd /tmp/test
sed -n '75,75p' CCcam > CCcam1
sed 's/\(["]\+\)/\n\1/g' CCcam1 > CCcam2
sed -n '2,2p' CCcam2 > CCcam3
tr -d '["]' < "CCcam3" > CCcam4
tr -d '[\]' < "CCcam4" > /tmp/film/film18
cd /
rm -rf /tmp/test
####################################################################################################
[ -d /tmp/test ] || mkdir -p /tmp/test

curl -k -A -k   https://prehraj.to/avengers-4-endgame-2019-cz-dabing-bst/5d5d23cf27b43 > /tmp/test/CCcam
chmod 644 /tmp/test/CCcam
cd /tmp/test
sed -n '75,75p' CCcam > CCcam1
sed 's/\(["]\+\)/\n\1/g' CCcam1 > CCcam2
sed -n '2,2p' CCcam2 > CCcam3
tr -d '["]' < "CCcam3" > CCcam4
tr -d '[\]' < "CCcam4" > /tmp/film/film19
cd /
rm -rf /tmp/test
####################################################################################################
[ -d /tmp/test ] || mkdir -p /tmp/test

curl -k -A -k   https://prehraj.to/antman-cz-dabing/5b437fcb3b446 > /tmp/test/CCcam
chmod 644 /tmp/test/CCcam
cd /tmp/test
sed -n '75,75p' CCcam > CCcam1
sed 's/\(["]\+\)/\n\1/g' CCcam1 > CCcam2
sed -n '2,2p' CCcam2 > CCcam3
tr -d '["]' < "CCcam3" > CCcam4
tr -d '[\]' < "CCcam4" > /tmp/film/film20
cd /
rm -rf /tmp/test
####################################################################################################
[ -d /tmp/test ] || mkdir -p /tmp/test

curl -k -A -k   https://prehraj.to/ant-man-2-2018-cz-dabing/5bda1d52509a8 > /tmp/test/CCcam
chmod 644 /tmp/test/CCcam
cd /tmp/test
sed -n '75,75p' CCcam > CCcam1
sed 's/\(["]\+\)/\n\1/g' CCcam1 > CCcam2
sed -n '2,2p' CCcam2 > CCcam3
tr -d '["]' < "CCcam3" > CCcam4
tr -d '[\]' < "CCcam4" > /tmp/film/film21
cd /
rm -rf /tmp/test
####################################################################################################
[ -d /tmp/test ] || mkdir -p /tmp/test

curl -k -A -k   https://prehraj.to/thor-akcni-2011-cz-dabing/5e2c8708c2717 > /tmp/test/CCcam
chmod 644 /tmp/test/CCcam
cd /tmp/test
sed -n '75,75p' CCcam > CCcam1
sed 's/\(["]\+\)/\n\1/g' CCcam1 > CCcam2
sed -n '2,2p' CCcam2 > CCcam3
tr -d '["]' < "CCcam3" > CCcam4
tr -d '[\]' < "CCcam4" > /tmp/film/film22
cd /
rm -rf /tmp/test
####################################################################################################
[ -d /tmp/test ] || mkdir -p /tmp/test

curl -k -A -k   https://prehraj.to/thor-2-cz-dabing/5bc3ec376969c > /tmp/test/CCcam
chmod 644 /tmp/test/CCcam
cd /tmp/test
sed -n '75,75p' CCcam > CCcam1
sed 's/\(["]\+\)/\n\1/g' CCcam1 > CCcam2
sed -n '2,2p' CCcam2 > CCcam3
tr -d '["]' < "CCcam3" > CCcam4
tr -d '[\]' < "CCcam4" > /tmp/film/film23
cd /
rm -rf /tmp/test
####################################################################################################
[ -d /tmp/test ] || mkdir -p /tmp/test

curl -k -A -k   https://prehraj.to/thor-3-ragnarok/5e7fd228b2eb9 > /tmp/test/CCcam
chmod 644 /tmp/test/CCcam
cd /tmp/test
sed -n '75,75p' CCcam > CCcam1
sed 's/\(["]\+\)/\n\1/g' CCcam1 > CCcam2
sed -n '2,2p' CCcam2 > CCcam3
tr -d '["]' < "CCcam3" > CCcam4
tr -d '[\]' < "CCcam4" > /tmp/film/film24
cd /
rm -rf /tmp/test
####################################################################################################
[ -d /tmp/test ] || mkdir -p /tmp/test

curl -k -A -k   https://prehraj.to/capitan-marvel-cz-dabing-2019/5d0fbd312c0ae > /tmp/test/CCcam
chmod 644 /tmp/test/CCcam
cd /tmp/test
sed -n '75,75p' CCcam > CCcam1
sed 's/\(["]\+\)/\n\1/g' CCcam1 > CCcam2
sed -n '2,2p' CCcam2 > CCcam3
tr -d '["]' < "CCcam3" > CCcam4
tr -d '[\]' < "CCcam4" > /tmp/film/film25
cd /
rm -rf /tmp/test
####################################################################################################
[ -d /tmp/test ] || mkdir -p /tmp/test

curl -k -A -k   https://prehraj.to/marvel-universe-18-black-panther-2018-brrip-cz-dabing-by-pretorian/5e52d99159aab > /tmp/test/CCcam
chmod 644 /tmp/test/CCcam
cd /tmp/test
sed -n '75,75p' CCcam > CCcam1
sed 's/\(["]\+\)/\n\1/g' CCcam1 > CCcam2
sed -n '2,2p' CCcam2 > CCcam3
tr -d '["]' < "CCcam3" > CCcam4
tr -d '[\]' < "CCcam4" > /tmp/film/film26
cd /
rm -rf /tmp/test
####################################################################################################
[ -d /tmp/test ] || mkdir -p /tmp/test

curl -k -A -k   https://prehraj.to/strazci-galaxie-1-cz-dabing/5c89b6d686395 > /tmp/test/CCcam
chmod 644 /tmp/test/CCcam
cd /tmp/test
sed -n '75,75p' CCcam > CCcam1
sed 's/\(["]\+\)/\n\1/g' CCcam1 > CCcam2
sed -n '2,2p' CCcam2 > CCcam3
tr -d '["]' < "CCcam3" > CCcam4
tr -d '[\]' < "CCcam4" > /tmp/film/film27
cd /
rm -rf /tmp/test
####################################################################################################
[ -d /tmp/test ] || mkdir -p /tmp/test

curl -k -A -k   https://prehraj.to/strazci-galaxie-2-2017-hd-cz-dabing-cz-forced-titulky/5ee30de35c26e > /tmp/test/CCcam
chmod 644 /tmp/test/CCcam
cd /tmp/test
sed -n '75,75p' CCcam > CCcam1
sed 's/\(["]\+\)/\n\1/g' CCcam1 > CCcam2
sed -n '2,2p' CCcam2 > CCcam3
tr -d '["]' < "CCcam3" > CCcam4
tr -d '[\]' < "CCcam4" > /tmp/film/film28
cd /
rm -rf /tmp/test
####################################################################################################
[ -d /tmp/test ] || mkdir -p /tmp/test

curl -k -A -k   https://prehraj.to/hulk-cz-dabing/591036ed592d7 > /tmp/test/CCcam
chmod 644 /tmp/test/CCcam
cd /tmp/test
sed -n '75,75p' CCcam > CCcam1
sed 's/\(["]\+\)/\n\1/g' CCcam1 > CCcam2
sed -n '2,2p' CCcam2 > CCcam3
tr -d '["]' < "CCcam3" > CCcam4
tr -d '[\]' < "CCcam4" > /tmp/film/film29
cd /
rm -rf /tmp/test
####################################################################################################
[ -d /tmp/test ] || mkdir -p /tmp/test

curl -k -A -k   https://prehraj.to/hulk-2-neuveritelny-hulk-cz-dabing-2008/560627d77fecd / > /tmp/test/CCcam
chmod 644 /tmp/test/CCcam
cd /tmp/test
sed -n '75,75p' CCcam > CCcam1
sed 's/\(["]\+\)/\n\1/g' CCcam1 > CCcam2
sed -n '2,2p' CCcam2 > CCcam3
tr -d '["]' < "CCcam3" > CCcam4
tr -d '[\]' < "CCcam4" > /tmp/film/film30
cd /
rm -rf /tmp/test
####################################################################################################
[ -d /tmp/test ] || mkdir -p /tmp/test

curl -k -A -k   https://prehraj.to/hulk-2003/5bc24ed65ed04 > /tmp/test/CCcam
chmod 644 /tmp/test/CCcam
cd /tmp/test
sed -n '75,75p' CCcam > CCcam1
sed 's/\(["]\+\)/\n\1/g' CCcam1 > CCcam2
sed -n '2,2p' CCcam2 > CCcam3
tr -d '["]' < "CCcam3" > CCcam4
tr -d '[\]' < "CCcam4" > /tmp/film/film31
cd /
rm -rf /tmp/test
####################################################################################################
[ -d /tmp/test ] || mkdir -p /tmp/test

curl -k -A -k   https://prehraj.to/sebevrazedny-oddil-2016-cz/5a6c5fff5e4cf > /tmp/test/CCcam
chmod 644 /tmp/test/CCcam
cd /tmp/test
sed -n '75,75p' CCcam > CCcam1
sed 's/\(["]\+\)/\n\1/g' CCcam1 > CCcam2
sed -n '2,2p' CCcam2 > CCcam3
tr -d '["]' < "CCcam3" > CCcam4
tr -d '[\]' < "CCcam4" > /tmp/film/film32
cd /
rm -rf /tmp/test
####################################################################################################
[ -d /tmp/test ] || mkdir -p /tmp/test

curl -k -A -k   https://prehraj.to/daredevil-2003-cz-dabing/5c05d6d6af22d > /tmp/test/CCcam
chmod 644 /tmp/test/CCcam
cd /tmp/test
sed -n '75,75p' CCcam > CCcam1
sed 's/\(["]\+\)/\n\1/g' CCcam1 > CCcam2
sed -n '2,2p' CCcam2 > CCcam3
tr -d '["]' < "CCcam3" > CCcam4
tr -d '[\]' < "CCcam4" > /tmp/film/film33
cd /
rm -rf /tmp/test
####################################################################################################
[ -d /tmp/test ] || mkdir -p /tmp/test

curl -k -A -k   https://prehraj.to/elektra-cz-dabing-akcni-dobrodruzny-usa-2005/56f6c9166fbe1 > /tmp/test/CCcam
chmod 644 /tmp/test/CCcam
cd /tmp/test
sed -n '75,75p' CCcam > CCcam1
sed 's/\(["]\+\)/\n\1/g' CCcam1 > CCcam2
sed -n '2,2p' CCcam2 > CCcam3
tr -d '["]' < "CCcam3" > CCcam4
tr -d '[\]' < "CCcam4" > /tmp/film/film34
cd /
rm -rf /tmp/test
####################################################################################################
[ -d /tmp/test ] || mkdir -p /tmp/test

curl -k -A -k   https://prehraj.to/ghost-rider-1-cage-2007-cz-dabing/5c51d37b8245c > /tmp/test/CCcam
chmod 644 /tmp/test/CCcam
cd /tmp/test
sed -n '75,75p' CCcam > CCcam1
sed 's/\(["]\+\)/\n\1/g' CCcam1 > CCcam2
sed -n '2,2p' CCcam2 > CCcam3
tr -d '["]' < "CCcam3" > CCcam4
tr -d '[\]' < "CCcam4" > /tmp/film/film35
cd /
rm -rf /tmp/test
####################################################################################################
[ -d /tmp/test ] || mkdir -p /tmp/test

curl -k -A -k   https://prehraj.to/ghost-rider-2/5c8954eb523b9 > /tmp/test/CCcam
chmod 644 /tmp/test/CCcam
cd /tmp/test
sed -n '75,75p' CCcam > CCcam1
sed 's/\(["]\+\)/\n\1/g' CCcam1 > CCcam2
sed -n '2,2p' CCcam2 > CCcam3
tr -d '["]' < "CCcam3" > CCcam4
tr -d '[\]' < "CCcam4" > /tmp/film/film36
cd /
rm -rf /tmp/test
####################################################################################################
[ -d /tmp/test ] || mkdir -p /tmp/test

curl -k -A -k   https://prehraj.to/soudce-dredd-2012/5aa9c9a329a5a > /tmp/test/CCcam
chmod 644 /tmp/test/CCcam
cd /tmp/test
sed -n '75,75p' CCcam > CCcam1
sed 's/\(["]\+\)/\n\1/g' CCcam1 > CCcam2
sed -n '2,2p' CCcam2 > CCcam3
tr -d '["]' < "CCcam3" > CCcam4
tr -d '[\]' < "CCcam4" > /tmp/film/film37
cd /
rm -rf /tmp/test
####################################################################################################
[ -d /tmp/test ] || mkdir -p /tmp/test

curl -k -A -k   https://prehraj.to/dredd-2012-cz/589ca025a5fd5 > /tmp/test/CCcam
chmod 644 /tmp/test/CCcam
cd /tmp/test
sed -n '75,75p' CCcam > CCcam1
sed 's/\(["]\+\)/\n\1/g' CCcam1 > CCcam2
sed -n '2,2p' CCcam2 > CCcam3
tr -d '["]' < "CCcam3" > CCcam4
tr -d '[\]' < "CCcam4" > /tmp/film/film38
cd /
rm -rf /tmp/test
####################################################################################################
[ -d /tmp/test ] || mkdir -p /tmp/test

curl -k -A -k   https://prehraj.to/deadpool-2016-cz/5f5b51b60d4cc > /tmp/test/CCcam
chmod 644 /tmp/test/CCcam
cd /tmp/test
sed -n '75,75p' CCcam > CCcam1
sed 's/\(["]\+\)/\n\1/g' CCcam1 > CCcam2
sed -n '2,2p' CCcam2 > CCcam3
tr -d '["]' < "CCcam3" > CCcam4
tr -d '[\]' < "CCcam4" > /tmp/film/film39
cd /
rm -rf /tmp/test
####################################################################################################
[ -d /tmp/test ] || mkdir -p /tmp/test

curl -k -A -k   https://prehraj.to/deadpool-2-2018-cz/5f59133109b0e > /tmp/test/CCcam
chmod 644 /tmp/test/CCcam
cd /tmp/test
sed -n '75,75p' CCcam > CCcam1
sed 's/\(["]\+\)/\n\1/g' CCcam1 > CCcam2
sed -n '2,2p' CCcam2 > CCcam3
tr -d '["]' < "CCcam3" > CCcam4
tr -d '[\]' < "CCcam4" > /tmp/film/film40
cd /
rm -rf /tmp/test
####################################################################################################
[ -d /tmp/test ] || mkdir -p /tmp/test

curl -k -A -k   https://prehraj.to/captain-america-prvni-avenger-nejlepsi-kvalita-cz/5ab229669b2b3 > /tmp/test/CCcam
chmod 644 /tmp/test/CCcam
cd /tmp/test
sed -n '75,75p' CCcam > CCcam1
sed 's/\(["]\+\)/\n\1/g' CCcam1 > CCcam2
sed -n '2,2p' CCcam2 > CCcam3
tr -d '["]' < "CCcam3" > CCcam4
tr -d '[\]' < "CCcam4" > /tmp/film/film41
cd /
rm -rf /tmp/test
####################################################################################################
[ -d /tmp/test ] || mkdir -p /tmp/test

curl -k -A -k   https://prehraj.to/capitan-america-navrat-prveho-avengera-cz-dabing/59d5b8108caca > /tmp/test/CCcam
chmod 644 /tmp/test/CCcam
cd /tmp/test
sed -n '75,75p' CCcam > CCcam1
sed 's/\(["]\+\)/\n\1/g' CCcam1 > CCcam2
sed -n '2,2p' CCcam2 > CCcam3
tr -d '["]' < "CCcam3" > CCcam4
tr -d '[\]' < "CCcam4" > /tmp/film/film42
cd /
rm -rf /tmp/test
####################################################################################################
[ -d /tmp/test ] || mkdir -p /tmp/test

curl -k -A -k   https://prehraj.to/capitan-america-obcanska-valka-cz-dabing-2016/5a005d8206690 > /tmp/test/CCcam
chmod 644 /tmp/test/CCcam
cd /tmp/test
sed -n '75,75p' CCcam > CCcam1
sed 's/\(["]\+\)/\n\1/g' CCcam1 > CCcam2
sed -n '2,2p' CCcam2 > CCcam3
tr -d '["]' < "CCcam3" > CCcam4
tr -d '[\]' < "CCcam4" > /tmp/film/film43
cd /
rm -rf /tmp/test
####################################################################################################
[ -d /tmp/test ] || mkdir -p /tmp/test

curl -k -A -k   https://prehraj.to/venom-2018-cz/5f5b0a90c01ba > /tmp/test/CCcam
chmod 644 /tmp/test/CCcam
cd /tmp/test
sed -n '75,75p' CCcam > CCcam1
sed 's/\(["]\+\)/\n\1/g' CCcam1 > CCcam2
sed -n '2,2p' CCcam2 > CCcam3
tr -d '["]' < "CCcam3" > CCcam4
tr -d '[\]' < "CCcam4" > /tmp/film/film44
cd /
rm -rf /tmp/test
####################################################################################################
[ -d /tmp/test ] || mkdir -p /tmp/test

curl -k -A -k   https://prehraj.to/robocop-cz-dabing-2014/5d6e4a56efbdf > /tmp/test/CCcam
chmod 644 /tmp/test/CCcam
cd /tmp/test
sed -n '75,75p' CCcam > CCcam1
sed 's/\(["]\+\)/\n\1/g' CCcam1 > CCcam2
sed -n '2,2p' CCcam2 > CCcam3
tr -d '["]' < "CCcam3" > CCcam4
tr -d '[\]' < "CCcam4" > /tmp/film/film45
cd /
rm -rf /tmp/test
####################################################################################################
[ -d /tmp/test ] || mkdir -p /tmp/test

curl -k -A -k   https://prehraj.to/robocop-1-cz-dabing-1987/57d40ddebfe4f > /tmp/test/CCcam
chmod 644 /tmp/test/CCcam
cd /tmp/test
sed -n '75,75p' CCcam > CCcam1
sed 's/\(["]\+\)/\n\1/g' CCcam1 > CCcam2
sed -n '2,2p' CCcam2 > CCcam3
tr -d '["]' < "CCcam3" > CCcam4
tr -d '[\]' < "CCcam4" > /tmp/film/film46
cd /
rm -rf /tmp/test
####################################################################################################
[ -d /tmp/test ] || mkdir -p /tmp/test

curl -k -A -k   https://prehraj.to/robocop-2-cz-dabing-1990/5b8ab20b2a4f4 > /tmp/test/CCcam
chmod 644 /tmp/test/CCcam
cd /tmp/test
sed -n '75,75p' CCcam > CCcam1
sed 's/\(["]\+\)/\n\1/g' CCcam1 > CCcam2
sed -n '2,2p' CCcam2 > CCcam3
tr -d '["]' < "CCcam3" > CCcam4
tr -d '[\]' < "CCcam4" > /tmp/film/film47
cd /
rm -rf /tmp/test
####################################################################################################
[ -d /tmp/test ] || mkdir -p /tmp/test

curl -k -A -k   https://prehraj.to/robocop-3-cz-dabing-1993/5a49d539e3a28 > /tmp/test/CCcam
chmod 644 /tmp/test/CCcam
cd /tmp/test
sed -n '75,75p' CCcam > CCcam1
sed 's/\(["]\+\)/\n\1/g' CCcam1 > CCcam2
sed -n '2,2p' CCcam2 > CCcam3
tr -d '["]' < "CCcam3" > CCcam4
tr -d '[\]' < "CCcam4" > /tmp/film/film48
cd /
rm -rf /tmp/test
####################################################################################################
[ -d /tmp/test ] || mkdir -p /tmp/test

curl -k -A -k   https://prehraj.to/robocop-4-cz-dabing-2000/5de6ef3149974 > /tmp/test/CCcam
chmod 644 /tmp/test/CCcam
cd /tmp/test
sed -n '75,75p' CCcam > CCcam1
sed 's/\(["]\+\)/\n\1/g' CCcam1 > CCcam2
sed -n '2,2p' CCcam2 > CCcam3
tr -d '["]' < "CCcam3" > CCcam4
tr -d '[\]' < "CCcam4" > /tmp/film/film49
cd /
rm -rf /tmp/test
####################################################################################################
[ -d /tmp/test ] || mkdir -p /tmp/test

curl -k -A -k   https://prehraj.to/terminator-1/590e3dff07c98 > /tmp/test/CCcam
chmod 644 /tmp/test/CCcam
cd /tmp/test
sed -n '75,75p' CCcam > CCcam1
sed 's/\(["]\+\)/\n\1/g' CCcam1 > CCcam2
sed -n '2,2p' CCcam2 > CCcam3
tr -d '["]' < "CCcam3" > CCcam4
tr -d '[\]' < "CCcam4" > /tmp/film/film50
cd /
rm -rf /tmp/test
####################################################################################################
[ -d /tmp/test ] || mkdir -p /tmp/test

curl -k -A -k   https://prehraj.to/terminator-2-den-zuctovani-1991-hdrip-cz-dabing-m3/5d56b5bd0d032 > /tmp/test/CCcam
chmod 644 /tmp/test/CCcam
cd /tmp/test
sed -n '75,75p' CCcam > CCcam1
sed 's/\(["]\+\)/\n\1/g' CCcam1 > CCcam2
sed -n '2,2p' CCcam2 > CCcam3
tr -d '["]' < "CCcam3" > CCcam4
tr -d '[\]' < "CCcam4" > /tmp/film/film51
cd /
rm -rf /tmp/test
####################################################################################################
[ -d /tmp/test ] || mkdir -p /tmp/test

curl -k -A -k   https://prehraj.to/vzpoura-stroju-1986-cz/5ce11979ae27a > /tmp/test/CCcam
chmod 644 /tmp/test/CCcam
cd /tmp/test
sed -n '75,75p' CCcam > CCcam1
sed 's/\(["]\+\)/\n\1/g' CCcam1 > CCcam2
sed -n '2,2p' CCcam2 > CCcam3
tr -d '["]' < "CCcam3" > CCcam4
tr -d '[\]' < "CCcam4" > /tmp/film/film52
cd /
rm -rf /tmp/test
####################################################################################################
[ -d /tmp/test ] || mkdir -p /tmp/test

curl -k -A -k   https://prehraj.to/navrat-do-budoucnosti-1-hd-720p-cz-bandy/5962b3f383429 > /tmp/test/CCcam
chmod 644 /tmp/test/CCcam
cd /tmp/test
sed -n '75,75p' CCcam > CCcam1
sed 's/\(["]\+\)/\n\1/g' CCcam1 > CCcam2
sed -n '2,2p' CCcam2 > CCcam3
tr -d '["]' < "CCcam3" > CCcam4
tr -d '[\]' < "CCcam4" > /tmp/film/film53
cd /
rm -rf /tmp/test
####################################################################################################
[ -d /tmp/test ] || mkdir -p /tmp/test

curl -k -A -k   https://prehraj.to/navrat-do-budoucnosti-2-cz-dabing-1989-by-kamer/5828aa1eeccd /1 > /tmp/test/CCcam
chmod 644 /tmp/test/CCcam
cd /tmp/test
sed -n '75,75p' CCcam > CCcam1
sed 's/\(["]\+\)/\n\1/g' CCcam1 > CCcam2
sed -n '2,2p' CCcam2 > CCcam3
tr -d '["]' < "CCcam3" > CCcam4
tr -d '[\]' < "CCcam4" > /tmp/film/film54
cd /
rm -rf /tmp/test
####################################################################################################
[ -d /tmp/test ] || mkdir -p /tmp/test

curl -k -A -k   https://prehraj.to/navrat-do-budoucnosti-3-cz-dabing-1990/57c2b4009264c > /tmp/test/CCcam
chmod 644 /tmp/test/CCcam
cd /tmp/test
sed -n '75,75p' CCcam > CCcam1
sed 's/\(["]\+\)/\n\1/g' CCcam1 > CCcam2
sed -n '2,2p' CCcam2 > CCcam3
tr -d '["]' < "CCcam3" > CCcam4
tr -d '[\]' < "CCcam4" > /tmp/film/film55
cd /
rm -rf /tmp/test
####################################################################################################
[ -d /tmp/test ] || mkdir -p /tmp/test

curl -k -A -k   https://prehraj.to/blizka-setkani-tretiho-druhu-1977-cz-avi/5dd5c4ba8e08a > /tmp/test/CCcam
chmod 644 /tmp/test/CCcam
cd /tmp/test
sed -n '75,75p' CCcam > CCcam1
sed 's/\(["]\+\)/\n\1/g' CCcam1 > CCcam2
sed -n '2,2p' CCcam2 > CCcam3
tr -d '["]' < "CCcam3" > CCcam4
tr -d '[\]' < "CCcam4" > /tmp/film/film56
cd /
rm -rf /tmp/test
####################################################################################################
[ -d /tmp/test ] || mkdir -p /tmp/test

curl -k -A -k   https://prehraj.to/vladci-vesmiru-cz-by-liqos/57c01181b879d > /tmp/test/CCcam
chmod 644 /tmp/test/CCcam
cd /tmp/test
sed -n '75,75p' CCcam > CCcam1
sed 's/\(["]\+\)/\n\1/g' CCcam1 > CCcam2
sed -n '2,2p' CCcam2 > CCcam3
tr -d '["]' < "CCcam3" > CCcam4
tr -d '[\]' < "CCcam4" > /tmp/film/film57
cd /
rm -rf /tmp/test
####################################################################################################
[ -d /tmp/test ] || mkdir -p /tmp/test

curl -k -A -k   https://prehraj.to/temny-andel-1990/5ab6d8b263252 > /tmp/test/CCcam
chmod 644 /tmp/test/CCcam
cd /tmp/test
sed -n '75,75p' CCcam > CCcam1
sed 's/\(["]\+\)/\n\1/g' CCcam1 > CCcam2
sed -n '2,2p' CCcam2 > CCcam3
tr -d '["]' < "CCcam3" > CCcam4
tr -d '[\]' < "CCcam4" > /tmp/film/film58
cd /
rm -rf /tmp/test
####################################################################################################
[ -d /tmp/test ] || mkdir -p /tmp/test

curl -k -A -k   https://prehraj.to/predator-1-cz/5a9f68ec46fb5 > /tmp/test/CCcam
chmod 644 /tmp/test/CCcam
cd /tmp/test
sed -n '75,75p' CCcam > CCcam1
sed 's/\(["]\+\)/\n\1/g' CCcam1 > CCcam2
sed -n '2,2p' CCcam2 > CCcam3
tr -d '["]' < "CCcam3" > CCcam4
tr -d '[\]' < "CCcam4" > /tmp/film/film59
cd /
rm -rf /tmp/test
####################################################################################################
[ -d /tmp/test ] || mkdir -p /tmp/test

curl -k -A -k   https://prehraj.to/predator-2-cz-720p-xvid-ac3-5-1-bandy/58d406facfa2d > /tmp/test/CCcam
chmod 644 /tmp/test/CCcam
cd /tmp/test
sed -n '75,75p' CCcam > CCcam1
sed 's/\(["]\+\)/\n\1/g' CCcam1 > CCcam2
sed -n '2,2p' CCcam2 > CCcam3
tr -d '["]' < "CCcam3" > CCcam4
tr -d '[\]' < "CCcam4" > /tmp/film/film60
cd /
rm -rf /tmp/test
####################################################################################################
[ -d /tmp/test ] || mkdir -p /tmp/test

curl -k -A -k   https://prehraj.to/predator-evoluce-cz-dabing-4k-kvalita/5c4fb28950e89 > /tmp/test/CCcam
chmod 644 /tmp/test/CCcam
cd /tmp/test
sed -n '75,75p' CCcam > CCcam1
sed 's/\(["]\+\)/\n\1/g' CCcam1 > CCcam2
sed -n '2,2p' CCcam2 > CCcam3
tr -d '["]' < "CCcam3" > CCcam4
tr -d '[\]' < "CCcam4" > /tmp/film/film61
cd /
rm -rf /tmp/test
####################################################################################################
[ -d /tmp/test ] || mkdir -p /tmp/test

curl -k -A -k   https://prehraj.to/alien-vs-predator-1-cz-dabing-2004/5820f7c7a9fce > /tmp/test/CCcam
chmod 644 /tmp/test/CCcam
cd /tmp/test
sed -n '75,75p' CCcam > CCcam1
sed 's/\(["]\+\)/\n\1/g' CCcam1 > CCcam2
sed -n '2,2p' CCcam2 > CCcam3
tr -d '["]' < "CCcam3" > CCcam4
tr -d '[\]' < "CCcam4" > /tmp/film/film62
cd /
rm -rf /tmp/test
####################################################################################################
[ -d /tmp/test ] || mkdir -p /tmp/test

curl -k -A -k   https://prehraj.to/alien-vs-predator-2-cz/572c6844075a5 > /tmp/test/CCcam
chmod 644 /tmp/test/CCcam
cd /tmp/test
sed -n '75,75p' CCcam > CCcam1
sed 's/\(["]\+\)/\n\1/g' CCcam1 > CCcam2
sed -n '2,2p' CCcam2 > CCcam3
tr -d '["]' < "CCcam3" > CCcam4
tr -d '[\]' < "CCcam4" > /tmp/film/film63
cd /
rm -rf /tmp/test
####################################################################################################
[ -d /tmp/test ] || mkdir -p /tmp/test

curl -k -A -k   https://prehraj.to/predatori-2010-1080p-cz/5a65ac07ddaca > /tmp/test/CCcam
chmod 644 /tmp/test/CCcam
cd /tmp/test
sed -n '75,75p' CCcam > CCcam1
sed 's/\(["]\+\)/\n\1/g' CCcam1 > CCcam2
sed -n '2,2p' CCcam2 > CCcam3
tr -d '["]' < "CCcam3" > CCcam4
tr -d '[\]' < "CCcam4" > /tmp/film/film64
cd /
rm -rf /tmp/test
####################################################################################################
[ -d /tmp/test ] || mkdir -p /tmp/test

curl -k -A -k   https://prehraj.to/vetrelec-1-1979-hdrip-cz-dabing-m3/5c8fa9274c149 > /tmp/test/CCcam
chmod 644 /tmp/test/CCcam
cd /tmp/test
sed -n '75,75p' CCcam > CCcam1
sed 's/\(["]\+\)/\n\1/g' CCcam1 > CCcam2
sed -n '2,2p' CCcam2 > CCcam3
tr -d '["]' < "CCcam3" > CCcam4
tr -d '[\]' < "CCcam4" > /tmp/film/film65
cd /
rm -rf /tmp/test
####################################################################################################
[ -d /tmp/test ] || mkdir -p /tmp/test

curl -k -A -k   https://prehraj.to/vetrelec-2/5b788f3b275c0 > /tmp/test/CCcam
chmod 644 /tmp/test/CCcam
cd /tmp/test
sed -n '75,75p' CCcam > CCcam1
sed 's/\(["]\+\)/\n\1/g' CCcam1 > CCcam2
sed -n '2,2p' CCcam2 > CCcam3
tr -d '["]' < "CCcam3" > CCcam4
tr -d '[\]' < "CCcam4" > /tmp/film/film66
cd /
rm -rf /tmp/test
####################################################################################################
[ -d /tmp/test ] || mkdir -p /tmp/test

curl -k -A -k   https://prehraj.to/vetrelec-3/5b7895b6e1b1f > /tmp/test/CCcam
chmod 644 /tmp/test/CCcam
cd /tmp/test
sed -n '75,75p' CCcam > CCcam1
sed 's/\(["]\+\)/\n\1/g' CCcam1 > CCcam2
sed -n '2,2p' CCcam2 > CCcam3
tr -d '["]' < "CCcam3" > CCcam4
tr -d '[\]' < "CCcam4" > /tmp/film/film67
cd /
rm -rf /tmp/test
####################################################################################################
[ -d /tmp/test ] || mkdir -p /tmp/test

curl -k -A -k   https://prehraj.to/vetrelec-4-cz-by-liqos/57c00e610ac3f > /tmp/test/CCcam
chmod 644 /tmp/test/CCcam
cd /tmp/test
sed -n '75,75p' CCcam > CCcam1
sed 's/\(["]\+\)/\n\1/g' CCcam1 > CCcam2
sed -n '2,2p' CCcam2 > CCcam3
tr -d '["]' < "CCcam3" > CCcam4
tr -d '[\]' < "CCcam4" > /tmp/film/film68
cd /
rm -rf /tmp/test
####################################################################################################
[ -d /tmp/test ] || mkdir -p /tmp/test

curl -k -A -k   https://prehraj.to/vetrelec-covenant-cz-dabing-2017-hd-prometheus-2/5c03223dcb98e > /tmp/test/CCcam
chmod 644 /tmp/test/CCcam
cd /tmp/test
sed -n '75,75p' CCcam > CCcam1
sed 's/\(["]\+\)/\n\1/g' CCcam1 > CCcam2
sed -n '2,2p' CCcam2 > CCcam3
tr -d '["]' < "CCcam3" > CCcam4
tr -d '[\]' < "CCcam4" > /tmp/film/film69
cd /
rm -rf /tmp/test
####################################################################################################
[ -d /tmp/test ] || mkdir -p /tmp/test

curl -k -A -k   https://prehraj.to/to-cz-dabing-1990-horor-it/5bddbbe8639c6 > /tmp/test/CCcam
chmod 644 /tmp/test/CCcam
cd /tmp/test
sed -n '75,75p' CCcam > CCcam1
sed 's/\(["]\+\)/\n\1/g' CCcam1 > CCcam2
sed -n '2,2p' CCcam2 > CCcam3
tr -d '["]' < "CCcam3" > CCcam4
tr -d '[\]' < "CCcam4" > /tmp/film/film70
cd /
rm -rf /tmp/test
####################################################################################################
[ -d /tmp/test ] || mkdir -p /tmp/test

curl -k -A -k   https://prehraj.to/to-it-2017-hdrip-cz-dabing-m3/5c4c7460dfa40 > /tmp/test/CCcam
chmod 644 /tmp/test/CCcam
cd /tmp/test
sed -n '75,75p' CCcam > CCcam1
sed 's/\(["]\+\)/\n\1/g' CCcam1 > CCcam2
sed -n '2,2p' CCcam2 > CCcam3
tr -d '["]' < "CCcam3" > CCcam4
tr -d '[\]' < "CCcam4" > /tmp/film/film71
cd /
rm -rf /tmp/test
####################################################################################################
[ -d /tmp/test ] || mkdir -p /tmp/test

curl -k -A -k   https://prehraj.to/to-kapitola-2-cz-dabing/5e171ecaa1e6e > /tmp/test/CCcam
chmod 644 /tmp/test/CCcam
cd /tmp/test
sed -n '75,75p' CCcam > CCcam1
sed 's/\(["]\+\)/\n\1/g' CCcam1 > CCcam2
sed -n '2,2p' CCcam2 > CCcam3
tr -d '["]' < "CCcam3" > CCcam4
tr -d '[\]' < "CCcam4" > /tmp/film/film72
cd /
rm -rf /tmp/test
####################################################################################################
[ -d /tmp/test ] || mkdir -p /tmp/test

curl -k -A -k   https://prehraj.to/smrtelne-zlo-2-1987-czdabing/57ebc338344d8 > /tmp/test/CCcam
chmod 644 /tmp/test/CCcam
cd /tmp/test
sed -n '75,75p' CCcam > CCcam1
sed 's/\(["]\+\)/\n\1/g' CCcam1 > CCcam2
sed -n '2,2p' CCcam2 > CCcam3
tr -d '["]' < "CCcam3" > CCcam4
tr -d '[\]' < "CCcam4" > /tmp/film/film73
cd /
rm -rf /tmp/test
####################################################################################################
[ -d /tmp/test ] || mkdir -p /tmp/test

curl -k -A -k   https://prehraj.to/navrat-ozivlich-mrtvol-2-1987/5d04c34a7087a > /tmp/test/CCcam
chmod 644 /tmp/test/CCcam
cd /tmp/test
sed -n '75,75p' CCcam > CCcam1
sed 's/\(["]\+\)/\n\1/g' CCcam1 > CCcam2
sed -n '2,2p' CCcam2 > CCcam3
tr -d '["]' < "CCcam3" > CCcam4
tr -d '[\]' < "CCcam4" > /tmp/film/film74
cd /
rm -rf /tmp/test
####################################################################################################
[ -d /tmp/test ] || mkdir -p /tmp/test

curl -k -A -k   https://prehraj.to/navrat-ozivlich-mrtvol-3-1993/5d77b587676a3 > /tmp/test/CCcam
chmod 644 /tmp/test/CCcam
cd /tmp/test
sed -n '75,75p' CCcam > CCcam1
sed 's/\(["]\+\)/\n\1/g' CCcam1 > CCcam2
sed -n '2,2p' CCcam2 > CCcam3
tr -d '["]' < "CCcam3" > CCcam4
tr -d '[\]' < "CCcam4" > /tmp/film/film75
cd /
rm -rf /tmp/test
####################################################################################################
[ -d /tmp/test ] || mkdir -p /tmp/test

curl -k -A -k   https://prehraj.to/usvit-mrtvych-dawn-of-the-dead-2004-cz-dabing/5913229bdf252 > /tmp/test/CCcam
chmod 644 /tmp/test/CCcam
cd /tmp/test
sed -n '75,75p' CCcam > CCcam1
sed 's/\(["]\+\)/\n\1/g' CCcam1 > CCcam2
sed -n '2,2p' CCcam2 > CCcam3
tr -d '["]' < "CCcam3" > CCcam4
tr -d '[\]' < "CCcam4" > /tmp/film/film76
cd /
rm -rf /tmp/test
####################################################################################################
[ -d /tmp/test ] || mkdir -p /tmp/test

curl -k -A -k   https://prehraj.to/soumrak-mrtvych-pegg-2004-cz-dabing/5dcc30905f0e6 > /tmp/test/CCcam
chmod 644 /tmp/test/CCcam
cd /tmp/test
sed -n '75,75p' CCcam > CCcam1
sed 's/\(["]\+\)/\n\1/g' CCcam1 > CCcam2
sed -n '2,2p' CCcam2 > CCcam3
tr -d '["]' < "CCcam3" > CCcam4
tr -d '[\]' < "CCcam4" > /tmp/film/film77
cd /
rm -rf /tmp/test
####################################################################################################
[ -d /tmp/test ] || mkdir -p /tmp/test

curl -k -A -k   https://prehraj.to/zombieland-2009-1080p-brrip-x264-ac3-cz/589a65d15bab4 > /tmp/test/CCcam
chmod 644 /tmp/test/CCcam
cd /tmp/test
sed -n '75,75p' CCcam > CCcam1
sed 's/\(["]\+\)/\n\1/g' CCcam1 > CCcam2
sed -n '2,2p' CCcam2 > CCcam3
tr -d '["]' < "CCcam3" > CCcam4
tr -d '[\]' < "CCcam4" > /tmp/film/film78
cd /
rm -rf /tmp/test
####################################################################################################
[ -d /tmp/test ] || mkdir -p /tmp/test

curl -k -A -k   https://prehraj.to/zombieland-2-cz-dabing/5e7a35721036f > /tmp/test/CCcam
chmod 644 /tmp/test/CCcam
cd /tmp/test
sed -n '75,75p' CCcam > CCcam1
sed 's/\(["]\+\)/\n\1/g' CCcam1 > CCcam2
sed -n '2,2p' CCcam2 > CCcam3
tr -d '["]' < "CCcam3" > CCcam4
tr -d '[\]' < "CCcam4" > /tmp/film/film79
cd /
rm -rf /tmp/test
####################################################################################################
[ -d /tmp/test ] || mkdir -p /tmp/test

curl -k -A -k   https://prehraj.to/zeme-mrtvych-cz-dabing-nejlepsi-kvalita/5ae5be390cd /db > /tmp/test/CCcam
chmod 644 /tmp/test/CCcam
cd /tmp/test
sed -n '75,75p' CCcam > CCcam1
sed 's/\(["]\+\)/\n\1/g' CCcam1 > CCcam2
sed -n '2,2p' CCcam2 > CCcam3
tr -d '["]' < "CCcam3" > CCcam4
tr -d '[\]' < "CCcam4" > /tmp/film/film80
cd /
rm -rf /tmp/test
####################################################################################################
[ -d /tmp/test ] || mkdir -p /tmp/test

curl -k -A -k   https://prehraj.to/smrtonosna-zbran-1-1987-cz/57e162361fa15 > /tmp/test/CCcam
chmod 644 /tmp/test/CCcam
cd /tmp/test
sed -n '75,75p' CCcam > CCcam1
sed 's/\(["]\+\)/\n\1/g' CCcam1 > CCcam2
sed -n '2,2p' CCcam2 > CCcam3
tr -d '["]' < "CCcam3" > CCcam4
tr -d '[\]' < "CCcam4" > /tmp/film/film81
cd /
rm -rf /tmp/test
####################################################################################################
[ -d /tmp/test ] || mkdir -p /tmp/test

curl -k -A -k   https://prehraj.to/smrtonosna-zbran-2-lethal-weapon-2-1989-dvdrip-cz/5a12dbd0cc8f4 > /tmp/test/CCcam
chmod 644 /tmp/test/CCcam
cd /tmp/test
sed -n '75,75p' CCcam > CCcam1
sed 's/\(["]\+\)/\n\1/g' CCcam1 > CCcam2
sed -n '2,2p' CCcam2 > CCcam3
tr -d '["]' < "CCcam3" > CCcam4
tr -d '[\]' < "CCcam4" > /tmp/film/film82
cd /
rm -rf /tmp/test
####################################################################################################
[ -d /tmp/test ] || mkdir -p /tmp/test

curl -k -A -k   https://prehraj.to/smrtonosna-zbran-3-gibson-1992-cz-dabing/5c4da2d17170a > /tmp/test/CCcam
chmod 644 /tmp/test/CCcam
cd /tmp/test
sed -n '75,75p' CCcam > CCcam1
sed 's/\(["]\+\)/\n\1/g' CCcam1 > CCcam2
sed -n '2,2p' CCcam2 > CCcam3
tr -d '["]' < "CCcam3" > CCcam4
tr -d '[\]' < "CCcam4" > /tmp/film/film83
cd /
rm -rf /tmp/test
####################################################################################################
[ -d /tmp/test ] || mkdir -p /tmp/test

curl -k -A -k   https://prehraj.to/smrtonosna-zbran-4-lethal-weapon-4-cz-dabing-1998/5814845815d38 > /tmp/test/CCcam
chmod 644 /tmp/test/CCcam
cd /tmp/test
sed -n '75,75p' CCcam > CCcam1
sed 's/\(["]\+\)/\n\1/g' CCcam1 > CCcam2
sed -n '2,2p' CCcam2 > CCcam3
tr -d '["]' < "CCcam3" > CCcam4
tr -d '[\]' < "CCcam4" > /tmp/film/film84
cd /
rm -rf /tmp/test
####################################################################################################
[ -d /tmp/test ] || mkdir -p /tmp/test

curl -k -A -k   https://prehraj.to/do-utoku-over-the-top-stallone-1987-cz-dabing/5c534f38121f4 > /tmp/test/CCcam
chmod 644 /tmp/test/CCcam
cd /tmp/test
sed -n '75,75p' CCcam > CCcam1
sed 's/\(["]\+\)/\n\1/g' CCcam1 > CCcam2
sed -n '2,2p' CCcam2 > CCcam3
tr -d '["]' < "CCcam3" > CCcam4
tr -d '[\]' < "CCcam4" > /tmp/film/film85
cd /
rm -rf /tmp/test
####################################################################################################
[ -d /tmp/test ] || mkdir -p /tmp/test

curl -k -A -k   https://prehraj.to/kriminal-1989-czdab/55c7916a7178d > /tmp/test/CCcam
chmod 644 /tmp/test/CCcam
cd /tmp/test
sed -n '75,75p' CCcam > CCcam1
sed 's/\(["]\+\)/\n\1/g' CCcam1 > CCcam2
sed -n '2,2p' CCcam2 > CCcam3
tr -d '["]' < "CCcam3" > CCcam4
tr -d '[\]' < "CCcam4" > /tmp/film/film86
cd /
rm -rf /tmp/test
####################################################################################################
[ -d /tmp/test ] || mkdir -p /tmp/test

curl -k -A -k   https://prehraj.to/krvavy-sport-1988-brrip-cz-dabing/58cd /52b0318dd > /tmp/test/CCcam
chmod 644 /tmp/test/CCcam
cd /tmp/test
sed -n '75,75p' CCcam > CCcam1
sed 's/\(["]\+\)/\n\1/g' CCcam1 > CCcam2
sed -n '2,2p' CCcam2 > CCcam3
tr -d '["]' < "CCcam3" > CCcam4
tr -d '[\]' < "CCcam4" > /tmp/film/film87
cd /
rm -rf /tmp/test
####################################################################################################
[ -d /tmp/test ] || mkdir -p /tmp/test

curl -k -A -k   https://prehraj.to/kickboxer-1989/5ab66f445140b > /tmp/test/CCcam
chmod 644 /tmp/test/CCcam
cd /tmp/test
sed -n '75,75p' CCcam > CCcam1
sed 's/\(["]\+\)/\n\1/g' CCcam1 > CCcam2
sed -n '2,2p' CCcam2 > CCcam3
tr -d '["]' < "CCcam3" > CCcam4
tr -d '[\]' < "CCcam4" > /tmp/film/film88
cd /
rm -rf /tmp/test
####################################################################################################
[ -d /tmp/test ] || mkdir -p /tmp/test

curl -k -A -k   https://prehraj.to/rambo-1-1982-hd-cz/5eabe3d5e2752 > /tmp/test/CCcam
chmod 644 /tmp/test/CCcam
cd /tmp/test
sed -n '75,75p' CCcam > CCcam1
sed 's/\(["]\+\)/\n\1/g' CCcam1 > CCcam2
sed -n '2,2p' CCcam2 > CCcam3
tr -d '["]' < "CCcam3" > CCcam4
tr -d '[\]' < "CCcam4" > /tmp/film/film89
cd /
rm -rf /tmp/test
####################################################################################################
[ -d /tmp/test ] || mkdir -p /tmp/test

curl -k -A -k   https://prehraj.to/rambo-2-cz-dabing/5b98c570387ee > /tmp/test/CCcam
chmod 644 /tmp/test/CCcam
cd /tmp/test
sed -n '75,75p' CCcam > CCcam1
sed 's/\(["]\+\)/\n\1/g' CCcam1 > CCcam2
sed -n '2,2p' CCcam2 > CCcam3
tr -d '["]' < "CCcam3" > CCcam4
tr -d '[\]' < "CCcam4" > /tmp/film/film90
cd /
rm -rf /tmp/test
####################################################################################################
[ -d /tmp/test ] || mkdir -p /tmp/test

curl -k -A -k   https://prehraj.to/rambo-3-cz-dabing/5b98c5e138161 > /tmp/test/CCcam
chmod 644 /tmp/test/CCcam
cd /tmp/test
sed -n '75,75p' CCcam > CCcam1
sed 's/\(["]\+\)/\n\1/g' CCcam1 > CCcam2
sed -n '2,2p' CCcam2 > CCcam3
tr -d '["]' < "CCcam3" > CCcam4
tr -d '[\]' < "CCcam4" > /tmp/film/film91
cd /
rm -rf /tmp/test
####################################################################################################
[ -d /tmp/test ] || mkdir -p /tmp/test

curl -k -A -k   https://prehraj.to/rambo-4-2008-hd-cz/5eac113ac9018 > /tmp/test/CCcam
chmod 644 /tmp/test/CCcam
cd /tmp/test
sed -n '75,75p' CCcam > CCcam1
sed 's/\(["]\+\)/\n\1/g' CCcam1 > CCcam2
sed -n '2,2p' CCcam2 > CCcam3
tr -d '["]' < "CCcam3" > CCcam4
tr -d '[\]' < "CCcam4" > /tmp/film/film92
cd /
rm -rf /tmp/test
####################################################################################################
[ -d /tmp/test ] || mkdir -p /tmp/test

curl -k -A -k   https://prehraj.to/rambo-last-blood-2019-cz/5e77252840ecc > /tmp/test/CCcam
chmod 644 /tmp/test/CCcam
cd /tmp/test
sed -n '75,75p' CCcam > CCcam1
sed 's/\(["]\+\)/\n\1/g' CCcam1 > CCcam2
sed -n '2,2p' CCcam2 > CCcam3
tr -d '["]' < "CCcam3" > CCcam4
tr -d '[\]' < "CCcam4" > /tmp/film/film93
cd /
rm -rf /tmp/test
####################################################################################################
[ -d /tmp/test ] || mkdir -p /tmp/test

curl -k -A -k   https://prehraj.to/rocky-1-cz-dabing-1080p-1976/56f3d21abaf2c > /tmp/test/CCcam
chmod 644 /tmp/test/CCcam
cd /tmp/test
sed -n '75,75p' CCcam > CCcam1
sed 's/\(["]\+\)/\n\1/g' CCcam1 > CCcam2
sed -n '2,2p' CCcam2 > CCcam3
tr -d '["]' < "CCcam3" > CCcam4
tr -d '[\]' < "CCcam4" > /tmp/film/film94
cd /
rm -rf /tmp/test
####################################################################################################
[ -d /tmp/test ] || mkdir -p /tmp/test

curl -k -A -k   https://prehraj.to/rocky-2-hd-1979-cz/584e11e835c5f > /tmp/test/CCcam
chmod 644 /tmp/test/CCcam
cd /tmp/test
sed -n '75,75p' CCcam > CCcam1
sed 's/\(["]\+\)/\n\1/g' CCcam1 > CCcam2
sed -n '2,2p' CCcam2 > CCcam3
tr -d '["]' < "CCcam3" > CCcam4
tr -d '[\]' < "CCcam4" > /tmp/film/film95
cd /
rm -rf /tmp/test
####################################################################################################
[ -d /tmp/test ] || mkdir -p /tmp/test

curl -k -A -k   https://prehraj.to/rocky-3-1982-720p-hdtv-x264-cz/59e0979b2f26e > /tmp/test/CCcam
chmod 644 /tmp/test/CCcam
cd /tmp/test
sed -n '75,75p' CCcam > CCcam1
sed 's/\(["]\+\)/\n\1/g' CCcam1 > CCcam2
sed -n '2,2p' CCcam2 > CCcam3
tr -d '["]' < "CCcam3" > CCcam4
tr -d '[\]' < "CCcam4" > /tmp/film/film96
cd /
rm -rf /tmp/test
####################################################################################################
[ -d /tmp/test ] || mkdir -p /tmp/test

curl -k -A -k   https://prehraj.to/rocky-4-1985-cz/5e5d6db0deea4 > /tmp/test/CCcam
chmod 644 /tmp/test/CCcam
cd /tmp/test
sed -n '75,75p' CCcam > CCcam1
sed 's/\(["]\+\)/\n\1/g' CCcam1 > CCcam2
sed -n '2,2p' CCcam2 > CCcam3
tr -d '["]' < "CCcam3" > CCcam4
tr -d '[\]' < "CCcam4" > /tmp/film/film97
cd /
rm -rf /tmp/test
####################################################################################################
[ -d /tmp/test ] || mkdir -p /tmp/test

curl -k -A -k   https://prehraj.to/rocky-5-nejlepsi-kvalita-cz/5abfd8119424c > /tmp/test/CCcam
chmod 644 /tmp/test/CCcam
cd /tmp/test
sed -n '75,75p' CCcam > CCcam1
sed 's/\(["]\+\)/\n\1/g' CCcam1 > CCcam2
sed -n '2,2p' CCcam2 > CCcam3
tr -d '["]' < "CCcam3" > CCcam4
tr -d '[\]' < "CCcam4" > /tmp/film/film98
cd /
rm -rf /tmp/test
####################################################################################################
[ -d /tmp/test ] || mkdir -p /tmp/test

curl -k -A -k   https://prehraj.to/rocky-5-nejlepsi-kvalita-cz/5abfd8119424c > /tmp/test/CCcam
chmod 644 /tmp/test/CCcam
cd /tmp/test
sed -n '75,75p' CCcam > CCcam1
sed 's/\(["]\+\)/\n\1/g' CCcam1 > CCcam2
sed -n '2,2p' CCcam2 > CCcam3
tr -d '["]' < "CCcam3" > CCcam4
tr -d '[\]' < "CCcam4" > /tmp/film/film98
cd /
rm -rf /tmp/test
####################################################################################################
[ -d /tmp/test ] || mkdir -p /tmp/test

curl -k -A -k   https://prehraj.to/rocky-6-rocky-balboa-6-2006-cz-dabing/56f3cc5ef40af > /tmp/test/CCcam
chmod 644 /tmp/test/CCcam
cd /tmp/test
sed -n '75,75p' CCcam > CCcam1
sed 's/\(["]\+\)/\n\1/g' CCcam1 > CCcam2
sed -n '2,2p' CCcam2 > CCcam3
tr -d '["]' < "CCcam3" > CCcam4
tr -d '[\]' < "CCcam4" > /tmp/film/film99
cd /
rm -rf /tmp/test
####################################################################################################
[ -d /tmp/test ] || mkdir -p /tmp/test

curl -k -A -k   https://prehraj.to/creed-2015-cz-dabing-1080p/5c755f4819a29 > /tmp/test/CCcam
chmod 644 /tmp/test/CCcam
cd /tmp/test
sed -n '75,75p' CCcam > CCcam1
sed 's/\(["]\+\)/\n\1/g' CCcam1 > CCcam2
sed -n '2,2p' CCcam2 > CCcam3
tr -d '["]' < "CCcam3" > CCcam4
tr -d '[\]' < "CCcam4" > /tmp/film/film100
cd /
rm -rf /tmp/test
####################################################################################################
[ -d /tmp/test ] || mkdir -p /tmp/test

curl -k -A -k   https://prehraj.to/creed-2-2018-hd-cz-dabing-denon/5c8ff1c662604 > /tmp/test/CCcam
chmod 644 /tmp/test/CCcam
cd /tmp/test
sed -n '75,75p' CCcam > CCcam1
sed 's/\(["]\+\)/\n\1/g' CCcam1 > CCcam2
sed -n '2,2p' CCcam2 > CCcam3
tr -d '["]' < "CCcam3" > CCcam4
tr -d '[\]' < "CCcam4" > /tmp/film/film101
cd /
rm -rf /tmp/test

##########################################################################################################################################
cd /
cd /tmp/film
echo "#EXTINF:-1,Blade 1" > m3u.m3u
cat film1 >> m3u.m3u
echo "#EXTINF:-1,Blade 2" >> m3u.m3u
cat film2 >> m3u.m3u
echo "#EXTINF:-1,Blade 3" >> m3u.m3u
cat film3 >> m3u.m3u
echo "#EXTINF:-1,Iron Man 1" >> m3u.m3u
cat film4 >> m3u.m3u
echo "#EXTINF:-1,Iron Man 2" >> m3u.m3u
cat film5 >> m3u.m3u
echo "#EXTINF:-1,Iron Man 3" >> m3u.m3u
cat film6 >> m3u.m3u
echo "#EXTINF:-1,Resident Evil 1" >> m3u.m3u
cat film7 >> m3u.m3u
echo "#EXTINF:-1,Resident Evil 2" >> m3u.m3u
cat film8 >> m3u.m3u
echo "#EXTINF:-1,Resident Evil 3" >> m3u.m3u
cat film9 >> m3u.m3u
echo "#EXTINF:-1,Resident Evil 4" >> m3u.m3u
cat film10 >> m3u.m3u
echo "#EXTINF:-1,Resident Evil 5" >> m3u.m3u
cat film11 >> m3u.m3u
echo "#EXTINF:-1,Resident Evil 6" >> m3u.m3u
cat film12 >> m3u.m3u
echo "#EXTINF:-1,Spiderman 1" >> m3u.m3u
cat film13 >> m3u.m3u
echo "#EXTINF:-1,Spiderman 2" >> m3u.m3u
cat film14 >> m3u.m3u
echo "#EXTINF:-1,Spiderman 3" >> m3u.m3u
cat film15 >> m3u.m3u
echo "#EXTINF:-1,Avengers 1" >> m3u.m3u
cat film16 >> m3u.m3u
echo "#EXTINF:-1,Avengers 2" >> m3u.m3u
cat film17 >> m3u.m3u
echo "#EXTINF:-1,Avengers 3" >> m3u.m3u
cat film18 >> m3u.m3u
echo "#EXTINF:-1,Avengers 4" >> m3u.m3u
cat film19 >> m3u.m3u
echo "#EXTINF:-1,Ant-Man 1" >> m3u.m3u
cat film20 >> m3u.m3u
echo "#EXTINF:-1,Ant-Man 2" >> m3u.m3u
cat film21 >> m3u.m3u
echo "#EXTINF:-1,Thor 1" >> m3u.m3u
cat film22 >> m3u.m3u
echo "#EXTINF:-1,Thor 2" >> m3u.m3u
cat film23 >> m3u.m3u
echo "#EXTINF:-1,Thor 3" >> m3u.m3u
cat film24 >> m3u.m3u
echo "#EXTINF:-1,Captain Marvel" >> m3u.m3u
cat film25 >> m3u.m3u
echo "#EXTINF:-1,Black Panther" >> m3u.m3u
cat film26 >> m3u.m3u
echo "#EXTINF:-1,Strážci Galaxie 1" >> m3u.m3u
cat film27 >> m3u.m3u
echo "#EXTINF:-1,Strážci Galaxie 2" >> m3u.m3u
cat film28 >> m3u.m3u
echo "#EXTINF:-1,Hulk 1" >> m3u.m3u
cat film29 >> m3u.m3u
echo "#EXTINF:-1,Hulk 2" >> m3u.m3u
cat film30 >> m3u.m3u
echo "#EXTINF:-1,Hulk 2003" >> m3u.m3u
cat film31 >> m3u.m3u
echo "#EXTINF:-1,Sebevražedný oddíl" >> m3u.m3u
cat film32 >> m3u.m3u
echo "#EXTINF:-1,Daredevil" >> m3u.m3u
cat film33 >> m3u.m3u
echo "#EXTINF:-1,Elektra" >> m3u.m3u
cat film34 >> m3u.m3u
echo "#EXTINF:-1,Ghost Rider 1" >> m3u.m3u
cat film35 >> m3u.m3u
echo "#EXTINF:-1,Ghost Rider 2" >> m3u.m3u
cat film36 >> m3u.m3u
echo "#EXTINF:-1,Soudce Dredd" >> m3u.m3u
cat film37 >> m3u.m3u
echo "#EXTINF:-1,Dredd" >> m3u.m3u
cat film38 >> m3u.m3u
echo "#EXTINF:-1,Deadpool 1" >> m3u.m3u
cat film39 >> m3u.m3u
echo "#EXTINF:-1,Deadpool 2" >> m3u.m3u
cat film40 >> m3u.m3u
echo "#EXTINF:-1,Captain America 1" >> m3u.m3u
cat film41 >> m3u.m3u
echo "#EXTINF:-1,Captain America 2" >> m3u.m3u
cat film42 >> m3u.m3u
echo "#EXTINF:-1,Captain America 3" >> m3u.m3u
cat film43 >> m3u.m3u
echo "#EXTINF:-1,Venom" >> m3u.m3u
cat film44 >> m3u.m3u
echo "#EXTINF:-1,Robocop 2014" >> m3u.m3u
cat film45 >> m3u.m3u
echo "#EXTINF:-1,Robocop 1" >> m3u.m3u
cat film46 >> m3u.m3u
echo "#EXTINF:-1,Robocop 2" >> m3u.m3u
cat film47 >> m3u.m3u
echo "#EXTINF:-1,Robocop 3" >> m3u.m3u
cat film48 >> m3u.m3u
echo "#EXTINF:-1,Robocop 4" >> m3u.m3u
cat film49 >> m3u.m3u
echo "#EXTINF:-1,Terminator 1" >> m3u.m3u
cat film50 >> m3u.m3u
echo "#EXTINF:-1,Terminator 2" >> m3u.m3u
cat film51 >> m3u.m3u
echo "#EXTINF:-1,Vzpoura strojů 1986" >> m3u.m3u
cat film52 >> m3u.m3u
echo "#EXTINF:-1,Návrat do budoucnosti 1" >> m3u.m3u
cat film53 >> m3u.m3u
echo "#EXTINF:-1,Návrat do budoucnosti 2" >> m3u.m3u
cat film54 >> m3u.m3u
echo "#EXTINF:-1,Návrat do budoucnosti 3" >> m3u.m3u
cat film55 >> m3u.m3u
echo "#EXTINF:-1,Blízká setkání třetího druhu" >> m3u.m3u
cat film56 >> m3u.m3u
echo "#EXTINF:-1,Vládci vesmíru" >> m3u.m3u
cat film57 >> m3u.m3u
echo "#EXTINF:-1,Temný anděl" >> m3u.m3u
cat film58 >> m3u.m3u
echo "#EXTINF:-1,Predátor 1" >> m3u.m3u
cat film59 >> m3u.m3u
echo "#EXTINF:-1,Predátor 2" >> m3u.m3u
cat film60 >> m3u.m3u
echo "#EXTINF:-1,Predátor Evoluce" >> m3u.m3u
cat film61 >> m3u.m3u
echo "#EXTINF:-1,Alien vs Predátor 1" >> m3u.m3u
cat film62 >> m3u.m3u
echo "#EXTINF:-1,Alien vs Predátor 2" >> m3u.m3u
cat film63 >> m3u.m3u
echo "#EXTINF:-1,Predátoři" >> m3u.m3u
cat film64 >> m3u.m3u
echo "#EXTINF:-1,Vetřelec 1" >> m3u.m3u
cat film65 >> m3u.m3u
echo "#EXTINF:-1,Vetřelec 2" >> m3u.m3u
cat film66 >> m3u.m3u
echo "#EXTINF:-1,Vetřelec 3" >> m3u.m3u
cat film67 >> m3u.m3u
echo "#EXTINF:-1,Vetřelec 4" >> m3u.m3u
cat film68 >> m3u.m3u
echo "#EXTINF:-1,Vetřelec Cov" >> m3u.m3u
cat film69 >> m3u.m3u
echo "#EXTINF:-1,To 1990" >> m3u.m3u
cat film70 >> m3u.m3u
echo "#EXTINF:-1,To 2017" >> m3u.m3u
cat film71 >> m3u.m3u
echo "#EXTINF:-1,To kapitola 2" >> m3u.m3u
cat film72 >> m3u.m3u
echo "#EXTINF:-1,Smrtelné zlo 2" >> m3u.m3u
cat film73 >> m3u.m3u
echo "#EXTINF:-1,Návrat oživlích mrtvol 2" >> m3u.m3u
cat film74 >> m3u.m3u
echo "#EXTINF:-1,Návrat oživlích mrtvol 3" >> m3u.m3u
cat film75 >> m3u.m3u
echo "#EXTINF:-1,Úsvit mrtvých" >> m3u.m3u
cat film76 >> m3u.m3u
echo "#EXTINF:-1,Soumrak mrtvých" >> m3u.m3u
cat film77 >> m3u.m3u
echo "#EXTINF:-1,Zombieland" >> m3u.m3u
cat film78 >> m3u.m3u
echo "#EXTINF:-1,Zombieland 2" >> m3u.m3u
cat film79 >> m3u.m3u
echo "#EXTINF:-1,Země mrtvých" >> m3u.m3u
cat film80 >> m3u.m3u
echo "#EXTINF:-1,Smrtonosná zbraň 1" >> m3u.m3u
cat film81 >> m3u.m3u
echo "#EXTINF:-1,Smrtonosná zbraň 2" >> m3u.m3u
cat film82 >> m3u.m3u
echo "#EXTINF:-1,Smrtonosná zbraň 3" >> m3u.m3u
cat film83 >> m3u.m3u
echo "#EXTINF:-1,Smrtonosná zbraň 4" >> m3u.m3u
cat film84 >> m3u.m3u
echo "#EXTINF:-1,Do útoku" >> m3u.m3u
cat film85 >> m3u.m3u
echo "#EXTINF:-1,Kriminál" >> m3u.m3u
cat film86 >> m3u.m3u
echo "#EXTINF:-1,Krvavý sport" >> m3u.m3u
cat film87 >> m3u.m3u
echo "#EXTINF:-1,Kickboxer" >> m3u.m3u
cat film88 >> m3u.m3u
echo "#EXTINF:-1,Rambo 1" >> m3u.m3u
cat film89 >> m3u.m3u
echo "#EXTINF:-1,Rambo 2" >> m3u.m3u
cat film90 >> m3u.m3u
echo "#EXTINF:-1,Rambo 3" >> m3u.m3u
cat film91 >> m3u.m3u
echo "#EXTINF:-1,Rambo 4" >> m3u.m3u
cat film92 >> m3u.m3u
echo "#EXTINF:-1,Rambo Last Blood" >> m3u.m3u
cat film93 >> m3u.m3u
echo "#EXTINF:-1,Rocky 1" >> m3u.m3u
cat film94 >> m3u.m3u
echo "#EXTINF:-1,Rocky 2" >> m3u.m3u
cat film95 >> m3u.m3u
echo "#EXTINF:-1,Rocky 3" >> m3u.m3u
cat film96 >> m3u.m3u
echo "#EXTINF:-1,Rocky 4" >> m3u.m3u
cat film97 >> m3u.m3u
echo "#EXTINF:-1,Rocky 5" >> m3u.m3u
cat film98 >> m3u.m3u
echo "#EXTINF:-1,Rocky 6" >> m3u.m3u
cat film99 >> m3u.m3u
echo "#EXTINF:-1,Creed" >> m3u.m3u
cat film100 >> m3u.m3u
echo "#EXTINF:-1,Creed 2" >> m3u.m3u
cat film101 >> m3u.m3u
#####################################################
cp m3u.m3u /movie/film.m3u

cd /
rm -rf /tmp/film


more /usr/lib/enigma2/python/Plugins/Extensions/OpenPanel/DATA/x  >> /etc/enigma2/bouquets.tv 
sed -i "s/%/userbouquet.Film.m3u.tv/" /etc/enigma2/bouquets.tv 


cd /
rm -rf /tmp/test
echo ""
echo "converter Film.m3u for Enigma"
sleep 1
echo "start"
[ -d /tmp/test ] || mkdir -p /tmp/test
cp /movie/film.m3u /tmp/test/Ru.m3u
awk 'BEGIN {FS="png"}{print  $NF}'  /tmp/test/Ru.m3u > /tmp/test/Rus3.m3u
awk 'BEGIN {FS="group-"}{print  $NF}'  /tmp/test/Rus3.m3u > /tmp/test/Rus4.m3u
sed 's/",/#DESCRIPTION /g' /tmp/test/Rus4.m3u > /tmp/test/Rus5.m3u
sed 's/#EXTINF/#DESCRIPTION /g' /tmp/test/Rus5.m3u > /tmp/test/Rus5a.m3u
sed 's/:-1 ,/ /g' /tmp/test/Rus5a.m3u > /tmp/test/Rus6.m3u
sed 's/:-1,/ /g' /tmp/test/Rus6.m3u > /tmp/test/Rus6a.m3u
sed 's/:0,/ /g' /tmp/test/Rus6a.m3u > /tmp/test/Rus6b.m3u
sed 's/: / /g' /tmp/test/Rus6b.m3u > /tmp/test/Rus6c.m3u
sed 's/:/%3a/g' /tmp/test/Rus6c.m3u > /tmp/test/Rus7.m3u
sed -e "s/http/#SERVICE 4097:0:1128:0:0:0:0:0:0:0:http/" /tmp/test/Rus7.m3u > /tmp/test/Rus8.m3u
sed -e "s/rtmp/#SERVICE 4097:0:1128:0:0:0:0:0:0:0:rtmp/" /tmp/test/Rus8.m3u > /tmp/test/Rus8a.m3u
sed -e "s/mmsh/#SERVICE 4097:0:1128:0:0:0:0:0:0:0:mmsh/" /tmp/test/Rus8a.m3u > /tmp/test/Rus8b.m3u
tr -d '["]' < "/tmp/test/Rus8b.m3u" > /tmp/test/Rus8c.m3u
tr -d '[,]' < "/tmp/test/Rus8c.m3u" > /tmp/test/Rus8.m3u
awk '{print NR " " $0}' /tmp/test/Rus8.m3u  > /tmp/test/Rus9.m3u
sort -n -r "/tmp/test/Rus9.m3u"|grep -o -i '#[^<]*' > /tmp/test/Rus10.m3u
echo "#NAME Film.m3u" > /etc/enigma2/userbouquet.Film.m3u.tv
cat /tmp/test/Rus10.m3u >> /etc/enigma2/userbouquet.Film.m3u.tv
rm -rf /tmp/test
cd /
wget -q -O - http://root%s@127.0.0.1/web/servicelistreload?mode=0 >>/dev/null 2>&1 </dev/null &
sleep 2
echo "OK"
exit







