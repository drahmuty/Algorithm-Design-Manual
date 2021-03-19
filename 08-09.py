"""Knapsack problem. Given a set S and total sum T, find a subset that adds up to exactly T."""



def knapsack(S, T):
    S = [None] + S
    n = len(S)
    k = T + 1

    M = [[0 for i in range(k)] for i in range(n)]
    P = [[0 for i in range(k)] for i in range(n)]

    for i in range(1, n):
        for j in range(1, k):
            M[i][j] = M[i-1][j]
            P[i][j] = j
            if S[i] <= j:
                parent_value = M[i-1][j-S[i]]
                if parent_value + S[i] > parent_value:
                    M[i][j] = parent_value + S[i]
                    P[i][j] = parent_value

    subset = []
    
    while i > 0 and j > 0:
        print(S[i], j)
        if S[i] > j:
            i -= 1
        elif M[i][j] == j:
            subset.append(S[i])
            j -= S[i]
            i -= 1
        else:
            i -= 1

    if j > 0:
        subset = []

    return subset
    
        
      
s = [1,2,5,9,10]      
knapsack(s, 22)
knapsack(s, 23)
