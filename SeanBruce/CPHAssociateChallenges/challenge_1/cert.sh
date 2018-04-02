#!/bin/bash
sudo yum update -y
sudo yum install yum-utils -y
sudo yum groupinstall development -y
sudo yum install -y zlib-devel bzip2-devel openssl-devel ncurses-devel sqlite-devel readline-devel tk-devel gdbm-devel db4-devel libpcap-devel xz-devel expat-devel
sudo yum install -y wget