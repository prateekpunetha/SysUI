#!/usr/bin/env bash

sudo apt update

sudo apt install python3 python3-pip \
	python-is-python3 python3-tk zenity gnupg htop -y

echo "Installing requirements..."
pip3 install -r requirements.txt
echo done!
