'''Pre Order Traversal

The search tree is deepened as much as possible on each node before
visiting the next node. This is similar to a depth first search in a
graph.

Traversal can be done iteratively by using a stack. NOTE that to have
the left node processed first, push the right node first as stack is
a LIFO data structure.

Time Complexity:  O(n)
Space Complexity: O(n)
'''

from .node import BinaryNode

def pre_order_traversal(root):
    """Order of processing nodes:

    1. Root
    2. Left subtree recursively
    3. Right subtree recursively
    """
    stack = list()
    stack.append(root)
    sequence = []
    while stack:
        current = stack.pop()
        sequence.append(current.key)        # print(current.data, end='\n')
        if current.right:
            stack.append(current.right)
        if current.left:
            stack.append(current.left)

    return sequence
