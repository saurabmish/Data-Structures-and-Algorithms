import unittest

from tree.node import BinaryNode
from tree.lowest_common_ancestor import lca

class TestLowestCommonAncestor(unittest.TestCase):

    def setUp(self):
        """Binary Tree

                          30
                         /  \
                        /    \
                       /      \
                      11      29
                     /  \    /  \
                    8   12  25  14
        """
        self.root = BinaryNode(30)
        self.root.left  = BinaryNode(11)
        self.root.right = BinaryNode(29)
        self.root.left.left  = BinaryNode(8)
        self.root.left.right = BinaryNode(12)
        self.root.right.left  = BinaryNode(25)
        self.root.right.right = BinaryNode(14)

    def test_same_branch_ancestor(self):
        """Both nodes (8 and 12) belong to the same subtree."""
        self.assertEqual(11,
            lca(self.root, self.root.left.left, self.root.left.right))

    def test_different_branch_ancestor(self):
        """Both nodes (8, 14) belong to different subtrees."""
        self.assertEqual(30,
            lca(self.root, self.root.left.left, self.root.right.right))

    def test_node1_isparent_node2(self):
        """
        If one of the node's is the parent of the other, it is also their
        lowest common ancestor, i.e., lca(8, 11) = 11.
        """
        self.assertEqual(11,
            lca(self.root, self.root.left.left, self.root.left))
