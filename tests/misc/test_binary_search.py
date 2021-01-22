'''
Binary search works only on sequences sorted in increasing order.
'''

import unittest

from misc.binary_search import binary_search

class TestBinarySearch(unittest.TestCase):

    def setUp(self):
        self.arr1 = [2, 4, 8, 9, 12, 14, 17, 19, 22, 25, 27, 28]
        self.arr2 = [-10, -8, -7, -3, -1]
        self.arr3 = [-90, -23, -11, -2, 0, 32, 56, 69, 78]
        self.arr4 = [-11, -2, 5, 7, 7, 9, 14, 14, 34]
        self.arr5 = [2, 2, 2, 2, 2]

    def test_positive_sequence_present(self):
        self.assertTrue(binary_search(self.arr1, 22, 0, len(self.arr1)-1))

    def test_positive_sequence_not_present(self):
        self.assertFalse(binary_search(self.arr1, 23, 0, len(self.arr1)-1))

    def test_negative_sequence_present(self):
        self.assertTrue(binary_search(self.arr2, -7, 0, len(self.arr2)-1))

    def test_negative_sequence_not_present(self):
        self.assertFalse(binary_search(self.arr2, -6, 0, len(self.arr2)-1))

    def test_mixed_sequence_present(self):
        self.assertTrue(binary_search(self.arr3, 69, 0, len(self.arr3)-1))

    def test_mixed_sequence_not_present(self):
        self.assertFalse(binary_search(self.arr3, -89, 0, len(self.arr3)-1))

    def test_present_in_duplicates(self):
        self.assertTrue(binary_search(self.arr4, 14, 0, len(self.arr4)-1))

    def test_not_present_in_duplicates(self):
        self.assertFalse(binary_search(self.arr4, 6, 0, len(self.arr4)-1))

    def test_present_in_same_elements(self):
        self.assertTrue(binary_search(self.arr5, 2, 0, len(self.arr5)-1))

    def test_not_present_in_same_elements(self):
        self.assertFalse(binary_search(self.arr5, 1, 0, len(self.arr5)-1))
