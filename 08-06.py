def min_coins(n, denoms):
    k = len(denoms)
    C = [float('inf') for i in range(n+1)]
    P = [None for i in range(n+1)]
    for i in range(n+1):
        if i == 0:
            C[i] = 0
        for j in range(k):
            d = denoms[j]
            if d <= i and C[i-d] + 1 < C[i]:
                C[i] = C[i-d] + 1
                P[i] = d

    # print(C)
    # print(P)

    coins = []
    while C[n] < float('inf') and i > 0:
        coins.append(P[i])
        i = i - P[i]

    return C[n], coins

print(min_coins(99, [1,5,10,25]))
