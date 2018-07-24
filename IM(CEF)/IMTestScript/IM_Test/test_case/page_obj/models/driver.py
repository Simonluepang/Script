#!\usr\bin\env python
# -*- coding:utf-8 -*-
'''
Title: 浏览器driver设置
Description: 拼接软件exe的地址与在本地电脑的路径地址
@author: Xushenwei
@update: 2018年6月11日
'''
import os
import sys
from selenium import webdriver

def common_path(path, npos):
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
	return driver

if __name__ == '__main__':
	
	dr = browser()
	handles = dr.window_handles
	dr.switch_to.window(handles[-1])
	print(dr.page_source)
	dr.quit()
