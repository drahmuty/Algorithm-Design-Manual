class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
    
    def insert(self, x):
        if self.data:
            if x < self.data:
                if not self.left:
                    self.left = Node(x)
                else:
                    self.left.insert(x)
            else:
                if not self.right:
                    self.right = Node(x)
                else:
                    self.right.insert(x)
        else:
            self.data = x

a = Node(4)
a.insert(2)
a.insert(6)
a.insert(1)
a.insert(3)
a.insert(5)
a.insert(7)


n = 0
ith_node_value = None

def find_ith_node(tree, i):
    global n
    global ith_node_value
    if tree.left:
        find_ith_node(tree.left, i)
    n += 1
    if n == i:
        if not ith_node_value:
            ith_node_value = tree.data
    if tree.right:
        find_ith_node(tree.right, i)

find_ith_node(a, 5)
print(y)
