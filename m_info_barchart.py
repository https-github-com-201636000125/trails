import numpy as np
import matplotlib.pyplot as plt
'''
将标注OURS1改成OURS2，将OURS3改成OURS1
'''
#互信息
def read_m_info(K,epsilon,pro_name):
    means=[]
    for i in range(len(pro_name)):
        means.append([])
    for kmeans_k in K:
        for p in range(len(pro_name)):
            fileName=pro_name[p]+'/'+pro_name[p]+'/output/'+'k(' + str(
                    kmeans_k) + ')_e(' + str(epsilon) + ')m_info' + '.txt'
            f=open(fileName,'r')
            infos=f.readlines()
            f.close()
            means[p].append(float(infos[0]))
    return means

if __name__ == '__main__':
    pro_name=['INFOCOM15','INFOCOM17','OURS1','OURS3']
    K = [10, 20, 30, 40, 50, 60, 70, 80]
    E = [0.1, 0.5, 1.0, 1.5, 2.0]
    
    for epsilon in E:
        means=read_m_info(K,epsilon,pro_name)
        infocom15_means=tuple(means[0])
        infocom17_means=tuple(means[1])
        ours1_means=tuple(means[2])
        ours3_means=tuple(means[3])
        
        plt.figure()
        print(ours3_means.__class__)
        ind = np.arange(len(infocom15_means))  # x轴
        
        width = 0.25  #柱宽
        deltaDis=width/10
        fig, ax = plt.subplots()
        rects1 = ax.bar(ind - width*3/4-deltaDis*2, infocom15_means, width/2,
                        color='#000000', label='INFOCOM15')
        rects2 = ax.bar(ind - width/4-deltaDis, infocom17_means, width/2,
                        color='#FAEBD7', label='INFOCOM17')
        rects4 = ax.bar(ind + width*3/4+deltaDis, ours3_means, width/2,
                        color='#DCDCDC', label='OURS1')
        rects3 = ax.bar(ind + width/4, ours1_means, width/2,
                        color='#808A87', label='OURS2')
        
        ax.set_xlabel('Numbers of Groups'+' (epsilon='+str(epsilon)+')')
        ax.set_ylabel('Mutual Inforcomation')
        ax.set_title('')
        ax.set_xticks(ind)
        ax.set_xticklabels(tuple(K))
        ax.legend(loc=2, bbox_to_anchor=(1.05,1.0),borderaxespad = 0)
        
        # 去除图形顶部边界和右边界的刻度
        plt.tick_params(top= 'off', right= 'off')
        plt.subplots_adjust(right=0.74)
        #plt.show()
        plt.savefig('output/Mutual Inforcomation/'+'_e('+str(epsilon)+')'+'.png')
        
        
        
        
        