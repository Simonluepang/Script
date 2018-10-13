from public.CommonInterface import *
import re
from public.readConfig import *
from public.ReadFile import *

#全局变量
pds_url = Config['pdsUrl']
splitSymbol = headerManage['joinSymbol']
headFilePath = headerManage['head_path']
user = Config['user']
pwd = Config['pwd']
epid = Config['epid']

center_url = Config['centerUrl']
center_cookie_name = headerManage['center_cookie']

pdsdoc_url = Config['pdsdocUrl']
pdsdoc_cookie_name = headerManage['pdsdoc_cookie']

gov_url = Config['prod_list ']['GOV']['url']
gov_cookie_name = headerManage["GOV_product_cookie"]

be_url = Config['prod_list ']['BE']['url']
be_pid = Config['prod_list ']['BE']['pid']
be_cookie_name =  headerManage['BE_product_cookie']


co_url = Config['prod_list ']['CO']['url']
co_cookie_name = headerManage['CO_product_cookie']

plan_url = Config['prod_list ']['PLAN']['url']
plan_pid = Config['prod_list ']['PLAN']['pid']
plan_cookie_name = headerManage['PLAN_product_cookie']


class pds_login:

    def login_get_cookie(self):
        '''
        获得cookie，并设置为全局变量
        拿到lt并组装写入文件
        :return:
        '''
        resp = pds().interface_login_get(pds_url)

        cookie = resp['headers']['Set-Cookie']
        global pds_cookie
        pds_cookie = cookie

        assert resp['status_code'] == 200
        assert pds_cookie != None,'pds_cookie为空'

        html = resp['html']
        pattern = 'value="LT(.+?)" />'
        lt = re.findall(pattern,html)[0]

        global reqCom  #login_get_CASTGC()需要用到
        reqCom = { "_eventId":"submit",
                   "execution":"e1s1",
                   "lt":'LT' + lt ,
                    "password" : pwd ,
                    "productId" : str(be_pid) ,
                    "submit":"%E7%99%BB%E5%BD%95",
                    "username":user}


        with open(headFilePath,'a+') as f:
            f.write( headerManage['pds_cookie'] + splitSymbol + str(pds_cookie) + '\n')

        print( u'pds获得登录cookie成功')


    def login_get_CASTGC(self):
        '''
        单点登录，获得CASTGC,并拼接pds_cookie写入文件
        :return:
        '''

        param = reqCom
        resp = pds().interface_login_post(pds_url,headers_form_urlencoded(pds_cookie), **param)
        assert resp['status_code'] == 200, ' %d error' % resp['status_code']

        Cookie = resp['headers']['Set-Cookie']
        CASTGC = 'CASTGC' + re.findall("CASTGC(.+?) Path=/",Cookie)[0]

        pds_CASTGC_cookie = pds_cookie + ';' + CASTGC

        with open(headFilePath,'a+') as f:
            f.write(headerManage["pds_CASTGC_cookie"] + splitSymbol + pds_CASTGC_cookie + '\n')


    def caslogin_get_serverUrl(self):
        '''
        获得服务的url，并设置为全局变量
        :return:
        '''
        resp = pds().interface_lbws_casLoginService(pds_url,pds_cookie)
        assert resp['status_code'] == 200, ' %d error' % resp['status_code']

        #获得severName为pdsdoc的URL
        pdsDocSeverName = 'pdsdoc'
        pdsCommonServerName = "pdscommon"

        docpos = resp['return_list']['serverName_list'].index(pdsDocSeverName)
        compos = resp['return_list']['serverName_list'].index(pdsCommonServerName)

        global pdsDoceSeverUrl
        global pdsComSeverUrl

        pdsDoceSeverUrl = resp['return_list']['serverURL_list'][docpos]
        pdsComSeverUrl = resp['return_list']['serverURL_list'][compos]

        assert 'http' in pdsDoceSeverUrl,u'pdsDoceSeverUrl获取不正确,为 %s'%pdsDoceSeverUrl
        assert 'http' in pdsComSeverUrl, u'pdsComSeverUrl获取不正确,为 %s' % pdsComSeverUrl

        return u'获得服务器url成功'


    def center_clientUpdate(self):
        '''
        获得当前服务器版本
        :return:
        '''
        resp = center().interface_clientUpdate(pdsComSeverUrl,pds_cookie,user,be_pid)
        assert resp['status_code'] == 200, ' %d error' % resp['status_code']

        #版本号一般为8.2.0,字串长度为5或者更大
        assert len(resp['return']) >= 5,u'服务器版本错误,为 %s'%resp['return']
        return u'获取服务器版本号正常'


    def get_companylist(self):
        '''
        获得企业列表
        :return:
        '''

        resp = pds().interface_casLoginService_getCommpanyList(pds_url,pds_cookie)
        assert resp['status_code'] == 200, ' %d error' % resp['status_code']

        for name in resp['return']['enterpriseName_list']:
            assert name != None and   name !='','公司名字为空 %s'%name

        assert str(Config['epid']) in resp['return']['enterpriseId_list']

    def pds_caslogin(cls):

        resp = pds().interface_casLoginServce_casLogin(pds_url,pds_cookie,Config['epid'])
        assert resp['status_code'] == 200, ' %d error' % resp['status_code']

    def join_all_login_step(cls):
        cls.login_get_cookie()
        cls.login_get_CASTGC()
        cls.caslogin_get_serverUrl()
        cls.center_clientUpdate()
        cls.get_companylist()
        cls.pds_caslogin()

