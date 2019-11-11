def bubblesort(x):
    for i in range(len(x), 0, -1):
        for j in range(0, i-1):
            if x[j] > x[j+1]:
                x[j], x[j+1] = x[j+1], x[j]
    return x
