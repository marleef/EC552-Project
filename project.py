#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Delaney Dow & Marlee Feltham
EC552 Spring 22 Final Project
"""
import csv
from logging import StringTemplateStyle
import os


#################### DATA PARSE #####################
# create graph function
def createAsmGraph(part, hashMem):
    # (1) memoization case
    if part in hashMem.values():
        return hashMem.values(part)
    if (len(part) == 1): 
        return part #return new graph with given part

    # graph framework:
    graph = {'stages': '', 'steps': '', 'sharing': ''}

    for i in range(len(part)): 
        subpartL = part.split(0,i)
        subpartR = part.split(i, len(part))
        graphL = createAsmGraph(subpartL, hashMem) #recursive, calls subpart as new part
        graphR = createAsmGraph(subpartR, hashMem) #recursive, calls subpart as new part 
        
        graphNew = combineGraphs(graphL, graphR) #combine L/R into new graph 
        graphBest = minCost(graphNew, graphBest)

    hashMem.insert(part, graphBest) #part is key, graphBest is value
    return graphBest   

    # (2) base case
    # if (len(part)) == 1:
    # construct graph?
    #   graph_new = graph.copy()
    #   graph_new['stages'] =
    #   graph_new['steps'] =
    #   graph_new = ['sharing'] =
    # return graph_new

    # (3) recursive step: iteratively partition part and recurse
    #    find best graph for left and right partitions
    #   combine left and right graphs into new graph for intermediate part
    #   if cost of new graph is the best so far save the geaph
    #
    # (4) add best graph to hash table and return

# combine graphs function
def combineGraphs(graphL, graphR):
    """USING DUMMY OUTPUTS FOR NOW"""
    graphNew = graphL 
    return graphNew 
    # (1) return graph created from combining two child graphs

    # (2) calculate cost of new graph


# min cost graph function
def minCost(graph0, graph1):
     """USING DUMMY OUTPUT FOR NOW"""
     return graph0

    # (1) num of stages always take priority -> change ?
    # (2) if num of stages = then graph w/ less steps is lower cost
    # (3) graphs have identical cost so arbitrarily choose one


#################### MAIN ###########################


def main():
    fileList = []
    # get input from csv, send to parser
    fileName = open('dataset.csv')
    file = csv.reader(fileName)
    for rows in file:
        # print(rows)
        fileList.append(rows)
    #print(fileList)

    hashMem = {}  # empty hashMem dictionary
    part = 'a'

    graphOut = createAsmGraph(part, hashMem)
    print(graphOut) 


if __name__ == '__main__':
    main()
