"""
Laurence Justin Labayen
Lab 6
Last Modified: 11/15/19
CS2302 Data Structures
MW 10:30
Professor: Olac Fuentes
TA: Anindita Nath
Description: Two part lab that includes implementing insert_edge, delete_edge,
display functions on various graph implementations (adjacency list, adjacency
matrix and edge list). Part 2 is the implementation of solving the problem of
crossing a fox, chicken and grain to the other side of the river using Breadth
first search and Depth first search.
"""

import graph_AL as AL
import graph_AM as AM
import graph_EL as EL
import test_graphs as test
import time


print('1. Run test_graphs')
print('2. Fox, Chicken, Grain, Farmer')
choice=int(input('Select choice: '))

if choice==1:
    test.tests()
    
if choice==2:
    
    print('\n1. Adjacency List')
    print('2. Adjacency Matrix')
    print('3. Edge List')
    
    choice2=int(input('Select implementation: '))
    
    print('\n1. Breadth First Search')
    print('2. Depth First Search')
    
    choice3=int(input('Select search function: '))
    
    if choice2==1:
        g=AL.Graph(16)
    if choice2==2:
        g=AM.Graph(16)
    if choice2==3:
        g=EL.Graph(16)
    
    g.insert_edge(0,5)
    g.insert_edge(5,4)
    g.insert_edge(4,7)
    g.insert_edge(4,13)
    g.insert_edge(2,13)
    g.insert_edge(7,11)
    g.insert_edge(10,11)
    g.insert_edge(10,15)
    
    timer=0    
    
    if choice3==1:
        start = time.perf_counter()
        print(g.BFS(0,15))
        end = time.perf_counter()
        print('')
        g.path_steps('BFS')
        
    if choice3==2:
        start = time.perf_counter()
        print(g.DFS(0,15))
        end = time.perf_counter()
        print('')
        g.path_steps('DFS')
        
    timer += end - start
    print('\nSearch running time:', str(round(timer,6)), 'seconds')
    print('\n1. Draw highlighted path')
    print('2. Draw complete graph')
    
    choice4=int(input('Select Draw function: '))
    
    if choice4==1:
        #defaults to BFS
        g.draw_path('BFS')
    if choice4==2:
        g.draw()
