"""Determine how many shelves it will take to fit n books of variable widths."""

def store_books_on_shelves(B, L):
    B = [0] + B
    n = len(B)
    C = [0 for i in range(n)]
    S = [0 for i in range(n)]
    for i in range(1, n):
        if C[i-1] + B[i] <= L:
            C[i] = C[i-1] + B[i]
            S[i] = S[i-1]
        elif B[i] <= L:
            C[i] = B[i]
            S[i] = S[i-1] + 1
        else:
            return None
    print(B)
    print(C)
    print(S)
    return S[i] + 1



B = [2,1,1,3,2,4,1,2,3]
L = 4
print(store_books_on_shelves(B, L))
