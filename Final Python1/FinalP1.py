import numpy as np
#   from random import shuffle
import random

nodes=int(input())
prob=float(input())

def GMLGeneratoer(numOfNodes, prob):

    numOf1s = round((numOfNodes*(numOfNodes-1)/2)*prob)
    numOf0s = (numOfNodes*(numOfNodes-1)/2) - numOf1s

    listOf1s = np.ones((numOf1s,), dtype=np.int)
    listOf0s = np.zeros((numOf0s,), dtype=np.int)

    randomList = []
    randomList.extend(listOf0s)
    randomList.extend(listOf1s)
    random.shuffle(randomList)

    gmlData = open('gmlFile.gml', 'w')

    arr = np.zeros(shape=(numOfNodes,numOfNodes), dtype=np.int32)
    k = 0
    gmlData.write('<?xml version="1.0" encoding="UTF-8"?>\n')
    gmlData.write('<graphml xmlns="http://graphml.graphdrawing.org/xmlns"\n')
    gmlData.write('\txmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"\n')
    gmlData.write('\txsi:schemaLocation="http://graphml.graphdrawing.org/xmlns\n')
    gmlData.write('\t\thttp://graphml.graphdrawing.org/xmlns/1.0/graphml.xsd">\n')

    gmlData.write('<graph id = "G" edgedefault = "undirected>'+'\n')
    for nodes in range(0,numOfNodes):
        gmlData.write('\t<node id=\"'+str(nodes + 1)+'\"/>\n')
    for i in range(0, numOfNodes):
        for j in range(i+1,numOfNodes):
            if randomList[k]==1:
                gmlData.write('\t<edge source=\"'+str(i + 1)+'\" target=\"'+str(j + 1)+'\"/>\n')
            k+=1
    gmlData.write('</graph>\n')
    gmlData.write('</graphml>')


GMLGeneratoer(nodes, prob)