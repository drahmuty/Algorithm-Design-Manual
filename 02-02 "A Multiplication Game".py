def game(n):
    p = 1
    winner = 'stan'
    nums = [2,3,4,5,6,7,8,9]
    numslen = len(nums)
    count = 0
    while p < n:
        p *= nums[count % numslen]
        if winner == 'stan':
            winner = 'ollie'
        else:
            winner == 'ollie':
                winner = 'stan'
    return winner

def strategy(p, n):
    # return the most strategic multiplier
    nums = [2,3,4,5,6,7,8,9]
    for num in nums:
        if (num * p) >= n:
            return num
    for num in nums:
        q = num * p
        q = q * strategy(q, n)
        if (num * q) >= n:
            return num
        
#     for a in nums:
#         for b in nums:
#             if (a * b * strategy((p * a * b), n)) >= n:
#                 return a

from math import ceil, log

def st(p, n):
    for x in range(9,1,-1):
        y = ceil(log(n,x))
        if (y % 2) != 0:
            return x
        
        
        
def st(p, n):
    print('p='+str(p)+', n='+str(n))
    nums = [2,3,4,5,6,7,8,9]
    for num in nums:
        if (num * p) >= n:
            print('found: '+str(num))
            return num
    for num in nums:
        print('try: '+str(num))
        q = num * p
        q = q * st(q, n)
        print('q='+str(q))
        if num * q >= n:
            return num
        elif (9 * q) < n:
            return num
        
