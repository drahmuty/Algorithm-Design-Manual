"""
4-35. Let M be an n×m integer matrix in which the entries of each row are sorted in increasing order 
(from left to right) and the entries in each column are in increasing order (from top to bottom). 
Give an efficient algorithm to find the position of an integer x in M, or to determine that x is not there. 
How many comparisons of x with matrix entries does your algorithm use in worst case?
"""

def matrix_search(M, x):
    m = len(M)      # Matrix depth
    n = len(M[0])   # Matrix width
    # Binary search for row
    low = 0
    high = m - 1
    while low <= high:
        row = (low + high) // 2
        c_first = M[row][0]
        c_last = M[row][n-1]
        if c_first <= x and c_last >= x:
            break
        elif c_first < x:
            low = row + 1
        else:
            high = row - 1
    # Binary search for column within row
    low = 0
    high = n - 1
    while low <= high:
        col = (low + high) // 2
        c = M[row][col]
        if c < x:
            low = col + 1
        elif c > x:
            high = col - 1
        else:
            return row, col
    return None


M = [
    [1,2,3,4,5],
    [6,7,8,9,10],
    [11,12,13,14,15],
    [16,17,18,19,20],
    [21,22,23,24,25]
]

for i in range(26):
    print(matrix_search(M, i))
