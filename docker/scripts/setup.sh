#!/usr/bin/env bash

# Install udev rules
# mkdir -p /etc/udev/rules.d
# cp /dbw_ws/src/dataspeed_can/dataspeed_can_usb/udev/90-DataspeedUsbCanToolRules.rules /etc/udev/rules.d/
# apt-get install -y udev
# udevadm control --reload-rules
# service udev restart
# udevadm trigger

# build
cd /dbw_ws
catkin_make
/bin/bash -c "source devel/setup.bash"