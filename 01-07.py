def multiply(y, z, c):
    if z == 0:
        return 0
    else:
        return multiply(c * y, z // c, c) + y * (z % c)
