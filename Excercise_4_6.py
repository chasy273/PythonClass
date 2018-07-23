#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jul 23 16:34:21 2018

@author: sorabhchadha
"""

s1 = int(input("Enter first side s1"))
s2 = int(input("Enter first side s2"))
s3 = int(input("Enter first side s3"))

if ((s1 > 0, s2 > 0, s3 > 0) and (s1 != s2 and  s2 != s3 and s1!= s3)):
    
    print("True")
else:
    print("False")
