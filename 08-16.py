def is_city_path(x, y, bad):
    
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
    
    for row in M:
        print(row)
    print()
    for row in P:
        print(row)
    print()

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
print(is_city_path(x, y, bad))
