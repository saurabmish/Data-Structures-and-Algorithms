'''Level Order Traversal

Nodes are processed in increasing order of their level (1, 2, ...) and
from left to right.
This is similar to breadth first search in a graph.

Time Complexity:  O(n)
Space Complexity: O(n)
'''

from collections import deque
from .node import BinaryNode

def level_order_traversal(root):
    """
    For each node in the queue, process nodes in the following order:
    1. Root
    2. Left
    3. Right
    """
    queue = deque()
    queue.append(root)
    sequence = []
    while queue:
        current = queue.popleft()
        sequence.append(current.key)    # print(current.data, end='\n')
        if current.left:
            queue.append(current.left)
        if current.right:
            queue.append(current.right)

    return sequence
