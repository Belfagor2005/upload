#!/bin/sh
echo "stahuji seznam m3u Pohádky"


#!/bin/sh
echo "stahuji  ...."
echo ""
echo "předpokládaný čas 2 minuty"
echo ""





echo ""
echo ""
[ -d /movie ] || mkdir -p /movie
[ -d /tmp/test ] || mkdir -p /tmp/test
[ -d /tmp/film ] || mkdir -p /tmp/film




curl -k -A -k   https://prehraj.to/krtecek-animovana-pohadka-zdenek-miler/5c2f481f81459 > /tmp/test/CCcam
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

curl -k -A -k   https://prehraj.to/krtecek-2-animovana-pohadka-zdenek-miler/5c3a7b56a8df4 > /tmp/test/CCcam
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

curl -k -A -k   https://prehraj.to/krtecek-3-animovana-pohadka-zdenek-miler/5c3a8a237f0fb > /tmp/test/CCcam
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

curl -k -A -k   https://prehraj.to/krtecek-4-animovana-pohadka-zdenek-miler/5c3a8ccb70de2 > /tmp/test/CCcam
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

curl -k -A -k   https://prehraj.to/krtecek-5-animovana-pohadka-zdenek-miler/5c3a8ccb6f335 > /tmp/test/CCcam
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

curl -k -A -k   https://prehraj.to/krtecek-6-animovana-pohadka-zdenek-miler/5c3a9378689bf > /tmp/test/CCcam
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

curl -k -A -k   https://prehraj.to/madagaskar-1-cz-dabing-nejlepsi-kvalita/5e8f91c38ef51 > /tmp/test/CCcam
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

curl -k -A -k   https://prehraj.to/madagaskar-2-cz-dabing/5ba4b9725f2a4 > /tmp/test/CCcam
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

curl -k -A -k   https://prehraj.to/madagaskar-3-cz-dabing/5bcc5caa3abb9 > /tmp/test/CCcam
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

curl -k -A -k   https://prehraj.to/doba-ledova-1-2002-cz/57d8384a6f781 > /tmp/test/CCcam
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

curl -k -A -k   https://prehraj.to/doba-ledova-2-2006-cz/57d838c3d41e6 > /tmp/test/CCcam
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

curl -k -A -k   https://prehraj.to/doba-ledova-3-usvit-dinosauru-anim-2009-cz-dabing/5c5154d5cac83 > /tmp/test/CCcam
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

curl -k -A -k   https://prehraj.to/doba-ledova-4-cz-dabing/5c53a868094ff > /tmp/test/CCcam
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

curl -k -A -k   https://prehraj.to/doba-ledova-5-mamuti-drcnuti-cz-dabing-2016-animovany/5e1aac58dbf11 > /tmp/test/CCcam
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

curl -k -A -k   https://prehraj.to/toy-story-1-pribeh-hracek-1995-cz-dabing/57e1865033138 > /tmp/test/CCcam
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

curl -k -A -k   https://prehraj.to/toy-story-2-pribeh-hracek-cz-dabing/5ba59dc03056c > /tmp/test/CCcam
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

curl -k -A -k   https://prehraj.to/toy-story-3-pribeh-hracek-cz-dabing/5ba59ededac87 > /tmp/test/CCcam
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

curl -k -A -k   https://prehraj.to/hleda-se-nemo-nejlepsi-kvalita-cz/5abacfc89534e > /tmp/test/CCcam
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

curl -k -A -k   https://prehraj.to/hleda-se-dori-hd-1080p-cz-dabing-2015-animovany-lehi/5969c1a8b3519 > /tmp/test/CCcam
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

curl -k -A -k   https://prehraj.to/smoulove-1-cz-dabing-2011/582143b6e9719 > /tmp/test/CCcam
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

curl -k -A -k   https://prehraj.to/smoulove-2-anim-2013-cz-dabing/5c68f66440c6e > /tmp/test/CCcam
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

curl -k -A -k   https://prehraj.to/smoulove-3-cz-dabing-2017-animovany/5b35a857dca94 > /tmp/test/CCcam
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

curl -k -A -k   https://prehraj.to/zelvy-ninja-1-cz-dabing-2014/5de9232ff1a50 > /tmp/test/CCcam
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

