'''In Order Traversal

The search tree is deepened as much as possible on each node before
visiting the next node. This is similar to a depth first search in a
graph.

Time Complexity:  O(n)
Space Complexity: O(n)
'''

from .node import BinaryNode

def in_order_traversal(root):
    """Order of processing nodes:

    1. Left subtree recursively
    2. Root
    3. Right subtree recursively
    """
    stack = list()
    sequence = []
    current = root
    while stack or current:
        if current:
            stack.append(current)
            current = current.left
        else:
            current = stack.pop()
            sequence.append(current.key)
            current = current.right

    return sequence
