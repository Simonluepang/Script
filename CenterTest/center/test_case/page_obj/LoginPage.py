#from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
#import sys
#sys.path.append('./page_obj')
#print(sys.path)
from Base import Page
from time import sleep
from selenium import webdriver

class Login(Page):

	url = '/'

	# 定位器
	login_username_loc = (By.XPATH, '//*[@id="app"]/div/div/div[2]/div[2]/div[2]/form/div[1]/div/div[1]/input')
	login_password_loc = (By.XPATH, '//*[@id="app"]/div/div/div[2]/div[2]/div[2]/form/div[2]/div/div[1]/input')
	login_button_loc = (By.XPATH, '//*[@id="app"]/div/div/div[2]/div[2]/div[2]/form/div[4]/button')

	def login_username(self, username):
		self.find_element(*self.login_username_loc).send_keys(username)

	def login_password(self, password):
		self.find_element(*self.login_password_loc).send_keys(password)

	def login_button(self):
		self.find_element(*self.login_button_loc).click()

	def user_login(self, username="15618713997", password="111111"):
		self.open()
		self.login_username(username)
		self.login_password(password)
		self.login_button()
		sleep(1)
		#cookie = ";".join([item["name"] + "=" + item["value"] for item in self.get_cookies()])
		#print(cookie)


if __name__ == '__main__':
	selenium_driver=webdriver.Chrome()
	lg = Login(selenium_driver)
	#lg.user_login()
	lg.login_button()
	lg.quit()