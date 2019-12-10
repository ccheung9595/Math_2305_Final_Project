# -*- coding: utf-8 -*-

def min_cost_edge(G, T):
    
    edges_0 = []  
    
    # finds all edges that have a vertex already in the minimum tree spanning graph
    for e in G[1]:
        for v in T[0]:
            if v in e and e not in T[1]:
              edges_0.append(e)
        
    
    edges = []
    # removes any cycles 
    for num in edges_0:
        if num not in edges:
            edges.append(num)
        elif num in edges:
            edges.remove(num)
            
        weights = []
    
     # finds weights corresponding to edges that have a vertex in the minimum spanning tree graph
    for j in G[1]:
        for i in edges:
            if i == j:
                weights.append(G[2][G[1].index(j)])
                
     # finds minimum weight of the edges that have a vertex in the minimum spanning tree graph
    minimum_weight = weights[0]   
        
    for t in weights:
        if t < minimum_weight:
            minimum_weight = t
    
     # creates a list with:
     # the edge with the lowest weight that has a vertex in the minimum spanning tree graph
     # the corresponding weight of that edge
    minimum_edge = edges[weights.index(minimum_weight)]    
    minimum = [minimum_edge, minimum_weight]
    
    return minimum

def min_cost(minimum):
     # returns cost of the incident edge with the lowest weight
    
    e = minimum[1]
    
    return e
