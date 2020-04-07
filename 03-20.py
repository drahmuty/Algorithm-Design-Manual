class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def insert(self, data):
        if self.head:
            temp = self.head
            self.head = Node(data)
            self.head.next = temp
        else:
            self.head = Node(data)
    
    def print_list(self):
        head = self.head
        while head:
            print(head.data)
            head = head.next

    def find_middle_node(self):
        # Count all nodes
        i = j = 0
        head = self.head
        while head:
            head = head.next
            i += 1
        i //= 2
        # Return middle node
        head = self.head
        while j < i:
            head = head.next
            j += 1
        return head


z = LinkedList()
for i in range(0, 100):
    z.insert(i)
