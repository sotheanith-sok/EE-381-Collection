"""
@title Project 3
@author Sotheanith Sok

This is the project 3 for EE 381 Spring 2018

Note: This project is heavily helped by Professor John De Sulima-Przyborowski at California
State University of Long Beach for EE381

"""
"""
Problem 2:
Finally generalize your previous results. Write a program in Python using the frequency simulation approach meeting
the following requirements. The user can input the probability of success. The user can enter the number of trials. The
user can input a range of values for the number of successes (for instance 50 ≤ 𝑋 ≤ 742). Your program should output
the probability of the number of success inputted and the average of the r.v. Your program should be able to print a bar
chart of the distribution when requested by the use
"""
#imports
import random
import matplotlib.pyplot as plt
import numpy as np

#Variables
p=0 #Probability of success
n=0 #Number of trials per run.
N=10000000000 #Number of run
x=0 #Initial target of success
y=0 #Final target of success

#Counters
count=0

#Stored Result
allResult=[0]*(n+1)

#Call this method to obtain new data.
def enterNewData():
    global p,x,n,y

    try:
        p=float(input("Probabillity of success: "))
        n=int(input("Number of trials: "))
        x=int(input("Initail range of success: "))
        y=int(input("Final range of success: "))
    except ValueError:
        print("Invalid Input. Return to menu.")
        return
    calculation()
    return

#Call this method to run the simulation 
def calculation():
    global p,n,x,y,count,allResult
    allResult=[0]*(n+1)
    #Loop for run
    for i in range(N): 
        
        #Loop for trial
        for j in range(n):
            result=random.uniform(0,1)
            
        #if success, add one to trial counter
            if(result<p):
                count=count+1
                
        
        #Store the result
        allResult[count]=allResult[count]+1
    
        #Reset trial counter
        count=0
    for i in range (len(allResult)):
        allResult[i]=allResult[i]/(N)
    return

#Print the result of the simulation
def printResult():
    E=0
    for i in range (len(allResult)):
        E=E+(allResult[i]*i)
    print('The result is: (Target:Probability)')
    print (dict(zip(range(x,y+1),allResult)))
    print("The expectation is %.4f" %(E))
    return

#Print the distribution as a graph
def printGraph():
    index = np.arange(len(allResult))
    plt.bar(index, allResult)
    plt.xlabel('Number of Success', fontsize=12)
    plt.ylabel('Probability', fontsize=12)
    plt.title('Probability vs Number of Success')
    plt.show()
    return

#Main menu
def menu():
    while True:
        enter=-1
        print ("\n-Menu")
        print ("1. Enter new data")
        print ("2. Print result of the last trial")
        print ("3. Print a bar chart of the distribution of the last trial.")
        print ("4. Exit")
        try:
            enter=int(input("Input:"))
        except ValueError:
            print("Invalid Input. Please try again.")
            continue
        
        if (enter<1 or enter>4):
            print("Invalid Input. Please try again.")
            continue
        else:
            return enter;

#Starting point of the program.
def main():
    while True:  
        var=menu()
        if(var==1):
            enterNewData()
        elif (var==2):
            printResult()
        elif (var==3):
            printGraph()
        elif (var==4):
            break
        
#Invoke main at the start of the program  
main()

