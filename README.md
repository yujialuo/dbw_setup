# BDD Software Environment Setup in Linux

## Overview
Following the installation guide below, you will be able to set up a docker environment in Linux with the following frameworks:

* ROS Kinetic (http://wiki.ros.org/kinetic)
* dbw_mkz_ros (https://bitbucket.org/DataspeedInc/dbw_mkz_ros)
* dashboard (https://github.com/yujialuo/BDD-Env-Setup)

## Installation Guide

1. Download Repository
```
git clone https://github.com/yujialuo/BDD-Env-Setup.git
```
2. Install Docker (Optional)
```
./setup_docker.sh
```
3. Build Docker
```
./docker-build.sh
```
4. Run Docker
```
./docker-compose.sh
```

** Note: make sure to make the shell scripts execuble before running them, e.g.
```
chmod +x ./setup_docker.sh
```