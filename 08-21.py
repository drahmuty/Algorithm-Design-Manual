"""Find max contiguous subvector."""


def max_subv(S):

    S = [0] + S
    n = len(S)

    all_negative = True
    for i in range(n):
        if S[i] > 0:
            all_negative = False
            break
    if all_negative:
        return 0

    A = [0] * n    # Max sum list.
    B = [0] * n    # Bit vector to add (1) or skip (0).
    C = [0] * n    # Sum of skipped values.

    for i in range(1, n):
        new_sum = S[i] + A[i-1] + C[i-1]
        if S[i] > new_sum:
            A[i] = S[i]
            B[i] = 1
            C[i] = 0
        elif new_sum >= A[i-1]:
            A[i] = new_sum
            B[i] = 1
            C[i] = 0
        else:
            A[i] = A[i-1]
            B[i] = 0
            C[i] = S[i] + C[i-1]

    max = A[i]
    sum = A[i]
    items = []
    while B[i] == 0:
        i -= 1
    while sum > 0:
        items = [S[i]] + items
        sum -= S[i]
        i -= 1

    print(items)
    print(max)

    return max, items
    




# S = [31, -41, 59, 26, -53, 58, 97, -93, -23, 84]
S = [1,1,1,1,1,1,1,1,1]
max_subv(S)
