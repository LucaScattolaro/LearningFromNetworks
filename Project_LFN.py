import numpy as np
import networkx as nx
import matplotlib.pyplot as plt
import glob
import pandas as pd

twitchGraph = nx.Graph()
#--Nodes
twitchNodes = pd.read_csv('twitch_gamers/large_twitch_features.csv')
print(twitchNodes)

#--Edges
twitchEdges = pd.read_csv('twitch_gamers/large_twitch_edges.csv')
print(twitchEdges)
