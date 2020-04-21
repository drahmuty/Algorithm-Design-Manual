"""
3-28. 
You have an unordered array X of n integers. 
Find the array M containing n elements where 
Mi is the product of all integers in X except for Xi. 
You may not use division. You can use extra memory. 
(Hint: There are solutions faster than O(n^2).)

Example:
X = [1, 2, 3, 4, 5]
M = [120, 60, 40, 30, 24]
"""

# O(n^2) approach:
# For each X
# Multiple all numbers except for Xi
# Store result in Mi

def foo(X):
    M = []
    for a in X:
        m = 1
        for b in X:
            if a == b:
                continue
            else:
                m *= b
        M.append(m)
    return M


# O(n) approach
# I looked the conceptual approach after hours 
# of trying on my own with no luck
# This is my own interpretation and implementation

def bar(x):
    x_len = len(x)                  # Get length of X
    m = [1 for r in range(x_len)]   # Initialize output array
    i = 0                           # Array index counter
    p = 1                           # Product accumulator
    while i < x_len - 1:            # Forward pass
        xi = x[i]                   # Get Xi (first item in array)
        i += 1                      # Move to Mi+1
        p *= xi                     # Multiply product by Xi
        m[i] = p                    # Store product in Mi+1
    p = 1                           # Reset product to 1
    while i > 0:                    # Reverse pass
        xi = x[i]                   # Get Xi (last item in array)
        i -= 1                      # Move to Mi-1
        p *= xi                     # Multiply product by Xi
        m[i] *= p                   # Multiply Mi-1 by product
    return m

a = [1,2,3,4,5]
b = [32,24,51]
print(bar(a))
print(bar(b))
