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

result = requests.request(method='get',url='https://www.shanghairanking.cn/rankings/bcur/2022')

print(result.status_code)

print(result.ok)

result.encoding = 'utf-8'

soup = BeautifulSoup(markup=result.text,features='html.parser')
rank = 0
print('排名    学校名称   省市    总分')
print()
for university in soup.select('.name-cn'):
    rank += 1
    print(rank,'    ',university.text.strip(),'    ',)












