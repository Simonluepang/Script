#!\usr\bin\env python
# -*- coding:utf-8 -*-
'''
Title: 功能试用demo
Description: 
@author: Xushenwei
@update: 2018年6月11日
'''
import sys
sys.path.append("..")  # 进到上一个文件夹下
# from models.driver import *

import driver  # 导入平级文件夹下的模块
# print(sys.path)
driver.browser()  # 引入模块前的名字要写全

import os
print(os.path.relpath(r"F:\pythondemo\Github\Python-script\IM(CEF+selenium)\IMTestScript\Client\x64_vc11_unicode_release\BimIM.exe"))