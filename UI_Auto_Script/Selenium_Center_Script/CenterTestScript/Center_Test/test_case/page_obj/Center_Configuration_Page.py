#!\usr\bin\env python
# -*- coding:utf-8 -*-
# Title: 页面元素封装功能
# Description:
# @author: Xushenwei
# @update: 2018年7月1日
# @editor:
from Selenium_Center_Script.CenterTestScript.Center_Test.test_case.page_obj.models.PageFunction import FunctionFactory


class PageConfiguration():
    def __init__(self, driver):
        self.FF = FunctionFactory(driver, 'Page_configuration')

    def configuration(self):
        self.FF.RunClick('configuration')

    def common(self):
        self.FF.RunClick('common')

    def data_catalog(self):
        self.FF.RunClick('data_catalog')