curl -k -A -k   https://prehraj.to/zelvy-ninja-2-cz-dabing-2016-full-hd-1080p/586c4b6ea8da4 > /tmp/test/CCcam
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

curl -k -A -k   https://prehraj.to/nekonecny-pribeh-cz-dabing/5b9cd /cbcf368a > /tmp/test/CCcam
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

curl -k -A -k   https://prehraj.to/nekonecny-pribeh-2-cz-dabing-denon/5c3f0f58cd /7e6 > /tmp/test/CCcam
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

curl -k -A -k   https://prehraj.to/nekonecny-pribeh-3-cz-dabing-denon/5c3f17f369026 > /tmp/test/CCcam
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

curl -k -A -k   https://prehraj.to/posledni-jednorozec-1982-dvdrip-xvid-cz-by-deejay-snoopy77/58c7fbbf3268a > /tmp/test/CCcam
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

curl -k -A -k   https://prehraj.to/snehurka-a-sedm-trpasliku-nejlepsi-kvalita-cz/5abb099baa8e4 > /tmp/test/CCcam
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

curl -k -A -k   https://prehraj.to/letopisy-narnie-1-lev-carodejnice-a-skrin-2005-cz/5dd6181b9b937 > /tmp/test/CCcam
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

curl -k -A -k   https://prehraj.to/letopisy-narnie-2-princ-kaspian-2008-cz-dabing/5837160263d86 > /tmp/test/CCcam
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

curl -k -A -k   https://prehraj.to/letopisy-narnie-3-plavba-jitriho-poutnika-2010-cz/5dd61a5b1b472 > /tmp/test/CCcam
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

curl -k -A -k   https://prehraj.to/starostlivi-medvidci-v-risi-kouzel/5820002908aa1 > /tmp/test/CCcam
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

curl -k -A -k   https://prehraj.to/shrek-1-2001-cz-dabing/5c38dc208f5ef > /tmp/test/CCcam
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

curl -k -A -k   https://prehraj.to/shrek-2-2004-cz-dabing/5c3a0a2a75699 > /tmp/test/CCcam
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

curl -k -A -k   https://prehraj.to/shrek-3-cz-dabing/5b9cf7801a6ff > /tmp/test/CCcam
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

curl -k -A -k   https://prehraj.to/shrek-4-zvonec-a-konec-2010-cz-dabing/5c3a0f7ba4df9 > /tmp/test/CCcam
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

curl -k -A -k   https://prehraj.to/jak-vycvicit-draka-1-anim-2010-cz-dabing/5ccd /994de4e9f > /tmp/test/CCcam
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

curl -k -A -k   https://prehraj.to/jak-vycvicit-draka-2-cz-dabing/5e32cf9371f4b > /tmp/test/CCcam
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

curl -k -A -k   https://prehraj.to/jak-vycvicit-draka-3-2019-czdabing/5eaa1a491b2d1 > /tmp/test/CCcam
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

curl -k -A -k   https://prehraj.to/lucie-postrach-ulice-1984/5c426d17685ce > /tmp/test/CCcam
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

curl -k -A -k   https://prehraj.to/a-zase-ta-lucie-cz-dabing-1984/5dfdcd /0fad863 > /tmp/test/CCcam
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

curl -k -A -k   https://prehraj.to/chobotnice-z-ii-patra-vesele-vanoce-preji-zelena-a-modry-cz-dabing-1986/5e130f8288b15 > /tmp/test/CCcam
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

curl -k -A -k   https://prehraj.to/baron-prasil-cz-dabing-1961/5c10bf9772fb6 > /tmp/test/CCcam
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

curl -k -A -k   https://prehraj.to/za-plotem-over-the-hedge-2006-cz/5e2614e9cb73c > /tmp/test/CCcam
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

curl -k -A -k   https://prehraj.to/auta-1-cz-dabing/5c83e09e6cb23 > /tmp/test/CCcam
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

curl -k -A -k   https://prehraj.to/auta-2/5d63f294e8be6 > /tmp/test/CCcam
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

curl -k -A -k   https://prehraj.to/auta-3-cz-dabing/5c847fba81443 > /tmp/test/CCcam
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

curl -k -A -k   https://prehraj.to/letadla-cz-dabing-2013-xxx/58ca48159650a > /tmp/test/CCcam
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

