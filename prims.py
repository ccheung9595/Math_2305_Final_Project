# -*- coding: utf-8 -*-


from Functions.reading_writing_functions import get_graph
from Functions.reading_writing_functions import initialize_tree


from Functions.graph_operations import min_cost_edge
from Functions.graph_operations import min_cost


def prims(textfile):
    
    G = get_graph(textfile)
    T_0 = initialize_tree(G)

    T = (T_0[0], T_0[1])
    
    minimum_cost = []
    minimum_cost.append(T_0[2])              
    
    while len(T[0]) != len(G[0]):
        minimum = min_cost_edge(G, T)
        e = min_cost(minimum)
        T[1].append(minimum[0])
        
        vertices = []
        
        for i in range(len(T[1])):
            for j in range(2):
                vertices.append(T[1][i][j])
                
        for l in vertices:
            if l not in T[0]:
                T[0].append(l)
                
        minimum_cost.append(e)
        
    minimum_graph = (T[0], T[1], minimum_cost)
    return minimum_graph
