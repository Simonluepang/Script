# from selenium import webdriver
# from selenium.webdriver.common.by import By
# import os
# import json
from time import sleep
import PageFunction

# driver = webdriver.Chrome()
# driver.get('http://192.168.13.195:8989/dist/#/login')
# print(driver.title)

# base_dir = str(os.path.dirname(os.path.dirname(__file__))).replace('\\', '/')
# base = base_dir.split('/test_case')[0]
# base = base_dir.split('/test_case')[0]
# file_path = base + "/report/image/" + 'file_name'
# print(base)

# file = open('Page_login.json', 'rb')
# fileJson = json.loads(file.read())
# elementname = fileJson['element_name']
# print(fileJson)

ff = PageFunction.FunctionFactory('http://192.168.13.195:8989/dist/#/login', 'Luban Center', 'Page_login')
ff.open()
# sleep(3)
messagelist = [('login_username', 'xushenwei'), ('login_password', '111111')]
for element_name, value in messagelist:
	ff.RunSendKeys(element_name, value)
for i in range(2):
	ff.RunClick('submit_login')
	sleep(1)

if ff.RunHint('login_success_hint')=='徐莘伟的企业1':
	print('login success!')
else:
	print('login fail!')

print(ff.RunHint('login_success_hint'))

# driver.get("http://192.168.13.195:8989/dist/#/login")
# sleep(3)
# a = driver.find_element(By.XPATH, "//*[@id='app']/div/div/div[1]/div[2]/p").text
# print(a)

ff.quit()

# a = [1,2,3,4,5]
# if 0 in a:
# 	raise Exception
# else:
# 	print('pass')