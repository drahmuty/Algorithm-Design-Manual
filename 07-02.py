"""Generate all distinct permutations of a multiset."""

from collections import defaultdict

# Create main backtracking algorithm.
def backtrack(a, k, data):
    if is_a_solution(a, k, data):
        process_solution(a, k, data)
    else:
        k += 1
        candidates = construct_candidates(a, k, data)
        for c in candidates:
            a[k] = c
            backtrack(a, k, data)
            a[k] = None

# Is a solution helper function.
def is_a_solution(a, k, data):
    return k == len(data)

# Construct candidates helper function.
def construct_candidates(a, k, data):

    c = []
    in_a = defaultdict(int)
    in_c = defaultdict(bool)

    for item in a:
        in_a[item] += 1

    for d in data:
        if in_a[d] < counts[d] and not in_c[d]:
            c.append(d)
            in_a[d] += 1
            in_c[d] = True

    return c

# Process solution helper function.
def process_solution(a, k, data):

    result = []
    
    for i in a:
        if i: result.append(i)
    
    print("SOLUTION:", result)

# Multiset permutations.
def multiset_perms(multiset):
    
    # Store number of occurences of each distinct item in set.
    global counts 
    counts = defaultdict(int)
    for m in multiset:
        counts[m] += 1

    # Init solution array.
    a = [None for i in range(len(multiset)+1)]    

    # Generate all permutations using backtrack algorithm.
    print("\nPermutations for multiset " + str(multiset) + ":")
    backtrack(a, 0, multiset)

# Test cases
multiset_perms([])
multiset_perms([1])
multiset_perms([1,1])
multiset_perms([1,1,1])
multiset_perms([1,2])
multiset_perms([1,1,2])
multiset_perms([1,1,1,2])
multiset_perms([1,1,2,2])
multiset_perms([1,1,2,2,3])
