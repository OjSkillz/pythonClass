from unittest import TestCase
import functionprimenumbers

class TestFunctionPrimeNumbers(TestCase):
    def test_that_function_prime_numbers_exists(self):
        functionprimenumbers.check_prime_status(7)
    
    def test_that_function_prime_numbers_returns_correct_value(self):
        actual = functionprimenumbers.check_prime_status(7)
        self.assertEqual(actual, True)
        actual = functionprimenumbers.check_prime_status(6)
        self.assertEqual(actual, False)
