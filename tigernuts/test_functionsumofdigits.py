from unittest import TestCase
import functionsumofdigits

class TestFunctionSumOfDigits(TestCase):
    def test_that_fuction_sum_of_digits_exists(self):
        functionsumofdigits.sum_digits(15324)
        
    def test_that_function_sum_of_digits_returns_correct_value(self):
        actual = functionsumofdigits.sum_digits(153241)
        expected = 16
        self.assertEqual(actual, expected)
