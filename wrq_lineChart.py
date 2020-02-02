# encoding=utf-8
import matplotlib.pyplot as plt

def read_wrq(kmeans_k,epsilon,D,pro_name):
    means=[]
    for i in range(len(pro_name)):
        means.append([])
    for delta in D:
        for p in range(len(pro_name)):
            fileName=pro_name[p]+'/'+pro_name[p]+'/output/'+'k(' + str(
                kmeans_k) + ')_e(' + str(epsilon) +')_delta('+str(delta)+ ')wrq' + '.txt'
            f=open(fileName,'r')
            infos=f.readlines()
            f.close()
            means[p].append(float(infos[0]))
    return means


if __name__ == '__main__':
    
    pro_name=['INFOCOM15','INFOCOM17','OURS1','OURS3']
    K = [10, 20, 30, 40, 50, 60, 70, 80]
    E = [0.1, 0.5, 1.0, 1.5, 2.0]
    D = [0.4,0.6,0.8,1.0]
    
    
    
    for kmeans_k in K:
        infocom15_means=[]
        infocom17_means=[]
        ours1_means=[]
        ours3_means=[]
        for e in range(len(E)):
            means=read_wrq(kmeans_k,E[e],D,pro_name)
            infocom15_means.append(tuple(means[0]))
            infocom17_means.append(tuple(means[1]))
            ours1_means.append(tuple(means[2]))
            ours3_means.append(tuple(means[3]))
        
        #pl.xlim(-1, 11) # 限定横轴的范围
        #pl.ylim(-1, 110) # 限定纵轴的范围
        
        p_long=9
        p_width=7
        
        for e in range(len(E)):
            #初始化画布
            plt.figure(figsize=(p_long,p_width))
            #x轴
            names = [0.4,0.6,0.8,1.0]
            x = range(len(names))
            
            plt.plot(x, infocom15_means[e],marker='p',label='INFOCOM15 epsilon='+str(E[e]))
            plt.plot(x, infocom17_means[e],marker='*',label='INFOCOM17 epsilon='+str(E[e]))
            plt.plot(x, ours1_means[e],marker='s',label='OURS1 epsilon='+str(E[e]))
            plt.plot(x, ours3_means[e],marker='x',label='OURS3 epsilon='+str(E[e]))
            
            #plt.legend(loc='best') # 让图例生效
            plt.legend(loc=2, bbox_to_anchor=(1.05,1.0),borderaxespad = 0)
            plt.xticks(x, names, rotation=45)
            plt.margins(0)
            plt.subplots_adjust(bottom=0.15)
            
            plt.xlabel('delta'+' ( Numbers of Groups= '+str(kmeans_k)+')') 
            plt.ylabel('wrq')
            plt.title('')
             
            #网格
            plt.grid(alpha=1,axis='y',linestyle='-')  
            plt.subplots_adjust(right=0.72)
            #plt.show()
            plt.savefig('output/wrq/'+'_e('+str(E[e])+')_k('+str(kmeans_k)+ ')'+'.png')
            
        
    