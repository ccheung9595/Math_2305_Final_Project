# -*- coding: utf-8 -*-

def get_graph(textfile):

    import numpy as np
    import os
    from os.path import dirname, abspath
    
    # Sets environment to proper working directory so the .txt file can be uploaded
    d = dirname(abspath("main.py"))
    directory = d + "\Data"  
    os.chdir(directory) 
    
    
    # loads data from text file into numpy array
    # whitespace is used to separate the values
    g = np.loadtxt(textfile, usecols=range(3), dtype = int)
    
    vertices = []
    g_column_0 = []
    g_column_1 = []
    g_column_2 = []
    
    # turns columns in numpy array(g) into rows
    for j in range(0, len(g)):
        g_column_0.append(g[j][0])
        
    for i in range(0, len(g)):
        g_column_1.append(g[i][1])
        
    for i in range(0, len(g)):
        g_column_2.append(g[i][2])
   

    # takes the edges from the graph given
    # creates a list of all unique vertices in the graph given
    vertices = g_column_0 + g_column_1
    unique_vertices = []
    
    for i in vertices:
        if i not in unique_vertices:
            unique_vertices.append(i)
    
    # empty list will be used to create new graph for data given
    # new graph will be used to determine the minimum spanning tree graph
    G = []
    
    edges = []
    
    # adds a row in the new graph that shows all the vertices in the graph given
    G.insert(0, unique_vertices)
    
    # adds a row in the new graph for the edges in the graph given
    # each element in the new row is an edge on the graph given
    for i in range(0, len(g_column_0)):
        add = (g_column_0[i], g_column_1[i])
        edges.append(add) 
    edges = [list(elem) for elem in edges]
    G.insert(1, edges)
    
    # adds a row in the new graph for the corresponding weights of each edge
    G.insert(2, g_column_2)
    
    return G


def initialize_tree(G):
    
    # intializes the minimum_weight variable
    minimum_weight = G[2][0]
    # iterates through weights of graph
    # if the weight is smaller than the initialized minimum weight
    # then the minimum weight will be replaced with that weight
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
    
    
    
    
    T_0 = ([v_0_1, v_0_2], [e_0], w_0)
    
    return T_0
