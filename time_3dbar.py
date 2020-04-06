
import matplotlib.pyplot as plt
import numpy as np
from mpl_toolkits.mplot3d import Axes3D
'''
将标注OURS1改成OURS2，将OURS3改成OURS1
'''
def read_time(K,E,pro_name):
    means=[]
    for p in range(len(pro_name)):
        means.append([])
        for k in range(len(K)):
            kmeans_k=K[k]
            means[p].append([])
            for e in range(len(E)):
                epsilon=E[e]
                fileName=pro_name[p]+'/'+pro_name[p]+'/output/'+'k(' + str(
                        kmeans_k) + ')_e(' + str(epsilon) + ')' + '.txt'
                f=open(fileName,'r')
                infos=f.readlines()
                f.close()
                means[p][k].append(float(infos[len(infos)-1]))
    return means

if __name__ == '__main__':
    
    pro_name=['INFOCOM15','INFOCOM17','OURS1','OURS3']
    output_name=['INFOCOM15','INFOCOM17','OURS2','OURS1']
    K = [10, 20, 30, 40, 50, 60, 70, 80]
    E = [0.1, 0.5, 1.0, 1.5, 2.0]
    #p*k*e
    means=read_time(K,E,pro_name)
    
    # k*e
    for p in range(len(pro_name)):
        fig = plt.figure()
        ax = fig.add_subplot(projection='3d')
        x = np.array([0.1, 0.5, 1.0, 1.5, 2.0])  #e
        y = np.array([10, 20, 30, 40, 50, 60, 70, 80]) #k
        
        _X, _Y = np.meshgrid(x, y)
        X, Y = _X.ravel(), _Y.ravel()
        Z =  np.array(means[p]).ravel()
        
        bottom = np.zeros_like(Z)
        width = 0.1
        depth= 5
        
        
        plt.tick_params(labelsize=7)
        ax.set_xlabel('epsilon')
        ax.set_ylabel('Numbers of Groups')
        ax.set_zlabel('time(s)')
        ax.bar3d(X, Y, bottom, width, depth, Z, shade=True)
        ax.set_title(output_name[p])
       #plt.show()
        plt.savefig('output/time_3dbar/'+pro_name[p]+'.jpg',dpi=800)
