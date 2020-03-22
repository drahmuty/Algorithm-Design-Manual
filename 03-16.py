# Characters to skip
skip = [' ', '\n', '\t', '.', ',', ':', ';', '?', '!']

# Main function
def main():
    doc = Doc('file.txt')
    words = LinkedList()
    w = doc.next_word()
    while w:
        if not words.search(w):
            words.insert(w)
        w = doc.next_word()
    words.array()
    return

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
    
    def show(self):
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
            
            
# Main function (first version, using functional programming)
# def words(file):
#     with open(file) as file_object:
#         contents = file_object.read().strip()
#         d = LinkedList()
#         word = ''
#         for c in contents:
#             if c in skip:
#                 if word and not d.search(word):
#                     d.insert(word)
#                 word = ''
#                 continue
#             else:
#                 word += c
#     d.array()
