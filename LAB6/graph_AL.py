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

# Adjacency list representation of graphs
import numpy as np
import matplotlib.pyplot as plt
from scipy.interpolate import interp1d
import graph_AM as AM
import graph_EL as EL

class Edge:
    def __init__(self, dest, weight=1):
        self.dest = dest
        self.weight = weight
        
class Graph:
    # Constructor
    def __init__(self, vertices, weighted=False, directed = False):
        self.al = [[] for i in range(vertices)]
        self.weighted = weighted
        self.directed = directed
    
    # Insert Edge function from class website    
    def insert_edge(self,source,dest,weight=1):
        if source >= len(self.al) or dest>=len(self.al) or source <0 or dest<0:
            print('Error, vertex number out of range')
        if weight!=1 and not self.weighted:
            print('Error, inserting weighted edge to unweighted graph')
        else:
            self.al[source].append(Edge(dest,weight)) 
            if not self.directed:
                self.al[dest].append(Edge(source,weight))
    # Delete Edge helper function from class website   
    def delete_edge_(self,source,dest):
        i = 0
        for edge in self.al[source]:
            if edge.dest == dest:
                self.al[source].pop(i)
                return True
            i+=1    
        return False
    # Insert Edge function from class website   
    def delete_edge(self,source,dest):
        if source >= len(self.al) or dest>=len(self.al) or source <0 or dest<0:
            print('Error, vertex number out of range')
        else:
            deleted = self.delete_edge_(source,dest)
            if not self.directed:
                deleted = self.delete_edge_(dest,source)
        if not deleted:        
            print('Error, edge to delete not found')  
    # Display function from class website              
    def display(self):
        print('[',end='')
        for i in range(len(self.al)):
            print('[',end='')
            for edge in self.al[i]:
                print('('+str(edge.dest)+','+str(edge.weight)+')',end='')
            print(']',end=' ')    
        print(']')   
    # Draw function from class website              
    def draw(self):

        scale = 30
        fig, ax = plt.subplots()
        for i in range(len(self.al)):
            for edge in self.al[i]:
                d,w = edge.dest, edge.weight
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
                    ax.plot(x,s*y,linewidth=1,color='k')
                    if self.directed:
                        xd = [x0[2]+2*s,x0[2],x0[2]+2*s]
                        yd = [y0[2]-1,y0[2],y0[2]+1]
                        yd = [y*s for y in yd]
                        ax.plot(xd,yd,linewidth=1,color='k')
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
        
    # as_EL converts current adjacency list graph to an edge list
    def as_EL(self):
        
        # create an empty graph with the same length as current graph
        edgelist = EL.Graph(len(self.al),self.weighted, self.directed)
        
        # insert edges using a nested loop
        for i in range(len(self.al)):
            for j in self.al[i]:
                edgelist.insert_edge(i, j.dest, j.weight)
        return edgelist
    # as_AM converts current adjacency list graph to an adjacency matrix
    def as_AM(self):
        
        # create an empty graph with the same length as current graph
        matrix =  AM.Graph(len(self.al), self.weighted, self.directed)
        
        # insert edges using a nested loop
        for i in range(len(self.al)):
            for j in self.al[i]:
                matrix.insert_edge(i, j.dest, j.weight)
                
        return matrix
    
    def as_AL(self):
        return self
    
    # Breadth first search function used to return path
    def BFS(self, s,end): 
  
        # Mark all the vertices as not visited 
        visited = [False] * (len(self.al)) 
  
        # Create a queue for BFS 
        queue = [[s]] 
  
        while queue: 
  
            # pop element from queue and assign it to s
            s = queue.pop(0)
            
            # if end is found, return
            if s[-1]==end:
                print('From AL BFS')
                return s

  
            # Get all adjacent vertices of the 
            # popped vertex s. If a adjacent 
            # has not been visited, then mark it 
            # visited and append it 
            for i in self.al[s[-1]]: 
                if visited[i.dest] == False: 
                    queue.append(s + [i.dest]) 
                    visited[i.dest] = True
    
    # Depth first search function used to return path
    def DFS(self, s, end):
        # start an empty list of visited elements
        visited=[]
        
        # call DFS helper function
        print('From AL DFS')
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
            for neighbour in self.al[s]:
                self.DFS_(visited, neighbour.dest, end)
        
        return visited
    
    # Function to print the path in the correct format as shown in the lab
    # instructions [b0,b1,b2,b3]
    def path_steps(self, func):
        if func == 'DFS':
            search_path = self.DFS(0,len(self.al)-1)
        if func == 'BFS':
            search_path = self.BFS(0,len(self.al)-1)
        
        for i in search_path:
            print (i, [int(x) for x in list('{0:04b}'.format(i))]) 
                
    # Modified draw function from class website used to highlight path
    #found from BFS or DFS
    def draw_path(self, func):
        scale = 30
        fig, ax = plt.subplots()
        
        if func == 'DFS':
            search_path = self.DFS(0,len(self.al)-1)
        if func == 'BFS':
            search_path = self.BFS(0,len(self.al)-1)
        
        # create path list to be used to highlight path
        path = []
        for j in range(len(search_path)-1):
            path.append((search_path[j], search_path[j+1]))
            

        for i in range(len(self.al)):
            for edge in self.al[i]:
                
                # highlighted path
                if (i, edge.dest) in path or (edge.dest, i) in path:
                    line_color = "#ff007f"

                else:
                    line_color = "#eeefff"
                
                d,w = edge.dest, edge.weight
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
