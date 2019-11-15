# Write a function to perform integer division without using either / or * operators. Find a fast way to do it.

def div(n, d):
    ans = 0
    if d == 0:
        return ans
    if (n < 0 or d < 0):
        sign = -1
    else:
        sign = 1
    n = abs(n)
    d = abs(d)
    while(n >= d):
        n -= d
        ans += 1
    return sign * ans
