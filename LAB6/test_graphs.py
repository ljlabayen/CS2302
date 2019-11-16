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

import matplotlib.pyplot as plt
import graph_AL as AL_test
import graph_AM as AM_test # Replace line 3 by this one to demonstrate adjacy maxtrix implementation
import graph_EL as EL_test # Replace line 3 by this one to demonstrate edge list implementation

def tests(choice):  
    
    plt.close("all")   
    
    if choice == 1:
        impl=AL_test
        print('\nYou selected Adjacency List\n')
    if choice == 2:
        impl=AM_test
        print('\nYou selected Adjacency Matrix\n')
    if choice == 3:
        impl=EL_test
        print('\nYou selected Edge List\n')
        
    g = impl.Graph(6)
    g.insert_edge(0,1)
    g.insert_edge(0,2)
    g.insert_edge(1,2)
    g.insert_edge(2,3)
    g.insert_edge(3,4)
    g.insert_edge(4,1)
    g.display()
    g.delete_edge(1,2)
    g.display()
    g.draw()
    
    
    g = impl.Graph(6,directed = True)
    g.insert_edge(0,1)
    g.insert_edge(0,2)
    g.insert_edge(1,2)
    g.insert_edge(2,3)
    g.insert_edge(3,4)
    g.insert_edge(4,1)
    g.display()
    g.draw()
    g.delete_edge(1,2)
    g.display()
    g.draw()
    
    g = impl.Graph(6,weighted=True)
    g.insert_edge(0,1,4)
    g.insert_edge(0,2,3)
    g.insert_edge(1,2,2)
    g.insert_edge(2,3,1)
    g.insert_edge(3,4,5)
    g.insert_edge(4,1,4)
    g.display()
    g.draw()
    g.delete_edge(1,2)
    g.display()
    g.draw()
    
    g = impl.Graph(6,weighted=True,directed = True)
    g.insert_edge(0,1,4)
    g.insert_edge(0,2,3)
    g.insert_edge(1,2,2)
    g.insert_edge(2,3,1)
    g.insert_edge(3,4,5)
    g.insert_edge(4,1,4)
    g.display()
    g.draw()
    g.delete_edge(1,2)
    g.display()
    g.draw()
    
    print('\nas_AL')
    g1=g.as_AL()
    g1.draw()
    g1.display()
    
    print('\nas_AM')
    g2=g.as_AM()
    g2.draw()
    g2.display()
    
    print('\nas_EL')
    g3=g.as_EL()
    g3.draw()
    g3.display()
    
    
