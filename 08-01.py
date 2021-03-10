"""Add 'swap' operation to edit distance function."""

MATCH = 0
INSERT = 1
DELETE = 2
SWAP = 3


class Cell:
    def __init__(self):
        self.cost = None
        self.parent = None

def print_matrix(s, t, matrix, parent=False):
    # Print out matrix in readable format.
    for row in matrix:
        pretty_row = []
        for col in row:
            if parent:
                pretty_row.append(col.parent)
            else:
                pretty_row.append(col.cost)
        print(pretty_row)

def match(c, d):
    if c == d:
        return 0
    else:
        return 1

def indel(c):
    return 1

def swap(a, b, c, d):
    if a == b and c == d:
        return 1
    else:
        return float('inf')

def goal_cell(s, t):
    return len(s) - 1, len(t) - 1

def string_compare(s, t):

    # Cost options.
    opt = [None, None, None, None]

    # Add empty string to beginning of input strings.
    s = ' ' + s
    t = ' ' + t

    # Length of input strings.
    n = len(s)
    m = len(t)

    # Create n-row by m-column matrix.
    matrix = [[Cell() for i in range(m)] for i in range(n)]

    # Init zeroth column.
    for i in range(n):
        matrix[i][0].cost = i
        if i > 0:
            matrix[i][0].parent = DELETE
        else:
            matrix[i][0].parent = -1

    # Init zeroth row.
    for i in range(m):
        matrix[0][i].cost = i
        if i > 0:
            matrix[0][i].parent = INSERT
        else:
            matrix[0][i].parent = -1

    for i in range(1, n):
        for j in range(1, m):
            opt[MATCH] = matrix[i-1][j-1].cost + match(s[i], t[j])
            opt[INSERT] = matrix[i][j-1].cost + indel(t[j])
            opt[DELETE] = matrix[i-1][j].cost + indel(s[i])

            # Add swap function.
            if i > 1 and j > 1:
                opt[SWAP] = matrix[i-2][j-2].cost + swap(s[i], t[j-1], s[i-1], t[j])
            else:
                opt[SWAP] = float('inf')

            matrix[i][j].cost = opt[MATCH]
            matrix[i][j].parent = MATCH
            for k in range(INSERT, SWAP+1):
                if opt[k] < matrix[i][j].cost:
                    matrix[i][j].cost = opt[k]
                    matrix[i][j].parent = k

    print_matrix(s, t, matrix)
    print()
    print_matrix(s, t, matrix, True)

    x, y = goal_cell(s, t)
    return matrix[x][y].cost







# print(string_compare('thou shalt not', 'you should not'))

print(string_compare('dada', 'adad'))
