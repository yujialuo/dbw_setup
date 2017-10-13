# BDD Software Environment Setup in Linux

## Overview
Following the installation guide below, you will be able to set up a docker environment in Linux with the following frameworks:

* ROS Kinetic (http://wiki.ros.org/kinetic)
* dbw_mkz_ros (https://bitbucket.org/DataspeedInc/dbw_mkz_ros)
* dashboard (https://github.com/Jmq14/ROS_car_dashboard)

## Installation Guide

1. Download Repository
```shell
git clone https://github.com/yujialuo/BDD-Env-Setup.git
```

2. Install Docker (Optional)
```shell
./setup_docker.sh
```

3. Build Docker
```shell
./docker-build.sh
```

4. Relocate Data (Optional)
```shell
If you want to use driving data in the docker, put them in directory bdd_env_setup/data/
```

5. Run Docker
```shell
./docker-compose.sh
```

** Note: make sure to make the shell scripts execuble before running them, e.g.
```shell
chmod +x ./setup_docker.sh
```