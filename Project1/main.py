# -*- coding: utf-8 -*-

"""
@title Project 1
@author Sotheanith Sok

This is the project 1 for EE 381 Spring 2018

"""

"""
Problem 1:
Write a program that determines and outputs the mean, median, mode, and 
standard deviation for a simple discrete data set entered by the user.
Use the data set [3, 2, 4, 1, 2, 3, 4, 3, 5, 10] as input into your program.
"""
import collections
import math
def summaryStatistics():
    c=[]
    done=False
    print('Part 1: Summaray Statistics')
    print('-Getting User Input-')
    while(not done):
        try:
            c.append(int(input('Enter your number:')))
        except ValueError:
            done=True
            print('-Solution-')
            
    #Calculate mean
    mean=sum(c)/len(c)
    print('Mean of your input is ',round(mean,4))
    
    #Calculate median
    c.sort()
    if(len(c)%2==0):
        median=(c[int(len(c)/2)-1]+c[int(len(c)/2)])/2
    else:
        median=c[int(len(c)/2)]
    print('Median of your input is ',median)
    
    #Calculate mode
    mode=[]
    i=0
    c1=(collections.Counter(c)).most_common()
    if(c1[0][1]<2):
        print('There is no mode for your input.')
    else:
        while(c1[i][1]==c1[0][1]):
            mode.append(c1[i][0])
            i+=1
        print('Mode of your input is ',', '.join(str(s) for s in mode))
    
    #Calculate standard deviation
    variance=sum(((x-mean)**2 for x in c))/len(c)
    print('The standard deviation of your input is ',round(math.sqrt(variance),4))

"""
Problem 2: 
Write a program in Python that generates 100 pseudorandom numbers in [0,1). Format it to four
decimal postions.
Use 𝑁 = 10000, 𝐴 = 4857, 𝑀 = 8601
When you generate random numbers from this what is the mean of the numbers generated?
That is write a program to determine the mean of the 100 numbers.
"""
def randomNumberGenerator():
    #Variables
    l=[]
    N=10000
    A=4857
    M=8601
    
    #Get user input
    print('Part 2: Random Number Generator')
    s=int(input("Enter the seed:"))
    z=int(input("Enther the amount of number you want:"))
    
    for i in range(z):
        s=(M*s+A)%N
        l.append(round(s/N,4))
    print('The mean of random number generated is',round(sum(l)/z,4))

"""
Problem 3:
Three balls are tossed randomly into 5 cans. 
What is the probability that they all land in different cans?
(Note each can is able to hold from 0 to 3 balls.)
"""
def probabilityCalculation():
    #Variable
    slot=[0]*3
    total=0
    N=10000
    A=4857
    M=8601
    S=0
    
    #Get user input
    print('Part 3: Probability Calculation')
    s=int(input("Enter the numbers of trial you want to do: "))
    #Start the program
    for i in range(s):
        for j in range (3):
            S=(M*S+A)%N
            pick=S/N    
            slot[j]=int(pick*5)
        c1=(collections.Counter(slot)).most_common()
        if(c1[0][1]==1):
            total+=1
        slot=[0]*3
    print('The probability of three balls tossed and all three land in different cans is',round(total*100/s,4))
        
    

        
        

