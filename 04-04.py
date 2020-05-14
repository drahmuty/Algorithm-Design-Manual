"""
4-4. Assume that we are given n pairs of items as input, where the first item is a number and the 
second item is one of three colors (red, blue, or yellow). Further assume that the items are sorted by number. 
Give an O(n) algorithm to sort the items by color (all reds before all blues before all yellows) 
such that the numbers for identical colors stay sorted. For example: (1,blue), (3,red), (4,blue), 
(6,yellow), (9,red) should become (3,red), (9,red), (1,blue), (4,blue), (6,yellow).
"""


def color_sort(arr):
    result = [None for i in range(len(arr))]    # Init empty array
    r = b = y = 0                               # Init color indexes
    for i in arr:                               # Determine color indexes
        if i[1] == 'red':
            b += 1
            y += 1
        elif i[1] == 'blue':
            y += 1
    for i in arr:                               # Add to next available color index
        if i[1] == 'red':
            result[r] = i
            r += 1
        elif i[1] == 'blue':
            result[b] = i
            b += 1
        else:
            result[y] = i
            y += 1
    return result


# Test case
a = [
    (1, 'blue'),
    (3, 'red'),
    (4, 'blue'),
    (6, 'yellow'),
    (9, 'red'),
    (11, 'blue'),
    (12, 'yellow'),
    (20, 'red')
    ]
print (color_sort(a))
