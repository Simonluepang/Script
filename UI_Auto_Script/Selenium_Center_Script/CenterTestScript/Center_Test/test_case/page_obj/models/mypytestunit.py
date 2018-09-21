#!/usr/bin/env python 
# -*- coding:utf-8 -*-
import pytest, PageFunction
from time import sleep
from selenium import webdriver

class myunit():

    @pytest.fixture(scope='function')
    def setup_teardown(self):
        ff = PageFunction.FunctionFactory('http://192.168.13.195:8989/dist/#/login', 'Luban Center', 'Page_login')
        ff.open()
        self.center_login(ff)
        yield
        ff.quit()
    def setup_function(function):
        print("start up!")

    def teardown(function):
        print("tear down !")

    def test_center_login(self):
        # ff = PageFunction.FunctionFactory('http://192.168.13.195:8989/dist/#/login', 'Luban Center', 'Page_login')
        # ff.open()
        messagelist = [('login_username', 'xushenwei'), ('login_password', '111111')]
        for element_name, value in messagelist:
            ff.RunSendKeys(element_name, value)
        for i in range(2):
            ff.RunClick('submit_login')
            sleep(1)
        if ff.RunHint('login_success_hint') == '徐莘伟的企业':
            print('login success!')
        else:
            raise Exception('login failed!')

# def setup_function(function):
#     print("start up!")
#
# def teardown(function):
#     print("tear down !")
#
# def test_center_login():
#     ff = PageFunction.FunctionFactory('http://192.168.13.195:8989/dist/#/login', 'Luban Center', 'Page_login')
#     ff.open()
#     messagelist = [('login_username', 'xushenwei'), ('login_password', '111111')]
#     for element_name, value in messagelist:
#         ff.RunSendKeys(element_name, value)
#     for i in range(2):
#         ff.RunClick('submit_login')
#         sleep(1)
#     if ff.RunHint('login_success_hint') == '徐莘伟的企业':
#         print('login success!')
#     else:
#         raise Exception('login failed!')

if __name__ == '__main__':
    pytest.main("-s mypytestunit.py")
    # pytest.main()