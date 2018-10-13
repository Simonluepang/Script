#coding=utf-8
from public.CommonLoginResp import *

class resp_lbws:
    def LoginValidateWebService(self,data):
        result = resp_base(data)
        json_data = eval(pythonXmlToJson(data.text))
        result['return'] = json_data.get("soap:Envelope").get( 'soap:Body').get('ns2:loginBEResponse').get('return')
        return result

class resp_address:
    def serviceAddress(self,data):

        result = resp_base(data)
        try:
            json_data = eval(pythonXmlToJson(data.text))
            result['return'] = json_data.get("soap:Envelope").get( 'soap:Body').get('ns2:getServUrlResponse').get('return')
            return result
        except Exception :
            print(result)


