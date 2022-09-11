# -*- coding = utf-8 -*-
# @Time : 2022/9/6 8:19
# @Author : 02雪乃赤瞳楪祈校条祭制作委员会
# @File : _01_request.py
# @Software : PyCharm

import urllib.request as rq

response = rq.urlopen('https://www.baidu.com') # type:HTTPResponse

# print("type >> ",type(response))
#
# print("地址信息 >> ",response)
#
# print("头部信息01 >> ",response.info())
#
# print("头部信息02 >> ",response.getheaders())
#
# print("头部属性信息 >> ",response.getheader("Server"))
#
# print("status >> ",response.status)
#
# print("status >>> "+(str)(response.status))

# print("查看信息 >> ",response.getcode())
#
# print("geturl >> ",response.geturl())
#

page = response.read()

print(page.decode('utf-8'))















