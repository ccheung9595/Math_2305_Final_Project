from reading_writing_functions import get_graph
from reading_writing_functions import initialize_tree


from graph_operations import min_cost_edge

G = get_graph("graph1.txt")
T = initialize_tree(G)


                


while len(T[0]) != len(G[0]):

    e = min_cost_edge(G, T)
       
    minimum_edge = G[1][G[2].index(e)]
    
    T[1].append(minimum_edge)
    
    print(T)
    
    vertices = []
    
    for i in range(len(T[1])):
        for j in range(2):
            vertices.append(T[1][i][j])
            
    print(vertices)
    
    for l in vertices:
        if l not in T[0]:
            T[0].append(l)
