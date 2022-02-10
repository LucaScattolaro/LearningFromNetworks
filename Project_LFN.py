from cmath import log
import numpy as np
import networkx as nx
import matplotlib.pyplot as plt
import glob
import pandas as pd
import graphLibrary as gl
import time
import csv
import collections
import scipy
import time
import math


########       CREATION OF THE GRAPH
twitchGraph = nx.Graph()
#twitchNodes = pd.read_csv('twitch_gamers/large_twitch_features.csv')
twitchEdges = pd.read_csv('twitch_gamers/large_twitch_edges.csv')
twitchGraph = nx.from_pandas_edgelist(twitchEdges, 'numeric_id_1', 'numeric_id_2')


Graph_test=nx.Graph()
Graph_test.add_nodes_from([0, 1, 2, 3, 4, 5, 6])
Graph_test.add_edges_from([(0, 1),(0,3),(1, 2), (1, 3), (2, 4), (3, 4), (3, 5), (4, 6), (5, 6)])
G=Graph_test
















########       MENU'
print('What do you want to compute?:\n   0- Drawing Graph\n   1- Centralities\n   2- Clustering Coefficients   \n   3- Motifs (ESU)')
value = input()


########       DRAWING GRAPH
pos = nx.spring_layout(G, seed=675)
gl.drawGraph(G,pos)






########       CENTRALITIES
###            Betweeness Centrality
print("Betweeness Centrality")
betw_exact=nx.betweenness_centrality(G)
print(betw_exact)
#gl.saveDictionaryCSV('test_exact_Between.csv',betw_exact,['node', 'value'],order=True)

###            Approximate Betweeness
print("\n\nStarting computing betweeness Centrality...")
betw_approximate = gl.approximated_betweenness_centrality(G, 0.01)
print(betw_approximate)
#gl.saveDictionaryCSV('test_approximated_betweenness_results.csv', betw_approximate, ['node', 'betweenness centrality'], order=True)


gl.draw(G, pos, betw_exact, 'EXACT Betweenness Centrality')
gl.draw(G, pos, betw_approximate, 'APPROXIMATE Betweenness Centrality')



###            Closeness Centrality
print("\n\nCloseness Centrality")
clos_exact=nx.closeness_centrality(G)
print(clos_exact)
#gl.saveDictionaryCSV('test_exact_Close.csv',clos_exact,['node', 'value'],order=True)

###            Approximate Closeness
print("\n\nStarting computing closeness centrality...")
print('choose K (number of iterations)\nFor good approximation (with epsilon = 0.1) choose  k=',(math.log10(len(list(G.nodes)))/0.01))
k = input()
clos_approximate = gl.approximated_closeness_centrality(G,int(k))
print(clos_approximate)
#gl.saveDictionaryCSV('test_approximated_betweenness_results.csv', clos_approximate, ['node', 'betweenness centrality'], order=True)


gl.draw(G, pos, clos_exact, 'EXACT Closeness Centrality')
gl.draw(G, pos, clos_approximate, 'APPROXIMATE Closeness Centrality')





########       CLUSTERING COEFFICIENTS

###            Local Clustering Coefficient

print('\n\nLocal Clustering Coefficient')
lccs_exact=gl.LCCs(G)
print(lccs_exact)
# gl.saveDictionaryCSV('exact_localClusteringCoefficients.csv',lccs_exact,['node', 'local_CC'],order=True)


###            Approximate Local Clustering Coefficient
print('\n\nApproximate Local Clustering Coefficient')
k=int(len(list(G.nodes))/2)
estimateLccs=gl.EstimateLCCs(G,k)
print(estimateLccs)
# gl.saveDictionaryCSV('ApproxLCC_k'+str(k)+'.csv',estimateLccs,['node', 'Approx_local_CC'],order=True)


gl.draw(G, pos, lccs_exact, 'EXACT Local Clustering Coefficients')
gl.draw(G, pos, estimateLccs, 'APPROXIMATE Local Clustering Coefficients')



###            Global Clustering Coefficient
print('\nGlobal Clustering Coefficient')
num_triangle,cc=gl.globalClusteringCoefficient(G)
print('     Num Real Triangles= ',num_triangle/6)
print('     Clsutering Coeff= ',cc)

# number_of_triangles = sum(nx.triangles(G).values()) / 3
# print('NetwrokX:')
# print('     NumTriangles= ',number_of_triangles)
# print('     Clsutering Coeff= ',number_of_triangles/scipy.special.binom(len(list(G.nodes)), 3))




########        MOTIFS - ESU algorithm
print('\n\nMotifs')
motifs=gl.enumerateSubgraphs(G,2)
print(gl.countSubgraphs(motifs))


