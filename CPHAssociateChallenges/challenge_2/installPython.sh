#!/bin/bash
echo "Installing Python"
wget http://python.org/ftp/python/3.6.3/Python-3.6.3.tar.xz --no-check-certificate
tar xf Python-3.6.3.tar.xz
cd Python-3.6.3
./configure --prefix=/usr/local --enable-shared LDFLAGS="-Wl,-rpath /usr/local/lib"
make && make altinstall
echo "Installing pip, setuptools and wheel"
wget https://bootstrap.pypa.io/get-pip.py --no-check-certificate