#!\usr\bin\env python
# -*- coding:utf-8 -*-
'''
Title: 测试用例
Description: 合同管理页面
@author: Xushenwei
@update: 2018年7月1日
'''
from time import sleep
import unittest, random, sys, autoit, threading, os
sys.path.append('page_obj/models')
from page_obj.models import myunit
from page_obj.ContractManagePage import *

def addfile():
	'''上传附件流程'''
	autoit.mouse_click(x=630, y=255)
	sleep(3)
	if autoit.win_exists('打开文件'):
		autoit.win_active('打开文件')
		autoit.mouse_click(x=780, y=50)
		path = os.path.dirname(__file__)
		npos = 'IMTestScript'
		APPLICATION_PATH = myunit.common_path(path=path, npos=npos) + r'IMTestScript\IM_Test\data\uploadfile'
		autoit.send(APPLICATION_PATH)
		autoit.send('{ENTER}')
		autoit.mouse_click(x=780, y=970)
		autoit.send('uploadfile_1.txt')
		autoit.send('!o')
		sleep(2)
	else:
		raise Exception('没有打开文件窗口')	


class NormalFlowTest(myunit.IMTest):
	'''正常流程相关测试'''
	def test1_creatnormal_flow(self):
		'''添加合同正常流程'''
		CM = ContractManage(self.driver)
		clicklist = (CM.Maximize_Window,CM.ProjectManage, CM.ContractManage, 
		CM.switch_ContractType, CM.ConstructionContract, CM.create_ConstructModal, )
		for i in clicklist:
			i()
			sleep(1)
		addfile()
		addlist = (
		CM.ContractNum('1111'), CM.ContractAmount('2222'), CM.ProvisionalSum('3333'), 
		CM.ConstructionUnit('测试建设单位'),CM.ExecutionUnit('测试施工单位'), CM.ConstructionManager('测试施工负责人'), 
		CM.StartStakeMark('4444'), CM.SectionLength('5555'), CM.Duration('6666'),CM.SectionNum('7777'), 
		CM.ProjectName('测试项目名称'), CM.SupervisionUnit('测试监理单位'), CM.EndStakeMark('8888'),
		CM.PlanStartDate('2018-06-20'), CM.ActualStartDate('2018-06-20'), CM.PlanEndDate('2018-06-22'), 
		CM.ActualEndDate('2018-06-22'), CM.SignedDate('2018-06-23'), CM.save_Contract(),)
		for i in addlist:
			i
		sleep(10)
		self.assertEqual(CM.ContractName_hint(), '7777')

	def test2_editcontract_flow(self):
		'''编辑合同'''
		CM = ContractManage(self.driver)
		clicklist = (CM.ProjectManage, CM.ContractManage, CM.switch_ContractType, 
		CM.ConstructionContract, CM.edit_Contract,)
		for i in clicklist:
			i()
			sleep(1)
		edit_list = (CM.SupervisingEngineer('测试总监理工程师'), CM.ProjectChief('测试项目总工'), CM.save_Contract(),)
		for i in edit_list:
			i
		sleep(1)
		# Verification is here.


	def test3_deletenormal_flow(self):
		'''删除合同正常流程'''
		CM = ContractManage(self.driver)
		clicklist = (CM.Maximize_Window, CM.delete_Contract, CM.Enter_DeleteContract,)
		for i in clicklist:
			i()
			sleep(2)
		self.assertEqual(CM.ContractName_hint(), '合同段')



if __name__ == '__main__':

	myunit.unittest.main()
	'''
	# 构造测试集
	suite = unittest.TestSuite()
	suite.addTest(NormalFlowTest("test1_creatnormal_flow"))
	
	# suite.addTest(NormalFlowTest("test2_editcontract_flow"))
	# suite.addTest(NormalFlowTest("test3_deletenormal_flow"))
	suite.addTest(CatalogTest(""))
	suite.addTest(CatalogTest(""))
	suite.addTest(CatalogTest(""))
	
	# 执行测试
	runner = unittest.TextTestRunner()
	runner.run(suite)
	'''
