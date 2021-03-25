"""
Given a set of points P on a string, determine the order in which to cut the string into segments. 
Each cut costs n (n = length of current string).
"""



def cut_string(P):

    print('Points:', P)

    global C
    global order_list

    P.sort()
    first = P[0]
    last = P[-1]

    n = len(P)
    
    M = [[float('inf') for i in range(n)] for i in range(n)]
    C = [[0 for i in range(n)] for i in range(n)]

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
                    C[i][j] = k
        i += 1
        j += 1
        if j == n:
            i = 0
            start += 1
            j = start

    order_list = []
    order = get_order(0, n-1, P)
    
    print('Order:', order_list)
    print('Cost:', M[0][n-1])

    return order_list

def get_order(i, j, P):
    if C[i][j] == 0:
        return
    else:
        order_list.append(P[C[i][j]])
        get_order(i, C[i][j], P)
        get_order(C[i][j], j, P)

    

cut_string([0, 3, 8, 10, 20])
