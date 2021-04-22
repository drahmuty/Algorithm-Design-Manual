"""
Find minimum cost path traveling across a matrix left-to-right.
https://onlinejudge.org/external/1/116.pdf
"""

def print_matrix(matrix):
    for m in matrix:
        print(m)
    print()


def uni_tsp(W):

    # Get size of matrix.
    n = len(W) + 1
    m = len(W[0]) + 1

    # Cost matrix.
    C = [[float('inf')] * m for i in range(n)]

    # Parent matrix.
    P = [[None] * m for i in range(n)]

    # Dynamic program. Fill in each column first.
    for j in range(m):
        for i in range(n):

            # Init base cases.
            if i == 0 or j == 0:
                C[i][j] = 0
                continue
                        
            # Enable "wrap" behavior for rows.
            up = i - 1
            side = i
            down = i + 1
            if i == 1:
                up = n - 1
            if i == (n - 1):
                down = 1
            
            # Calculate cost for each option.
            cost_up = C[up][j-1] + W[i-1][j-1]
            cost_side = C[side][j-1] + W[i-1][j-1]
            cost_down = C[down][j-1] + W[i-1][j-1]

            # Choose minimum cost.
            if cost_up < C[i][j]:
                C[i][j] = cost_up
                P[i][j] = up
            if cost_side < C[i][j]:
                C[i][j] = cost_side
                P[i][j] = side
            if cost_down < C[i][j]:
                C[i][j] = cost_down
                P[i][j] = down
    
    # Find the minimum cost in the final column.
    min_cost = float('inf')
    min_cost_row = None
    for i in range(n-1, 0, -1):
        if C[i][m-1] < min_cost:
            min_cost = C[i][m-1]
            min_cost_row = i

    # Construct minimum path.
    min_cost_path = []
    for j in range(m-1, 0, -1):
        min_cost_path = [min_cost_row] + min_cost_path
        min_cost_row = P[min_cost_row][j]
    print(min_cost_path)
    print(min_cost)



# Test cases.
W1 = [
    [3,4,1,2,8,6],
    [6,1,8,2,7,4],
    [5,9,3,9,9,5],
    [8,4,1,3,2,6],
    [3,7,2,8,6,4]
]
W2 = [
    [3,4,1,2,8,6],
    [6,1,8,2,7,4],
    [5,9,3,9,9,5],
    [8,4,1,3,2,6],
    [3,7,2,1,2,3]
]
W3 = [
    [9, 10],
    [9, 10]
]
uni_tsp(W1)
uni_tsp(W2)
uni_tsp(W3)
