"""
3-27. 
Determine whether a linked list contains a loop 
as quickly as possible without using any extra storage. 
Also, identify the location of the loop.

I had to look up the solution (in pseudo-code).
Below is my own implementation.

"""

# Find loop in linked list
def findloop(x):
    if not x.head:
        return False                # Head does not exist
    slow = x.head
    fast = x.head.next
    while True:
        if not fast:
            return False
        elif (fast == slow):
            break                   # Loop exists; Continue with rest of program
        elif fast.next:
            slow = slow.next
            fast = fast.next.next
        else:
            return False
    fast = fast.next    
    loop_len = 1
    while fast != slow:
        fast = fast.next
        loop_len += 1
    slow = fast = x.head
    for i in range(loop_len):
        fast = fast.next
    while fast != slow:
        slow = slow.next
        fast = fast.next
    return fast


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


# Driver program
z = LinkedList()
for i in range(4,0,-1):                     # Build normal linked list
    z.insert(i)
print('Contents of z:')
z.show()
print('Start location of loop:')
print(findloop(z))
z.head.next.next.next.next = z.head.next    # Create loop in linked list
print('Start location of loop:')
print(findloop(z).data)
