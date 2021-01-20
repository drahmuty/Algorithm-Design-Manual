"""Subgraph isomorphism."""


# Import the isomorphic test solution from file "07-03.py"
# In this file I refer to it as "iso" (see import below).

import iso
from collections import defaultdict


# Backtrack function to generate all subsets of a graph
# by removing an arbitary number of edges.
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

            
# Check if graph has the correct number of edges removed.
def is_a_solution(a, k, data):
    return k == len(a)-1


# Run isomorphic test for current graph.
def process_solution(a, k, data):
    iso.isomorphic_test(G, data)

    
# Generate possible remaining edges to remove. 
# To eliminate duplicate permutations, only allow edges in
# ascending order. This is what the series of conditional
# statements accomplish in the lower half of the function.
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
            # If this is the very first item.
            if not prev_a:
                c.append(curr)
                prev_c = curr
            # If this is the first item in this round of constructing
            # candidates then make sure its greater than the most recent
            # candidate present in the current solution.
            elif not prev_c and prev_a[0] <= curr[0] and prev_a[1] <= curr[1]:
                c.append(curr)
                prev_c = curr
            # Add all remaining candidates in ascending order.
            elif prev_c and prev_c[0] <= curr[0] and prev_c[1] <= curr[1]:
                c.append(curr)
                prev_c = curr
    return c


# Main program - Test for subgraph isomorphism.
def sub_isomporhic_test(a, b):
    
    # Make sure b has at least as many vertices as a.
    if len(b.graph) < len(a.graph):
        return False
    
    # Make sure b has ad least as many edges as a.
    edge_diff = b.edges - a.edges
    if edge_diff == 0:
        iso.isomorphic_test(a, b)
        return
    elif edge_diff < 0:
        return False

    sol_arr = [None for i in range(edge_diff+1)]

    # Global graph of a to use for comparison when calling the 
    global G
    G = a

    # Create a sorted list of graph b's edges.
    global EDGES
    EDGES = []
    for v in b.graph:
        for y in b.graph[v]:
            if v < y:
                EDGES.append((v, y))
    EDGES.sort()

    # Generate all subgraphs of graph b and test if any are
    # isomorphic to graph a.
    backtrack(sol_arr, 0, b)
    print("Done")

# --------------------------------------------------------------------------------

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
