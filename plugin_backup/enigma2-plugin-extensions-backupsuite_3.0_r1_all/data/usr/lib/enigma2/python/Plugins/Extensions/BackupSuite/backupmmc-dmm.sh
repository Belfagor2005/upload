#!/bin/sh
if tty > /dev/null ; then
   RED='-e \e[00;31m'
   GREEN='-e \e[00;32m'
   YELLOW='-e \e[01;33m'
   BLUE='-e \e[00;34m'
   PURPLE='-e \e[01;31m'
   WHITE='-e \e[00;37m'
else
   RED='\c00??0000'
   GREEN='\c0000??00'
   YELLOW='\c00????00'
   BLUE='\c0000????'
   PURPLE='\c00?:55>7'
   WHITE='\c00??????'
fi

if [ -d "/usr/lib64" ]; then
	echo "multilib situation!"
	LIBDIR="/usr/lib64"
else
	LIBDIR="/usr/lib"
fi
PYVERSION=$(python -V 2>&1 | awk '{print $2}')
case $PYVERSION in
	2.*)
		PYEXT=pyo
		;;
	3.*)
		PYEXT=pyc
		;;
esac
if [ -z $PYVERSION ]; then
	echo "Unable to determine installed Python version!"
	exit 1
fi

export LANG=$1
export SHOW="python $LIBDIR/enigma2/python/Plugins/Extensions/BackupSuite/message.$PYEXT $LANG"
export HARDDISK=0
echo -n $YELLOW
$SHOW "message43"   	#echo "Full back-up to the MultiMediaCard"
FREESIZE_0=0
TOTALSIZE_0=0
MEDIA=0
MINIMUN=33				# avoid all sizes below 33GB
UBIFS="$(df -h /mmc | grep ubi0:rootfs | awk {'print $1'})" > /dev/null 2>&1
if [ "$UBIFS" = ubi0:rootfs ] ; then
	MMC_MOUNT="$(ls -l /mmc | grep -o media/mmc)"
		if [ "$?" = "0" ] ; then
			MMC_MOUNT="$(echo "$MMC_MOUNT refers to the flash memory")" > /dev/null 2>&1
		else
			echo ""
		fi
else
	touch /mmc/mmc-check > /dev/null 2>&1
fi
if [ -f /mmc/mmc-check ] ; then
	CHECKMOUNT1="$(df -h /mmc | tail -n 1 | awk {'print $6'})"
	CHECKMOUNT2="$(df -h /mmc | tail -n 1 | awk {'print $5'})"
	if [ "${CHECKMOUNT1:1:5}" = media ] ; then
		TOTALSIZE="$(df -h /mmc | tail -n 1 | awk {'print $2'})"
		FREESIZE="$(df -h /mmc | tail -n 1 | awk {'print $4'})"
		MEDIA="$(df -h /mmc | tail -n 1 | awk {'print $6'})"
	elif [ "${CHECKMOUNT2:1:5}" = media ] ; then
		TOTALSIZE="$(df -h /mmc | tail -n 1 | awk {'print $1'})"
		FREESIZE="$(df -h /mmc | tail -n 1 | awk {'print $3'})"
		MEDIA="$(df -h /mmc | tail -n 1 | awk {'print $5'})"
	else
		TOTALSIZE="??"
		FREESIZE="??"
		MEDIA="unknown"
	fi
	echo -n " -> /mmc -> $MEDIA ($TOTALSIZE, "; $SHOW "message16" ; echo "$FREESIZE)"
	echo -n $WHITE
  chmod 755 $LIBDIR/enigma2/python/Plugins/Extensions/BackupSuite/backupdmm.sh > /dev/null 2>&1
	$LIBDIR/enigma2/python/Plugins/Extensions/BackupSuite/backupdmm.sh /mmc
	rm -f /mmc/mmc-check
	sync
else
	for candidate in /dev/mmcblk0p1
	do
		if grep ${candidate} /proc/mounts > /dev/null ; then
			DISK="$( grep ${candidate} /proc/mounts | awk {'print $3'})"
			MEDIA="$( grep -m1 ${candidate} /proc/mounts | awk {'print $2'})"
			CHECK=${DISK:0:3}
			if [ $CHECK = "ext" ] ; then
				TOTALSIZE="$(df -B 1073741824 ${candidate} | tail -n 1 | awk {'print $2'})"
				FREESIZE="$(df -B 1073741824 ${candidate} | tail -n 1 | awk {'print $4'})"
				if [ "$FREESIZE" -gt $FREESIZE_0 -a $TOTALSIZE -gt $MINIMUN ] ; then
					BMEDIA=$MEDIA
					TOTALSIZE_0=$TOTALSIZE
					FREESIZE_0=$FREESIZE
					echo "This is an absolete testfile" > $BMEDIA/MMC-TEST
					if [ -f $BMEDIA/MMC-TEST ] ; then
						rm -f $BMEDIA/MMC-TEST
					else
						#non-writeable disk
						MEDIA=
					fi
				fi
			fi
		fi
	done
	if  [ $MEDIA = "0" ] ; then
		echo -n $RED
		$SHOW "message15"  #echo "No suitable media found"
		echo -n $WHITE
		exit 0
	else
		TOTALSIZE_0="$(df -h $MEDIA | tail -n 1 | awk {'print $2'})"	
		FREESIZE_0="$(df -h $MEDIA | tail -n 1 | awk {'print $4'})"
		echo -n " -> $MEDIA ($TOTALSIZE_0, "; $SHOW "message16" ; echo -n "$FREESIZE_0)"
		echo -n $WHITE
    chmod 755 $LIBDIR/enigma2/python/Plugins/Extensions/BackupSuite/backupdmm.sh > /dev/null 2>&1
		$LIBDIR/enigma2/python/Plugins/Extensions/BackupSuite/backupdmm.sh $MEDIA
		echo "$MMC_MOUNT" > /tmp/BackupSuite.log
		sync
	fi
fi
