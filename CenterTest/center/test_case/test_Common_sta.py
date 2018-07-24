from time import sleep
import unittest, random, sys
sys.path.append("./models")
sys.path.append("./page_obj")
from models import myunit, function
from page_obj.ConfigurationCommonPage import *
from page_obj.LoginPage import Login


class CatalogTest(myunit.MyTest):
	'''资料目录文件夹相关测试'''

	
	def add_folder(self, filename=""):
		'''添加文件夹'''
		lg = Login(self.driver)
		lg.user_login()	
		sleep(1)
		DataCatalog(self.driver).add(filename)
	
	def test1_add(self):
		'''添加文件夹成功'''
		self.add_folder(filename="123")
		dc = DataCatalog(self.driver)
		self.assertEqual(dc.add_success_hint(), "添加成功")

	def test2_add(self):
		'''文件夹名称为空'''
		self.add_folder(filename="")
		dc = DataCatalog(self.driver)
		self.assertEqual(dc.add_name_is_empty(), "文件夹名称不能为空")

	def test3_add(self):
		'''文件夹名称重复'''
		self.add_folder(filename="123")
		dc = DataCatalog(self.driver)
		self.assertEqual(dc.add_name_is_repetition(), "文件夹【123】已存在")

	def test4_add(self):
		'''重复添加内部文件夹'''
		self.add_folder(filename="1")
		sleep(0.5)
		dc = DataCatalog(self.driver)
		DataCatalog(self.driver).add_three_inner_catalog()
		self.assertEqual(dc.find_folder_data_hint(), '暂无数据')

	def delete_folder(self):
		'''删除文件夹'''
		lg = Login(self.driver)
		lg.user_login()	
		sleep(1)
		DataCatalog(self.driver).delete()
		
	def test5_delete_success(self):
		'''删除文件夹成功'''
		self.delete_folder()
		dc = DataCatalog(self.driver)
		self.assertEqual(dc.delete_success_hint(), "删除成功")


class AttributeTemplateTest(myunit.MyTest):
	'''属性模板相关测试'''
	def edit_construction_template(self):
		lg = Login(self.driver)
		lg.user_login()	
		sleep(1)
		AttributeTemplate(self.driver).edit_construction_template()

	def test1_add_first_level_success(self):
		self.edit_construction_template()
		at = AttributeTemplate(self.driver)
		at.add_first_level(firstlevelname="1")
		self.assertEqual(at.first_level_name_hint(), "1")

	def test2_add_second_level_success(self):
		self.edit_construction_template()
		at = AttributeTemplate(self.driver)
		at.add_second_level(secondlevelname="2", secondlevelvalue="2")
		sleep(1)
		self.assertEqual(at.second_level_name_hint(), "2")
		self.assertEqual(at.second_level_value_hint(), "2")

	def test3_edit_first_level_contribute(self):
		self.edit_construction_template()
		at = AttributeTemplate(self.driver)
		at.edit_first_level_contribute(editname="new1")
		self.assertEqual(at.floating_text_hint(), '编辑成功')
		self.assertEqual(at.first_level_name_hint(), 'new1')

	def test4_edit_second_level_contribute(self):
		self.edit_construction_template()
		at = AttributeTemplate(self.driver)
		at.edit_second_level_contribute(editname="newvalue1", editvalue="newvalue2")
		self.assertEqual(at.floating_text_hint(), '编辑成功')
		self.assertEqual(at.second_level_name_hint(), 'newvalue1')
		self.assertEqual(at.second_level_value_hint(), 'newvalue2')

	def test5_down_move_second_level_attribute(self):
		self.edit_construction_template()
		at = AttributeTemplate(self.driver)
		at.add_second_level(secondlevelname="3", secondlevelvalue="3")
		sleep(1)
		at.down_move_second_level_attribute()
		self.assertEqual(at.floating_text_hint(), '移动成功')

	def test6_up_move_second_level_attribute(self):
		self.edit_construction_template()
		at = AttributeTemplate(self.driver)
		at.up_move_second_level_attribute()
		self.assertEqual(at.floating_text_hint(), '移动成功')

	def test7_up_move_first_level_attribute(self):
		self.edit_construction_template()
		at = AttributeTemplate(self.driver)
		at.up_move_first_level_attribute()
		self.assertEqual(at.floating_text_hint(), '移动成功')

	def test8_down_move_first_level_attribute(self):
		self.edit_construction_template()
		at = AttributeTemplate(self.driver)
		at.down_move_first_level_attribute()
		self.assertEqual(at.floating_text_hint(), '移动成功')

	def test9_delete_second_level_attribute(self):
		self.edit_construction_template()
		at = AttributeTemplate(self.driver)
		at.delete_second_level_attribute()
		self.assertEqual(at.floating_text_hint(), '删除成功')

	def test11_delete_first_level_attribute(self):
		self.edit_construction_template()
		at = AttributeTemplate(self.driver)
		at.delete_first_level_attribute()
		self.assertEqual(at.floating_text_hint(), '删除成功')

'''
class AddLabelTest(myunit.MyTest):

	def add_label(self):
		LabelManagement(self.driver).add_label()

	def test1_add(self):
		self.add_label()

	def delete_label(self):
		LabelManagement(self.driver).delete_label()

	def test1_delete(self):
		self.delete_label()
'''


if __name__ == '__main__':

	#unittest.main()
	
	# 构造测试集
	suite = unittest.TestSuite()
	suite.addTest(CatalogTest("test1_add"))
	#suite.addTest(CatalogTest("test2_add"))
	#suite.addTest(CatalogTest("test3_add"))
	#suite.addTest(CatalogTest("test4_add"))
	#suite.addTest(CatalogTest("test5_delete_success"))
	#suite.addTest(CatalogTest("test6_delete_first_level_attribute"))

	# 执行测试
	runner = unittest.TextTestRunner()
	runner.run(suite)
	'''
	'''