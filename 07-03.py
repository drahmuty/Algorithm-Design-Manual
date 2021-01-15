"""Test whether two graphs are isomorphic to each other."""


from collections import defaultdict


# Graph adjacency list representation.
class Graph:

    def __init__(self, directed=False):
        self.graph = defaultdict(list)
        self.degree = defaultdict(int)
        self.seen = defaultdict(bool)
        self.directed = directed
        self.edges = 0
        self.dfs_list = [None]
    
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

    # Simple DFS function used to create a list of 
    # vertices in order of discovery.
    def dfs(self):
        for v in self.graph.keys():
            if not self.seen[v]:
                self.dfs_recur(v)
    
    def dfs_recur(self, v):
        if self.seen[v]:
            return
        self.seen[v] = True
        self.dfs_list.append(v)
        for y in self.graph[v]:
            self.dfs_recur(y)


# Backtracking algorithm.
def backtrack(a, k, data):
    result = False
    if is_a_solution(a, k, data):
        result = process_solution(a, k, data)
    else:
        k += 1
        candidates = construct_candidates(a, k, data)
        for c in candidates:
            a[k] = c
            result = backtrack(a, k, data)
            a[k] = None
    return result

# Construct candidates helper function.
def construct_candidates(a, k, data):

    # Mark items already in solution.
    in_solution = defaultdict(bool)
    for i in a:
        in_solution[i] = True

    # Get expected degree for current slot.
    d = g1.degree[model[k]]    

    # Init candidates list.
    c = []

    # For first position, pick any vertex with the expected number of degrees.
    if k == 1:
        for y in data[1:]:
            if g2.degree[y] == d:
                c.append(y)
    
    # For all other positions, return neighbors of the previous vertex.
    else:
        v = a[k-1]
        for y in g2.graph[v]:
            if not in_solution[y] and g2.degree[y] == d:
                c.append(y)

    # If no more connected vertices, search for new vertices to start from.    
    if len(c) < 1:        
        for y in data[1:]:
            if not in_solution[y] and g2.degree[y] == d:
                c.append(y)

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
def isomorphic_test(graph1, graph2):

    global g1
    global g2
    g1, g2, = graph1, graph2

    print(g1.graph)
    print(g2.graph)

    # Test for equal number of vertices.
    if len(g1.graph) != len(g2.graph):
        print("Unequal number of vertices.")
        return False

    # Test for equal number of edges.
    if g1.edges != g2.edges:
        print("Unequal number of edges.")
        return False

    # Test for equal number of degrees by vertex.
    g1_degrees = get_degrees(g1)
    g2_degrees = get_degrees(g2)
    for i in range(len(g1_degrees)):
        if g1_degrees[i] != g2_degrees[i]:
            print("Unequal number of degrees per edge.")
            return False

    global g1_vertices
    g1_vertices = [None]
    for v in g1.graph:
        g1_vertices.append(v)

    g2_vertices = [None]
    for v in g2.graph:
        g2_vertices.append(v)

    a = [None for i in range(len(g1.graph)+1)]
    
    # Create model to test against.
    g1.dfs()
    global model
    model = g1.dfs_list
    print("Model:", model[1:])
        
    return backtrack(a, 0, g2_vertices)


# --------------------------------------------------------------------------------


# Test cases
a = Graph()
a.add_edge(1,2)
a.add_edge(2,3)
a.add_edge(3,1)
a.add_edge(3,4)


b = Graph()
b.add_edge(4,3)
b.add_edge(1,3)
b.add_edge(3,2)
b.add_edge(2,1)
b.add_edge(4,5)

isomorphic_test(a, b)


# --------------------------------------------------------------------------------



"""
The code below is an earlier brainstorm as I was attempting to solve the above problem. 
The algorithm finds all paths through a given graph that goes through each vertex once 
in a "straight line" (i.e. the path forms a tree of length n where n = number of vertices,
and contains only two endpoints). I don't know if it has any practical application or is 
even a correct algorithm (it's definitely not in a presentable form - I'd have to clean
it up), but I figured it was worth saving.
"""

