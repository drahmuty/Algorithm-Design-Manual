import math

def dial(N, k):
    # N: str phone number
    # k: int number of keypad digits

    N = '0' + N
    n = len(N)

    # Solution lists.
    C = [float('inf')] * n
    P = [[None, None] for i in range(n)]
    D = make_keypad(k)

    C[0] = 0
    P[0][0] = 10
    P[0][1] = 11

    # Dynamic loop.
    for i in range(1, n):
        for a in range(k):
            for b in range(k):
                if str(a) != N[i] and str(b) != N[i]:
                    continue
                current_cost = C[i-1] + D[P[i-1][0]][a] + D[P[i-1][1]][b]
                if current_cost < C[i]:
                    C[i] = current_cost
                    P[i][0] = a
                    P[i][1] = b
    
    for p in P:
        print(p)
    print(round(C[i], 1))
    
def make_keypad(k):

    D = [[float('inf') for i in range(k + 1)] for i in range(k + 1)] 

    # Get x and y coordinates of a number.
    # Assumes keypad width of 3.
    get_x = lambda x: (x - 1) % 3 + 1
    get_y = lambda x: math.ceil(x / 3)

    # Matrix of Euclidian distance between keys.
    # 1  2  3
    # 4  5  6
    # 7  8  9
    # *  0  #    (* = 10 and # = 11)
    for i in range(k):
        for j in range(k):
            if i == j:
                D[i][j] = 0
            else:
                if i == 0:
                    x1 = get_x(k - 1)
                    y1 = get_y(k - 1)
                elif i == k - 1:
                    x1 = get_x(k)
                    y1 = get_y(k)
                else:
                    x1 = get_x(i)
                    y1 = get_y(i)
                if j == 0:
                    x2 = get_x(k - 1)
                    y2 = get_y(k - 1)
                elif j == k - 1:
                    x2 = get_x(k)
                    y2 = get_y(k)
                else:
                    x2 = get_x(j)
                    y2 = get_y(j)
                D[i][j] = math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)

    return D



dial('123456789', 12)
