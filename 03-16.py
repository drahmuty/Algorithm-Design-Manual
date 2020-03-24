# Characters to skip
skip = [' ', '\n', '\t', '.', ',', ':', ';', '?', '!']

# Main function
def main():
    doc = Doc('file.txt')
    w = doc.next_word()
    words_list = LinkedList()
    words_tree = Tree(w)
    words_hash = HashTable()
    while w:
        words_list.insert(w.lower())
        words_tree.insert(w.lower())
        words_hash.insert(w.lower())
        w = doc.next_word()
    print('\nLINKED LIST:')
    words_list.print_items()
    print(words_list.item_count())
    print('\nBINARY TREE:')
    words_tree.print_items()
    print(tree_count(words_tree))
    print('\nHASH TABLE:')
    words_hash.print_items()
    print(words_hash.item_count)


# Document class
class Doc():
    def __init__(self, filename):
        with open(filename) as file_obj:
            self.contents = file_obj.read().strip()
        self.index = 0
        self.length = len(self.contents)
        self.word_count = 0

    def next_word(self):
        word = ''
        stop = False
        while self.index < self.length:
            c = self.contents[self.index]
            if c in skip:
                if stop:
                    self.word_count += 1
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
    
    def item_count(self):
        i = 0
        c = self.head
        while c:
            i += 1
            c = c.next
        return i

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

def tree_count(tree):
    i = 0
    if tree:
        i += 1
    if tree.left:
        i += tree_count(tree.left)
    if tree.right:
        i += tree_count(tree.right)
    return i
    
def tree_list(tree):
    arr = []
    def helper(x):
        if x.left:
            helper(x.left)
        arr.append(x.value)
        if x.right:
            helper(x.right)
    helper(tree)
    return arr
    

# Hash table class
class HashTable:
    def __init__(self):
        self.size = 1000
        table = [[] for a in range(self.size)]
        self.dict = table
        self.item_count = 0

    def hash(self, x):
        return hash(x) % self.size

    def insert(self, x):
        if self.search(x):
            return
        k = self.hash(x)
        self.dict[k].append(x)
        self.item_count += 1

    def search(self, x):
        k = self.hash(x)
        for v in self.dict[k]:
            if v == x:
                return True
        return False
    
    def delete(self, x):
        if not self.search(x):
            print(str(x) + ' not found')
            return
        k = self.hash(x)
        self.dict[k].remove(x)
        self.item_count -= 1

    def print_items(self):
        for x in self.dict:
            for y in x:
                print(y)
