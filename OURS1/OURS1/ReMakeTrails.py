import trie
import random
import numpy as np
import math
import staircase

class Trail:
    def __init__(self, trail, label, real, noisy):
        self.trail = trail
        self.label = label
        self.real = real
        self.noisy = noisy

    def __eq__(self, other):
        return self.noisy == other.noisy

    def __le__(self, other):
        return self.noisy < other.noisy

    def __gt__(self, other):
        return self.noisy > other.noisy


def label_cmp(a, b):
    len_a = len(a.label)
    for i in range(len_a):
        if a.label[i] < b.label[i]:
            return -1
        elif a.label[i] > b.label[i]:
            return 1
    return 0


def getDistence(a, b):
    #if math.sqrt((a[0]-b[0])*(a[0]-b[0])+(a[1]-b[1])*(a[1]-b[1]))>5:
    #   print(a[0],a[1],b[0],b[1],math.sqrt((a[0]-b[0])*(a[0]-b[0])+(a[1]-b[1])*(a[1]-b[1])))
    return math.sqrt((a[0] - b[0]) * (a[0] - b[0]) + (a[1] - b[1]) *
                     (a[1] - b[1]))
    #return 0


'''
def newTrailCmp(trailA,trailB):
    return trailA.noisy<trailB.noisy
'''


def getRandomTrail(k, segNum, centers, maxlen):
    res = []
    '''
    for i in range(segNum):
        res.append(random.randint(0,k-1))
    '''
    #res=dfs(k,0,segNum,centers,maxlen,-1)
    vis = []
    ran = []
    for i in range(segNum):
        vis.append([])
        ran.append([])
        for j in range(k):
            vis[i].append(0)
    for i in range(segNum - 1, -1, -1):
        if i == segNum - 1:
            for j in range(k):
                vis[i][j] = 1
                ran[i].append(j)
        else:
            for j in range(k):
                for l in range(k):
                    if vis[i + 1][l] == 1 and getDistence(
                            centers[j][i], centers[l][i + 1]) <= maxlen:
                        vis[i][j] = 1
                        break
                if vis[i][j] == 1:
                    ran[i].append(j)
    res = []
    for i in range(segNum):
        num = random.choice(ran[i])
        while i > 0 and maxlen < getDistence(centers[num][i],
                                             centers[res[i - 1]][i - 1]):
            num = random.choice(ran[i])
        res.append(num)
    #print('aaaa',res)
    return res


def judgeTrail(trail, maxlen):
    tlen = len(trail)
    for i in range(tlen - 1):
        if getDistence(trail[i], trail[i + 1]) <= maxlen:
            continue
        else:
            return False
    return True


def get_second_trails(fileName, segNum, choiceNum):
    f = open(fileName, 'r')
    infos = f.readlines()
    f.close()
    #1000*32
    trails = []
    for i in range(choiceNum):
        trails.append([])
        for ite in range(segNum):
            p = infos[i * segNum + ite].split()
            pf = [float(p[0]), float(p[1])]
            trails[i].append(pf)
    return trails


def get_maxlen(trails, segNum, choiceNum):
    #1000*32
    maxlen = 0
    for i in range(choiceNum):
        lp = [0, 0]
        for ite in range(segNum):
            if ite > 0:
                #pass
                maxlen = max(maxlen, getDistence(trails[i][ite], lp))
            lp = trails[i][ite]
    return maxlen


def get_second_centers(fileName, segNum, kmeans_k):
    f = open(fileName, 'r')
    infos = f.readlines()
    f.close()
    #k*32
    centers = []
    for i in range(kmeans_k):
        centers.append([])
        for j in range(segNum):
            p = infos[segNum * i + j].split()
            centers[i].append([float(p[0]), float(p[1])])
    return centers


