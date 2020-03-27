# Encrypt file
def encrypt(x):
    with open('file.txt') as file_obj:
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
    
    # Count each letter and store in dictionary
    letter_table = HashTable()
    for c in contents:
        letter_table.insert(c)
    
    # Print dictionary
    print(letter_table.dict)

    # Insert dictionary items into binary tree

    # Return ordered list by letter count
        # Pair letter with ordered list of letter frequency
    
    # Replace letters with their paired letter

    # Print contents of file
    
    

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
