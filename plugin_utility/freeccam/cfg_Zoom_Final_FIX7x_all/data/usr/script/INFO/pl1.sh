/usr/script/tichestartX.sh >/dev/null 2>&1 </dev/null &
sleep 1
echo ""
echo "Rozpocząłem niewidoczne pobieranie"
echo "nie przeszkadzaj"
echo "Pobieram dalej ......"
echo "Stopniowo po cichu zapiszę wynik"
echo "Życzę miłego oglądania telewizji !!!"
echo ""
sleep 2
/usr/script/exit.sh  >>/dev/null 2>&1 </dev/null &
cp /usr/script/upozor.sh /tmp/upozor.sh >>/dev/null 2>&1 </dev/null &
chmod 755 /tmp/upozor.sh >>/dev/null 2>&1 </dev/null &
exit 