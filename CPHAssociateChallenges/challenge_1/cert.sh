#!/bin/bash
sudo yum install mod_ssl openssl -y

# Generate private key 
sudo openssl genrsa -out server.key 4096
sudo openssl req -new -key server.key -out server.csr
sudo openssl x509 -req -days 368 -in server.csr -signkey server.key -out server.crt

sudo openssl rsa -in server.key -out server.key.insecure
sudo mv server.key server.key.secure
sudo mv server.key.insecure server.key

sudo cp server.key /etc/httpd/conf/server.key/127.0.0.1:8080/index.php/key
sudo cp server.key /etc/httpd/conf/server.crt/https://127.0.0.1:8443/index.php
sudo cp server.key /etc/httpd/conf/server.csr/https://127.0.0.1:8443/index.php