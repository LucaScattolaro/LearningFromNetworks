# Mid Term Report
## Update on the with respect to the original project proposal.

The main structure of the project is unchanged. What we are currently working on is the optimization and approximation of the computation of the betweenness centralities and the motifs.

**Betweenness Centralities**
We are using the algorithm [1] as described in the original project proposal, and we are looking for:
 - Optimization of the computing time at code level
 - The best number of iteration to obtain a result in feasible time

**Motifs computation**
We have tried to compute the exactly using the ESU [2] algorithm for motifs seen in class, but it takes too much time as expected. Currently we are looking for approximated algorithms for motifs computation.

## References
[1] Matteo Riondato and Evgenios M Kornaropoulos. Fast approximation of betweenness centrality through sampling.
Data Mining and Knowledge Discovery, 30(2):438–475, 2016.

[2] Wernicke, S. (2006) Ecient detection of network motifs. IEEE/ACM Transactions on Computational Biology and Bioinformatics.
