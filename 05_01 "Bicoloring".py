from collections import defaultdict, deque
    
# Adjacency list graph representation
class Graph:

    def __init__(self, directed=False):
        self.graph = defaultdict(list)
        self.degree = defaultdict(int)
        self.directed = directed
        self.n = 0                      # Number of vertices
        self.m = 0                      # Number of edges
    
    def add_edge(self, x, y, stop=False):
        self.graph[x].append(y)
        self.degree[x] += 1
        self.n += 1
        if not self.directed and not stop:
            self.add_edge(y, x, True)
        else:
            self.m += 1

    def print_graph(self):
        for i in self.graph:
            print(i, self.graph[i])

    def initialize_search(self):
        self.discovered = defaultdict(bool)
        self.processed = defaultdict(bool)
        self.parent = defaultdict(int)

    def bfs(self, v, pve=None, pe=None, pvl=None):
        self.initialize_search()
        q = deque()
        q.append(v)
        self.discovered[v] = True

        while(q):
            v = q.popleft()
            # process_vertex_early(v)
            print('process vertex early', v)
            if pve:
                pve(v)
            self.processed[v] = True
            for y in self.graph[v]:
                if not self.processed[y] or self.directed:
                    # process_edge(v, y)
                    print('process edge', v, y)
                    if pe:
                        pe(v, y)
                if not self.discovered[y]:
                    q.append(y)
                    self.discovered[y] = True
                    self.parent[y] = v
            # process_vertex_late(v)
            print('process vertex late', v)
            if pvl:
                pvl(v)

    def bipartite(self):
        self.is_bipartite = True
        self.color = defaultdict(str)
        self.initialize_search()

        for v in self.graph:
            if not self.discovered[v]:
                self.color[v] = 'BLACK'
                self.bfs(v, None, self.bipartite_process_edge)
        
        print(self.is_bipartite)
        return self.is_bipartite
        
    def bipartite_process_edge(self, x, y):
        if self.color[x] == self.color[y]:
            self.is_bipartite = False
        print(self.color[x], self.color[y])
        if self.color[x] == 'BLACK':
            self.color[y] = 'WHITE'
        elif self.color[x] == 'WHITE':
            self.color[y] = 'BLACK'
        print(self.color[x], self.color[y])
    

# Driver code
g = Graph()
g.add_edge(0, 1)
g.add_edge(1, 2)
g.add_edge(0, 3)

print("Graph:")
g.print_graph()
print()
print("Bipartite Test:")
g.bipartite()
