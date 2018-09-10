"""
@title Project 4
@author Sotheanith Sok

This is the project 4 for EE 381 Spring 2018

Note: This project is heavily helped by Professor John De Sulima-Przyborowski at California
State University of Long Beach for EE381

"""

#Imports
import math
import matplotlib.pyplot as plt
import numpy as np



"""
Part 1: Plot a binominal distribution for n=18 and p=0.5 
"""
#Variable
n=18 #number of possible X
p=0.5 #success probability

#Store probability for all possbile X
bdData=[0]*(n+1)

for i in range (n+1):
    #Calculate combination
    c=math.factorial(n)/math.factorial(i)/math.factorial(n-i)
    #Caclcule probability
    bdData[i]= c*(p**i)*((1-p)**(n-i))

#Graph the binominal distribution
index = list(range(len(bdData)))
plt.bar(index, bdData)
plt.xlabel('X', fontsize=12)
plt.xticks(index)
plt.ylabel('Probability', fontsize=12)
plt.title('Binominal Distribution n=18 and p=0.5', fontsize=15)
plt.show()    



"""
Part 2: Find the critical value closed to 0.05

"""
#Store the sum of all probability
cvData=[0]*(n+1)

#Calculate the sum of all probablity for X>i for i from 0 to n
for i in range (n+1):   
    cvData[i]=np.sum(bdData[i:len(bdData)])
    
#Find the closest critical value to 0.05
difference=100
index=-1
for i in range(len(cvData)):
    temp=abs(cvData[i]-0.05)
    if(temp<difference):
        index=i
        difference=temp
#Print Result
print("The critical value is",index,"\n\n\n")
    
print(cvData)

"""
Part 3: Find beta error for p̃ from 0.5 to 1 incrased by 0.05
 
"""
#Varaibles
p=np.arange(0.50,1.05,0.05) #List of all possible p̃
betaErrorData=[0]*len(p) #Storage for all β
cv=index #The critical value from part 2

#Loop through all p̃
for i in range(len(p)):
    #Calculate β for p̃ for X from 0 to C.V-1 
    addition=0
    for j in range(cv-1+1):
        c=math.factorial(n)/math.factorial(j)/math.factorial(n-j)
        temp=c*(p[i]**j)*((1-p[i])**(n-j))
        addition=addition+temp
    betaErrorData[i]=addition
    #Print Results
    print("Beta Error(β) of p̃ =",p[i].round(2),"is",betaErrorData[i].round(4))
#Plot the result on to a graph.
plt.plot(p,betaErrorData) 
plt.xticks(p)
plt.ylabel('Beta Error(β)', fontsize=12)
plt.xlabel("Probability (p̃)", fontsize=12)
plt.title("Beta Error vs Probability", fontsize=15)
plt.show()



"""
Part 4: Create binominal distribution graphs for all p̃ from 0.5 to 1 increased by 0.05
"""
for j in range(len(p)):
    for i in range (n+1):
        #Calculate combination
        c=math.factorial(n)/math.factorial(i)/math.factorial(n-i)
        #Caclulate the probablity     
        bdData[i]= c*(p[j]**i)*((1-p[j])**(n-i))
    index = list(range(len(bdData)))
    #Graph the result
    plt.bar(index, bdData)
    plt.xlabel('X', fontsize=12)
    plt.xticks(index)
    plt.ylabel('Probability', fontsize=12)
    s="Binominal Distribution for n=18 and p̃="+str(p[j].round(2))
    plt.title(s, fontsize=15)
    plt.show()   



"""
Part 5: Create a power curve a.k.a 1-β vs p̃
"""   
#Perform summation
power=[1-i for i in betaErrorData]
#Graph
plt.plot(p,power) 
plt.xticks(p)
plt.ylabel('1-β', fontsize=12)
plt.xlabel("p̃", fontsize=12)
plt.title("The Power Curve", fontsize=15)
plt.show()