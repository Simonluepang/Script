from selenium.webdriver import Remote
from selenium import webdriver
from time import sleep

def browser():
	#driver = webdriver.Chrome()
	driver = webdriver.Firefox()
	return driver

if __name__ == '__main__':
	dr = browser()
	dr.get("http://www.baidu.com")
	sleep(3)
	dr.quit()