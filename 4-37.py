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

# Selection sort (standard solution)
def selection_sort(A):
    for i in range(len(A)):
        min_index = i
        for j in range(i+1, len(A)):
            if A[j] < A[min_index]:
                min_index = j
        A[i], A[min_index] = A[min_index], A[i]

# Insertion sort
def insertion_sort(A):
    for i in range(len(A)):
        for j in range(i-1, -1, -1):
            if A[i] < A[j]:
                A[i], A[j] = A[j], A[i]
                i -= 1
            else:
                break

# Insertion sort (standard solution)
def insertion_sort(A):
    for i in range(len(A)):
        j = i
        while j > 0 and A[j] < A[j-1]:
            A[j], A[j-1] = A[j-1], A[j]
            j -= 1

# Heapsort
def heapsort(items):
    h = Heap()
    h.make_heap(items)
    for i in range(len(items)):
        items[i] = h.extract_min()
        
class Heap:
    def __init__(self):
        self.q = [None]
        self.n = 0
    
    def parent(self, x):
        if x <= 1:
            return None
        else:
            return x // 2

    def child_left(self, x):
        return 2 * x
    
    def child_right(self, x):
        return 2 * x + 1
    
    def insert(self, x):
        self.q.append(x)
        self.n += 1
        self.bubble_up(self.n)
    
    def bubble_up(self, x):
        p = self.parent(x)
        if not p:
            return
        if self.q[p] > self.q[x]:
            self.q[p], self.q[x] = self.q[x], self.q[p]
            self.bubble_up(p)
    
    def make_heap(self, items):
        for item in items:
            self.insert(item)
    
    def extract_min(self):
        if self.n <=0:
            print('Empty')
        else:
            min = self.q[1]
            self.q[1] = self.q[self.n]
            self.n -= 1
            self.bubble_down(1)
        return min
    
    def bubble_down(self, x):
        c = self.child_left(x)
        min_index = x
        for i in range(0, 2):
            if (c+i) > self.n:
                break
            if self.q[min_index] > self.q[c+i]:
                min_index = c+i
        if min_index != x:
            self.q[x], self.q[min_index] = self.q[min_index], self.q[x]
            self.bubble_down(min_index)

# Mergesort
def mergesort(s, low, high):
    if low < high:
        mid = (low + high) // 2
        mergesort(s, low, mid)
        mergesort(s, mid+1, high)
        merge(s, low, mid, high)

def merge(s, low, mid, high):
    buffer1 = s[low:mid+1]
    buffer2 = s[mid+1:high+1]
    i = low
    while buffer1 and buffer2:
        if buffer1[0] < buffer2[0]:
            s[i] = buffer1.pop(0)
        else:
            s[i] = buffer2.pop(0)
        i += 1
    while buffer1:
        s[i] = buffer1.pop(0)
        i += 1
    while buffer2:
        s[i] = buffer2.pop(0)
        i += 1
