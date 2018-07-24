from time import sleep
import unittest, random, sys
sys.path.append("./models")
sys.path.append("./page_obj")
from models import myunit, function
from page_obj.HeadPage import CompanyInformation
from page_obj.LoginPage import Login


class EditCompanyNameTest(myunit.MyTest):
	'''更改企业名称'''

	def edit_company_name(self, companyname=""):
		lg = Login(self.driver)
		lg.user_login()	
		sleep(1)
		CompanyInformation(self.driver).edit_change_company_name(companyname)

	def test1_edit_name(self):
		self.edit_company_name(companyname="徐莘伟的企业")
		ci = CompanyInformation(self.driver)
		self.assertEqual(ci.company_name_hint(), '徐莘伟的企业')
		self.assertEqual(ci.edit_success_hint(), '修改企业信息成功')

	def test2_edit_name(self):
		self.edit_company_name(companyname=" ")
		ci = CompanyInformation(self.driver)
		self.assertEqual(ci.only_space_verification_hint(), '必填项不能为空')


class EditContactAddressTest(myunit.MyTest):
	'''更改联系地址'''

	def edit_contact_address(self):
		lg = Login(self.driver)
		lg.user_login()	
		sleep(1)
		CompanyInformation(self.driver).edit_change_contact_address()

	def test1_edit_contact_address(self):
		self.edit_contact_address()
		sleep(2)
		ci = CompanyInformation(self.driver)
		self.assertEqual(ci.contact_address_hint(), '北京市-北京市')


class EditDetailAddressTest(myunit.MyTest):
	'''更改详细地址'''

	def edit_detail_address(self, detailaddress=""):
		lg = Login(self.driver)
		lg.user_login()	
		sleep(1)
		CompanyInformation(self.driver).edit_change_detail_address(detailaddress)

	def test1_edit_detail_address(self):
		self.edit_detail_address(detailaddress="五角场淞沪路创智天地")
		ci = CompanyInformation(self.driver)
		self.assertEqual(ci.detail_address_hint(), '五角场淞沪路创智天地')
		self.assertEqual(ci.edit_success_hint(), '修改企业信息成功')

	def test2_edit_detail_address(self):
		self.edit_detail_address(detailaddress=" ")
		ci = CompanyInformation(self.driver)
		self.assertEqual(ci.only_space_verification_hint(), '必填项不能为空')


class EditTelephoneNumTest(myunit.MyTest):
	'''更改电话号码'''

	def edit_telephone_num(self, telephonenum=""):
		lg = Login(self.driver)
		lg.user_login()	
		sleep(1)
		CompanyInformation(self.driver).edit_change_telephone_num(telephonenum)

	def test1_edit_telephone_num(self):
		self.edit_telephone_num(telephonenum="2654987")
		ci = CompanyInformation(self.driver)
		self.assertEqual(ci.telephone_num_hint(), '2654987')
		self.assertEqual(ci.edit_success_hint(), '修改企业信息成功')

	def test2_edit_telephone_num(self):
		self.edit_telephone_num(telephonenum=" ")
		ci = CompanyInformation(self.driver)
		self.assertEqual(ci.empty_telephone_num_hint(), '请输入正确的电话号')


class EditEnglishNameTest(myunit.MyTest):
	'''更改英文名'''

	def edit_english_name(self, englishname=""):
		lg = Login(self.driver)
		lg.user_login()	
		sleep(1)
		CompanyInformation(self.driver).edit_change_english_name(englishname)

	def test1_edit_english_name(self):
		self.edit_english_name(englishname="Simon")
		ci = CompanyInformation(self.driver)
		self.assertEqual(ci.english_name_hint(), 'Simon')
		self.assertEqual(ci.edit_success_hint(), '修改企业信息成功')

	def test2_edit_english_name(self):
		self.edit_english_name(englishname=" ")
		ci = CompanyInformation(self.driver)
		self.assertEqual(ci.only_space_verification_hint(), '必填项不能为空')


class EditCompanyManagerNameTest(myunit.MyTest):
	'''更改企业管理员'''

	def edit_company_manager_name(self, companymanagername):
		lg = Login(self.driver)
		lg.user_login()	
		sleep(1)
		CompanyInformation(self.driver).edit_change_company_manager_name(companymanagername)

	def test1_edit_company_manager_name(self):
		self.edit_company_manager_name(companymanagername='徐莘伟')
		ci = CompanyInformation(self.driver)
		self.assertEqual(ci.company_manager_name_hint(), '徐莘伟')
		self.assertEqual(ci.edit_success_hint(), '修改企业信息成功')

	def test2_edit_company_manager_name(self):
		self.edit_company_manager_name(companymanagername=' ')
		ci = CompanyInformation(self.driver)
		self.assertEqual(ci.empty_company_manager_name_hint(), '请输入中文或者英文')


