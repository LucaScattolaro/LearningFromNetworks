import networkx as nx
import pandas as pd
import random as rd
import math
import collections
import csv
from sys import maxsize
from collections import deque
from numpy.random import choice
import time


def saveDictionaryCSV(nameFile, dict, header, order):
    if order:
        print('Order Dictionary')
        dict = collections.OrderedDict(sorted(dict.items()))

    print('Write Data of Dictionary')
    f = open(nameFile, 'w')
    writer = csv.writer(f)
    # --Write the Header to the csv file
    writer.writerow(header)
    # --Write the Data of nodes to the csv file
    for k, v in dict.items():
        writer.writerow([k, v])
    # --Close the file
    f.close()


def add_edge(adj, src, dest):
    adj[src].append(dest)
    adj[dest].append(src)


def find_paths(paths, path, parent, n, u):
    # Base Case
    if u == -1:
        paths.append(path.copy())
        return

    # Loop for all the parents
    # of the given vertex
    for par in parent[u]:
        # Insert the current
        # vertex in path
        path.append(u)

        # Recursive call for its parent
        find_paths(paths, path, parent, n, par)

        # Remove the current vertex
        path.pop()


def bfs(adj, parent, n, start):
    # dist will contain shortest distance
    # from start to every other vertex
    dist = [maxsize for _ in range(n)]
    q = deque()

    # Insert source vertex in queue and make
    # its parent -1 and distance 0
    q.append(start)
    parent[start] = [-1]
    dist[start] = 0

    # Until Queue is empty
    while q:
        u = q[0]
        q.popleft()
        for v in adj[u]:
            if dist[v] > dist[u] + 1:

                # A shorter distance is found
                # So erase all the previous parents
                # and insert new parent u in parent[v]
                dist[v] = dist[u] + 1
                q.append(v)
                parent[v].clear()
                parent[v].append(u)

            elif dist[v] == dist[u] + 1:

                # Another candidate parent for
                # shortes path found
                parent[v].append(u)


def shortest_paths(adj, n, start, end):
    paths = []
    path = []
    parent = [[] for _ in range(n)]

    # Function call to bfs
    bfs(adj, parent, n, start)

    # Function call to find_paths
    find_paths(paths, path, parent, n, end)

    for v in paths:
        v.reverse()

    return paths


def number_shortest_paths(adj, n, start, end):
    return len(shortest_paths(adj, n, start, end))


def compute_vertex_diameter_approximation(G):
    # Sample one random node
    v = rd.sample(G.nodes, 1)

    # Compute all the shortest path lengths from the sampled node to every other
    # node and store them in a ordered dictionary
    paths = nx.single_source_shortest_path_length(G, v[0])

    # Since now we have a ordered dictionary with all the lengths of each shortest path,
    # to compute the approximation we just need to select the last two entries and sum them
    return list(paths.values())[-1] + list(paths.values())[-2]


