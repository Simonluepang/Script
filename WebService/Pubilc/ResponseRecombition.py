#coding=utf-8

def resp_base(response):
	#提取接口返回的状态码以及headers
	result = {}
	result["status_code"] = response.status_code
	result["headers"] = response.headers
	return result

def Recombition_list(keys, data_list):
	# 将list根据key重组
	'''
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
			result[key+"_list"].append(data.get(key))

	return result

def Recombition(keys, data_list):
	# 将list中的项作为key，该项的位置作为value保存在dict中
	'''
    :param keys:['first','last','number']
    :param data_List:{
                        'first':0,
                        'last':1,
                        'number':2
    }
    :return:
            result:{"first":0,"last":1,'number':2}
    '''
	result = {}

	for key in keys:
		result[key] = data_list.get(key)

	return result

class Public_Response(object):
	def msg_data_code(self,data):
		try:
			result = resp_base(data)
			context = data.json()
			result['code'] = context.get('code')
			result['msg'] = context.get('msg')
			result['data'] = context.get('data')
			return result
		except BaseException as e:
			return str(e)

class Response_url_controler(Public_Response):
	def resp_provinceAndCity(self, data):
		try:
			result = self.msg_data_code(data)

			#拆解data下的city
			cities = result['data'].get('cities')
			cities_keys = ['city', 'cityId', 'provinceId']
			result['data_cities_list'] = Recombition_list(cities_keys, cities)

			#拆解data下的province

			#拆解data下的countries

			return result
		except BaseException as e:
			return str(e)


class Response_project_dashboard(Public_Response):
	def resp_showListProjectDashboard(self,data):
		try:
			result = self.msg_data_code(data)

			#拆解data
			keys = ['epid', 'footprint', 'logoUrl', 'orgId', 'orgName', 'projects', 'space', 'subAdmin', 'superAdmin', 'title']
			result['data_list'] = Recombition_list(keys, result['data'])
			return result
		except BaseException as e:
			return str(e)


class Response_user_controller(Public_Response):
	def resp_user_list_prjects(self,data):
		try:
			result = self.msg_data_code(data)

			#拆解data
			data_keys = ['area','cityId','cityName','contractType','countyId','countyName','endDate','endDateStr','epid','id','location','logo','logoUrl=','managerName','mileage','mobile','name','parentId',
                     'provinceId','provinceName','remarks','sortStatus','startDate','startDateStr','status']
			result['data_list'] = Recombition_list(data_keys, result['data'])
			return result
		except BaseException as e:
			return str(e)


class Response_feedback_controller(Public_Response):
	def resp_feedback_type(self,data):
		try:
			result = self.msg_data_code(data)

			#拆解data
			data_keys = ['typeId', 'typeName']
			result['data_list'] = Recombition_list(data_keys, result['data'])
			return result
		except BaseException as e:
			return str(e)
