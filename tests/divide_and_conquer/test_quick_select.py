import unittest

from divide_and_conquer.quick_select import select

class TestQuickSelect(unittest.TestCase):

    def setUp(self):
        self.arr1 = [3, 2, 1, 5, 6, 4]
        self.arr2 = [9, 6, 4, 2, 1]
        self.arr3 = [-9, 12, 7, -4, 0]
        self.arr4 = [-1, -3, -8, -21, -4, -9, -2]

    def test_random_positive_array(self):
        self.assertEqual(select(self.arr1, 0, len(self.arr1)-1, 4), 4)

    def test_decreasing_positive_array(self):
        self.assertEqual(select(self.arr2, 0, len(self.arr2)-1, 5), 9)

    def test_random_mixed_array(self):
        self.assertEqual(select(self.arr3, 0, len(self.arr3)-1, 3), 0)

    def test_random_negative_array(self):
        self.assertEqual(select(self.arr4, 0, len(self.arr4)-1, 1), -21)