def get_second_labels(fileName, segNum, choiceNum):
    f = open(fileName, 'r')
    infos = f.readlines()
    f.close()
    #1000*32
    labels = []
    for i in range(choiceNum):
        labels.append([])
        for j in range(segNum):
            labels[i].append(int(infos[j * choiceNum + i]))
    return labels

def add_staircase_noisy(epsilon,sensitivity,top):
    re=staircase.randomise(epsilon,sensitivity)
    '''
    T=100
    while T>0 and re>top:
        T-=1
        re=staircase.randomise(epsilon,sensitivity)
    if T==0:
        re=0
    '''
    return re


def centers_add_noisy(trails,centers,labels,segNum,choiceNum,kmeans_k,epsilon):
    '''
    trails  1000*32
    centers k*32
    labels  1000*32
    '''
    c_dis=[]
    c_near=[]
    for i in range(kmeans_k):
        c_dis.append([])
        c_near.append([])
        for j in range(segNum):
            c_dis[i].append(math.inf)
            c_near[i].append([0,0])
            
    for i in range(choiceNum):
        for j in range(segNum):
            '''
            if abs(trails[i][j][0]-centers[labels[i][j]][j][0])<c_dis[labels[i][j]][j]:
                c_dis[labels[i][j]][j]=abs(trails[i][j][0]-centers[labels[i][j]][j][0])
            if abs(trails[i][j][1]-centers[labels[i][j]][j][1])<c_dis[labels[i][j]][j]:
                c_dis[labels[i][j]][j]=abs(trails[i][j][1]-centers[labels[i][j]][j][1])
            '''
            if getDistence(centers[labels[i][j]][j],trails[i][j])<c_dis[labels[i][j]][j]:
                c_dis[labels[i][j]][j]=getDistence(centers[labels[i][j]][j],trails[i][j])
                c_near[labels[i][j]][j]=trails[i][j]
    for i in range(kmeans_k):
        for j in range(segNum):
            '''
            centers[i][j][0]+=add_staircase_noisy(epsilon,c_dis[i][j]/choiceNum,c_dis[i][j])
            centers[i][j][1]+=add_staircase_noisy(epsilon,c_dis[i][j]/choiceNum,c_dis[i][j])
            '''
            add_longitude=add_staircase_noisy(epsilon,1,c_dis[i][j])
            add_latitude=add_staircase_noisy(epsilon,1,c_dis[i][j])
            if add_longitude*add_longitude+add_latitude*add_latitude>=  \
                                    getDistence(centers[i][j],c_near[i][j]):
                centers[i][j]=c_near[i][j]
    return 
    
def get_trails_trie(segNum, choiceNum, centers, labels, maxlen):
    myTrie = trie.Trie()
    for i in range(choiceNum):
        newTrail = []
        newCenterTrail = []
        for j in range(segNum):
            la = labels[i][j]
            ce = centers[la][j]
            newTrail.append(la)
            newCenterTrail.append(ce)
        newLen = 0
        for i in range(segNum - 1):
            newlen = max(newLen,
                         getDistence(newCenterTrail[i], newCenterTrail[i + 1]))
        if newlen <= maxlen:
            myTrie.update(newTrail, 1)
            #print(trie.query(newTrail))
    return myTrie


def get_real_trails(myTrie, segNum, choiceNum, centers, labels, epsilon,alpha,beta):
    newTrails = []
    newCnt = 0
    newSum = 0
    for i in range(choiceNum):
        newTrail = []
        newCenterTrail = []
        for j in range(segNum):
            la = labels[i][j]
            ce = centers[la][j]
            newTrail.append(la)
            newCenterTrail.append(ce)
        rea = myTrie.query(newTrail)
        if rea > 0:
            '''
            for j in range(segNum):
                if math.isnan(newCenterTrail[j][0]) or math.isnan(newCenterTrail[j][1]):
                    la = labels[i][j]
                    ce = centers[la][j]
                    print('nan','label=',la,'center=',ce)
            '''
            newSum += rea
            newCnt += 1
            myTrie.update(newTrail, -rea - 1)
            real_noisy=rea+staircase.randomise(epsilon,1)
            if real_noisy<alpha*rea:
                real_noisy=alpha*rea
            elif real_noisy>beta*rea:
                real_noisy=beta*rea
            newTrails.append(Trail(newCenterTrail,newTrail,rea,int(real_noisy)))
    '''
    for i in newTrails:
        for j in i.trail:
            if math.isnan(j[0]) or math.isnan(j[1]) :
                print(j,'nan')
    '''
    
    newTrails.sort()
    return newTrails, newCnt, newSum


