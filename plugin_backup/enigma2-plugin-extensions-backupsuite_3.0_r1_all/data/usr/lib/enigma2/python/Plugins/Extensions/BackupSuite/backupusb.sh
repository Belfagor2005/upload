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
export HARDDISK=0
export SHOW="python $LIBDIR/enigma2/python/Plugins/Extensions/BackupSuite/message.$PYEXT $LANG"
TARGET="XX"
USEDSIZE=`df -k /usr/ | grep [0-9]% | tr -s " " | cut -d " " -f 3` # size of rootfs
NEEDEDSPACE=$(((4*$USEDSIZE)/1024))
for candidate in `cut -d ' ' -f 2 /proc/mounts | grep '^/media/'`
do
	if [ -f "${candidate}/"*[Bb][Aa][Cc][Kk][Uu][Pp][Ss][Tt][Ii][Cc][Kk]* ] || [ -d "${candidate}/"*[Bb][Aa][Cc][Kk][Uu][Pp][Ss][Tt][Ii][Cc][Kk]* ] 
	then
	TARGET="${candidate}"
	fi 
done
if [ "$TARGET" = "XX" ] ; then
	echo -n $RED
	$SHOW "message21" #error about no USB-found
	echo -n $WHITE
else
	echo -n $YELLOW
	$SHOW "message22" 
	SIZE_1="$(df -h "$TARGET" | tail -n 1 | awk {'print $(NF-2)'})"
	SIZE_2="$(df -h "$TARGET" | tail -n 1 | awk {'print $(NF-4)'})"
	echo -n " -> $TARGET ($SIZE_2, " ; $SHOW "message16" ; echo "$SIZE_1)"
	FREESIZE="$(df -B 1048576 "$TARGET" | tail -n 1 | awk {'print $(NF-2)'})"
	if [ $FREESIZE -lt $NEEDEDSPACE ] ; then
		echo $RED
		$SHOW "message30" ; echo -n "$TARGET" ; $SHOW "message31"
		printf '%5s' $FREESIZE ; $SHOW "message32"
		printf '%5s' $NEEDEDSPACE ; $SHOW "message33"
		echo " "
		$SHOW "message34"
		echo $WHITE
		exit 0
	fi
	chmod 755 $LIBDIR/enigma2/python/Plugins/Extensions/BackupSuite/backupsuite.sh > /dev/null 2>&1
	$LIBDIR/enigma2/python/Plugins/Extensions/BackupSuite/backupsuite.sh "$TARGET" 
	sync
fi
