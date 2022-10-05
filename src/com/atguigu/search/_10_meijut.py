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

res_bs = BeautifulSoup(result.text,'html.parser')
count = -1
file_save = open(file='d:/meijut.xlsx',encoding='utf-8',mode='w')
for item in res_bs.select('h5'):
    count+=1#第一个不是!!
    if count >= 1:
        file_save.writelines(item.text)
        file_save.write('\n')
        print(count,'>>',item.text)
    pass






