# Description ==> TODO
# BelongsProject ==> search_basic
# BelongsPackage ==> 
# Version ==> 1.0
# CreateTime ==> 2022-10-18 10:27:17
# Author ==> _02雪乃赤瞳楪祈校条祭_艾米丽可锦木千束木更七草荠_制作委员会_start

import re
import numpy  as np
from string import Template
# res = re.findall(pattern='((0\d{2}|0\d{3})-(\d{8}|\d{6}))',string='电话号码021-62232333')
# res01 = list(res)
# print(res01[0][0])

# res02 = re.findall(pattern='\d{1,3}[.]\d{1,3}[.]\d{1,3}[.]\d{1,3}',string='莉可丽丝192.168.200.171果咩~^_^')
# print(res02)

random01 = np.arange(0,256)
# print(random01)
res02 = re.findall(pattern='\d{1,3}[.]\d{1,3}[.]\d{1,3}[.]\d{1,3}',string='莉可丽丝992.168.200.171果咩~^_^')
print(res02)

