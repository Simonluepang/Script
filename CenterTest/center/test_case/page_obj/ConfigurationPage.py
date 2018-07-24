from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from Base import Page
from time import sleep
from selenium import webdriver
from autoit_function import MouseControl, WinControl, ProcessControl
import autoit


class ExplorerCivil(Page):
	'''Explorer(Civil)'''

	url = '/'
	pass


class Govern(Page):
	'''Govern'''

	url = '/'
	pass


class Plan(Page):
	'''Plan'''

	url = '/'
	pass


class Inspector(Page):
	'''Inspector'''

	url = '/'
	pass


class PreGovern(Page):
	'''PreGovern'''

	url = '/'
	pass