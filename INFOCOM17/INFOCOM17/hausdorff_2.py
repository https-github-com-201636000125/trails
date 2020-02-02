import math

def getDistence_2(a, b):
    return (a[0] - b[0]) * (a[0] - b[0]) + (a[1] - b[1]) * \
                     (a[1] - b[1])

def hausdorff_distance_2(x,y,segNum):
    print('hausdorff',len(x),len(y))
    re=0
    cnt=0
    for i in x:
        mn=math.inf
        for j in y:
            t_dis_2=0
            for e in range(segNum):
                t_dis_2+=getDistence_2(i[e],j[e])
                if t_dis_2>mn:
                    break
            mn=min(mn,t_dis_2)
        cnt+=1
        if (cnt%100==0):
            print('h_d',cnt)
        re=max(mn,re)
    
    for i in y:
        mn=math.inf
        for j in x:
            t_dis_2=0
            for e in range(segNum):
                t_dis_2+=getDistence_2(i[e],j[e])
                if t_dis_2>mn:
                    break
            mn=min(mn,t_dis_2)
        re=max(mn,re)

    return math.sqrt(re)


if __name__ == '__main__' :

    pass
