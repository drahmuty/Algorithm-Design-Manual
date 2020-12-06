







"""
# I initially thought it was finding the MST, but we're supposed to find
# the overall shortest path from any vertex. So we need to use Floyd's algo
# instead for all-pairs shortest path. Saving original code here.

from collections import defaultdict, deque
    
# Adjacency list graph representation
class Graph:

    # Init graph
    def __init__(self, directed=False):
        self.graph = defaultdict(list)
        self.directed = directed
        self.maxint = float('inf')
    
    # Add an edge to graph
    def add_edge(self, x, y, w, stop=False):
        self.graph[x].append([y, w])
        if not self.directed and not stop:
            self.add_edge(y, x, w, True)

    # Print graph contents
    def print_graph(self):
        for i in self.graph:
            print(i, self.graph[i])

    # Prim's algorithm
    def prim(self, start):

        # Init dictionaries
        intree = defaultdict(bool)
        parent = defaultdict(int)
        distance = defaultdict(int)
        for v in self.graph:
            distance[v] = self.maxint

        # Init start vertex
        parent[start] = -1
        distance[start] = 0
        v = start

        # Main loop
        while(not intree[v]):
            intree[v] = True
            neighbors = self.graph[v]

            # Update distance to neighbor vertices
            for neighbor in neighbors:
                y = neighbor[0]
                w = neighbor[1]
                if not intree[y] and w < distance[y]:
                    distance[y] = w
                    parent[y] = v
            
            # Select nearest vertex
            v = 1
            dist = self.maxint
            for i in self.graph:
                if not intree[i] and distance[i] < dist:
                    dist = distance[i]
                    v = i

        return parent


import math

def freckles(vertices):

    # Create adjacency list graph object
    g = Graph()

    # Add vertices to graph
    num_vertices = len(vertices)
    for i in range(num_vertices):
        for j in range(i+1, num_vertices):
            # Calculate weight and add to graph
            v1 = vertices[i]
            v2 = vertices[j]
            x1 = v1[0]
            y1 = v1[1]
            x2 = v2[0]
            y2 = v2[1]
            w = math.sqrt(abs(x2-x1)**2 + abs(y2-y1)**2)
            g.add_edge(v1, v2, w)
    
    # Use Floyd's algorithm to find the all-pairs shortest path
    



# Test cases
freckles([(1,1), (2,2), (2,4)])
"""
