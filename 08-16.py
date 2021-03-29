"""
City streets are defined as X by Y grid. 
Find if a path exists from upper left corner to lower right corner.
Avoid "bad" intersections.

Part 1) Find a path ('city_path' function).
Part 2) Find shortest path ('shortest_city_path' function).
"""

def city_path(x, y, bad):
    
    # Init bad intersection matrix.
    B = [[False for i in range(y+1)] for i in range(x+1)]
    for b in bad:
        B[b[0]][b[1]] = True
    
    # Init solution matries.
    M = [[False for i in range(y+1)] for i in range(x+1)]
    P = [[None for i in range(y+1)] for i in range(x+1)]

    # Fill in dynamic matrix via BFS.
    queue = [(1, 1)]
    while queue:

        # Get current intersection (vertex).
        v = queue.pop(0)
        i = v[0]
        j = v[1]

        # Skip bad intersections, otherwise mark true.
        if B[i][j]:
            P[i][j] = 'BAD'
            continue
        else:
            # Mark starting vertex as root.
            if i == 1 and j == 1:
                P[i][j] = 'ROOT'
            M[i][j] = True
                
        # Look right.
        if j < y and P[i][j+1] is None:
            queue.append((i, j+1))
            P[i][j+1] = v

        # Look down.
        if i < x and P[i+1][j] is None:
            queue.append((i+1, j))
            P[i+1][j] = v
        
        # Look left.
        if j > 1 and P[i][j-1] is None:
            queue.append((i, j-1))
            P[i][j-1] = v
        
        # Look up.
        if i > 1 and P[i-1][j] is None:
            queue.append((i-1, j))
            P[i-1][j] = v

    # Find path.
    path = []
    i = x
    j = y
    while M[i][j]:
        path = [(i, j)] + path
        v = P[i][j]
        if v == 'ROOT':
            break
        i = v[0]
        j = v[1]
    
    print(path)
    return path



# Test cases.
x = 5
y = 5
bad = [
    (1,2),
    (2,2),
    (3,2),
    (4,2),
    (2,4),
    (3,4),
    (4,4),
    (5,4,)
]
city_path(x, y, bad)




def shortest_city_path(x, y, bad):
    
    # Init "bad" intersection matrix.
    B = [[False for i in range(y+1)] for i in range(x+1)]
    for b in bad:
        B[b[0]][b[1]] = True
    
    # Init solution matries.
    M = [[float('inf') for i in range(y+1)] for i in range(x+1)]
    P = [[None for i in range(y+1)] for i in range(x+1)]

    # Fill in dynamic matrix via BFS.
    queue = [(1, 1)]
    while queue:

        # Get current intersection (vertex).
        v = queue.pop(0)
        i = v[0]
        j = v[1]

        # Skip "bad" intersections.
        if B[i][j]:
            P[i][j] = None
            continue

        # Handle start intersection.
        if i == 1 and j == 1:
            P[i][j] = 'START'
            M[i][j] = 1

        # Get cost of next move.
        cost = M[i][j] + 1
                
        # Look right.
        if j < y and not B[i][j+1] and cost < M[i][j+1]:
            queue.append((i, j+1))
            M[i][j+1] = cost
            P[i][j+1] = v

        # Look down.
        if i < x and not B[i+1][j] and cost < M[i+1][j]:
            queue.append((i+1, j))
            M[i+1][j] = cost
            P[i+1][j] = v
        
        # Look left.
        if j > 1 and not B[i][j-1] and cost < M[i][j-1]:
            queue.append((i, j-1))
            M[i][j-1] = cost
            P[i][j-1] = v
        
        # Look up.
        if i > 1 and not B[i-1][j] and cost < M[i-1][j]:
            queue.append((i-1, j))
            M[i-1][j] = cost
            P[i-1][j] = v

    total_cost =  M[i][j]

    # Find path.
    path = []
    i = x
    j = y
    while P[i][j]:
        path = [(i, j)] + path
        v = P[i][j]
        if v == 'START':
            break
        i = v[0]
        j = v[1]
    
    print('Shortest path cost:', total_cost)
    print('Shortest path:')
    for p in path:
        print(p)

    return total_cost, path


# Test cases.
x = 5
y = 10
bad = [
    (1,2),
    (2,2),
    (3,2),
    (4,2),
    (2,4),
    (3,4),
    (4,4),
    (5,4)
]
shortest_city_path(x, y, bad)
