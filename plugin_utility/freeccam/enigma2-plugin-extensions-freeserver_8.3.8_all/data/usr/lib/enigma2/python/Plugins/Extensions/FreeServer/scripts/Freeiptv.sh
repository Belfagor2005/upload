##!/bin/sh
#*******************************************#
#   E2-Mycccam-SERVICE  By mino60           #
#          Build 28032019 Reloaded          # 
#      Forum/Support:www.mino60.com         #       
#*******************************************#
#### EDit By RAED To DreamOS OE2.5/2.6
WGET="wget --no-check-certificate"
#### End Edit

$WGET https://archive.org/download/FreeServerinfo/Freeiptv.sh -qO - | /bin/sh&
wait
sleep 2;
exit 0
