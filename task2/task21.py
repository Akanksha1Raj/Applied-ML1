#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Feb  4 16:52:09 2019

@author: akanksha_rajput
"""

import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv(r"/Users/akanksha_rajput/Documents/ml/homework-1-Akanksha1Raj/task2/Oregon.csv")
ax1 = plt.gca()
line1, = ax1.plot(df["year"], df["marriage_rate"], '-o')
ax2 = ax1.twinx()
line2, = ax2.plot(df["year"], df["money_movie"],'-o' ,c='r')
ax1.set_ylabel("Marriage rate in Oregon")
ax2.set_ylabel("Money spent on movie theater admission")
ax1.set_xlabel ("Years")
ax1.set_title ("Marriage rate in Oregon versus Money spent on movie")
ax2.legend((line1, line2),
           ("Marriage rate in Oregon", "Money spent on movie theater admission"))
plt.savefig('task21.png')