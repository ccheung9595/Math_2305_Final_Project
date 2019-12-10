# -*- coding: utf-8 -*-

from Functions.prims import prims

graph = input('Please provide the file name of the graph to run the TSP on: ')

MST = prims(graph)

T = (MST[0],  MST[1])

e = sum(MST[2])

print('')

print(f'Optimal Tree Is: {T}')

print('')

print(f'Optimal Cost Is: {e}')
