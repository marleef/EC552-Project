#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Delaney Dow & Marlee Feltham
EC552 Spring 22 Final Project
"""
import csv
from logging import StringTemplateStyle
import os
import copy
import random


#################### DATA PARSE #####################
# create graph function
def createAsmGraph(part, hashMem):
    # (1) memoization case
    if part in hashMem.values():
        return hashMem.values(part)
    if (len(part) == 1):
        return part  # return new graph with given part

    # graph framework:
    graph = {'stages': '', 'steps': '', 'sharing': ''}
    graphBest = graph #create best graph to be null 

    for i in range(len(part)):
        subpartL = part.split("." ) #split according to "." denoter
        subpartR = part.split(i, len(part))
        # recursive, calls subpart as new part
        graphL = createAsmGraph(subpartL, hashMem)
        # recursive, calls subpart as new part
        graphR = createAsmGraph(subpartR, hashMem)

        graphNew = combineGraphs(graphL, graphR)  # combine L/R into new graph
        graphBest = minCost(graphNew, graphBest)

    hashMem.insert(part, graphBest)  # part is key, graphBest is value
    return graphBest


def combineGraphs(graphL, graphR):
    """USING DUMMY OUTPUTS FOR NOW"""
    # Return graph created from combining two child graphs
    graphNew = copy.deepcopy(graphL)  # make a copy of graphL
    graphNew.update(graphR)  # add graphR to graphNew (merges)

    # Calculate the cost of new graph
    graphNew['stages'] = max(graphL['stages'], graphR['stages']) + 1
    graphNew['steps'] = graphL['steps'] + graphR['steps'] + 1

    return graphNew

# min cost graph function


def minCost(graph0, graph1):
    """USING DUMMY OUTPUT FOR NOW"""
    if graph0['stages'] < graph1['stages']:
        return graph0
    if graph1['stages'] < graph0['stages']:
        return graph1

    # If number of stages equal, then graph with less steps is lower cost
    if graph0['steps'] < graph1['steps']:
        return graph0
    if graph1['steps'] < graph0['steps']:
        return graph1

    # Graphs have identical cost so arbitrarily choose one
    g = [graph0, graph1]
    return random.choice(g)

def maxCost(graph0, graph1): 
    #start by choosing maximum number of stages
    if graph0['stages'] > graph1['stages']:
        return graph0
    if graph1['stages'] > graph0['stages']:
        return graph1

    # If number of stages equal, then graph with more steps is of higher cost
    if graph0['steps'] > graph1['steps']:
        return graph0
    if graph1['steps'] > graph0['steps']:
        return graph1

    # Graphs have identical cost so arbitrarily choose one
    g = [graph0, graph1]
    return random.choice(g)

#################### MAIN ###########################


def main():
    fileList = []
    # get input from csv, send to parser
    fileName = open('dataset.csv')
    file = csv.reader(fileName)
    for rows in file:
        # print(rows)
        fileList.append(rows)
    # print(fileList)

    hashMem = {}  # empty hashMem dictionary
    part = 'a.b.c.d.'

    graphOut = createAsmGraph(part, hashMem)
    print(graphOut)


if __name__ == '__main__':
    main()
