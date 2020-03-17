# Implement a dictionary that performs search, insertion, and deletion in O(1) running time.

class Dict():
    def __init__(self):
        self.list = {}
    
    def search(self, item):
        return self.list[item]
    
    def insert(self, item):
        self.list[item] = item
    
    def delete(self, item):
        del self.list[item]
