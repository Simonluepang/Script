
class req_webservice:
    def req_lbws_casLoginService(self):

        req_xml = '''
        <SOAP-ENV:Envelope xmlns:SOAP-ENV="http://schemas.xmlsoap.org/soap/envelope/" xmlns:SOAP-ENC="http://schemas.xmlsoap.org/soap/encoding/" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xmlns:xsd="http://www.w3.org/2001/XMLSchema" xmlns:SASS="http://login.webservice.login.sso.lubansoft.com/">
            <SOAP-ENV:Body>
                <SASS:getServUrl/>
            </SOAP-ENV:Body>
        </SOAP-ENV:Envelope>
        '''
        return req_xml

    def req_casLoginService_getCommpanyList(self):
        req_xml = '''
        <SOAP-ENV:Envelope xmlns:SOAP-ENV="http://schemas.xmlsoap.org/soap/envelope/" xmlns:SOAP-ENC="http://schemas.xmlsoap.org/soap/encoding/" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xmlns:xsd="http://www.w3.org/2001/XMLSchema" xmlns:SASS="http://login.webservice.login.sso.lubansoft.com/">
        <SOAP-ENV:Body>
            <SASS:getCompanyList/>
        </SOAP-ENV:Body>
        </SOAP-ENV:Envelope>
        '''
        return req_xml

    def req_casLoginService_casLogin(self,epid):
        req_xml = '''
        <SOAP-ENV:Envelope xmlns:SOAP-ENV="http://schemas.xmlsoap.org/soap/envelope/" xmlns:SOAP-ENC="http://schemas.xmlsoap.org/soap/encoding/" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xmlns:xsd="http://www.w3.org/2001/XMLSchema" xmlns:SASS="http://login.webservice.login.sso.lubansoft.com/">
    <SOAP-ENV:Body>
        <SASS:casLogin>
            <param xsi:type="SASS:pdsLoginParam">
                <hardwareCodes>49148c4de728a29f95f561f85243385f-d0b7ebe000d64b4e31cb7ca6b13a010d</hardwareCodes>
                <innetIp>192.168.99.1</innetIp>
                <platform>pc64</platform>
                <systemVersion/>
                <version>8.2.0</version>
                <epid>%s</epid>
            </param>
        </SASS:casLogin>
    </SOAP-ENV:Body>
</SOAP-ENV:Envelope>
        '''%epid
        return req_xml

class req_center:
    def req_clentUpdate(self,username,pid):
        req_xml = '''
        <SOAP-ENV:Envelope xmlns:SOAP-ENV="http://schemas.xmlsoap.org/soap/envelope/" xmlns:SOAP-ENC="http://schemas.xmlsoap.org/soap/encoding/" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xmlns:xsd="http://www.w3.org/2001/XMLSchema" xmlns:CUpdate="http://webservice.clientupdate.pdscommon.lubansoft.com/">
    <SOAP-ENV:Body>
        <CUpdate:getServerVersion>
            <username>%s</username>
            <productId>%s</productId>
        </CUpdate:getServerVersion>
    </SOAP-ENV:Body>
</SOAP-ENV:Envelope>
        '''%(username,str(pid))
        return req_xml

    def req_clientConfig(self):
        req_xml = '''
        <SOAP-ENV:Envelope xmlns:SOAP-ENV="http://schemas.xmlsoap.org/soap/envelope/" xmlns:SOAP-ENC="http://schemas.xmlsoap.org/soap/encoding/" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xmlns:xsd="http://www.w3.org/2001/XMLSchema" xmlns:CLIENTCFGSERVICE="http://webservice.clientconfig.pdscommon.lubansoft.com/">
    <SOAP-ENV:Body>
        <CLIENTCFGSERVICE:getUserConfig>
            <param>
                <ppid>0</ppid>
                <type>2</type>
                <wsid>0</wsid>
            </param>
            <keyList>hoops_bsd</keyList>
            <keyList>hoops_bbl</keyList>
            <keyList>hoops_bao</keyList>
            <keyList>hoops_bfse</keyList>
            <keyList>hoops_bfr</keyList>
            <keyList>hoops_bli</keyList>
        </CLIENTCFGSERVICE:getUserConfig>
    </SOAP-ENV:Body>
</SOAP-ENV:Envelope>
'''
        return req_xml

