# -*- coding: utf-8 -*-
#Tutorial on determining summary statistic using Python. 

numbers = []

#User inputs data
while True:
    try:
        n= int (input("To stop enter the letter x. \nEnter a number:"))
        numbers.append(n)
    except ValueError:
        break

#Mean calculation
s = sum(numbers)
N = len(numbers)
#Calculate the mean.
mean = s/N
print("The mean of the numbers you entered is ", mean)

#Calculate the median.
numbers.sort()

if N%2==0:
    mone=int(N/2)-1
    mtwo=int(N/2)
    median=(numbers[mone]+numbers[mtwo])/2
else:
    median=numbers[int(N/2)]
print("The median of the number you entered is", median)

#Calculate the mode.
from collections import Counter

c=Counter(numbers)
mode = c.most_common()
if mode[0][1]>1:
    print ("The mode of the data you entered is",mode[m][0] for m in range(len(mode)))
else:
    print("There is no mode for the data you entered")
#print("The mode of the data you entered is", m)
    
#Calculate the standard deviation.
import math
a=0

for x in number:
    y=(x-mean)**2
    a=a+y
sigma = math.sqrt(a/N)

print("The stand deviation is", sigma )