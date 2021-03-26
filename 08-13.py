"""Find minimum number of given substrings to encode a string."""



def encode_string(S, T):
    
    # Append empty value to beginning of each input.
    S = ' ' + S
    T = [' ' + T[i] for i in range(len(T))]

    # Set range values.
    n = len(S)
    m = len(T)
    p = max(len(T[i]) for i in range(m))
        
    # Array to store solution.
    A = [None for i in range(n)]
    
    # Array to store cost of solution.
    C = [float('inf') for i in range(n)]

    # Array to store length of each item in T.
    L = [len(T[i]) for i in range(m)]

    # Dynamic matrix.
    M = [[[-1 for i in range(n)] for i in range(p)] for i in range(m)]

    # Fill in dynamic matrix.
    for i in range(p):
        for j in range(n):
            for k in range(m):
                if i == 0:
                    M[k][i][j] = 0
                elif j == 0 or i >= L[k]:
                    continue
                elif M[k][i-1][j-1] > -1 and T[k][i] == S[j]:
                    M[k][i][j] = M[k][i-1][j-1] + 1
    
    # Find optimal solution.
    for j in range(n):
        for k in range(m):
            i = L[k] - 1
            if j == 0:
                C[j] = 0
            elif M[k][i][j] > 0 and C[j-M[k][i][j]] + 1 < C[j]:
                A[j] = k
                C[j] = C[j-M[k][i][j]] + 1
    
    # Build result by backtracking through solution array.
    result = []
    while j > 0:
        if A[j] is None:
            return None
        result = [T[A[j]].strip()] + result
        j -= (L[A[j]] - 1)
    
    print('Result:', result)
    return result



# Test case.
string = 'bababbaababa'
text_items = ['a', 'ba', 'abab', 'b']
encode_string('string', text_items)
