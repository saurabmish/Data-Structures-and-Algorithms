'''K-th Smallest Element in Binary Search Tree

Time Complexity: O(n)
'''
from .node import BinaryNode

def kth_smallest(root, k):
    stack = list()
    current = root
    while stack or current:
        if current:
            stack.append(current)
            current = current.left
        else:
            current = stack.pop()
            k -= 1
            if k == 0:
                return current.key
            current = current.right

    return -1
