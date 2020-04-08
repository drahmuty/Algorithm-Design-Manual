
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


# Create linked list for testing
z = LinkedList()
for i in range(1,10):
    z.insert(i)
print('Contents of z:')
z.show()


# Reverse linked list, with recursion
def reverse_list(x):
    p = None
    c = x.head
    while c:
        n = c.next
        c.next = p
        p = c
        c = n
    x.head = p
