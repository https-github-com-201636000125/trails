# encoding=utf-8
import matplotlib.pyplot as plt

def read_wrq(pro_name,E,K,D):
    #name*epsilon*k*delta
    means=[]
    for p in range(len(pro_name)):
        means.append([])
        for e in range(len(E)):
            means[p].append([])
            for k in range(len(K)):
                means[p][e].append([])
                for d in range(len(D)):
                    fileName=pro_name[p]+'/'+pro_name[p]+'/output/'+'k(' + str(K[k]) + \
                        ')_e(' + str(E[e]) +')_delta('+str(D[d])+ ')wrq' + '.txt'
                    f=open(fileName,'r')
                    infos=f.readlines()
                    f.close()
                    means[p][e][k].append(float(infos[0]))
    return means

def get_info(means,p,e,K,d):
    re=[]
    for k in range(len(K)):
        re.append(means[p][e][k][d])
    return re

if __name__ == '__main__':
    
    pro_name=['INFOCOM15','INFOCOM17','OURS1','OURS3']
    K = [10, 20, 30, 40, 50, 60, 70, 80]
    E = [0.1, 0.5, 1.0, 1.5, 2.0]
    D = [0.4,0.6,0.8,1.0]
    
    #means ( name*epsilon*k*delta )
    means=read_wrq(pro_name,E,K,D)
    
    
    for e in range(len(E)):
        
        #初始化画布
        p_long=9
        p_width=9
        fig=plt.figure(figsize=(p_long,p_width))
        
        #pl.xlim(-1, 11) # 限定横轴的范围
        #pl.ylim(-1, 110) # 限定纵轴的范围
        ax=[]
        for d in range(len(D)):
            #x轴
            names = K
            x = range(len(names))
            
            #2行2列第（d+1）个子图
            new=fig.add_subplot(220+d+1)
            
            infocom15_means=get_info(means,0,e,K,d)
            infocom17_means=get_info(means,1,e,K,d)
            ours1_means=get_info(means,2,e,K,d)
            ours3_means=get_info(means,3,e,K,d)
            
            new.plot(x, infocom15_means,linewidth=1.8,linestyle='-.',marker='p',label='INFOCOM15')
            new.plot(x, infocom17_means,linewidth=1.8,linestyle='-.',marker='*',label='INFOCOM17')
            new.plot(x, ours1_means,linewidth=1.8,linestyle='-.',marker='s',label='OURS1')
            new.plot(x, ours3_means,linewidth=1.8,linestyle='-.',marker='x',label='OURS3')
            
            ax.append(new)
        
            plt.plot(fontsize=15)
            plt.legend(loc='best') # 让图例生效
            #plt.legend(loc=2, bbox_to_anchor=(1.05,1.0),borderaxespad = 0)
            plt.xticks(x, names, rotation=45,fontsize=15)
            plt.yticks(fontsize=15)
            plt.margins(0)
            plt.subplots_adjust(bottom=0.15)
            plt.xlabel('(Numbers of Groups)',fontsize=15) 
            plt.ylabel('wrq',fontsize=15)
            
            #网格
            plt.grid(alpha=1,linestyle='-.',c='gray')  
            #plt.subplots_adjust(right=0.72)
        #plt.show()
        plt.savefig('output/wrq/'+'_e('+str(E[e])+')'+'.png')
            
        
    