import codecs
import re
import matplotlib.pyplot as plt
import numpy as np
f1 = codecs.open('RACTest_record.txt', mode='r', encoding='utf-8')  # 打开txt文件，以‘utf-8’编码读取

x,y=[],[]
line1=f1.readline()
curr=0
coflow_set=set()
while line1:
    tempX, tempY = [], []
    broken_line = line1.split(',')
    coflow_id=int(broken_line[0].split(':')[0])
    if coflow_id in coflow_set:
        for _ in range(4):
            line1=f1.readline()
    else:
        coflow_set.add(coflow_id)
        total_data=float(broken_line[1].split()[-1])
        existing_time=broken_line[-1].split('=')[-1]
        tmp=broken_line[2].split('=')[-1]
        startTime,endTime=int(broken_line[2].split('=')[-1]),int(broken_line[3].split('=')[-1])

        line1=f1.readline()
        timeLine=line1.replace("[","").replace("]","").split(',')#去掉中括号之后以逗号分隔
        length=len(timeLine)
        timeLine=timeLine[0:length-1]
        for tL in timeLine:
            if len(tL)==0:
                break
            tL=tL.replace("(","").replace(")","").split()
            tempX.append(float(tL[0])-200000)
            tempY.append(float(tL[1])/total_data)
        x.append(tempX)
        y.append(tempY)

        line1=f1.readline()
        speeds=line1.replace("[","").replace("]","").replace("KB/s","").split(',') #暂时对speed没有什么操作，就先跳过
        line1=f1.readline() #对path暂时也没有什么操作，暂时先跳过
        line1=f1.readline() #跳到下一组coflow
f1.close()
x,y=np.array(x),np.array(y)

plt.ylim((0,1))
plt.xlabel('Time/s')
plt.ylabel('Percentage of completed parts')

num_plots = 10

line1,=plt.plot(x[0],y[0],'rs-',linestyle='-',linewidth=3)
line2,=plt.plot(x[1],y[1],'bo-',linestyle=(5,(9,1)),linewidth=3)
line3,=plt.plot(x[2],y[2],'y^-',linestyle='dashed',linewidth=3)
line4,=plt.plot(x[3],y[3],'gv-',linestyle=(0,(3,4)),solid_capstyle='butt',linewidth=3)
line5,=plt.plot(x[4],y[4],'c<-.',linestyle=(0,(9,9)),linewidth=3)
line6,=plt.plot(x[5],y[5],'m>--',linestyle='dashdot',linewidth=3)
line7,=plt.plot(x[6],y[6],'ro--',linestyle=':',linewidth=3)
line8,=plt.plot(x[7],y[7],color='#2F4F4F',linestyle=(0,(2,3)),marker='d',markersize=10,linewidth=3)
line9,=plt.plot(x[8],y[8],color='#9E5FFA',linestyle='--',marker='D',linewidth=3)
line10,=plt.plot(x[9],y[9],color='#8E5F9D',linestyle='-.',marker='H',markersize=10,linewidth=3)

for i in range(10):
    plt.plot(x[i][-1], y[i][-1], 'ko',markersize=10,markerfacecolor='none')

plt.savefig('./RACTest.jpg')
plt.show()

