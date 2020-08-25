"""
Flapjack challenge.
http://citeseerx.ist.psu.edu/viewdoc/download?doi=10.1.1.111.2131&rep=rep1&type=pdf
"""
def flapjack(stack):
    
    # Return list if sorted
    if(all(stack[i] <= stack[i + 1] for i in range(len(stack)-1))):
        return stack

    # Find max index
    max = None
    max_index = None
    for a in range(len(stack)):
        if not max:
            max = stack[a]
            max_index = a
            continue
        if stack[a] > max:
            max = stack[a]
            max_index = a

    # Flip to top
    top = stack[:max_index+1]
    bottom = stack[max_index+1:]
    top.reverse()
    stack = top + bottom
    print('Flip at ' + str(max_index))
    
    # Flip to bottom
    stack.reverse()
    print('Flip at ' + str(len(stack)-1))

    # Combine result into final list
    return flapjack(stack[:len(stack)-1]) + stack[len(stack)-1:]


# Test cases
a = [1,2,3,4,5]
b = [5,4,3,2,1]
c = [5,1,2,3,4]
d = [5,2,1,4,3,9,6,8,7]
