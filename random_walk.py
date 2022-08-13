#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon May 10 21:03:25 2021
@author: aliemirkaragulle
"""
import random
import matplotlib.pyplot as plt

""" Random Walk Simulation 2-D """

#Assume a walker is walking on a line (2-Dimensions). 
#The walker can only go to the left or to the right.

#Discrete Walk
def random_walk_v1(T):
    x = 0 #Initial position
    for t in range(T):
        if random.normalvariate(0, 0.5) < 0: #coin flip
            x -= 1 #go left
        else:
            x += 1
    return x

#Continuous
def random_walk_v2(T):
    x = 0 
    for t in range(T):
        x += random.normalvariate(0,1)
    return x

#Let's collect the trajectory, position in each time step, of the walker in a list.

def random_walk(T):
    x = 0
    l = [x]
    for t in range(T):
        x += random.normalvariate(0, 1)
        l.append(x)
    return l

T = 100
num_walkers = 10 
t = list(range(0,T+1)) # x- axis/ 
#t should be of the same length with l and since l defined in the function starts with a length equal to 1,
#we have to add 1 to the t, otherwise they will have different shapes.

#Graph each walkers trajectory. 
#x-axis is number of epochs, y-axis is the walkers' location 
for walkers in range(num_walkers):
    l = random_walk(T) # y-axis
    plt.plot(t,l)