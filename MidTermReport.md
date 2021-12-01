# Mid Term Report
## Update on the with respect to the original project proposal.

The main structure of the project is unchanged. What we are currently working on is the optimization and approximation of the computation of the betweenness centralities and the motifs.

**Betweenness Centralities**
The exact version [1] of the computation takes too much time as expected, so we're working on approximate computation. We are using the algorithm [2] as described in the original project proposal, and we are looking for:
 - optimize the computation time at code level
 - the best number of iteration to obatin a result in acceptable time

**Motifs computation**
We have tried to compute the exactly using the ESU [3] algorithm for motifs seen in class, but it takes too much time as expected. Currently we are looking for approximated algorithms for motifs computation.

## References
[1]https://networkx.org/documentation/stable/reference/algorithms/generated/networkx.algorithms.centrality.betweenness_centrality.html#networkx.algorithms.centrality.betweenness_centrality

[2] Matteo Riondato and Evgenios M Kornaropoulos. Fast approximation of betweenness centrality through sampling.
Data Mining and Knowledge Discovery, 30(2):438–475, 2016.

[3] Wernicke, S. (2006) Ecient detection of network motifs. IEEE/ACM Transactions on Computational Biology and Bioinformatics.
