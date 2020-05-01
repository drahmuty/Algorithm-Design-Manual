class Waldorf:
    def __init__(self, array):
        # self.grid = [
        #     'abcDEFGhigg',
        #     'hEbkWalDork',
        #     'FtyAwaldORm',
        #     'FtsimrLqsrc',
        #     'byoArBeDeyv',
        #     'Klcbqwikomk',
        #     'strEBGadhrb',
        #     'yUiqlxcnBjf'
        # ]
        self.grid = array
        self.l = len(self.grid)
        self.w = len(self.grid[0])

    def search(self, key):
        key_len = len(key)
        key_rev = key[::-1]
        grid = self.grid
        row = col = 0
        while row < self.w:
            while col < self.w:
                if key[0].lower() == grid[row][col].lower():
                    if self.search_h(key, row, col) or \
                       self.search_v(key, row, col) or \
                       self.search_dr(key, row, col) or \
                       self.search_dl(key, row, col):
                        return row, col
                    else:
                        col += 1
                elif key[key_len - 1].lower() == grid[row][col].lower():
                    if self.search_h(key_rev, row, col):
                        dir = 'h'
                    elif self.search_v(key_rev, row, col):
                        dir = 'v'
                    elif self.search_dr(key_rev, row, col):
                        dir = 'd'
                    elif self.search_dl(key_rev, row, col):
                        dir = 'dr'
                    else:
                        col += 1
                        continue
                    return self.endpoint(row, col, dir, key_len)
                else:
                    col += 1
            col = 0
            row += 1
        return False
    
    # Horizontal right search
    def search_h(self, key, row, col):
        if key.lower() in self.grid[row][col:].lower():
            return True
        else:
            return False
    
    # Vertical down search
    def search_v(self, key, row, col):
        key_len = len(key)
        i = 0
        while row < self.l and i < key_len:
            if key[i].lower() != self.grid[row][col].lower():
                return False
            else:
                i += 1
                row += 1
        if i == key_len:
            return True
        else:
            return False

    # Diagonal right down search
    def search_dr(self, key, row, col):
        key_len = len(key)
        i = 0
        while row < self.l and col < self.w and i < key_len:
            if key[i].lower() != self.grid[row][col].lower():
                return False
            else:
                i += 1
                row += 1
                col += 1
        if i == key_len:
            return True
        else:
            return False
    
    # Diagonal left down search
    def search_dl(self, key, row, col):
        key_len = len(key)
        i = 0
        while row < self.l and col > -1 and i < key_len:
            if key[i].lower() != self.grid[row][col].lower():
                return False
            else:
                i += 1
                row += 1
                col -= 1
        if i == key_len:
            return True
        else:
            return False
    
    # Calculate vector endpoint
    def endpoint(self, row, col, dir, len):
        x = len - 1
        if dir == 'h':
            return row, col + x
        elif dir == 'v':
            return row + x, col
        elif dir == 'd':
            return row + x, col + x
        elif dir == 'dr':
            return row - x, col - x
        else:
            return None



# z = Waldorf()

# def remove_tabs_from_text_file(x):
#     with open(x) as file_obj:
#         contents = file_obj.read().strip().replace('\t', '')
#     with open(x, 'w') as file_obj:
#         file_obj.write(contents)

# remove_tabs_from_text_file('word_search_puzzle.txt')

# Create word search puzzle grid
with open('word_search_puzzle.txt') as file_obj:
    contents = file_obj.read()
i = 1
x = ''
y = []
for c in contents:
    if c == '\n' or c == ' ':
        continue
    elif i % 25 == 0:
        x += c
        y.append(x)
        x = ''
    else:
        x += c
    i += 1

z = Waldorf(y)
keys = [
    'DAVE',
    'HELLO',
    'CODING',
    'FUN',
    'BICYCLE',
    'GUITAR',
    'QUARANTINE',
    'GOOGLE',
    'RUNNING',
    'YOGA',
    'VEGAN',
    'PIANO',
    'PINKFLOYD',
    'MEDITATE'
]
for k in keys:
    print(k, z.search(k))
