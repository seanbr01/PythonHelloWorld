#!/bin/bash

if [ ! -e /127.0.0.1/info.php ]; then
    echo "File not found!"
else
	echo "Found!"
fi