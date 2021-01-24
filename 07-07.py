"""Bandwidth minimization."""


import math
from collections import defaultdict

# Solution class.
class Solution:
    def __init__(self, n):
        self.solution = [None for i in range(n+1)]
        self.bandwidth = n-1
        self.solved = False
        self.final_solution = None

# Matrix representation of a graph.
class Graph:
    
    def __init__(self, n):
        self.n_vertices = n
        self.n_edges = 0
        self.graph = [[0 for i in range(n)] for i in range(n)]
        self.min_band = None
        self.max_band = n - 1

    def print(self):
        for i in self.graph:
            print(i)
    
    def add_edge(self, x, y):
        self.graph[x-1][y-1] = 1
        self.graph[y-1][x-1] = 1

    def remove_edge(self, x, y):
        pass

    def cost(self, x, y):
        pass

    # Get largest min bandwidth for graph vertices.
    # This value is the lower bound for the bandwidth solution.
    def get_min_band(self):
        min = None
        for v in self.graph:
            degree = 0
            for y in v:
                degree += y
            bandwidth = math.ceil(degree / 2)
            if not min or bandwidth > min:
                min = bandwidth
            if min == 1:
                break
        self.min_band = min
        return min

# Find the max bandwidth in a linear ordering of vertices.
def max_band(sol, graph):
    max = 0
    k = len(sol)
    for i in range(k-1, -1, -1):
        x = sol[i]
        for j in range(i-1, -1, -1):
            y = sol[j]
            if graph.graph[x-1][y-1]:
                b = i - j
                if b > max:
                    max = b
    return max

def backtrack(a, k, data):
    if a.solved:
        return
    if is_a_solution(a, k, data):
        process_solution(a, k, data)
    else:
        k += 1
        candidates = construct_candidates(a, k, data)
        for c in candidates:
            a.solution[k] = c
            backtrack(a, k, data)
            a.solution[k] = None

def is_a_solution(a, k, data):
    return k == len(a.solution)-1

def process_solution(a, k, data):
    solution = a.solution[1:]
    max = None
    k = len(solution)
    for i in range(k-1):
        x = solution[i]
        for j in range(i+1, k):
            y = solution[j]
            if data.graph[x-1][y-1]:
                d = j - i
                if not max or d > max:
                    max = d
                if max == MAX:
                    break
    if max == MIN or MIN == MAX:
        a.final_solution = solution
        a.bandwidth = max
        a.solved = True
    elif max < a.bandwidth:
        a.final_solution = solution
        a.bandwidth = max

def construct_candidates(a, k, data):
    partial_sol = a.solution[1:k]
    candidates = []
    in_sol = defaultdict(bool)
    for i in range(1, k):
        in_sol[a.solution[i]] = True
    for i in range(len(data.graph)):
        c = i+1
        if k == 1:
            candidates.append(c)
        elif not in_sol[c]:
            if partial_sol:
                p = partial_sol + [c]
                b = max_band(p, data)
                if b > a.bandwidth:
                    # print('skipping', c, '('+str(b)+' > '+str(a.bandwidth)+')')
                    continue
                candidates.append(c)
    return candidates

# MAIN PROGRAM - Find the minimum bandwidth of a graph.
def min_bandwidth(graph):

    print('GRAPH:')
    graph.print()

    global MIN, MAX
    MIN = graph.get_min_band()
    MAX = graph.max_band

    solution = Solution(graph.n_vertices)

    backtrack(solution, 0, graph)

    print('SOLUTION:', solution.final_solution)
    print('MAX BANDWIDTH:', solution.bandwidth)
    print()
    return solution.final_solution, solution.bandwidth



# Test cases.
a = Graph(4)
a.add_edge(1,2)
a.add_edge(1,3)
a.add_edge(1,4)
min_bandwidth(a)

b = Graph(5)
b.add_edge(1,2)
b.add_edge(1,3)
b.add_edge(1,4)
b.add_edge(1,5)
min_bandwidth(b)

c = Graph(8)
c.add_edge(1,8)
c.add_edge(8,2)
c.add_edge(2,7)
c.add_edge(7,3)
c.add_edge(3,6)
c.add_edge(6,4)
c.add_edge(4,5)
min_bandwidth(c)
