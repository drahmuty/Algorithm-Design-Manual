# Characters to skip
skip = [' ', '\n', '\t', '.', ',', ':', ';', '?', '!']

# Main function
def main():
    doc = Doc('file.txt')
    words_list = LinkedList()
    w = doc.next_word()
    words_tree = Tree(w)
    while w:
        words_list.insert(w.lower())
        words_tree.insert(w.lower())
        w = doc.next_word()
    
    print('\nLINKED LIST:')
    words_list.print_items()
    print('\nBINARY TREE:')
    words_tree.print_items()

# Document class
class Doc():
    def __init__(self, filename):
        with open(filename) as file_obj:
            self.contents = file_obj.read().strip()
        self.index = 0
        self.length = len(self.contents)

    def next_word(self):
        word = ''
        stop = False
        while self.index < self.length:
            c = self.contents[self.index]
            if c in skip:
                if stop:
                    return word
                self.index += 1
                continue
            stop = True
            word += c
            self.index += 1
    
# Node class
class Node():
    def __init__(self, value):
        self.value = value
        self.next = None
        
# Linked list class
class LinkedList():
    def __init__(self):
        self.head = None
    
    def print_items(self):
        c = self.head
        while c:
            print(c.value)
            c = c.next
        
    def array(self):
        arr = []
        c = self.head
        while c:
            arr.append(c.value)
            c = c.next
        print(arr)
            
    def search(self, value):
        c = self.head
        while c:
            if c.value == value:
                return True
            c = c.next
        return False            

    def insert(self, value):
        if self.search(value):
            return
        temp = self.head
        self.head = Node(value)
        self.head.next = temp
    
    def delete(self, value):
        prev = None
        c = self.head
        while c:
            if c.value == value:
                if prev:
                    prev.next = c.next
                else:
                    self.head = c.next
                return
            prev = c
            c = c.next

# Binary tree class
class Tree():
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
    
    def search(self, value):
        if not self:
            return False
        if value < self.value:
            if self.left:
                return self.left.search(value)
            else:
                return False
        elif value > self.value:
            if self.right:
                return self.right.search(value)
            else:
                return False
        else:
            return True
    
    def insert(self, value):
        if value < self.value:
            if self.left:
                self.left.insert(value)
            else:
                self.left = Tree(value)
        elif value > self.value:
            if self.right:
                self.right.insert(value)
            else:
                self.right = Tree(value)

    def print_items(self):
        if self.left:
            self.left.print_items()
        print(self.value)
        if self.right:
            self.right.print_items()
