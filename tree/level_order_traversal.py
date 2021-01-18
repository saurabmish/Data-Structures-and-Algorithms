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
