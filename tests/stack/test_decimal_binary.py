import unittest

from stack.decimal_to_binary import decimal_to_binary

class TestDecimalToBinary(unittest.TestCase):

    def test_zero(self):
        self.assertEqual(decimal_to_binary(0), '')

    def test_one(self):
        self.assertEqual(decimal_to_binary(1), bin(1).replace("0b", ""))

    def test_single_digit(self):
        self.assertEqual(decimal_to_binary(9), bin(9).replace("0b", ""))

    def test_double_digit(self):
        self.assertEqual(decimal_to_binary(17), bin(17).replace("0b", ""))

    def test_three_digit(self):
        self.assertEqual(decimal_to_binary(129), bin(129).replace("0b", ""))
