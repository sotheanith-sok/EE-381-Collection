"""
@title Project 3
@author Sotheanith Sok

This is the project 3 for EE 381 Spring 2018

Note: This project is heavily helped by Professor John De Sulima-Przyborowski at California
State University of Long Beach for EE381

"""
"""
Problem 1:
Let us consider a simple binomial distribution experiment. Let there be five trials. In each trial the probability of success
is 0.7. What is the probability of exactly three successes?

Write a Python program to simulate the specific problem above. In this program import and use the
Python random number generator. You, arguably, need to consider the finite number of Bernoulli trials in the problem
and the number of successes in the finite number of Bernoulli trials.
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
    #Reset trial counter
    trialCount=0

#Print result
print("The probability of getting %.f success out of %.f trials is %.10f%%" %(x,n,(runCount/N*100)))


        