"""Knapsack problem. Given a set S and total sum T, find a subset that adds up to exactly T."""



def knapsack(S, T):
    S = [None] + S
    n = len(S)
    k = T + 1

    M = [[0 for i in range(k)] for i in range(n)]

    for i in range(1, n):
        for j in range(1, k):
            M[i][j] = M[i-1][j]
            if S[i] <= j and M[i-1][j-S[i]] + S[i] > M[i][j]:
                M[i][j] = M[i-1][j-S[i]] + S[i]

    subset = []
    
    while i > 0 and j > 0:
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
    
        
      
s = [1,2,3,4,5]      
knapsack(s, 6)
knapsack(s, 12)
