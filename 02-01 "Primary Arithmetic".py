def carry(x, y):
    count = 0
    c = 0
    while (x > 0) or (y > 0):
        a = x % 10
        b = y % 10
        if (a + b + c) > 9:
            c = 1
            count += 1
        else:
            c = 0
        x //= 10
        y //= 10
    return count
