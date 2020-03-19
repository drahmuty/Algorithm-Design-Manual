"""
For best-fit scenario:
- Each bucket is a node on the tree. 
- For each new item, find the maximum node that can hold the new item. This takes O(n log n) time worst case.
- Add the new item to that node and update the total value of the node.
- Rebalance the tree.
- Return the total number of nodes as the final step. This takes O(n) time.

For worst-fit scenario:
- For each new item, find the minimum node that can hold the new item. This takes O(n log n) time worst case.
- Add the new item to that node and update the total value of the node.
- Rebalance the tree.
- Return the total number of nodes as the final step. This takes O(n) time.
"""

def main(items, tree, total):
    for item in items:
        bestfit(item, tree, total)
    countnodes(tree)

def bestfit(item, tree, total):
    max = total - item
    while tree.value <= max:
        if tree.right is None:
            tree.value = tree.value + item
            break
        tree = tree.right
        
def worstfit(item, tree, total):
    while tree.left is not None:
        tree = tree.left
    if tree.value + item <= total:
        tree.value = tree.value + item
    else:
        tree.left = Tree(item)
