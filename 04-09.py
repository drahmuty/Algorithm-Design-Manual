"""
4-9. Give an efficient algorithm to compute the union of sets A and B, where n=max(|A|,|B|). 
The output should be an array of distinct elements that form the union of the sets, such that 
they appear exactly once in the union.
"""



def union_unique(A, B):

    # Sort each array.
    A.sort()
    B.sort()

    # Initialize empty array.
    C = []

    # Initialize helper variables.
    i = j = 0
    a_len = len(A)
    b_len = len(B)
    prev = None

    # Merge arrays.
    while i < a_len and j < b_len:
        a, b = A[i], B[j]
        if a == prev:
            i += 1
        elif b == prev:
            j += 1
        elif a < b:
            C.append(a)
            prev = a
            i += 1
        elif a > b:
            C.append(b)
            prev = b
            j += 1
        else:
            C.append(a)
            prev = a
            i += 1
            j += 1

    # Add remaining unique elements from A.
    while i < a_len:
        a = A[i]
        if a != prev:
            C.append(a)
            prev = a
        i += 1

    # Add remaining unique elements from B.
    while j < b_len:
        b = B[j]
        if b != prev:
            C.append(b)
            prev = b
        j += 1
    
    # Return union array.
    return C


# Test program.
s1 = [3,6,9,3,1,2,5,3,3,2]
s2 = [9,4,2,7,8,8,9,4,7,4]

print(union_unique(s1, s2))
