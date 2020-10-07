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
        self.entry_time = defaultdict(int)
        self.exit_time = defaultdict(int)
        self.time = 0
        self.finished = False
        self.path = []

    # Breadth-first search
    def bfs(self, v, pve=None, pe=None, pvl=None):
        self.initialize_search()
        q = deque()
        q.append(v)
        self.discovered[v] = True

        while(q):
            v = q.popleft()
            # print('process vertex early', v)
            if pve:
                pve(v)
            self.processed[v] = True
            for y in self.graph[v]:
                if not self.processed[y] or self.directed:
                    # print('process edge', v, y)
                    if pe:
                        pe(v, y)
                if not self.discovered[y]:
                    q.append(y)
                    self.discovered[y] = True
                    self.parent[y] = v
            # print('process vertex late', v)
            if pvl:
                pvl(v)

    
    # Find path
    def find_path(self, start, end):
        if start == end:
            print('Start')
            print(end)
            if not self.finished:
                self.path.append(end)
        elif end == 0:
            self.finished = True
        else:
            self.find_path(start, self.parent[end])
            print(end)
            if not self.finished:
                self.path.append(end)




# Create a string representation of integers
def int_to_str(a, b, c, d):
    return str(a) + str(b) + str(c) + str(d)


# Main program
# Return smallest number of wheel turns required to reach the 
# target result or return None if there is no path.
def wheels(start, end, forbidden_vertices):
    g = Graph()
    a = b = c = d = 0
    
    # Create dictionary of forbidden vertices for faster lookup time
    forbidden_vertices_dict = defaultdict(str)
    for f in forbidden_vertices:
        forbidden_vertices_dict[f] = True
    
    # Create graph, skipping forbidden vertices
    while True:
        v = int_to_str(a, b, c, d)
        if forbidden_vertices_dict[v]:
            print('Forbidden:', v)
        else:
            w = int_to_str(((a + 1) % 10), b, c, d)
            x = int_to_str(a, ((b + 1) % 10), c, d)
            y = int_to_str(a, b, ((c + 1) % 10), d)
            z = int_to_str(a, b, c, ((d + 1) % 10))
            if not forbidden_vertices_dict[w]:
                g.add_edge(v, w)
            if not forbidden_vertices_dict[x]:
                g.add_edge(v, x)
            if not forbidden_vertices_dict[y]:
                g.add_edge(v, y)
            if not forbidden_vertices_dict[z]:
                g.add_edge(v, z)
        
        # Increment vertex
        d += 1
        if d > 9:
            d = 0
            c += 1
        if c > 9:
            c = 0
            b += 1
        if b > 9:
            b = 0
            a += 1
        if a > 9:
            break
    
    # Run BFS and find shortest path, if one exists
    g.bfs(start)
    g.find_path(start, end)
    
    # Return path length, if one exists
    if g.path:
        return len(g.path)-1
    else:
        return None
            
        
        


# Driver code
print(wheels('8056', '6508', ['8057', '8047', '5508', '7508', '6408']))
print(wheels('0000', '5317', ['0001', '0009', '0010', '0090', '0100', '0900', '1000', '9000']))

