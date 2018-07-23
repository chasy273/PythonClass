#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jul 23 15:52:18 2018

@author: sorabhchadha
"""

x = 1
y = 1 
z = 5
res = x < y
print(res)

res = y < x and z < y
print(res)
res = x = z
print(res)

res = y < x or y == z 
print(res)


