from unittest import TestCase
import functionfactorialof

class TestFunctionFactorialOf(TestCase):
    def test_that_function_factorial_of_exists(self):
        functionfactorialof.factorial_of(5)
        
    def test_that_function_factorial_of_returns_correct_value(self):
        actual = functionfactorialof.factorial_of(5)
        expected = 120
        self.assertEqual(actual, expected)
