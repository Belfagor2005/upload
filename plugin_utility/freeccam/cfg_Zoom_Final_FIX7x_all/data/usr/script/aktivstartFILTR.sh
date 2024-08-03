#!/bin/sh
echo "Nastavuji FILTR"
echo "pro funkci ...stažení všech serverů"
echo ""
echo ""
sed -i '/startF/d' /usr/script/tichestart1.sh
sleep 1
sed -i '/exit/d' /usr/script/tichestart1.sh
echo "" >> /usr/script/tichestart1.sh
echo "/usr/script/startF.sh" >> /usr/script/tichestart1.sh
echo "" >> /usr/script/tichestart1.sh
echo "exit " >> /usr/script/tichestart1.sh
echo ""
echo ""
sed -i '/startF/d' /usr/script/tichestartX.sh
sleep 1
sed -i '/exit/d' /usr/script/tichestartX.sh
echo "" >> /usr/script/tichestartX.sh
echo "/usr/script/startF.sh" >> /usr/script/tichestartX.sh
echo "" >> /usr/script/tichestartX.sh
echo "exit " >> /usr/script/tichestartX.sh
echo ""
sleep 1
echo "hotovo..."


sed -i '/exit/d' /usr/script/INFO/cz.sh
sed -i '/exit/d' /usr/script/INFO/cz1.sh
sed -i '/exit/d' /usr/script/INFO/de.sh
sed -i '/exit/d' /usr/script/INFO/de1.sh
sed -i '/exit/d' /usr/script/INFO/en.sh
sed -i '/exit/d' /usr/script/INFO/en1.sh
sed -i '/exit/d' /usr/script/INFO/gr.sh
sed -i '/exit/d' /usr/script/INFO/gr1.sh
sed -i '/exit/d' /usr/script/INFO/pl.sh
sed -i '/exit/d' /usr/script/INFO/pl1.sh
sed -i '/exit/d' /usr/script/INFO/ru.sh
sed -i '/exit/d' /usr/script/INFO/ru1.sh
sed -i '/exit/d' /usr/script/INFO/sl.sh
sed -i '/exit/d' /usr/script/INFO/sl1.sh
sed -i '/exit/d' /usr/script/INFO/tu.sh
sed -i '/exit/d' /usr/script/INFO/tu1.sh

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

echo "" >> /usr/script/INFO/cz.sh
echo "" >> /usr/script/INFO/cz1.sh
echo "" >> /usr/script/INFO/de.sh
echo "" >> /usr/script/INFO/de1.sh
echo "" >> /usr/script/INFO/en.sh
echo "" >> /usr/script/INFO/en1.sh
echo "" >> /usr/script/INFO/gr.sh
echo "" >> /usr/script/INFO/gr1.sh
echo "" >> /usr/script/INFO/pl.sh
echo "" >> /usr/script/INFO/pl1.sh
echo "" >> /usr/script/INFO/ru.sh
echo "" >> /usr/script/INFO/ru1.sh
echo "" >> /usr/script/INFO/sl.sh
echo "" >> /usr/script/INFO/sl1.sh
echo "" >> /usr/script/INFO/tu.sh
echo "" >> /usr/script/INFO/tu1.sh

for i in 1 2 3 4 5 6 7 8 9 10
do
echo "echo '*************************'" >> /usr/script/INFO/cz.sh
echo "echo '*************************'" >> /usr/script/INFO/cz1.sh
echo "echo '*************************'" >> /usr/script/INFO/de.sh
echo "echo '*************************'" >> /usr/script/INFO/de1.sh
echo "echo '*************************'" >> /usr/script/INFO/en.sh
echo "echo '*************************'" >> /usr/script/INFO/en1.sh
echo "echo '*************************'" >> /usr/script/INFO/gr.sh
echo "echo '*************************'" >> /usr/script/INFO/gr1.sh
echo "echo '*************************'" >> /usr/script/INFO/pl.sh
echo "echo '*************************'" >> /usr/script/INFO/pl1.sh
echo "echo '*************************'" >> /usr/script/INFO/ru.sh
echo "echo '*************************'" >> /usr/script/INFO/ru1.sh
echo "echo '*************************'" >> /usr/script/INFO/sl.sh
echo "echo '*************************'" >> /usr/script/INFO/sl1.sh
echo "echo '*************************'" >> /usr/script/INFO/tu.sh
echo "echo '*************************'" >> /usr/script/INFO/tu1.sh
done