class req_pdsdoc:
    def req_projFormModelWebService(self):
        req_xml = '''
        <SOAP-ENV:Envelope xmlns:SOAP-ENV="http://schemas.xmlsoap.org/soap/envelope/" xmlns:SOAP-ENC="http://schemas.xmlsoap.org/soap/encoding/" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xmlns:xsd="http://www.w3.org/2001/XMLSchema" xmlns:ZYDOCOPER="http://webservice.zydoc.pdsdoc.lubansoft.com/">
        <SOAP-ENV:Body>
            <ZYDOCOPER:findUserZyFormModels/>
        </SOAP-ENV:Body>
        </SOAP-ENV:Envelope>
    '''
        return req_xml

class req_product:
        def req_BE_LoginValidateWebService(self, epid, pwd, pid, user):
            req_xml = '''
            <SOAP-ENV:Envelope xmlns:SOAP-ENV="http://schemas.xmlsoap.org/soap/envelope/" xmlns:SOAP-ENC="http://schemas.xmlsoap.org/soap/encoding/" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xmlns:xsd="http://www.w3.org/2001/XMLSchema" xmlns:ns1="http://login.webservice.be.lubansoft.com/">
        <SOAP-ENV:Body>
            <ns1:loginBE>
                <loginParam>
                    <admin>true</admin>
                    <enterpriseId>%s</enterpriseId>
                    <hardwareCodes>49148c4de728a29f95f561f85243385f-d0b7ebe000d64b4e31cb7ca6b13a010d</hardwareCodes>
                    <innetIp>192.168.99.1</innetIp>
                    <password>%s</password>
                    <productId>%s</productId>
                    <username>%s</username>
                    <version/>
                </loginParam>
            </ns1:loginBE>
        </SOAP-ENV:Body>
    </SOAP-ENV:Envelope>
    ''' % (epid, pwd, pid, user)
            return req_xml

        def req_GOV_deptmap(self):
            req_xml = '''
                    <?xml version="1.0" encoding="UTF-8"?>
            <SOAP-ENV:Envelope xmlns:SOAP-ENV="http://schemas.xmlsoap.org/soap/envelope/" xmlns:SOAP-ENC="http://schemas.xmlsoap.org/soap/encoding/" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xmlns:xsd="http://www.w3.org/2001/XMLSchema" xmlns:PROJDEPTINFO="http://webservice.managecontrol.pdsmc.lubansoft.com/">
                <SOAP-ENV:Body>
                    <PROJDEPTINFO:getProvinceInfo/>
                </SOAP-ENV:Body>
            </SOAP-ENV:Envelope>
            '''
            return req_xml

        def req_PLAN_ommonlogin(self,epid, pwd, pid, user):
            req_xml = '''
            <SOAP-ENV:Envelope xmlns:SOAP-ENV="http://schemas.xmlsoap.org/soap/envelope/" xmlns:SOAP-ENC="http://schemas.xmlsoap.org/soap/encoding/" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xmlns:xsd="http://www.w3.org/2001/XMLSchema" xmlns:COMMONLOGIN="http://webservice.login.pds.lubansoft.com/">
    <SOAP-ENV:Body>
        <COMMONLOGIN:login2018>
            <loginParam>
                <enterpriseId>%s</enterpriseId>
                <hardwareCodes>49148c4de728a29f95f561f85243385f-d0b7ebe000d64b4e31cb7ca6b13a010d</hardwareCodes>
                <innetIp>192.168.99.1</innetIp>
                <password>%s</password>
                <username>%s</username>
                <version>4.5.0</version>
            </loginParam>
            <productId>%s</productId>
        </COMMONLOGIN:login2018>
    </SOAP-ENV:Body>
</SOAP-ENV:Envelope>
            '''%(epid,pwd,user,pid)
            return req_xml
