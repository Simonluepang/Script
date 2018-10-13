#coding=utf-8

class req_lbws:
    def LoginValidateWebService(self,epid,pwd,pid,user):
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
'''%(epid,pwd,pid,user)
        return req_xml

class req_address:
    def serviceAddress(self,servername):
        req_xml = '''
        <SOAP-ENV:Envelope xmlns:SOAP-ENV="http://schemas.xmlsoap.org/soap/envelope/" xmlns:SOAP-ENC="http://schemas.xmlsoap.org/soap/encoding/" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xmlns:xsd="http://www.w3.org/2001/XMLSchema" xmlns:ns1="http://address.webservice.be.lubansoft.com/">
    <SOAP-ENV:Body>
        <ns1:getServUrl>
            <serverNames>%s</serverNames>
        </ns1:getServUrl>
    </SOAP-ENV:Body>
</SOAP-ENV:Envelope>
'''%servername
        return req_xml