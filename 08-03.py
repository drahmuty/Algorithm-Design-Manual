def print_matrix(matrix):
    # Print matrix in a readable format.
    for row in matrix:
        pretty_row = []
        for col in row:
            pretty_row.append(col)
        print(pretty_row)


def longest_substring_dynamic(s, t):

    # Add empty string prefix to both strings.
    s = str(' ' + s)
    t = str(' ' + t)

    # Get length of both strings.
    n = len(s)
    m = len(t)

    # Initialize matrix.
    matrix = [[0 for i in range(m)] for i in range(n)]

    max = 0
    max_i = 0

    # Fill in matrix.
    for i in range(1, n):
        for j in range(1, m):
            last = matrix[i-1][j-1]
            if s[i] == t[j]:
                matrix[i][j] = last + 1
                if matrix[i][j] > max:
                    max = matrix[i][j]
                    max_i = i
            else:
                matrix[i][j] = 0

    # Result.
    substr = s[max_i - (max - 1) : max_i + 1]
    print(s.strip())
    print(t.strip())
    print(substr, max)
    return substr, max


# Test cases.
longest_substring_dynamic('david', 'dave')
longest_substring_dynamic('isthisacopyortherealthing', 'thisisacopyortherealthingitis')
