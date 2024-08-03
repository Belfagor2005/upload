
#!/bin/sh
echo "************************************************************"
echo "*                                                          *"
echo "*   *       *    * * * * *  *              *    * *        *"
echo "*   *      *     *            *           *   *     *      *"
echo "*   *     *      *              *        *   *       *     *"
echo "*   *   *        *               *      *    *             *"
echo "*   * *          *                 *   *     *             *"
echo "*   *   *        * ***               *         *           *"
echo "*	  *    *       *                   *           *         *"
echo "*	  *      *     *                   *              *      *"
echo "*   *       *    *                   *      *        *     *"
echo "*   *        *   *                   *       *      *      *"
echo "*	  *         *  * * * * *           *         *  *        *"
echo "*                                                          *"
echo "************************************************************"
echo "Downloading Oscam keys : SoftCam.Org Team"
echo "Checking the key folder..."
echo ""
[ -d /usr/keys ] || mkdir -p /usr/keys
[ -d /var/tuxbox/config ] || mkdir -p /var/tuxbox/config
echo ""
echo "Processing...."
echo ""
rm -rf /usr/keys/oscam.keys
rm -rf /var/tuxbox/config/oscam.keys
wget -O /usr/keys/oscam.keys http://www.SoftCam.Org/deneme6.php?file=oscam.keys
cp /usr/keys/oscam.keys /var/tuxbox/config/oscam.keys 
chmod 644 /usr/keys/oscam.keys
chmod 644 /var/tuxbox/config/oscam.keys
echo ""
echo "keys updates completed successfully."
echo ""
sleep 1
cp /var/keys/oscam.keys /tmp/key1.txt
more /tmp/key1.txt
echo ""
rm -rf /tmp/key1.txt
sleep 2
echo ""
echo ""
echo ""
echo ""
echo ""


echo "Downloading CCcam keys : SoftCam.Org Team"
echo ""
echo "Checking the key folder..."
echo ""

echo "Processing...."
echo ""
rm -rf /usr/keys/constant.cw
rm -rf /usr/keys/SoftCam.Key
rm -rf /usr/keys/AutoRoll.Key
wget -O /usr/keys/constant.cw http://www.softcam.org/deneme6.php?file=constant.cw
cp /usr/keys/constant.cw /tmp/key1.txt
more /tmp/key1.txt
echo ""
rm -rf /tmp/key1.txt
sleep 1
wget -O /usr/keys/SoftCam.Key http://www.softcam.org/deneme6.php?file=SoftCam.Key
cp /usr/keys/SoftCam.Key /tmp/key2.txt
more /tmp/key2.txt
echo ""
rm -rf /tmp/key2.txt
sleep 1
wget -O /usr/keys/AutoRoll.Key http://www.softcam.org/deneme6.php?file=AutoRoll.Key
cp /usr/keys/AutoRoll.Key /tmp/key3.txt
more /tmp/key3.txt
echo ""
rm -rf /tmp/key3.txt
sleep 1
chmod 644 /usr/keys/constant.cw
chmod 644 /usr/keys/SoftCam.Key
chmod 644 /usr/keys/AutoRoll.Key
echo ""
echo "keys updates completed successfully."
echo ""
echo ""
echo ""
echo ""
echo ""
sleep 2
exit