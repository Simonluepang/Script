#!\usr\bin\env python
# -*- coding:utf-8 -*-
'''
Title: 页面元素:动作+验证
Description: 模板页面元素提取
@author: Xushenwei
@update: 2018年7月11日
'''
from selenium.webdriver.common.by import By 
from selenium import webdriver
from time import sleep
import driver as driver
import Base as Base

class PageName(Base.Page):
	'''合同管理页面元素'''
	url = 'url'
	# Action
	ElementName_loc = (By.XPATH, 'xpath')
	def ElementName(self):
		'''元素点击动作'''
		self.find_element(*self.ElementName_loc).click()

	ElementName_loc = (By.XPATH, 'xpath')
	def ElementName(self, message):
		'''元素输入动作'''
		self.find_element(*self.ElementName_loc).send_keys(message)

	# Verification
	ElementName_hint_loc = (By.XPATH, 'xpath')
	def ElementName_hint(self):
		'''验证元素'''
		return self.find_element(*self.ElementName_hint_loc).text
