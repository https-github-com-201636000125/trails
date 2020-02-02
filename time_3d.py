
import matplotlib.pyplot as plt
import numpy as np
from mpl_toolkits.mplot3d import Axes3D

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
    K = [10, 20, 30, 40, 50, 60, 70, 80]
    E = [0.1, 0.5, 1.0, 1.5, 2.0]
    #p*k*e
    means=read_time(K,E,pro_name)
    
    # k*e
    for p in range(len(pro_name)):
        fig = plt.figure()
        ax = fig.gca(projection='3d')
        x = np.array([0.1, 0.5, 1.0, 1.5, 2.0])  #e
        y = np.array([10, 20, 30, 40, 50, 60, 70, 80]) #k
        
        X, Y = np.meshgrid(x, y)
        surf = ax.plot_surface(X, Y, np.array(means[p]))
        
        ax.set_xlabel('epsilon')
        ax.set_ylabel('Numbers of Groups')
        ax.set_zlabel('time(s)')
        ax.set_title(pro_name[p])
        #plt.show()
        plt.savefig('output/time_3d/'+pro_name[p]+'.jpg')
