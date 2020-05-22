"""
4-6. Given two sets S1 and S2 (each of size n), and a number x, describe an O(nlogn) algorithm 
for finding whether there exists a pair of elements, one from S1 and one from S2, that add up to x. 
(For partial credit, give a Θ(n2) algorithm for this problem.)
"""

"""
Sort S2.
For each element in S1:
    Do a binary search in S2 to find a pair that adds up to x.
    Return true if a pair exists.
Return false if no pair exists.

Runs in O(nlogn) + O(nlogn) = O(nlogn)
"""


def pairs(s1, s2, x):
    s2.sort()
    for i in s1:
        k = x - i
        if binary_search(k, s2):
            return True
    return False

def binary_search(value, elements):
    left, right = 0, len(elements) - 1

    while left <= right:
        middle = (left + right) // 2
        middle_element = elements[middle]
        
        if value == middle_element:
            return middle
        if value < middle_element:
            right = middle - 1
        elif value > middle_element:
            left = middle + 1



s1 = [3,6,9,3,1,2,5,3,3,2]
s2 = [9,4,2,7,8,8,9,4,7,4]
x = 5

print(pairs(s1, s2, x))
