import numpy as np
import matplotlib.pyplot as plt

'''
将标注OURS1改成OURS2，将OURS3改成OURS1
'''
#互信息
def read_m_info(K,E,p,pro_name):
    means=[]
    for e in range(len(E)):
        means.append([])
    for kmeans_k in K:
        for e in range(len(E)):
            epsilon=E[e]
            fileName=pro_name[p]+'/'+pro_name[p]+'/output/'+'k(' + str(
                    kmeans_k) + ')_e(' + str(epsilon) + ')' + '.txt'
            f=open(fileName,'r')
            infos=f.readlines()
            f.close()
            noisy_time=float(infos[len(infos)-1])
            
            fileName=pro_name[p]+'/'+pro_name[p]+'/output/'+'k(' + str(
                    kmeans_k) + ')_e(' + str(epsilon) + ')Cluster_time' + '.txt'
            f=open(fileName,'r')
            infos=f.readlines()
            f.close()
            noisy_time-=float(infos[0])
            
            means[e].append(noisy_time)
    return means

if __name__ == '__main__':
    pro_name=['INFOCOM15','INFOCOM17','OURS1','OURS3']
    output_name=['INFOCOM15','INFOCOM17','OURS2','OURS1']
    K = [10, 20, 30, 40, 50, 60, 70, 80]
    E = [0.1, 0.5, 1.0, 1.5, 2.0]
    
    for p in range(len(pro_name)):
        means=read_m_info(K,E,p,pro_name)
        
        info=[]
        for i in range(len(means)):
            #print(len(means[i]))
            info.append(tuple(means[i]))
        
        plt.figure()
        print(info[0].__class__)
        ind = np.arange(len(info[0]))  # x轴
        
        width = 0.25  #柱宽
        deltaDis=width/10
        fig, ax = plt.subplots()
        rects1 = ax.bar(ind - width*3/4-deltaDis*2, info[0], width/2,
                        color='#000000', label='epsilon='+str(E[0]))
        rects2 = ax.bar(ind - width/4-deltaDis, info[1], width/2,
                        color='#FAEBD7', label='epsilon='+str(E[1]))
        rects3 = ax.bar(ind + width/4, info[2], width/2,
                        color='#DCDCDC', label='epsilon='+str(E[2]))
        rects4 = ax.bar(ind + width*3/4+deltaDis, info[3], width/2,
                        color='#F5DEB3', label='epsilon='+str(E[3]))
        rects5 = ax.bar(ind + width*5/4+deltaDis*2, info[4], width/2,
                        color='#808A87', label='epsilon='+str(E[4]))
        
        ax.set_xlabel('Numbers of Groups'+' ('+output_name[p]+')')
        ax.set_ylabel('noisy time')
        ax.set_title('')
        ax.set_xticks(ind)
        ax.set_xticklabels(tuple(K))
        ax.legend(loc=2, bbox_to_anchor=(1.05,1.0),borderaxespad = 0)
        
        # 去除图形顶部边界和右边界的刻度
        plt.tick_params(top= 'off', right= 'off')
        plt.subplots_adjust(right=0.74)
        plt.grid(axis='y',alpha=1,linestyle='--',c='gray')
        #plt.show()
        plt.savefig('output/noisy_time_barchart/'+'_name('+output_name[p]+')'+'.png')
        
        
        
        
        