from unittest import TestCase
import functionfactorial

class TestFunctionFactorial(TestCase):
    def test_that_function_factorial_exists(self):
        functionfactorial.get_factorial(5)
        
    def test_that_function_factorial_returns_correct_value(self):
        actual = functionfactorial.get_factorial(5)
        expected = 120
        self.assertEqual(actual, expected)
