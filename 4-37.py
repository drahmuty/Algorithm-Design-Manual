# Selection sort (first attempt)
def selection_sort(A):
    sorted = []
    while A:
        min = None
        for i in range(len(A)):
            if not min or A[i] < min:
                min = A[i]
                min_index = i
        sorted.append(A.pop(min_index))
    return sorted

# Selection sort (correct solution)
def selection_sort(A):

    for i in range(len(A)):
        min_index = i
        
        for j in range(i+1, len(A)):
            if A[j] < A[min_index]:
                min_index = j
        
        A[i], A[min_index] = A[min_index], A[i]
