#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Feb  4 15:57:02 2019

@author: akanksha_rajput
"""
import pandas as pd

def n_m_sum(df):
    print("hello")
    df= df.set_index('year')
    df.fillna(0, inplace=True)
    k = df.shape
    df.replace('--',float(0), inplace=True)
    df['2010']= df['2010'].astype(float)
    df['2010']= df['2010'].astype(float)
    sum = df['2010'].sum()
    return k[0], k[1], sum

