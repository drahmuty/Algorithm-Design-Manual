"""Bandwidth minimization."""



from collections import defaultdict



# Matrix representation of a graph.
class Graph:
    
    def __init__(self, n):
        self.n_vertices = n
        self.n_edges = 0
        self.graph = [[0 for i in range(n)] for i in range(n)]

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



# Find the max edge length in a linear ordering of vertices.
def max_distance(line, graph):
    max = 0
    k = len(line)
    for i in range(k-1):
        x = line[i]
        for j in range(i+1, k):
            y = line[j]
            if graph.graph[x-1][y-1]:
                d = j - i
                if d > max:
                    max = d
    return max



# Backtracking algorithm and helper functions.
def backtrack(a, k, data):
    if is_a_solution(a, k, data):
        process_solution(a, k, data)
    else:
        k += 1
        candidates = construct_candidates(a, k, data)
        for c in candidates:
            a[k] = c
            backtrack(a, k, data)
            a[k] = None

def is_a_solution(a, k, data):
    return k == len(a)-1

def process_solution(a, k, data):
    solution = a[1:]
    print(solution)
    print(max_distance(solution, data))

def construct_candidates(a, k, data):
    candidates = []
    in_sol = defaultdict(bool)
    for i in range(1, k):
        in_sol[a[i]] = True
    for i in range(len(data.graph)):
        if not in_sol[i+1]:
            candidates.append(i+1)
    return candidates







# a = Graph(8)
# a.add_edge(1,8)
# a.add_edge(8,2)
# a.add_edge(2,7)
# a.add_edge(7,3)
# a.add_edge(3,6)
# a.add_edge(6,4)
# a.add_edge(4,5)
# a.print()
# backtrack([None for i in range(9)], 0, a)


# b = Graph(5)
# b.add_edge(1,2)
# b.add_edge(1,3)
# b.add_edge(1,4)
# b.add_edge(1,5)
# b.print()

c = Graph(4)
c.add_edge(1,2)
c.add_edge(1,3)
c.add_edge(1,4)
c.print()
backtrack([None for i in range(5)], 0, c)
