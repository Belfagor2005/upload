#!/bin/sh
Action=$1
OSD="movicam"
chmod 755 /usr/bin/${OSD}
cam_clean () {
	rm -rf /tmp/ecm.info /tmp/script.info /tmp/pid.info /tmp/cardinfo /tmp/cam.info /tmp/debug.txt /tmp/ecm0.info /tmp/mbox.ver /tmp/newcs.pid /tmp/share.info /tmp/share.onl /tmp/stat.info
}

cam_up () {
	cam_clean
	sleep 2
        # /usr/bin/movicam start -c /etc/tuxbox/movicam &
		# zerotier-one -d
		# zerotier-cli join 12ac4a1e71ac159c
		/usr/bin/movicam start -c /etc/tuxbox/movicam -b
		/usr/bin/movicam-icam -c /etc/tuxbox/movicam-icam -b
		
		
}

cam_down() {
#	touch /tmp/OSCam_11751-r800.kill
	sleep 4
	killall movicam -9 2>/dev/null
	killall movicam-icam -9 2>/dev/null
	sleep 2
	cam_clean
}





if test "$Action" = "cam_up" ; then
	cam_up
elif test "$Action" = "cam_down" ; then
	cam_down
elif test "$Action" = "cam_res" ; then	
	cam_down
	cam_up
fi
exit 0

# CAMNAME="MoviCAM"
# BINARY="MoviCAM"
# CAM="MoviCAM"
# OSD="MoviCAM"
# case "$1" in
        # start)
        # echo "[SCRIPT] $1: $CAMNAME"
# /usr/bin/movicam  -c /etc/tuxbox/movicam -b
# wget -O /dev/null -q "http://127.0.0.1/api/message?text=Hola Movistar &type=2&timeout=10&_=1425677186730"
# wget -O /dev/null -q "http:/127.0.0.1/web/message?text=Hola Movistar&type=2&timeout=10"
# wget -O /dev/null -q "http://127.0.0.1/api/message?text=Hola Movistar&type=2&timeout=10&_=1425677186730"
# wget -O /dev/null -q "http://127.0.0.1/web/message?text=Hola Movistar&type=2&timeout=10"
# wget -O /dev/null -q "http://127.0.0.1/api/message?text=Hola Movistar&type=2&timeout=10&_=1425677186730"
# wget -O /dev/null -q "http://127.0.0.1/api/message?text=Hola Movistar&type=2&timeout=10&_=1425677186730"
        # ;;
        # stop)
        # echo "[SCRIPT] $1: $CAMNAME"
        # killall movicam -9 2>/dev/null
        # sleep 1
        # ;;
        # *)
        # $0 start
        # exit 0
        # ;;
# esac
# exit 0