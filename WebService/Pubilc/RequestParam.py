#!/usr/bin/env python 
# -*- coding:utf-8 -*-

# 将输入的信息转化为字典形式

class req_login_controller:

    def rest_login(self, user, pwd):
        params = {
            'username': user,
            'password': pwd
        }
        return params