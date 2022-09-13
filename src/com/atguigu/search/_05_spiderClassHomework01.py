# -*- coding = utf-8 -*-
# Description==>TODO
# BelongsProject==>search_basic
# BelongsPackage==>
# CreateTime==>2022-09-13 09:39:57
# Version==>1.0
# Author==>02雪乃赤瞳楪祈校条祭制作委员会
# Software==>PyCharm


import requests

from bs4 import BeautifulSoup

response = requests.request(method='get', url='https://www.shanghairanking.cn/rankings/bcur/2022')

print(response.status_code)

response.encoding = 'utf-8'

soup = BeautifulSoup(response.text, 'html.parser')
rank = 0
# TODO 去掉重复的大学英文名的说...比如:"清华大学" 其实的话在控制台还打印了英文的"Tsinghua University"...这个就显得冗余了....
for university in soup.select('.link-container'):
    rank += 1
    print('Number',rank, university.select('a')[0].text.strip())


