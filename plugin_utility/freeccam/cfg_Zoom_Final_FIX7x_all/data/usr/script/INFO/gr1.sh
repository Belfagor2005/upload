/usr/script/tichestartX.sh >/dev/null 2>&1 </dev/null &
sleep 1
echo ""
echo "Ξεκίνησα μια αόρατη λήψη"
echo "μην ενοχλείς"
echo "Θα συνεχίσω τη λήψη ......"
echo "Θα αποθηκεύσω σταδιακά το αποτέλεσμα ήσυχα"
echo "Σας εύχομαι μια ευχάριστη παρακολούθηση τηλεόρασης !!!"
echo ""
sleep 2
/usr/script/exit.sh  >>/dev/null 2>&1 </dev/null &
cp /usr/script/upozor.sh /tmp/upozor.sh >>/dev/null 2>&1 </dev/null &
chmod 755 /tmp/upozor.sh >>/dev/null 2>&1 </dev/null &
exit 