#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jul 30 15:08:56 2018

@author: sorabhchadha
"""
password = ""
count = 1

while (count <= 3) and password != "belinda":
    password = input ("Enter your passowrd: ")
    count += 1
    if password == "belinda":
        print ("Sucessfull")
    else:
       print ("Please try again")
        



  #Write a program that will ask the user for a message and the number of 
#    times they want that message displayed. Then output the message that 
#    number of times.
    
message = str (input(" Please enter your messsage"))
number = int (input("how many times you need to display that message"))
while number > 0:
    print (message)
    

    
    
    
    
