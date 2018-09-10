"""
@title Project 3
@author Sotheanith Sok

This is the project 3 for EE 381 Spring 2018

Note: This project is heavily helped by Professor John De Sulima-Przyborowski at California
State University of Long Beach for EE381

"""
"""
Problem 2:
Consider the same simple binomial distribution experiment as above with five trials and in each trial the probability of
success is 0.7. What is the expected (average) value?

Augment the program from simulation 1 to calculate the expected value of the binomial r.v
"""

#Import
import random

#Variables
p=0.7 #Probability of success
x=3 #Target success
n=5 #Number of trials per run.
N=1000000 #Number of run

#Counters
runCount=0
trialCount=0

#Store all number of trial
allResult=[0]*(n+1)

#Loop for run
for i in range(N): 
    
    #Loop for trial
    for j in range(n):
        result=random.uniform(0,1)
        
        #if success, add one to trial counter
        if(result<p):
            trialCount=trialCount+1
            
    #If achieve a target number of success per trial, add one to run counter
    if(trialCount==x):
        runCount=runCount+1
    
    #Store the result
    allResult[trialCount]=allResult[trialCount]+1

    #Reset trial counter
    trialCount=0

#Calculate the probability of all target success
for i in range (len(allResult)):
    allResult[i]=allResult[i]/(N)

#Calculate Expectation
E=0 #Expectation
for i in range (len(allResult)):
    E=E+(allResult[i]*i)

#Print Results  
print("The probablity of getting %.f success out of %.f trials is %.4f%%" %(x,n,(runCount/N*100)))
print("The expectation is %.4f" %(E))


        