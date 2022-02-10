# Instructions
We provide a script `Project_LFN.py` that allows you to test all our methods. Nevertheless, we also provide instructions on how to import the library that contains all the functions in order to try it out. Notice that these implementations are designed to work on `networkx` graphs.

### Graph Library
Graph Library is defined in `graphLibrary.py`. It contains all the methods to compute the centralities, the clustering coefficients and the motifs plus some helper functions that allow to draw a graph, save the results in a `.csv` file or produce a ranking of scores (e.g. for the centralities). To import the library into your code, just write:
```
import graphLibrary as gl
```
Then, you can call the functions from code as:
```
closeness = gl.approximated_closeness_centrality(G, k)
betweenness = gl.approximated_betweenness_centrality(G, epsilon)
...
```
