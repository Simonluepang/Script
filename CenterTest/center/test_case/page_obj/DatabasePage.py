from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
# import sys
# sys.path.append('..')
from Base import Page
from time import sleep
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

class MaterielClass(Page):
	'''物料类'''

	url = '/'

	#Action

	database_loc = (By.XPATH, '//*[@id="app"]/div/div[2]/ul/li[2]')

	def database(self):
		self.find_element(*self.database_loc).click()

	materiel_class_loc = (By.XPATH, '//*[@id="app"]/div/div[3]/div/div[1]/ul/li[1]')

	def materiel_class(self):
		self.find_element(*self.materiel_class_loc).click()


class OrganizationClass(Page):
	'''组织类'''

	url = '/'

	#Action

	organization_class_loc = (By.XPATH, '//*[@id="app"]/div/div[3]/div/div[1]/ul/li[2]')

	def organization_class_loc(self):
		self.find_element(*self.organization_class_loc).click()
		

class ItemClass(Page):
	'''组织类'''

	url = '/'

	#Action

	item_class_loc = (By.XPATH, '//*[@id="app"]/div/div[3]/div/div[1]/ul/li[3]')

	def item_class_loc(self):
		self.find_element(*self.item_class_loc).click()