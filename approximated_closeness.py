import networkx as nx
import pandas as pd
import random as rd


def approximate_closeness_centrality(G, k):
    """
    Approximated closeness centrality implementation using the Eppstein-Wang algorithm.

    :param G: weighted/unweighted graph
    :param k: number of iterations
    :return: dictionary containing the approximated closeness centralities for each node
    """

    # Initialize variables
    n = len(list(G.nodes))
    sum_nodes = {}
    approximated_centralities = {}

    # Initialize with 0 the dictionaries containing the sum of distances and
    # the approximated closeness centralities for each node
    for node in list(G.nodes):
        sum_nodes[node] = 0
        approximated_centralities[node] = 0

    # Sample k random vertices from G
    random_nodes = rd.sample(G.nodes, k)
    for src in random_nodes:

        # Solve the SSSP problem for the source
        shortest_paths = nx.single_source_shortest_path(G, src)

        # Update the sum of distances for all the nodes
        for node, path in shortest_paths.items():
            sum_nodes[node] += len(path) - 1

    # Compute the approximated closeness centralities
    for node in list(G.nodes):
        approximated_centralities[node] = 1 / ((n * sum_nodes[node]) / (k * (n - 1)))
    return approximated_centralities


if __name__ == "__main__":
    twitchNodes = pd.read_csv('twitch_gamers/large_twitch_features.csv')
    twitchEdges = pd.read_csv('twitch_gamers/large_twitch_edges.csv')

    G = nx.Graph()
    G.add_nodes_from(twitchNodes)
    G = nx.from_pandas_edgelist(twitchEdges, 'numeric_id_1', 'numeric_id_2')

    centralities = approximate_closeness_centrality(G, 5)
    print(centralities)
