def sum_of_elements(s, t, k):
    # s: list of integers
    # t: target sum
    # k: number of addends
    
    if k > len(s):
        return 'Error: k greater than list length'    
    s.sort()    
    return soe_recur(s, t, k)
        
        
def soe_recur(s, t, k):             # recursive helper function
    if k == 1:                      # base case when one remaining addend
        if binary_search(t, s):
            return True
    i = 0
    for v in s:
        y = soe_recur(s[i+1:], t-v, k-1)
        if y:
            return True
        i += 1


def binary_search(k, s):
    l, h = 0, len(s) - 1
    while l <= h:
        m = (l + h) // 2
        c = s[m]
        if k == c:
            return True
        if k < c:
            h = m - 1
        elif k > c:
            l = m + 1


s = [5,4,2,7,8,9,3,1,6]
for i in range(50):
    print(i, sum_of_elements(s, i, 9))