class EditMobilephoneNumTest(myunit.MyTest):
	'''更改手机号码'''

	def edit_mobilephone_num(self, mobilephonenum):
		lg = Login(self.driver)
		lg.user_login()	
		sleep(1)
		CompanyInformation(self.driver).edit_change_mobilephone_num(mobilephonenum)

	def test1_edit_mobilephone_num(self):
		self.edit_mobilephone_num(mobilephonenum='15618713997')
		sleep(1)
		ci = CompanyInformation(self.driver)
		self.assertEqual(ci.mobilephone_num_hint(), '15618713997')
		self.assertEqual(ci.edit_success_hint(), '修改企业信息成功')

	def test2_edit_mobilephone_num(self):
		self.edit_mobilephone_num(mobilephonenum=' ')
		ci = CompanyInformation(self.driver)
		self.assertEqual(ci.empty_mobilephone_num_hint(), '请输入11位正确的手机号')


class EditEmailAddressTest(myunit.MyTest):
	'''更改注册邮箱'''	

	def edit_email_address(self, emailaddress=""):
		lg = Login(self.driver)
		lg.user_login()	
		sleep(1)
		CompanyInformation(self.driver).edit_change_email_address(emailaddress)

	def test1_edit_email_address(self):
		self.edit_email_address(emailaddress='13939201399@163.com')
		sleep(0.5)
		ci = CompanyInformation(self.driver)
		self.assertEqual(ci.email_address_hint(), '13939201399@163.com')
		self.assertEqual(ci.edit_success_hint(), '修改企业信息成功')
	
	def test2_edit_email_address(self):
		self.edit_email_address(emailaddress=' ')
		ci = CompanyInformation(self.driver)
		self.assertEqual(ci.empty_email_address_hint(), '请输入正确的邮箱地址')
	


class InputPasswordVerificationTest(myunit.MyTest):
	'''输入密码验证'''

	def input_password_verification(self, password=""):
		lg = Login(self.driver)
		lg.user_login()	
		sleep(1)
		CompanyInformation(self.driver).input_change_password_verification(password)

	def test1_input_password_verification(self):
		self.input_password_verification(password='')
		ci = CompanyInformation(self.driver)
		self.assertEqual(ci.empty_password_verification_hint(), '管理员密码不能为空')

	def test2_input_password_verification(self):
		self.input_password_verification(password='654321')
		ci = CompanyInformation(self.driver)
		self.assertEqual(ci.wrong_password_verification_hint(), '账号/密码错误！')


class EmptyInputCondition(myunit.MyTest):
	'''因为clear+传空值无法成功，故换另一种方法测试空值情况'''

	def login_page(self):
		lg = Login(self.driver)
		lg.user_login()	
		sleep(2)

	def test1_edit_name(self, companyname=""):
		EmptyInputCondition.login_page(self)
		ci = CompanyInformation(self.driver)
		ci.empty_edit_change_company_name(companyname="1")
		self.assertEqual(ci.empty_company_name_hint(), '企业名称不能为空')

	def test2_edit_detail_address(self, detailaddress=""):
		EmptyInputCondition.login_page(self)
		ci = CompanyInformation(self.driver)
		ci.empty_edit_change_detail_address(detailaddress="1")
		self.assertEqual(ci.empty_detail_address_hint(), '详细地址不能为空')

	def test3_edit_telephone_num(self, telephonenum=""):
		EmptyInputCondition.login_page(self)
		ci = CompanyInformation(self.driver)
		ci.empty_edit_change_telephone_num(telephonenum="1")
		self.assertEqual(ci.telephone_num_hint(), '')

	def test4_edit_english_name(self, englishname=""):
		EmptyInputCondition.login_page(self)
		ci = CompanyInformation(self.driver)
		ci.empty_edit_change_english_name(englishname="1")
		self.assertEqual(ci.empty_english_name_hint(), '英文名称不能为空')

	def test5_edit_company_manager_name(self, companymanagername=""):
		EmptyInputCondition.login_page(self)
		ci = CompanyInformation(self.driver)
		ci.empty_edit_change_company_manager_name(companymanagername="1")
		self.assertEqual(ci.empty_company_manager_name_hint(), '管理员不能为空')

	def test6_edit_mobilephone_num(self, mobilephonenum=''):
		EmptyInputCondition.login_page(self)
		ci = CompanyInformation(self.driver)
		ci.empty_edit_change_mobilephone_num(mobilephonenum='1')
		self.assertEqual(ci.empty_mobilephone_num_hint(), '手机号不能为空')

	def test7_edit_email_address(self, emailaddress=''):
		EmptyInputCondition.login_page(self)
		ci = CompanyInformation(self.driver)
		ci.empty_edit_change_email_address(emailaddress='1')
		self.assertEqual(ci.empty_email_address_hint(), '注册邮箱不能为空')




if __name__ == '__main__':
	unittest.main()
	'''
	# 构造测试集
	suite = unittest.TestSuite()
	suite.addTest(EditEmailAddressTest("test2_edit_email_address"))
	#suite.addTest(EditMobilephoneNumTest("test1_edit_mobilephone_num"))

	# 执行测试
	runner = unittest.TextTestRunner()
	runner.run(suite)
	
	'''
	