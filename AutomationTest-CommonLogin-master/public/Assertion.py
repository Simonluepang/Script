#coding=utf-8

def assert_status_code(data,code=200):
    assert data == code, 'status_code error,it is %s'%data['status_code']