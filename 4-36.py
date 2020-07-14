"""
4-36. Consider an n×n array A containing integer elements (positive, negative, and zero). 
Assume that the elements in each row of A are in strictly increasing order, and the elements 
of each column of A are in strictly decreasing order. (Hence there cannot be two zeroes in 
the same row or the same column.) Describe an efficient algorithm that counts the number of 
occurrences of the element 0 in A. Analyze its running time.
"""


def count_zeros(A):
    n = len(A)
    zeros = 0
    row = 0
    row_start = 0
    row_end = n - 1
    while row < n and row_start <= row_end:
        zero_index = binary_search(A[row], 0, row_start, row_end)
        if zero_index > -1:
            zeros += 1
            row_start = zero_index
        row += 1
    return zeros

def binary_search(list, x, low, high):
    while low <= high:
        mid = (low + high) // 2
        c = list[mid]
        if c == x:
            return mid
        elif c < x:
            low = mid + 1
        else:
            high = mid - 1
    return -1

M = [
    [0,1,2,3,4],
    [-1,0,1,2,3],
    [-2,-1,0,1,2],
    [-3,-2,-1,0,1],
    [-4,-3,-2,-1,0]
]

print(count_zeros(M))



# Runs in O(n log n) worst case because it could potentially do a binary search for each of n rows.

# However, it may run faster if zeros are present because when a zero is found on a given row we
# only have to search the right side of the array for the remaining row(s).

# So best case would be O(log n) if a zero is found in the last column of the first row because
# we'd know there can't possibly be any more zeros to search for. 
