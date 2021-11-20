import numpy as np
import networkx as nx
import matplotlib.pyplot as plt
import glob
import pandas as pd
import graphLibrary
import time
import csv
import collections


########       CREATION OF THE GRAPH
twitchGraph = nx.Graph()
#--Nodes
#twitchNodes = pd.read_csv('twitch_gamers/large_twitch_features.csv')
#--Edges
twitchEdges = pd.read_csv('twitch_gamers/large_twitch_edges.csv')
#--Creation of the Graph
twitchGraph = nx.from_pandas_edgelist(twitchEdges, 'numeric_id_1', 'numeric_id_2')



###graphLibrary.EstimateLCCs(twitchGraph,1)

########       LOCAL CLUSTERING COEFFICIENT FOR ALL NODES
#--Compute local clustering coefficient and save it into a Dictionary in order to save it later
# start=time.time()
# nodeLCC_dictionary={}
# i=0
# for node in list(twitchGraph.nodes):
#     start=time.time()
#     deg_v,lcc_v=graphLibrary.LCC(twitchGraph,node)
#     nodeLCC_dictionary[node]={'degree':deg_v,'local_CC':lcc_v}
#     print('iteration: ',i,'    --->    time:  ',time.time()-start)
#     i=i+1


# print('Order Dictionary')
# nodeLCC_dictionaryOrdered=collections.OrderedDict(sorted(nodeLCC_dictionary.items()))

# #--Create the csv writer that will contain the data ragarding local clustering coefficients of all nodes

# print('Write Data of Dictionary')
# f = open('localClusteringCoefficients.csv', 'w')
# writer = csv.writer(f)
# #--Write the Header to the csv file
# writer.writerow(['node', 'degree','local_CC'])
# #--Write the Data of nodes to the csv file
# for k, v in nodeLCC_dictionaryOrdered.items(): 
#     writer.writerow([k, v['degree'],v['local_CC']])

# #--Close the file
# f.close()

### ESU algorithm

#motifs=graphLibrary.enumerateSubgraphs(twitchGraph,2)

#print(graphLibrary.countSubgraphs(motifs))