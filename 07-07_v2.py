"""Minimum bandwidth, version 2."""


import time
import math
from collections import defaultdict


class Graph:

    def __init__(self, n):
        self.graph = [[0 for i in range(n)] for i in range(n)]

    def print(self):
        for i in self.graph:
            print(i)

    def add_edge(self, x, y):
        self.graph[x - 1][y - 1] = 1
        self.graph[y - 1][x - 1] = 1

    def get_vertices_list(self):
        return [i+1 for i in range(len(self.graph))]

    # Get largest minimum bandwidth.
    def get_min_bandwidth(self):
        min = None
        for v in self.graph:
            degree = 0
            for y in v:
                degree += y
            total = math.ceil(degree / 2)
            if not min or total > min:
                min = total
            if min == 1:
                break
        return min

    
class Solution:

    def __init__(self, graph):
        self.g = graph
        self.n = len(self.g.graph)
        self.upper_bound = self.n - 1
        self.lower_bound = self.g.get_min_bandwidth()
        self.current_solution = [None for i in range(self.n + 1)]
        self.current_bandwidth = defaultdict(int)
        self.current_position = defaultdict(int)
        self.skip = defaultdict(bool)
        self.best_solution = None
        self.best_bandwidth = self.n
        self.done = False

    def bandwidth(self, x):
        bandwidth = 0
        for i in range(self.n):
            y = i + 1
            if self.g.graph[x - 1][y - 1] and self.current_position[y]:
                d = self.current_position[x] - self.current_position[y]
                if not bandwidth or d > bandwidth:
                    bandwidth = d
        return bandwidth

    def add_bandwidth(self, k):
        x = self.current_solution[k]
        new_bandwidth = self.bandwidth(x)
        old_bandwidth = self.current_bandwidth[k - 1]
        if new_bandwidth > old_bandwidth:
            self.current_bandwidth[k] = new_bandwidth
        else:
            self.current_bandwidth[k] = old_bandwidth

    def del_bandwidth(self, k):
        self.current_bandwidth[k] = 0

        
def backtrack(a, k, data):
    # print(k, '\t', a.current_solution)
    if is_a_solution(a, k, data):
        process_solution(a, k, data)
    else:
        k += 1
        candidates = construct_candidates(a, k, data)
        for c in candidates:
            a.current_solution[k] = c
            a.current_position[c] = k
            a.add_bandwidth(k)
            backtrack(a, k, data)
            a.current_solution[k] = None
            a.current_position[c] = None
            a.del_bandwidth(k)
            a.skip[k] = defaultdict(bool)
            if a.done:
                return

            
def is_a_solution(a, k, data):
    return k == a.n


def process_solution(a, k, data):
    if not a.best_solution or a.current_bandwidth[k] < a.best_bandwidth:
        a.best_solution = a.current_solution.copy()
        a.best_bandwidth = a.current_bandwidth[k]
        # print('NEW BEST SOLUTION:', a.best_solution, a.best_bandwidth)
    if a.best_bandwidth == a.lower_bound or a.lower_bound == a.upper_bound:
        # print('FOUND LOWER BOUND')
        a.done = True

        
def construct_candidates(a, k, data):
    candidates = []
    for x in data:
        if not a.current_position[x]:
            a.current_position[x] = k
            if a.skip[x] or a.bandwidth(x) >= a.best_bandwidth:
                a.skip[x] = True
                a.current_position[x] = None
                return []
            else:
                candidates.append(x)
                a.skip[x] = False
                a.current_position[x] = None
    return candidates


def build_graph_from_file(filename):
    with open(filename) as file_obj:
        data = file_obj.readlines()
    n = int(data[1])
    g = Graph(n)
    for i in range(2, len(data)):
        x = int(data[i].split(' ')[0])
        y = int(data[i].split(' ')[1])
        g.add_edge(x, y)
    return g


def min_bandwidth(graph):
    solution = Solution(graph)
    vertices_list = graph.get_vertices_list()
    backtrack(solution, 0, vertices_list)
    print('SOLUTION:\t', solution.best_solution[1:])
    print('BANDWIDTH:\t', solution.best_bandwidth)
    return solution.best_solution, solution.best_bandwidth


def min_bandwidth_file_input(file):
    start_time = time.time()
    graph = build_graph_from_file(file)
    min_bandwidth(graph)
    print('Running time:', time.time() - start_time)



# TEST CASES.
min_bandwidth_file_input('01.txt')

# a = Graph(5)
# a.add_edge(1, 2)
# a.add_edge(1, 3)
# a.add_edge(1, 4)
# a.add_edge(1, 5)
# min_bandwidth(a)

# c = Graph(8)
# c.add_edge(1,8)
# c.add_edge(8,2)
# c.add_edge(2,7)
# c.add_edge(7,3)
# c.add_edge(3,6)
# c.add_edge(6,4)
# c.add_edge(4,5)
# min_bandwidth(c)
