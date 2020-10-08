from collections import defaultdict, deque
    
# Adjacency list graph representation
class Graph:

    def __init__(self, directed=False):
        self.graph = defaultdict(list)
        self.degree = defaultdict(int)
        self.directed = directed
        self.n = 0                      # Number of vertices
        self.m = 0                      # Number of edges
        self.max_depth = 0
    
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
        self.depth = defaultdict(int)

    # Breadth-first search
    def bfs(self, v, pve=None, pe=None, pvl=None):
        q = deque()
        q.append(v)
        self.discovered[v] = True

        while(q):
            v = q.popleft()
            print('process vertex early', v)
            if pve:
                pve(v)
            self.processed[v] = True
            for y in self.graph[v]:
                if not self.processed[y] or self.directed:
                    print('process edge', v, y)
                    if pe:
                        pe(v, y)
                if not self.discovered[y]:
                    q.append(y)
                    self.discovered[y] = True
                    self.parent[y] = v
            print('process vertex late', v)
            if pvl:
                pvl(v)

    # Depth-first search
    def dfs(self, v, pve=None, pe=None, pvl=None):
        if self.finished:
            return
        self.discovered[v] = True
        self.time += 1
        self.entry_time[v] = self.time
        
        print('process vertex early', v)
        if pve:
            pve(v)
        
        for y in self.graph[v]:
            if not self.discovered[y]:
                self.parent[y] = v
                print('tree edge', v, y)
                if pe:
                    pe(v, y)
                self.dfs(y, pve, pe, pvl)
            elif not self.processed[y] or self.directed:
                if not self.directed:
                    print('back edge', v, y)
                else:
                    print('directed edge', v, y)
                if pe:
                    pe(v, y)
                if self.finished:
                    return

        print('process vertex late', v)
        if pvl:
            pvl(v)
        self.time += 1
        self.exit_time[v] = self.time
        self.processed[v] = True
    
    # Finding cycles
    def find_cycle(self, x, y):
        if self.parent[x] != y:
            print('cycle from', y, 'to', x)
            self.finished = True

    # Bipartite test
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
        if self.color[x] == 'BLACK':
            self.color[y] = 'WHITE'
        elif self.color[x] == 'WHITE':
            self.color[y] = 'BLACK'

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

    # Calculate graph depth
    def get_depth(self, v):
        if self.parent[v]:
            self.depth[v] = self.depth[self.parent[v]] + 1
        else:
            self.depth[v] = 1
        if self.depth[v] > self.max_depth:
            self.max_depth = self.depth[v]
    

# For each word
# Compare to remaining words for edit step match
# If edit step, add edge
# This runs in O(n-1 + n-2 +...+ 1) = O(2n) = O(n) 
# Do BFS to find the depth of the graph
# Runs in O(n+m) + O(n) = O(n+m)

def step_ladder(words):

    g = Graph()

    first_v = None

    # Add edges to graph
    for i in range(0, len(words)):
        for j in range(i+1, len(words)):
            if is_edit_step(words[i], words[j]):
                g.add_edge(words[i], words[j])
                if not first_v:
                    first_v = words[i]

    print(graph)

    # BFS through graph, starting at first word
    # Track vertex depth and max depth with custom
    # process vertext late funcion get_depth
    g.initialize_search()
    for word in words:
        if not g.discovered[word]:
            g.bfs(word, None, None, g.get_depth)

    # Return graph depth
    return g.max_depth


def is_edit_step(x, y):
    # This function determines if there is an edit step
    # between two words

    # Are x and y the same word?
    if x == y:
        return False

    # Get length of each word
    x_len = len(x)
    y_len = len(y)

    # x and y the same size
    if x_len == y_len:
        # Compare each letter
        # If more than one difference, return false
        diffs = 0
        for i in range(x_len):
            if x[i] != y[i]:
                diffs += 1
            if diffs > 1:
                return False
        return True

    # x bigger than y by exactly 1 letter
    elif x_len - y_len == 1:
        i = j = 0
        while j < y_len:
            if i - j > 1:
                return False
            elif x[i] == y[j]:
                i += 1
                j += 1
            else:
                i += 1
        return True

    # y bigger than x by exactly 1 letter
    elif y_len - x_len == 1:
        i = j = 0
        while j < x_len:
            if i - j > 1:
                return False
            elif y[i] == x[j]:
                i += 1
                j += 1
            else:
                i += 1        
        return True
    
    # More than 1 letter difference in size
    else:
        return False




# Driver code
words = ['cat', 'dig', 'dog', 'fig', 'fin', 'fine', 'fog', 'log', 'wine']
print(step_ladder(words))

print()

words = ['cat', 'hat', 'mat', 'sat', 'grow', 'row', 'crow', 'crowd', 'ham', 'sham']
print(step_ladder(words))
