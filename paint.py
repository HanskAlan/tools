import matplotlib.pyplot as plt
import numpy as np


# om_interval=[68249.8,71415.38,77495.12]#interval从高到低
# rap_interval=[86267.32,82935.9,93242.88]

# om_width=[87163.94,71415.38,56949.5]
# rap_width=[109876.18,82935.9,61004.98]
#
# intervals=["1-400","1-600","1-900"]
# width=["1-13","1-20","1-30"]
#
# x1=range(len(intervals))
# x2=range(len(width))
#
# # compare_rap_om=[default_om,defalt_rap]
compare_tag=["OMCoflow","Rapier"]



plt.rcParams['font.sans-serif'] = ['SimHei']
plt.rcParams['axes.unicode_minus'] = False

# 输入统计数据
intervals = ('高间隔', '中等间隔', '低间隔')
width=('较大宽度','中等宽度','较小宽度')
om_interval_sim=[33739,34136,32456]#interval从高到低
rap_interval_sim=[35881,36213,33427]
om_width_sim=[38588,34136,30831]#从大到小
rap_width_sim=[40576,36213,32268]

om_interval_sys=[52788,51289,48346]
rap_interval_sys=[53260,54270,51704]
om_width_sys=[55862,51289,46740]
rap_width_sys=[58530,54270,47264]


bar_width = 0.3  # 条形宽度
index_om = np.arange(len(intervals))  # omcoflow条形图的横坐标
index_rap = index_om + bar_width  # rapier条形图的横坐标

# 模拟实验  om与rapier 的interval对比
# plt.bar(index_om, height=om_interval_sim, width=bar_width, color='black', label='OMCoflow')
# plt.bar(index_rap, height=rap_interval_sim, width=bar_width, color='grey', label='Rapier')
# plt.legend(loc=2, bbox_to_anchor=(1.05,1.0),borderaxespad = 0.)  # 显示图例
# plt.xticks(index_om + bar_width / 2, intervals)  # 让横坐标轴刻度显示 waters 里的饮用水， index_male + bar_width/2 为横坐标轴刻度的位置
# plt.ylabel('平均协流完成时间(毫秒)')  # 纵坐标轴标题
#
# plt.title('模拟实验不同间隔效果对比',verticalalignment='bottom')  # 图形标题
# plt.savefig('./sim_interval.jpg')
# plt.show()
#
# #模拟实验 om与rapier的width对比
# plt.bar(index_om, height=om_width_sim, width=bar_width, color='black', label='OMCoflow')
# plt.bar(index_rap, height=rap_width_sim, width=bar_width, color='grey', label='Rapier')
# plt.legend(loc=2, bbox_to_anchor=(1.05,1.0),borderaxespad = 0.)  # 显示图例
# plt.xticks(index_om + bar_width / 2, width)  # 让横坐标轴刻度显示 waters 里的饮用水， index_male + bar_width/2 为横坐标轴刻度的位置
# plt.ylabel('平均协流完成时间(毫秒)')  # 纵坐标轴标题
# plt.title('模拟实验不同宽度效果对比')  # 图形标题
# plt.savefig('./sim_width.jpg')
# plt.show()
#
# #系统实验 om与rapier的interval对比
# plt.bar(index_om, height=om_interval_sys, width=bar_width, color='black', label='OMCoflow')
# plt.bar(index_rap, height=rap_interval_sys, width=bar_width, color='grey', label='Rapier')
# plt.legend(loc=2, bbox_to_anchor=(1.05,1.0),borderaxespad = 0.)  # 显示图例
# plt.xticks(index_om + bar_width / 2, intervals)  # 让横坐标轴刻度显示 waters 里的饮用水， index_male + bar_width/2 为横坐标轴刻度的位置
# plt.ylabel('平均协流完成时间(毫秒)')  # 纵坐标轴标题
# plt.title('系统实验不同间隔效果对比')  # 图形标题
# plt.savefig('./sys_interval.jpg')
# plt.show()
#
# #系统实验 om与rapier的width对比
# plt.bar(index_om, height=om_width_sys, width=bar_width, color='black', label='OMCoflow')
# plt.bar(index_rap, height=rap_width_sys, width=bar_width, color='grey', label='Rapier')
# plt.legend(loc=2, bbox_to_anchor=(1.05,1.0),borderaxespad = 0.)  # 显示图例
# plt.xticks(index_om + bar_width / 2, width)  # 让横坐标轴刻度显示 waters 里的饮用水， index_male + bar_width/2 为横坐标轴刻度的位置
# plt.ylabel('平均协流完成时间(毫秒)')  # 纵坐标轴标题
# plt.title('系统实验不同宽度效果对比')  # 图形标题
# plt.savefig('./sys_width.jpg')
# plt.show()
#
# #om的系统与模拟进行对比，不同间隔
# plt.bar(index_om, height=om_interval_sim, width=bar_width, color='black', label='模拟实验')
# plt.bar(index_rap, height=om_interval_sys, width=bar_width, color='grey', label='系统实验')
# plt.legend(loc=2, bbox_to_anchor=(1.05,1.0),borderaxespad = 0.)  # 显示图例
# plt.xticks(index_om + bar_width / 2, intervals)  # 让横坐标轴刻度显示 waters 里的饮用水， index_male + bar_width/2 为横坐标轴刻度的位置
# plt.ylabel('平均协流完成时间(毫秒)')  # 纵坐标轴标题
# plt.title('OMCoflow的系统与模拟实验下不同间隔对比')  # 图形标题
# plt.savefig('./OM_interval.jpg')
# plt.show()
#
# #rapier的系统与模拟进行对比，不同interval
# plt.bar(index_om, height=rap_interval_sim, width=bar_width, color='black', label='模拟实验')
# plt.bar(index_rap, height=rap_interval_sys, width=bar_width, color='grey', label='系统实验')
# plt.legend(loc=2, bbox_to_anchor=(1.05,1.0),borderaxespad = 0.)  # 显示图例
# plt.xticks(index_om + bar_width / 2, intervals)  # 让横坐标轴刻度显示 waters 里的饮用水， index_male + bar_width/2 为横坐标轴刻度的位置
# plt.ylabel('平均协流完成时间(毫秒)')  # 纵坐标轴标题
# plt.title('rapier的系统与模拟实验下不同间隔对比')  # 图形标题
# plt.savefig('./rap_interval.jpg')
# plt.show()
#
# #om的系统与模拟进行对比，不同width
# plt.bar(index_om, height=om_width_sim, width=bar_width, color='black', label='模拟实验')
# plt.bar(index_rap, height=om_width_sys, width=bar_width, color='grey', label='系统实验')
# plt.legend(loc=2, bbox_to_anchor=(1.05,1.0),borderaxespad = 0.)  # 显示图例
# plt.xticks(index_om + bar_width / 2, width)  # 让横坐标轴刻度显示 waters 里的饮用水， index_male + bar_width/2 为横坐标轴刻度的位置
# plt.ylabel('平均协流完成时间(毫秒)')  # 纵坐标轴标题
# plt.title('OMCoflow的系统与模拟实验下不同宽度对比')  # 图形标题
# plt.savefig('./OM_width.jpg')
# plt.show()
#
# #rapier的系统与模拟进行对比，不同width
# plt.bar(index_om, height=rap_width_sim, width=bar_width, color='black', label='模拟实验')
# plt.bar(index_om, bottom=rap_width_sim,height=rap_width_sys, width=bar_width, color='grey', label='系统实验')
# plt.legend(loc=2, bbox_to_anchor=(1.05,1.0),borderaxespad = 0.)  # 显示图例
# plt.xticks(index_om + bar_width / 2, width)  # 让横坐标轴刻度显示 waters 里的饮用水， index_male + bar_width/2 为横坐标轴刻度的位置
# plt.ylabel('平均协流完成时间(毫秒)')  # 纵坐标轴标题
# plt.title('rapier的系统与模拟实验下不同宽度对比')  # 图形标题
# plt.savefig('./rap_width.jpg')
# plt.show()

