letter_frequency_list = ('E','T','A','O','I','N','S','R','H','D','L','U','C','M','F','Y','W','G','P','B','V','K','X','Q','J','Z')

# Encrypt file
def encrypt(x):
    with open('moby.txt') as file_obj:
        contents = file_obj.read().strip()
    encrypted_contents = cshift(contents, x)
    with open('encrypted_file.txt', 'w') as file_w:
        file_w.write(encrypted_contents)
    # doc = Doc('encrypted_file.txt')
    # t = HashTable()
    # w = doc.next_word()
    # while w:
    #     t.insert(w)
    #     w = doc.next_word()
    # print(t.print_items())

# Decryption program
def decrypt():

    # Open file
    with open('encrypted_file.txt') as file_obj:
        contents = file_obj.read().strip()
    
    # Store each letter and its count in a hash table
    letter_table = HashTable()
    for c in contents:
        letter_table.insert(c)

    # Create ordered list by letter count
    letter_table_sorted = []
    c = letter_table.max_pop()
    while c:
        letter_table_sorted.append(c)
        c = letter_table.max_pop()

    # Pair letter with ordered list of letter frequency
    letter_pairs = HashTablePairs()
    i = 0
    for c in letter_table_sorted:
        old = c[0]
        new = letter_frequency_list[i]
        letter_pairs.insert((old, new))
        i += 1
     
    # Replace each letter with its paired letter
    decrypted_contents = ''
    for c in contents:
        new = letter_pairs.search(c)
        if new:
            c = new
        decrypted_contents += c

    # Print contents of file
    print(decrypted_contents)

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

# Hash table class for storing letter count
class HashTable:
    def __init__(self):
        self.size = 26
        table = [0 for a in range(self.size)]
        self.dict = table

    def hash(self, x):
        return (ord(x) - 65) % self.size

    def insert(self, x):
        if ord(x) < 65 or ord(x) > 90:
            return
        k = self.hash(x)
        self.dict[k] += 1

    def search(self, x):
        k = self.hash(x)
        if self.dict[k] > 0:
            return True
        else:
            return False
    
    def delete(self, x):
        if not self.search(x):
            print(str(x) + ' not found')
        else:
            k = self.hash(x)
            self.dict[k] = 0

    def max(self):
        k = max_key = 0
        max_val = 0
        for d in self.dict:
            if d > max_val:
                max_key = k
                max_val = d
            k += 1
        return max_key, max_val

    def max_pop(self):
        max = self.max()
        max_key = chr(max[0] + 65)
        max_val = max[1]
        if max_val < 1:
            return None
        self.delete(max_key)
        return max_key, max_val


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

def replace_letter(string, old, new):
    new_string = ''
    for s in string:
        if s == old:
            s = new
        new_string += s
    return new_string

# Hash table to store old-new letter pairs
class HashTablePairs:
    def __init__(self):
        self.size = 1000
        table = [None for a in range(self.size)]
        self.dict = table

    def hash(self, x):
        return hash(x) % self.size

    def insert(self, x):
        k = self.hash(x[0])
        self.dict[k] = x[1]
    
    def search(self, x):
        k = self.hash(x)
        if self.dict[k]:
            return self.dict[k]
        else:
            return False
