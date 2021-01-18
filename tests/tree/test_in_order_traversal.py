import unittest

from tree.node import BinaryNode
from tree.in_order_traversal import in_order_traversal

class TestPreOrderTraversal(unittest.TestCase):

    def test_strict_binary_tree(self):
        """Strict Binary Tree

        Each node has exactly 0 or 2 children.

                                  18
                                 /  \
                                /    \
                               /      \
                              15      20
                             /  \
                            40  50
        """
        self.root = BinaryNode(18)
        self.root.left  = BinaryNode(15)
        self.root.right = BinaryNode(20)
        self.root.left.left  = BinaryNode(40)
        self.root.left.right = BinaryNode(50)

        self.assertEqual(in_order_traversal(self.root),
                         [40, 15, 50, 18, 20])


    def test_full_binary_tree(self):
        """Full (Perfect) Binary Tree

        Each node has exactly 0 or 2 children and all leaf nodes are on
        the same level.

                                  18
                                 /  \
                                /    \
                               /      \
                              15      20
                             /  \    /  \
                            40  50  16  25
        """
        self.root = BinaryNode(18)
        self.root.left  = BinaryNode(15)
        self.root.right = BinaryNode(20)
        self.root.left.left  = BinaryNode(40)
        self.root.left.right = BinaryNode(50)
        self.root.right.left  = BinaryNode(16)
        self.root.right.right = BinaryNode(25)

        self.assertEqual(in_order_traversal(self.root),
                         [40, 15, 50, 18, 16, 20, 25])


    def test_complete_binary_tree(self):
        """Complete Binary Tree

        All levels are completely filled except the last level, which
        has all keys as left as possible.

                                  18
                                 /  \
                                /    \
                               /      \
                              15      20
                             /  \    /  \
                            40   50 16  25
                           /  \  /
                          8   7 1
        """
        self.root = BinaryNode(18)
        self.root.left  = BinaryNode(15)
        self.root.right = BinaryNode(20)
        self.root.left.left  = BinaryNode(40)
        self.root.left.right = BinaryNode(50)
        self.root.right.left  = BinaryNode(16)
        self.root.right.right = BinaryNode(25)
        self.root.left.left.left = BinaryNode(8)
        self.root.left.left.right = BinaryNode(7)
        self.root.left.right.left = BinaryNode(1)

        self.assertEqual(in_order_traversal(self.root),
                         [8, 40, 7, 15, 1, 50, 18, 16, 20, 25])
