# Kruskal’s Minimum Spanning Tree Algorithm

## Author: Yusen Peng

## introduction

This lab is about implementing and testing Kruskal's Mininum Spanning Tree algorithm. Apart from understanding and implementing Kruskal's Minimum Spanning Tree algorithm, this lab also integrates the basic application of Python graph library -- ```networkx```.

## file structures

The files in this labs are structured as follows:

1. ```kruskal.py```: it contains the kernel Kruskal's MST algorithm and a whole bunch of private helper methods to assist in implementing the algorithm itself.

2. ```kruskal_test.py```: it contains the graph initialization of 3 test cases and it is the file that actually executes our testing.

3. ```utils.py``` : it contains two helper functions to help draw the original graph and its minumum spanning tree. it further simplifies the complex process of just drawing a graph.

## how to test the algorithm

It's incredibly easy to run the test driver. just open the terminal and issue the following command (make sure you run python3, not python):

```bash
python3 kruskal_test.py
```

## visual output

See outputs in the ```test_graphs``` directory. There are only three test cases (yeah each graph is very tedious to build manually). On PuTTY/Mac terminal, it's not possible to get a visual view of these original graphs and their corresponding MST. I recommend using __FileZilla__ or __WinSCP__ to download these visual graphs from the remote server to a local directory.

## test output for the first test case

Original Graph:

1. ![alt text](test_graphs/problem_1/graph.png)

Minimum spanning tree:

1. ![alt text](test_graphs/problem_1/MST.png)

## test output for the second test case

Original Graph:

1. ![alt text](test_graphs/problem_2/graph.png)

Minimum spanning tree:

1. ![alt text](test_graphs/problem_2/MST.png)

## test output for the third test case

Original Graph:

1. ![alt text](test_graphs/problem_3/graph.png)

Minimum spanning tree:

1. ![alt text](test_graphs/problem_3/MST.png)
