from unittest import TestCase
import functiondivide

class TestFunctionDivide(TestCase):
    def test_that_function_divide_exists(self):
        functiondivide.divide(4, 5)
        
    def test_that_function_divide_returns_correct_value(self):            
        actual = functiondivide.divide(4, 5)
        expected = 1
        self.assertEqual(actual, expected)
    
    def test_that_function_subtract_returns_correct_value_with_second_input_zero(self):
        actual = functiondivide.divide(4, 0)
        expected = 0
        self.assertEqual(actual, expected)
