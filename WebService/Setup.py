#!/usr/bin/env python 
# -*- coding:utf-8 -*-
import sys
sys.path.append("..")
from Pubilc.LoginMyluban import *
from Setting import *

Cookie = loginweb()

with open(Path["cookieRoot"],"w") as f:
    f.write(Cookie)