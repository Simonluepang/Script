from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
# import sys
# sys.path.append('..')
from Base import Page
from time import sleep
from selenium import webdriver
from selenium.webdriver.common.keys import Keys


class OrganizationStructure(Page):
	'''组织结构'''

	url = '/'

	# Action

	company_profile_loc = (By.XPATH, '//*[@id="app"]/div/div[2]/ul/li[1]')

	def company_profile(self):
		self.find_element(*company_profile_loc).click()

	organization_structure_loc = (By.XPATH, '//*[@id="app"]/div/div[3]/div/div[1]/ul/li[1]')

	def organization_structure(self):
		self.find_element(*organization_structure_loc).click()

	expand_all_loc = (By.XPATH, '//*[@id="app"]/div/div[3]/div/div[2]/div/div[1]/button[1]')

	pack_up_all_loc = (By.XPATH, '//*[@id="app"]/div/div[3]/div/div[2]/div/div[1]/button[2]')

	def expand_all(self):
		self.find_element(*self.expand_all_loc).click()

	def pack_up_all(self):
		self.find_element(*self.pack_up_all_loc).click()
	#***************************************************************************************

	pick_company_loc = (By.XPATH, '//*[@id="root-name"]')

	add_organization_loc = (By.XPATH, '//*[@id="app"]/div/div[3]/div/div[2]/div/div[1]/div/div/div[3]/div/button[1]')

	input_filiale_name_loc = (By.XPATH, '//*[@id="app"]/div/div[3]/div/div[2]/div/div[3]/div/div[2]/form/div/div[1]/div/div/input')

	save_filiale_name_loc = (By.XPATH, '//*[@id="app"]/div/div[3]/div/div[2]/div/div[3]/div/div[2]/form/div/div[2]/button[1]')

	cancel_filiale_name_loc = (By.XPATH, '//*[@id="app"]/div/div[3]/div/div[2]/div/div[3]/div/div[2]/form/div/div[2]/button[2]')

	def pick_company(self):
		self.find_element(*self.pick_company_loc).click()

	def add_organization(self):
		self.find_element(*self.add_organization_loc).click()

	def input_filiale_name(self, filiale_name):
		self.find_element(*self.input_filiale_name_loc).send_keys(filiale_name)

	def save_filiale_name(self):
		self.find_element(*self.save_filiale_name_loc).click()

	def cancel_filiale_name(self):
		self.find_element(*self.cancel_filiale_name_loc).click()
	#***************************************************************************************

	pick_filiale_loc = (By.XPATH, '//*[@id="ztree-2_1_a"]')

	add_filiale_organization_loc = (By.XPATH, '//*[@id="app"]/div/div[3]/div/div[2]/div/div[1]/div/div/div[3]/div/button[1]')

	delete_filiale_loc = (By.XPATH, '//*[@id="app"]/div/div[3]/div/div[2]/div/div[1]/div/div/div[3]/div/button[3]')

	enter_delete_filiale_loc = (By.XPATH, '/html/body/div[8]/div/div[3]/button[2]')

	cancel_delete_filiale_loc = (By.XPATH, '/html/body/div[8]/div/div[3]/button[1]')

	edit_filiale_loc = (By.XPATH, '//*[@id="app"]/div/div[3]/div/div[2]/div/div[1]/div/div/div[3]/div/button[4]')

	input_edit_filiale_name_loc = (By.XPATH, '//*[@id="app"]/div/div[3]/div/div[2]/div/div[4]/div/div[2]/form/div/div/div/div/input')

	enter_edit_filiale_name_loc = (By.XPATH, '//*[@id="app"]/div/div[3]/div/div[2]/div/div[4]/div/div[3]/div/button[1]')

	cancel_delete_filiale_name_loc = (By.XPATH, '//*[@id="app"]/div/div[3]/div/div[2]/div/div[4]/div/div[3]/div/button[2]')

	def pick_filiale(self):
		self.find_element(*self.pick_filiale_loc).click()

	def add_filiale_organization(self):
		self.find_element(*self.add_filiale_organization_loc).click()

	def delete_filiale(self):
		self.find_element(*self.delete_filiale_loc).click()

	def enter_delete_filiale(self):
		self.find_element(*self.enter_delete_filiale_loc).click()

	def cancel_delete_filiale(self):
		self.find_element(*self.cancel_delete_filiale_loc).click()

	def edit_filiale(self):
		self.find_element(*self.edit_filiale_loc).click()

	def input_edit_filiale_name(self, filiale_name):
		self.find_element(*self.input_edit_filiale_name_loc).send_keys(filiale_name)

	def enter_edit_filiale_name(self):
		self.find_element(*self.enter_edit_filiale_name_loc).click()

	def cancel_delete_filiale_name(self):
		self.find_element(*self.cancel_delete_filiale_name_loc).click()

	#***************************************************************************************

	add_filiale_project_department_loc = (By.XPATH, '//*[@id="app"]/div/div[3]/div/div[2]/div/div[1]/div/div/div[3]/div/button[2]')

	add_project_name_loc = (By.XPATH, '//*[@id="app"]/div/div[3]/div/div[2]/div/div[4]/div/div[2]/form/div/div[1]/div[1]/div/div/input')

	add_project_manager_name_loc = (By.XPATH, '//*[@id="app"]/div/div[3]/div/div[2]/div/div[4]/div/div[2]/form/div/div[1]/div[2]/div/div/input')

	add_mobliephone_number_loc = (By.XPATH, '//*[@id="app"]/div/div[3]/div/div[2]/div/div[4]/div/div[2]/form/div/div[1]/div[3]/div/div/input')

	add_commencement_date_loc = (By.XPATH, '//*[@id="app"]/div/div[3]/div/div[2]/div/div[4]/div/div[2]/form/div/div[1]/div[4]/div/div/div/div/input')
	
	add_completion_date_loc = (By.XPATH, '//*[@id="app"]/div/div[3]/div/div[2]/div/div[4]/div/div[2]/form/div/div[1]/div[5]/div/div/div/div/input')

	add_structure_area_loc = (By.XPATH, '//*[@id="app"]/div/div[3]/div/div[2]/div/div[4]/div/div[2]/form/div/div[1]/div[6]/div/div/input')

	add_mileage_loc = (By.XPATH, '//*[@id="app"]/div/div[3]/div/div[2]/div/div[4]/div/div[2]/form/div/div[2]/div[1]/div/div/input')

	add_location_loc = (By.XPATH, '//*[@id="provinLink"]')

	add_location_province_Beijing_loc = (By.XPATH, '//*[@id="_citys0"]/a[1]')
	
	add_location_city_Beijing_loc = (By.XPATH, '//*[@id="_citys1"]/a')

	add_location_county_Dongchengqu_loc = (By.XPATH, '//*[@id="_citys2"]/a[1]')

	add_contract_type_loc = (By.XPATH, '//*[@id="app"]/div/div[3]/div/div[2]/div/div[4]/div/div[2]/form/div/div[2]/div[3]/div/div/div[1]/input')

	add_lump_sum_contract_loc = (By.XPATH, '/html/body/div[9]/div/div[1]/ul/li[2]')

	add_status_loc = (By.XPATH, '//*[@id="app"]/div/div[3]/div/div[2]/div/div[4]/div/div[2]/form/div/div[2]/div[4]/div/div/div[1]/input')

	add_not_in_service_loc = (By.XPATH, '/html/body/div[9]/div/div[1]/ul/li[1]')

	add_remark_loc = (By.XPATH, '//*[@id="app"]/div/div[3]/div/div[2]/div/div[4]/div/div[2]/form/div/div[2]/div[5]/div/div/textarea')

	save_add_project_department_loc = (By.XPATH, '//*[@id="app"]/div/div[3]/div/div[2]/div/div[4]/div/div[3]/div/button[1]')

	cancel_add_porject_department_loc = (By.XPATH, '//*[@id="app"]/div/div[3]/div/div[2]/div/div[4]/div/div[3]/div/button[2]')

	def add_filiale_project_department(self):
		self.find_element(*self.add_filiale_project_department_loc).click()

	def add_project_name(self, project_name):
		self.find_element(*self.add_project_name_loc).send_keys(project_name)

	def add_project_manager_name(self, project_manager_name):
		self.find_element(*self.add_project_manager_name_loc).send_keys(project_manager_name)

	def add_mobliephone_number(self, mobilephone_number):
		self.find_element(*self.add_mobliephone_number_loc).send_keys(mobilephone_number)

	def add_commencement_date(self, commencement_date):
		self.find_element(*self.add_commencement_date_loc).send_keys(commencement_date)
	
	def add_completion_date(self,completion_date):
		self.find_element(*self.add_completion_date_loc).send_keys(completion_date)

	def add_structure_area(self, structure_area):
		self.find_element(*self.add_structure_area_loc).send_keys(structure_area)

	def add_mileage(self, mileage):
		self.find_element(*self.add_mileage_loc).send_keys(mileage)

	def add_location(self):
		self.find_element(*self.add_location_loc).click()

	def add_location_province_Beijing(self):
		self.find_element(*self.add_location_province_Beijing_loc).click()

	def add_location_city_Beijing(self):
		self.find_element(*self.add_location_city_Beijing_loc).click()

	def add_location_county_Dongchengqu(self):
		self.find_element(*self.add_location_county_Dongchengqu_loc).click()

	def add_contract_type(self, contract_type):
		self.find_element(*self.add_contract_type_loc).send_keys(contract_type)

	def add_lump_sum_contract(self):
		self.find_element(*self.add_lump_sum_contract_loc).click()

	def add_status(self, status):
		self.find_element(*self.add_status_loc).send_keys(status)

	def add_not_in_service(self):
		self.find_element(*self.add_not_in_service_loc).click()

	def add_remark(self):
		self.find_element(*self.add_remark_loc).click()

	def save_add_project_department(self):
		self.find_element(*self.save_add_project_department_loc).click()

	def cancel_add_porject_department(self):
		self.find_element(*self.cancel_add_porject_department_loc).click()
	#***************************************************************************************

	pick_filiale_project_department_loc = (By.XPATH, '//*[@id="ztree-2_2_a"]')

	def pick_filiale_project_department(self):
		self.find_element(*self.pick_filiale_project_department_loc).click()

	delete_filiale_project_department_loc = (By.XPATH, '//*[@id="app"]/div/div[3]/div/div[2]/div/div[1]/div/div/div[3]/div/button[1]')

	def delete_filiale_project_department(self):
		self.find_element(*self.delete_filiale_project_department_loc).click()

	enter_delete_project_department_loc = (By.XPATH, '/html/body/div[6]/div/div[3]/button[2]')

	def enter_delete_project_department(self):
		self.find_element(*self.enter_delete_project_department_loc)

	cancel_delete_project_department_loc = (By.XPATH, '/html/body/div[6]/div/div[3]/button[1]')

	def cancel_delete_project_department(self):
		self.find_element(*self.cancel_delete_project_department_loc).click()

	edit_filiale_project_department_loc = (By.XPATH,'//*[@id="app"]/div/div[3]/div/div[2]/div/div[1]/div/div/div[3]/div/button[2]')

	def edit_filiale_project_department(self):
		self.find_element(*self.edit_filiale_project_department_loc).click()

	edit_project_name_loc = (By.XPATH, '//*[@id="app"]/div/div[3]/div/div[2]/div/div[5]/div/div[2]/form/div/div[1]/div[1]/div/div/input')

	def edit_project_name(self, project_name):
		self.find_element(*self.edit_project_name_loc).send_keys(project_name)

	edit_project_manager_name_loc = (By.XPATH, '//*[@id="app"]/div/div[3]/div/div[2]/div/div[5]/div/div[2]/form/div/div[1]/div[2]/div/div/input')

	def edit_project_manager_name(self, project_manager_name):
		self.find_element(*self.edit_project_manager_name_loc).send_keys(project_manager_name)

	edit_mobliephone_number_loc = (By.XPATH, '//*[@id="app"]/div/div[3]/div/div[2]/div/div[5]/div/div[2]/form/div/div[1]/div[3]/div/div/input')

	def edit_mobliephone_number(self, mobilephone_number):
		self.find_element(*self.edit_mobliephone_number_loc).send_keys(mobilephone_number)

	edit_commencement_date_loc = (By.XPATH, '//*[@id="app"]/div/div[3]/div/div[2]/div/div[5]/div/div[2]/form/div/div[1]/div[4]/div/div/div/div/input')

	def edit_commencement_date(self, commencement_date):
		self.find_element(*self.edit_commencement_date_loc).send_keys(commencement_date)

	edit_completion_date_loc = (By.XPATH, '//*[@id="app"]/div/div[3]/div/div[2]/div/div[5]/div/div[2]/form/div/div[1]/div[5]/div/div/div/div/input')

	def edit_completion_date(self, completion_date):
		self.find_element(*self.edit_completion_date_loc).send_keys(completion_date)

	edit_structure_area_loc = (By.XPATH, '//*[@id="app"]/div/div[3]/div/div[2]/div/div[5]/div/div[2]/form/div/div[1]/div[6]/div/div/input')

	def edit_structure_area(self, structure_area):
		self.find_element(*self.edit_structure_area_loc).send_keys(structure_area)

	edit_mileage_loc = (By.XPATH, '//*[@id="app"]/div/div[3]/div/div[2]/div/div[5]/div/div[2]/form/div/div[2]/div[1]/div/div/input')

	def edit_mileage(self, mileage):
		self.find_element(*self.edit_mileage_loc).send_keys(mileage)

	edit_location_loc = (By.XPATH, '//*[@id="provinLink1"]')

	def edit_location(self):
		self.find_element(*self.edit_location_loc).click()

	edit_location_province_Shanghai_loc = (By.XPATH, '//*[@id="_citys0"]/a[9]')

	def edit_location_province_Shanghai(self):
		self.find_element(*self.edit_location_province_Shanghai_loc).click()

	edit_location_city_Shanghai_loc = (By.XPATH, '//*[@id="_citys1"]/a')

	def edit_location_city_Shanghai(self):
		self.find_element(*self.edit_location_city_Shanghai_loc).click()

	edit_location_county_Yangpuqu_loc = (By.XPATH, '//*[@id="_citys2"]/a[9]')

	def edit_location_county_Yangpuqu(self):
		self.find_element(*self.edit_location_county_Yangpuqu_loc).click()

	edit_contract_type_loc = (By.XPATH, '//*[@id="app"]/div/div[3]/div/div[2]/div/div[5]/div/div[2]/form/div/div[2]/div[3]/div/div/div[1]/input')

	def edit_contract_type(self, contract_type):
		self.find_element(*self.edit_contract_type_loc).send_keys(contract_type)

	edit_lump_unit_contract_loc = (By.XPATH, '/html/body/div[5]/div/div[1]/ul/li[1]')

	def edit_lump_unit_contract(self):
		self.find_element(*self.edit_lump_unit_contract_loc).click()

	edit_status_loc = (By.XPATH, '//*[@id="app"]/div/div[3]/div/div[2]/div/div[5]/div/div[2]/form/div/div[2]/div[4]/div/div/div[1]/input')

	def edit_status(self, status):
		self.find_element(*self.edit_status_loc).send_keys(status)

	edit_under_construction_loc = (By.XPATH, '/html/body/div[6]/div/div[1]/ul/li[2]')

	def edit_under_construction(self):
		self.find_element(*self.edit_under_construction_loc).click()

	edit_remark_loc = (By.XPATH, '//*[@id="app"]/div/div[3]/div/div[2]/div/div[5]/div/div[2]/form/div/div[2]/div[5]/div/div/textarea')

	def edit_remark(self, remark):
		self.find_element(*self.edit_remark_loc).send_keys(remark)

	save_edit_project_department_loc = (By.XPATH, '//*[@id="app"]/div/div[3]/div/div[2]/div/div[5]/div/div[3]/div/button[1]')

	def save_edit_project_department(self):
		self.find_element(*self.save_edit_project_department_loc).click()

	cancel_edit_porject_department_loc = (By.XPATH, '//*[@id="app"]/div/div[3]/div/div[2]/div/div[5]/div/div[3]/div/button[2]')

	def cancel_edit_porject_department(self):
		self.find_element(*self.cancel_edit_porject_department_loc).click()


class SpaceUsae(Page):
	'''空间使用'''
	url = '/'

	#Action

	space_usage_loc = (By.XPATH, '//*[@id="app"]/div/div[3]/div/div[1]/ul/li[2]')

	def space_usage(self):
		self.find_element(*self.space_usage_loc).click()

	#Verification

	space_usage_hint_loc = (By.XPATH, '//*[@id="app"]/div/div[3]/div/div[2]/div/div/div[2]/div/div[1]/span')

	def space_usage_hint(self):
		return self.find_element(*space_usage_hint_loc).text