"""Generate all permutations of letters in a string."""

from collections import defaultdict

def string_perms(string):
    global perms
    perms = list()
    char_freq = defaultdict(int)
    for s in string:
        char_freq[s] += 1
    backtrack(str(), -1, string, char_freq)

def backtrack(a, k, string, char_freq):
    # print(k, a)
    if is_a_solution(a, k, string):
        process_solution(a, k, string)
    else:
        k += 1
        candidates = get_candidates(a, k, string, char_freq)
        for c in candidates:
            a += c
            backtrack(a, k, string, char_freq)
            a = a[:k]

def is_a_solution(a, k, string):
    return len(a) == len(string)

def process_solution(a, k, string):
    print(a)

def get_candidates(a, k, string, char_freq):
    candidates = []
    in_sol = defaultdict(int)
    for char in a:
        in_sol[char] += 1
    for s in string:
        if in_sol[s] < char_freq[s]:
            candidates.append(s)
    return sorted(set(candidates))



# Test cases.
string_perms('dave')
string_perms('hello')
string_perms('google')
