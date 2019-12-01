from math import sqrt

def m1(n, ans):
    high = n
    low = 0
    mid = (high-low)//2
    while mid != high:
        if mid >= ans:
            high = mid
        else:
            low = mid
        mid = high - (high-low)//2
    return mid



"""
Use this to log helper variables in while loop:
    logger = "High="+str(high)+", "
    logger += "Mid="+str(mid)+", "
    logger += "Low="+str(low)+", "
    print(logger)                   
"""


# Two marbles approach
def m2(n, ans):
    start = round((-1 + sqrt(1 - 8*(-n))) / 2)
    lo = 1
    hi = start
    while hi <= n:
        if hi >= ans:
            while lo < ans:
                lo += 1
            return lo
        else:
            lo = hi + 1
            start -= 1
            hi += start
    return None
