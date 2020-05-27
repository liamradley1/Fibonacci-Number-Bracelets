# -*- coding: utf-8 -*-
"""
Created on Mon May 11 09:39:06 2020

@author: Liam
"""
import random

# Given a pair of numbers, num1 & num2, and a maximum number 
# that can appear in the bracelet, returns a Fibonacci 
# number bracelet that stops once a loop is reached.
def numberBracelet(num1, num2, maxNum):
    bracelet = [num1, num2]
    i=2
    first = num1
    second = num2
    fin = False
    while(fin == False):
        min2=bracelet[len(bracelet) - 2]
        min1=bracelet[len(bracelet) - 1]
        if(((min2 + min1)%(maxNum+1) == first) & ((min1 + first)%(maxNum+1)== second)):
            fin = True
        else: 
            i+=1
            newnum = (num1 + num2) % (maxNum+1)
            bracelet.append(newnum)
            num1=num2
            num2=newnum
    
    return bracelet

def countNumbers(maxNum):
    a=allBracelets(maxNum)
    count=0
    for bracelet in a:
        count+=len(bracelet)    
    return count

def allBracelets(maxNum):
    indicator = True
    braceletList=[]
    sortedBraceletList=[]

    for i in range(0,maxNum):
        for j in range(0,maxNum):
            indicator = True
            bracelet=numberBracelet(i,j,maxNum)
            sortedBracelet=sorted(bracelet)

            for bracelet1 in sortedBraceletList:
                if(indicator == True):
                    if (sortedBracelet == bracelet1):
                        indicator = False
                        
            if(indicator == True):
                braceletList.append(bracelet)
                sortedBraceletList.append(sortedBracelet)
            for bracelet in braceletList:
                if str(bracelet) == str([0,0]):
                    bracelet.pop()
                    
    return braceletList

def allBraceletsTest():
    maxNum=random.randint(1,25)
    assert(int(countNumbers(maxNum))==int((maxNum+1)*(maxNum+1)))


def main():
    maxNum=9
    print(allBracelets(maxNum))
    print(countNumbers(maxNum))

main()