from collections import defaultdict
import math



# Connect a series of freckles using the least amount of ink
# Input is a list of (x,y) coordinates representing freckle location
# Output is total amount of ink needed (i.e. MST weight)
def freckles(items):
    
    # Number of vertices
    n = len(items)

    # Init graph
    graph = defaultdict(list)

    # Add edges to graph
    for i in range(n):
        for j in range(i+1, n):
            # Calculate weight and add to graph
            v1, v2 = items[i], items[j]
            x1, y1 = v1[0], v1[1]
            x2, y2 = v2[0], v2[1]
            w = round(math.sqrt(abs(x2-x1)**2 + abs(y2-y1)**2), 2)
            graph[v1].append((v2, w))
            graph[v2].append((v1, w))
    
    # Find MST
    mst = prim(graph, items[0])

    # Calculate total weight of MST
    mst_weight = 0
    for m in mst:
        p = mst[m]
        if p == -1: continue
        neighbors = graph[m]
        for i in neighbors:
            if i[0] == p:
                mst_weight += i[1]
                break
    
    # Return total weight of MST
    return round(mst_weight, 2)



# Prim's algorithm to compute MST
def prim(graph, start):

    # Init dictionaries
    intree = defaultdict(bool)
    parent = defaultdict(int)
    distance = defaultdict(int)
    for v in graph:
        distance[v] = float('inf')

    # Init start vertex
    parent[start] = -1
    distance[start] = 0
    v = start

    # Main loop
    while(not intree[v]):
        intree[v] = True
        neighbors = graph[v]

        # Update distance to neighbor vertices
        for neighbor in neighbors:
            y = neighbor[0]
            w = neighbor[1]
            if not intree[y] and w < distance[y]:
                distance[y] = w
                parent[y] = v
        
        # Select nearest vertex
        v = 1
        dist = float('inf')
        for i in graph:
            if not intree[i] and distance[i] < dist:
                dist = distance[i]
                v = i
    
    # Return MST represented as dictionary of parent vertices
    return parent



# Test cases
print(freckles([(1,1), (2,2), (2,4)]))
print(freckles([(0,0), (1,2), (2,1)]))
print(freckles([(0,0), (1,2), (1,5), (2,1), (3,4), (4,5), (5,2), (6,3)]))
