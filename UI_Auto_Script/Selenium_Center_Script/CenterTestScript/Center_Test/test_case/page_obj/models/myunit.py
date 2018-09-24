#!\usr\bin\env python
# -*- coding:utf-8 -*-
'''
Title: 继承unittest
Description: 初始化测试框架
@author: Xushenwei
@update: 2018年6月11日
@editor:
'''
import unittest
from time import sleep
from selenium import webdriver
from Script.UI_Auto_Script.Selenium_Center_Script.CenterTestScript.Center_Test.test_case.page_obj.models.PageFunction import \
    FunctionFactory


class CenterTest(unittest.TestCase):
    """初始化测试框架"""

    # def Center_login(self):
        #     """center登录流程"""
        #     self.driver.maximize_window()
        #     self.driver.get("http://center.lubansoft.com/#/login")
        #     self.driver.find_element_by_xpath('//*[@id="username"]/input').send_keys("徐莘伟")
        #     self.driver.find_element_by_xpath('//*[@id="password"]/input').send_keys("123456")
        #     self.driver.find_element_by_xpath('//*[@id="app"]/div/div/div[2]/div[2]/div[2]/form/div[4]/button').click()
        #     try:
        #         text = WebDriverWait(self.driver, 1, 0.5).until(expected_conditions.visibility_of_element_located((By.CLASS_NAME, "el-form-item__label"))).text
        #         if text == "选择企业：":
        #             self.driver.find_element_by_xpath('//*[@id="app"]/div/div/div[2]/div[2]/div[2]/form/div[4]/button').click()
        #     except:
        #         pass

    def Center_login(self, driver):
        login = FunctionFactory(driver, 'Page_login_css')
        login.open('http://192.168.13.195:8989/dist/#/login', 'Luban Center')
        messagelist = [('login_username', 'xushenwei'), ('login_password', '111111')]
        for element_name, value in messagelist:
            login.RunSendKeys(element_name, value)
        for i in range(2):
            login.RunClick('submit_login')
            sleep(1)
        if login.RunHint('login_success_hint') == '徐莘伟的企业':
            pass
            # print('login success!')
        else:
            raise Exception('login failed!')

    def setUp(self):
        self.driver = webdriver.Chrome()
        self.Center_login(self.driver)
        
    def tearDown(self):
        self.driver.quit()
        sleep(1)

if __name__ == "__main__":

    MLT = CenterTest()
    MLT.setUp()
    MLT.tearDown()
    # unittest.main()