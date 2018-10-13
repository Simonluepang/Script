#coding=utf-8

import xmltodict
import json

#定义函数
def pythonXmlToJson(xmlStr):

    convertedDict = xmltodict.parse(xmlStr)
    jsonStr = json.dumps(convertedDict, indent=1)
    return jsonStr

def Recombition_list(keys,data_list):
    '''
    :将list根据key重组
    :param keys:["epid","orgId"]
    :param data_list:
         [{
            "epid": 1,
            "orgId": "7c01a75941549a705cf7275e41b21f0b"

        }, {
            "epid": 713,
            "orgId": "8c01a75941549a705cf7275e41b21f0d"
        }]
    :return:
            result = {'epid_list': [1, 713], 'orgId_list': ['7c01a75941549a705cf7275e41b21f0b', '8c01a75941549a705cf7275e41b21f0d']}
    '''

    result = {}

    for key in keys:
        result[key+"_list"] = []

    for data in data_list:
        for key in keys:
            result[key +"_list"].append(data.get(key))
    return result

def resp_base(data):
    result = {}
    result["status_code"] = data.status_code
    result['headers'] = data.headers
    return result

class resp_webservice:
    def resp_login_get(self,data):
        result = resp_base(data)
        result['html'] = data.text
        return result

    def resp_login_post(self,data):
        result = resp_base(data)
        return result


    def resp_lbws_casLoginService_getServUrlResponse(self,data):
        result = resp_base(data)
        json_data = eval(pythonXmlToJson(data.text))
        severUrl_list = json_data.get("soap:Envelope").get( 'soap:Body').get('ns2:getServUrlResponse').get('return')

        key_list = ['serverName','serverURL']
        result['return_list'] = Recombition_list(key_list,severUrl_list)
        return result

    def resp_casLoginService_getCommpanyList(self,data):
        result = resp_base(data)
        json_data = eval(pythonXmlToJson(data.text))
        severUrl_list = json_data.get("soap:Envelope").get( 'soap:Body').get('ns2:getCompanyListResponse').get('return')

        key_list = ['enterpriseId','enterpriseName']
        result['return'] = Recombition_list(key_list,severUrl_list)
        return result

    def resp_casLoginService_casLogin(self,data):
        result = resp_base(data)
        json_data = eval(pythonXmlToJson(data.text))
        result['return'] = json_data.get("soap:Envelope").get('soap:Body').get('ns2:casLoginResponse').get('return')
        return result

class resp_center:
    def resp_clientUpdate(self,data):
        result = resp_base(data)
        json_data = eval(pythonXmlToJson(data.text))
        result['return'] = json_data.get("soap:Envelope").get( 'soap:Body').get('ns2:getServerVersionResponse').get('return')
        return result

    def resp_clientConfig(self,data):
        result = resp_base(data)
        return result

class resp_product:
    def resp_BE_LoginValidateWebService(self,data):
        result = resp_base(data)
        json_data = eval(pythonXmlToJson(data.text))
        result['return'] = json_data.get("soap:Envelope").get( 'soap:Body').get('ns2:loginBEResponse').get('return')
        return result

    def resp_PLAN_ommonlogin(self,data):
        result = resp_base(data)
        json_data = eval(pythonXmlToJson(data.text))
        result['return'] = json_data.get("soap:Envelope").get( 'soap:Body').get('ns2:login2018Response').get('return')
        return result



if __name__ =="__main__":
    data = '''
    <soap:Envelope xmlns:soap="http://schemas.xmlsoap.org/soap/envelope/">
    <soap:Body>
        <ns2:getServUrlResponse xmlns:ns2="http://login.webservice.login.sso.lubansoft.com/">
            <return>
                <serverName>pdscommon</serverName>
                <serverURL>http://center.lubansoft.com/pdscommon</serverURL>
            </return>
            <return>
                <serverName>pdsdoc</serverName>
                <serverURL>http://pdsdoc.lubansoft.com</serverURL>
            </return>
            <return>
                <serverName>LBBV</serverName>
                <serverURL>http://bv.lubansoft.com</serverURL>
            </return>
            <return>
                <serverName>EDS</serverName>
                <serverURL>http://center.lubansoft.com</serverURL>
            </return>
            <return>
                <serverName>pds</serverName>
                <serverURL>http://pds.lubansoft.com</serverURL>
            </return>
            <return>
                <serverName>bimco</serverName>
                <serverURL>http://bimco.lubansoft.com</serverURL>
            </return>
            <return>
                <serverName>msgPush</serverName>
                <serverURL>http://msgpush.lubansoft.com</serverURL>
            </return>
            <return>
                <serverName>msgPushRealtime</serverName>
                <serverURL>http://msgpushrt.lubansoft.com:80/subs</serverURL>
            </return>
            <return>
                <serverName>LBBE</serverName>
                <serverURL>http://be3.lubansoft.com</serverURL>
            </return>
            <return>
                <serverName>LBBW</serverName>
                <serverURL>http://bw.lubansoft.com</serverURL>
            </return>
            <return>
                <serverName>LBMC</serverName>
                <serverURL>http://govern.lubansoft.com</serverURL>
            </return>
            <return>
                <serverName>data</serverName>
                <serverURL>http://mc.lubansoft.com/data</serverURL>
            </return>
            <return>
                <serverName>LBSP</serverName>
                <serverURL>http://plan.lubansoft.com</serverURL>
            </return>
            <return>
                <serverName>feedback</serverName>
                <serverURL>http://175.102.128.138:9011</serverURL>
            </return>
            <return>
                <serverName>boss</serverName>
                <serverURL>http://boss.lubansoft.com</serverURL>
            </return>
            <return>
                <serverName>BZCLS</serverName>
                <serverURL>http://eds.nestsoft.com.cn/banzhucls</serverURL>
            </return>
            <return>
                <serverName>BZCLSPage</serverName>
                <serverURL>http://eds.nestsoft.com.cn/banzhucls</serverURL>
            </return>
            <return>
                <serverName>LBIM</serverName>
                <serverURL>http://127.0.0.1</serverURL>
            </return>
            <return>
                <serverName>ZY</serverName>
                <serverURL>http://175.102.128.132:8080</serverURL>
            </return>
            <return>
                <serverName>myluban</serverName>
                <serverURL>http://www.myluban.com/myluban</serverURL>
            </return>
            <return>
                <serverName>blender</serverName>
                <serverURL>http://api.lubansoft.com/blender</serverURL>
            </return>
            <return>
                <serverName>ac</serverName>
                <serverURL>http://passport.luban.com</serverURL>
            </return>
        </ns2:getServUrlResponse>
    </soap:Body>
</soap:Envelope>
'''
    print(resp_webservice().resp_lbws_casLoginService(data))

    data = '''<soap:Envelope xmlns:soap="http://schemas.xmlsoap.org/soap/envelope/">
    <soap:Body>
        <ns2:getCompanyListResponse xmlns:ns2="http://login.webservice.login.sso.lubansoft.com/">
            <return>
                <enterpriseId>-1</enterpriseId>
                <enterpriseName>鲁班建设集团</enterpriseName>
            </return>
            <return>
                <enterpriseId>1</enterpriseId>
                <enterpriseName>鲁班软件研发中心</enterpriseName>
            </return>
            <return>
                <enterpriseId>713</enterpriseId>
                <enterpriseName>云部署企业数据移植</enterpriseName>
            </return>
        </ns2:getCompanyListResponse>
    </soap:Body>
</soap:Envelope>'''
    print(resp_webservice().resp_casLoginService_getCommpanyList(data))
