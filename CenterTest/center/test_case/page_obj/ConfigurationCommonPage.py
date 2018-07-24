from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from Base import Page
from time import sleep
from selenium import webdriver
from autoit_function import MouseControl, WinControl, ProcessControl
import autoit


class DataCatalog(Page):
	'''资料目录'''

	url = '/'

	# Action
	configuration_loc = (By.XPATH,'//*[@id="app"]/div/div[2]/ul/li[9]')

	common_loc = (By.XPATH, '//*[@id="app"]/div/div[3]/div/div[1]/ul/li[1]')

	data_catalog_loc = (By.XPATH, '//*[@id="app"]/div/div[3]/div/div[2]/div[2]/ul/li[1]')

	add_data_catalog_loc = (By.XPATH, '//*[@id="app"]/div/div[3]/div/div[2]/div[2]/div/div/div[1]/div[1]/button[1]')

	delete_data_catalog_loc = (By.XPATH, '//*[@id="app"]/div/div[3]/div/div[2]/div[2]/div/div/div[1]/div[1]/button[2]')

	pick_all_data_catalog_loc = (By.XPATH, '//*[@id="app"]/div/div[3]/div/div[2]/div[2]/div/div/div[1]/div[3]/div[2]/table/thead/tr/th[1]/div/label/span/span')

	enter_delete_catalog_loc = (By.XPATH, '/html/body/div[4]/div/div[3]/button[2]')

	cancel_delete_catalog_loc = (By.XPATH, '/html/body/div[4]/div/div[3]/button[1]')

	input_data_catalog_name_loc = (By.XPATH, '//*[@id="app"]/div/div[3]/div/div[2]/div[2]/div/div/div[1]/div[3]/div[3]/table/tbody/tr[1]/td[2]/div/div[2]/div/input')

	enter_data_catalog_name_loc = (By.XPATH, '//*[@id="app"]/div/div[3]/div/div[2]/div[2]/div/div/div[1]/div[3]/div[3]/table/tbody/tr[1]/td[2]/div/div[2]/span[2]')

	cancel_data_catalog_name_loc = (By.XPATH, '//*[@id="app"]/div/div[3]/div/div[2]/div[2]/div/div/div[1]/div[3]/div[3]/table/tbody/tr[1]/td[2]/div/div[2]/span[3]')

	assert_enter_loc = (By.XPATH, '/html/body/div[4]/div/div[3]/button[2]')

	point_data_catalog_folder_loc = (By.XPATH, '//*[@id="app"]/div/div[3]/div/div[2]/div[2]/div/div/div[1]/div[3]/div[3]/table/tbody/tr[1]/td[2]/div/div[1]')


	def data_catalog(self):
		'''切换到资料目录页面'''
		self.find_element(*self.configuration_loc).click()
		sleep(1.5)
		self.find_element(*self.common_loc).click()
		self.find_element(*self.data_catalog_loc).click()

	def add(self, filename):
		'''添加文件夹'''
		self.data_catalog()
		self.find_element(*self.add_data_catalog_loc).click()
		self.find_element(*self.input_data_catalog_name_loc).send_keys(filename)	
		self.find_element(*self.enter_data_catalog_name_loc).click()

	def assert_enter(self, filename):
		self.find_element(*self.assert_enter_loc).click()
		sleep(1)
		self.find_element(*self.cancel_data_catalog_name_loc).click()

	def add_three_inner_catalog(self):
		'''添加一个内外嵌套三个的文件夹'''
		for i in range(3):
			self.find_element(*self.point_data_catalog_folder_loc).click()
			sleep(0.5)
			self.find_element(*self.add_data_catalog_loc).click()
			self.find_element(*self.input_data_catalog_name_loc).send_keys(i)	
			self.find_element(*self.enter_data_catalog_name_loc).click()
			sleep(1)
		self.find_element(*self.point_data_catalog_folder_loc).click()

	#  Verification
	name_error_hint_loc = (By.XPATH, "/html/body/div[3]/div/div[2]/div[2]/p")

	add_success_hint_loc = (By.XPATH, "/html/body/div[5]/div/p")

	add_name_is_empty_loc = (By.XPATH, '/html/body/div[3]/div/div[2]/div[2]/p')

	add_name_is_repetition_loc = (By.XPATH, '/html/body/div[3]/div/div[2]/div[2]/p')

	find_folder_data_hint_loc = (By.XPATH, '//*[@id="app"]/div/div[3]/div/div[2]/div/div/div/div[2]/div[3]/div[3]/div/span')

	def name_error_hint(self):
		return self.find_element(*self.name_error_hint_loc).text

	def add_success_hint(self):
		# 这种只停留几秒的标签，需要使用循环来查找，否则是找不到这个元素的
		for i in range(3):
			a1 = self.find_element(*self.add_success_hint_loc).text
		return a1

	def add_name_is_empty(self):
		return self.find_element(*self.add_name_is_empty_loc).text

	def add_name_is_repetition(self):
		return self.find_element(*self.add_name_is_repetition_loc).text

	def find_folder_data_hint(self):
		return self.find_element(*self.find_folder_data_hint_loc).text

	delete_success_hint_loc = (By.XPATH, '/html/body/div[4]/div/p')

	def delete_success_hint(self):
		for i in range(3):
			a1 = self.find_element(*self.delete_success_hint_loc).text
		return a1

	def delete(self):
		self.data_catalog()
		self.find_element(*self.pick_all_data_catalog_loc).click()
		self.find_element(*self.delete_data_catalog_loc).click()
		self.find_element(*self.enter_delete_catalog_loc).click()
		sleep(1)


