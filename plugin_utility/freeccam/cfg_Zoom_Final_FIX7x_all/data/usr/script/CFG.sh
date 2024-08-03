#!/bin/sh
if [ -e "/usr/keys/CCcam.cfg" ]; then
cp /etc/CCcam.cfg /usr/keys/CCcam.cfg
rm -rf /etc/CCcam.cfg
fi
exit



