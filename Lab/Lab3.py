# -*- coding: utf-8 -*-

# Below are fixed values for the generator formula.
N=10000 #norm
A=4857 #adder
M=8601 #multiplier
a=0
S=int(input("Enter a nonnegative integer for the seed."))

k=int(input("Enter the number of random numbers you want."))

for i in range(k):
    S=(M*S+A)%N
    r=S/N #Random numbers on [0.1)
    print(format ('%.4f'%r))
    
    a+=r
    
average=a/k