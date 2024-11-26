from unittest import TestCase
import functionissquare

class TestFunctionIsSquare(TestCase):
    def test_that_function_is_square_exists(self):
        functionissquare.is_square(10)
    
    def test_that_function_is_square_returns_correct_value_with_square_input(self):
        actual = functionissquare.is_square(25)
        expected = True
        self.assertEqual(actual, expected)
    
    def test_that_function_is_square_returns_correct_value_with_non_square_input(self):
        actual = functionissquare.is_square(10)
        expected = False
        self.assertEqual(actual, expected)
