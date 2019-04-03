#!/usr/bin/env python 
# -*- coding:utf-8 -*-
from selenium.webdriver.common.by import By
from Public.Base import *

class Page(Base):

    def _location(self,method,elementLocation):
        if method == 'CSS':
            return self.find_element(By.CSS_SELECTOR,elementLocation)
        elif method == 'ID':
            return self.find_element(By.ID,elementLocation)
        elif method == 'NAME':
            return self.find_element(By.NAME,elementLocation)
        elif method == 'CLASS':
            return self.find_element(By.CLASS_NAME,elementLocation)
        elif method == 'TAG':
            return self.find_element(By.TAG_NAME,elementLocation)
        elif method == 'LINK':
            return self.find_element(By.LINK_TEXT,elementLocation)
        elif method == 'PARTIAL_LINK':
            return self.find_element(By.PARTIAL_LINK_TEXT,elementLocation)
        elif method == 'XPATH':
            return self.find_element(By.XPATH,elementLocation)
        else:
            raise Exception(f"没有找到{method}此种定位方式！")

    def location(self,method,act,elementLocation,message='',readOnly=False,clickFirst=False):
        if act == 'CLICK':
            self._location(method,elementLocation).click()
            sleep(0.7)
        elif act == 'SENDKEYS':
            if readOnly==True:
                js = "document.getElementById('" + elementLocation + "').removeAttribute('readonly');"
                self.script(js)
            if clickFirst == True:
                self._location(method,elementLocation).click()
            self._location(method,elementLocation).clear()
            self._location(method,elementLocation).send_keys(message)
            sleep(0.7)
        elif act == 'HINT':
            return self._location(method,elementLocation).text
        else:
            raise Exception(f"没有收录{act}此种动作！")

    def _JSlocation(self,method,elementLocation):
        if method == 'CSS':
            return f'document.getElementByCSS(" + {elementLocation} + ")'
        elif method == 'ID':
            return f'document.getElementById(" + {elementLocation} + ")'
        elif method == 'NAME':
            return f'document.getElementByName(" + {elementLocation} + ")'
        elif method == 'CLASS':
            return f'document.getElementByClassName(" + {elementLocation} + ")'
        else:
            raise Exception(f"没有找到{method}此种定位方式！")


    def JSlocation(self,method,elementLocation,act,message=''):
        if act == 'CLICK':
            self.script(self._JSlocation(method,elementLocation) + '.click()')
        elif act == 'SENDKEYS':
            self.script(self._JSlocation(method, elementLocation) + '.clear()')
            self.script(self._JSlocation(method, elementLocation) + f'.send_keys({message})')
        else:
            raise Exception(f"没有收录{act}此种动作！")