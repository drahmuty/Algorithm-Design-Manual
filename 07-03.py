"""Test whether two graphs are isomorphic to each other."""


# ROUGH DRAFT / INCOMPLETE


from collections import defaultdict


# Graph adjacency list representation.
class Graph:

    def __init__(self, directed=False):
        self.graph = defaultdict(list)
        self.degree = defaultdict(int)
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


# --------------------------------------------------------------------------------


# Backtracking algorithm.
def backtrack(a, k, data):
    if is_a_solution(a, k, data):
        process_solution(a, k, data)
    else:
        k += 1
        candidates = construct_candidates(a, k, data)
        for c in candidates:
            a.add_edge(k, c)
            backtrack(a, k, data)
            a.remove_edge(k, c)


# Construct candidates helper function.
def construct_candidates(a, k, data):
    in_solution = defaultdict(bool)
    for i in a.keys():
        in_solution[i] = True
    c = []
    for i in data.keys():
        if not in_solution[i]:
            c.append(i)
            in_solution[i]
    return c


# Is a solution helper function.
def is_a_solution(a, k, data):
    return len(a.graph) == len(g1.graph)


# Process solution helper function.
def process_solution(a, k, data):
    print(a.graph)


# Main program.
def isomorphic_test(a, b):
    global g1
    global g2
    g1, g2, = a, b
    backtrack(Graph(), 0, g2)


# --------------------------------------------------------------------------------


# Test cases
a = Graph()
a.add_edge(1,2)
a.add_edge(2,3)
a.add_edge(3,4)
a.add_edge(4,1)

b = Graph()
a.add_edge(1,2)
a.add_edge(2,3)
a.add_edge(3,4)
a.add_edge(4,1)

isomorphic_test(a, b)
