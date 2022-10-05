# Description ==> TODO
# BelongsProject ==> search_basic
# BelongsPackage ==> 
# Version ==> 1.0
# CreateTime ==> 2022-10-05 20:38:52
# Author ==> _02雪乃赤瞳楪祈校条祭_艾米丽可锦木千束木更七草荠_制作委员会_start


import requests
from bs4 import BeautifulSoup

result = requests.request(method='get',url='http://meijut.cc/label/hit.html')

print(result.status_code)

result.encoding = 'utf-8'








