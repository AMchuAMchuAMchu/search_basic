# -*- coding = utf-8 -*-
# Description==>TODO
# BelongsProject==>search_basic
# BelongsPackage==>
# CreateTime==>2022-09-11 21:16:59
# Version==>1.0
# Author==>02雪乃赤瞳楪祈校条祭制作委员会
# Software==>PyCharm

import requests

from lxml import etree

from bs4 import BeautifulSoup

# html = rqs.request('get',r'https://www.baidu.com')
#
# # print(html.text)
#
# etree = etree.HTML(html.text)

headers = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.5112.102 Safari/537.36 Edg/104.0.1293.70'}

# 爬取第一财经的网页信息
# response = requests.get('https://www.yicai.com/')

# 爬取百度热搜的信息
response = requests.request(method='get',
url='https://top.baidu.com/board?platform=pc&sa=pcindex_entry',headers=headers)

print(response.ok)

print(response.status_code)

response.encoding = 'utf-8'


soup = BeautifulSoup(response.text,'html.parser')

for history in soup.select('.item-wrap_2oCLZ'):
    print(history.select('.c-single-text-ellipsis'))


# 对爬取到的第一次财经的信息进行处理...
# for news in soup.select('.m-list'):
#     print(news.select('h2'))

# for news in soup.select('.m-list'):
#     print(news.select('h2')[0])
#
# for news in soup.select('.m-list'):
#     print(news.select('h2')[0].text)


























