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
    part = part.replace(".", "")

    graphBest = copy.deepcopy(graph)
    graphBest['stages'] = 500
    graphBest['steps'] = 500

    for i in range(len(part)):
        subpartL = part[0:i]
        subpartR = part[i:len(part)]
        print(subpartL, subpartR)
        # graphL = createAsmGraph(subpartL, hashMem)
        # graphR = createAsmGraph(subpartR, hashMem)
        # graphNew = combineGraphs(graphL, graphR)
        # graphBest = minCost(graphNew, graphBest)

    # hashMem['part'] = graphBest
    # print(graphBest)
    # return graphBest


def combineGraphs(graphL, graphR):
    """USING DUMMY OUTPUTS FOR NOW"""
    # Return graph created from combining two child graphs
    graphNew = {**graphL, **graphR}
    print('graphL: ', graphL, 'graphR: ', graphR)

    # Calculate the cost of new graph
    # graphNew['stages'] = max(graphL['stages'], graphR['stages']) + 1
    # graphNew['steps'] = graphL['steps'] + graphR['steps'] + 1

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
    part = 'a.b.c.d'

    graphOut = createAsmGraph(part, hashMem)
    # print(graphOut)


if __name__ == '__main__':
    main()
