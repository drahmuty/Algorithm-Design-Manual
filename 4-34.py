"""
4-34. Suppose that you are given a sorted sequence of distinct integers {a1,a2,…,an}, 
drawn from 1 to m where n<m. Give an O(lgn) algorithm to find an integer ≤m that is 
not present in a. For full credit, find the smallest such integer.
"""


def find_gap(A):
    low = 0
    high = len(A) - 1
    gap = None
    while low <= high:
        mid = (low + high) // 2
        midVal = mid + 1
        if A[mid] == midVal:
            low = mid + 1
        elif A[mid] > midVal:
            gap = midVal
            high = mid - 1
    return gap


A = [1,2,3,4,5,6,7,8,9,10,11]
print(find_gap(A))
