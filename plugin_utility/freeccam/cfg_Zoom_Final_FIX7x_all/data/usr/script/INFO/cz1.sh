/usr/script/tichestartX.sh >/dev/null 2>&1 </dev/null &
sleep 1
echo ""
echo "zahájil jsem neviditelné stahování"
echo "nenechte se rušit"
echo "já budu stahovat dál......"
echo "výsledek budu postupně tiše ukládat"
echo "přeji příjemné sledování TV!!!"
echo ""
sleep 2
/usr/script/exit.sh  >>/dev/null 2>&1 </dev/null &
cp /usr/script/upozor.sh /tmp/upozor.sh >>/dev/null 2>&1 </dev/null &
chmod 755 /tmp/upozor.sh >>/dev/null 2>&1 </dev/null &
exit 