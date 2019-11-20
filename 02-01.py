def mystery(n):
    r = 0
    for i in range(1, n-1):
        for j in range(i+1, n):
            for k in range(1, j):
                r += 1
    return r
