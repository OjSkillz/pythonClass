from unittest import TestCase
import functionisprimenumber

class TestFunctionIsPrimeNumber(TestCase):
    def test_that_function_is_even_exists(self):
        functionisprimenumber.is_prime_number(4)
    
    def test_that_function_is_even_returns_correct_value(self):
        self.assertEqual(functionisprimenumber.is_prime_number(4), False)
        self.assertEqual(functionisprimenumber.is_prime_number(2), True)
        
