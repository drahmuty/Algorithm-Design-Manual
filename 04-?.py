"""
Flapjack challenge.
http://citeseerx.ist.psu.edu/viewdoc/download?doi=10.1.1.111.2131&rep=rep1&type=pdf
"""

def flapjack(stack):
    
    # Return list if sorted
    if(all(stack[i] <= stack[i + 1] for i in range(len(stack)-1))):
        print('sorted')
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
    
    # Flip to bottom
    stack.reverse()

    # Sort remaining stack and cobine with sorted bottom
    return flapjack(stack[:len(stack)-1]) + stack[len(stack)-1:]
