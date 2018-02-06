#Probability Problem
#Three ball in five cans at random
#Each ball in a different can

import math

#Random number generator formula values

N=10000 #norm
A=4857 #adder
M=8601 #multiplier
S=0 #seed

Sum=0 #initialize counter
trial =0 #number of trails

Can=[0,0,0]

K=int(input("Enter the number of expereiments"))

for k in range(K):
    S=(M*S+A)%N
    r=S/N #Random numbers on [0,1)
    
    Can_Number=math.floor