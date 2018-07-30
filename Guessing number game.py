#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jul 30 16:39:50 2018

@author: sorabhchadha
"""

# Write a program that generates a random number (0-10) and ask you to 
#    guess it. You have three attempts.

import random as rm 
temp = rm.randint(0,10)
count = 1
number = ""
while (count <= 3) and (temp != number):
    
    
    number = input ("Your guess")
    
    
    
    
    
    if number == temp:
        print("Congratulations you guessed a correct number") 
    else:
        print("Try again")
        count += 1
print("You do have any attempts left")
    

        
#