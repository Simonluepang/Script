#!\usr\bin\env python
# -*- coding:utf-8 -*-
# Title:
# Description:
# @author:
# @update:
# @editor:

import random, string
from time import sleep
from page_obj.models import Base
from page_obj.models import myunit
from page_obj.models import PageFunction_XML

class CompanyprofileTest(myunit.CenterTest):
	'''企业概况流程测试'''

	def test1_organization_structure_flow(self):
		'''组织结构相关流程'''
		controlled_company_name = "分公司" + ''.join(random.sample(string.ascii_letters + string.digits, 4))
		project_department_name = "项目部" + ''.join(random.sample(string.ascii_letters + string.digits, 4))
		click_list = ["company_profile", "organization_structure", "company_name", "add_controlled_company_name", 
		"save_controlled_company", "choose_controlled_company", "add_project_department", "save_project_department", 
		"choose_project_department","edit_project_department", "save_project_department", "choose_project_department", 
		"delete_project_department", "enter_delete_project_department", "choose_controlled_company", "edit_controlled_company", 
		"enter_edit_controlled_company", "choose_controlled_company", "delete_controlled_company", "enter_delete_controlled_company"]
		project_department_message_list = [("project_name", ""), ("project_manager", ""), ("phone_number", ""), ("covered area", ""), 
		]