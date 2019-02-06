#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Feb  6 03:10:28 2019

@author: akanksha_rajput
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import requests

url_defined = False

print("Set url_defined True and put the URL in the else part if you would like to access the data using URL")
if (url_defined == False):
    df = pd.read_csv(r"/Users/akanksha_rajput/Documents/ml/homework-1-Akanksha1Raj/task2/mpg.csv")
else:
    url="https:......csv"
    s=requests.get(url).content
    c=pd.read_csv(io.StringIO(s.decode('utf-8')))
    

groups = df.groupby('drv')
def jitter(a,n):
    stdev = n*(max(a)-min(a))
    return a + np.random.randn(len(a)) * stdev

fig, ax = plt.subplots(2, 2, figsize=(10,10))

for name, group in groups:
    ax[0,0].plot(group.displ, group.hwy, marker='o',linestyle='', ms=8, label=name)
for name, group in groups:
    ax[0,1].plot(group.displ, group.hwy, marker='o', linestyle='', ms=8, label=name, alpha =0.5) 
for name, group in groups:
    ax[1,0].plot(jitter(group.displ,.01), jitter(group.hwy,.01), marker='o', linestyle='', ms=8, label=name, alpha =0.5)
for name, group in groups:
    ax[1,1].plot(jitter(group.displ,0.4), jitter(group.hwy,0.4), marker='o', linestyle='', ms=8, label=name, alpha =0.5)

ax[0,0].set_ylabel('fuel economy (mpg)')
ax[0,0].set_xlabel('displacement (l)')
ax[0,0].set_title('Orgininal Data Points')
ax[0,0].legend()

ax[0,1].set_ylabel('fuel economy (mpg)')
ax[0,1].set_xlabel('displacement (l)')
ax[0,1].set_title('Applying Alpha to Tranparent the data')
ax[0,1].legend()

ax[1,0].set_ylabel('fuel economy (mpg)')
ax[1,0].set_xlabel('displacement (l)')
ax[1,0].set_title('Applying Jitter to Introduce Noise')
ax[1,0].legend()

ax[1,1].set_ylabel('fuel economy (mpg)')
ax[1,1].set_xlabel('displacement (l)')
ax[1,1].set_title('Original Information is lost by Applying  a lot of Jitter') 
ax[1,1].legend()

plt.savefig('task23.png')