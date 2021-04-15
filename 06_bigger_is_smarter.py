def elephant_order(E):

    # Add extra value to E for easier indexing into array.
    E = [None] + E
    n = len(E)
    
    # Create directed graph of possible orderings.
    G = [[0] * n for i in range(n)]
    for i in range(1, n):
        for j in range(1, n):
            if i == j:
                continue
            if E[i][0] < E[j][0] and E[i][1] > E[j][1]:
                G[i][j] = 1

    # Depth from each elephant.
    D = [0] * n
    max_depth = 0
    first_elephant = None

    # Parent vertex list.
    P = [None] * n

    # Find max depth using dynamic DFS.
    i = 1
    while i < n:
        if D[i] > 0:
            if D[i] > max_depth:
                max_depth = D[i]
                first_elephant = i
            i += 1
        else:
            D, P = dfs_max_depth(i, G, D, P, n)
    
    # Get elephant order.
    elephant_order = []
    while first_elephant:
        elephant_order.append(first_elephant)
        first_elephant = P[first_elephant]
    
    print('Depth:', max_depth)
    print('Order:', elephant_order)



def dfs_max_depth(v, G, D, P, n):
    if D[v] == 0:
        D[v] = 1
    w = 1
    while w < n:
        if G[v][w] == 0:
            w += 1
        elif D[w] > 0:
            if D[w] + 1 > D[v]:
                D[v] = D[w] + 1
                P[v] = w
            w += 1
        else:
            D, P = dfs_max_depth(w, G, D, P, n)
    return D, P




elephants = [
    [6008, 1300],
    [6000, 2100],
    [500, 2000],
    [1000, 4000],
    [1100, 3000],
    [6000, 2000],
    [8000, 1400],
    [6000, 1200],
    [2000, 1900]
]
elephant_order(elephants)
