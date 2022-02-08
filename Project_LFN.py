import numpy as np
import networkx as nx
import matplotlib.pyplot as plt
import glob
import pandas as pd
import graphLibrary
import time
import csv
import collections
import scipy
import time


########       CREATION OF THE GRAPH
twitchGraph = nx.Graph()
#--Nodes
twitchNodes = pd.read_csv('twitch_gamers/large_twitch_features.csv')
#--Edges
#print(len(twitchNodes))
twitchEdges = pd.read_csv('twitch_gamers/large_twitch_edges.csv')
#print(len(twitchEdges))
#--Final Graph
twitchGraph = nx.from_pandas_edgelist(twitchEdges, 'numeric_id_1', 'numeric_id_2')


########       DRAWING GRAPH

# pos = nx.spring_layout(twitchGraph, seed=675)
# graphLibrary.drawGraph(twitchGraph,pos)






########       CENTRALITIES
###            Betweeness Centrality
# b=nx.betweenness_centrality(twitchGraph)
# graphLibrary.saveDictionaryCSV('ResultsCentralities/testBetween.csv',b,['node', 'value'],order=True)

print("Start")
start=time.time()
###            Closeness Centrality
c=nx.closeness_centrality(twitchGraph)
graphLibrary.saveDictionaryCSV('ResultsCentralities/testClose.csv',c,['node', 'value'],order=True)
print('Time: ',time.time()-start)



########       CLUSTERING COEFFICIENTS

###            Local Clustering Coefficient
# lccs=graphLibrary.LCCs(twitchGraph)
# graphLibrary.saveDictionaryCSV('localClusteringCoefficients__.csv',lccs,['node', 'local_CC'],order=True)


###            Approximate Local Clustering Coefficient
# k=1000
# start=time.time()
# estimateLccs=graphLibrary.EstimateLCCs(twitchGraph,k)
# line='Estimation lccs k:'+str(k)+'  --->  '+str(time.time()-start)
# graphLibrary.saveTime('ComputationalTimes.info', line)
# graphLibrary.saveDictionaryCSV('ApproxLCC_k'+str(k)+'.csv',estimateLccs,['node', 'Approx_local_CC'],order=True)


###            Global Clustering Coefficient
# num_triangle,cc=graphLibrary.globalClusteringCoefficient(twitchGraph)
# print('mine:')
# print('     NumTriangles= ',num_t)
# print('     Num Real Triangles= ',num_t/6)
# print('     Clsutering Coeff= ',cc)

# number_of_triangles = sum(nx.triangles(twitchGraph).values()) / 3
# print('NetwrokX:')
# print('     NumTriangles= ',number_of_triangles)
# print('     Clsutering Coeff= ',number_of_triangles/scipy.special.binom(len(list(twitchGraph.nodes)), 3))






########        MOTIFS - ESU algorithm

# motifs=graphLibrary.enumerateSubgraphs(twitchGraph,2)
# print(graphLibrary.countSubgraphs(motifs))
# 
#motifs=graphLibrary.enumerateSubgraphs(twitchGraph,2)

#print(graphLibrary.countSubgraphs(motifs))

#nodes=list(twitchGraph.nodes)
#n=len(nodes)

#m=len(twitchEdges)

#file= open("graph.txt", "w")

#file.write(str(n)+" "+str(m))

#for node in nodes:
    #neighbors_v = list(twitchGraph.neighbors(node))
    #for u in neighbors_v:
        #file.write("\n"+str(node)+" "+str(u))

#file.close()

