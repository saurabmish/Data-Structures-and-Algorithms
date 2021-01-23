import unittest

from stack.postfix_evaluation import postfix_evaluation

class TestPostfixEvaluation(unittest.TestCase):

    def test_expression_1(self):
        self.assertEqual(postfix_evaluation("231*+9-"), str(-4))

    def test_expression_2(self):
        self.assertEqual(postfix_evaluation("456*+"), str(34))

    def test_expression_3(self):
        self.assertEqual(postfix_evaluation("45+72-*"), str(45))

    @unittest.expectedFailure
    def test_invalid_expression_1(self):
        self.assertEqual(postfix_evaluation("43"), "43",
                         "No operator present in expression")

    def test_invalid_expression_2(self):
        """Extra operators."""
        with self.assertRaises(IndexError):
            postfix_evaluation("23+-*")
