'''
预处理 - 数据离散化
使用T-drive数据集，该数据集包括一周内10357辆出租车的数据，
包括出租车ID，时间，位置（经纬度表示）
1,2008-02-02 15:36:08,116.51172,39.92123
选取每天8点半到下午的两点半的时间段
将其离散化成32个时间点，这样任意两个时间戳之间的时间间隔大概为10分钟
这样预处理后会得到6000个左右出租车轨迹
从中随机选取1000个作为实验
每次实验运行10次，然后取平均值作为最终结果
'''
#类
#库
import datetime
#得到离散化的点
def solveTravel(myInfo,begintime,endtime,num):
    #初始化
    res=[]
    step=(endtime.timestamp()-begintime.timestamp())/num
    travel=[]
    newInfo=[]
    for item in myInfo:
        if item[0]>=begintime and item[0]<endtime :
            if item[1][0]>=110 and item[1][0]<=130 and item[1][1]>=30 and item[1][1]<=50:
                newInfo.append([item[0].timestamp()-begintime.timestamp(),item[1]])
            #print(item[1][0],item[1][1],item[1][0]>=110,item[1][0]<=130,item[1][1]>=30, item[1][1]<=50)
    pos=0
    for i in range(num):
        if pos>=len(newInfo) or newInfo[pos][0]/step>i+1:
            return [] 
        midtime=(i+0.5)*step
        travel.append(newInfo[pos])
        while pos+1<len(newInfo) and newInfo[pos+1][0]/step<i+1:
            pos+=1
            #print(newInfo[pos][0])
            if abs(travel[i][0]-midtime)>abs(newInfo[pos][0]-midtime):
                travel[i]=newInfo[pos]
        pos+=1
    res=[]
    for item in travel:
        #print(item)
        res.append(item[1])
    return res

#读出时间，位置数据    
def getTravel(fileName):
    #taxi id, date time, longitude, latitude
    fp=open(fileName,'r')
    info=fp.readlines();
    fp.close()
    myInfo=[]
    for s in info:
        taxiId,dateStr,longitude,latitude=s.split(',')
        date=datetime.datetime.strptime(dateStr,"%Y-%m-%d %H:%M:%S")
        myInfo.append([date,[float(longitude),float(latitude)]])
    return myInfo
