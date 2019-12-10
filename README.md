# Math_ 2305_Final_Project.

A program that has multi-fucntions to find a minimum spanning tree for a given graph

### What is it?


A spanning tree of a graph can be defined 
as a graph with minimal set of edges that connect all vertices. 

A minimum spanning tree of a graph is a spanning tree of the graph with least weight where the weight is computed by adding the weights of all the edges in the spanning tree.

In general, a graph can have multiple minimum spanning trees.    

### Graph File Format (.txt)

The graph file should be a .txt file that is either created or downloaded by the user.

The user's graph file should have 3 columns.

The first column will be vertices in the graph.

The second column will be the vertices that create an edge with each vertex on the same row.

The third column will be the weight of the edge on the same row.

### Graph File Example

```
1 3 1
1 2 5
1 4 4
2 6 6
3 4 3
3 5 2
4 6 8
5 6 7
5 7 9
```

The first column is [1, 1, 1, 2, 3, 3, 4, 5, 5]
The second column is [3, 2, 4, 6, 4, 5, 6, 6, 7]
The third column is [1, 5, 4, 6, 3, 2, 8, 7, 9]

For the first row, [1, 3, 1], (1,3) represents an edge with 1 and 3 each being a vertex in the graph. 1 represents the weight of the edge between vertices 1 and 3.

### User Input

The user should upload the .txt file of the graph into the "Data" folder provided.

When the main.py script prompts the user to "Please provide the file name of the graph to run the TSP on: ", the user should enter the entire file name of the graph.

For example, if the file name is "test_graph.txt" then the user should input test_graph.txt when prompted.
