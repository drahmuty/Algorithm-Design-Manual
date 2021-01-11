# Construct all derangements of a set of n items.

from collections import defaultdict

# Backtracking algorithm.
def backtrack(a, k, n):
    if is_a_solution(a, k, n):
        process_solution(a, k, n)
    else:
        k += 1
        candidates = construct_candidates(a, k, n)
        for c in candidates:
            a[k] = c
            backtrack(a, k, n)
            a[k] = None

# Is a solution helper function.
def is_a_solution(a, k, n):
    return k == n 

# Construct candidates helper function.
def construct_candidates(a, k, n):
    candidates = []
    in_perm = defaultdict(bool)
    for item in a:
        in_perm[item] = True
    for i in range(1, n+1):
        if not in_perm[i] and i!= k:
            candidates.append(i)
    return candidates

# Process solution helper function.
def process_solution(a, k, n):
    result = []
    for i in a:
        if i: result.append(i)
    print("SOLUTION:", result)

# Main program.
def derangement(n):
    a = [None for i in range(n+1)]
    print("Derangement(s) for n=" + str(n) + ":")
    backtrack(a, 0, n)

# Test cases.
for i in range(1, 6):
    derangement(i)
