import unittest

from dynamic_programming.longest_increasing_subsequence import \
longest_increasing_subsequence

class TestLongestNonDecreasingSubsequence(unittest.TestCase):

    def setUp(self):
        self.sequence1 = [2, 3, 4, 78, 90]
        self.sequence2 = [90, 81, 67, 11, 10, 7, 1]
        self.sequence3 = [0, 1, 0, 3, 2, 3]
        self.sequence4 = [10, 9, 2, 5, 3, 7, 101, 18]
        self.sequence5 = [0, 8, 4, 12, 2, 10, 6, 14, 1, 9]
        self.sequence6 = [7, 7, 7, 7]

    def test_increasing_sequence(self):
        self.assertEqual(longest_increasing_subsequence(self.sequence1),
                         len(self.sequence1))

    def test_decreasing_sequence(self):
        self.assertEqual(longest_increasing_subsequence(self.sequence2), 1)

    def test_short_random_sequence(self):
        self.assertEqual(longest_increasing_subsequence(self.sequence3), 4)

    def test_medium_random_sequence(self):
        self.assertEqual(longest_increasing_subsequence(self.sequence4), 4)

    def test_long_random_sequence(self):
        self.assertEqual(longest_increasing_subsequence(self.sequence5), 4)

    def test_repeating_sequence(self):
        self.assertEqual(longest_increasing_subsequence(self.sequence6), 1)

    def test_empty_sequence_error_type(self):
        self.assertRaises(ValueError, longest_increasing_subsequence, [])

    def test_empty_sequence_error_message(self):
        with self.assertRaises(ValueError) as context:
            longest_increasing_subsequence([])
        self.assertIn("Input sequence not provided", str(context.exception))
