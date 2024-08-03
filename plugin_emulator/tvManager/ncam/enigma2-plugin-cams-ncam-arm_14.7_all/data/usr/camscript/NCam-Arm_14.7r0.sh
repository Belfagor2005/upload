#!/bin/sh
Action=$1
OSD="NCam-Arm_14.7r0"
chmod 755 /usr/bin/${OSD}
cam_clean () {
	rm -rf /tmp/ecm.info /tmp/script.info /tmp/pid.info /tmp/cardinfo /tmp/cam.info /tmp/debug.txt /tmp/ecm0.info /tmp/mbox.ver /tmp/newcs.pid /tmp/share.info /tmp/share.onl /tmp/stat.info
}

cam_up () {
	cam_clean
	sleep 2
	/usr/bin/NCam-Arm_14.7r0 -c /etc/tuxbox/config &
}

cam_down() {
#	touch /tmp/ncam.kill
	sleep 4
	killall -9 NCam-Arm_14.7r0
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

