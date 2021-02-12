"""List all k-element subsets of a set of n items."""



def k_subsets(n, k):
    a = [0 for i in range(n)]
    backtrack(a, -1, n, k, 0)

def backtrack(solution, counter, n, k, sum):
    if sum == k:
        subset = []
        for s in range(n):
            if solution[s] == 1:
                subset.append(s + 1)
        print(subset)
    elif counter == n - 1:
        return
    elif n - (counter + 1) < k - sum:
        return
    else:
        counter += 1
        candidates = [1, 0]
        for c in candidates:
            solution[counter] = c
            sum += c
            backtrack(solution, counter, n, k, sum)
            solution[counter] = 0
            sum -= c



# Test cases.
k_subsets(3, 2)
k_subsets(5, 3)
k_subsets(10, 5)