om_sys_intervalPlusWidth=np.array(om_interval_sys+om_width_sys)
rap_sys_intervalPlusWidth=np.array(rap_interval_sys+rap_width_sys)

om_sim_intervalPlusWidth=np.array(om_interval_sim+om_width_sim)
rap_sim_intervalPlusWidth=np.array(rap_interval_sim+rap_width_sim)

intervalPlusWidth=('高间隔', '中等间隔', '低间隔','较大宽度','中等宽度','较小宽度')
bar_width = 0.3  # 条形宽度
index_left = np.arange(len(intervalPlusWidth))  # omcoflow条形图的横坐标
index_right = index_left + bar_width


#从左至右为三种interval,三种width，左为omcoflow，右为rapier，下为模拟，上为系统实验
plt.bar(index_left,height=om_sim_intervalPlusWidth,width=bar_width, color='Turquoise',label='模拟实验_omcoflow')
plt.bar(index_left,height=-om_sys_intervalPlusWidth,width=bar_width, color='Teal',label='系统实验_omcoflow')
plt.bar(index_right,height=rap_sim_intervalPlusWidth,width=bar_width, color='SteelBlue',label='模拟实验_rapier')
plt.bar(index_right,height=-rap_sys_intervalPlusWidth,width=bar_width, color='DeepSkyBlue',label='系统实验_rapier')
plt.legend(loc=2, bbox_to_anchor=(1.01,1.0),borderaxespad = 0.)  # 显示图例
plt.xticks(index_left + bar_width / 2, intervalPlusWidth)  # 让横坐标轴刻度显示 waters 里的饮用水， index_male + bar_width/2 为横坐标轴刻度的位置
plt.ylabel('平均协流完成时间(毫秒)')  # 纵坐标轴标题
#plt.title('coflow parameters for different algorithm')  # 图形标题
plt.savefig('./total_fig.jpg')
plt.show()
