def game(n):
    p = 1
    winner = 'stan'
    while True:
        p *= strategy(p, n)
        if p >= n:
            break
        if winner == 'stan':
            winner = 'ollie'
        else:
            winner = 'stan'
    return winner
            
def strategy(p, n):
    for x in range(2, 10):
        if (x * p) >= n:
            return x
    for y in range(9, 1, -1):
        if (y * p * 9) < n:
            return y
    return 2
