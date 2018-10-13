#coding=utf-8
#coding=utf-8
import os


Config = {
    "prodUrl":"http://be3.lubansoft.com",
    "pdsUrl":"http://pds.lubansoft.com",
    "centerUrl":"http://center.lubansoft.com",
    'pdsdocUrl':'http://pdsdoc.lubansoft.com',
    "user": 'fairy',
    "pwd" : "b8f8f597f244d3761efefd19fc6f2b14",
    "pid" : 12,
    "epid": 1,
    'prod_list ':{
                    'BE': {'pid': 12, 'url': 'http://be3.lubansoft.com'},
                    'GOV': {'pid': 38, 'url': 'http://govern.lubansoft.com'},
                    'CO':{'pid': 33,'url':'http://bimco.lubansoft.com/'},
                    'PLAN' : {'pid':39,'url':'http://plan.lubansoft.com'}}
    }



root = os.path.dirname(os.path.abspath(__file__))
headerManage = {
    'head_path': root + os.sep + 'Data' + os.sep + 'header.txt',
    'pds_cookie':'pds_cookie',
    'lt_joint':'lt_joint',
    'pdsdoc_url':"pdsdoc_url",
    'center_url':'pdscom_url',
    'pds_CASTGC_cookie':"pds_CASTGC_cookie",
    'joinSymbol': "==>",
    'center_cookie':'center_cookie',
    'BE_product_cookie':'BE_product_cookie',
    'GOV_product_cookie': 'GOV_product_cookie',
    'CO_product_cookie':'CO_product_cookie',
    'PLAN_product_cookie':'PLAN_product_cookie',
    'pdsdoc_cookie': 'pdsdoc_cookie'

}


if os.environ.get("API_MODE") == "PROD":
        Config['pdsUrl'] = "http://pds.lubansoft.com"
        Config['centerUrl'] = "http://center.lubansoft.com"
        Config['user']= 'fairy'
        Config['pwd'] = 'b8f8f597f244d3761efefd19fc6f2b14'
        Config['prod_list'] = {
        'BE':{'pid':12,'url':'http://be3.lubansoft.com'},
        'GOV':{'pid':38,'url':'http://govern.lubansoft.com'}}


elif os.environ.get("API_MODE") == "RLS":
        Config['pdsUrl'] = "http://pds.lubansoft.com"
        Config['centerUrl'] = "http://center.lubansoft.com"
        Config['user']= 'fairy'
        Config['pwd'] = 'b8f8f597f244d3761efefd19fc6f2b14'
        Config['prod_list'] = {
        'BE':{'pid':12,'url':'http://be3.lubansoft.com'},
        'GOV':{'pid':38,'url':'http://govern.lubansoft.com'}}


elif os.environ.get("API_MODE") == "LOCAL":
        Config['pdsUrl'] = "http://pds.lubansoft.com"
        Config['centerUrl'] = "http://center.lubansoft.com"
        Config['user']= 'fairy'
        Config['pwd'] = 'b8f8f597f244d3761efefd19fc6f2b14'
        Config['prod_list'] = {
        'BE':{'pid':12,'url':'http://be3.lubansoft.com'},
        'GOV':{'pid':38,'url':'http://govern.lubansoft.com'}}

