# Main program
def main(x):
    with open('file.txt') as file_obj:
        contents = file_obj.read().strip()
    encrypted_contents = cshift(contents, x)
    with open('encrypted_file.txt', 'w') as file_w:
        file_w.write(encrypted_contents)
    doc = Doc('encrypted_file.txt')
    t = HashTable()
    w = doc.next_word()
    while w:
        t.insert(w)
        w = doc.next_word()
    print(t.print_items())

# Decryption program
def decrypt():
    with open('encrypted_file.txt') as file_obj:
        contents = file_obj.read().strip()

# Dictionary data structure
class Dict:
    def __init__(self):
        self.dict = {}
        self.keys = self.dict.keys()
    
    def search(self, x):
        if x in self.keys:
            return True
        else:
            return False
    
    def insert(self, x):
        if self.search(x):
            self.dict[x] += 1
        else:
            self.dict[x] = 1

# Caesar shift (text = string; x = integer shift value)
def cshift(text, x):
    text_shifted = ''
    for t in text:
        t = t.upper()               # Convert to uppercase
        tn = ord(t)                 # Get Ascii value
        if tn > 64 and tn < 91:     # Check for letter character
            t = chr(((tn + x - 65) % 26) + 65)
        text_shifted += t
    return text_shifted

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

# Document class
class Doc():
    def __init__(self, filename):
        with open(filename) as file_obj:
            self.contents = file_obj.read().strip()
        self.index = 0
        self.length = len(self.contents)
        self.word_count = 0
        self.skip = [' ', '\n', '\t', '.', ',', ':', ';', '?', '!']

    def next_word(self):
        word = ''
        stop = False
        while self.index < self.length:
            c = self.contents[self.index]
            if c in self.skip:
                if stop:
                    self.word_count += 1
                    return word
                self.index += 1
                continue
            stop = True
            word += c
            self.index += 1
