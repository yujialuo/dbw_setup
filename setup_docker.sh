#!/usr/bin/env bash

# Install Docker
sudo usermod -aG docker $(whoami)
curl -fsSL get.docker.com -o get-docker.sh
sh get-docker.sh
