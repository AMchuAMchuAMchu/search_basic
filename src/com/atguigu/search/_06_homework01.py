# -*- coding = utf-8 -*-
# Description==>TODO
# BelongsProject==>search_basic
# BelongsPackage==>
# CreateTime==>2022-09-14 07:14:21
# Version==>1.0
# Author==>02雪乃赤瞳楪祈校条祭制作委员会
# Software==>PyCharm

import requests

from bs4 import BeautifulSoup

result = requests.request(method='get', url='https://www.shanghairanking.cn/rankings/bcur/2022')

print(result.status_code)

print(result.ok)

result.encoding = 'utf-8'

soup = BeautifulSoup(markup=result.text, features='html.parser')
print('排名    学校名称      EN             brand        省市   类型   总分')
print()

# 爬取大学信息
i = 0
for info in soup.select('tr'):
    i += 1  # 因为前面有一个tr标签不是包括大学的所以需要过滤掉...
    if i > 1:
        rank = info.select('td')[0].text.strip()#排名
        name_en_b = info.select('td')[1].text.strip().split(' ')# 学校名称,英语名称,brand
        cn_name = name_en_b[0]
        en_name = name_en_b[4]
        brand = name_en_b[len(name_en_b)-1]
        address = info.select('td')[2].text.strip()#省市
        type = info.select('td')[3].text.strip()#办学类型
        score = info.select('td')[4].text.strip()#得分
        print(rank,'    ',cn_name,'    ',en_name,'    ',brand,' ',address,' ',type,' ',score)