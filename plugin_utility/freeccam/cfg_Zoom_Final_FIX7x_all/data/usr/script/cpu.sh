#!/bin/sh
echo "CPU ????"
sleep 1
echo ""
echo ""

if [ -n "$(uname -m | grep armv7l)" ]; then
    echo ":Tvůj procesor je ARM ..."
    echo ":Your Device IS ARM processor ..."
    
elif [ -n "$(uname -m | grep aarch64)" ]; then
    echo ${FIN}
    echo ":Tvůj procesor je AARCH64 ..."
    echo ":Your Device IS AARCH64 processor ..."
    echo ${FIN}
   
elif [ -n "$(uname -m | grep mips)" ]; then
    echo ${FIN}
    echo ":Tvůj procesor je MIPS ..."
    echo ":Your Device IS MIPS processor ..."
    echo ${FIN}
  
elif [ -n "$(uname -m | grep 7401c0)" ]; then #dm800 clone
    echo ${FIN}
    echo ":Tvůj procesor je dm800 klon ..."
    echo ":Your Device IS dm800 clone processor ..."
    echo ${FIN}
fi

exit   