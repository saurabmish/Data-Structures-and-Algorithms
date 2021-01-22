import unittest

from divide_and_conquer.karatsuba_multiplication import karatsuba

class TestKaratsubaMultiplication(unittest.TestCase):

    def test_small_positives(self):
        self.assertEqual(karatsuba(1, 3), (1 * 3))

    def test_medium_positives(self):
        self.assertEqual(karatsuba(1234, 5678), (1234 * 5678))

    def test_large_positives(self):
        self.assertEqual(karatsuba(3141592653589793238, 462643383279502884),
                        (3141592653589793238 * 462643383279502884))

    def test_negative_positive(self):
        self.assertEqual(karatsuba(-9, 12), (-9 * 12))

    def test_positive_negative(self):
        self.assertEqual(karatsuba(5, -14), (5 * -14))

    def test_both_negatives(self):
        self.assertEqual(karatsuba(-2, -98), 196)

    def test_one_zero(self):
        self.assertEqual(karatsuba(5, 0), 0)

    def test_both_zeroes(self):
        self.assertEqual(karatsuba(0, 0), 0)
