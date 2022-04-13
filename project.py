#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Delaney Dow & Marlee Feltham
EC552 Spring 22 Final Project
"""
import csv 
import os 


#################### DATA PARSE #####################
#create graph function 
def createAsmGraph(part, hashMem): 
    if part in hashMem.values():
        return hashMem.values(part)
    #base case 
    #if ((len(part)) = 1): 
        

#combine graphs function 

#min cost graph function 

#################### MAIN ###########################
def main(): 
    fileList = []
    # get input from csv, send to parser  
    fileName = open('dataset.csv')
    file = csv.reader(fileName)
    for rows in file:   
        #print(rows)
        fileList.append(rows)
    print(fileList) 
   
    
    hashMem = {} #empty hashMem dictionary 
    part = 'a'
    
    createAsmGraph(part, hashMem)
    
    
    
    
if __name__ == '__main__': 
    main()     

