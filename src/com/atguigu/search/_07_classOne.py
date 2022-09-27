# -*- coding = utf-8 -*-
# Description==>TODO
# BelongsProject==>search_basic
# BelongsPackage==>
# CreateTime==>2022-09-20 09:08:28
# Version==>1.0
# Author==>02雪乃赤瞳楪祈校条祭制作委员会
# Software==>PyCharm


import urllib3
import requests
# 忽略警告
requests.packages.urllib3.disable_warnings()
# 一个PoolManager实例来生成请求
http = urllib3.PoolManager()
# 通过request()方法创建一个请求：
response = http.request('GET', 'http://www.baidu.com/')
print(response.status)   # 响应状态200
# 获得html源码,utf-8解码
print(response.data.decode())


