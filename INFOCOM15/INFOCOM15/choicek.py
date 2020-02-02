import numpy as np
import k_means
import math


def dis(a, b):
    return math.sqrt(((a - b)**2).sum())


def MeanDist(points, centers, labels):
    res = 0
    for i in range(len(points)):
        res += dis(points[i], centers[labels[i]])
    return res / len(points)


def U(points, centers, labels, mdp):
    return MeanDist(points, centers, labels) / mdp


class Partition:
    def __init__(self, centers, labels, p=1):
        self.centers = centers
        self.labels = labels
        self.p = p


class Modification:
    def __init__(self, T, Gk, Gopt, dis):
        self.T = T
        self.Gk = Gk
        self.Gopt = Gopt
        self.dis = dis


class ExpChoice:
    def __init__(self, points, k, idx, phi):
        self.points = points
        self.k = k
        self.idx = idx
        self.phi = phi
        self.optCenters, self.optLabels = k_means.k_means(self.points, self.k)
        self.mdp = MeanDist(self.points, self.optCenters, self.optLabels)
        self.pars = [Partition(self.optCenters, self.optLabels)]

    def getS(self):
        for del_i in self.idx:
            newP = []
            newC = self.optCenters.copy()
            for i in range(len(self.points)):
                if i != del_i:
                    newP.append(self.points[i])
            newP = np.array(newP)
            k_means.update_centers(newP, newC)
            lab = k_means.get_labels(self.points, newC)
            self.pars.append(
                Partition(newC, lab, U(self.points, newC, lab, self.mdp)))

    def PhiSubOptimal(self):
        indvSubs = self.PhiSubOptimalIndividual()
        res = [[indvSubs[0]]]
        for i in range(1, len(indvSubs)):
            a = indvSubs[i]
            temp = [[a]]
            for mod in res:
                f = True
                for elm in mod:
                    if elm.T == a.T:
                        f = False
                        break
                if f:
                    newMod = mod.copy()
                    newMod.append(a)
            res.extend(temp)
            res.sort(key=lambda x: np.array([i.dis for i in x]).sum())
            if len(res) > self.phi:
                res = res[:self.phi]
        return res

    def PhiSubOptimalIndividual(self):
        mods = []
        for i, point in enumerate(self.points):
            for j, center in enumerate(self.optCenters):
                if j == self.optLabels[i]:
                    continue
                d = dis(point, center) - dis(
                    point, self.optCenters[self.optLabels[i]])
                mods.append(Modification(i, j, self.optLabels[i], d))
        mods.sort(key=lambda x: x.dis)
        return mods[:self.phi]

    def getPhi(self):
        phiSubOpt = self.PhiSubOptimal()
        for mod in phiSubOpt:
            tmpLab = self.optLabels.copy()
            for elm in mod:
                tmpLab[elm.T] = elm.Gk
            self.pars.append(
                Partition(self.optCenters, tmpLab,
                          U(self.points, self.optCenters, tmpLab, self.mdp)))

    def solve(self, epsilon):
        s = 0
        self.getS()
        self.getPhi()
        for par in self.pars:
            s += math.exp(epsilon / 2.0)
        s = np.random.random() * s
        for par in self.pars:
            s -= math.exp(epsilon / 2.0)
            if s < 0:
                return par.centers, par.labels
        assert (False)


if __name__ == '__main__':
    a = []
    for i in range(100):
        a.append(np.random.random(2) * 100)
    a = np.array(a)
    idx = [1, 2, 3, 4]
    test = ExpChoice(a, 10, idx, 4)
    test.getS()
    test.getPhi()
    print(test.solve(0.1))
    pass
