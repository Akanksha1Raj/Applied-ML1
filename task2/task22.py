#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Feb  6 03:09:13 2019

@author: akanksha_rajput
"""

import pandas as pd
from sklearn.datasets import load_iris 
import matplotlib.pyplot as plt
dataset = load_iris()
fig, ax = plt.subplots(4, 5, figsize=(17,17))
for i in range(4):
    ax[i,4].set_yticks([])
    ax[i,4].set_xticks([])
    ax[i,4].axis('off')
plt.subplots_adjust(wspace=0, hspace=0) 
values = [0,1,2]
species = ['virginica','setosa', 'versicolor']
colors = ["blue","red", "green"]
for i in range(4):
    ax[i,0].set_ylabel(dataset.feature_names[i])
    for j in range(4):
        if (i != 3):
            ax[i,j].set_xticklabels([])
            ax[i,j].set_xticks([])
        if (j != 0):
            ax[i,j].set_yticklabels([])
            ax[i,j].set_yticks([])
        if (i == j):
            ax[i,i].hist(dataset['data'][:,i])
            if (i == 3):
                ax[i,j].set_xlabel(dataset.feature_names[i])
        else:
            for data, color, s in zip(values, colors, species):
                ax[i, j].scatter(dataset.data[dataset.target==data][:,j], dataset.data[dataset.target==data][:,i] , c=color, label = s)    
            if (i == 3):
                ax[i,j].set_xlabel(dataset.feature_names[j])

handles, labels = ax[0,1].get_legend_handles_labels()                
plt.legend(handles,labels)
plt.savefig('task22.png')