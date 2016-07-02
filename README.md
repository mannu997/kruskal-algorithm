# kruskal-algorithm
Given a graph which consists of several edges connecting the  nodes in it. 
It is required to find a subgraph of the given graph with the following properties:

The subgraph contains all the nodes present in the original graph.
The subgraph is of minimum overall weight (sum of all edges) among all such subgraphs.
It is also required that there is exactly one, exclusive path between any two nodes of the subgraph.
One specific node  is fixed as the starting point of finding the subgraph. 
Find the total weight of such a subgraph (sum of all edges in the subgraph)

Input Format

First line has two integers , denoting the number of nodes in the graph and , denoting the number of edges in the graph.

The next  lines each consist of three space separated integers   , where  and  denote the two nodes between which the undirected edge exists,  denotes the length of edge between the corresponding nodes.

The last line has an integer , denoting the starting node.

Constraints 
 
 
 
 
If there are edges between the same pair of nodes with different weights, they are to be considered as is, like multiple edges.

Output Format

Print a single integer denoting the total weight of tree so obtained (sum of weight of edges).

Sample Input


5 6

1 2 3

1 3 4

4 2 6

5 2 2

2 3 5

3 5 7
1

Sample Output

15
