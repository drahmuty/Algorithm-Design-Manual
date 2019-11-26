def mar(n, ans):
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
