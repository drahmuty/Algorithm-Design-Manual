
"""Find max contiguous sum in circle array."""



def kadane(A):
    max_sum = 0
    current_sum = 0
    for i in range(len(A)):
        print('i', A[i])
        current_sum += A[i]
        print('current sum', current_sum)
        current_sum = max(current_sum, 0)
        max_sum = max(max_sum, current_sum)
    return max_sum

def max_contiguous_sum(A):

    # Invert array values.
    for i in range(len(A)):
        A[i] = -A[i]
    
    # Find max contiguous sum of inverted array.
    max_neg_sum = kadane(A)

    # Revert array.
    for i in range(len(A)):
        A[i] = -A[i]
        
    return max(kadane(A), sum(A) + max_neg_sum)

    

# Test cases.
A = [1,2,3,-6,2,10,-7,9]
print(max_contiguous_sum(A))


"""https://www.techiedelight.com/maximum-sum-circular-subarray/"""
