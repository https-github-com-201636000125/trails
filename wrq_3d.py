
import matplotlib.pyplot as plt
import numpy as np
from mpl_toolkits.mplot3d import Axes3D

def read_time(K,E,pro_name,delta):
    means=[]
    for p in range(len(pro_name)):
        means.append([])
        for k in range(len(K)):
            kmeans_k=K[k]
            means[p].append([])
            for e in range(len(E)):
                epsilon=E[e]
                fileName=pro_name[p]+'/'+pro_name[p]+'/output/'+'k(' + str(
                        kmeans_k) + ')_e(' + str(epsilon) +')_delta('+str(delta)+ ')wrq' + '.txt'
                f=open(fileName,'r')
                infos=f.readlines()
                f.close()
                means[p][k].append(float(infos[0]))
    return means

if __name__ == '__main__':
    
    pro_name=['INFOCOM15','INFOCOM17','OURS1','OURS3']
    K = [10, 20, 30, 40, 50, 60, 70, 80]
    E = [0.1, 0.5, 1.0, 1.5, 2.0]
    D = [0.4,0.6,0.8,1.0]
    
    for delta in D:
        #p*k*e
        means=read_time(K,E,pro_name,delta)
        
        fig = plt.figure()
        ax = fig.gca(projection='3d')
        x = np.array([0.1, 0.5, 1.0, 1.5, 2.0])  #e
        y = np.array([10, 20, 30, 40, 50, 60, 70, 80]) #k
        X, Y = np.meshgrid(x, y)
        
        # k*e
        for p in range(len(pro_name)):  
            surf = ax.plot_surface(X, Y,np.array(means[p]))
        #ax.legend(loc=2, bbox_to_anchor=(1.05,1.0),borderaxespad = 0)
        #ax.legend()
        ax.set_xlabel('epsilon')
        ax.set_ylabel('Numbers of Groups')
        ax.set_zlabel('wrq')
        ax.set_title('delta='+str(delta))
        #plt.subplots_adjust(right=0.74)
        #plt.show()
        plt.savefig('output/wrq_3d/'+'(delta='+str(delta)+')'+'.jpg')