class AttributeTemplate(Page):
	'''属性模板'''

	url = '/'

	# Action
	configuration_loc = (By.XPATH,'//*[@id="app"]/div/div[2]/ul/li[9]')

	common_loc = (By.XPATH, '//*[@id="app"]/div/div[3]/div/div[1]/ul/li[1]')

	attribute_template_loc = (By.XPATH, '//*[@id="app"]/div/div[3]/div/div[2]/div/ul/li[2]')

	edit_construction_template_loc = (By.XPATH, '//*[@id="app"]/div/div[3]/div/div[2]/div/div/div/div[2]/div/div[3]/table/tbody/tr[1]/td[5]/div/span')

	def edit_construction_template(self):

		self.find_element(*self.configuration_loc).click()
		sleep(1)
		self.find_element(*self.common_loc).click()
		self.find_element(*self.attribute_template_loc).click()
		self.find_element(*self.edit_construction_template_loc).click()
		sleep(1)

	add_first_level_loc = (By.XPATH, '//*[@id="app"]/div/div[3]/div/div[2]/div/div/div/div[3]/div/div[2]/div[2]/button[1]')

	input_first_level_name_loc = (By.XPATH, '//*[@id="app"]/div/div[3]/div/div[2]/div/div/div/div[5]/div/div[2]/div/div/div/input')

	enter_first_level_name_loc = (By.XPATH, '//*[@id="app"]/div/div[3]/div/div[2]/div/div/div/div[5]/div/div[3]/span/button[1]')

	cancel_first_level_name_loc = (By.XPATH, '//*[@id="app"]/div/div[3]/div/div[2]/div/div/div/div[5]/div/div[3]/span/button[2]')

	def add_first_level(self, firstlevelname):

		self.find_element(*self.add_first_level_loc).click()
		sleep(1)
		self.find_element(*self.input_first_level_name_loc).send_keys(firstlevelname)
		self.find_element(*self.enter_first_level_name_loc).click()

	new_first_level_attribute_loc = (By.XPATH, '//*[@id="app"]/div/div[3]/div/div[2]/div/div/div/div[3]/div/div[2]/div[1]/div[3]/table/tbody/tr[10]/td[1]/div/div')

	add_second_level_loc = (By.XPATH, '//*[@id="app"]/div/div[3]/div/div[2]/div/div/div/div[3]/div/div[2]/div[2]/button[2]')

	input_second_level_name_loc = (By.XPATH, '//*[@id="app"]/div/div[3]/div/div[2]/div/div/div/div[6]/div/div[2]/div[1]/div/div/input')

	input_second_level_value_loc = (By.XPATH, '//*[@id="app"]/div/div[3]/div/div[2]/div/div/div/div[6]/div/div[2]/div[2]/div/div/input')

	enter_second_level_loc = (By.XPATH, '//*[@id="app"]/div/div[3]/div/div[2]/div/div/div/div[6]/div/div[3]/span/button[1]')

	cancel_second_level_loc = (By.XPATH, '//*[@id="app"]/div/div[3]/div/div[2]/div/div/div/div[6]/div/div[3]/span/button[2]')

	def add_second_level(self, secondlevelname, secondlevelvalue):
		
		self.find_element(*self.new_first_level_attribute_loc).click()
		self.find_element(*self.add_second_level_loc).click()
		sleep(1)
		self.find_element(*self.input_second_level_name_loc).send_keys(secondlevelname)
		self.find_element(*self.input_second_level_value_loc).send_keys(secondlevelvalue)
		self.find_element(*self.enter_second_level_loc).click()

	new_second_level_attribute_loc = (By.XPATH, '//*[@id="app"]/div/div[3]/div/div[2]/div/div/div/div[3]/div/div[2]/div[1]/div[3]/table/tbody/tr[11]/td[1]/div/div')

	edit_attribute_loc = (By.XPATH, '//*[@id="app"]/div/div[3]/div/div[2]/div/div/div/div[3]/div/div[2]/div[2]/button[3]')

	edit_attribute_name_loc = (By.XPATH, '//*[@id="app"]/div/div[3]/div/div[2]/div/div/div/div[4]/div/div[2]/div[1]/div/div/input')

	edit_attribute_value_loc = (By.XPATH, '//*[@id="app"]/div/div[3]/div/div[2]/div/div/div/div[4]/div/div[2]/div[2]/div/div/input')

	enter_edit_attribute_loc = (By.XPATH, '//*[@id="app"]/div/div[3]/div/div[2]/div/div/div/div[4]/div/div[3]/span/button[1]')

	cancel_edit_attribute_loc = (By.XPATH, '//*[@id="app"]/div/div[3]/div/div[2]/div/div/div/div[4]/div/div[3]/span/button[2]')

	def edit_first_level_contribute(self, editname):
		
		self.find_element(*self.new_first_level_attribute_loc).click()
		self.find_element(*self.edit_attribute_loc).click()
		sleep(1)
		self.find_element(*self.edit_attribute_name_loc).clear()
		self.find_element(*self.edit_attribute_name_loc).send_keys(editname)
		self.find_element(*self.enter_edit_attribute_loc).click()

	def edit_second_level_contribute(self, editname, editvalue):
		
		self.find_element(*self.new_second_level_attribute_loc).click()
		self.find_element(*self.edit_attribute_loc).click()
		sleep(1)
		self.find_element(*self.edit_attribute_name_loc).clear()
		self.find_element(*self.edit_attribute_value_loc).clear()
		self.find_element(*self.edit_attribute_name_loc).send_keys(editname)
		self.find_element(*self.edit_attribute_value_loc).send_keys(editvalue)
		self.find_element(*self.enter_edit_attribute_loc).click()

	delete_attribute_loc = (By.XPATH, '//*[@id="app"]/div/div[3]/div/div[2]/div/div/div/div[3]/div/div[2]/div[2]/button[4]')

	move_up_attribute_loc = (By.XPATH, '//*[@id="app"]/div/div[3]/div/div[2]/div/div/div/div[3]/div/div[2]/div[2]/button[5]')

	move_down_attribute_loc = (By.XPATH, '//*[@id="app"]/div/div[3]/div/div[2]/div/div/div/div[3]/div/div[2]/div[2]/button[6]')

	close_edit_construction_template_loc = (By.XPATH, '//*[@id="app"]/div/div[3]/div/div[2]/div/div/div/div[3]/div/div[1]/button/i')

	def delete_first_level_attribute(self):
		
		self.find_element(*self.new_first_level_attribute_loc).click()
		self.find_element(*self.delete_attribute_loc).click()

	def delete_second_level_attribute(self):
		
		self.find_element(*self.new_second_level_attribute_loc).click()
		self.find_element(*self.delete_attribute_loc).click()

	def up_move_second_level_attribute(self):

		self.find_element(*self.new_second_level_attribute_loc).click()
		self.find_element(*self.move_up_attribute_loc).click()

	def down_move_second_level_attribute(self):

		self.find_element(*self.new_second_level_attribute_loc).click()
		self.find_element(*self.move_down_attribute_loc).click()

	def up_move_first_level_attribute(self):

		self.find_element(*self.new_first_level_attribute_loc).click()
		self.find_element(*self.move_up_attribute_loc).click()

	def down_move_first_level_attribute(self):

		self.find_element(*self.new_first_level_attribute_loc).click()
		self.find_element(*self.move_down_attribute_loc).click()


	#  Verification
	first_level_name_hint_loc = (By.XPATH, '//*[@id="app"]/div/div[3]/div/div[2]/div/div/div/div[3]/div/div[2]/div[1]/div[3]/table/tbody/tr[10]/td[1]/div/div/span')

	def first_level_name_hint(self):
		return self.find_element(*self.first_level_name_hint_loc).text

	second_level_name_hint_loc = (By.XPATH, '//*[@id="app"]/div/div[3]/div/div[2]/div/div/div/div[3]/div/div[2]/div[1]/div[3]/table/tbody/tr[11]/td[1]/div/div/span')

	def second_level_name_hint(self):
		return self.find_element(*self.second_level_name_hint_loc).text

	second_level_value_hint_loc = (By.XPATH, '//*[@id="app"]/div/div[3]/div/div[2]/div/div/div/div[3]/div/div[2]/div[1]/div[3]/table/tbody/tr[11]/td[2]/div')

	def second_level_value_hint(self):
		return self.find_element(*self.second_level_value_hint_loc).text

	floating_text_hint_loc = (By.XPATH, '/html/body/div[4]/div/p')

	def floating_text_hint(self):
		for i in range(3):
			a1 = self.find_element(*self.floating_text_hint_loc).text
		return a1


