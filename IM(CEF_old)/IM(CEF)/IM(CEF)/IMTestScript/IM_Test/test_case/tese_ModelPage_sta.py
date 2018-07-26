#!\usr\bin\env python
# -*- coding:utf-8 -*-
'''
Title: 测试用例
Description: 模板页面测试集
@author: Xushenwei
@update: 2018年7月11日
'''
from time import sleep
import unittest, random, sys, autoit, os
sys.path.append('page_obj/functions')
from page_obj.functions import myunit
from page_obj.ModelPage import *

"""
class TestSuite_Test(myunit.IMTest):
	'''此处对Suite进行简单描述'''
	def test1_TestCase(self):
		'''此处对Case进行简单描述'''
		PN = PageName(self.driver)
		# 添加动作
		PN.ElementName()
		PN.ElementName('Message')
		# 添加断言
		self.assertEqual(PN.ElementName_hint(), 'Verification')
"""

if __name__ == '__main__':

	myunit.unittest.main()

	# # 构造测试集
	# suite = unittest.TestSuite()
	# suite.addTest(TestSuite_Test("test1_TestCase"))
	# suite.addTest(TestSuite_Test(""))
	# suite.addTest(TestSuite_Test(""))
	# suite.addTest(TestSuite_Test(""))
	# suite.addTest(TestSuite_Test(""))
	# suite.addTest(TestSuite_Test(""))
	
	# # 执行测试
	# runner = unittest.TextTestRunner()
	# runner.run(suite)
