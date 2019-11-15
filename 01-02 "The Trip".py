# n = number of students (we can eliminate this variable and just use the length of the list)
# exp = list of expenses for each student

def trip(exp):
    y = 0
    avg = sum(exp) / len(exp)
    for e in exp:
        if e < avg:
            y += avg - e
    return y
