"""
4-18. Suppose an array A consists of n elements, each of which is red, white, or blue. 
We seek to sort the elements so that all the reds come before all the whites, which 
come before all the blues The only operation permitted on the keys are

Examine(A,i) -- report the color of the ith element of A.
Swap(A,i,j) -- swap the ith element of A with the jth element.
Find a correct and efficient algorithm for red-white-blue sorting. There is a 
linear-time solution. This is also known as the Dutch national flag problem. 
The simplest linear time solution performs two passes of the partition operation 
from Quicksort. The first pass treats the red and white elements as indistinguishable, 
and separates them from the blue. The second pass is just separates the elements within 
the red/white sub-array.
"""



# Sort colors using Quicksort-style partition.
def sort_colors(A, color_order_list):
    max_index = len(A)
    while len(color_order_list) > 1:
        last_color = color_order_list.pop()
        max_index = sort_colors_helper(A, last_color, max_index)
    print(A)

# Helper function. Moves last color items to end of list and returns index of its first occurence.
def sort_colors_helper(A, last_color, max_index):
    i = j = 0
    for i in range(max_index):
        if A[i] != last_color:
            temp = A[i]
            A[i] = A[j]
            A[j] = temp
            j += 1
    return j

A = ['blue', 'green', 'red', 'white', 'white', 'red', 'blue', 'green', 'blue', 'red', 'red', 'white']

sort_colors(A, ['red', 'white', 'blue', 'green'])
