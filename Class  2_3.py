#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jul 30 16:25:23 2018

@author: sorabhchadha
"""

   # Write a program to output a backwards count by 5s from 100 down a number 
#    between 50 and 100 that is input before the countdown begins. The program 
#    should stop when the count would be greater than the number input.
   
x = int(input( "Enter number between 50 and 100"))
count = 100
while count > x:
    print (count)
    count = count-5
    

    
       