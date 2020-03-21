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
