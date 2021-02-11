"""List all k element subsets of a set of n items."""

from collections import defaultdict

def k_subsets1(set_items, k):
    backtrack(defaultdict(bool), 0, set_items, k)
def backtrack1(solution, counter, set_items, k):
    # print(counter, solution)
    if counter == k:
        print('SOLUTION', solution)
    else:
        counter += 1
        candidates = set()
        for item in set_items:
            if not item in solution:
                candidates.add(item)
        # print('CANDIDATES', candidates)
        for c in candidates:
            solution.add(c)
            backtrack(solution, counter, set_items, k)
            solution.remove(c)



def k_subsets(k, items):
    print('Subsets of ' + str(items) + ' (k = ' + str(k) + ')')
    backtrack([None for i in range(k)], -1, k, sorted(items))
    print()

def backtrack(solution, j, k, items):
    if j + 1 == k:
        print(solution)
    else:
        j += 1
        in_solution = defaultdict(bool)
        for s in solution:
            in_solution[s] = True
        candidates = []
        for item in items:
            if j == 0:
                candidates.append(item)
            elif not in_solution[item] and item > solution[j - 1]:
                candidates.append(item)
        for c in candidates:
            solution[j] = c
            backtrack(solution, j, k, items)
            solution[j] = None



# Test cases.
k_subsets(2, [1, 2, 3])
k_subsets(2, [1, 2, 3, 4])
k_subsets(3, [1, 2, 3, 4, 5])
