import os
import json
import codecs
import math
import numpy as np
import matplotlib.pyplot as plt

file_list=os.listdir('RACLog/RACLog') #获取log中所有的txt文件
coflow_dict={}#以字典方式存储dict，以coflowID为索引，以tuple(min,max)为值索引，min表示的是到达时间，max表示的是完成时间
overhead=0 #这个东西计算的应该是一个累加值
coflow_flownum={}#用来记录每个coflow的flow数目，这个第一次遍历就应该记清楚，并不再修改
coflow_overhead={}

flow_arrive_time={}#用来记录各个数据流的到来时间，以（coflowID,flowID）这个tuple作为key，到来时间作为value
for file in file_list:#先遍历获得所有的coflow
    txt_path = 'E:\RACLogProcessing\RACLog\RACLog'+'\\'+file
    f = codecs.open(txt_path, mode='r', encoding='utf-8')  # 打开txt文件，以‘utf-8’编码读取
    line=f.readline()
    while line:
        line_info=line.split()
        if line_info[0]=='FLOW_ARRIVE':
            flowJson=json.loads(line_info[3])
            #print(flowJson["coflowID"])
            coflow_dict.update({flowJson["coflowID"]:(0,0)})
            # overhead_dict.update({flowJson["coflowID"]:0})
            flow_arrive_time.update({(flowJson["coflowID"],flowJson["flowID"]):int(line_info[2])})
        line=f.readline()
    f.close()
for key in coflow_dict:#这次遍历是为了求解cct
    arriveTime, completeTime = float('inf'), -float('inf')
    # arriveTime_last=-float('inf')#这个是用来计算overhead的，因为计算时间是最后一条到达的流的得到结果的时间减去该流到达时间
    for file in file_list:
        txt_path = 'E:\RACLogProcessing\RACLog\RACLog' + '\\' + file
        f = codecs.open(txt_path, mode='r', encoding='utf-8')  # 打开txt文件，以‘utf-8’编码读取
        line = f.readline()
        while line:
            line_info=line.split()
            if line_info[0]=='FLOW_ARRIVE':
                # print(line_info[3])
                flowJson=json.loads(line_info[3])
                if flowJson["coflowID"]==key:
                    arriveTime=min(arriveTime,int(line_info[2]))
                    # arriveTime_last=max(arriveTime_last,int(line_info[2]))
            if line_info[0]=='FLOW_COMPLETE':
                flowJson=json.loads(line_info[3])
                if flowJson["coflowID"]==key:
                    completeTime=max(completeTime,int(line_info[2]))
                    # flowJson=json.loads(tmp)
                    # # flowJson=json.loads(line_info[3])
                    # if flowJson["coflowID"]==key:
                    #     overhead_dict.update({key:max(overhead_dict[key],int(line_info[2]))})
                    #     # print(key)
                    #     print("upated overhead value %d"%overhead_dict[key])
            line=f.readline()
        f.close()
    coflow_dict.update({key:(arriveTime,completeTime)})
for file in file_list:#这次遍历是为了求解overhead
    txt_path = 'E:\RACLogProcessing\RACLog\RACLog' + '\\' + file
    f = codecs.open(txt_path, mode='r', encoding='utf-8')  # 打开txt文件，以‘utf-8’编码读取
    line = f.readline()
    while line:
        line_info=line.split()
        if line_info[0]=="GET_ANSWER" and line_info[3]!="[]":
            tmp=line_info[3][1:len(line_info[3])-1] #去掉flowassignment两边的中括号
            assignments=tmp.split("\"flowAssignments\"")#按照flowAssignment进行分割
            assignments=assignments[1:len(assignments)]
            for i in range(len(assignments)):#就是对数据进行一点点调整以符合json的格式，方便程序进行加载
                if i==len(assignments)-1:
                    assignments[i]="{\"flowAssignments\""+assignments[i]
                    continue
                assignments[i]="{\"flowAssignments\""+assignments[i][0:len(assignments[i])-2]
            #max_arrivetime=-1
            for assign in assignments: #一个assign就是一个coflow里面的情况
                flowJson = json.loads(assign)
                flowassigns=flowJson["flowAssignments"]#flowassigns是把flowAssignments中的每个流的具体安排抽取出来
                max_coflow_arriveTime=-1
                coflowID = flowJson["coflowID"]
                for fa in flowassigns: #fa就是一个流的具体安排
                    fa=str(fa).replace("\'","\"")
                    singleFlowJson=json.loads(fa)
                    # print(singleFlowJson)
                   # coflowID=flowassigns["coflowID"]
                    max_coflow_arriveTime=max(max_coflow_arriveTime,flow_arrive_time[(coflowID,singleFlowJson["flowID"])])
                   # max_arrivetime=max(max_arrivetime,flow_arrive_time[(coflowID,singleFlowJson["flowID"])])
                if coflowID not in coflow_overhead:
                    coflow_overhead.update({coflowID:int(line_info[2])-max_coflow_arriveTime})

            er=int(line_info[2])
            # overhead+=int(line_info[2])-max_arrivetime
        line=f.readline()
    f.close()
    # overhead_dict.update({key:overhead_dict[key]-arriveTime_last})
total_CCT=0
valid_num=0
inf_num=0
for key in coflow_dict:
    if math.isinf(coflow_dict[key][1]):
        inf_num+=1
        continue
    if coflow_dict[key][1]-coflow_dict[key][0]<=1800000:#由于存在一些奇怪的数据，去掉某些较大的值
        total_CCT+=coflow_dict[key][1]-coflow_dict[key][0]
    valid_num+=1
    print("CCT of %d:%d"%(key,(coflow_dict[key][1]-coflow_dict[key][0])))
print(valid_num)
print(inf_num)
print(len(coflow_dict))
average_cct=total_CCT/valid_num
print("The average CCT is %f\n"%average_cct)
# print(overhead/total_CCT)
#print(coflow_overhead)
x,y=[],[]
overhead_sum=0
max_key=-1
for key in coflow_overhead:
    x.append(key)
    y.append(coflow_overhead[key])
    overhead_sum+=coflow_overhead[key]
max_key=max(coflow_overhead,key=coflow_overhead.get)
print(overhead_sum/total_CCT)
# nx= [str(i) for i in x]
# ny= np.array(y)
# plt.bar(range(len(nx)), ny,color='rgb',tick_label=nx)
# plt.show()
#
#
#
# coflowX,CCT=[],[]
# for key in coflow_dict:
#     coflowX.append(key)
#     CCT.append(coflow_dict[key][1]-coflow_dict[key][0])
# cx=[str(i) for i in coflowX]
# cy=np.array(CCT)
# plt.bar(range(len(cx)),cy,color='rgb')


plt.show()

#对overhead的计算没有问题，因为coflow10的信息不全面，所以暂时计算有问题

# a={}
# a.update({(1,2):5})
# print(a)
