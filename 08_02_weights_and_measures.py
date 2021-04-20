"""
Find maximum stack height of turtles of given weights and strength.
Full problem description: https://onlinejudge.org/external/101/10154.pdf
"""


def turtles(T):

    # Sort T by decreasing weight and strength.
    T.sort(reverse=True, key=lambda x: (x[0], x[1]))
    
    # Add empty item to T for easier indexing.
    T = [None] + T
    n = len(T)

    # Dynamic solution list.
    C = [0] * n

    # Main loop.
    for i in range(1, n):
        weight = T[i][0]
        carrying_capacity = T[i][1] - weight
        # Skip turtles that can't carry their own weight.
        if carrying_capacity < 0:
            continue
        C[i] = max(C[i], 1)
        for j in range(i - 1, 0, -1):
            weight += T[j][0]
            carrying_capacity = T[j][1] - weight
            # Skip turtles that can't carry the total weight.
            if carrying_capacity < 0:
                continue
            # Choose option with larger stack height.
            C[i] = max(C[i], C[j] + 1)            

    return max(C)




# Test case.
T = [
    (300, 1000),
    (1000, 1200),
    (200, 600),
    (100, 101),
]
print(turtles(T))
