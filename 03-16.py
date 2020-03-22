# Characters to skip
skip = [' ', '\n', '\t', '.', ',', ':', ';', '?', '!']

# Main function
def words(file):
    with open(file) as file_object:
        contents = file_object.read().strip()
        word = ''
        for c in contents:
            if c in skip:
                print(word)
                # insert(word)
                word = ''
                continue
            else:
                word += c

# words('file.txt')


# Linked list
class linked_list():
    
    def __init__(self, value):
        self.value = value
        self.next = None
    
    def insert(self, value):
        if self.next == None:
            self.next = linked_list(value)
        else:
            self.next.insert(value)

    def search(self, value):
        if self.value == value:
            return True
        elif self.next == None:
            return False
        else:
            return self.next.search(value)

    def show(self):
        if self.next == None:
            print(self.value)
            return
        print(self.value)
        self.next.show()
    
    def delete(self, value, prev = None):
        if self.value == value:
            if prev == None:
                self = None
            else:
                prev.next = self.next
        elif self.next == None:
            return
        else:
            self.next.delete(value, self)


x = linked_list(1)
x.insert(2)
x.insert(3)
x.insert(4)



# Attempt 2

class Node():
    def __init__(self, value):
        self.value = value
        self.next = None

class LinkedList():
    def __init__(self):
        self.head = None

    def insert(self, value):
        temp = self.head
        self.head = Node(value)
        self.head.next = temp
    
    def show(self):
        c = self.head
        while c:
            print(c.value)
            c = c.next
    
    def search(self, value):
        c = self.head
        while c:
            if c.value == value:
                return True
            c = c.next
        return False
    
    def delete(self, value):
        prev = None
        c = self.head
        while c:
            if c.value == value:
                prev.next = c.next
                return
            
        

x = LinkedList()
for i in range(0,10):
    x.insert(i)
