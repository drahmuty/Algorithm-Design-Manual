# ATTEMP 2: USING DYNAMIC PROGRAMMING.

def sort_key(x):
    weight, iq, num = x
    return weight * 10000 - iq


def sort_elephants(elephants):

    n = len(elephants) + 1

    # Add number to each elephant.
    for i in range(n - 1):
        elephants[i].append(i + 1)

    # Sort the elephants by decreasing weight and increasing iq.
    elephants_sorted = sorted(elephants, reverse=True, key=sort_key)

    # Add empty value to beginning of elephants list
    # for easier indexing. 
    elephants_sorted = [None] + elephants_sorted

    # Solution arrays.
    A = [1] * n
    A[0] = 0
    P = [None] * n

    # Find max length for each possible ordering.
    max_length = 0
    max_index = 0
    for i in range(1, n):
        current_weight, current_iq, current_num = elephants_sorted[i]
        current_cost = A[i]

        for j in range(i + 1, n):
            next_weight, next_iq, next_num = elephants_sorted[j]
            next_cost = A[j]

            if next_weight >= current_weight or next_iq <= current_iq:
                continue

            if current_cost >= next_cost:
                A[j] = current_cost + 1
                P[j] = i

                if current_cost + 1 > max_length:
                    max_length = current_cost + 1
                    max_index = j
    
    print('Max:', max_length)
    
    # Get solution ordering.
    while max_index:
        weight, iq, num = elephants_sorted[max_index]
        print(num, weight, iq)
        max_index = P[max_index]


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

sort_elephants(elephants)





# ATTEMPT 1: USING GRAPH DFS AND MEMOIZATION.

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
