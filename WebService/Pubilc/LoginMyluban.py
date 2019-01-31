#!/usr/bin/env python 
# -*- coding:utf-8 -*-
from Pubilc.Interface import  *
from Pubilc.RequestParam import *
from Setting import *

def loginweb():
    param = req_login_controller().rest_login(Config['user'], Config['pwd'])
    result = login().rest_login(url, **param)
    return result.headers['Set-Cookie'][0:46]

if __name__ == "__main__":
    result = loginweb()
    print(result)