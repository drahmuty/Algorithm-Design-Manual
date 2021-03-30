"""Find number of safe paths through a city, avoiding bad intersections. Move right or down only."""

def num_safe_paths(x, y, bad):

    B = [[False for i in range(y+1)] for i in range(x+1)]
    for b in bad:
        B[b[0]][b[1]] = True

    M = [[0 for i in range(y+1)] for i in range(x+1)]

    for i in range(x+1):
        for j in range(y+1):
            if i == 0 or j == 0:
                M[i][j] = 0
            elif B[i][j]:
                continue
            elif i == 1 and j == 1:
                M[i][j] = 1
            else:
                M[i][j] = M[i][j-1] + M[i-1][j]
    
    for row in M:
        print(row)


x = 5
y = 5
bad = [
    (1,2),
    (3,3),
    (5,4)
]
num_safe_paths(x, y, bad)
