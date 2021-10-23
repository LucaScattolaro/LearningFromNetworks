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
- Directed	No.
- Node features	No.
- Edge features	No.
- Node labels	Yes.
- Temporal	No.
- Nodes	168,114
- Edges	6,797,557
- Density	0.0005
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
 - Algorithms: the ones that we will see during the course (since we did not cover this topic yet)
    
Problem: compute the motifs of the network:
 - Algorithms: the ones that we will see during the course (since we did not cover this topic yet)

**Baseline and Machines**:	
We	will	use	the	following implementations:
  - Closeness centrality 
    - Exact version ----> https://networkx.org/documentation/stable/reference/algorithms/generated/networkx.algorithms.centrality.closeness_centrality.html#networkx.algorithms.centrality.closeness_centrality
    - Eppstein-Wang algorithm  
    - Chechik-Cohen-Kaplan algorithm
  - Betweeness centrality
    - Exact version ----> https://networkx.org/documentation/stable/reference/algorithms/generated/networkx.algorithms.centrality.betweenness_centrality.html#networkx.algorithms.centrality.betweenness_centrality
    - Approximate version   

.	It	provides exact	methods	and	approximate	methods	and we will modify it to calculate the approximations
- Machines	for	experiments: We are going to use different machines due to avalability:
  - PC1: (Luca) 
  - PC2: (Alessandro)
  - PC3: (Alberto)
  - PC4: (Lavoro Luca)

**Experiments**:	
  - compute	centralities	on	the	data and create a rank	
  - compute	motifs and try to understand what these	motifs represent



