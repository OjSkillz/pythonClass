from unittest import TestCase
import functionextractdigits

class TestFunctionExtractDigits(TestCase):
    def test_that_function_extract_digits_exists(self):
        functionextractdigits.extract_digits(2342)
    
    def test_that_function_extract_digits_returns_correct_value(self):
        actual = functionextractdigits.extract_digits(2342)
        expected = [2,3,4,2]
        self.assertEqual(actual, expected)
