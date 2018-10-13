#coding=utf-8
from Setting import *
from public.WebRequest import *
from public.CommonReqParam import *
from public.CommonLoginResp import *

Webrequests = Webrequests()

def head_text_xml(token):
    headers = {'Content-type': 'text/xml',
               "Cookie": 'JSESSIONID='+ token +';'}
    return headers

def headers(token):
    headers = {"Cookie": token}
    return headers

def headers_no_token():
    headers = {'Content-type': 'application/json'}
    return headers

def headers_form_urlencoded(token):
    headers = {"Cookie": token,
               'Content-type': 'application/x-www-form-urlencoded'}
    return headers

def headers_text_xml(token=None):
    headers = {'Content-type': 'text/xml',
               "Cookie": token}
    return headers



class center:
    def interface_clientUpdate(self,url,token,username,pid,**kwargs):
        url = url + '/webservice/common/clientUpdate'
        req_xml = req_center().req_clentUpdate(username,pid)
        resp_xml = Webrequests.post(url,req_xml,headers_text_xml(token))
        return resp_center().resp_clientUpdate(resp_xml)

    def interface_clientConfig(self,url,token,**kwargs):
        url = url + '/pdscommon/webservice/lbws/clientConfig'
        req_xml = req_center().req_clientConfig()
        resp_xml = Webrequests.post(url,req_xml,headers_text_xml(token))
        return resp_center().resp_clientConfig(resp_xml)


class pds:
    def interface_login_get(self,url, token=None, **kwargs):
        url = url + "/login?"
        return resp_webservice().resp_login_get(Webrequests.get(url, kwargs, token))

    def interface_login_post(self,url, token=None, **kwargs):
        url = url + "/login?"
        return resp_webservice().resp_login_post(Webrequests.post(url, kwargs, token))


    def interface_casLoginService_getCommpanyList(self,url,token):
        url = url + '/webservice/lbws/casLoginService'
        req_xml = req_webservice().req_casLoginService_getCommpanyList()
        resp_xml = Webrequests.post(url,req_xml,headers_text_xml(token))
        return resp_webservice().resp_casLoginService_getCommpanyList(resp_xml)

    def interface_casLoginServce_casLogin(self,url,token,epid):
        url = url + '/webservice/lbws/casLoginService'
        req_xml = req_webservice().req_casLoginService_casLogin(epid)
        resp_xml =  Webrequests.post(url,req_xml,headers_text_xml(token))
        return resp_webservice().resp_casLoginService_casLogin(resp_xml)

    def interface_lbws_casLoginService(self,url, token, **kwargs):
        url = url + '/webservice/lbws/casLoginService'
        req_xml = req_webservice().req_lbws_casLoginService()
        resp_xml = Webrequests.post(url, req_xml, headers_text_xml(token))
        return resp_webservice().resp_lbws_casLoginService_getServUrlResponse(resp_xml)


class product:
    def BE_LoginValidateWebService(self, url, epid, pwd, pid, user, token=None):
        url = url + '/webservice/lbsca/LoginValidateWebService'
        req_xml = req_product().req_BE_LoginValidateWebService(epid, pwd, pid, user)
        return resp_product().resp_BE_LoginValidateWebService(Webrequests.post(url, req_xml, headers_text_xml(token)))

    def GOV_deptmap(self,url,token=None):
        url = url +  '/webservice/managecontrol/deptMap'
        req_xml = req_product().req_GOV_deptmap()
        return Webrequests.post(url,req_xml,headers_text_xml(token))

    def CO(self,url,token=None):
        return Webrequests.get(url,'',token)

    def PLAN_ommonlogin(self, url, epid, pwd, pid, user, token=None):
        url = url + '/webservice/login/commonlogin'
        req_xml = req_product().req_PLAN_ommonlogin(epid,pwd,pid,user)
        return resp_product().resp_PLAN_ommonlogin(Webrequests.post(url, req_xml, headers_text_xml(token)))

class pdsdoc:
    def proFormModelWebService(self,url,token=None):
        url = url + '/webservice/document/projFormModelWebService'
        req_xml = req_pdsdoc().req_projFormModelWebService()
        return Webrequests.post(url,req_xml, headers_text_xml(token))


if __name__ == '__main__':
    print(pdsdoc().proFormModelWebService('http://pdsdoc.lubansoft.com').headers)







