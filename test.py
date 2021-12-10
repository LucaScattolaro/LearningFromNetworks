import networkx as nx
import matplotlib.pyplot as plt
import matplotlib.colors as mcolors
import graphLibrary as graphLib
import time

def LCC(G,v):
    #--Calculate the exact local clustering coefficient of a node v of grapgh G
    num_t=0
    neighbors_v=list(G.neighbors(v))
    for u1 in neighbors_v:
        for u2 in neighbors_v:
            if u1!=u2 and G.has_edge(u1,u2):
                num_t=num_t+1
    
    deg_v=len(neighbors_v)
    if deg_v==1:
        return deg_v, num_t
    else:
        return deg_v, num_t/(deg_v*(deg_v-1))

def LCCs(G):
    #--Calculate the exact local clustering coefficient for all the nodes of grapgh G
    lccs={}
    for node in list(G.nodes):
        deg, lcc=LCC(G,node)
        lccs[node]=lcc
    return lccs

def draw(G, pos, measures, measure_name):
    nodes = nx.draw_networkx_nodes(G, pos, node_size=250, cmap=plt.cm.plasma,node_color=list(measures.values()),nodelist=measures.keys())
    nodes.set_norm(mcolors.SymLogNorm(linthresh=0.01, linscale=1, base=10))
    labels = nx.draw_networkx_labels(G, pos)
    edges = nx.draw_networkx_edges(G, pos)
    plt.title(measure_name)
    plt.colorbar(nodes)
    plt.axis('off')
    plt.show()

def drawGraph(G,pos):
    nodes = nx.draw_networkx_nodes(G, pos, node_size=250)
    nodes.set_norm(mcolors.SymLogNorm(linthresh=0.01, linscale=1, base=10))
    labels = nx.draw_networkx_labels(G, pos)
    edges = nx.draw_networkx_edges(G, pos)
    plt.title('Graph')
    plt.axis('off')
    plt.show()


G=nx.Graph()
G.add_nodes_from([1,2,3,4,5,6,7])
G.add_edges_from([(1, 2), (1, 3),(2, 3), (1, 4), (2, 4),(6,7),(5, 4),(6, 4)])



pos = nx.spring_layout(G, seed=675)


# drawGraph(G,pos)
# draw(G, pos, nx.degree_centrality(G), 'Degree Centrality')
start=time.time()
lccs=LCCs(G)
print('LCCS time: ',time.time()-start)

start2=time.time()
approxLccs=graphLib.EstimateLCCs(G,6)
k=1
line='Estimation lccs k:'+str(k)+'  --->  '+str(time.time()-start2)+'\n'
graphLib.saveTime('ComputationalTimes.info', line)
graphLib.saveDictionaryCSV('test.csv',approxLccs,['node', 'Approx_local_CC'],order=True)
print('approx LCCS time: ',time.time()-start2)



draw(G,pos,lccs,'Local Clustering Coeff')
draw(G,pos,approxLccs,'Estimate Local Clustering Coeff')
# draw(G, pos, nx.closeness_centrality(G), 'Closeness Centrality')
# draw(G, pos, nx.betweenness_centrality(G), 'Betweenness Centrality')