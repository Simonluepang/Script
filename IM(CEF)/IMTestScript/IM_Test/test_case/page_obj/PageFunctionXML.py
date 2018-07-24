#!\usr\bin\env python
# -*- coding:utf-8 -*-
'''
Title: 页面元素:动作+验证
Description: 合同管理页面
@author: Xushenwei
@update: 2018年6月11日
'''
import os
from selenium.webdriver.common.by import By 
from selenium import webdriver
from time import sleep
import xml.dom.minidom as xmlParser
''' 
import Base as Base
'''
#单独运行本文件的时候使用以下路径
import models.Base as Base

class ElementClass:
	'''获取配置文件中的信息'''
	def __init__(self, function_name, xpath, class_name):
		self.function_name = function_name
		self.xpath = xpath
		self.class_name = class_name

	def get_function_name(self):
		return self.function_name

	def get_xpath(self):
		return self.xpath

	def get_class_name(self):
		return self.class_name

def ReadXMlData(xmlPath, parent):
	'''读取配置文件中的信息，并返回每个项为一个(name,path,classname)的列表'''
	dom = xmlParser.parse(xmlPath)
	db = dom.documentElement
	data_list = []
	itemlist = db.getElementsByTagName(parent)
	for item in itemlist:
		it = ElementClass(item.getAttribute('Function_name'), item.getAttribute('Xpath'), item.getAttribute('Class_name'))
		data_list.append(it)
	return data_list

class MakeFunction(Base.Page):
	'''创建元素操作方法'''
	def make_function_click_by_xpath(self, xpath):
		def fcbx():
			self.find_element(By.XPATH, xpath).click()
		return fcbx

	def make_function_click_by_class_name(self, class_name):
		def fc():
			self.find_element(By.CLASS_NAME, class_name).click()
		return fcbcn

	def make_function_send_Keys(self,xpath):
		def fsk(message):
			self.find_element(By.XPATH, xpath).send_keys(message)
		return fsk

	def make_function_time_widget(self,xpath):
		def ftw(id_name, message):
			self.driver.execute_script("document.getElementById(%s).removeAttribute('readonly');" % id_name)
			self.find_element(By.XPATH, xpath).send_keys(message)
		return ftw

	def make_function_hint(self, xpath):
		def fh():
			return self.find_element(By.XPATH, xpath).text
		return fh

class FunctionFactory():
	'''功能工厂'''
	def __init__(self, driver, xmlpath):
		self.FuncMap = {}
		listclick = ReadXMlData(xmlpath, "FUNCTION_CLICK_XPATH")
		#初始化点击事件，并保存在FuncMap中
		for list1 in listclick:
			self.FuncMap[list1.get_function_name()] = MakeFunction(driver).make_function_click_by_xpath(list1.get_xpath())

		listclickbyclassname = ReadXMlData(xmlpath, "FUNCTION_CLICK_CLASS_NAME")
		#初始化点击事件，并保存在FuncMap中
		for list1 in listclickbyclassname:
			self.FuncMap[list1.get_function_name()] = MakeFunction(driver).make_function_click_by_class_name(list1.get_class_name())

		#初始化信息输入事件，并保存在FuncMap中
		listsSend = ReadXMlData(xmlpath, "FUNCTION_SEND")
		for list1 in listsSend:
			self.FuncMap[list1.get_function_name()] = MakeFunction(driver).make_function_send_Keys(list1.get_xpath())

		#初始化时间控件事件，并保存在FuncMap中
		listTimeWidget = ReadXMlData(xmlpath, "FUNCTION_TIME_WDIGET")
		for list1 in listTimeWidget:
			self.FuncMap[list1.get_function_name()] = MakeFunction(driver).make_function_time_widget(list1.get_xpath())

		#初始化元素验证事件，并保存在FuncMap中
		listHint = ReadXMlData(xmlpath, "FUNCTION_HINT")
		for list1 in listHint:
		 	self.FuncMap[list1.get_function_name()] = MakeFunction(driver).make_function_hint(list1.get_xpath())
	
	def RunClick(self, funcname):
		'''运行点击事件'''
		element = self.FuncMap.get(funcname)
		element()

	def RunSendKeys(self, funcname, message):
		'''运行信息输入事件'''
		element = self.FuncMap.get(funcname)
		element(message)

	def RunTimeWidget(self, funcname, id_name, message):
		'''运行时间控件事件'''
		element = self.FuncMap.get(funcname)
		element(id_name, message)

	def RunHint(self, funcname):
		'''运行验证事件'''
		element = self.FuncMap.get(funcname)
		element()



if __name__ == "__main__":
	selenium_driver =Base.browser()
	FunctionFactory  = FunctionFactory(selenium_driver,'Element.xml' )
	FunctionFactory.RunClick('Maximize_Window')
	sleep(3)
	selenium_driver.quit()
