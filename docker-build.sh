#!/usr/bin/env bash

# Install Docker
# sudo usermod -aG docker $(whoami)
# curl -fsSL get.docker.com -o get-docker.sh
# sh get-docker.sh

# Intall Ros
mkdir -p ./etc/udev/rules.d/
cp /etc/udev/rules.d/* ./etc/udev/rules.d/
sudo docker build -t bdd/dbw_mkz_ros -f RosDockerfile .