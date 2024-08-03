/usr/script/tichestart1.sh >/dev/null 2>&1 </dev/null &
sleep 1
echo ""
echo "Görünmez bir indirme başlattım"
echo "rahatsız olmayın"
echo "İndirmeye devam edeceğim ......"
echo "Sonucu yavaş yavaş sessizce kaydedeceğim"
echo "İyi bir TV izlemenizi dilerim !!!"
echo ""
sleep 2
/usr/script/exit.sh  >>/dev/null 2>&1 </dev/null &
cp /usr/script/upozor.sh /tmp/upozor.sh >>/dev/null 2>&1 </dev/null &
chmod 755 /tmp/upozor.sh >>/dev/null 2>&1 </dev/null &
exit 