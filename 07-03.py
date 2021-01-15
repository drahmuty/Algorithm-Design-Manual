"""Test whether two graphs are isomorphic to each other."""


# ROUGH DRAFT / INCOMPLETE


from collections import defaultdict


# Graph adjacency list representation.
class Graph:

    def __init__(self, directed=False):
        self.graph = defaultdict(list)
        self.degree = defaultdict(int)
        self.label = defaultdict(int)
        self.next_label = 1
        self.directed = directed
        self.edges = 0
    
    def add_edge(self, x, y, go=True):
        self.graph[x].append(y)
        self.degree[x] += 1
        self.edges += 1
        self.graph[y]        
        if go and not self.directed:
            self.edges -= 1
            self.add_edge(y, x, False)
    
    def remove_edge(self, x, y, go=True):
        self.graph[x].remove(y)
        self.degree[x] -= 1
        self.edges -= 1
        if go and not self.directed:
            self.edges += 1
            self.remove_edge(y, x, False)


# Backtracking algorithm.
def backtrack(a, k, data):
    if is_a_solution(a, k, data):
        process_solution(a, k, data)
    else:
        k += 1
        # print("k:", k)
        candidates = construct_candidates(a, k, data)
        # print("c:", candidates)
        for c in candidates:
            a[k] = c
            # print("a:", a)
            backtrack(a, k, data)
            a[k] = None


# Construct candidates helper function.
def construct_candidates(a, k, data):
    in_solution = defaultdict(bool)
    for i in a:
        in_solution[i] = True

    c = []

    # Get last vertex added to graph.
    if k == 1:
        # print("first")
        return data[1:]
    else:
        v = a[k-1]

    # print("v:", v)

    # Get expected degree.
    d = g1.degree[g1_vertices[k-1]]

    # Consider potential neighbors of v.
    for u in g2.graph[v]:
        if not in_solution[u]:
            c.append(u)
    return c


# Is a solution helper function.
def is_a_solution(a, k, data):
    return k == len(g1.graph)


# Process solution helper function.
def process_solution(a, k, data):
    print("SOLUTION:", a[1:])
    return True


# Get a list of degrees for each vertex in a graph.
def get_degrees(g):
    degrees = []
    for v in g.graph.keys():
        degrees.append(g.degree[v])
    degrees.sort()
    return degrees


# Main program.
def isomorphic_test(a, b):

    print(a.graph)
    print(b.graph)

    # Test for equal number of vertices.
    if len(a.graph) != len(b.graph):
        print("length")
        return False

    # Test for equal number of edges.
    if a.edges != b.edges:
        print("edges")
        return False

    # Test for equal number of degrees by vertex.
    a_degrees = get_degrees(a)
    b_degrees = get_degrees(b)
    for i in range(len(a_degrees)):
        if a_degrees[i] != b_degrees[i]:
            print("degrees")
            return False

    global g1
    global g2
    g1, g2, = a, b

    global g1_vertices
    g1_vertices = [None]
    for v in g1.graph:
        g1_vertices.append(v)

    g2_vertices = [None]
    for v in g2.graph:
        g2_vertices.append(v)

    a = [None for i in range(len(g1.graph)+1)]
        
    backtrack(a, 0, g2_vertices)


# --------------------------------------------------------------------------------


# Test cases
a = Graph()
a.add_edge(1,2)
a.add_edge(2,3)
a.add_edge(3,4)
a.add_edge(3,1)

b = Graph()
b.add_edge(3,1)
b.add_edge(3,4)
b.add_edge(2,3)
b.add_edge(1,2)

isomorphic_test(a, b)
