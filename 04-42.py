def unique_items(a):
    quicksort(a)
    b = []
    p = None
    for c in a:
        if c != p:
            b.append(c)
            p = c
    return b
    
    


# Quicksort
def quicksort(s):
    quicksort_recur(s, 0, len(s)-1)

def quicksort_recur(s, l, h):
    if l < h:
        p = partition(s, l, h)
        quicksort_recur(s, l, p-1)
        quicksort_recur(s, p+1, h)

def partition(s, l, h):
    p = h
    firsthigh = l
    for i in range(l, h):
        if s[i] < s[p]:
            s[i], s[firsthigh] = s[firsthigh], s[i]
            firsthigh += 1
    s[p], s[firsthigh] = s[firsthigh], s[p]
    return firsthigh