class LogoManagement(Page):
	'''标识管理'''
	pass



class LabelManagement(Page):
	'''标签管理'''

	url = '/'

	# Action
	configuration_loc = (By.XPATH,'//*[@id="app"]/div/div[2]/ul/li[9]')

	common_loc = (By.XPATH, '//*[@id="app"]/div/div[3]/div/div[1]/ul/li[1]')

	label_management_loc = (By.XPATH, '//*[@id="app"]/div/div[3]/div/div[2]/div/ul/li[4]')

	def label_management(self):
		'''切换到标签管理页面'''
		self.find_element(*self.configuration_loc).click()
		sleep(1)
		self.find_element(*self.common_loc).click()
		self.find_element(*self.label_management_loc).click()
		sleep(1)

	add_label_loc = (By.XPATH, '//*[@id="app"]/div/div[3]/div/div[2]/div/div/div/div[1]/button[1]')

	input_label_name_loc = (By.XPATH, '//*[@id="app"]/div/div[3]/div/div[2]/div/div/div/div[4]/div/div[2]/div/div/div/input')

	enter_label_name_loc = (By.XPATH, '//*[@id="app"]/div/div[3]/div/div[2]/div/div/div/div[4]/div/div[3]/span/button[1]')

	cancel_label_name_loc = (By.XPATH, '//*[@id="app"]/div/div[3]/div/div[2]/div/div/div/div[4]/div/div[3]/span/button[2]')

	def add_label(self, labelname="测试用添加标签"):
		'''添加多个标签'''
		self.label_management()
		for i in range(20):
			self.find_element(*self.add_label_loc).click()
			sleep(1)
			self.find_element(*self.input_label_name_loc).send_keys(labelname + str(i))
			self.find_element(*self.enter_label_name_loc).click()
			sleep(1)

	check_first_label_loc = (By.XPATH, '//*[@id="app"]/div/div[3]/div/div[2]/div/div/div/div[2]/div/div[1]/div[3]/table/tbody/tr[1]/td[1]/div/label/span/span')

	delete_label_loc = (By.XPATH, '//*[@id="app"]/div/div[3]/div/div[2]/div/div/div/div[1]/button[2]')

	enter_delete_label_loc = (By.XPATH, '/html/body/div[3]/div/div[3]/button[2]')

	cancel_delete_label_loc = (By.XPATH, '/html/body/div[3]/div/div[3]/button[1]')

	def delete_label(self):
		'''删除多个标签'''
		self.label_management()
		for i in range(20):
			self.find_element(*self.check_first_label_loc).click()
			self.find_element(*self.delete_label_loc).click()
			sleep(1)
			self.find_element(*self.enter_delete_label_loc).click()
			sleep(1)

	
	edit_label_hint_loc = (By.XPATH, '//*[@id="app"]/div/div[3]/div/div[2]/div/div/div/div[2]/div/div[1]/div[3]/table/tbody/tr[1]/td[5]/div/span')
	
	edit_label_name_hint_loc = (By.XPATH, '//*[@id="app"]/div/div[3]/div/div[2]/div/div/div/div[4]/div/div[2]/div/div/div/input')
	
	enter_label_name_hint_loc = (By.XPATH, '//*[@id="app"]/div/div[3]/div/div[2]/div/div/div/div[4]/div/div[3]/span/button[1]')
	
	cancel_label_name_hint_loc = (By.XPATH, '//*[@id="app"]/div/div[3]/div/div[2]/div/div/div/div[4]/div/div[3]/span/button[2]')

	def edit_label(self, newlabelname):
		'''修改标签'''
		self.find_element(*self.edit_label_hint_loc).click()
		sleep(1)
		self.find_element(*self.edit_label_name_hint_loc).clear()
		self.find_element(*self.edit_label_name_hint_loc).send_keys(newlabelname)
		self.find_element(*self.enter_label_name_hint_loc).click()


