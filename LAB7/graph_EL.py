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

# Edge list representation of graphs
import numpy as np
import matplotlib.pyplot as plt
from scipy.interpolate import interp1d
#import graph_AM as AM
import graph_AL as AL
import sys

sys.setrecursionlimit(150000)

class Edge:
    def __init__(self, source, dest, weight=1):
        self.source = source
        self.dest = dest
        self.weight = weight
        
class Graph:
    # Constructor
    def __init__(self, vertices, weighted=False, directed = False):
        self.el = []
        self.vertices = vertices
        self.weighted = weighted
        self.directed = directed
        self.representation = 'EL'
    
    # Insert edge function that adds an edge given its source, destination and weight
    def insert_edge(self,source,dest,weight=1):

        if weight!=1 and not self.weighted:
            print('Error, inserting weighted edge to unweighted graph')
        else:
            # insert edge to graph
            self.el.append(Edge(source,dest,weight)) 

    # Delete edge function that deletes an edge given its source and destination
    def delete_edge(self,source,dest):
        
        # find position of the given edge and remove from graph
        for i in self.el:
            if i.source==source and i.dest==dest:
                self.el.remove(i)
    
    # Displays all the edges in the graph            
    def display(self):
        print('[',end='')
        for i in self.el:
            print('('+str(i.source)+','+str(i.dest)+','+str(i.weight)+')',end='')
        print(']',end=' ')
        print('')
    
