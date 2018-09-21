#!\usr\bin\env python
# -*- coding:utf-8 -*-
# Title: 测试用例
# Description: 合同管理页面
# @author: Xushenwei
# @update: 2018年7月1日
# @editor:

import random, string, unittest
from time import sleep

from Selenium_Center_Script.CenterTestScript.Center_Test.test_case.page_obj.models.PageFunction import FunctionFactory
from Selenium_Center_Script.CenterTestScript.Center_Test.test_case.page_obj.models.myunit import CenterTest


class ConfigurationTest(CenterTest):
	'''应用配置流程测试'''

	def test1_datacatalog_flow(self):
		'''资料目录相关流程'''
		FF = FunctionFactory(self.driver, 'Page_configuration')
		message = "测试" + ''.join(random.sample(string.ascii_letters + string.digits, 4))
		click_list = ["configuration", "common", "data_catalog", "add_folder", "success_add_folder",
		 "search_folder", "edit_folder", "success_edit_folder", "delete_folder_box", "delete_folder", "success_delete"]
		for Function_Name in click_list:
			FF.RunClick(Function_Name)
			sleep(1.3)
			if Function_Name == "add_folder":
				"""添加文件夹"""
				FF.RunSendKeys("add_folder_name", message)
			elif Function_Name == "success_add_folder":
				FF.RunSendKeys('search_folder_name', message)
			elif Function_Name == "search_folder":
				"""搜索文件夹"""
				# 验证文件夹是否添加成功
				self.assertEqual(FF.RunHint('new_folder_name_hint'), message)
			elif Function_Name == "edit_folder":
				"""修改文件夹"""
				ed_message = message + 'edit'
				FF.RunSendKeys('edit_folder_name', ed_message)
			elif Function_Name == "success_edit_folder":
				# 验证文件夹是否修改成功
				self.assertEqual(FF.RunHint('new_folder_name_hint'), message+'edit')
			elif Function_Name == "success_delete_folder":
				'''删除文件夹'''
				# 验证文件夹是否删除成功
				self.assertEqual(FF.RunHint('success_delete_folder_hint'), '暂无数据')

	def test2_labelmanagement_flow(self):
		'''标签管理相关流程'''
		FF = FunctionFactory(self.driver, 'Page_configuration')
		click_list = ["configuration", "common", "label_management", "add_label", "success_add_label", 
		"search_label", "edit_label", "success_edit_label", "delete_label_box", "delete_label", "success_delete"]
		message = "测试" + ''.join(random.sample(string.ascii_letters + string.digits, 4))
		for Function_Name in click_list:
			FF.RunClick(Function_Name)
			sleep(1.3)
			if Function_Name == "add_label":
				"""添加标签"""
				FF.RunSendKeys('add_label_name', message)
			elif Function_Name == "success_add_label":
				"""搜索标签"""
				FF.RunSendKeys('search_label_name', message)
			elif Function_Name == "search_label":
				# 验证标签是否添加成功
				self.assertEqual(FF.RunHint('new_label_name_hint'), message)
			elif Function_Name == "edit_label":
				"""修改标签"""
				ed_message = message + 'edit'
				FF.RunSendKeys('edit_label_name', ed_message)
			elif Function_Name == "success_edit_label":
				# 验证标签是否修改成功
				self.assertEqual(FF.RunHint('new_label_name_hint'), message+'edit')
			elif Function_Name == "success_delete_label":
				"""删除标签"""
				# 验证标签是否删除成功
				self.assertEqual(FF.RunHint('label_hint'), '暂无数据')

	def test3_formmanagement_flow(self):
		'''表单管理相关流程'''
		FF = FunctionFactory(self.driver, 'Page_configuration')
		click_list = ["configuration", "common", "form_management", "add_form", "upload_templatefile", 
		"success_add_form", "edit_form", "success_edit_form", "delete_form_box", "delete_form", "success_delete"]
		message = "测试" + ''.join(random.sample(string.ascii_letters + string.digits, 4))
		for Function_Name in click_list:
			FF.RunClick(Function_Name)
			sleep(1.3)
			if Function_Name == "upload_templatefile":
				FF.addfile('打开', 'uploadfile_1.doc')
			elif Function_Name == 'success_add_form':
				# 验证表单模板是否上传成功
				self.assertEqual(FF.RunHint('form_hint'), 'uploadfile_1')
			elif Function_Name == "edit_form":
				FF.RunSendKeys('edit_template_name', message)
			elif Function_Name == "success_edit_form":
				# 验证表单模板修改名称是否成功
				self.assertEqual(FF.RunHint('form_hint'), message)
			elif Function_Name == "success_delete_form":
				# 验证表单模板删除是否成功
				self.assertEqual(FF.RunHint('success_delete_form_hint'), '暂无数据')

		

if __name__ == '__main__':
	CenterTest.main()

	# 构造测试集
	'''
	suite = unittest.TestSuite()
	suite.addTest(ConfigurationTest("test1_datacatalog_flow"))
	suite.addTest(ConfigurationTest("test2_labelmanagement_flow"))
	suite.addTest(ConfigurationTest("test3_formmanagement_flow"))
	
	suite.addTest(NormalFlowTest(""))
	suite.addTest(NormalFlowTest(""))
	suite.addTest(NormalFlowTest(""))
	suite.addTest(NormalFlowTest(""))
	

	# 执行测试
	runner = unittest.TextTestRunner()
	runner.run(suite)
	'''