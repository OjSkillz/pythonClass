from unittest import TestCase
import functionsquareof

class TestFunctionSquareOf(TestCase):
    def test_that_function_square_of_exists(self):
        functionsquareof.square_of(5)
        
    def test_that_function_square_of_returns_correct_value(self):
        actual = functionsquareof.square_of(5)
        expected = 25
        self.assertEqual(actual, expected)
