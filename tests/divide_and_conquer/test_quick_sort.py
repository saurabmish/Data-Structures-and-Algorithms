import unittest

from divide_and_conquer.quick_sort import quicksort

class TestQuickSort(unittest.TestCase):

    def setUp(self):
        self.arr1 = [-2, 0, 32, 1, 56, 99, -4]
        self.arr2 = [-4, -1, 1, 4, 7, 9]
        self.arr3 = [90, 87, 32, 21, 8, 4, -1]
        self.arr4 = [5, 1, 1, 9, 7, 7, 14, 2, 34, 1, 21]
        self.arr5 = [123, 1, 23, 56, 43, 7, 4]
        self.arr6 = [123, 1, 23, 56, 43, 194, 4, 195]
        self.arr7 = [1, 234, 78, 5, 90]
        self.arr8 = [234, 78, 5, 90, 2]
        self.arr9 = [5, 5, 5, 5]
        self.arr10 = [0, -21, 4, 8.2, 5, 4.9, 7, 88.1, 12, 0, -9]

    def test_random_integers(self):
        self.assertEqual(quicksort(self.arr1, 0, len(self.arr1)-1),
                         sorted(self.arr1))

    def test_increasing_sequence(self):
        self.assertEqual(quicksort(self.arr2, 0, len(self.arr2)-1),
                         self.arr2)

    def test_decreasing_sequence(self):
        self.assertEqual(quicksort(self.arr3, 0, len(self.arr3)-1),
                         sorted(self.arr3))


    def test_duplicates(self):
        self.assertEqual(quicksort(self.arr4, 0, len(self.arr4)-1),
                         sorted(self.arr4))

    def test_largest_beginning(self):
        self.assertEqual(quicksort(self.arr5, 0, len(self.arr5)-1),
                         sorted(self.arr5))

    def test_largest_end(self):
        self.assertEqual(quicksort(self.arr6, 0, len(self.arr6)-1),
                         sorted(self.arr6))

    def test_smallest_beginning(self):
        self.assertEqual(quicksort(self.arr7, 0, len(self.arr7)-1),
                         sorted(self.arr7))

    def test_smallest_end(self):
        self.assertEqual(quicksort(self.arr8, 0, len(self.arr8)-1),
                         sorted(self.arr8))

    def test_all_same(self):
        self.assertEqual(quicksort(self.arr9, 0, len(self.arr9)-1),
                         sorted(self.arr9))

    def test_all_variety(self):
        self.assertEqual(quicksort(self.arr10, 0, len(self.arr10)-1),
                         sorted(self.arr10))
