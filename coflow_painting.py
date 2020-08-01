import codecs
import re
import matplotlib.pyplot as plt
import numpy as np


#包含了从文本中截取数字，和画图的一些技巧。
f1 = codecs.open('record.txt', mode='r', encoding='utf-8')  # 打开txt文件，以‘utf-8’编码读取
x,y=[],[]

line1 = f1.readline()   # 以行的形式进行读取文件

while line1:
    tempX,tempY=[],[]
    broken_line = line1.split(',')
    total_data=float(broken_line[2])  # 这是选取需要读取的位数
    existing_time=broken_line[1].split('->')
    start_time,end_time=int(existing_time[0]),int(existing_time[1])

    # diff_stages_data=line1.replace("[","")
    # diff_stages_data=diff_stages_data.replace("]","")
    length=len(broken_line)
    for i in range(3,length):
        curr=broken_line[i].replace("(","")
        curr=curr.replace(")","")
        curr=curr.split(' ')
        tempX.append(float(curr[0])-200000)
        tempY.append(float(curr[1])/total_data)
    x.append(tempX)
    y.append(tempY)
    line1 = f1.readline()
f1.close()

x,y=np.array(x),np.array(y)
plt.ylim((0,1))


num_plots = 10
# Have a look at the colormaps here and decide which one you'd like:
# http://matplotlib.org/1.2.1/examples/pylab_examples/show_colormaps.html
# colormap = plt.cm.gist_ncar
# plt.gca().set_color_cycle([colormap(i) for i in np.linspace(0, 0.9, num_plots)])
# Plot several different functions...
# x = np.arange(10)
# labels = []
for i in range(10):
    plt.plot(x[i], y[i])
    #labels.append(r'$y = %ix + %i$' % (i, 5*i))
    # labels.append(r'$ coflow%i$' % (i))

# I'm basically just demonstrating several different legend options here...
# plt.legend(labels, ncol=4, loc='upper center',
# bbox_to_anchor=[0.5, 1.1],
# columnspacing=1.0, labelspacing=0.0,
# handletextpad=0.0, handlelength=1.5,
# fancybox=True, shadow=True)
# plt.show()

plt.savefig('./record1.jpg')
plt.show()
