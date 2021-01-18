from collections import defaultdict


def backtrack(a, k, data):
    if is_a_solution(a, k, data):
        process_solution(a, k, data)
    else:
        k += 1
        candidates = construct_candidates(a, k, data)
        for c in candidates:
            a[k] = c
            backtrack(a, k, data)
            a[k] = None


def is_a_solution(a, k, data):
    solution = ""
    if k == len(a)-1:
        for letter in a:
            solution += letter
        if WORDS.search(solution):
            return True
    return False


def process_solution(a, k, data):
    solution = ""
    for s in a:
        solution += str(s)
    print("SOLUTION:", solution)


def construct_candidates(a, k, data):
    string = data[0]
    count = data[1]
    used_count = defaultdict(int)
    in_candidates = defaultdict(bool)
    sol = ""
    is_a_word = False
    c = []
    for i in a:
        if i:
            used_count[i] += 1
            sol += i
    for s in string:
        if used_count[s] < count[s] and not in_candidates[s]:
            is_a_word = WORDS.partial_search(sol+s)
            if is_a_word:
                c.append(s)
                in_candidates[s] = True
    return c


class TrieNode:
    def __init__(self):
        self.children = [None]*26
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
                last_eow = i+1
            c = c.children[index]
        # String is in trie, either as a compelete word or partial word with 
        # additional children to follow. 
        if has_children:
            return True
        # Repeat search, excluding preceding complete words.
        elif last_eow:
            return self.partial_search(word[last_eow:])
        # String is not in trie or does not form a partial word.
        else:
            return False
    
    # Show contents of trie.
    def print_trie(self):
        self.print_trie_recur(self.root)
        
    # Recursive helper function for pritn_trie
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
def init_words():
    with open('words.txt') as file:
        words = file.readlines()
    t = Trie()
    t.multi_insert(words)
    return t


# Main program - Find all anagrams of a given word.
def anagrams(string):

    print("Anagrams for " + str(string) + ":")

    # Solution array.
    a = [None for i in range(len(string))]

    # Dictionary of letters and their frequency.
    count = defaultdict(int)
    for s in string:
        count[s] += 1
    
    # Generate all permutations.
    backtrack(a, -1, (string, count))

    print()


# Init word list.
global WORDS
WORDS = init_words()

# Test cases
anagrams('art')
anagrams('dog')
anagrams('ads')
anagrams('angel')
anagrams('alto')
anagrams('this')
anagrams('team')
anagrams('mood')
anagrams('bowl')
anagrams('dad')
