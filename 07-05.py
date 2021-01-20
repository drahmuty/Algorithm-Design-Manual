"""Subgraph isomorphism."""


from collections import defaultdict

def backtrack(a, k, data):
    if is_a_solution(a, k, data):
        process_solution(a, k, data)
    else:
        k += 1
        candidates = construct_candidates(a, k, data)
        for c in candidates:
            a[k] = c
            x, y = c[0], c[1]
            data.remove_edge(x, y)
            backtrack(a, k, data)
            a[k] = None
            data.add_edge(x, y)

def is_a_solution(a, k, data):
    return k == len(a)-1

def process_solution(a, k, data):
    iso.isomorphic_test(G, data)

def construct_candidates(a, k, data):
    c = []
    prev_a = a[k-1]
    prev_c = None
    in_sol = defaultdict(bool)
    for i in a:
        in_sol[i] = True
    for i in range(len(EDGES)):
        curr = EDGES[i]
        if not in_sol[curr]:
            if not prev_a:
                c.append(curr)
                prev_c = curr
            elif not prev_c and prev_a[0] <= curr[0] and prev_a[1] <= curr[1]:
                c.append(curr)
                prev_c = curr
            elif prev_c and prev_c[0] <= curr[0] and prev_c[1] <= curr[1]:
                c.append(curr)
                prev_c = curr
    return c




def sub_isomporhic_test(a, b):
    
    if len(b.graph) < len(a.graph):
        return False

    edge_diff = b.edges - a.edges

    if edge_diff == 0:
        iso.isomorphic_test(a, b)
        return
    elif edge_diff < 0:
        return False

    sol_arr = [None for i in range(edge_diff+1)]

    global G
    G = a

    global EDGES
    EDGES = []
    for v in b.graph:
        for y in b.graph[v]:
            if v < y:
                EDGES.append((v, y))
    EDGES.sort()

    backtrack(sol_arr, 0, b)






# Test cases
a = iso.Graph()
a.add_edge(1,2)
a.add_edge(2,3)
a.add_edge(3,1)
a.add_edge(3,4)


b = iso.Graph()
b.add_edge(4,3)
b.add_edge(1,3)
b.add_edge(3,2)
b.add_edge(2,1)
b.add_edge(4,5)
b.add_edge(5,6)
b.add_edge(4,6)
b.add_edge(6,7)


sub_isomporhic_test(a, b)