class center_login:

    def get_service_url_from_location(self):
        resp = center().interface_clientConfig(center_url,'')
        return  resp['headers']['Location']


    def get_center_ticket(self):
        serviceUrl = self.get_service_url_from_location()

        pds_CASTGC_match = headerManage['pds_CASTGC_cookie']
        token = read_txt(headFilePath, pds_CASTGC_match, splitSymbol)
        resp = Webrequests.get(serviceUrl, '', headers(token))
        return resp.headers['Location']


    def get_center_cookie(self):
        ticketUrl = self.get_center_ticket()
        resp = Webrequests.get(ticketUrl,'',headers_text_xml())
        center_cookie_value = resp.headers['Set-Cookie']
        with open(headFilePath,'a+') as f:
            f.write(center_cookie_name + splitSymbol + center_cookie_value + '\n')
        print('center获得登陆cookie成功！')

class pdsdoc_login:


    @classmethod
    def get_location_url(cls):
        resp = pdsdoc().proFormModelWebService(pdsdoc_url)
        return  resp.headers['Location']

    @classmethod
    def get_location_ticket(cls):
        serviceUrl = cls.get_location_url()
        pds_CASTGC_match = headerManage['pds_CASTGC_cookie']
        token = read_txt(headFilePath, pds_CASTGC_match, splitSymbol)
        resp = Webrequests.get(serviceUrl,'',headers(token))
        return resp.headers['Location']

    @classmethod
    def get_pdsdoc_cookie(cls):
        ticketUrl = cls.get_location_ticket()
        resp = Webrequests.get(ticketUrl,'',headers_text_xml())
        pdsdoc_cookie_value = resp.headers['Set-Cookie']
        with open(headFilePath,'a+') as f:
            f.write(pdsdoc_cookie_name + splitSymbol + pdsdoc_cookie_value + '\n')
        print(u'pdsdoc获得登陆cookie成功！')

class product_login:

    def BE_lbsca_LoginValidateWebService(self):

        resp = product().BE_LoginValidateWebService(be_url, epid, pwd, be_pid, user)

        # 断言用户角色不为空
        assert len(resp['return']['rolename']) > 1, u'用户角色为空'
        assert len(resp['return']['userProperty']) > 1, u'用户角色为空'
        # 断言返回的用户名同请求的用户名
        assert resp['return']['username'] == user

        with open(headFilePath, 'a+') as f:
            f.write(be_cookie_name  + splitSymbol + resp['headers']['Set-Cookie'] + '\n')
        print(u'%s获得登陆成功！' % be_cookie_name)

    def PLAN_commonlogin(self):
        resp = product().PLAN_ommonlogin(plan_url,epid,pwd,plan_pid,user)
        with open(headFilePath, 'a+') as f:
            f.write(plan_cookie_name  + splitSymbol + resp['headers']['Set-Cookie'] + '\n')
        print(u'%s获得登陆成功！' % plan_cookie_name)

    def prod_login_common_method(self,req_func,name_product_cookie):
        '''
        GOV,CO等登录的公共方法，通过跳转302来最终获得cookie
        :param req_func: 请求返回的响应方法
        :param name_product_cookie: 生成在headertxt中的cookie名字,方便后续产品获取
        :return:
        '''
        #获得service_url from Location
        resp = req_func
        service_url = resp.headers['Location']

        #获得ticket_url
        pds_CASTGC_match = headerManage['pds_CASTGC_cookie']
        token = read_txt(headFilePath, pds_CASTGC_match, splitSymbol)
        resp = Webrequests.get(service_url,'',headers(token))
        ticket_url = resp.headers['Location']

        #获得GOV的cookie
        resp = Webrequests.post(ticket_url,'',headers_text_xml())

        with open(headFilePath,'a+') as f:
            f.write(name_product_cookie  + splitSymbol + resp.headers['Set-Cookie'] + '\n')
        print(u'%s获得登陆成功！'%name_product_cookie)

    def GOV_login(self):
        self.prod_login_common_method(product().GOV_deptmap(gov_url), gov_cookie_name)

    def CO_login(self):
        self.prod_login_common_method(product().CO(co_url),co_cookie_name)

    def join_all_product_login(self):
        self.BE_lbsca_LoginValidateWebService()
        self.PLAN_commonlogin()
        self.GOV_login()
        self.CO_login()











