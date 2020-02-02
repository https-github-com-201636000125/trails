from hausdorff_2 import hausdorff_distance_2
from sklearn import metrics
import numpy as np

def get_Hausdorff(newTrails,trails,segNum,choiceNum):
    #return 0

    X=trails
    Y=[]
    for i in newTrails:
            Y.append(i.trail)
    X=np.array(X)
    Y=np.array(Y)
    return hausdorff_distance_2(X, Y,segNum)

    
def output_Hausdorff(fileName,sign_Hausdorff):
    f = open(fileName, 'w')
    print(sign_Hausdorff,file=f)
    f.close()
    return
    
def get_m_info(newTrails,labels,trails,centers,maxlen,segNum,choiceNum):
    '''
    trails  1000*32
    centers k*32
    labels  1000*32
    '''
    dic={}
    X=[]
    Y=[]
    cnt=0
    for i in range(choiceNum):
        if str(newTrails[i].label) not in dic:
            cnt+=1
            X.append(cnt)
            dic[str(newTrails[i].label)]=cnt
        else:
            X.append(dic[str(newTrails[i].label)])
            
    for i in range(choiceNum):
        if str(labels[i]) not in dic:
            cnt+=1
            Y.append(cnt)
            dic[str(labels[i])]=cnt
        else:
            Y.append(dic[str(labels[i])])
            
    return metrics.adjusted_mutual_info_score(Y,X) 

def output_m_info(fileName,sign_m_info):
    f = open(fileName, 'w')
    print(sign_m_info,file=f)
    f.close()
    return

#半径最好是0.2,0.4,0.6,0.8,1.0
def get_wrq(newTrails,trails,delta,segNum,choiceNum):

    avg_longitude=0
    avg_latitude=0
    for i in trails:
        for j in i:
            avg_longitude+=j[0]
            avg_latitude+=j[1]
    for i in newTrails:
        for j in i.trail:
            avg_longitude+=j[0]
            avg_latitude+=j[1]
    avg_longitude/=(choiceNum*segNum*2)
    avg_latitude/=(choiceNum*segNum*2)
    rg=0
    rc=0
    r_both=0
    for i in trails:
        jug=True
        j=i[0]
        if j[0]<avg_longitude-delta or j[0]>avg_longitude+delta or \
                                        j[1]<avg_latitude-delta or j[1]>avg_latitude+delta:
            jug=False
        if jug==True:
            rc+=1
    for i in newTrails:
        jug=True
        j=i.trail[0]
        if j[0]<avg_longitude-delta or j[0]>avg_longitude+delta or \
                                        j[1]<avg_latitude-delta or j[1]>avg_latitude+delta:
            jug=False
        if jug==True:
            rg+=1
            if i.real>0:
                r_both+=1
    print(rc,rg,r_both)
    prec=r_both/rc
    recall=r_both/rg
    F1=2*prec*recall/(prec+recall)
    return  F1

def output_wrq(fileName,sign_wrq):
    f = open(fileName, 'w')
    print(sign_wrq,file=f)
    f.close()
    return

if __name__ == '__main__':
    
    pass



