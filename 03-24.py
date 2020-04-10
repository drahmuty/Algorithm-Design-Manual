"""
Store URL in hash table when it's visited for the first time.
Search the hash table to check if a URL has already been visisted.
"""


# Hash table class
class HashTable:

    # Initialize table
    def __init__(self, size):
        self.size = size
        list = [[] for a in range(self.size)]
        self.list = list
    
    # Hash function
    def get_hash_key(self, x):
        return hash(x) % self.size
    
    # Search table for key
    def search(self, x):
        k = self.get_hash_key(x)
        if x in self.list[k]:
            return True
        return False

    # Insert into table
    def insert(self, x):
        if self.search(x):
            return
        k = self.get_hash_key(x)
        self.list[k].append(x)
    
    # Delete from table
    def delete(self, x):
        if not self.search(x):
            return
        k = self.get_hash_key(x)
        self.list[k].remove(x)


