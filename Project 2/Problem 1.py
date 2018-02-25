"""
@title Project 2
@author Sotheanith Sok

This is the project 2 for EE 381 Spring 2018

Note: This project is heavily helped by Professor John De Sulima-Przyborowski at California
State University of Long Beach for EE381

"""

"""
Problem 1:
You will write a Python program to simulate Bernoulli trials. This in turn will be used to simulate a
random coin toss of a coin with a specified probability of heads (success).
As discussed in seminar a Bernoulli trial is a random experiment with exactly two possible outcomes
usually termed success and failure. The probability of success is the same every time the experiment is
conducted. Use the pseudorandom number generator available in Python to generate the random
numbers.
Computer Program Specifications
The user should input the probability of success or equivalently the probability of heads.
The user should input the number of trials to simulate.
The output should be a random stream of “success” and “failure” statements or equivalently heads and
tails.
"""
#Import function
import random

#Get user input
n=int(input("How many trial you want to do?\n"))
p=float(input("What is the probability(%) of getting head?\n"))

#Internal values
head=0
tail=0

#Start trial
for i in range(n):
    rand=random.uniform(0,1)
    if(rand<(p/100.0)):
        head=head+1
        print("success")
    else:
        tail=tail+1
        print("failure")

#Final result
print("Probability of head: %.2f%%. \nProbability of tail %.2f%%."%(head/n*100,tail/n*100))