class FormManagement(Page):
	'''表单管理'''

	def __init__(self):
		self.upload_forms = '打开'


	url = '/'

	# Action
	configuration_loc = (By.XPATH,'//*[@id="app"]/div/div[2]/ul/li[9]')

	common_loc = (By.XPATH, '//*[@id="app"]/div/div[3]/div/div[1]/ul/li[1]')

	form_management_hint_loc = (By.XPATH, '//*[@id="app"]/div/div[3]/div/div[2]/div/ul/li[5]')

	def form_management(self):
		'''切换到表单管理界面'''
		self.find_element(*self.configuration_loc).click()
		sleep(1)
		self.find_element(*self.common_loc).click()
		self.find_element(*self.label_management_loc).click()
		sleep(1)

	add_form_hint_loc = (By.XPATH, '//*[@id="app"]/div/div[3]/div/div[2]/div/div/div/div[1]/button[1]')

	upload_form_hint_loc = (By.XPATH, '//*[@id="app"]/div/div[3]/div/div[2]/div/div/div/div[4]/div/div[2]/div[1]/div[1]/div/div[2]/div/button')\

	cooperation_type_loc = (By.XPATH, '//*[@id="app"]/div/div[3]/div/div[2]/div/div/div/div[4]/div/div[2]/div[2]/div/div[1]/div[1]/i')

	fanganhuiqian_type_hint_loc = (By.XPATH, '/html/body/div[4]/div/div[1]/ul/li[4]')

	enter_add_form_hint_loc = (By.XPATH, '//*[@id="app"]/div/div[3]/div/div[2]/div/div/div/div[4]/div/div[3]/span/button[1]')
	
	cancel_add_form_hint_loc = (By.XPATH, '//*[@id="app"]/div/div[3]/div/div[2]/div/div/div/div[4]/div/div[3]/span/button[2]')

	def add_form_inner(self):
		'''上传模板'''
		sleep(1)
		w0 = WinControl(self.upload_forms)
		if w0.exists():
			w0.wait(3)
			m1 = MouseControl()
			m1.click(self.upload_forms, '', 1000, 50)
			autoit.send(r"F:\pythondemo\Github\Python-script\CenterTest\center\data")
			autoit.send("{ENTER}")
			sleep(1)
			m1.click(self.upload_forms, '', 1000, 970)
			autoit.send("uploadtestfile.docx")
			w0.controlClick('[CLASS:Button; INSTANCE:1]')
			sleep(3)
		else:
			raise Exception("未打开上传窗口")

	def add_form(self):
		'''添加模板'''
		self.form_management()
		self.find_element(*self.upload_form_hint_loc).click()
		self.find_element(*self.add_form_hint_loc).click()
		self.add_form_inner()
		self.find_element(*self.cooperation_type_loc).click()
		sleep(1)
		self.find_element(*self.fanganhuiqian_type_hint_loc).click()
		self.find_element(*self.enter_add_form_hint_loc).click()


	edit_form_hint_loc = (By.XPATH, '//*[@id="app"]/div/div[3]/div/div[2]/div/div/div/div[2]/div[3]/table/tbody/tr/td[6]/div/span[1]')

	edit_form_name_hint_loc = (By.XPATH, '//*[@id="app"]/div/div[3]/div/div[2]/div/div/div/div[4]/div/div[2]/div[1]/div[2]/div/div/input')

	edit_form_cooperation_type_hint_loc = (By.XPATH, '//*[@id="app"]/div/div[3]/div/div[2]/div/div/div/div[4]/div/div[2]/div[2]/div/div[2]/div[1]/input')

	choose_paper_change_type_hint_loc = (By.XPATH, '/html/body/div[5]/div/div[1]/ul/li[6]')

	enter_edit_form_hint_loc = (By.XPATH, '//*[@id="app"]/div/div[3]/div/div[2]/div/div/div/div[4]/div/div[3]/span/button[1]')

	cancel_edit_form_hint_loc = (By.XPATH, '//*[@id="app"]/div/div[3]/div/div[2]/div/div/div/div[4]/div/div[3]/span/button[2]')

	def edit_form(self):
		'''编辑模板'''
		self.form_management()
		self.find_element(*self.edit_form_hint_loc).click()
		sleep(1)
		self.find_element(*self.edit_form_name_hint_loc).clear()
		self.find_element(*self.edit_form_name_hint_loc).send_keys("renamefile")
		self.find_element(*self.edit_form_cooperation_type_hint_loc).click()
		sleep(1)
		self.find_element(*self.choose_paper_change_type_hint_loc).click()
		self.find_element(*self.enter_edit_form_hint_loc).click()

	choose_all_forms_hint_loc = (By.XPATH, '//*[@id="app"]/div/div[3]/div/div[2]/div/div/div/div[2]/div[2]/table/thead/tr/th[1]/div/label/span/span')

	delete_choosed_form_hint_loc = (By.XPATH, '//*[@id="app"]/div/div[3]/div/div[2]/div/div/div/div[1]/button[2]')

	enter_delete_form_hint_loc = (By.XPATH, '/html/body/div[3]/div/div[3]/button[2]')

	cancel_delete_form_hint_loc = (By.XPATH, '/html/body/div[3]/div/div[3]/button[1]')

	def delete_form(self):
		'''删除表单'''
		self.form_management()
		self.find_element(*self.choose_all_forms_hint_loc).click()
		self.find_element(*self.delete_choosed_form_hint_loc).cilck()
		sleep(1)
		self.find_element(*self.enter_delete_form_hint_loc).click()


