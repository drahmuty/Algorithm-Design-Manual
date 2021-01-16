"""Find all anagrams of a word."""

from collections import defaultdict

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

def is_a_solution(a, k, data):
    return k == len(a)-1

def process_solution(a, k, data):
    solution = ""
    for s in a:
        solution += str(s)
    print("SOLUTION:", solution)

def construct_candidates(a, k, data):
    string = data[0]
    count = data[1]
    used_count = defaultdict(int)
    c = []
    for i in a:
        used_count[i] += 1
    for s in string:
        if used_count[s] < count[s]:
            c.append(s)
    return c

# Main program.
def anagrams(string):

    # Solution array.
    a = [None for i in range(len(string))]

    # Dictionary of letters and their frequency.
    count = defaultdict(int)
    for s in string:
        count[s] += 1
    
    # Generate all permutations.
    backtrack(a, -1, (string, count))

# Test cases.
anagrams('dave')
anagrams('hello')
