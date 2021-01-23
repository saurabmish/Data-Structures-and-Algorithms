import unittest

from dynamic_programming.maximum_sum_subarray import maximum_sum_subarray

class TestMaximumSubarray(unittest.TestCase):

    def setUp(self):
        self.positive_array = [22, 10, 34, 33, 56, 90, 66]
        self.negative_array = [-13, -3, -25, -20, -3, -16, -23, -12, -22, -15, -4]
        self.mixed_array = [904, 40, 523, 12, -335, -124, 690, -31]
        self.zero_array = [0, 0, 0, 0, 0]

    def test_positive_array(self):
        self.assertGreaterEqual(maximum_sum_subarray(self.positive_array), 1)

    def test_negative_array(self):
        self.assertLessEqual(maximum_sum_subarray(self.negative_array), -1)

    def test_mixed_array(self):
        self.assertGreater(maximum_sum_subarray(self.mixed_array), 0)

    def test_all_zeroes(self):
        self.assertEqual(maximum_sum_subarray(self.zero_array), 0)
