import sys
sys.path.append('..')

from public.WebRequest import  Webrequests
from public.ReqParam import *
from public.ResponseRecombition import *
Webrequests = Webrequests()

def headers(token):

    headers = {
                "Cookie": token}

    return headers

def headers_application_json(token):

    headers = {
                "Cookie": token,
                'Content-type': 'application/json'}

    return headers

def headers_no_token():
    headers = {'Content-type': 'application/json'}
    return headers

def headers_text_xml(token):
    headers = {'Content-type': 'text/xml',
               "Cookie":token}
    return headers

class lbsca:
    def LoginValidateWebService(self,url,token,epid,pwd,pid,user):
        url = url +  '/webservice/lbsca/LoginValidateWebService'
        req_xml = req_lbws().LoginValidateWebService(epid,pwd,pid,user)
        return resp_lbws().LoginValidateWebService(Webrequests.post(url,req_xml,headers_text_xml(token)))

class address:
    def serviceAddress(self,url,token,severname):
        url = url + '/webservice/address/serviceAddress'
        req_xml = req_address().serviceAddress(severname)
        return resp_address().serviceAddress(Webrequests.post(url,req_xml,headers_text_xml(token)))



