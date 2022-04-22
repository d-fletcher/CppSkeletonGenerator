#!/bin/bash

if [ "$EUID" -ne 0 ]
  then echo "Run as root. ie sudo ./install.sh"
  exit
fi

chmod +x ./gen_cpp.py
cp gen_cpp.py /usr/bin/gen_cpp
mkdir -p /usr/local/bin/gen_cpp
cp sample.cc /usr/local/bin/gen_cpp/sample.cc
