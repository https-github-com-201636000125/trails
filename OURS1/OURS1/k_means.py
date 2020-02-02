# -*- coding: utf-8 -*-
import math
import random
import numpy as np


def getD2(centers, point):
    res = math.inf
    for center in centers:
        res = min(res, ((point - center)**2).sum())
    return res


def get_centers_null(points, k):
    n = len(points)
    tot = n
    vis = [False for i in range(len(points))]
    newpoints = []
    while n > 0 and tot > 0:
        x = np.random.randint(0, tot)
        for i in range(len(points)):
            if vis[i]:
                continue
            if x == 0:
                x = i
                break
            x -= 1
        tmp = []
        for i, point in enumerate(points):
            if vis[i]:
                continue
            tmp.append([i, ((point - points[x])**2).sum()])
        tmp.sort(key=lambda x: x[1])
        tmp = tmp[:min(k, tot)]
        for p in tmp:
            vis[p[0]] = True
            newpoints.append(points[p[0]])
        tot -= len(tmp)
        n//=2
    return get_centers_pp(np.array(newpoints), k)
def get_centers_pp(points, k):
    centers = []
    centers.append(random.choice(points))
    for _ in range(k - 1):
        dis2 = np.array([getD2(centers, p) for p in points])
        rd = np.random.random() * dis2.sum()
        for i in range(len(dis2)):
            rd -= dis2[i]
            if rd < 0:
                centers.append(points[i])
                break
    return centers
def get_centers(points, k):
    return points[np.random.choice(len(points), k, replace=False)]
def get_labels(points, centers):
    distances = np.zeros((points.shape[0], len(centers)))
    for i in range(len(centers)):
        distances[:, i] = ((points - centers[i])**2).sum(axis=1)
    labels = np.argmin(distances, axis=1)
    return labels
def update_centers(points, centers, T=100):
    w = 0.1
    D = np.array([getD2(centers, p) for p in points]).sum()
    while (1):
        labels = get_labels(points, centers)
        for i in range(len(centers)):
            p_i = points[labels == i]
            if len(p_i)==0 :
                continue
            new_center = np.zeros(points.shape[1])
            for p in p_i:
                new_center += p
            new_center = new_center / len(p_i)
            centers[i] = w * centers[i] + (1.0 - w) * new_center
        newD = np.array([getD2(centers, p) for p in points]).sum()
        if newD > D:
            break
        D = newD
        T -= 1
        if T == 0:
            break
def k_means_null(points, k, T=100):
    centers = get_centers_null(points, k)
    update_centers(points, centers, T)
    labels = get_labels(points, centers)
    return centers, labels
def k_means_pp(points, k, T=100):
    centers = get_centers_pp(points, k)
    update_centers(points, centers, T)
    labels = get_labels(points, centers)
    return centers, labels
def k_means(points, k, T=100):
    centers = get_centers(points, k)
    update_centers(points, centers, T)
    labels = get_labels(points, centers)
    return centers, labels
if __name__ == "__main__":   
    pass
