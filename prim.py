from collections import defaultdict, deque
    
# Adjacency list graph representation
class Graph:

    # Init graph
    def __init__(self, directed=False):
        self.graph = defaultdict(list)
        self.directed = directed
        self.maxint = float('inf')

    # Add vertex to graph
    def add_vertex(self, v):
        if not self.graph[v]:
            self.graph[v] = []
    
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


        



# Driver code
g = Graph()
g.add_edge(1, 2, 1)
g.add_edge(2, 3, 2)
g.add_edge(3, 4, 3)
g.add_edge(4, 1, 4)
g.print_graph()
print()
p = g.prim(1)
print("Parent", p.items())
