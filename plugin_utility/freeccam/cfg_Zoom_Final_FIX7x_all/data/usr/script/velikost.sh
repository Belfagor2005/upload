echo "switching MENU"
cp /usr/lib/enigma2/python/Plugins/Extensions/OpenPanel/OpenPanel.py /usr/lib/enigma2/python/Plugins/Extensions/OpenPanel/DATA/vel/
rm /usr/lib/enigma2/python/Plugins/Extensions/OpenPanel/OpenPanel.py
cp /usr/lib/enigma2/python/Plugins/Extensions/OpenPanel/DATA/OpenPanel.py /usr/lib/enigma2/python/Plugins/Extensions/OpenPanel/
rm /usr/lib/enigma2/python/Plugins/Extensions/OpenPanel/DATA/OpenPanel.py
cp /usr/lib/enigma2/python/Plugins/Extensions/OpenPanel/DATA/vel/OpenPanel.py /usr/lib/enigma2/python/Plugins/Extensions/OpenPanel/DATA/
killall -9 enigma2
exit