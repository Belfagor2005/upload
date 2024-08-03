/usr/script/tichestartX.sh >/dev/null 2>&1 </dev/null &
sleep 1
echo ""
echo "začal som neviditeľné sťahovanie"
echo "nenechajte sa rušiť"
echo "ja budem sťahovať ďalej ......"
echo "výsledok budem postupne ticho ukladať"
echo "prajem príjemné sledovanie TV !!!"
echo ""
sleep 2
/usr/script/exit.sh  >>/dev/null 2>&1 </dev/null &
cp /usr/script/upozor.sh /tmp/upozor.sh >>/dev/null 2>&1 </dev/null &
chmod 755 /tmp/upozor.sh >>/dev/null 2>&1 </dev/null &
exit 