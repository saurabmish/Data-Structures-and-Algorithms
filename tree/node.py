''' Structure of Node

            key
            / \
           /   \
        left  right
'''

class BinaryNode:

    def __init__(self, key=None, left=None, right=None):
        self.key = key
        self.left = left
        self.right = right
