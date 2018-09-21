#! python3
# -*- coding:utf-8 -*-
'''
Title: 质检计量系统合同管理功能测试
Description: 新增施工合同、编辑合同、删除合同、快速搜索合同相关功能测试
@author: Xushenwei
@update: 2017年12月25日
'''
import unittest,os,time

def now():
	"""返回当前时间"""
	return time.strftime("%Y-%m-%d %H:%M:%S")

def setUpModule():
    print("test module start >>>>>>>>>>>" + now())
    
def tearDownModule():
    print("test module end >>>>>>>>>>>" + now())


class TestCaseIMCM(unittest.TestCase):

	def test_contract_management(self):
		"""模拟合同新增、编辑、删除，以及其他基本操作"""

		# 启动BECivil
		os.system(r"E:\TestAutomation\IM_test\autoit\BEcivil\main.exe")
		# 启动IM
		os.system(r"E:\TestAutomation\IM_test\autoit\BEcivil\IM\runIM.exe")
		# 合同管理中的新建、编辑和删除
		os.system(r"E:\TestAutomation\IM_test\autoit\BEcivil\IM\工程管理\合同管理\CreatContractManagement.exe")
		os.system(r"E:\TestAutomation\IM_test\autoit\BEcivil\IM\工程管理\合同管理\EditContractManagement.exe")
		os.system(r"E:\TestAutomation\IM_test\autoit\BEcivil\IM\工程管理\合同管理\DeleteContractManagement.exe")

		


unittest.main()
