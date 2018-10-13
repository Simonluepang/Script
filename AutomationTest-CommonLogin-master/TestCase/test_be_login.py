#coding=utf-8
import sys
sys.path.append('..')
from public.interface import *
from public.Assertion import *
from public.CommonLogin import *

#获得be_cookie
be_cookie = read_txt(headFilePath, be_cookie_name, splitSymbol)

class Test_login:

    def test_address_serviceAddress(self):
        resp = address().serviceAddress(be_url,be_cookie,'message')
        assert_status_code(resp["status_code"])
        serverURL = resp['return']['serverURL']
        assert 'http' in serverURL,'url 格式不正确或不存在%s'%serverURL


