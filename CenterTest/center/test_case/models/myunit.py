from selenium import webdriver
# from driver import browser
import unittest


from time import sleep

def browser():
	driver = webdriver.Chrome()
	#driver = webdriver.Firefox()
	return driver

class MyTest(unittest.TestCase):

	def setUp(self):
		# self.driver = driver.browser()
		self.driver = browser()
		self.driver.implicitly_wait(10)
		self.driver.maximize_window()	
		sleep(1)


	def tearDown(self):
		self.driver.quit()


if __name__ == '__main__':
	MT = MyTest()
	MT.setUp()
	MT.tearDown()