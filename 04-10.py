"""
4-10. Given a set S of n integers and an integer T, 
give an O(nk−1logn) algorithm to test whether k of 
the integers in S add up to T.
"""

"""
inputs:
s (list of integers)
t (target sum)
k (number of addends)

output:
true or false
or return addends?

program steps:
sort s

recursive
    remove one element from s
    target sum = t - currently selected element from s
    k--

base case when k = 0
binary search for remaining set of numbers

"""


def sum_of_elements(s, t, k):
    
    # Return false if k is greater than the number of elements in s
    if k > len(s):
        return False
    
    # Sort list of elements
    s.sort()
    
    # Run recursive helper function
    return soe_recur(s, t, k)


def soe_recur(s, t, k):
    for a in s:
        b = t - s[a]
        if k <= 2:
            # if binary search through remaining list for b is true:
                # return True
            return
        else:
            return soe_recur(s[a+1:], b, k-1)


def binary_search(k, s):
    l, h = 0, len(s) - 1
    while l < h:
        m = (l + h) // 2
        c = s[m]
        if k == c:
            return True
        elif k < c:
            h = m - 1
        elif k > c:
            l = m + 1
































