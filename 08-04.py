def longest_common_subsequence(X, Y):

    # Append single space to beginning of input strings.
    X = ' ' + X
    Y = ' ' + Y

    # Get length of input strings.
    n = len(X)
    m = len(Y)

    # Init matrix.
    matrix = [[None for i in range(m)] for i in range(n)]

    # Fill in matrix to find lcs length.
    lcs_len = 0
    for i in range(n):
        for j in range(m):
            if i == 0 or j == 0:
                matrix[i][j] = 0
            elif X[i] == Y[j]:
                matrix[i][j] = matrix[i-1][j-1] + 1
            else:
                matrix[i][j] = max(matrix[i-1][j], matrix[i][j-1])
    lcs_len = matrix[i][j]

    # Traverse matrix in reverse order to find subsequence.
    lcs = ''
    while i > 0 and j > 0:
        if X[i] == Y[j]:
            lcs = X[i] + lcs
            i -= 1
            j -= 1
        elif matrix[i][j-1] > matrix[i-1][j]:
            j -= 1
        else:
            i -= 1

    return lcs, lcs_len

def print_matrix(matrix):
    # Print out matrix in readable format.
    for row in matrix:
        pretty_row = []
        for col in row:
            pretty_row.append(col)
        print(pretty_row)


print(longest_common_subsequence('helloworld', 'goodbyefornow'))
