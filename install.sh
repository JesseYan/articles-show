#!/usr/bin/env bash
# mac
sudo easy_install virtualenv

# Ubuntu
# sudo apt-get install python-virtualenv

virtualenv venv

venv/bin/pip install requirements.txt

