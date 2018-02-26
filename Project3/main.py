"""
@Title: Simulation of a binomial random varaible

This simulation will use the sum of Bernoulli r.v.'s to 
simluate the binomial r.v.

"""
import random

n=5 #The number of trial
x=3 #the number of successes 
p=0.7 #the probability of succeess for an outcome

N=10000 #The number of time the process is repeated

trial=[0]
trial = trial*n #an empty trial list

j=0 #accumulator initialized 

E=0 #accumulator for the average

for k in range (N): #outside loop
    for i in range(n): #inner loop, the individual experiment 
        
        # Generation of Bernoulli r.v
        
        r=random.uniform(0,1)
        
        if r<p:
            trial[i]=1 #success
        else:
            trial[i]=0 #failure
            
    s=sum(trial) #counts the number of successes
    E=E+s
    if s==x:
        j=j+1 #counts the number of trails with the desired successes 
print(j/N)
print('Average:',(E/N))