curl -k -A -k   https://prehraj.to/letadla-2-hasici-a-zachranari-2014-cz-dabing-animovany/558bd39b28fee > /tmp/test/CCcam
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

curl -k -A -k   https://prehraj.to/ja-padouch-1-2010-cz/5dd60a9b650da > /tmp/test/CCcam
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

curl -k -A -k   https://prehraj.to/ja-padouch-2-cz-dabing/5ba4b23559d87 > /tmp/test/CCcam
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

curl -k -A -k   https://prehraj.to/ja-padouch-3-2017-hd-cz/5e881000b1c4d > /tmp/test/CCcam
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

curl -k -A -k   https://prehraj.to/priserky-z-vesmiru-cz-dabing/5c69d4d363621 > /tmp/test/CCcam
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

curl -k -A -k   https://prehraj.to/priserky-sro-kim-cz/58d5698222b32 > /tmp/test/CCcam
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

curl -k -A -k   https://prehraj.to/v-hlave-nejlepsi-kvalita-cz/5ab064d0b6c32 > /tmp/test/CCcam
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

##########################################################################################################################################
cd /
cd /tmp/film
echo "#EXTINF:-1,Krteček 1" > m3u.m3u
cat film1 >> m3u.m3u
echo "#EXTINF:-1,Krteček 2" >> m3u.m3u
cat film2 >> m3u.m3u
echo "#EXTINF:-1,Krteček 3" >> m3u.m3u
cat film3 >> m3u.m3u
echo "#EXTINF:-1,Krteček 4" >> m3u.m3u
cat film4 >> m3u.m3u
echo "#EXTINF:-1,Krteček 5" >> m3u.m3u
cat film5 >> m3u.m3u
echo "#EXTINF:-1,Krteček 6" >> m3u.m3u
cat film6 >> m3u.m3u
echo "#EXTINF:-1,Madagaskar 1" >> m3u.m3u
cat film7 >> m3u.m3u
echo "#EXTINF:-1,Madagaskar 2" >> m3u.m3u
cat film8 >> m3u.m3u
echo "#EXTINF:-1,Madagaskar 3" >> m3u.m3u
cat film9 >> m3u.m3u
echo "#EXTINF:-1,Doba ledová 1" >> m3u.m3u
cat film10 >> m3u.m3u
echo "#EXTINF:-1,Doba ledová 2" >> m3u.m3u
cat film11 >> m3u.m3u
echo "#EXTINF:-1,Doba ledová 3" >> m3u.m3u
cat film12 >> m3u.m3u
echo "#EXTINF:-1,Doba ledová 4" >> m3u.m3u
cat film13 >> m3u.m3u
echo "#EXTINF:-1,Doba ledová 5" >> m3u.m3u
cat film14 >> m3u.m3u
echo "#EXTINF:-1,Toy Story 1" >> m3u.m3u
cat film15 >> m3u.m3u
echo "#EXTINF:-1,Toy Story 2" >> m3u.m3u
cat film16 >> m3u.m3u
echo "#EXTINF:-1,Toy Story 3" >> m3u.m3u
cat film17 >> m3u.m3u
echo "#EXTINF:-1,Hledá se Nemo" >> m3u.m3u
cat film18 >> m3u.m3u
echo "#EXTINF:-1,Hledá se Dory" >> m3u.m3u
cat film19 >> m3u.m3u
echo "#EXTINF:-1,Šmoulové 1" >> m3u.m3u
cat film20 >> m3u.m3u
echo "#EXTINF:-1,Šmoulové 2" >> m3u.m3u
cat film21 >> m3u.m3u
echo "#EXTINF:-1,Šmoulové 3" >> m3u.m3u
cat film22 >> m3u.m3u
echo "#EXTINF:-1,Želvy Ninja 1" >> m3u.m3u
cat film23 >> m3u.m3u
echo "#EXTINF:-1,Želvy Ninja 2" >> m3u.m3u
cat film24 >> m3u.m3u
echo "#EXTINF:-1,Nekonečný příběh 1" >> m3u.m3u
cat film25 >> m3u.m3u
echo "#EXTINF:-1,Nekonečný příběh 2" >> m3u.m3u
cat film26 >> m3u.m3u
echo "#EXTINF:-1,Nekonečný příběh 3" >> m3u.m3u
cat film27 >> m3u.m3u
echo "#EXTINF:-1,Poslední jednorožec" >> m3u.m3u
cat film28 >> m3u.m3u
echo "#EXTINF:-1,Sněhurka a sedm trpaslíků" >> m3u.m3u
cat film29 >> m3u.m3u
echo "#EXTINF:-1,Letopisy Narnie 1" >> m3u.m3u
cat film30 >> m3u.m3u
echo "#EXTINF:-1,Letopisy Narnie 2" >> m3u.m3u
cat film31 >> m3u.m3u
echo "#EXTINF:-1,Letopisy Narnie 3" >> m3u.m3u
cat film32 >> m3u.m3u
echo "#EXTINF:-1,Starostlivi-medvidci-v-risi-kouzel" >> m3u.m3u
cat film33 >> m3u.m3u
echo "#EXTINF:-1,Shrek 1" >> m3u.m3u
cat film34 >> m3u.m3u
echo "#EXTINF:-1,Shrek 2" >> m3u.m3u
cat film35 >> m3u.m3u
echo "#EXTINF:-1,Shrek 3" >> m3u.m3u
cat film36 >> m3u.m3u
echo "#EXTINF:-1,Shrek 4" >> m3u.m3u
cat film37 >> m3u.m3u
echo "#EXTINF:-1,Jak vycvičit draka 1" >> m3u.m3u
cat film38 >> m3u.m3u
echo "#EXTINF:-1,Jak vycvičit draka 2" >> m3u.m3u
cat film39 >> m3u.m3u
echo "#EXTINF:-1,Jak vycvičit draka 3" >> m3u.m3u
cat film40 >> m3u.m3u
echo "#EXTINF:-1,Lucie postrach ulice" >> m3u.m3u
cat film41 >> m3u.m3u
echo "#EXTINF:-1,A zase ta Lucie" >> m3u.m3u
cat film42 >> m3u.m3u
echo "#EXTINF:-1,Chobotnice z II. patra1,2,3,4" >> m3u.m3u
cat film43 >> m3u.m3u
echo "#EXTINF:-1,Baron Prášil" >> m3u.m3u
cat film44 >> m3u.m3u
echo "#EXTINF:-1,Za plotem" >> m3u.m3u
cat film45 >> m3u.m3u
echo "#EXTINF:-1,Auta 1" >> m3u.m3u
cat film46 >> m3u.m3u
echo "#EXTINF:-1,Auta 2" >> m3u.m3u
cat film47 >> m3u.m3u
echo "#EXTINF:-1,Auta 3" >> m3u.m3u
cat film48 >> m3u.m3u
echo "#EXTINF:-1,Letadla 1" >> m3u.m3u
cat film49 >> m3u.m3u
echo "#EXTINF:-1,Letadla 2" >> m3u.m3u
cat film50 >> m3u.m3u
echo "#EXTINF:-1,Já padouch 1" >> m3u.m3u
cat film51 >> m3u.m3u
echo "#EXTINF:-1,Já padouch 2" >> m3u.m3u
cat film52 >> m3u.m3u
echo "#EXTINF:-1,Já padouch 3" >> m3u.m3u
cat film53 >> m3u.m3u
echo "#EXTINF:-1,Příšerky z vesmíru" >> m3u.m3u
cat film54 >> m3u.m3u
echo "#EXTINF:-1,Příšerky sro" >> m3u.m3u
cat film55 >> m3u.m3u
echo "#EXTINF:-1,V hlavě" >> m3u.m3u
cat film56 >> m3u.m3u
echo "#EXTINF:-1,Vládci vesmíru" >> m3u.m3u
cat film57 >> m3u.m3u






#####################################################
cp m3u.m3u /movie/Pohádky.m3u
cp m3u.m3u /usr/lib/enigma2/python/Plugins/Extensions/XBMCAddons/XBMC/plugin.video.m3u.player/playlists/Pohádky.m3u
cd /
rm -rf /tmp/film

echo "seznam hotov..."
echo "uloženo jako (m3u) do..../movie/"
echo "uloženo jako (m3u) do..../playlists/"

exit

