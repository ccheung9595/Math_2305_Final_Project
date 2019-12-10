
def min_cost_edge(G, T):

    edges_0 = []
    
    
    
    for e in G[1]:
        for v in T[0]:
            if v in e and e not in T[1]:
              edges_0.append(e)
        
    
    edges = []
    
    for num in edges_0:
        if num not in edges:
            edges.append(num)
        elif num in edges:
            edges.remove(num)
            
        weights = []
    
    for j in G[1]:
        for i in edges:
            if i == j:
                weights.append(G[2][G[1].index(j)])
                
    
    minimum_weight = weights[0]
    
        
    for t in weights:
        if t < minimum_weight:
            minimum_weight = t
    

    minimum_edge = edges[weights.index(minimum_weight)]    
    minimum = [minimum_edge, minimum_weight]
    
    return minimum

def min_cost(minimum):
    
    e = minimum[1]
    
    return e