def add_virtual_trails(newTrails,newCnt,newSum,centers,segNum,choiceNum,kmeans_k,maxlen,myTrie):
    print('get virtual',newCnt,newSum)
    pos=0
    cntTop=newCnt
    #print(newCnt,choiceNum)
    while newCnt<choiceNum:
        if newCnt==choiceNum:
            break
        elif pos+1==cntTop-1:
            num=choiceNum-newCnt
        else:
            num=random.randint(0,choiceNum-newCnt)
        for itera in range(num):
            newTrail=getRandomTrail(kmeans_k,segNum,centers,maxlen)
            #print(newTrail)
            newCenterTrail=[]
            outLen=False
            for it in range(segNum):
                newCenterTrail.append(centers[newTrail[it]][it])
                if it>0 and getDistence(newCenterTrail[it-1],newCenterTrail[it])>maxlen:
                    outLen=True
            while myTrie.query(newTrail)==-1 or outLen==True:
                newTrail=getRandomTrail(kmeans_k,segNum,centers,maxlen)
                outLen=False
                for it in range(segNum):
                    newCenterTrail.append(centers[newTrail[it]][it])
                    if it>0 and getDistence(newCenterTrail[it-1],newCenterTrail[it])>maxlen:
                        outLen=True
                #print(newTrail)
                print(myTrie.query(newTrail),outLen)
            if (newTrails[pos].noisy>newTrails[pos+1].noisy):
                print(pos+1,len(newTrails),newTrails[pos].noisy,newTrails[pos+1].noisy)
            newTrails.append(Trail(newCenterTrail,newTrail,0, \
            max(0,int(0+random.randint(newTrails[pos].noisy,newTrails[pos+1].noisy)))))
        pos+=1
        newCnt+=num
    newTrails.sort(key=lambda x:x.label)
    print('len',len(newTrails))
    return newTrails



def output_trails(newTrails, fileName):
    #newTrails=sorted(newTrails,cmp=label_cmp)
    #newTrails.sort(key=label_cmp)
    T_len = len(newTrails)
    print(fileName)
    f = open(fileName, 'w')
    for i in range(T_len):
        l_len = len(newTrails[i].label)
        for j in range(l_len - 1):
            #print('t'+str(j+1)+str(newTrails[i].label[j]),end='→',file=f)
            print(str(newTrails[i].label[j] + 1), end=' ', file=f)
            #print(newTrails[i].trail[j])
        #print('t'+str(l_len)+str(newTrails[i].label[l_len-1]+1),end=' ',file=f)
        print(str(newTrails[i].label[l_len - 1] + 1), end=' ', file=f)
        print(newTrails[i].real, newTrails[i].noisy, end='\n', file=f)
    f.close()

def output_selected_trails(trails,fileName, segNum, choiceNum):
    f = open(fileName, 'w')
    for i in range(choiceNum):
        for j in range(segNum):
            print(trails[i][j][0],trails[i][j][1],file=f)
    f.close()
    return 

def output_final_trails(labels,newTrails,fileName, segNum, choiceNum):
    f = open(fileName, 'w')
    for i in range(choiceNum):
        for j in range(segNum):
            print(newTrails[i].trail[j][0],newTrails[i].trail[j][1],file=f)
    f.close()
    
    
    
    return

if __name__ == '__main__':

    pass
