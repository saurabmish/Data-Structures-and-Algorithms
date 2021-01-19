import unittest

from tree.node import BinaryNode
from tree.validate_bst import validate_bst

class TestValidateBST(unittest.TestCase):

    def test_small_valid_bst(self):
        """Binary Tree

                    2
                   / \
                  1   5
        """
        self.root = BinaryNode(2)
        self.root.left = BinaryNode(1)
        self.root.right = BinaryNode(5)

        self.assertTrue(validate_bst(self.root))


    def test_large_valid_bst(self):
        """Binary Tree

                      8
                     / \
                    /   \
                   /     \
                  6      10
                 / \     / \
                3   7   9   12
        """
        self.root = BinaryNode(8)
        self.root.left = BinaryNode(6)
        self.root.right = BinaryNode(10)
        self.root.left.left = BinaryNode(3)
        self.root.left.right = BinaryNode(7)
        self.root.right.left = BinaryNode(9)
        self.root.right.right = BinaryNode(12)

        self.assertTrue(validate_bst(self.root))


    def test_invalid_bst(self):
        """Binary Tree

                      5
                     / \
                    /   \
                   /     \
                  1       4
                         / \
                        3   6
        """
        self.root = BinaryNode(5)
        self.root.left = BinaryNode(1)
        self.root.right = BinaryNode(4)
        self.root.right.left = BinaryNode(3)
        self.root.right.right = BinaryNode(6)

        self.assertFalse(validate_bst(self.root))
