"""
3-26. 
Reverse the words in a sentence.
i.e., My name is Chris becomes Chris is name My.
Optimize for time and space.

"""

# Reverse the words in a sentence
def reverse_sentence(sentence):

    # Create sentence object and linked list
    sentence_obj = Sentence(sentence)
    sentence_list = LinkedList()

    # Add each word to linked list
    word = sentence_obj.get_next_word()
    while word:
        sentence_list.insert(word)
        word = sentence_obj.get_next_word()

    # Reconstruct sentence using LIFO order
    sentence_reversed = ''
    word = sentence_list.pop()
    while word:
        sentence_reversed += word
        word = sentence_list.pop()
    return sentence_reversed

# Sentence class
class Sentence:
    def __init__(self, string):
        self.string = str(string)
        self.length = len(self.string)
        self.index = 0

    # Get next word or string of symbols
    def get_next_word(self):
        i = self.index
        j = self.length
        s = self.string
        y = ''
        word = False
        symbol = False
        while i < j:
            c = s[i]
            if ord(c.upper()) < 65 or ord(c.upper()) > 90:
                if word:
                    break
                symbol = True
            else:
                if symbol:
                    break
                word = True
            y += c
            i += 1
        self.index = i
        return y
            

# Linked list node class
class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

# Linked list class
class LinkedList:

    # Initialize linked list
    def __init__(self):
        self.head = None

    # Insert into list
    def insert(self, x):
        new_node = Node(x)
        if self.head:
            new_node.next = self.head
            self.head = new_node
        else:
            self.head = new_node
    
    # Return/remove first item from list
    def pop(self):
        if self.head:
            top = self.head.value
            self.head = self.head.next
            return top
        else:
            return None

# Driver program
a = reverse_sentence('Hello, world!')
b = reverse_sentence('This is the greatest Saturday of my life! You just wait and see. - Dave')
print(a)
print(b)
