# -*- coding: utf-8 -*-
"""
Created on Mon Apr 22 16:47:48 2019

@author: jidi
"""

# encoding=utf-8
import matplotlib.pyplot as plt
from pylab import *                                 #支持中文
plt.rcParams['font.sans-serif'] = ['SimHei']
plt.grid()  # 生成网格
plt.grid(axis="y")
axis='x'
plt.grid(linestyle='--')
plt.grid(ls='-.')
plt.grid(c='gray')
names = ['3', '5', '7', '9', '11','13','15']
x = range(len(names))
y = [13,15,21,29,31,32,34]
y1=[9,11,18,26,28,29,31]
y2= [11,13,20,27,28,30,31]
y3=[8,10,15,21,23,25,29]
y4= [9,11,19,25,27,28,29]
y5=[7,8,15,20,23,25,27]
#plt.plot(x, y, 'ro-')
#plt.plot(x, y1, 'bo-')
#pl.xlim(-1, 11)  # 限定横轴的范围
#pl.ylim(-1, 110)  # 限定纵轴的范围
plt.plot(x, y, color='r',linewidth=1.8,linestyle=':',marker='H',mfc='w',label='CTPP f=25%')
plt.plot(x, y1, color='darkgreen',linewidth=1.8,marker='D',mfc='w',label=r'$k^τ$   f=25%' )
plt.plot(x, y2, color='coral',linewidth=1.8,linestyle='-.',marker='x',mfc='r',label='CTPP f=50%')
plt.plot(x, y3, color='b',linewidth=1.8,linestyle='-.',marker='H',mfc='w',label=r'$k^τ$   f=50%')
plt.plot(x, y4, color='darkviolet',linewidth=1.8,linestyle=':',marker='o',mfc='w',label='CTPP f=75%')
plt.plot(x, y5, color='k',linewidth=1.8,linestyle='-.',marker='x',mfc='w',label=r'$k^τ$   f=75%')
plt.plot(fontsize=15)
plt.legend()  # 让图例生效
plt.xticks(x, names,fontsize=15)
plt.yticks(fontsize=15)
plt.margins(0)
plt.subplots_adjust(bottom=0.15)
#plt.xlim(1,15)#设置横坐标范围
plt.ylim(6,35)#设置横坐标范围
plt.xlabel("h",fontsize=15) #X轴标签
plt.ylabel("communication cost",fontsize=15) #Y轴标签
plt.title(r'$N_m$''$_a$''$_x$=6',fontsize=15) #标题

plt.show()
