# -*- coding = utf-8 -*-
# @Time : 2022/9/6 9:56
# @Author : 02雪乃赤瞳楪祈校条祭制作委员会
# @File : _03_requests.py
# @Software : PyCharm

import requests as rqs

# response = rqs.request('get','https://bilibili.com')
response = rqs.request('get','https://www.bilibili.com/video/BV1r14y1s76N?spm_id_from=333.337.search-card.all.click&vd_source=70a16752cc0517b09c4df99e0c2fa14a')

print(' >> ',response.ok)


# print("status::",response.status_code)
#
# print("url::",response.url)
#
# print("headers::",response.headers)
#
# print("cookies::",response.cookies)
#
# print("text::",response.text)
#
# file = open(r'D:\seldom\rd\Python_ProjectAll\search_basic\src\com\atguigu\assets\_01_bilibili.txt',mode='w',encoding='utf8')
#
# file.write(response.text)
#
# print("content::",response.content)
































