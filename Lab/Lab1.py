# -*- coding: utf-8 -*-
"""
Created on Wed Jan 24 11:19:51 2018

@author: Sotheanith Sok

Purpose: Pseudorandom number generator tutorial
"""
import math
#Below the parameters in the formula are assigned their values. 

M = 41
A = 31
N = 100

#Below is a prompt for the user to enter their seed.
S=int(input("Enter the value of your seed.\n"))

#Below is the formula for the pseudorandom generator
for i in range(15):
    S=(M*S+A)%N
    #Make it between [0,1)
    r=S/N
    #print ("%.3f"%r)
    number=math.floor(r*6+1)
    print(number);
    
