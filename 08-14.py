def chess_win_prob(n, P):
    # n = number of games
    # P = array of probabilites []

    # Alternate probability for white and black games.
    # Odd games return white (0th index).
    W = lambda x: P[(x+1)%2][0]
    L = lambda x: P[(x+1)%2][1]
    D = lambda x: P[(x+1)%2][2]

    M = [[0 for i in range(2*n+1)] for i in range(n+1)]

    for i in range(n+1):
        for j in range(2*n+1):
            if i == 0 and j == 0:
                M[i][j] = 1.0
                continue
            elif i == 0 or j == 0:
                M[i][j] = 0.0
                continue
            else:
                M[i][j] = L(i) * M[i-1][j] + D(i) * M[i-1][j-1]
            if j/2 >= 1:
                M[i][j] += W(i) * M[i-1][j-2]

    return M[i][j]
            
    

games = 24
probs = [[.5, -.3, .2], [.3, -.3, .4]]
print(chess_win_prob(games, probs))
