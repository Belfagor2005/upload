#!/bin/sh
echo "Ruším FILTR"
echo "pro funkci ...stažení všech serverů"
echo "OFF"
echo ""
sed -i '/startF/d' /usr/script/tichestart1.sh
sleep 1
sed -i '/exit/d' /usr/script/tichestart1.sh
echo "" >> /usr/script/tichestart1.sh
echo "exit " >> /usr/script/tichestart1.sh
echo ""
echo ""
sed -i '/startF/d' /usr/script/tichestartX.sh
sleep 1
sed -i '/exit/d' /usr/script/tichestartX.sh
echo "" >> /usr/script/tichestartX.sh
echo "exit " >> /usr/script/tichestartX.sh
echo ""
sed -i '/FILTR ...ON/d' /usr/script/INFO/cz.sh
sed -i '/FILTR ...ON/d' /usr/script/INFO/cz1.sh
sed -i '/FILTR ...ON/d' /usr/script/INFO/de.sh
sed -i '/FILTR ...ON/d' /usr/script/INFO/de1.sh
sed -i '/FILTR ...ON/d' /usr/script/INFO/en.sh
sed -i '/FILTR ...ON/d' /usr/script/INFO/en1.sh
sed -i '/FILTR ...ON/d' /usr/script/INFO/gr.sh
sed -i '/FILTR ...ON/d' /usr/script/INFO/gr1.sh
sed -i '/FILTR ...ON/d' /usr/script/INFO/pl.sh
sed -i '/FILTR ...ON/d' /usr/script/INFO/pl1.sh
sed -i '/FILTR ...ON/d' /usr/script/INFO/ru.sh
sed -i '/FILTR ...ON/d' /usr/script/INFO/ru1.sh
sed -i '/FILTR ...ON/d' /usr/script/INFO/sl.sh
sed -i '/FILTR ...ON/d' /usr/script/INFO/sl1.sh
sed -i '/FILTR ...ON/d' /usr/script/INFO/tu.sh
sed -i '/FILTR ...ON/d' /usr/script/INFO/tu1.sh

sed -i '/*/d' /usr/script/INFO/cz.sh
sed -i '/*/d' /usr/script/INFO/cz1.sh
sed -i '/*/d' /usr/script/INFO/de.sh
sed -i '/*/d' /usr/script/INFO/de1.sh
sed -i '/*/d' /usr/script/INFO/en.sh
sed -i '/*/d' /usr/script/INFO/en1.sh
sed -i '/*/d' /usr/script/INFO/gr.sh
sed -i '/*/d' /usr/script/INFO/gr1.sh
sed -i '/*/d' /usr/script/INFO/pl.sh
sed -i '/*/d' /usr/script/INFO/pl1.sh
sed -i '/*/d' /usr/script/INFO/ru.sh
sed -i '/*/d' /usr/script/INFO/ru1.sh
sed -i '/*/d' /usr/script/INFO/sl.sh
sed -i '/*/d' /usr/script/INFO/sl1.sh
sed -i '/*/d' /usr/script/INFO/tu.sh
sed -i '/*/d' /usr/script/INFO/tu1.sh

sed -i "/'/d" /usr/script/INFO/cz.sh
sed -i "/'/d" /usr/script/INFO/cz1.sh
sed -i "/'/d" /usr/script/INFO/de.sh
sed -i "/'/d" /usr/script/INFO/de1.sh
sed -i "/'/d" /usr/script/INFO/en.sh
sed -i "/'/d" /usr/script/INFO/en1.sh
sed -i "/'/d" /usr/script/INFO/gr.sh
sed -i "/'/d" /usr/script/INFO/gr1.sh
sed -i "/'/d" /usr/script/INFO/pl.sh
sed -i "/'/d" /usr/script/INFO/pl1.sh
sed -i "/'/d" /usr/script/INFO/ru.sh
sed -i "/'/d" /usr/script/INFO/ru1.sh
sed -i "/'/d" /usr/script/INFO/sl.sh
sed -i "/'/d" /usr/script/INFO/sl1.sh
sed -i "/'/d" /usr/script/INFO/tu.sh
sed -i "/'/d" /usr/script/INFO/tu1.sh

sed -i '/3/d' /usr/script/INFO/cz.sh
sed -i '/3/d' /usr/script/INFO/cz1.sh
sed -i '/3/d' /usr/script/INFO/de.sh
sed -i '/3/d' /usr/script/INFO/de1.sh
sed -i '/3/d' /usr/script/INFO/en.sh
sed -i '/3/d' /usr/script/INFO/en1.sh
sed -i '/3/d' /usr/script/INFO/gr.sh
sed -i '/3/d' /usr/script/INFO/gr1.sh
sed -i '/3/d' /usr/script/INFO/pl.sh
sed -i '/3/d' /usr/script/INFO/pl1.sh
sed -i '/3/d' /usr/script/INFO/ru.sh
sed -i '/3/d' /usr/script/INFO/ru1.sh
sed -i '/3/d' /usr/script/INFO/sl.sh
sed -i '/3/d' /usr/script/INFO/sl1.sh
sed -i '/3/d' /usr/script/INFO/tu.sh
sed -i '/3/d' /usr/script/INFO/tu1.sh
sleep 1
sed -i -E '/^(#|$)/d' /usr/script/INFO/cz.sh
sed -i -E '/^(#|$)/d' /usr/script/INFO/cz1.sh
sed -i -E '/^(#|$)/d' /usr/script/INFO/de.sh
sed -i -E '/^(#|$)/d' /usr/script/INFO/de1.sh
sed -i -E '/^(#|$)/d' /usr/script/INFO/en.sh
sed -i -E '/^(#|$)/d' /usr/script/INFO/en1.sh
sed -i -E '/^(#|$)/d' /usr/script/INFO/gr.sh
sed -i -E '/^(#|$)/d' /usr/script/INFO/gr1.sh
sed -i -E '/^(#|$)/d' /usr/script/INFO/pl.sh
sed -i -E '/^(#|$)/d' /usr/script/INFO/pl1.sh
sed -i -E '/^(#|$)/d' /usr/script/INFO/ru.sh
sed -i -E '/^(#|$)/d' /usr/script/INFO/ru1.sh
sed -i -E '/^(#|$)/d' /usr/script/INFO/sl.sh
sed -i -E '/^(#|$)/d' /usr/script/INFO/sl1.sh
sed -i -E '/^(#|$)/d' /usr/script/INFO/tu.sh
sed -i -E '/^(#|$)/d' /usr/script/INFO/tu1.sh
echo ""
echo "hotovo..."

exit
