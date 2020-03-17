# Define node class
class Node():
    def __init__(self, value):
        self.value = value
        self.next = None

# Define linked list class
class LinkedList():
    def __init__(self):
        self.head = None

# Generate a linked list
x = LinkedList()
x.head = Node(1)
y = 2
target = x.head
while True:
    if y > 10:
        break
    target.next = Node(y)
    target = target.next
    y += 1

# Print a linked list
def printList(list):
    current = list.head
    while current != None:
        print(current.value)
        current = current.next
        
# Reverse a linked list
def revList(list):
    prev = None
    curr = list.head
    while curr =! None:
        next = curr.next
        curr.next = prev
        prev = curr
        curr = next
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
