import codecs
import re

import numpy as np
import csv
#包含了从文本中截取数字，和画图的一些技巧。
f1 = codecs.open('FB2010-1Hr-150-0.txt', mode='r', encoding='utf-8')  # 打开txt文件，以‘utf-8’编码读取
f2 = open('processed.txt', 'w+')



line1 = f1.readline()   # 以行的形式进行读取文件
line1 = f1.readline()

while line1:

    a = line1.split()#讲数据按空格分开，a[i]即可按照索引得到数据
    write_to_txt = [a[0],a[1]]
    num_mappers=int(re.findall(r"\d+\.?\d*", a[2])[0])
    set_mapper=set()
    for i in range(3,3+num_mappers):
        location_mapper=int(re.findall(r"\d+\.?\d*", a[i])[0])
        set_mapper.add(location_mapper%8)




    num_reducers = int(re.findall(r"\d+\.?\d*", a[num_mappers+3])[0])
    dict_reducer={0:0,1:0,2:0,3:0,4:0,5:0,6:0,7:0}
    for i in range(num_mappers+4,num_mappers+4+num_reducers):
        reducer_info=a[i].split(':')
        location_reducer=int(reducer_info[0])
        dict_reducer[location_reducer%8]+=float(reducer_info[1])
    for k in range(8):
        if dict_reducer[k]==0:
            del dict_reducer[k]
    write_to_txt.append(str(len(set_mapper)))
    list_mapper=list(set_mapper)
    for i in range(len(list_mapper)):
        write_to_txt.append(str(list_mapper[i]))

    write_to_txt.append(str(len(dict_reducer)))
    for k,v in dict_reducer.items():
        temp=str(k)+":"+str(v)
        write_to_txt.append(temp)

    line=""
    for i in range(len(write_to_txt)):
        line=line+" "+write_to_txt[i]

    f2.writelines(line)
    f2.write('\r\n')
    line1 = f1.readline()
f1.close()
# list1.sort(reverse=True)
#
# with open('data.csv', 'w', newline='') as csvfile:
#     writer  = csv.writer(csvfile)
#     writer.writerow(list1)
# dict={3:4}
# x=str(dict)
#
# x=x.replace('{','')
# x=x.replace('}','')
# x=x.replace(' ','')
# print(x)




