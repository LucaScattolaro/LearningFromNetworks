# Twitch Gamers Social Network Graph Analysis
In this repository you can find the results for the **centralities** in the `ResultsCentralities` folder (notice that for the approximated centralities, we have also indicated the number of iterations used to compute them in the filename), the **clustering coefficients** in the `ResultsCC` folder and the **motifs** in the `ResultsMotifs` folder.
We also provide a script `Project_LFN.py` that allows you to test all our methods. Nevertheless, we below there are the instructions on how to import the library that contains all the functions in order to try it out. Notice that these implementations are designed to work on `networkx` graphs.
In this repository you can also find a `.pdf` file called `Project_contributions.pdf` which contains the detailed contribution of each member of the group on the project.

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
