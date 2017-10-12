#!/usr/bin/env bash

docker run -v /dev:/dev -v /etc/udev/rules.d:/dbw_ws/src/dataspeed_can/dataspeed_can_usb/udev/90-DataspeedUsbCanToolRules.rules -it bdd/dbw_mkz_ros bash