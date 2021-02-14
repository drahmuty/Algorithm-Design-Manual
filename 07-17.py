"""Generate all possible words from a given sequence of digits on a telephone keypad."""

# Word list from 'www.ef.edu/english-resources/english-vocabulary/top-3000-words/'.

digit_letter_map = {
    0: ' ',
    1: ' ',
    2: 'ABC',
    3: 'DEF',
    4: 'GHI',
    5: 'JKL',
    6: 'MNO',
    7: 'PQRS',
    8: 'TUV',
    9: 'WXYZ',
}

def phoneword(digits):
    digits_str = ''
    for digit in str(digits):
        if int(digit) > 1:
            digits_str += digit
    backtrack('', -1, digits_str)

def backtrack(a, k, digits):
    if k + 1 == len(digits):
        if WORDS.multi_search(a):
            print(a)
    else:
        k += 1
        letters = digit_letter_map[int(digits[k])]
        for letter in letters:
            if WORDS.partial_search(a + letter):
                a += letter
                backtrack(a, k, digits)
                a = a[:k]



class TrieNode:
    def __init__(self):
        self.children = [None] * 26
        self.is_end_of_word = False


class Trie:
    def __init__(self):
        self.root = self.get_node()

    def get_node(self):
        return TrieNode()

    def char_to_index(self, c):
        i = ord(str(c).lower()) - ord('a')
        if i >= 0 and i < 26:
            return i
        return None

    def insert(self, word):
        c = self.root
        word = word.strip()
        for w in word:
            i = self.char_to_index(w)
            if i is None:
                continue
            if not c.children[i]:
                c.children[i] = self.get_node()
            c = c.children[i]
        c.is_end_of_word = True

    def multi_insert(self, words):
        for word in words:
            self.insert(word)

    def search(self, word):
        c = self.root
        for w in word:
            i = self.char_to_index(w)
            if not c.children[i]:
                return False
            c = c.children[i]
        return c != None and c.is_end_of_word

    # Check if a string of word(s) exists in the trie, either completely or partially.
    def partial_search(self, word):
        c = self.root
        k = len(word)
        last_eow = None
        has_children = True
        for i in range(k):
            w = word[i]
            index = self.char_to_index(w)
            if not c.children[index]:
                has_children = False
                break
            if c.children[index].is_end_of_word:
                last_eow = i + 1
            c = c.children[index]
        if has_children:
            # String is in trie, either as a complete word or partial word with
            # additional children to follow.
            return True
        elif last_eow:
            # Repeat search, excluding preceding complete words.
            return self.partial_search(word[last_eow:])
        else:
            # String is not in trie or does not form a partial word.
            return False

    # Check to make sure string contains fully-formed words only.
    def multi_search(self, string):
        c = self.root
        k = len(string)
        last_eow = None
        out_of_word = False
        for i in range(k):
            s = string[i]
            index = self.char_to_index(s)
            if not c.children[index]:
                out_of_word = True
                break
            if c.children[index].is_end_of_word:
                last_eow = i + 1
            c = c.children[index]
        if not out_of_word and c.is_end_of_word:
            return True
        elif out_of_word and last_eow:
            return self.multi_search(string[last_eow:])
        else:
            return False

    # Show contents of trie.
    def print_trie(self):
        self.print_trie_recur(self.root)

    # Recursive helper function for print_trie
    # This is a quick implementation with an ugly output.
    # It could use some further refining.
    def print_trie_recur(self, x):
        print(x.children)
        if x.is_end_of_word:
            print('EOW')
        for i in range(len(x.children)):
            if x.children[i]:
                self.print_trie_recur(x.children[i])


# Create a trie from a text file of words.
# One word on eaach line.
def init_words(filename):
    with open(filename) as file:
        words = file.readlines()
    t = Trie()
    t.multi_insert(words)
    return t



# Driver program.
WORDS = init_words('words.txt')
phoneword(43556)        # HELLO
phoneword(4663293)      # GOODBYE
phoneword(225563)       # CALLME
