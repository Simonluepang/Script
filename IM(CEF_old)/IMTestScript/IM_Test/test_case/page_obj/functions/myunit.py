#!\usr\bin\env python
# -*- coding:utf-8 -*-
'''
Title: 继承unittest
Description: 设置setup和teardown
@author: Xushenwei
@update: 2018年6月11日
'''
import os, unittest
from selenium import webdriver

def common_path(path, npos):
    '''拼装相对位置组成绝对位置'''
    n1 = path.find(npos)
    BASE_DIR = path[0:n1]
    return BASE_DIR

def browser():
    path = os.path.dirname(__file__)
    npos = 'IMTestScript'
    APPLICATION_PATH = common_path(path=path, npos=npos) + r'IMTestScript\Client\x64_vc11_unicode_release\BimIM.exe'
    options = webdriver.ChromeOptions()
    options.binary_location = APPLICATION_PATH
    driver = webdriver.Chrome (chrome_options=options)
    handles = driver.window_handles
    driver.switch_to.window(handles[-1])
    os.popen('TASKKILL/F /IM ZY.Downloader.exe')
    return driver

class IMTest(unittest.TestCase):
    """质检计量初始化与清理程序"""

    def setUp(self):
        self.driver = browser()
        self.driver.implicitly_wait(10)
        
    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":

    IMT = IMTest()
    IMT.setUp()
    IMT.tearDown()
    # unittest.main()