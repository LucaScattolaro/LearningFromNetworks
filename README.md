# Project_Proposal
## Finding significant Nodes in Twitch network with Node Features and find important motifs.

**Motivation**
Social network analysis is a field of study that attempt to understand relationships between entities in a network based on the assumption about the “importance” of relationship between entities.
Twitch and Social Live-Streaming (SLS) services are recent internet phenomena that support massive amounts of users congregating together around common interests to form
interactive and social communities.

- We want to find the most influent people in this Social Network since it is an important task that may be useful for marketing and statistical purposes. We will do this by computing several centrality and clustering coefficient statistics.
- We want	to understand	what motifs	are	more surprising	in Twitch in order to discover and analyze the structure of the Twitch network and see what we can understand from it

**Data**
We are going to use a social network of Twitch users collected from the public API in Spring 2018. 
Nodes are Twitch users and edges are mutual follower relationships between them. The graph forms a single strongly connected component without missing attributes. The dataset can be found here: https://snap.stanford.edu/data/twitch_gamers.html
      
Here we report some dataset statistics:
- Directed	      No.
- Node features	No.
- Edge features	No.
- Node labels	Yes.
- Temporal	      No.
- Nodes	      168,114
- Edges	      6,797,557
- Density	      0.0005
- Transitvity	0.0184

**Method**	
Problem: compute the centrality scores for all nodes using exact algorithms and also their approximations in order to compare the computational time and error between exact algorithms and their:
  - Closeness centrality 
    - Exact version
    - Eppstein-Wang algorithm
    - Chechik-Cohen-Kaplan algorithm
  - Betweeness centrality
    - Exact version
    - Approximate version    

Problem: compute the clustering coefficient for the graph:
 - Local clustering coefficient
 - Global clustering coefficient
    
Problem: compute the motifs of the network:
 - Algorithms: the ones that we will see during the course (since we did not cover this topic yet)

**Baseline and Machines** 	
We will use the following implementations:
  - Closeness centrality 
    - Exact version ----> https://networkx.org/documentation/stable/reference/algorithms/generated/networkx.algorithms.centrality.closeness_centrality.html#networkx.algorithms.centrality.closeness_centrality
    - Eppstein-Wang algorithm ----> we will implement it ourselves (using the pseudocode we have seen in the lessons)
  - Betweeness centrality
    - Exact version ----> https://networkx.org/documentation/stable/reference/algorithms/generated/networkx.algorithms.centrality.betweenness_centrality.html#networkx.algorithms.centrality.betweenness_centrality
    - Approximate version ----> we will implement it ourselves (using the pseudocode we have seen in the lessons)

  - Clustering coefficient
    - Local clustering coefficient ---> we will implement it ourselves (using the pseudocode we have seen in the lessons)
    - Global clustering coefficient ---> we will implement it ourselves (using the pseudocode we have seen in the lessons)
  
  - Motifs ---> we don't know yet, we will choose after we have covered this topic in class

**Machine for experiments** We are going to use different machines due to avalability:
  - PC1: 
      - CPU: Intel(R) Core(TM) i7-2670QM CPU @ 2.20GHz
      - RAM: 6,0 GB 
  - PC2: 
      - CPU: Intel(R) Core(TM) i5-3570K CPU @ 3.40GHz
      - RAM: 8,0 GB 
  - PC3: 
      - CPU: Intel(R) Core(TM) i5-8250U CPU @ 1.60GHz-1.80 GHz
      - RAM: 16,0 GB   
  - PC4: 
      - CPU: : 11th Gen Intel(R) Core(TM) i5-11600K @ 3.90GHz
      - RAM: 32,0 GB 

**Experiments** 
  - Compute centralities on the data, compare the results and create the rankings
  - Compute clustering coefficients and analyze them
  - Compute motifs and try to understand what these motifs represent



