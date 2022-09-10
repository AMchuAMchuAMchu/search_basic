# -*- coding = utf-8 -*-
# @Time : 2022/9/6 9:35
# @Author : 02雪乃赤瞳楪祈校条祭制作委员会
# @File : _02_basic02.py
# @Software : PyCharm

import urllib3 as ul3

import requests as rq

rq.packages.urllib3.disable_warnings()

http = ul3.PoolManager()

headers = {'user-agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.5112.102 Safari/537.36 Edg/104.0.1293.70'}

response = http.request('get','https://www.bilibili.com/?vd_source=70a16752cc0517b09c4df99e0c2fa14a',headers=headers)

print("status::",response.status)

print("data::",response.data.decode('utf8'))








