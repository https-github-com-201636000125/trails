import solveTravels
import ReMakeTrails
import time
import get_sign


class Solver:
    def __init__(self, segNum=32, choiceNum=1000, k=40, real_alpha=0, real_beta=1.5):
        self.segNum = segNum
        self.choiceNum = choiceNum
        self.k = k
        self.real_alpha = real_alpha
        self.real_beta = real_beta

    def work(self, E, D):

        # maxlen=ReMakeTrails.get_maxlen(trails,self.segNum,self.choiceNum)
        '''
        print(maxlen)
        '''
        # myTrie=ReMakeTrails.get_trails_trie(self.segNum,self.choiceNum,centers,labels,maxlen)
        # real轨迹，轨迹数，轨迹real之和
        for epsilon in E:
            a = time.time()
            solveTravels.solve(self.segNum, self.choiceNum,
                               self.k, epsilon/(2.0*self.segNum))
            fileName = 'output/' + 'k(' + str(
                self.k) + ')_e(' + str(epsilon) + ')' + 'Cluster_time.txt'
            fout = open(fileName, 'w')
            print(time.time() - a, file=fout)
            fout.close()
            trails = ReMakeTrails.get_second_trails('output_trails.txt',
                                                    self.segNum,
                                                    self.choiceNum)
            centers = ReMakeTrails.get_second_centers('output_centers.txt',
                                                      self.segNum, self.k)
            labels = ReMakeTrails.get_second_labels('output_labels.txt',
                                                    self.segNum,
                                                    self.choiceNum)
            # ReMakeTrails.centers_add_noisy(trails,centers,labels,self.segNum,
            #                                     self.choiceNum,self.k,epsilon/(2*self.segNum))
            maxlen = ReMakeTrails.get_maxlen(trails, self.segNum,
                                             self.choiceNum)
            myTrie = ReMakeTrails.get_trails_trie(self.segNum, self.choiceNum,
                                                  centers, labels, maxlen)
            fileName = 'output/' + 'k(' + str(
                self.k) + ')_e(' + str(epsilon) + ')' + '.txt'
            # ours1,ours3不同epsilon分配
            realTrails, realCnt, realSum = ReMakeTrails.get_real_trails(
                myTrie, self.segNum, self.choiceNum, centers, labels, epsilon/(2.0))

            newTrails = ReMakeTrails.add_virtual_trails(
                realTrails, realCnt, realSum, centers, self.segNum, self.choiceNum, self.k, maxlen, myTrie)
            ReMakeTrails.output_trails(newTrails, fileName)

            fout = open(fileName, 'a')
            print(time.time() - a, file=fout)
            fout.close()

            # 以下计算并输出对比参数
            # 选中轨迹
            fileName = 'output/' + 'k(' + str(
                self.k) + ')_e(' + str(epsilon) + ')selected_trails' + '.txt'
            ReMakeTrails.output_selected_trails(
                trails, fileName, self.segNum, self.choiceNum)

            # 发布轨迹
            fileName = 'output/' + 'k(' + str(
                self.k) + ')_e(' + str(epsilon) + ')final_trails' + '.txt'
            ReMakeTrails.output_final_trails(
                labels, newTrails, fileName, self.segNum, self.choiceNum)

            # Hausdorff距离
            fileName = 'output/' + 'k(' + str(
                self.k) + ')_e(' + str(epsilon) + ')Hausdorff' + '.txt'
            sign_Hausdorff = get_sign.get_Hausdorff(
                newTrails, trails, self.segNum, self.choiceNum)
            get_sign.output_Hausdorff(fileName, sign_Hausdorff)

            # 互信息
            # def get_m_info(newTrails,labels,trails,centers,maxlen,segNum,choiceNum):
            fileName = 'output/' + 'k(' + str(
                self.k) + ')_e(' + str(epsilon) + ')m_info' + '.txt'
            sign_m_info = get_sign.get_m_info(
                newTrails, labels, trails, centers, maxlen, self.segNum, self.choiceNum)
            get_sign.output_m_info(fileName, sign_m_info)

            # wrq
            for delta in D:
                fileName = 'output/' + 'k(' + str(
                    self.k) + ')_e(' + str(epsilon) + ')_delta('+str(delta) + ')wrq' + '.txt'
                sign_wrq = get_sign.get_wrq(
                    newTrails, trails, delta, self.segNum, self.choiceNum)
                get_sign.output_wrq(fileName, sign_wrq)

            print("done", self.k, epsilon)


# 半径delta最好是0.2,0.4,0.6,0.8,1.0
# k=60,e=1.0
if __name__ == '__main__':
    K = [10, 20, 30, 40, 50, 60, 70, 80]
    E = [0.1, 0.5, 1.0, 1.5, 2.0]
    D = [0.4, 0.6, 0.8, 1.0]
    for k in K:
        sol = Solver(32, 1000, k, 0, 1.5)
        sol.work(E, D)
    # sol=Solver()
    # sol.gao("output_trails_data.txt")
    pass
