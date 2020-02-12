# -*- coding: utf-8 -*
import numpy as np
#import choicek
import k_means

def fileInit(fileName):
    file = open(fileName, 'w')
    file.close()


def solve(segNum, choiceNum, k,all_epsilon):
    fileName ='tempTrails.txt'
    file = open(fileName, 'r')
    infos = file.readlines()
    file.close()
    ran = np.random.choice(len(infos) // segNum, choiceNum, replace=False)
    fileName ='temp/' + 'k(' + str(
                k) + ')_e(' + str(all_epsilon) + ')' +  'output_trails.txt'
    fileInit(fileName)
    fileName ='temp/' + 'k(' + str(
                k) + ')_e(' + str(all_epsilon) + ')' +  'output_centers.txt'
    fileInit(fileName)
    fileName ='temp/' + 'k(' + str(
                k) + ')_e(' + str(all_epsilon) + ')' +  'output_labels.txt'
    fileInit(fileName)

    outputName ='temp/' + 'k(' + str(
                k) + ')_e(' + str(all_epsilon) + ')' +  'output_trails.txt'
    fileName = open(outputName, 'a')
    for i in range(choiceNum):
        for ite in range(segNum):
            p = infos[ran[i] * segNum + ite].split()
            print(float(p[0]), float(p[1]), end='\n', file=fileName)
    fileName.close()
    points = []
    for ite in range(segNum):
        print(ite)
        points.append([])
        for i in range(choiceNum):
            p = infos[ran[i] * segNum + ite].split()
            points[ite].append([float(p[0]), float(p[1])])

        points[ite] = np.array(points[ite])
        '''
        solver = choicek.ExpChoice(
            points[ite], k,
            np.random.choice(len(points[ite]), 10, replace=False), 10)
        centers, labels = solver.solve(epsilon)
        '''
        centers,labels=k_means.k_means_null(points[ite],k)

        outputName ='temp/' + 'k(' + str(
                k) + ')_e(' + str(all_epsilon) + ')' +  'output_centers.txt'
        fileName = open(outputName, 'a')
        for it in centers:
            print(it[0], it[1], end='\n', file=fileName)
        fileName.close()

        outputName ='temp/' + 'k(' + str(
                k) + ')_e(' + str(all_epsilon) + ')' +  'output_labels.txt'
        fileName = open(outputName, 'a')
        for it in labels:
            print(it, end='\n', file=fileName)
        fileName.close()