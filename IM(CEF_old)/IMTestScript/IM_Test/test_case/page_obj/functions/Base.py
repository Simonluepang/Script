#!\usr\bin\env python
# -*- coding:utf-8 -*-
'''
Title: 页面功能继承类
Description: open、find_element、find_elements、quit、script
@author: Xushenwei
@update: 2018年6月11日
'''
class Page(object):

	center_url = "/"

	def __init__(self, selenium_driver, base_url=center_url, parent=None):
		self.base_url = base_url
		self.driver = selenium_driver
		self.timeout = 30
		self.parent = parent

	def on_page(self):
		return self.driver.current_url == (self.base_url + self.url)

	def _open(self, url):
		url = self.base_url + url 
		self.driver.get(url)
		assert self.on_page(), 'Did not land on %s' % url

	def open(self):
		self._open(self.url)

	def find_element(self, *loc):
		return self.driver.find_element(*loc)

	def find_elements(self, *loc):
		return self.driver.find_elements(*loc)

	def script(self, src):
		return self.driver.execute_script(src)

	def quit(self):
		return self.driver.quit()