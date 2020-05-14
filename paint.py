import codecs
import re
import matplotlib.pyplot as plt
import numpy as np

f1 = codecs.open('pporesult.txt', mode='r', encoding='utf-8')  # 打开txt文件，以‘utf-8’编码读取
line1 = f1.readline()   # 以行的形式进行读取文件
list1 = []
while line1:
    a = line1.split()
    b = a[-1]   # 这是选取需要读取的位数
    s=-float(re.findall(r"\d+\.?\d*", b)[0])
    list1.append(s)  # 将其添加在列表之中
    line1 = f1.readline()
f1.close()

f2 = codecs.open('ppo_heuristic.txt', mode='r', encoding='utf-8')  # 打开txt文件，以‘utf-8’编码读取
line2 = f2.readline()   # 以行的形式进行读取文件
list2 = []
while line2:
    a = line2.split()
    b = a[-1]   # 这是选取需要读取的位数
    s=-float(re.findall(r"\d+\.?\d*", b)[0])
    list2.append(s)  # 将其添加在列表之中
    line2 = f2.readline()
f2.close()
episode_num=3000
reward1=np.array(list1)
reward2=np.array(list2)
x=np.arange(0,episode_num)

plt.title("reward in contrast")
plt.xlabel("x axis caption")
plt.ylabel("y axis caption")

l1,=plt.plot(x, reward1)
l2,=plt.plot(x, reward2, color='red', linewidth=1, linestyle='--')
plt.legend([l1,l2],['rl','heuristic'],loc='upper right')
plt.savefig('./result.jpg')
plt.show()


