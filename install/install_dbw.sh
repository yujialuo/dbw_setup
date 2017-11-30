#!/bin/bash

removeOld = 
if [ -d ~/dbw_ws ]
  then
    echo "Removing old install and reinstalling"
    rm -rf ~/dbw_ws
  else
    echo "Starting new install"
fi

mkdir -p /home/bdd/dbw_ws/src && cd /home/bdd/dbw_ws && wstool init src
wstool merge -t src https://bitbucket.org/DataspeedInc/dbw_mkz_ros/raw/default/dbw_mkz.rosinstall

wstool update -t src
rosdep update && rosdep install --from-paths src --ignore-src

sudo cp /home/bdd/dbw_ws/src/dataspeed_can/dataspeed_can_usb/90-DataspeedUsbCanToolRules.rules /etc/udev/rules.d/
sudo udevadm control --reload-rules && sudo service udev restart && sudo udevadm trigger

catkin_make -DCMAKE_BUILD_TYPE=Release


