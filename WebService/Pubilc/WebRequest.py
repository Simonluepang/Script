#!/usr/bin/env python 
# -*- coding:utf-8 -*-
import requests, json, warnings
warnings.filterwarnings("ignore")

# 为什么要添加session这个方法？
session = requests.session()
# 这个keep_alive是有什么作用？
session.keep_alive = False

class Webrequests(object):

    def get(self, url, params, headers):
        try:
            r = session.get(url, params=params, headers=headers, verify=False, allow_redirects=False)
            return r
        except BaseException as e:
            print("Response failed!", str(e))
        finally:
            print(r.status_code)

    def post(self, url, params, headers):
        try:
            r = session.post(url, params=params, headers=headers, verify=False, allow_redirects=False)
            return r
        except BaseException as e:
            print("Response failed!", str(e))
        finally:
            print(r.status_code)

    def post_json(self, url, params, headers):
        try:
            data = json.dumps(params)   # Python数据类型转化为json数据类型
            r = session.post(url, data=data, headers=headers, verify=False, allow_redirects=False)
            return r
        except BaseException as e:
            print("Response failed!", str(e))
        finally:
            print(r.status_code)

    def delete(self, url, params, headers):
        try:
            data = json.dumps(params)
            r = session.delete(url, data=data, headers=headers, verify=False, allow_redirects=False)
            return r
        except BaseException as e:
            print("Response failed!", str(e))
        finally:
            print(r.status_code)

    def put(self, url, params, headers):
        try:
            data = json.dumps(params)
            r = session.put(url, data=data, headers=headers, verify=False, allow_redirect=False)
            return r
        except BaseException as e:
            print("Response failed!", str(e))
        finally:
            print(r.status_code)
