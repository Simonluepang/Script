#!/usr/bin/env python 
# -*- coding:utf-8 -*-
from Public.page_base import *

class Login(Page):

    def inputUsername(self,username):
        self.location('CSS','SENDKEYS','div#username>input.el-input__inner',username)

    def inputPassword(self,password):
        self.location('CSS','SENDKEYS','div#password>input.el-input__inner',password)

    def submitLogin(self):
        self.location('CSS','CLICK','button.enterprise-login')

    def hintLoginSuccess(self):
        return self.location('CSS','HINT','div.logo-title')

    def hintChooseCompany(self):
        return self.location('CSS','HINT','label.el-form-item__label')