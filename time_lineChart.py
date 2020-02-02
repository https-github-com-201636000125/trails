# encoding=utf-8
import matplotlib.pyplot as plt

def read_time(K,epsilon,pro_name):
    means=[]
    for i in range(len(pro_name)):
        means.append([])
    for p in range(len(pro_name)):
        for kmeans_k in K:
            fileName=pro_name[p]+'/'+pro_name[p]+'/output/'+'k(' + str(
                    kmeans_k) + ')_e(' + str(epsilon) + ')' + '.txt'
            f=open(fileName,'r')
            infos=f.readlines()
            f.close()
            means[p].append(float(infos[len(infos)-1]))
    return means


if __name__ == '__main__':
    
    pro_name=['INFOCOM15','INFOCOM17','OURS1','OURS3']
    K = [10, 20, 30, 40, 50, 60, 70, 80]
    E = [0.1, 0.5, 1.0, 1.5, 2.0]
    
    
    for e in range(len(E)):
        means=read_time(K,E[e],pro_name)
        infocom15_means=tuple(means[0])
        infocom17_means=tuple(means[1])
        ours1_means=tuple(means[2])
        ours3_means=tuple(means[3])
        #pl.xlim(-1, 11) # 限定横轴的范围
        #pl.ylim(-1, 110) # 限定纵轴的范围
        
        p_long=9
        p_width=7
        #初始化画布
        plt.figure(figsize=(p_long,p_width))
        
        #x轴
        names = [10, 20, 30, 40, 50, 60, 70, 80]
        x = range(len(names))       
        plt.plot(x, infocom15_means,marker='p',label='INFOCOM15')
        plt.plot(x, infocom17_means,marker='*',label='INFOCOM17')
        plt.plot(x, ours1_means,marker='s',label='OURS1')
        plt.plot(x, ours3_means,marker='x',label='OURS3')
        
        #plt.legend(loc='best') # 让图例生效
        plt.legend(loc=2, bbox_to_anchor=(1.05,1.0),borderaxespad = 0)
        plt.xticks(x, names, rotation=45)
        plt.margins(0)
        plt.subplots_adjust(bottom=0.15,right=0.74)
        
        plt.xlabel('Numbers of Groups') 
        plt.ylabel('time(s)')
        plt.title('')
        
        #网格
        plt.grid(alpha=1,axis='y',linestyle='-')  
        
        #plt.show()
        plt.savefig('output/time/'+'_e('+str(E[e])+')'+'.png')

    