from networkx.classes.function import neighbors
import numpy as np
import networkx as nx
import matplotlib.pyplot as plt
import glob
import pandas as pd



def LCC(G,v):
    num_t=0
    neighbors_v=list(G.neighbors(v))
    for u1 in neighbors_v:
        for u2 in neighbors_v:
            if u1!=u2 and G.has_edge(u1,u2):
                num_t=num_t+1

    deg_v=len(neighbors_v)
    #print('deg_v: ',deg_v)
    return deg_v, num_t/(deg_v*(deg_v-1))

def globalClusteringCoefficient():
    print('global Clustering Coefficient')