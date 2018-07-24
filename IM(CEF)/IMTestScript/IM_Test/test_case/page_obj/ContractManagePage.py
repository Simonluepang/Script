#!\usr\bin\env python
# -*- coding:utf-8 -*-
'''
Title: 页面元素:动作+验证
Description: 合同管理页面
@author: Xushenwei
@update: 2018年6月11日
'''
import threading
from selenium.webdriver.common.by import By 
from selenium import webdriver
from time import sleep

import driver as driver
import Base as Base
'''
#单独运行本文件的时候使用以下路径
import models.driver as driver
import models.Base as Base
''' 

class ContractManage(Base.Page):
	'''合同管理页面元素'''
	url = 'http://172.16.21.242:8082/im/resource/index.html#!/ld/contractManage'

	# Action
	#**===========================================================================**
	Maximize_Window_loc = (By.XPATH, '//*[@id="w-max"]')
	def Maximize_Window(self):
		'''最大化窗口'''
		self.find_element(*self.Maximize_Window_loc).click()

	ProjectManage_loc = (By.XPATH, '/html/body/div[1]/div[1]/header/div/div[2]/div/a[1]/i')
	def ProjectManage(self):
		'''工程管理'''
		self.find_element(*self.ProjectManage_loc).click()

	#**===========================================================================**

	ContractManage_loc = (By.XPATH, '/html/body/div[1]/div[1]/article/section/div[1]/a[1]/span')
	def ContractManage(self):
		'''合同管理'''
		self.find_element(*self.ContractManage_loc).click()

	ProjectDivisionContract_loc = (By.XPATH, '/html/body/div/div[1]/article/section/div[1]/a[2]/span')
	def ProjectDivisionContract(self):
		'''工程划分'''
		self.find_element(*self.ProjectDivisionContract_loc).click()

	ListManageContract_loc = (By.XPATH, '/html/body/div/div[1]/article/section/div[1]/a[3]/span')
	def ListManageContract(self):
		'''清单管理'''
		self.find_element(*self.ListManageContract_loc).click()

	#**===========================================================================**

	switch_ContractType_loc = (By.XPATH, '//*[@id="menu1"]/span[2]')
	def switch_ContractType(self):
		'''切换合同类型下拉框'''
		self.find_element(*self.switch_ContractType_loc).click()

	ConstructionContract_loc = (By.XPATH, '//*[@id="dropdown-menu1"]/li[1]/a')
	def ConstructionContract(self):
		'''施工合同'''
		self.find_element(*self.ConstructionContract_loc).click()

	SupervisionContract_loc = (By.XPATH, '//*[@id="dropdown-menu1"]/li[2]/a')#
	def SupervisionContract(self):
		'''监理合同'''
		self.find_element(*self.SupervisionContract_loc).click()

	#**===========================================================================**

	#施工合同元素列表：
	create_ConstructModal_loc = (By.XPATH, '//*[@id="createConstructModal"]')
	def create_ConstructModal(self):
		'''新增施工合同'''
		self.find_element(*self.create_ConstructModal_loc).click()

	edit_Contract_loc = (By.XPATH, '//*[@id="edit-contract"]')
	def edit_Contract(self):
		'''编辑合同'''
		self.find_element(*self.edit_Contract_loc).click()



	close_CreateorEditContract_loc = (By.XPATH, '//*[@id="modal-title"]/a/i')
	def close_CreateorEditContract(self):
		'''关闭新增编辑合同界面'''
		self.find_element(*self.close_CreateorEditContract_loc).click()

	LeftChange_loc = (By.XPATH, '//*[@id="modal-body"]/div[1]/div/div[1]/i')
	def LeftChange(self):
		'''向左切换上传附件列表'''
		self.find_element(*self.LeftChange_loc).click()

	RightChange_loc = (By.XPATH, '//*[@id="modal-body"]/div[1]/div/div[3]/i')
	def RightChange(self):
		'''向右切换上传附件列表'''
		self.find_element(*self.RightChange_loc).click()

	upload_Accessory_loc = (By.XPATH, '//*[@id="modal-body"]/div[1]/div/div[2]/element/input')
	# 此函数在前端中应该是个阻塞函数，故使用selenium点击的时候会出现程序不往下进行的问题。
	# 使用autoit暴力点击不会出现该问题。
	def upload_Accessory(self):
		'''上传附件'''
		self.find_element(*self.upload_Accessory_loc).click()

	def upload_Accessory_thread(self):
		'''线程实现上传附件'''
		# t1 = threading.Thread(target=ContractManage.upload_Accessory(self), name='upload_Accessory')
		print('pre')
		t1 = threading.Thread(target=self.find_element(*self.upload_Accessory_loc).click(), name='upload_Accessory')
		print('done')
		t1.start()

	ContractNum_loc = (By.XPATH, '//*[@id="contractNum"]')
	def ContractNum(self, message):
		'''合同编号'''
		self.find_element(*self.ContractNum_loc).send_keys(message)

	ContractAmount_loc = (By.XPATH, '//*[@id="contractAmount"]')
	def ContractAmount(self, message):
		'''合同金额'''
		self.find_element(*self.ContractAmount_loc).send_keys(message)

	ProvisionalSum_loc = (By.XPATH, '//*[@id="provisionalSum"]')
	def ProvisionalSum(self, message):
		'''暂列金额'''
		self.find_element(*self.ProvisionalSum_loc).send_keys(message)

	ConstructionUnit_loc = (By.XPATH, '//*[@id="constructionUnit"]')
	def ConstructionUnit(self, message):
		'''建设单位'''
		self.find_element(*self.ConstructionUnit_loc).send_keys(message)

	ExecutionUnit_loc = (By.XPATH, '//*[@id="executionUnit"]')
	def ExecutionUnit(self,message):
		'''施工单位'''
		self.find_element(*self.ExecutionUnit_loc).send_keys(message)

	ConstructionManager_loc = (By.XPATH, '//*[@id="constructionManager"]')
	def ConstructionManager(self, message):
		'''施工负责人'''
		self.find_element(*self.ConstructionManager_loc).send_keys(message)

	StartStakeMark_loc = (By.XPATH, '//*[@id="startStakeMark"]')
	def StartStakeMark(self, message):
		'''起始桩号'''
		self.find_element(*self.StartStakeMark_loc).send_keys(message)

	SectionLength_loc = (By.XPATH, '//*[@id="sectionLength"]')
	def SectionLength(self, message):
		'''合同段长度'''
		self.find_element(*self.SectionLength_loc).send_keys(message)

	PlanStartDate_loc = (By.XPATH, '//*[@id="planStartDate"]')
	def PlanStartDate(self, message):
		'''计划开工日期'''
		js = "document.getElementById('planStartDate').removeAttribute('readonly');"
		self.driver.execute_script(js)
		self.find_element(*self.PlanStartDate_loc).send_keys(message)
		self.find_element(*self.PlanStartDate_loc).click()

	ActualStartDate_loc = (By.XPATH, '//*[@id="actualStartDate"]')
	def ActualStartDate(self, message):
		'''实际开工日期'''
		js = "document.getElementById('actualStartDate').removeAttribute('readonly');"
		self.driver.execute_script(js)
		self.find_element(*self.ActualStartDate_loc).send_keys(message)
		self.find_element(*self.ActualStartDate_loc).click()

	Duration_loc = (By.XPATH, '//*[@id="duration"]')
	def Duration(self, message):
		'''工期'''
		self.find_element(*self.Duration_loc).send_keys(message)

	SectionNum_loc = (By.XPATH, '//*[@id="sectionNum"]')
	def SectionNum(self, message):
		'''标段号'''
		self.find_element(*self.SectionNum_loc).send_keys(message)

	ProjectName_loc = (By.XPATH, '//*[@id="projectName"]')
	def ProjectName(self, message):
		'''项目名称'''
		self.find_element(*self.ProjectName_loc).send_keys(message)

	ContractType_loc = (By.XPATH, '//*[@id="contract_type"]')
	def ContractType(self, message):
		'''合同类型'''
		self.find_element(*self.ContractType_loc).send_keys(message)

	SupervisionUnit_loc = (By.XPATH, '//*[@id="supervisionUnit"]')
	def SupervisionUnit(self, message):
		'''监理单位'''
		self.find_element(*self.SupervisionUnit_loc).send_keys(message)

	SupervisingEngineer_loc = (By.XPATH, '//*[@id="supervisingEngineer"]')
	def SupervisingEngineer(self, message):
		'''总监理工程师'''
		self.find_element(*self.SupervisingEngineer_loc).send_keys(message)

	ProjectChief_loc = (By.XPATH, '//*[@id="projectChief"]')
	def ProjectChief(self, message):
		'''项目总工'''
		self.find_element(*self.ProjectChief_loc).send_keys(message)

	EndStakeMark_loc = (By.XPATH, '//*[@id="endStakeMark"]')
	def EndStakeMark(self, message):
		'''结束桩号'''
		self.find_element(*self.EndStakeMark_loc).send_keys(message)

	ProjectCategory_loc = (By.XPATH, '//*[@id="modal-body"]/div[2]/form/div[2]/div[8]/div[2]/div/div/button')
	def ProjectCategory(self):
		'''工程类别'''
		self.find_element(*self.ProjectCategory_loc).click()

	PlanEndDate_loc = (By.ID, 'planEndDate')
	PlanEndDate_Label_loc = (By.XPATH, '//*[@id="modal-body"]/div[2]/form/div[2]/div[10]/div[1]/label')
	def PlanEndDate(self, message):
		'''计划完工日期'''
		js = "document.getElementById('planEndDate').removeAttribute('readonly');"
		self.driver.execute_script(js)
		self.find_element(*self.PlanEndDate_loc).send_keys(message)
		#self.find_element(*self.PlanEndDate_loc).click()

	ActualEndDate_loc = (By.XPATH, '//*[@id="actualEndDate"]')
	def ActualEndDate(self, message):
		'''实际完工日期'''
		js = "document.getElementById('actualEndDate').removeAttribute('readonly');"
		self.driver.execute_script(js)
		self.find_element(*self.ActualEndDate_loc).send_keys(message)
		#self.find_element(*self.ActualEndDate_loc).click()

	SignedDate_loc = (By.XPATH, '//*[@id="signedDate"]')
	def SignedDate(self, message):
		'''合同签订日期'''
		js = "document.getElementById('signedDate').removeAttribute('readonly');"
		self.driver.execute_script(js)
		self.find_element(*self.SignedDate_loc).send_keys(message)
		#self.find_element(*self.SignedDate_loc).click()

	#Contact_Project_loc = (By.XPATH, '')
	def contact_Project(self):
		'''关联工程'''
		pass

	save_Contract_loc = (By.XPATH, '/html/body/div[1]/div/div/div[1]/div[3]/div[1]/button')
	def save_Contract(self):
		'''保存工程'''
		self.find_element(*self.save_Contract_loc).click()

	cancel_save_Contract_loc = (By.XPATH, '/html/body/div[1]/div/div/div[1]/div[3]/div[2]/button')
	def cancel_save_Contract(self):
		'''取消保存工程'''
		self.find_element(*self.cancel_save_Contract_loc).click()

	#**===========================================================================**

	delete_Contract_loc = (By.XPATH, '//*[@id="delete-contract"]')
	def delete_Contract(self):
		'''删除合同'''
		self.find_element(*self.delete_Contract_loc).click()

	Chose_FirstProjectManagement_loc = (By.XPATH, '//*[@id="firstLeftTree"]/li[1]/a')
	def Chose_FirstProjectManagement(self):
		'''选择第一个项目部'''
		self.find_element(*self.Chose_FirstProjectManagement_loc).click()

	Chose_FirstContract_loc = (By.XPATH, '//*[@id="contract_1011"]')
	def Chose_FirstContract(self):
		'''选择第一个合同'''
		self.find_element(*self.Chose_FirstContract_loc).click()

	Enter_DeleteContract_loc = (By.CLASS_NAME, 'layui-layer-btn0')
	def Enter_DeleteContract(self):
		'''确定删除合同'''
		self.find_element(*self.Enter_DeleteContract_loc).click()

	Cancel_DeleteContrat_loc = (By.CLASS_NAME, 'layui-layer-btn1')
	def Cancel_DeleteContrat(self):
		'''取消删除合同'''
		self.find_element(*self.Cancel_DeleteContrat_loc).click()

	# Verification
	ContractName_hint_loc = (By.XPATH, '//*[@id="construct"]/span')
	def ContractName_hint(self):
		'''验证合同名称'''
		return self.find_element(*self.ContractName_hint_loc).text


if __name__ == '__main__':

	selenium_driver =driver.browser()
	CM = ContractManage(selenium_driver)
	CM.create_ConstructModal()
	sleep(3)
	CM.quit()
