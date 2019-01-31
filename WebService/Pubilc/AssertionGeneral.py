#!/usr/bin/env python 
# -*- coding:utf-8 -*-
def assert_general(result):
    assert result['status_code'] ==200
    assert result['msg'] =='success'