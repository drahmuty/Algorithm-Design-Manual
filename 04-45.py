"""
4-45. Given a search string of three words, find the smallest snippet of the document 
that contains all three of the search words---i.e., the snippet with smallest number 
of words in it. You are given the index positions where these words occur in the document, 
such as word1: (1, 4, 5), word2: (3, 9, 10), and word3: (2, 6, 15). Each of the lists are 
in sorted order, as above.
"""



def snippet(arr1, arr2, arr3):
    low = None
    mid = None
    high = None
    new = None
    min_length = None
    snippet_indexes = None
    while True:
        a = None 
        b = None
        c = None
        # Merge three arrays
        if arr1 and arr2 and arr3:
            a = arr1[0]
            b = arr2[0]
            c = arr3[0]
            if a < b and a < c:
                new = ('A', a)
            elif b < a and b < c:
                new = ('B', b)
            else:
                new = ('C', c)
        elif arr1 and arr2:
            a = arr1[0]
            b = arr2[0]
            if a < b:
                new = ('A', a)
            else:
                new = ('B', b)
        elif arr1 and arr3:
            a = arr1[0]
            c = arr3[0]            
            if a < c:
                new = ('A', a)
            else:
                new = ('C', c)
        elif arr2 and arr3:
            b = arr2[0]
            c = arr3[0]            
            if b < c:
                new = ('B', b)
            else:
                new = ('C', c)
        elif arr1:
            a = arr1[0]
            new = ('A', a)
        elif arr2:
            b = arr2[0]
            new = ('B', b)
        elif arr3:
            c = arr3[0]
            new = ('C', c)
        else:
            break
        
        # Remove item from min list
        if new[0] == 'A':
            arr1.pop(0)
        elif new[0] == 'B':
            arr2.pop(0)
        else:
            arr3.pop(0)

        # Fill if list is not full
        if not low and not mid:
            low = new
            continue
        elif not mid:
            if low[0] == new[0]:
                low = new
            else:
                mid = new
            continue

        # Determine what to do with new value
        if new[0] == low[0]:
            low = mid
            mid = new
            continue
        elif new[0] == mid[0]:
            mid = new
            continue
        else:
            high = new
        
        # Calculate snippet length and determine if it's the smallest
        length = high[1] - low[1] + 1
        if not min_length or length < min_length:
            min_length = length
            snippet_indexes = (low, mid, high)
        
        # Shift down for next iteration
        low = mid
        mid = high
        high = None

    return snippet_indexes, min_length


word1 = [1, 4, 5, 25]
word2 = [8, 9, 10, 20]
word3 = [2, 14, 15, 30]

print(snippet(word1, word2, word3))