def approximate_betweenness_centrality(G, epsilon, delta=0.1, c=0.5):
    """
    Approximated betweenness centrality implementation using the Riondato-Karnaropoulos algorithm (2016).

    :param G: weighted/unweighted graph
    :param epsilon: desired accuracy
    :param delta: used to select the desired confidence (which is expressed by 1-delta) for the accuracy; we set
                  delta=0.1 as in the paper
    :param c: constant (we set c=0.5 as in Löffler and Phillips, 2009)
    :return: dictionary containing the approximated betweenness centralities for each node
    """

    # Initialize variables
    n = len(list(G.nodes))
    vertex_diameter_approximation = compute_vertex_diameter_approximation(G)
    print("VD(G) = {}".format(vertex_diameter_approximation))
    r = int((c / epsilon ** 2) * (math.floor(math.log2(vertex_diameter_approximation - 2)) + math.log(1 / delta)))
    approximated_centralities = {}

    # Initialize with 0 the dictionaries containing the approximated betweenness
    # centralities for each node
    for node in list(G.nodes):
        approximated_centralities[node] = 0

    # Build adjacency list representation for the graph in order to compute shortest
    # paths between pair of nodes
    adj = [[] for _ in range(n)]
    for (u, v) in G.edges:
        add_edge(adj, u, v)

    # Loop for the number of iterations r
    print("r = {}".format(r))
    for i in range(0, r):
        start_time = time.time()
        print("-------- ITERAZIONE NUMERO {} su {}------------".format(i, r))
        # Randomly sample a pair of nodes and compute all the shortest paths between them
        u, v = rd.sample(G.nodes, 2)
        while (u > v):
            u, v = rd.sample(G.nodes, 2)
        paths = shortest_paths(adj, n, u, v)

        # Check if there are at least one path
        if len(paths) > 0:

            # Start the procedure to randomly sample a shortest path
            # by setting as starting node the destination node
            t = v

            # Loop until we reach the source node
            while t != u:
                # print("u: {}".format(u))
                # print("t: {}".format(t))

                # Initialize variables. Pu_t contains the subset of neighbors of t that
                # are predecessors of t along the shortest paths from u to t; each of these nodes
                # will be sampled with a probability defined in probability_distribution
                Pu_t = []
                probability_distribution = []
                paths_u_t = shortest_paths(adj, n, u, t)

                # Compute the number of shortest paths between u and t
                sigma_u_t = len(paths_u_t)
                # print(sigma_u_t)
                # print()

                # For each shortest path
                for j in range(0, len(paths_u_t)):

                    # Build the subset of neighbors of t that are predecessors of t
                    # along the shortest paths from u to t (notice that we always consider the
                    # "original" shortest paths from u to v; therefore, we iteratively select one
                    # predecessor "before" using a variable count updated after every addition to the
                    # randomly sampled shortest path
                    predecessor = paths_u_t[j][-2]
                    # print("ITERATION: {}".format(j))
                    # print(predecessor)
                    if j == 0:
                        Pu_t.append(predecessor)
                        sigma_u_predecessor = 1
                    else:
                        if predecessor == Pu_t[-1]:
                            sigma_u_predecessor += 1
                        else:

                            # For each of these predecessor nodes, define their probability of being chosen as
                            # the number of shortest paths between u and the given predecessor divided by
                            # the number of shortest paths between u and t
                            sampling_probability = sigma_u_predecessor / sigma_u_t
                            probability_distribution.append(sampling_probability)
                            Pu_t.append(predecessor)
                            sigma_u_predecessor = 1

                    if j == len(paths_u_t) - 1:
                        sampling_probability = sigma_u_predecessor / sigma_u_t
                        probability_distribution.append(sampling_probability)

                # Sample z according to the probability distribution defined above;
                # this node is the next node for our sampled shortest path
                # print(Pu_t)
                # print(probability_distribution)
                z = choice(Pu_t, 1, p=probability_distribution)
                z = int(z)
                # print(z)

                # Update betweenness centralities estimations
                if z != u:
                    approximated_centralities[z] += 1 / r

                # Update t
                t = z
        print('Iteration time: {}'.format(time.time() - start_time))

    return approximated_centralities


if __name__ == "__main__":
    twitchNodes = pd.read_csv('twitch_gamers/large_twitch_features.csv')
    twitchEdges = pd.read_csv('twitch_gamers/large_twitch_edges.csv')

    print("Loading graph...")
    G = nx.Graph()
    G.add_nodes_from(twitchNodes)
    G = nx.from_pandas_edgelist(twitchEdges, 'numeric_id_1', 'numeric_id_2')
    print("Finished!")

    # G.add_nodes_from([0, 1, 2, 3, 4, 5, 6])
    # G.add_edges_from([(0, 1),(1, 2), (1, 3), (2, 4), (3, 4), (3, 5), (4, 6), (5, 6)])

    # G.add_edges_from([(0, 1), (1, 2), (0, 3), (1, 3), (2, 4), (3, 4), (3, 5), (4, 6), (5, 6)])

    print("Starting computing centralities...")
    centralities = approximate_betweenness_centrality(G, 0.01)
    saveDictionaryCSV('approximated_betweenness_results.csv', centralities, ['node', 'betweenness centrality'], order=True)
