"""
3-29. 
Give an algorithm for finding an ordered word pair (e.g., New York) 
occurring with the greatest frequency in a given webpage. 
Which data structures would you use? Optimize both time and space.

I would use a hash table. 
1. Store each consecutive pair of words as a value in hash table.
2. Find max.
O(n) runtime and O(n) space.

"""

def max_pair():
    f = File('nyc.txt')
    t = HashTable(10000)
    word1 = f.get_next_word()
    word2 = f.get_next_word()
    while word2:
        t.insert(word1 + ' ' + word2)
        word1 = word2
        word2 = f.get_next_word()
    print(t.max_val + ' (' + str(t.max_count) + ')')


# Text file class
class File:
    def __init__(self, x):
        with open (x) as file_obj:
            self.string = str(file_obj.read().strip())
        self.length = len(self.string)
        self.index = 0

    # Get next word, skipping spaces and symbols
    def get_next_word(self):
        i = self.index
        j = self.length
        s = self.string
        next_word = ''
        in_word = False
        while i < j:
            c = s[i]
            cval = ord(c.upper())
            if cval < 65 or cval > 90:
                i += 1
                if in_word:
                    break
                continue
            else:
                in_word = True
                next_word += c
                i += 1
        self.index = i
        return next_word


# Hash table class
class HashTable:
    def __init__(self, size):
        self.size = size
        array = [[None, 0] for a in range(self.size)]
        self.array = array
        self.max_key = None
        self.max_val = None
        self.max_count = 0

    def get_key(self, x):
        return hash(x) % self.size
    
    def insert(self, x):
        key = self.get_key(x)
        if not self.array[key][0]:
            self.array[key][0] = x
            self.array[key][1] = 1
        elif self.array[key][0] == x:
            self.array[key][1] += 1
        if self.array[key][1] > self.max_count:
            self.max_key = key
            self.max_val = self.array[key][0]
            self.max_count = self.array[key][1]