echo "echo ''" >> /usr/script/INFO/cz.sh
echo "echo ''" >> /usr/script/INFO/cz1.sh
echo "echo ''" >> /usr/script/INFO/de.sh
echo "echo ''" >> /usr/script/INFO/de1.sh
echo "echo ''" >> /usr/script/INFO/en.sh
echo "echo ''" >> /usr/script/INFO/en1.sh
echo "echo ''" >> /usr/script/INFO/gr.sh
echo "echo ''" >> /usr/script/INFO/gr1.sh
echo "echo ''" >> /usr/script/INFO/pl.sh
echo "echo ''" >> /usr/script/INFO/pl1.sh
echo "echo ''" >> /usr/script/INFO/ru.sh
echo "echo ''" >> /usr/script/INFO/ru1.sh
echo "echo ''" >> /usr/script/INFO/sl.sh
echo "echo ''" >> /usr/script/INFO/sl1.sh
echo "echo ''" >> /usr/script/INFO/tu.sh
echo "echo ''" >> /usr/script/INFO/tu1.sh

echo "sleep 3" >> /usr/script/INFO/cz.sh
echo "sleep 3" >> /usr/script/INFO/cz1.sh
echo "sleep 3" >> /usr/script/INFO/de.sh
echo "sleep 3" >> /usr/script/INFO/de1.sh
echo "sleep 3" >> /usr/script/INFO/en.sh
echo "sleep 3" >> /usr/script/INFO/en1.sh
echo "sleep 3" >> /usr/script/INFO/gr.sh
echo "sleep 3" >> /usr/script/INFO/gr1.sh
echo "sleep 3" >> /usr/script/INFO/pl.sh
echo "sleep 3" >> /usr/script/INFO/pl1.sh
echo "sleep 3" >> /usr/script/INFO/ru.sh
echo "sleep 3" >> /usr/script/INFO/ru1.sh
echo "sleep 3" >> /usr/script/INFO/sl.sh
echo "sleep 3" >> /usr/script/INFO/sl1.sh
echo "sleep 3" >> /usr/script/INFO/tu.sh
echo "sleep 3" >> /usr/script/INFO/tu1.sh

echo "echo 'FILTR ...ON'" >> /usr/script/INFO/cz.sh
echo "echo 'FILTR ...ON'" >> /usr/script/INFO/cz1.sh
echo "echo 'FILTR ...ON'" >> /usr/script/INFO/de.sh
echo "echo 'FILTR ...ON'" >> /usr/script/INFO/de1.sh
echo "echo 'FILTR ...ON'" >> /usr/script/INFO/en.sh
echo "echo 'FILTR ...ON'" >> /usr/script/INFO/en1.sh
echo "echo 'FILTR ...ON'" >> /usr/script/INFO/gr.sh
echo "echo 'FILTR ...ON'" >> /usr/script/INFO/gr1.sh
echo "echo 'FILTR ...ON'" >> /usr/script/INFO/pl.sh
echo "echo 'FILTR ...ON'" >> /usr/script/INFO/pl1.sh
echo "echo 'FILTR ...ON'" >> /usr/script/INFO/ru.sh
echo "echo 'FILTR ...ON'" >> /usr/script/INFO/ru1.sh
echo "echo 'FILTR ...ON'" >> /usr/script/INFO/sl.sh
echo "echo 'FILTR ...ON'" >> /usr/script/INFO/sl1.sh
echo "echo 'FILTR ...ON'" >> /usr/script/INFO/tu.sh
echo "echo 'FILTR ...ON'" >> /usr/script/INFO/tu1.sh

