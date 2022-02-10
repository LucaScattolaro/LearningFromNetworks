# Instructions
We provide a script `test.py` that allows you to test all our methods using a dummy graph. Nevertheless, we also provide instructions on how to import these libraries in order to try out our methods and test the code. Notice that these implementations are designed to work on `networkx` graphs.

### Approximated Centralities
For the approximated centralities, the _Eppstein-Wang algorithm_ and the _Riondato-Kornaropoulos algorithm_ are implemented in `ApproximatedCentralitiesLibrary.py`. To import  the library into your code, just write:
```
from ApproximatedCentralitiesLibrary import *
```
Then, you can call the 2 functions from code as:
```
closeness = approximated_closeness_centrality(G, k)
betweenness = approximated_betweenness_centrality(G, epsilon)
```

### Clustering Coefficients

