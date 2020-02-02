import math

def read_time(K,epsilon,pro_name):
    means=[]
    for i in range(len(pro_name)):
        means.append([])
    for p in range(len(pro_name)):
        for kmeans_k in K:
            fileName=pro_name[p]+'/'+pro_name[p]+'/output/'+'k(' + str(
                    kmeans_k) + ')_e(' + str(epsilon) + ')final_trails' + '.txt'
            f=open(fileName,'r')
            infos=f.readlines()
            f.close()
            for i in infos:
                a=i.split(' ')
                for j in a:
                    if math.isnan(float(j)) and p==3:
                        print(pro_name[p])
    return 



if __name__=='__main__':
    '''
    from hausdorff import hausdorff_distance
    import numpy as np
    
    X=np.array([[1,2],[2,3],[3,4]])
    Y=np.array([[5,6],[6,7],[7,8]])
    
    hausdorff_distance(X, Y)
    '''
    
    
    
    '''   
    import math
    a=float('nan')
    mx=1
    print(a/math.sqrt(a))
    print(mx>a)
    '''
    
    
    pro_name=['INFOCOM15','INFOCOM17','OURS1','OURS3']
    K = [10, 20, 30, 40, 50, 60, 70, 80]
    E = [0.1, 0.5, 1.0, 1.5, 2.0]
    
    for e in E:
        read_time(K,e,pro_name)
    
    
    