echo "sleep 3" >> /usr/script/INFO/cz.sh
echo "sleep 3" >> /usr/script/INFO/cz1.sh
echo "sleep 3" >> /usr/script/INFO/de.sh
echo "sleep 3" >> /usr/script/INFO/de1.sh
echo "sleep 3" >> /usr/script/INFO/en.sh
echo "sleep 3" >> /usr/script/INFO/en1.sh
echo "sleep 3" >> /usr/script/INFO/gr.sh
echo "sleep 3" >> /usr/script/INFO/gr1.sh
echo "sleep 3" >> /usr/script/INFO/pl.sh
echo "sleep 3" >> /usr/script/INFO/pl1.sh
echo "sleep 3" >> /usr/script/INFO/ru.sh
echo "sleep 3" >> /usr/script/INFO/ru1.sh
echo "sleep 3" >> /usr/script/INFO/sl.sh
echo "sleep 3" >> /usr/script/INFO/sl1.sh
echo "sleep 3" >> /usr/script/INFO/tu.sh
echo "sleep 3" >> /usr/script/INFO/tu1.sh

echo "/usr/script/exit.sh  >>/dev/null 2>&1 </dev/null &"  >> /usr/script/INFO/cz.sh
echo "/usr/script/exit.sh  >>/dev/null 2>&1 </dev/null &"  >> /usr/script/INFO/cz1.sh
echo "/usr/script/exit.sh  >>/dev/null 2>&1 </dev/null &"  >> /usr/script/INFO/de.sh
echo "/usr/script/exit.sh  >>/dev/null 2>&1 </dev/null &"  >> /usr/script/INFO/de1.sh
echo "/usr/script/exit.sh  >>/dev/null 2>&1 </dev/null &"  >> /usr/script/INFO/en.sh
echo "/usr/script/exit.sh  >>/dev/null 2>&1 </dev/null &"  >> /usr/script/INFO/en1.sh
echo "/usr/script/exit.sh  >>/dev/null 2>&1 </dev/null &"  >> /usr/script/INFO/gr.sh
echo "/usr/script/exit.sh  >>/dev/null 2>&1 </dev/null &"  >> /usr/script/INFO/gr1.sh
echo "/usr/script/exit.sh  >>/dev/null 2>&1 </dev/null &"  >> /usr/script/INFO/pl.sh
echo "/usr/script/exit.sh  >>/dev/null 2>&1 </dev/null &"  >> /usr/script/INFO/pl1.sh
echo "/usr/script/exit.sh  >>/dev/null 2>&1 </dev/null &"  >> /usr/script/INFO/ru.sh
echo "/usr/script/exit.sh  >>/dev/null 2>&1 </dev/null &"  >> /usr/script/INFO/ru1.sh
echo "/usr/script/exit.sh  >>/dev/null 2>&1 </dev/null &"  >> /usr/script/INFO/sl.sh
echo "/usr/script/exit.sh  >>/dev/null 2>&1 </dev/null &"  >> /usr/script/INFO/sl1.sh
echo "/usr/script/exit.sh  >>/dev/null 2>&1 </dev/null &"  >> /usr/script/INFO/tu.sh
echo "/usr/script/exit.sh  >>/dev/null 2>&1 </dev/null &"  >> /usr/script/INFO/tu1.sh

echo "exit" >> /usr/script/INFO/cz.sh
echo "exit" >> /usr/script/INFO/cz1.sh
echo "exit" >> /usr/script/INFO/de.sh
echo "exit" >> /usr/script/INFO/de1.sh
echo "exit" >> /usr/script/INFO/en.sh
echo "exit" >> /usr/script/INFO/en1.sh
echo "exit" >> /usr/script/INFO/gr.sh
echo "exit" >> /usr/script/INFO/gr1.sh
echo "exit" >> /usr/script/INFO/pl.sh
echo "exit" >> /usr/script/INFO/pl1.sh
echo "exit" >> /usr/script/INFO/ru.sh
echo "exit" >> /usr/script/INFO/ru1.sh
echo "exit" >> /usr/script/INFO/sl.sh
echo "exit" >> /usr/script/INFO/sl1.sh
echo "exit" >> /usr/script/INFO/tu.sh
echo "exit" >> /usr/script/INFO/tu1.sh

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


exit


