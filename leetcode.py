import codecs
import re

import numpy as np
import csv
#包含了从文本中截取数字，和画图的一些技巧。
f1 = codecs.open('FB2010-1Hr-150-0.txt', mode='r', encoding='utf-8')  # 打开txt文件，以‘utf-8’编码读取


line1 = f1.readline()   # 以行的形式进行读取文件
line1 = f1.readline()
list1 = []
ans=0
while line1:
    a = line1.split()
    num_mappers=a[2]
    num_mappers = int(re.findall(r"\d+\.?\d*", num_mappers)[0])
    num_reducers=a[2+num_mappers+1]
    num_reducers=int(re.findall(r"\d+\.?\d*", num_reducers)[0])
    scale=num_mappers*num_reducers
    # b = a[0]  # 这是选取需要读取的位数
    # s = -float(re.findall(r"\d+\.?\d*", b)[0])
    list1.append(scale)  # 将其添加在列表之中
    line1 = f1.readline()
f1.close()
list1.sort(reverse=True)

with open('data.csv', 'w', newline='') as csvfile:
    writer  = csv.writer(csvfile)
    writer.writerow(list1)

print(max(list1))