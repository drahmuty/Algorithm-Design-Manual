"""Minimize bookcase height with n books of variable height and width and max shelf width."""

def bookshelves(books, width):
    
    B = [None] + books
    n = len(B)
    C = [float('inf')] * n
    C[0] = 0
    
    # Evaluate all books.
    for i in range(1, n):
        j = i
        h = 0
        w = 0
        
        # Find optimal solution for current and preceding books.
        while j > 0:
            
            # Make sure current book fits within shelf width.
            w += B[j][0]
            if w > width:
                break
            
            # Update shelf height if current book is bigger.
            h = max(h, B[j][1])
            
            # Choose arrangement that minimized overall bookcase height.
            C[i] = min(C[i], C[j-1] + h)
            
            # Move on to next book.
            j -= 1
            
    print(C)

    
# Test case.
books = [[1,2], [1,1], [1,1], [1,2], [1,2]]
width = 2
bookshelves(books, width)



# Found solution: https://h1ros.github.io/posts/coding/1105-filling-bookcase-shelves-dynamic-programming/
