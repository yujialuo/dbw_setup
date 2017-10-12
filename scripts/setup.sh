#!/usr/bin/env bash

## dbw_mkz_ros

# Set up workspace
mkdir -p /dbw_ws/src
cd /dbw_ws
wstool init src
wstool merge -t src https://bitbucket.org/DataspeedInc/dbw_mkz_ros/raw/default/dbw_mkz.rosinstall

# Update workspace and resolve dependencies
wstool update -t src
sudo rosdep init
rosdep update
rosdep install --from-paths src --ignore-src --rosdistro kinetic -y -r

# Install udev rules
sudo apt-get install -y udev
sudo udevadm control --reload-rules
sudo service udev restart
sudo udevadm trigger

# Build workspace
catkin_make -DCMAKE_BUILD_TYPE=Release

# Source the workspace
/bin/bash -c "source /dbw_ws/devel/setup.bash"


## Dashboard
apt-cache search pyqt
sudo apt-get install -y python-qt4

cd src
git clone git@github.com:Jmq14/ROS_car_dashboard.git
mv ROS_car_dashboard monitor

# build
cd ../
catkin_make
/bin/bash -c "source devel/setup.bash"