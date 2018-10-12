#coding=utf-8

def reso_base(response):
	#提取接口返回的状态码以及headers
	result = {}
	result["status_code"] = response.status_code
	result["headers"] = response.headers
	return result

def recombition_list(keys, data_list):
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

def recombition_dict(keys, data_list):
	# 将key放入dict中
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