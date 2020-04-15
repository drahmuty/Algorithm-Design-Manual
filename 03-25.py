# Determine if magazine contains all leters in search string
def mag_search(string, magazine):

    # Create hash table to count each char in search string
    string_table = AsciiHashTable()
    for s in string:
        string_table.inc(s)

    # Loop through magazine string
    for m in magazine:

        # If all chars found, return True    
        if string_table.sum < 1:
            return True

        # If char in string_table, decrement count        
        if string_table.search(m):
            string_table.dec(m)
    
    # Final check to see if all chars found
    if string_table.sum < 1:
        return True
    else:
        return False


# Hash table class for counting ASCII characters
class AsciiHashTable:
    
    # Initialize array for all 256 ASCII chars
    def __init__(self):
        array = [0 for a in range(256)]
        self.arr = array
        self.sum = 0

    # Search for key in table
    def search(self, x):
        if self.arr[ord(x)] > 0:
            return True
        else:
            return False
    
    # Increment char count and total count
    def inc(self, x):
        self.arr[ord(x)] += 1
        self.sum += 1
    
    # Decrement char count and total count
    def dec(self, x):
        if self.arr[ord(x)] > 0:
            self.arr[ord(x)] -= 1
            self.sum -= 1


# Driver program
search_string = 'superfluous'
magazine = 'This is a magazine. It contains lots of words about fun and interesting topics around the world.'
print(mag_search(search_string, magazine))
