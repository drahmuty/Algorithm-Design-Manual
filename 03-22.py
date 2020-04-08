import random



# Binary tree class
class Tree:

    # Initialize node
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

    # Insert item into tree
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

    # Search for item in tree
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

    # Print all node values in tree
    def show(self):
        if self.left:
            self.left.show()
        print(self.data)
        if self.right:
            self.right.show()



# Linked list node class
class LinkedListNode:

    # Initialize node
    def __init__(self, data):
        self.data = data
        self.next = None



# Linked list class
class LinkedList:

    # Initialize list
    def __init__(self):
        self.head = None
    
    # Insert item into list
    def insert(self, x):
        new_node = LinkedListNode(x)
        new_node.next = self.head
        self.head = new_node
    
    # Print all items in linked list
    def show(self):
        c = self.head
        while c:
            print(c.data)
            c = c.next



# Convert binary tree to linked list
def tree_to_list(t):

    # Initialize empty linked list
    linked_list = LinkedList()
    
    # Use recursive helper function to traverse tree and insert each node value into linked list
    return tree_to_list_helper(t, linked_list)

# Helper function to convert binary tree to linked list
# This can also be used standalone if you provide an existing linked list
def tree_to_list_helper(t, l):
    if t.left:
        tree_to_list_helper(t.left, l)
    l.insert(t.data)
    if t.right:
        tree_to_list_helper(t.right, l)
    return l
    


# Create binary tree for testing
z = Tree(50)
for x in range(100):
    z.insert(random.randint(1,10000))
