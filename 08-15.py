"""Find minimum number of drops needed to test which floor an egg will break when dropped from."""

def egg_drop(e, f):
    
    # e is number of eggs
    # f is number of floors
    
    C = [[float('inf') for i in range(f+1)] for i in range(e+1)]
    P = [[0 for i in range(f+1)] for i in range(e+1)]

    for i in range(e+1):
        for j in range(f+1):
            if i == 0 or j == 0:
                C[i][j] = 0
            elif i == 1:
                C[i][j] = j
                P[i][j] = j
            elif j == 1:
                C[i][j] = 1
                P[i][j] = j
            else:
                for k in range(1, j+1):
                    cost = max(C[i][j-k], C[i-1][k-1]) + 1
                    if cost < C[i][j]:
                        C[i][j] = cost
                        P[i][j] = k
    
    return C[i][j]

print(egg_drop(2, 100))
