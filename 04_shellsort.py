from collections import OrderedDict

def shellsort(x, y):
    # x = original list
    # y = list in desired order

    # We need to map the desired order values
    # to the original list. We'll do that using
    # a hash table (dictionary).

    # Store items in dictionary
    x_dict = OrderedDict()
    for item in x:
        x_dict[item] = None
    
    # Enumerate sorted list and add order to dictionary
    y_order = enumerate(y)
    for order, item in y_order:
        x_dict[item] = order

    # Find first max out of order
    prev = None
    first_max = None
    for item, order in x_dict.items():
        if not prev:
            prev = order
        elif order < prev:
            first_max = prev
            break
        else:
            prev = order
    
    # All items less than first max crawl to top in desc order
    for i in range(first_max-1, -1, -1):
        print(y[i])
    



# Driver program
x1 = ['y', 'd', 's']
y1 = ['d', 'y', 's']
print(x1)
print(y1)
shellsort(x1, y1)
print()

x2 = ['y', 'd', 's', 'e', 'me', 'rmn', 'mr', 'f', 'mack']
y2 = ['y', 'rmn', 's', 'd', 'e', 'me', 'mr', 'f', 'mack']
print(x2)
print(y2)
shellsort(x2, y2)
print()

x3 = [2, 4, 1, 3, 5]
y3 = [1, 2, 3, 4, 5]
print(x3)
print(y3)
shellsort(x3, y3)
print()