# from collections import defaultdict


# # Graph adjacency list representation.
# class Graph:

#     def __init__(self, directed=False):
#         self.graph = defaultdict(list)
#         self.degree = defaultdict(int)
#         self.label = defaultdict(int)
#         self.next_label = 1
#         self.directed = directed
#         self.edges = 0
    
#     def add_edge(self, x, y, go=True):
#         self.graph[x].append(y)
#         self.degree[x] += 1
#         self.edges += 1
#         self.graph[y]        
#         if go and not self.directed:
#             self.edges -= 1
#             self.add_edge(y, x, False)
    
#     def remove_edge(self, x, y, go=True):
#         self.graph[x].remove(y)
#         self.degree[x] -= 1
#         self.edges -= 1
#         if go and not self.directed:
#             self.edges += 1
#             self.remove_edge(y, x, False)


# # Backtracking algorithm.
# def backtrack(a, k, data):
#     if is_a_solution(a, k, data):
#         process_solution(a, k, data)
#     else:
#         k += 1
#         # print("k:", k)
#         candidates = construct_candidates(a, k, data)
#         # print("c:", candidates)
#         for c in candidates:
#             a[k] = c
#             # print("a:", a)
#             backtrack(a, k, data)
#             a[k] = None


# # Construct candidates helper function.
# def construct_candidates(a, k, data):
#     in_solution = defaultdict(bool)
#     for i in a:
#         in_solution[i] = True

#     c = []

#     # Get last vertex added to graph.
#     if k == 1:
#         # print("first")
#         return data[1:]
#     else:
#         v = a[k-1]

#     # print("v:", v)

#     # Get expected degree.
#     d = g1.degree[g1_vertices[k-1]]

#     # Consider potential neighbors of v.
#     for u in g2.graph[v]:
#         if not in_solution[u]:
#             c.append(u)
#     return c


# # Is a solution helper function.
# def is_a_solution(a, k, data):
#     return k == len(g1.graph)


# # Process solution helper function.
# def process_solution(a, k, data):
#     print("SOLUTION:", a[1:])
#     return True


# # Get a list of degrees for each vertex in a graph.
# def get_degrees(g):
#     degrees = []
#     for v in g.graph.keys():
#         degrees.append(g.degree[v])
#     degrees.sort()
#     return degrees


# # Main program.
# def isomorphic_test(a, b):

#     print(a.graph)
#     print(b.graph)

#     # Test for equal number of vertices.
#     if len(a.graph) != len(b.graph):
#         print("length")
#         return False

#     # Test for equal number of edges.
#     if a.edges != b.edges:
#         print("edges")
#         return False

#     # Test for equal number of degrees by vertex.
#     a_degrees = get_degrees(a)
#     b_degrees = get_degrees(b)
#     for i in range(len(a_degrees)):
#         if a_degrees[i] != b_degrees[i]:
#             print("degrees")
#             return False

#     global g1
#     global g2
#     g1, g2, = a, b

#     global g1_vertices
#     g1_vertices = [None]
#     for v in g1.graph:
#         g1_vertices.append(v)

#     g2_vertices = [None]
#     for v in g2.graph:
#         g2_vertices.append(v)

#     a = [None for i in range(len(g1.graph)+1)]
        
#     backtrack(a, 0, g2_vertices)


# # --------------------------------------------------------------------------------


# # Test cases
# a = Graph()
# a.add_edge(1,2)
# a.add_edge(2,3)
# a.add_edge(3,4)
# a.add_edge(3,1)

# b = Graph()
# b.add_edge(3,1)
# b.add_edge(3,4)
# b.add_edge(2,3)
# b.add_edge(1,2)

# isomorphic_test(a, b)
