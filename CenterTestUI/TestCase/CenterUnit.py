#!/usr/bin/env python 
# -*- coding:utf-8 -*-
import Setting,random,string,unittest
from selenium import webdriver
from PageObject.page_Login_object import *

class CenterUnit(unittest.TestCase):

    def rdmstr(self,addName,digit):
        """
        生成随机字符串
        :param addName:
        :param digit:
        :return:
        """
        return addName + ''.join(random.sample(string.ascii_letters + string.digits, int(digit)))

    def _login(self,driver):
        """
        登录动作
        :param driver:
        :return:
        """
        login = Login(driver)
        login.open(Setting.Login_info['loginUrl'])
        login.inputUsername(Setting.Login_info['username'])
        login.inputPassword(Setting.Login_info['password'])
        login.submitLogin()
        try:
            hint_choose = login.hintChooseCompany()
            if hint_choose == '选择企业：':
                login.submitLogin()
        except:
            pass
        finally:
            assert login.hintLoginSuccess() == Setting.Login_info['companyName']
            print('成功登陆！')


    def setUp(self):

        self.driver = webdriver.Chrome()
        self._login(self.driver)

    def tearDown(self):
        return self.driver.quit()

if __name__ == '__main__':
    driver = webdriver.Chrome()
    CenterUnit()._login(driver)
    driver.quit()
