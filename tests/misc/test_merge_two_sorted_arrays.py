import unittest

from misc.merge_two_sorted_arrays import merge_sorted_arrays

class TestMergeTwoSortedArrays(unittest.TestCase):

    def setUp(self):
        self.arr1 = [1, 2, 3, 5, 7]
        self.arr2 = [9, 10, 20, 21, 22]
        self.arr3 = [4, 6, 8]
        self.arr4 = [2, 5, 9, 13, 23, 45, 90]
        self.arr5 = [6, 8, 9]

    def test_equal_length_unique_arrays(self):
        self.assertEqual(merge_sorted_arrays(self.arr1, self.arr2),
                         [1, 2, 3, 5, 7, 9, 10, 20, 21, 22])

    def test_unequal_length_unique_arrays(self):
        self.assertEqual(merge_sorted_arrays(self.arr1, self.arr3),
                         [1, 2, 3, 4, 5, 6, 7, 8])

    def test_equal_length_duplicates(self):
        self.assertEqual(merge_sorted_arrays(self.arr3, self.arr5),
                         [4, 6, 6, 8, 8, 9])

    def test_unequal_length_duplicates(self):
        self.assertEqual(merge_sorted_arrays(self.arr1, self.arr4),
                         [1, 2, 2, 3, 5, 5, 7, 9, 13, 23, 45, 90])

    def test_one_array_none(self):
        self.assertEqual(merge_sorted_arrays(self.arr5, []), self.arr5)

    def test_both_arrays_none(self):
        self.assertEqual(merge_sorted_arrays([], []), [])
