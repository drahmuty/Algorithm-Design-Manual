# Program to check for proper parantheses pairing and nesting

def foo(x):
    # make sure there are the same total number of ( and )
    # make sure ( comes before )
    string = str(x)
    c = l = r = 0
    for s in string:
        c += 1
        if s == '(':
            l += 1
        elif s == ')':
            r += 1
        if r > l:
            return 'error at ' + str(c)
    if l == r:
        return 'valid'
    else:
        return 'error: missing one or more )'
