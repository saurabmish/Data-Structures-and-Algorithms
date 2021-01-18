'''Post Order Traversal

The search tree is deepened as much as possible on each node before
visiting the next node. This is similar to a depth first search in a
graph.

Traversal can be done iteratively by using a stack. NOTE that to have
the right node processed first, push the left node first as stack is
a LIFO data structure.

Time Complexity:  O(n)
Space Complexity: O(n)

NOTE: Deques have O(1) speed for appendleft() and popleft() while
lists have O(n) performance for insert(0, value) and pop(0).
'''

from collections import deque
from .node import BinaryNode

def post_order_traversal(root):
    """Order of processing nodes:

    1. Left subtree recursively
    2. Right subtree recursively
    3. Root
    """
    stack = list()
    stack.append(root)
    sequence = deque()
    while stack:
        current = stack.pop()
        sequence.appendleft(current.key)
        if current.left:
            stack.append(current.left)
        if current.right:
            stack.append(current.right)

    return list(sequence)   # convert deque object to regular list
