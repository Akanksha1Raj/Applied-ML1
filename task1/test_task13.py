#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Feb  4 15:57:02 2019

@author: akanksha_rajput
"""
import pandas as pd
from task13 import n_m_sum

df = pd.read_csv("input.txt",  encoding = "utf-16be", escapechar="\\")
row, col, sum_p = n_m_sum(df)
def test_rows_1():
    assert row == 225
def test_cols_1():
    assert col == 31
def test_sum_1():
    assert int(sum_p) == 7065
    