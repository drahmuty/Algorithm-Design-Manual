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
    


# Build graph
# For each cube
    # Compare to the rest of the cubes below it
        # For each face of cube1
            # For each face of cube2
                # If same color
                    # Add directed edge from cube1(opposite face) to cube2 face
def opposite_face(x):
    if x == 'front':
        return 'back'
    if x == 'back':
        return 'front'
    if x == 'left':
        return 'right'
    if x == 'right':
        return 'left'
    if x == 'top':
        return 'bottom'
    if x == 'bottom':
        return 'top'


def tower_of_cubes(cubes):

    # Create graph
    g = Graph(True)
    for i in range(len(cubes)):
        for j in range(i+1, len(cubes)):
            for k in cubes[i].faces:
                for l in cubes[j].faces:
                    if cubes[i].faces[k] == cubes[j].faces[l]:
                        g.add_edge((i, opposite_face(k)), (j, l))
    
    g.print_graph()

    # DFS

            
        




# For each undiscovered vertex
    # DFS


# Class representation of a cube
class Cube:
    def __init__(self, front, back, left, right, top, bottom):
        self.faces = {
            'front': front,
            'back': back,
            'left': left,
            'right': right,
            'top': top,
            'bottom': bottom
        }

d = [
    Cube(1,2,2,2,1,2),
    Cube(3,3,3,3,3,3),
    Cube(3,2,1,1,1,1)
]

e = [
    Cube(1,5,10,3,6,5),
    Cube(2,6,7,3,6,9),
    Cube(5,7,3,2,1,9),
    Cube(1,3,3,5,8,10),
    Cube(6,6,2,2,4,4),
    Cube(1,2,3,4,5,6),
    Cube(10,9,8,7,6,5),
    Cube(6,1,2,3,4,7),
    Cube(1,2,3,3,2,1),
]


# tower_of_cubes(c)
tower_of_cubes(d)
print()
tower_of_cubes(e)
