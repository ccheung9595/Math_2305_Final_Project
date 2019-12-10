from reading_writing_functions import get_graph
from reading_writing_functions  import prims_mst_alg

Data = input("Choose a graph from Data: ")

VT = int(input("Choose a starting Vertex: "))

graph = get_graph(Data)

MST= prims_mst_alg(graph, VT)

print('')

print(f'The minimum spanning tree for graph {Data} is: {MST[0]}')

print(f'The tree's cost:  {MST[1]}')
