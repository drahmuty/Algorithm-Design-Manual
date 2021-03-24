"""Find the order to a cut string at given positions at minimum cost. Each cut of string size n costs n."""

# Input: Array of positions in string,
# including start (0) and end (total length)

# m = total string length (last position in array)
# n = number of cut points (array len minus 2)

# Make sure array is sorted in increasing order
# Create n x n matrix

def cut_string(P):
    P.sort()
    first = P[0]
    last = P[-1]

    n = len(P)
    
    M = [[float('inf') for i in range(n)] for i in range(n)]
    Z = [[0 for i in range(n)] for i in range(n)]

    i = 0
    j = 0
    start = 0
    while start < n:
        if i >= j - 1:
            M[i][j] = 0
        else:
            for k in range(i+1, j):
                c = M[i][k] + M[k][j] + (P[j] - P[i])
                if c < M[i][j]:
                    M[i][j] = c
                    Z[i][j] = P[k]
        i += 1
        j += 1
        if j == n:
            i = 0
            start += 1
            j = start
        
    for row in M:
        print(row)
    print()
    for row in Z:
        print(row)

        
    # Still figuring out how to calculate order.
    # cut_order = []
    # i = 0
    # j = n-1
    # while i < n and j > 0 and M[i][j] > 0:
    #     cut_order.append(Z[i][j])
    #     if M[i][j-1] < M[i+1][j]:
    #         j -= 1
    #     else:
    #         i += 1

    return M[0][n-1]
    

print(cut_string([0,1,3,8,10,20]))
