/usr/script/tichestart1.sh >/dev/null 2>&1 </dev/null &
sleep 1
echo ""
echo "I started an invisible download"
echo "don't be disturbed"
echo "I'll continue downloading ......"
echo "I will gradually save the result quietly"
echo "I wish you a pleasant TV watching !!!"
echo ""
sleep 2
/usr/script/exit.sh  >>/dev/null 2>&1 </dev/null &
cp /usr/script/upozor.sh /tmp/upozor.sh >>/dev/null 2>&1 </dev/null &
chmod 755 /tmp/upozor.sh >>/dev/null 2>&1 </dev/null &
exit 