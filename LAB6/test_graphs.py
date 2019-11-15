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
import numpy as np
#import graph_AL as graph
#import graph_AM as graph # Replace line 3 by this one to demonstrate adjacy maxtrix implementation
import graph_EL as graph # Replace line 3 by this one to demonstrate edge list implementation

def tests():  
    plt.close("all")   
    g = graph.Graph(6)
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
    
    
    g = graph.Graph(6,directed = True)
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
    
    g = graph.Graph(6,weighted=True)
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
    
    g = graph.Graph(6,weighted=True,directed = True)
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
    
    g1=g.as_AL()
    g1.draw()
    g1.display()