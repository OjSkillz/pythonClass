from unittest import TestCase
import functionsubtract

class TestFunctionSubtract(TestCase):
    def test_that_function_subtract_exists(self):
        functionsubtract.subtract(5, 7)
    
    def test_that_function_subtract_returns_correct_value(self):
        actual = functionsubtract.subtract(5, 7)
        expected = 2
        self.assertEqual(actual, expected)
    
 
