import random


# Binary tree class
class Tree:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

    def insert(self, x):
        if x < self.data:
            if self.left:
                return self.left.insert(x)
            else:
                self.left = Tree(x)
                return True
        elif x > self.data:
            if self.right:
                return self.right.insert(x)
            else:
                self.right = Tree(x)
                return True
        else:
            return False

    def search(self, x):
        if x < self.data:
            if self.left:
                return self.left.search(x)
            else:
                return False
        elif x > self.data:
            if self.right:
                return self.right.search(x)
            else:
                return False
        else:
            return True

    def show(self):
        if self.left:
            self.left.show()
        print(self.data)
        if self.right:
            self.right.show()
    

# Function to compare two binary trees for identicality 
def compare(a, b):
    if compare_helper(a, b) > 0:
        return False
    else:
        return True

# Recursive helper function for compare function
def compare_helper(a, b):
    c = 0
    if a.data != b.data:
        return 1
    if a.left and b.left:
        c += compare_helper(a.left, b.left)
    elif not a.left and not b.left:
        pass
    else:
        return 1
    if a.right and b.right:
        c += compare_helper(a.right, b.right)
    elif not a.right and not b.right:
        pass
    else:
        return 1
    return c


# Generate two identical trees for testing
t1 = Tree(50)
t2 = Tree(50)
for x in range(10):
    y = random.randint(1,100)
    t1.insert(y)
    t2.insert(y)

# Generate two nonidentical trees for testing
t3 = Tree(50)
t4 = Tree(50)
for x in range(5):
    y = random.randint(1,100)
    z = random.randint(1,100)
    t3.insert(y)
    t4.insert(z)

# Test cases
print(compare(t1, t2))
print(compare(t3, t4))
print(compare(t1, t3))
print(compare(t2, t4))
print(compare(Tree(1), Tree(1)))
