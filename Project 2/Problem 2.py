"""
@title Project 2
@author Sotheanith Sok

This is the project 2 for EE 381 Spring 2018

Note: This project is heavily helped by Professor John De Sulima-Przyborowski at California
State University of Long Beach for EE381

"""

"""
Problem 2:
You will write a Python program to calculate Bayes’ probabilities.
Consider a rare disease. Let 𝐶 be the probability of having the disease. Let 𝐵 be the event that the
diagnostic procedure indicates the disease is present. Consider the following probabilities:
P(C):
    0.0001
    0.001
    0.001
    0.0001  
    0.001
P(B|C):
    0.9
    0.9
    0.9
    0.95
    0.95
P(B|C'):
    0.001
    0.001
    0.01
    0.001
    0.01
P(C|B):?

"""
#Define variables

A=[0.0001,0.001, 0.001, 0.0001, 0.001] #P(C)
B=[0.9, 0.9, 0.9, 0.95, 0.95] #P(B|C)
C=[0.001, 0.001, 0.01, 0.001, 0.01,] #P(B|C')
D=[0]*len(A) #P(C|B)

for i in range (len(A)):
    D[i]=(A[i]*B[i])/(B[i]+C[i])
    print("P(C): {0:<8g} P(B|C): {1:<8g} P(B|C'): {2:<8g} P(C|B): {3:<8g}".
          format(+A[i], B[i], C[i], D[i]))
