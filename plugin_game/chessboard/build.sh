#!/bin/sh

cd meta
version=$(grep Version control|cut -d " " -f 2)
package=$(grep Package control|cut -d " " -f 2)
mkdir -p usr/lib/enigma2/python/Plugins/Extensions/ChessBoard
cp -r ../src/* usr/lib/enigma2/python/Plugins/Extensions/ChessBoard

for po in $(find ../locale -name *.po ); do
    lang=$(basename $po .po)
    mkdir -p usr/lib/enigma2/python/Plugins/Extensions/ChessBoard/locale/${lang%}/LC_MESSAGES/
    msgfmt -o usr/lib/enigma2/python/Plugins/Extensions/ChessBoard/locale/${lang%}/LC_MESSAGES/ChessBoard.mo ../locale/$lang.po
done

tar -cvzf data.tar.gz usr
tar -cvzf control.tar.gz control

[ -d ../dist ] || mkdir ../dist

rm -f ../dist/${package}_${version}_all.ipk
ar -r ../dist/${package}_${version}_all.ipk debian-binary control.tar.gz data.tar.gz

rm -fr control.tar.gz data.tar.gz usr
