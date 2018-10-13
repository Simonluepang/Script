#coding=utf-8

from public.CommonLogin import *
from Setting import *

#清空header.txt中记录的值
headfilepath = headerManage['head_path']
with open(headfilepath,'w') as f:
    f.write('')

#pds登录
login_pds = pds_login()
login_pds.join_all_login_step()

#center登录
login_center = center_login()
login_center.get_center_cookie()

#pdsdoc登录
# login_pdsdoc = pdsdoc_login()
# login_pdsdoc.get_pdsdoc_cookie()

#登录具体的产品端
# pro_login = product_login()
# pro_login.join_all_product_login()

#BE端测试用例执行
# from TestCase.test_be_login import *
# Test_login().test_address_serviceAddress()
