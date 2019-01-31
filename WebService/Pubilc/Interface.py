#!/usr/bin/env python 
# -*- coding:utf-8 -*-
import sys,os
sys.path.append('..')
from Pubilc.WebRequest import Webrequests
from Pubilc.ResponseRecombition import *
from Setting import *

Webrequests = Webrequests()

url = Config['mainUrl']

try:
    open(Path["cookieRoot"], 'r')
except:
    open(Path["cookieRoot"], 'w')

token = open(Path["cookieRoot"], 'r').readline()

def headers():
    headers = {
        "Cookie": token
    }
    return headers

def headers_application_json():
    headers = {
        "Cookie": token,
        "Content-type": "application/json"
    }
    return headers

class login:
    def rest_login(self, url, **kwargs):
        url = url + "/rest/login?"
        return Webrequests.post_json(url, kwargs, headers_application_json())
