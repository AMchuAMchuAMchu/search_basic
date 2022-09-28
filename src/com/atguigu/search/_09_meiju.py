# Description ==> TODO
# BelongsProject ==> search_basic
# BelongsPackage ==> 
# Version ==> 1.0
# CreateTime ==> 2022-09-28 21:54:37
# Author ==> _02雪乃赤瞳楪祈校条祭_艾米丽可锦木千束木更七草荠_制作委员会_start

import requests

from bs4 import BeautifulSoup

result = requests.request(method='get',url='https://www.meiju56.com/')

print(result.status_code)

result.encoding = 'utf-8'

movies = BeautifulSoup(result.text,features='html.parser')
i = 0
for item in movies.select('.module-item-title'):
    i += 1
    print(i,'>>',item.text)