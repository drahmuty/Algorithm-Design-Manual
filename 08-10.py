# If M is odd, return None
# If n < 2, return None
# Construct n x M/2 matrix
# If sum does not equal M/2, return None
# Else identify items that add up to M/2 for one subset
#   and remaining items are in the other subset

from collections import defaultdict

def int_partition(S):

    n = len(S)
    m = sum(S)
    
    if m % 2 == 1:
        return None
    if n < 2:
        return None

    half_m = m//2
    
    M = [[0 for i in range(half_m+1)] for i in range(n+1)]

    for i in range(1, n+1):
        for j in range(1, half_m+1):
            M[i][j] = M[i-1][j]
            if S[i-1] <= j:
                M[i][j] = max(M[i][j], M[i-1][j-S[i-1]] + S[i-1])

    # for i in range(n+1):
    #     print(M[i])

    if M[i][j] != half_m:
        return None

    p1 = defaultdict(int)
    p2 = defaultdict(int)
    for i in range(n):
        p1[S[i]] += 1

    while i > 0 and j > 0:
        if S[i-1] > j:
            i -= 1
        elif M[i][j] == j:
            p1[S[i-1]] -= 1
            p2[S[i-1]] += 1
            j -= S[i-1]
            i -= 1
        else:
            i -= 1

    s1, s2 = [], []
    for k in p1:
        if p1[k] > 0:
            while p1[k] > 0:
                s1.append(k)
                p1[k] -= 1
        if p2[k] > 0:
            while p2[k] > 0:
                s2.append(k)
                p2[k] -= 1

    return s1, s2



print(int_partition([1,2,3,4,2,12]))
