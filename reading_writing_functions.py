def get_graph(textfile):

    import numpy as np
    import os
    from os.path import dirname, abspath
    
    
    
    d = dirname(dirname(abspath("test.py")))
    
    directory = d + "\Data"
    
    os.chdir(directory)
    
    g = np.loadtxt(textfile, usecols=range(3), dtype = int)
    
    vertices = []
    g_column_0 = []
    g_column_1 = []
    g_column_2 = []
    
    #for i in range(0, len(g)-1):
    #    for j in range(0, len(g[0]-1)):
     #   glist.insert(g[i][0])
        
    
    for j in range(0, len(g)):
        g_column_0.append(g[j][0])
      
        
    for i in range(0, len(g)):
        g_column_1.append(g[i][1])
        
    for i in range(0, len(g)):
        g_column_2.append(g[i][2])
    
    vertices = g_column_0 + g_column_1
    
    unique_vertices = []
    
    for i in vertices:
        if i not in unique_vertices:
            unique_vertices.append(i)
    
    
    G = []
    
    edges = []
    
    G.insert(0, unique_vertices)
    
    
    for i in range(0, len(g_column_0)):
        add = (g_column_0[i], g_column_1[i])
        edges.append(add)
    
    edges = [list(elem) for elem in edges]
    
    G.insert(1, edges)
    
    G.insert(2, g_column_2)
    
    return G

#####################################################

def initialize_tree(G):

    minimum_weight = G[2][0]
    
    for i in range(len(G[2]) - 1):
        if G[2][i] < minimum_weight:
            minimum_weight = G[2][i]
            
            
    
    minimum_weight_location = G[2].index(minimum_weight)
    
    
    v_0_1 = G[1][minimum_weight_location][0]
    v_0_2 = G[1][minimum_weight_location][1]
    e_0 = G[1][minimum_weight_location]
    w_0 = minimum_weight
    
    #list(v_0_1)
    #list(v_0_2)
    list(e_0)
    w_0.tolist()
    
    
    
    T = ([v_0_1, v_0_2], [e_0])
    
    return T
