"""
4-8. Given a set of S containing n real numbers, and a real number x. 
We seek an algorithm to determine whether two elements of S exist whose sum is exactly x.
"""


def sum_pairs(s, x):
    s.sort()
    l, h = 0, len(s) - 1
    while l < h:
        sum = s[l] + s[h]
        if sum == x:
            return True
        elif sum < x:
            l += 1
        elif sum > x:
            h -= 1

# Test program
s1 = [3,6,9,3,1,2,5,3,3,2]
for i in range(20):
    print(i, sum_pairs(s1, i))
