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


########       CREATION OF THE GRAPH
twitchGraph = nx.Graph()
#--Nodes
#twitchNodes = pd.read_csv('twitch_gamers/large_twitch_features.csv')
#--Edges
twitchEdges = pd.read_csv('twitch_gamers/large_twitch_edges.csv')
#--Final Graph
twitchGraph = nx.from_pandas_edgelist(twitchEdges, 'numeric_id_1', 'numeric_id_2')




########       DRAWING GRAPH
# pos = nx.spring_layout(twitchGraph, seed=675)
# graphLibrary.drawGraph(twitchGraph,pos)




########       CLUSTERING COEFFICIENTS
###            Local Clustering Coefficient
# lccs=graphLibrary.LCCs(twitchGraph)
# graphLibrary.saveDictionaryCSV('localClusteringCoefficients.csv',lccs,['node', 'local_CC'],order=True)


###            Approximate Local Clustering Coefficient
k=10
estimateLccs=graphLibrary.EstimateLCCs(twitchGraph,k)
graphLibrary.saveDictionaryCSV('ApproxLCC_k'+str(k)+'.csv',estimateLccs,['node', 'Approx_local_CC'],order=True)


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

motifs=graphLibrary.enumerateSubgraphs(twitchGraph,2)
print(graphLibrary.countSubgraphs(motifs))