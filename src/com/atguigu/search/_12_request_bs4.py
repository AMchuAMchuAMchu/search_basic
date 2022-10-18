# Description ==> TODO
# BelongsProject ==> search_basic
# BelongsPackage ==> 
# Version ==> 1.0
# CreateTime ==> 2022-10-18 11:11:25
# Author ==> _02雪乃赤瞳楪祈校条祭_艾米丽可锦木千束木更七草荠_制作委员会_start

from bs4 import BeautifulSoup
import requests


res01 = requests.request(method='get',url='https://top.baidu.com/board')

print(res01.ok)

res01.encoding = 'utf-8'

_res01 = BeautifulSoup(res01.text,'html.parser')

count = 0
page = 0
for item in _res01.select('.c-single-text-ellipsis'):
    if count % 2 == 0:
        page += 1
        print(page,' >> ',item.text)
    count += 1

