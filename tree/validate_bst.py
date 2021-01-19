'''Validate Whether a Given Binary Tree is a Binary Search Tree

Time Complexity: O(n)
'''

from .node import BinaryNode

def validate_bst(root):
    stack = list()
    sequence = []
    current = root
    previous = None
    while stack or current:
        if current:
            stack.append(current)
            current = current.left
        else:
            current = stack.pop()
            if previous != None and current.key <= previous.key:
                return False
            previous = root
            current = current.right

    return True
