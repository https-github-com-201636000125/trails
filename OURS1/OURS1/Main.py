'''
流程：
数据预处理，得到1000条时间戳长度为32的轨迹数据库
对每个时间戳下位置进k均值聚类，进行轨迹重构与筛选
对重构轨迹计数加噪

预处理后会得到6000个左右出租车轨迹
从中随机选取1000个作为实验
每次实验运行10次，然后取平均值作为最终结果

'''

#类

#离散化
import Discretization
#k均值聚类

#轨迹重构，轨迹筛选，加噪

#库

import datetime

'''
主函数
'''
if __name__=='__main__':
    travels=[]  
    fileTempWrite=open('tempTrails.txt','w');
    for fileNum in range(10357):
        fileName='data/taxi_log_2008_by_id/'+str(fileNum+1)+'.txt'
        
        '''
        for day in range(2,9):
            tempTravels=Discretization.solveTravel(Discretization.getTravel(fileName),\
            datetime.datetime(2008,2,day,8,30,0),datetime.datetime(2008,2,day,14,30,0),32)
            for i in tempTravels:
                travels.append(i)
        '''
        
        #2008.2.6  Wed
        day=6
        tempTravels=Discretization.solveTravel(Discretization.getTravel(fileName),\
        datetime.datetime(2008,2,day,8,30,0),datetime.datetime(2008,2,day,14,30,0),32)
        for i in tempTravels:
            travels.append(i)
            print(i[0],i[1],file=fileTempWrite)
        if tempTravels!=[]:    
            print(fileNum+1,len(travels)/32,end='\n')
    fileTempWrite.close()
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
