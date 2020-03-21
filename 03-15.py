A = []
B = []

for r in range(0, 100):
    A[r] = 0

def insert(x, y):
    y[x] = x

def search(x, y):
    if y[x] == x:
        return x
    else:
        return None

def delete(x, y):
    if search(x, y) is not None:
        y[x] = None
    else:
        return 'not found'

    
    
# Looked up correct solution and modified it for Python

A = [None] * 100
B = [None] * 100   
k = 0

def insert(x):
    global k
    A[x] = k
    B[k] = x
    k = k + 1
    return

def search(x):
    global k
    return A[x] < k and B[A[x]] == x

def delete(x):
    global k
    k -= 1
    A[B[k]] = A[x]
    B[A[x]] = B[k]
    return
