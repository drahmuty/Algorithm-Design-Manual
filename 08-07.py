"""Number of ways to make change for amount n with a given set of denominations."""

def num_ways_to_make_change(n, denoms):
    denoms = [None] + denoms
    k = len(denoms)
    c = [[0 for i in range(n+1)] for i in range(k)]
    for i in range(k):
        for j in range(n+1):
            if j == 0:
                c[i][j] = 1
            elif i == 0:
                c[i][j] = 0
            elif denoms[i] <= j:
                c[i][j] = c[i][j-denoms[i]] + c[i-1][j]
            else:
                c[i][j] = c[i-1][j]
    print_matrix(c)
    return c[i][j]
  
def print_matrix(matrix):
    # Print out matrix in readable format.
    for row in matrix:
        pretty_row = []
        for col in row:
            pretty_row.append(col)
        print(pretty_row)  

print(num_ways_to_make_change(20, [1,6,10]))
