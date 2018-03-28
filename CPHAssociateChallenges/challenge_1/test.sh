#!/bin/bash

echo "it worked"

device0="/bootstrap.sh"    # /   (root directory)
if [ -b "$device0" ]
then
  echo "$device0 is a block device."
fi