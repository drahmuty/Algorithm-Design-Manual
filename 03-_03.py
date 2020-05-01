class Waldorf:
    def __init__(self):
        self.grid = [
            'abcDEFGhigg',
            'hEbkWalDork',
            'FtyAwaldORm',
            'FtsimrLqsrc',
            'byoArBeDeyv',
            'Klcbqwikomk',
            'strEBGadhrb',
            'yUiqlxcnBjf'
        ]
        self.l = len(self.grid)
        self.w = len(self.grid[0])

    def search(self, key):
        keylen = len(key)
        grid = self.grid
        row = col = 0
        while row < self.w:
            while col < self.w:
                if key[0] == grid[row][col]:
                    # check four directions
                    if (
                        self.search_h(key)
                        or self.search_v(key)
                        or self.search_d(key)
                        or self.search_dr(key)
                    )
                    if True:
                        return row, col
                elif key[keylen - 1] == grid[row][col]:
                    # reverse key
                    # check four directions
                    # return ending coordinates
                    # calc using keylen and direction
                    return row, col
                else:
                    col += 1
            row += 1
        return False
    
    def search_h(self, key):
        return
    
    def search_v(self, key):
        return

    def search_d(self, key):
        return
    
    def search_dr(self, key):
        return
    
    def end_coordinates(self, direction, length):
        # calculate vector based on direction
        return
