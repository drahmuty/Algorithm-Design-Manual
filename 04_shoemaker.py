def shoemaker(orders):
    # orders is a list of tuple pairs
    # first item is the numbers of days it takes to finish the job
    # second item is the fine per day delayed

    # Get length of list
    n = len(orders)

    # Handle empty and single-item lists
    if n == 0:
        return
    elif n == 1:
        return orders[0]

    # Sort by fine in descending order
    quicksort(orders)
    orders.reverse()

    # Main loop
    result = []
    i = 0
    j = 1
    while j < n:
        i_days = orders[i][0]
        i_fine = orders[i][1]
        j_fine = orders[j][1]
        if i_fine > i_days * j_fine:
            result.append(orders[i])
            i = j
        else:
            result.append(orders[j])
        j += 1
    result.append(orders[i])

    return result


# Attempt 2
def shoemaker2(orders):
    ratio_list = []
    for order in orders:
        ratio_list.append((order[1]/order[0], order[0], order[1]))
    quicksort((ratio_list))
    ratio_list.reverse()
    return ratio_list


# Quicksort
def quicksort(s):
    quicksort_recur(s, 0, len(s) - 1)

def quicksort_recur(s, l, h):
    if l < h:
        p = partition(s, l, h)
        quicksort_recur(s, l, p - 1)
        quicksort_recur(s, p + 1, h)

def partition(s, l, h):
    # Modified to handle tuple pairs
    x = 0  # Reference index in tuple pair
    p = h
    firsthigh = l
    for i in range(l, h):
        if s[i][x] < s[p][x]:
            s[i], s[firsthigh] = s[firsthigh], s[i]
            firsthigh += 1
    s[p], s[firsthigh] = s[firsthigh], s[p]
    return firsthigh


# Driver code
a = [(3,4), (1,1000), (2,2), (5,5)]
b = [(1,1), (2,2), (3,3)]
print(shoemaker2(a))
