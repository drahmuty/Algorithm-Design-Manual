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
            if pve:
                pve(v)
            self.processed[v] = True
            for y in self.graph[v]:
                if not self.processed[y] or self.directed:
                    if pe:
                        pe(v, y)
                if not self.discovered[y]:
                    q.append(y)
                    self.discovered[y] = True
                    self.parent[y] = v
            if pvl:
                pvl(v)

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

    # Add edges to graph
    for i in range(0, len(words)):
        for j in range(i+1, len(words)):
            if is_edit_step(words[i], words[j]):
                g.add_edge(words[i], words[j])

    g.print_graph()

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

words = ['cat', 'hat', 'ham', 'him', 'tim', 'trim', 'grow', 'row', 'crow', 'crowd']
print(step_ladder(words))
