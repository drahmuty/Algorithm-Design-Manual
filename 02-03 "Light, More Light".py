# O(n) algorithm
def light(n):
    x = 0
    for i in range(1, n+1):
        if n % i == 0:
            x += 1
    if x % 2 == 0:
        return 'off'
    else:
        return 'on'

# O(1) algorithm - I looked up this solution and translated it from C to Python
def light(n):
    s = round(sqrt(n))
    if s * s == n:
        return 'on'
    else:
        return 'off'