class ProcessTemplate(Page):
	'''工序模板'''

	url = '/'

	# Action
	configuration_loc = (By.XPATH,'//*[@id="app"]/div/div[2]/ul/li[9]')

	common_loc = (By.XPATH, '//*[@id="app"]/div/div[3]/div/div[1]/ul/li[1]')

	process_template_hint_loc = (By.XPATH, '//*[@id="app"]/div/div[3]/div/div[2]/div/ul/li[6]')

	def process_template(self):
		'''切换到工序模板界面'''
		self.find_element(*self.configuration_loc).click()
		sleep(1)
		self.find_element(*self.common_loc).click()
		self.find_element(*self.process_template_hint_loc).click()
		sleep(1)

	add_process_template_hint_loc = (By.XPATH, '//*[@id="app"]/div/div[3]/div/div[2]/div/div/div/div[2]/div[1]/button[1]')

	input_process_template_name_hint_loc = (By.XPATH, '//*[@id="app"]/div/div[3]/div/div[2]/div/div/div/div[3]/div/div[2]/div[1]/div[1]/div[1]/div/div/div/input')

	enter_add_process_template_hint_loc = (By.XPATH, '//*[@id="app"]/div/div[3]/div/div[2]/div/div/div/div[3]/div/div[3]/span/button[1]')

	cancel_add_process_template_hint_loc = (By.XPATH, '//*[@id="app"]/div/div[3]/div/div[2]/div/div/div/div[3]/div/div[3]/span/button[2]')

	