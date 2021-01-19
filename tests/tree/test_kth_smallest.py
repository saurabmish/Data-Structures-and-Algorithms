import unittest

from tree.node import BinaryNode
from tree.kth_smallest import kth_smallest

class TestKthSmallest(unittest.TestCase):

    def setUp(self):
        """Valid binary search tree."""
        self.root = BinaryNode(18)
        self.root.left  = BinaryNode(15)
        self.root.right = BinaryNode(20)
        self.root.left.left  = BinaryNode(9)
        self.root.left.right = BinaryNode(17)

    def test_smallest_value(self):
        self.assertEqual(kth_smallest(self.root, 1), 9)

    def test_second_smallest_value(self):
        self.assertEqual(kth_smallest(self.root, 2), 15)

    def test_third_smallest_value(self):
        self.assertEqual(kth_smallest(self.root, 3), 17)

    def test_fourth_smallest_value(self):   # second largest value
        self.assertEqual(kth_smallest(self.root, 4), 18)

    def test_fifth_smallest_value(self):    # largest value
        self.assertEqual(kth_smallest(self.root, 5), 20)

    def test_k_more_than_nodes(self):
        self.assertEqual(kth_smallest(self.root, 6), -1)
