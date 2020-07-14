# Selection sort
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
