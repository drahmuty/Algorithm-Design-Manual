class Tree():
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
    
    def show(self):
        out = 'val = ' + str(self.value) + ', '
        out += 'left = ' + str(self.left) + ', '
        out += 'right = ' + str(self.right)
        print(out)

def insert(x, tree):
    if tree is None:
        tree = x
    elif x.value < tree.value:
        if tree.left == None:
            tree.left = x
        else:
            insert(x, tree.left)
    else:
        if tree.right == None:
            tree.right = x
        else:
            insert(x, tree.right)

def traverse(tree):
    if tree == None:
        return
    traverse(tree.left)
    print(tree.value)
    traverse(tree.right)
