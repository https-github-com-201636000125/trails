# -*- coding: utf-8 -*-
"""
Created on Fri Jan 10 20:19:10 2020

@author: 24457
"""

from numpy.random import random,geometric
import numpy as np

def randomise(_epsilon,_sensitivity):
    _gamma = 1/(1 + np.exp(_epsilon / 2))
    _sensitivity = 1
    sign = -1 if random() < 0.5 else 1
    geometric_rv = geometric(1 - np.exp(-_epsilon)) - 1
    unif_rv = random()
    binary_rv = 0 if random() < _gamma / (_gamma + (1 - _gamma) *np.exp(- _epsilon))else 1
    return sign *((1-binary_rv)*((geometric_rv+ _gamma * unif_rv) * _sensitivity) + \
            binary_rv* ((geometric_rv +_gamma + (1-_gamma) *  unif_rv) * _sensitivity))

if __name__ == '__main__':
    pass