#    # Draw function that converts the current graph to an adjacency list then draws
#    # the graph (as per lab instructions)
#    def draw(self):
#        
#        # converts current graph to an adjacency list to be used for the function
#        adjlist = self.as_AL()
#        
#        scale = 30
#        fig, ax = plt.subplots()
#        for i in range(len(adjlist.al)):
#            for edge in adjlist.al[i]:
#                d,w = edge.dest, edge.weight
#                if self.directed or d>i:
#                    x = np.linspace(i*scale,d*scale)
#                    x0 = np.linspace(i*scale,d*scale,num=5)
#                    diff = np.abs(d-i)
#                    if diff == 1:
#                        y0 = [0,0,0,0,0]
#                    else:
#                        y0 = [0,-6*diff,-8*diff,-6*diff,0]
#                    f = interp1d(x0, y0, kind='cubic')
#                    y = f(x)
#                    s = np.sign(i-d)
#                    ax.plot(x,s*y,linewidth=1,color='k')
#                    if self.directed:
#                        xd = [x0[2]+2*s,x0[2],x0[2]+2*s]
#                        yd = [y0[2]-1,y0[2],y0[2]+1]
#                        yd = [y*s for y in yd]
#                        ax.plot(xd,yd,linewidth=1,color='k')
#                    if self.weighted:
#                        xd = [x0[2]+2*s,x0[2],x0[2]+2*s]
#                        yd = [y0[2]-1,y0[2],y0[2]+1]
#                        yd = [y*s for y in yd]
#                        ax.text(xd[2]-s*2,yd[2]+3*s, str(w), size=12,ha="center", va="center")
#            ax.plot([i*scale,i*scale],[0,0],linewidth=1,color='k')        
#            ax.text(i*scale,0, str(i), size=20,ha="center", va="center",
#             bbox=dict(facecolor='w',boxstyle="circle"))
#        ax.axis('off') 
#        ax.set_aspect(1.0) 
            
    def as_EL(self):
        return self
    
    # as_AM converts current edge list graph to an adjacency matrix
    def as_AM(self):
        
         # create an empty graph with the same length as current graph
        matrix =  AM.Graph(self.vertices, self.weighted, self.directed)
        
        # insert edges using a loop
        for i in self.el:
            matrix.insert_edge(i.source, i.dest, i.weight)
        return matrix
    
    # as_AM converts current adjacency matrix graph to an adjacency list
    def as_AL(self):
        
         # create an empty graph with the same length as current graph
        adjlist =  AL.Graph(self.vertices, self.weighted, self.directed)

        # insert edges using a loop
        for i in self.el:
            adjlist.insert_edge(i.source, i.dest, i.weight)
        return adjlist
    
    # Breadth first search function used to return path
    def BFS(self, s,end): 
  
        # Mark all the vertices as not visited 
        visited = [False] * (self.vertices)
        # Assign visited element at s to True
        visited[s]=True
        # Create a queue for BFS 
        queue = [[s]] 
        # Create a path list with s as the first element
        path=[s]
  
        while queue: 
  
            # pop element from queue and assign it to s 
            s = queue.pop(0)
            if s==end:
                return

  
            # Get all adjacent vertices of the 
            # popped vertex s. If a adjacent 
            # has not been visited, then mark it 
            # visited and append it 
            for i in self.el: 
                if visited[i.dest] == False: 
                    queue.append(i.dest)
                    visited[i.dest] = True
                    path.append(i.dest)
            print('From EL BFS')      
            return path
    
    # Depth first search function used to return path                 
    def DFS(self, s, end):
        
        # start an empty list of visited elements
        visited=[]
        
        # call DFS helper function
        print('From EL DFS')
        return self.DFS_(visited, s, end)
    
    # Depth first search helper function used to return path
    def DFS_(self, visited, s, end):
        
        # check if s is in the visited list
        if s not in visited:
            
            # check if visited is not empty and if the last element of
            # visited is the end element
            if len(visited) > 0 and visited[-1]==end:
                return
            
            # append s to visited list
            visited.append(s)

            # call function recursively with the starting element as the
            # destination of the neighbours of s
            for neighbour in self.el:
                self.DFS_(visited, neighbour.dest, end)
          
        return visited
    
    # Function to print the path in the correct format as shown in the lab
    # instructions [b0,b1,b2,b3]    
    def path_steps(self, func):
        if func == 'DFS':
            search_path = self.DFS(0,self.vertices-1)
        if func == 'BFS':
            search_path = self.BFS(0,self.vertices-1)
        
        for i in search_path:
            print (i, [int(x) for x in list('{0:04b}'.format(i))]) 
            
    # Modified draw function from class website used to highlight path
    #found from BFS or DFS
    def draw_path(self, func):
        
        if func == 'DFS':
            search_path = self.DFS(0,self.vertices-1)
        if func == 'BFS':
            search_path = self.BFS(0,self.vertices-1)
        
        scale = 30
        fig, ax = plt.subplots()
        
        # create path list to be used to highlight path
        path = []
        
        for j in range(len(search_path)-1):
            path.append((search_path[j], search_path[j+1]))

        adjlist=self.as_AL()
        
        for i in range(len(adjlist.al)):
            for j in adjlist.al[i]:
                # highlighted path
                if (i, j.dest) in path or (j.dest, i) in path:
                    line_color = "#ff007f"

                else:
                    line_color = "#eeefff"
                
                d,w = j.dest, j.weight
                if self.directed or d>i:
                    x = np.linspace(i*scale,d*scale)
                    x0 = np.linspace(i*scale,d*scale,num=5)
                    diff = np.abs(d-i)
                    if diff == 1:
                        y0 = [0,0,0,0,0]
                    else:
                        y0 = [0,-6*diff,-8*diff,-6*diff,0]
                    f = interp1d(x0, y0, kind='cubic')
                    y = f(x)
                    s = np.sign(i-d)
                    ax.plot(x,s*y,linewidth=1,color=line_color)
                    if self.directed:
                        xd = [x0[2]+2*s,x0[2],x0[2]+2*s]
                        yd = [y0[2]-1,y0[2],y0[2]+1]
                        yd = [y*s for y in yd]
                        ax.plot(xd,yd,linewidth=1,color=line_color)
                    if self.weighted:
                        xd = [x0[2]+2*s,x0[2],x0[2]+2*s]
                        yd = [y0[2]-1,y0[2],y0[2]+1]
                        yd = [y*s for y in yd]
                        ax.text(xd[2]-s*2,yd[2]+3*s, str(w), size=12,ha="center", va="center")
            ax.plot([i*scale,i*scale],[0,0],linewidth=1,color='k')        
            ax.text(i*scale,0, str(i), size=20,ha="center", va="center",
             bbox=dict(facecolor='w',boxstyle="circle"))
        ax.axis('off') 
        ax.set_aspect(1.0)
        plt.show(block = True)
        
    def rev(self):
        g=Graph(self.vertices, self.weighted, self.directed)
        
        for i in self.el:
            g.insert_edge(i.dest, i.source, i.weight)
            
        self.el=g.el
        
