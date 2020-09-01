def cross_bridge(p):
    # p is a list of integers representing walking speeds

    # Initialize total time t to zero
    t = 0

    # Handle lists < 2
    l = len(p)
    if l < 1:
        return t
    elif l < 2:
        return p[0]

    # Sort list of people by walking speed
    p.sort()

    # Set up variables
    fast1 = p[0]
    fast2 = p[1]
    i = l - 1

    # Main loop
    while i > 0:
        t += fast2          # Fast pair crosses
        print(fast1, fast2)
        if i > 1:
            t += fast1      # Fast1 returns
            print(fast1)
        else:
            break
        slow = p[i]
        t += slow           # Slow pair crosses
        print(slow)
        i -= 2
        if i > 0:
            t += fast2      # Fast2 returns
            print(fast2)
        else:
            break

    # Return total crossing time
    return t

# Driver program
a = [1,2,3,4,5,6,7,8,9,10]
print('total time = ' + str(cross_bridge(a)))
