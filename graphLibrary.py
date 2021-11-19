from networkx.classes.function import neighbors
import numpy as np
import networkx as nx
import matplotlib.pyplot as plt
import glob
import pandas as pd
import random


#########        Clustering Coefficient Methods

def LCC(G,v):
    #--Calculate the exact local clustering coefficient of a node v of grapgh G
    num_t=0
    neighbors_v=list(G.neighbors(v))
    for u1 in neighbors_v:
        for u2 in neighbors_v:
            if u1!=u2 and G.has_edge(u1,u2):
                num_t=num_t+1
    
    deg_v=len(neighbors_v)

    return deg_v, num_t/(deg_v*(deg_v-1))

def LCCs(G):
    #--Calculate the exact local clustering coefficient for all the nodes of grapgh G
    ccs={}
    for node in list(G.nodes):
        deg, cc=LCC(G,node)
        ccs[node]={'degree':deg, 'localCC':cc}
    return ccs

def EstimateLCCs(G,k):
    #--Calculate the approximate local clustering coefficient for all the nodes of graph G
    edges=list(G.edges())
    nodes=list(G.nodes)
    Z={}
    i=0
    for edge in edges:
        Z[frozenset(edge)]=0
        i=i+1
        if i==10:
            break

    V=list(range(0, G.number_of_nodes()))
    for i in range(k):
        random.shuffle(V)
        min_v={}
        for node in nodes:
            print('Node: ',node)
            neighbors=list(G.neighbors(node))
            min_v[node]=min([V[x] for x in neighbors]) 

        for edge in edges:
            if min_v[edge[0]]==min_v[edge[0]]:
                Z[frozenset(edge)]=Z[frozenset(edge)]+1

    ccs={}
    for node in nodes:
        neighbors_v=list(G.neighbors(node))
        num_neigh=len(neighbors_v)

        sum=0
        for u in neighbors_v:
            sum=sum+((Z[frozenset(u,node)]/(Z[frozenset(u,node)]+k))*(num_neigh+G.neighbors(u)))
        
        ccs[node]=(0.5*sum)/(num_neigh*(num_neigh-1))

    return ccs





    




def globalClusteringCoefficient():
    print('global Clustering Coefficient')