import requests, json, re

class BWadmin(object):
	'''BW登录'''
	def __init__(self):
		pass

	def admin(self):
		"""清理已标记删除的合同"""
		# Login(登录pds-GET)
		PDS_URL = 'http://192.168.13.210:8080/pds'
		r1 = requests.get(url=PDS_URL+'/login')
		# 查询Cookie_pds
		Cookie_pds = r1.headers['Set-Cookie']
		text1 = r1.text

		# 查找含有LT的这行string，截取出来
		compile1 = re.compile(r'      <input type="hidden" name="lt" value="LT.*? />')
		find_LT = compile1.findall(text1)
		ltvalue = find_LT[0]
		ltvalue = list(ltvalue)
		ltvalue = ltvalue[44:-4]
		ltvalue = ('').join(ltvalue)

		# Login(登录pds-POST)
		logindata0 = {
			'_eventId' : 'submit',
			'execution' : 'e1s1',
			'lt' : ltvalue,
			'password' : '96e79218965eb72c92a549dd5a330112',
			'productId' : '40',
			'submit' : '%E7%99%BB%E5%BD%95',
			'username' : 'xushenwei',
			}
		loginheaders0 = {
			'Cookie' : Cookie_pds,
			'REQUEST' : 'application/x-www-form-urlencoded'
			}
		r2 = requests.post(url=PDS_URL+'/login', data=logindata0, headers=loginheaders0)

		# 查询TGT
		Set_Cookie = r2.headers['Set-Cookie']
		TGT = list(Set_Cookie)
		TGT = TGT[66:-12]
		TGT = ('').join(TGT)

		# 获取URL
		r3 = requests.get(url=PDS_URL+'/webservice/lbws/casLoginService', data=logindata0, headers=loginheaders0)
		text2 = r3.text
		print(text2)
		'''
		# Method1(LBLD跳转)
		logindata1 = {
			'service' : 'http://192.168.13.215:8082/LBIM/webservice/lbws/contractlistservice?wsdl&qwea'
			}
		loginheaders1 = {
			'Cookie' : Cookie_pds+';'+TGT,
			}
		# 这一步会有网页自动跳转，添加参数以防止自动跳转来抓取location
		r3 = requests.post(url=PDS_URL+'/login', data=logindata1, headers=loginheaders1, allow_redirects = False)
		LBLD_URL_302 = r3.headers['Location']

		# LBLD_URL_302(跳转)
		logindata2 = {
			'function' : '登录',
			'functionGroup' : '打开软件'
			}
		r4 = requests.post(url=LBLD_URL_302, data=logindata2, allow_redirects = False)
		Cookie_LBLD = r4.headers['Set-Cookie']
		# print(Cookie_LBLD)
		'''


if __name__ == '__main__':
	BA = BWadmin()
	BA.admin()